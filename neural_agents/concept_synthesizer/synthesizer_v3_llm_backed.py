#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Concept Synthesizer v3 — LLM-Backed with Claude

ARCHITECTURE:
- FAST PATH: Cache lookup for validated concepts (12 entries)
- SYNTHESIS PATH: LLM call for new concepts using Nano Kernel + few-shot
- Elimination test methodology embedded in prompt

This synthesizer truly SYNTHESIZES instead of just doing dictionary lookup.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
import traceback
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List

# Add shared to path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))

try:
    from file_sync import FileSync
except ImportError:
    class FileSync:
        def write_network_result(self, d): pass
        def wait_for_mapping(self, timeout=120): return {}


class ConceptSynthesizerV3:
    """
    Concept Synthesizer v3 — LLM-backed architecture.

    Uses validated concepts as cache + few-shot examples.
    For unknown concepts, generates synthesis using Claude + Nano Kernel.
    """

    def __init__(self, use_llm: bool = True, api_key: Optional[str] = None):
        """
        Initialize Synthesizer v3.

        Args:
            use_llm: Whether to use LLM for unknown concepts (vs returning error)
            api_key: Anthropic API key (optional, can use env var)
        """
        self.sync = FileSync()
        self.synthesis_history: List[Dict[str, Any]] = []
        self.use_llm = use_llm
        self.api_key = api_key or self._get_api_key()

        # Load context
        self.nano_kernel = self._load_nano_kernel()
        self.validated_cache = self._load_validated_cache()

        # LLM client (lazy init)
        self._client = None

    def _get_api_key(self) -> Optional[str]:
        """Get API key from environment."""
        import os
        return os.environ.get('ANTHROPIC_API_KEY')

    def _load_nano_kernel(self) -> str:
        """Load EAR Nano Kernel."""
        kernel_path = Path(__file__).parent.parent.parent.parent.parent / \
                      "LA_BIBLIOTECA_DI_ALESSANDRIA/AILA/AILA_MINI/EAR_NANO_KERNEL_AILA_v1_0.md"

        if kernel_path.exists():
            return kernel_path.read_text(encoding='utf-8')
        else:
            print(f"[WARN] Nano Kernel not found at {kernel_path}")
            return "# EAR Nano Kernel (not loaded)"

    def _load_validated_cache(self) -> Dict[str, Dict[str, Any]]:
        """
        Load validated concepts as cache.

        These 12 concepts serve dual purpose:
        1. Fast path for frequent concepts
        2. Few-shot examples for LLM synthesis
        """
        return {
            "pythagorean theorem": {
                'concept_type': 'theorem',
                'formal_statement': 'a² + b² = c² — defines the metric boundary in Euclidean geometry',
                'ontological_structures': [
                    {'pattern': 'Δ', 'evidence': 'PRIMARY — defines the boundary between right and non-right triangles', 'primary': True},
                    {'pattern': '⇄', 'evidence': 'Relates three sides structurally'},
                    {'pattern': '⟳', 'evidence': 'Minimal — static identity, no temporal process'}
                ],
                'dimension_hints': 'D=1 (point/foundational) — pure geometry, no spatial extension needed',
                'attribute_dominant': 'Δ',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove Δ (distinction a²+b²=c²) → nothing remains. Remove ⇄ → identity still there. Remove ⟳ → already minimal. Δ is essential.',
                'related': ['Euclidean geometry', 'Distance metrics']
            },

            "fundamental theorem of calculus": {
                'concept_type': 'theorem',
                'formal_statement': 'Differentiation and integration are inverse operations',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — theorem IS the bidirectional correspondence', 'primary': True},
                    {'pattern': '⟳', 'evidence': 'Process of accumulation vs rate of change'},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes local from global'}
                ],
                'dimension_hints': 'D=1 (foundational) — meta-principle of calculus',
                'attribute_dominant': '⇄',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⇄ → theorem vanishes. Remove Δ → correspondence still holds. Remove ⟳ → correspondence still static. ⇄ is essential.',
                'related': ['Leibniz', 'Newton', 'Analysis']
            },

            "maxwell's equations": {
                'concept_type': 'law',
                'formal_statement': 'Four equations governing electromagnetic field evolution',
                'ontological_structures': [
                    {'pattern': '⟳', 'evidence': 'PRIMARY — equations describe temporal evolution; without dynamics, no Maxwell', 'primary': True},
                    {'pattern': '⇄', 'evidence': 'E and B fields mutually generate'},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes sources from fields'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — spacetime field dynamics',
                'attribute_dominant': '⟳',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⟳ (propagation) → static fields, no waves, no light. Remove ⇄ → fields still propagate. Remove Δ → fields still propagate. ⟳ is essential.',
                'related': ['Electromagnetism', 'Light', 'Wave equation']
            },

            # Additional cache entries can be added here...
            # (keeping short for now, full 12 can be imported from protocol.py)
        }

    def synthesize_concept(self, concept_name: str) -> Dict[str, Any]:
        """
        Synthesize concept ontologically.

        FAST PATH: Check cache first.
        SYNTHESIS PATH: Use LLM + Nano Kernel if not in cache.

        Args:
            concept_name: Name of concept to synthesize

        Returns:
            Synthesis result with status
        """
        print(f"\n{'='*60}")
        print(f"CONCEPT SYNTHESIZER v3: Synthesizing {concept_name}")
        print(f"{'='*60}\n")

        concept_key = concept_name.lower()

        # FAST PATH: Cache lookup
        if concept_key in self.validated_cache:
            print(f"[CACHE HIT] Using validated synthesis")
            synthesis = self.validated_cache[concept_key]

            result = {
                'status': 'success',
                'source': 'cache',
                'concept_name': concept_name,
                'synthesis': synthesis,
                'synthesized_at': datetime.now().isoformat()
            }

            print(f"[SUCCESS] Synthesis complete (cached)")
            print(f"Type: {synthesis.get('concept_type', 'unknown')}")
            print(f"Dominant: {synthesis.get('attribute_dominant', 'unset')}")

            return result

        # SYNTHESIS PATH: LLM call
        if self.use_llm and self.api_key:
            print(f"[SYNTHESIS] Calling LLM for ontological analysis...")

            try:
                synthesis = self._synthesize_with_llm(concept_name)

                result = {
                    'status': 'success',
                    'source': 'llm',
                    'concept_name': concept_name,
                    'synthesis': synthesis,
                    'synthesized_at': datetime.now().isoformat()
                }

                print(f"[SUCCESS] Synthesis complete (LLM)")
                print(f"Type: {synthesis.get('concept_type', 'unknown')}")
                print(f"Dominant: {synthesis.get('attribute_dominant', 'unset')}")

                return result

            except Exception as e:
                print(f"[ERROR] LLM synthesis failed: {e}")
                # Fall through to prompt generation

        # FALLBACK: Generate prompt for manual synthesis
        print(f"[FALLBACK] Generating synthesis prompt...")
        prompt = self._generate_synthesis_prompt(concept_name)

        result = {
            'status': 'needs_synthesis',
            'source': 'prompt_generated',
            'concept_name': concept_name,
            'synthesis_prompt': prompt,
            'synthesized_at': datetime.now().isoformat(),
            'note': 'Use this prompt with Claude to synthesize the concept, then paste result back'
        }

        print(f"[PROMPT GENERATED] Copy prompt and use with Claude")

        return result

    def _synthesize_with_llm(self, concept_name: str) -> Dict[str, Any]:
        """
        Synthesize using Claude API.

        Sends Nano Kernel + few-shot examples + concept to Claude.
        Returns parsed JSON synthesis.
        """
        if not self._client:
            import anthropic
            self._client = anthropic.Anthropic(api_key=self.api_key)

        prompt = self._generate_synthesis_prompt(concept_name)

        message = self._client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Parse JSON from response
        response_text = message.content[0].text

        # Extract JSON (assuming Claude returns it in ```json blocks or directly)
        import re
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', response_text, re.DOTALL)
        if json_match:
            synthesis_json = json.loads(json_match.group(1))
        else:
            # Try parsing entire response
            synthesis_json = json.loads(response_text)

        return synthesis_json

    def _generate_synthesis_prompt(self, concept_name: str) -> str:
        """
        Generate prompt for ontological synthesis.

        Includes:
        - Nano Kernel
        - Few-shot examples (2-3 validated concepts)
        - Elimination test methodology
        - Output format
        """
        few_shot_examples = self._format_few_shot_examples()

        prompt = f"""You are an ontological analyzer using the EAR (Existence, Attribution, Resonance) framework.

# EAR NANO KERNEL

{self.nano_kernel}

---

# ELIMINATION TEST METHODOLOGY

For any concept, determine the dominant attribute by asking:
- Remove Δ (distinction) → does concept survive? If NO, Δ is dominant
- Remove ⇄ (relation) → does concept survive? If NO, ⇄ is dominant
- Remove ⟳ (process) → does concept survive? If NO, ⟳ is dominant

The attribute whose removal DESTROYS the concept is the PRIMARY attribute.

---

# FEW-SHOT EXAMPLES

{few_shot_examples}

---

# YOUR TASK

Analyze: **{concept_name}**

Provide ontological synthesis following this EXACT JSON format:

```json
{{
  "concept_type": "theorem | law | theory | principle | threshold",
  "formal_statement": "concise formal statement of the concept",
  "ontological_structures": [
    {{"pattern": "Δ|⇄|⟳", "evidence": "why this pattern is present", "primary": true|false}}
  ],
  "dimension_hints": "D=1|2|3|4 with brief justification",
  "attribute_dominant": "Δ|⇄|⟳",
  "complexity": "foundational (1) | recursive (2) | synthetic (3)",
  "elimination_test": "explicit reasoning: remove X → Y happens, therefore Z is dominant",
  "related": ["concept1", "concept2"]
}}
```

CRITICAL:
- Order ontological_structures with PRIMARY first
- Mark primary: true only for the dominant attribute
- elimination_test must show reasoning for all three attributes
- dimension_hints must have explicit D=N value

Return ONLY the JSON, no other text."""

        return prompt

    def _format_few_shot_examples(self) -> str:
        """Format 2-3 cache entries as few-shot examples."""
        examples = []

        for name, synthesis in list(self.validated_cache.items())[:3]:
            example = f"""
## {name.title()}

```json
{json.dumps(synthesis, indent=2, ensure_ascii=False)}
```
"""
            examples.append(example)

        return "\n".join(examples)

    def synthesize_and_report(self, concept_name: str) -> Dict[str, Any]:
        """Full pipeline: synthesize → report to Mapper."""
        result = self.synthesize_concept(concept_name)

        if result.get('status') == 'success':
            self.sync.write_network_result(result)
            print(f"[REPORTED] Synthesis sent to Mapper")

        return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Concept Synthesizer v3 — LLM-backed")
    parser.add_argument('--concept', type=str, help="Concept to synthesize")
    parser.add_argument('--prompt-only', action='store_true', help="Generate prompt without calling API")
    parser.add_argument('--api-key', type=str, help="Anthropic API key")

    args = parser.parse_args()

    if args.concept:
        use_llm = not args.prompt_only
        synthesizer = ConceptSynthesizerV3(use_llm=use_llm, api_key=args.api_key)

        result = synthesizer.synthesize_concept(args.concept)

        if result.get('status') == 'needs_synthesis':
            print("\n" + "="*70)
            print("SYNTHESIS PROMPT")
            print("="*70)
            print(result['synthesis_prompt'])
            print("="*70)
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("Usage:")
        print("  python synthesizer_v3_llm_backed.py --concept 'Euler Identity'")
        print("  python synthesizer_v3_llm_backed.py --concept 'Hooke Law' --prompt-only")
