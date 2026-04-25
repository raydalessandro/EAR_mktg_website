# Mapping Guide — Scientific Concepts to Tesseract

**Mission:** Map scibile umano (fisica/matematica) onto Matrix 72 (Tesseract)

---

## Strategy

### Input: Paper Concepts
From Paper Analyzer, you receive:
- Theorems (mathematical statements)
- Laws (physical principles)
- Definitions (formal concepts)
- Principles (fundamental rules)

### Output: Tesseract Nodes
Propose Σ coordinates for each concept

### Tools Available
1. **EAR Nano Kernel** — Σ structure, Δ⇄⟳ definitions
2. **GRAFO Tesseract** — 72 nodes, existing mappings
3. **Judge validation** — AILA completes ensures coherence

---

## Mapping Process

### 1. Analyze Concept Type

**Theorem** (mathematical)
→ Abstract, formal, provable
→ Likely dimensions 1-2 (point/line)
→ Likely Δ (distinction) dominant

**Law** (physical)
→ Empirical, measurable, universal
→ Likely dimensions 3-4 (organism/field)
→ May involve ⇄ (relation) or ⟳ (process)

**Principle** (fundamental)
→ Meta-level, foundational
→ Could span multiple dimensions
→ Often involves process (⟳)

### 2. Query GRAFO

Look for similar concepts already mapped:
```python
# Example: conservation laws
grafo = self.context_docs['GRAFO_GRAFO_MATRIX_72']
nodes = grafo['nodes']

# Find conservation-related nodes
for sigma, node in nodes.items():
    if 'conservation' in node.get('name', '').lower():
        print(f"{sigma}: {node['name']}")
```

### 3. Propose Σ Coordinate

Based on:
- **Dimension** (1=point, 2=line, 3=organism, 4=field)
- **Attribute** (1=Δ, 2=⇄, 3=⟳)
- **Complexity** (1=foundational, 2=intermediate, 3=complex)
- **Polarity** (+/-)

### 4. Provide Reasoning

Explain why concept maps to proposed Σ:
```
"Noether's Theorem → Σ₄₃₂₊
Reasoning:
- Dimension 4 (field): Connects symmetries to conservations at field level
- Attribute ⟳ (process): Describes temporal evolution
- Complexity 2: Intermediate (connects simpler concepts)
- Polarity +: Constructive (generates conservation laws)"
```

---

## Example Mappings

### Conservation Laws
- Energy conservation → Σ₄₃₁₊ (field-level process, foundational)
- Momentum conservation → Σ₄₃₁₊ (same structure)
- Angular momentum → Σ₄₃₂₊ (adds rotational complexity)

### Symmetries
- Time translation → Σ₂₃₁₊ (line-level process)
- Space translation → Σ₂₃₁₊ (same)
- Rotation → Σ₃₂₂₊ (organism-level relation)

### Fundamental Theorems
- Pythagorean Theorem → Σ₁₁₁₊ (point-level distinction, foundational)
- Calculus Fundamental Theorem → Σ₂₃₂₊ (line-level process, connects derivative/integral)

---

## Validation Checklist

Before proposing Σ, ask:

1. **Dimension correct?**
   - Is this point/line/organism/field level?

2. **Attribute correct?**
   - Is it about distinction (Δ), relation (⇄), or process (⟳)?

3. **Complexity appropriate?**
   - Foundational (1), intermediate (2), or complex (3)?

4. **Polarity makes sense?**
   - Constructive (+) or deconstructive (-)?

5. **GRAFO consistency?**
   - Do similar concepts live near this Σ?

---

## Iterating on Judge Feedback

If Judge returns **INVALID**:
1. Read concerns carefully
2. Adjust Σ based on ontological reasoning
3. Re-propose with refined rationale

If Judge returns **UNCERTAIN**:
1. Provide more context
2. Explain edge cases
3. Reference similar GRAFO nodes

---

## Building the Knowledge Graph

Each validated mapping adds a node to Tesseract:
- Node ID: Concept name
- Node Σ: Validated coordinate
- Edges: Relations to other concepts

Over time, we build a **comprehensive physics/math knowledge graph** grounded in EAR ontology.

---

**Goal:** Map all fundamental physics & mathematics onto Tesseract structure, creating a queryable ontological knowledge base.
