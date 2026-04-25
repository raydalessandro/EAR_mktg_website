"""
EAR Triangulation Engine — Tribunal v2

Mechanical convergence checker. NO LLM involved.

Logic:
  - Synth output = REFERENCE
  - Compare each monodoc agent (delta, rel, proc) against Synth per coordinate
  - Count matches: 3/3 = all match Synth → VALID → Scriba
  - <3/3 on ANY coordinate → REVIEW → Arbiter
  
Mutual exclusion: result routes to exactly one of Scriba or Arbiter, never both.
"""

import json
from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum


class Route(Enum):
    SCRIBA = "SCRIBA"    # 3/3 match → insert into network
    ARBITER = "ARBITER"  # <3/3 → blind spot analysis


@dataclass
class CoordinateMatch:
    """Result of comparing one coordinate across 3 monodoc agents vs Synth."""
    coordinate: str          # D, A, X, P
    synth_value: str         # Synth's value (the reference)
    agent_values: dict       # {agent_name: value}
    matches: dict            # {agent_name: True/False}
    match_count: int         # 0-3
    full_match: bool         # all 3 match Synth
    dissenters: list         # agent names that diverged


@dataclass
class TribunalResult:
    concept: str
    route: Route                         # SCRIBA or ARBITER
    synth_output: dict                   # Synth's full output
    monodoc_outputs: dict                # {delta, rel, proc} full outputs
    coordinate_matches: List[CoordinateMatch]
    type_match: dict                     # {agent: True/False} for type field
    all_coordinates_unanimous: bool      # True only if every coord is 3/3
    all_types_match: bool                # True only if all 3 agree with Synth on type
    total_match_score: str               # "3/3" or "2/3" etc (worst coordinate)
    summary: str                         # human-readable


def parse_agent_output(raw_text: str) -> dict:
    """Extract JSON from agent response, handling markdown fences."""
    text = raw_text.strip()
    
    # Strip markdown code fences
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines)
    
    return json.loads(text)


def _get_value(output: dict, coord: str) -> str:
    """Extract a coordinate value from agent output, handling constraints."""
    if output.get("type") == "constraint":
        return "CONSTRAINT"
    val = output.get("coordinates", {}).get(coord)
    return str(val) if val is not None else "MISSING"


def match_coordinate(coord: str, synth: dict, monodocs: dict) -> CoordinateMatch:
    """
    Compare one coordinate: 3 monodoc agents vs Synth reference.
    
    synth: parsed Synth output
    monodocs: {"delta": parsed, "rel": parsed, "proc": parsed}
    """
    synth_val = _get_value(synth, coord)
    
    agent_values = {}
    matches = {}
    dissenters = []
    
    for name, output in monodocs.items():
        val = _get_value(output, coord)
        agent_values[name] = val
        match = (val == synth_val)
        matches[name] = match
        if not match:
            dissenters.append(name)
    
    match_count = sum(1 for m in matches.values() if m)
    
    return CoordinateMatch(
        coordinate=coord,
        synth_value=synth_val,
        agent_values=agent_values,
        matches=matches,
        match_count=match_count,
        full_match=(match_count == 3),
        dissenters=dissenters
    )


def run_tribunal(concept: str, synth_output: dict, monodoc_outputs: dict) -> TribunalResult:
    """
    Run mechanical tribunal: compare 3 monodoc agents against Synth reference.
    
    synth_output: parsed JSON from Synth
    monodoc_outputs: {
        "delta": parsed JSON from Ag-Δ,
        "rel":   parsed JSON from Ag-⇄,
        "proc":  parsed JSON from Ag-⟳
    }
    
    Returns TribunalResult with route = SCRIBA (3/3) or ARBITER (<3/3).
    """
    
    # --- Step 1: Type match (node vs constraint) ---
    synth_type = synth_output.get("type", "node")
    type_match = {}
    for name, output in monodoc_outputs.items():
        agent_type = output.get("type", "node")
        type_match[name] = (agent_type == synth_type)
    
    all_types_match = all(type_match.values())
    
    # --- Step 2: If Synth says constraint and all agree → special handling ---
    if synth_type == "constraint" and all_types_match:
        # All agree it's a constraint — check constraint_ref match
        synth_ref = synth_output.get("constraint_ref", "")
        ref_matches = all(
            monodoc_outputs[name].get("constraint_ref", "") == synth_ref
            for name in monodoc_outputs
        )
        
        return TribunalResult(
            concept=concept,
            route=Route.SCRIBA if ref_matches else Route.ARBITER,
            synth_output=synth_output,
            monodoc_outputs=monodoc_outputs,
            coordinate_matches=[],
            type_match=type_match,
            all_coordinates_unanimous=ref_matches,
            all_types_match=True,
            total_match_score="3/3" if ref_matches else "type:constraint but ref differs",
            summary=f"CONSTRAINT:{synth_output.get('constraint_ref', '?')} — "
                    f"{'unanimous' if ref_matches else 'ref divergence'}"
        )
    
    # --- Step 3: If type disagreement → straight to Arbiter ---
    if not all_types_match:
        return TribunalResult(
            concept=concept,
            route=Route.ARBITER,
            synth_output=synth_output,
            monodoc_outputs=monodoc_outputs,
            coordinate_matches=[],
            type_match=type_match,
            all_coordinates_unanimous=False,
            all_types_match=False,
            total_match_score="type_mismatch",
            summary=f"Type disagreement: Synth={synth_type}, "
                    f"agents={{{', '.join(f'{k}={v}' for k, v in type_match.items())}}}"
        )
    
    # --- Step 4: All agree it's a node → vote per coordinate ---
    coord_matches = []
    for coord in ["D", "A", "X", "P"]:
        cm = match_coordinate(coord, synth_output, monodoc_outputs)
        coord_matches.append(cm)
    
    all_unanimous = all(cm.full_match for cm in coord_matches)
    
    # Worst coordinate score for summary
    worst = min(cm.match_count for cm in coord_matches)
    total_match_score = f"{worst}/3" if not all_unanimous else "3/3"
    
    # Build summary
    summary_parts = []
    for cm in coord_matches:
        if cm.full_match:
            summary_parts.append(f"{cm.coordinate}={cm.synth_value} ✓")
        else:
            dissent_detail = ", ".join(
                f"{d}={cm.agent_values[d]}" for d in cm.dissenters
            )
            summary_parts.append(
                f"{cm.coordinate}={cm.synth_value} [{cm.match_count}/3, dissent: {dissent_detail}]"
            )
    
    return TribunalResult(
        concept=concept,
        route=Route.SCRIBA if all_unanimous else Route.ARBITER,
        synth_output=synth_output,
        monodoc_outputs=monodoc_outputs,
        coordinate_matches=coord_matches,
        type_match=type_match,
        all_coordinates_unanimous=all_unanimous,
        all_types_match=True,
        total_match_score=total_match_score,
        summary=" | ".join(summary_parts)
    )


def format_tribunal_report(result: TribunalResult) -> str:
    """Human-readable tribunal report."""
    lines = []
    lines.append(f"═══ TRIBUNAL: {result.concept} ═══")
    lines.append(f"Route: {result.route.value}")
    lines.append(f"Match: {result.total_match_score}")
    lines.append(f"Synth Σ: {result.synth_output.get('sigma', '?')}")
    lines.append("")
    
    if result.coordinate_matches:
        lines.append("COORDINATE MATCHES (vs Synth reference):")
        for cm in result.coordinate_matches:
            if cm.full_match:
                lines.append(f"  {cm.coordinate}: {cm.synth_value} — ✓ 3/3")
            else:
                dissent = ", ".join(
                    f"{d}→{cm.agent_values[d]}" for d in cm.dissenters
                )
                lines.append(
                    f"  {cm.coordinate}: Synth={cm.synth_value} — "
                    f"{cm.match_count}/3 (dissent: {dissent})"
                )
        lines.append("")
    
    if not result.all_types_match:
        lines.append(f"⚠ TYPE MISMATCH: {result.type_match}")
        lines.append("")
    
    if result.route == Route.SCRIBA:
        lines.append("→ SCRIBA: inserting into network")
    else:
        lines.append("→ ARBITER: analyzing divergences")
    
    return "\n".join(lines)
