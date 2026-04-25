"""
EAR Triangulation Engine — Scriba

Network writer agent. Called ONLY after 3/3 tribunal match.
Responsibilities:
  1. Validate sigma format
  2. Insert node/constraint into network_state.json
  3. Create backup before each modification
  4. Return insertion confirmation

NO LLM involved — pure mechanical Python.
"""

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class ScribaResult:
    action: str              # INSERT_NODE or INSERT_CONSTRAINT
    concept: str
    sigma: str
    coordinates: dict
    constraint_ref: Optional[str]
    domain: str
    well_formed: bool
    error: Optional[str]
    inserted: bool
    backup_path: Optional[str]
    network_size: int        # total nodes after insertion


class Scriba:
    """
    Network writer. Maintains network_state.json.
    Creates backup before every modification.
    """
    
    def __init__(self, network_path: str = "data/network_state.json",
                 backup_dir: str = "data/backups"):
        self.network_path = Path(network_path)
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize network if doesn't exist
        if not self.network_path.exists():
            self._init_network()
    
    def _init_network(self):
        """Create empty network state."""
        state = {
            "version": "2.0",
            "created": datetime.now(timezone.utc).isoformat(),
            "last_modified": datetime.now(timezone.utc).isoformat(),
            "nodes": [],
            "constraints": [],
            "stats": {
                "total_nodes": 0,
                "total_constraints": 0,
                "cells_occupied": 0,
                "coverage_pct": 0.0
            }
        }
        self._save_network(state)
    
    def _load_network(self) -> dict:
        with open(self.network_path, "r") as f:
            return json.load(f)
    
    def _save_network(self, state: dict):
        with open(self.network_path, "w") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    
    def _backup(self) -> str:
        """Create timestamped backup. Returns backup path."""
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / f"network_{ts}.json"
        shutil.copy2(self.network_path, backup_path)
        return str(backup_path)
    
    def _validate_sigma(self, sigma: str, coords: dict) -> tuple:
        """
        Validate sigma notation.
        Returns (well_formed: bool, error: str or None)
        """
        # Check coordinates
        d = coords.get("D")
        a = coords.get("A")
        x = coords.get("X")
        p = coords.get("P")
        
        errors = []
        
        if d not in (1, 2, 3, 4):
            errors.append(f"D={d} not in {{1,2,3,4}}")
        if a not in (1, 2, 3):
            errors.append(f"A={a} not in {{1,2,3}}")
        if x not in (1, 2, 3):
            errors.append(f"X={x} not in {{1,2,3}}")
        if p not in ("+", "-"):
            errors.append(f"P={p} not in {{+,-}}")
        
        # Check sigma matches coordinates
        expected_sigma = f"Σ_{d}{a}{x}{p}"
        if sigma != expected_sigma:
            errors.append(f"sigma '{sigma}' doesn't match coordinates → expected '{expected_sigma}'")
        
        if errors:
            return False, "; ".join(errors)
        return True, None
    
    def _update_stats(self, state: dict):
        """Recalculate network stats."""
        nodes = state["nodes"]
        constraints = state["constraints"]
        
        # Count unique cells occupied
        cells = set()
        for node in nodes:
            cells.add(node.get("sigma", ""))
        
        state["stats"] = {
            "total_nodes": len(nodes),
            "total_constraints": len(constraints),
            "cells_occupied": len(cells),
            "coverage_pct": round(len(cells) / 72 * 100, 1)
        }
        state["last_modified"] = datetime.now(timezone.utc).isoformat()
    
    def _is_duplicate(self, state: dict, concept: str) -> bool:
        """Check if concept already exists in network."""
        for node in state["nodes"]:
            if node.get("concept", "").lower() == concept.lower():
                return True
        for constraint in state["constraints"]:
            if constraint.get("concept", "").lower() == concept.lower():
                return True
        return False
    
    def insert(self, synth_output: dict, domain: str = "") -> ScribaResult:
        """
        Insert a validated mapping into the network.
        
        synth_output: Synth's parsed output (the reference that was matched 3/3)
        domain: concept domain
        
        Returns ScribaResult with insertion details.
        """
        concept = synth_output.get("concept", "UNKNOWN")
        sigma = synth_output.get("sigma", "")
        coords = synth_output.get("coordinates", {})
        concept_type = synth_output.get("type", "node")
        constraint_ref = synth_output.get("constraint_ref")
        
        # Ensure coordinate values are ints where needed
        try:
            coords = {
                "D": int(coords.get("D", 0)),
                "A": int(coords.get("A", 0)),
                "X": int(coords.get("X", 0)),
                "P": str(coords.get("P", "?"))
            }
        except (ValueError, TypeError) as e:
            return ScribaResult(
                action="INSERT_NODE" if concept_type == "node" else "INSERT_CONSTRAINT",
                concept=concept, sigma=sigma, coordinates=coords,
                constraint_ref=constraint_ref, domain=domain,
                well_formed=False, error=f"Coordinate type error: {e}",
                inserted=False, backup_path=None, network_size=0
            )
        
        # Validate sigma
        well_formed, error = self._validate_sigma(sigma, coords)
        if not well_formed:
            return ScribaResult(
                action="INSERT_NODE" if concept_type == "node" else "INSERT_CONSTRAINT",
                concept=concept, sigma=sigma, coordinates=coords,
                constraint_ref=constraint_ref, domain=domain,
                well_formed=False, error=error,
                inserted=False, backup_path=None, network_size=0
            )
        
        # Load network
        state = self._load_network()
        
        # Check duplicate
        if self._is_duplicate(state, concept):
            return ScribaResult(
                action="INSERT_NODE" if concept_type == "node" else "INSERT_CONSTRAINT",
                concept=concept, sigma=sigma, coordinates=coords,
                constraint_ref=constraint_ref, domain=domain,
                well_formed=True, error=f"Duplicate: '{concept}' already in network",
                inserted=False, backup_path=None,
                network_size=state["stats"]["total_nodes"]
            )
        
        # Backup before modification
        backup_path = self._backup()
        
        # Build entry
        entry = {
            "concept": concept,
            "sigma": sigma,
            "coordinates": coords,
            "domain": domain,
            "confidence": 0.95,
            "validation": "3/3 monodoc match against synth reference",
            "inserted_at": datetime.now(timezone.utc).isoformat()
        }
        
        # Insert
        if concept_type == "constraint":
            entry["constraint_ref"] = constraint_ref
            state["constraints"].append(entry)
            action = "INSERT_CONSTRAINT"
        else:
            state["nodes"].append(entry)
            action = "INSERT_NODE"
        
        # Update stats and save
        self._update_stats(state)
        self._save_network(state)
        
        return ScribaResult(
            action=action,
            concept=concept,
            sigma=sigma,
            coordinates=coords,
            constraint_ref=constraint_ref,
            domain=domain,
            well_formed=True,
            error=None,
            inserted=True,
            backup_path=backup_path,
            network_size=state["stats"]["total_nodes"]
        )
    
    def get_stats(self) -> dict:
        """Return current network stats."""
        state = self._load_network()
        return state["stats"]
    
    def get_network(self) -> dict:
        """Return full network state."""
        return self._load_network()


def format_scriba_report(result: ScribaResult) -> str:
    """Human-readable Scriba report."""
    lines = []
    lines.append(f"═══ SCRIBA: {result.concept} ═══")
    lines.append(f"Action: {result.action}")
    lines.append(f"Sigma: {result.sigma}")
    lines.append(f"Well-formed: {'✓' if result.well_formed else '✗'}")
    
    if result.inserted:
        lines.append(f"Inserted: ✓")
        lines.append(f"Backup: {result.backup_path}")
        lines.append(f"Network size: {result.network_size} nodes")
    elif result.error:
        lines.append(f"NOT inserted: {result.error}")
    
    return "\n".join(lines)
