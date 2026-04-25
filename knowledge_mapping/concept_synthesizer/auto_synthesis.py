#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto Synthesis — Integrates LLM-backed synthesis into protocol.py

This module extends the existing Synthesizer protocol with automatic
synthesis capability for unknown concepts.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
from pathlib import Path
from typing import Dict, Any, Optional

class AutoSynthesisExtension:
    """
    Extension for protocol.py that adds automatic synthesis.

    When a concept is not in the validated cache, this generates
    a synthesis prompt and can invoke Claude Code to synthesize it.
    """

    def __init__(self, base_synthesizer):
        """
        Initialize with base synthesizer instance.

        Args:
            base_synthesizer: ConceptSynthesizerProtocol instance
        """
        self.base = base_synthesizer
        self.nano_kernel = self._load_nano_kernel()

    def _load_nano_kernel(self) -> str:
        """Load EAR Nano Kernel."""
        kernel_path = Path(__file__).parent.parent.parent.parent.parent / \
                      "LA_BIBLIOTECA_DI_ALESSANDRIA/AILA/AILA_MINI/EAR_NANO_KERNEL_AILA_v1_0.md"

        if kernel_path.exists():
            return kernel_path.read_text(encoding='utf-8')
        else:
            return "# EAR Nano Kernel (not loaded)"

    def synthesize_with_auto(self, concept_name: str,
                            use_claude_code: bool = True) -> Dict[str, Any]:
        """
        Synthesize concept with automatic fallback.

        Flow:
        1. Try cache (fast path)
        2. If not in cache and use_claude_code=True:
           - Generate prompt
           - Return prompt for manual/automatic synthesis
        3. Otherwise return unknown

        Args:
            concept_name: Concept to synthesize
            use_claude_code: Whether to enable automatic synthesis

        Returns:
            Synthesis result or prompt for synthesis
        """
        # Try base synthesizer first (cache lookup)
        concept_key = concept_name.lower()

        # Check if in validated knowledge base
        if hasattr(self.base, 'knowledge') and concept_key in self.base.knowledge:
            return self.base.synthesize_concept(concept_name)

        # Not in cache — need synthesis
        if use_claude_code:
            return self._generate_auto_synthesis(concept_name)
        else:
            # Return unknown
            return {
                'status': 'unknown',
                'concept_name': concept_name,
                'message': 'Concept not in validated cache'
            }

    def _generate_auto_synthesis(self, concept_name: str) -> Dict[str, Any]:
        """
        Generate synthesis prompt for Claude Code to execute.

        Returns a structured result that can be:
        1. Executed automatically (if Claude Code is available)
        2. Shown to user for manual synthesis
        3. Cached for future use
        """
        prompt = self._build_synthesis_prompt(concept_name)

        return {
            'status': 'needs_synthesis',
            'concept_name': concept_name,
            'synthesis_prompt': prompt,
            'instruction': (
                f"Please synthesize '{concept_name}' using the prompt below. "
                f"Return JSON following the exact format specified."
            ),
            'auto_synthesis_ready': True
        }

    def _build_synthesis_prompt(self, concept_name: str) -> str:
        """Build synthesis prompt with Nano Kernel + few-shot."""
        few_shot = self._get_few_shot_examples()

        prompt = f"""You are an ontological analyzer using the EAR framework.

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

{few_shot}

---

# YOUR TASK

Analyze: **{concept_name}**

Provide ontological synthesis following this EXACT JSON format:

```json
{{
  "concept_type": "theorem | law | theory | principle | threshold",
  "formal_statement": "concise formal statement",
  "ontological_structures": [
    {{"pattern": "Δ|⇄|⟳", "evidence": "why present", "primary": true|false}}
  ],
  "dimension_hints": "D=1|2|3|4 with justification",
  "attribute_dominant": "Δ|⇄|⟳",
  "complexity": "foundational (1) | recursive (2) | synthetic (3)",
  "elimination_test": "explicit reasoning for all three attributes",
  "related": ["concept1", "concept2"]
}}
```

CRITICAL:
- Order ontological_structures with PRIMARY first
- Mark primary: true only for dominant attribute
- elimination_test must show reasoning for Δ, ⇄, and ⟳
- dimension_hints must have explicit D=N

Return ONLY the JSON."""

        return prompt

    def _get_few_shot_examples(self) -> str:
        """Get 3 validated examples for few-shot."""
        examples = []

        # Use 3 diverse examples from validated cache
        sample_concepts = [
            ('pythagorean theorem', 'Σ111₊'),
            ('fundamental theorem of calculus', 'Σ121₊'),
            ('maxwell\'s equations', 'Σ431₊')
        ]

        for name, sigma in sample_concepts:
            key = name.lower()
            if hasattr(self.base, 'knowledge') and key in self.base.knowledge:
                synthesis = self.base.knowledge[key]
                example = f"""
## {name.title()} → {sigma}

```json
{json.dumps(synthesis, indent=2, ensure_ascii=False)}
```
"""
                examples.append(example)

        return "\n".join(examples) if examples else "# No examples available"


def test_auto_synthesis():
    """Test auto synthesis extension."""
    from protocol import ConceptSynthesizerProtocol

    base_synth = ConceptSynthesizerProtocol()
    auto_synth = AutoSynthesisExtension(base_synth)

    # Test with unknown concept
    print("\nTesting auto synthesis with unknown concept...")
    result = auto_synth.synthesize_with_auto("Fermat's Last Theorem")

    if result.get('status') == 'needs_synthesis':
        print("\n[PROMPT GENERATED]")
        print("="*70)
        print(result['synthesis_prompt'][:500] + "...")
        print("="*70)
        print("\n✅ Auto synthesis ready")
    else:
        print(f"\nStatus: {result.get('status')}")


if __name__ == "__main__":
    test_auto_synthesis()
