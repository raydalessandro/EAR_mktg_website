"""
EAR Triangulation Engine — Universal LLM Adapter
Supports: DeepSeek, Claude (API), Ollama (local)
Switch provider with one config change.
"""

import os
import json
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class LLMResponse:
    text: str
    model: str
    tokens_in: int
    tokens_out: int
    latency_ms: int
    raw: Optional[dict] = None


class LLMProvider(ABC):
    """Base class for all LLM providers."""
    
    @abstractmethod
    def complete(self, system: str, user: str, temperature: float = 0.3) -> LLMResponse:
        pass
    
    @abstractmethod
    def name(self) -> str:
        pass


class DeepSeekProvider(LLMProvider):
    """DeepSeek API (OpenAI-compatible)."""
    
    def __init__(self, api_key: str = None, model: str = "deepseek-chat", base_url: str = "https://api.deepseek.com"):
        self.api_key = api_key or os.environ.get("DEEPSEEK_API_KEY", "")
        self.model = model
        self.base_url = base_url
    
    def complete(self, system: str, user: str, temperature: float = 0.3) -> LLMResponse:
        import requests
        t0 = time.time()
        
        resp = requests.post(
            f"{self.base_url}/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ],
                "temperature": temperature,
                "max_tokens": 2000
            },
            timeout=120
        )
        resp.raise_for_status()
        data = resp.json()
        
        return LLMResponse(
            text=data["choices"][0]["message"]["content"],
            model=self.model,
            tokens_in=data.get("usage", {}).get("prompt_tokens", 0),
            tokens_out=data.get("usage", {}).get("completion_tokens", 0),
            latency_ms=int((time.time() - t0) * 1000),
            raw=data
        )
    
    def name(self) -> str:
        return f"deepseek:{self.model}"


class ClaudeProvider(LLMProvider):
    """Anthropic Claude API."""
    
    def __init__(self, api_key: str = None, model: str = "claude-sonnet-4-20250514"):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        self.model = model
    
    def complete(self, system: str, user: str, temperature: float = 0.3) -> LLMResponse:
        import requests
        t0 = time.time()
        
        resp = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "Content-Type": "application/json"
            },
            json={
                "model": self.model,
                "max_tokens": 2000,
                "system": system,
                "messages": [
                    {"role": "user", "content": user}
                ],
                "temperature": temperature
            },
            timeout=120
        )
        resp.raise_for_status()
        data = resp.json()
        
        return LLMResponse(
            text=data["content"][0]["text"],
            model=self.model,
            tokens_in=data.get("usage", {}).get("input_tokens", 0),
            tokens_out=data.get("usage", {}).get("output_tokens", 0),
            latency_ms=int((time.time() - t0) * 1000),
            raw=data
        )
    
    def name(self) -> str:
        return f"claude:{self.model}"


class OllamaProvider(LLMProvider):
    """Ollama local models."""
    
    def __init__(self, model: str = "qwen2.5:3b", base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url
    
    def complete(self, system: str, user: str, temperature: float = 0.3) -> LLMResponse:
        import requests
        t0 = time.time()
        
        resp = requests.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ],
                "options": {"temperature": temperature},
                "stream": False
            },
            timeout=300
        )
        resp.raise_for_status()
        data = resp.json()
        
        return LLMResponse(
            text=data["message"]["content"],
            model=self.model,
            tokens_in=data.get("prompt_eval_count", 0),
            tokens_out=data.get("eval_count", 0),
            latency_ms=int((time.time() - t0) * 1000),
            raw=data
        )
    
    def name(self) -> str:
        return f"ollama:{self.model}"


class OpenAICompatibleProvider(LLMProvider):
    """Any OpenAI-compatible API (vLLM, LM Studio, Together, etc.)."""
    
    def __init__(self, api_key: str = "", model: str = "default", base_url: str = "http://localhost:8000"):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
    
    def complete(self, system: str, user: str, temperature: float = 0.3) -> LLMResponse:
        import requests
        t0 = time.time()
        
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        resp = requests.post(
            f"{self.base_url}/v1/chat/completions",
            headers=headers,
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ],
                "temperature": temperature,
                "max_tokens": 2000
            },
            timeout=300
        )
        resp.raise_for_status()
        data = resp.json()
        
        return LLMResponse(
            text=data["choices"][0]["message"]["content"],
            model=self.model,
            tokens_in=data.get("usage", {}).get("prompt_tokens", 0),
            tokens_out=data.get("usage", {}).get("completion_tokens", 0),
            latency_ms=int((time.time() - t0) * 1000),
            raw=data
        )
    
    def name(self) -> str:
        return f"openai-compat:{self.model}"


# --- Factory ---

PROVIDERS = {
    "deepseek": DeepSeekProvider,
    "claude": ClaudeProvider,
    "ollama": OllamaProvider,
    "openai": OpenAICompatibleProvider,
}

def create_provider(config: dict) -> LLMProvider:
    """
    Create provider from config dict.
    
    Examples:
        {"provider": "deepseek", "api_key": "sk-...", "model": "deepseek-chat"}
        {"provider": "claude", "api_key": "sk-ant-...", "model": "claude-sonnet-4-20250514"}
        {"provider": "ollama", "model": "qwen2.5:3b"}
        {"provider": "openai", "base_url": "http://localhost:8000", "model": "my-model"}
    """
    provider_name = config.pop("provider")
    cls = PROVIDERS.get(provider_name)
    if not cls:
        raise ValueError(f"Unknown provider: {provider_name}. Available: {list(PROVIDERS.keys())}")
    return cls(**config)
