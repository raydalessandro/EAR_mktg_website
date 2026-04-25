#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FileSync — Local Communication Layer for Neural Mapping Agents

Same pattern as DriveSync but purely local filesystem.
3 agents communicate via shared directory.
"""

import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional


class FileSync:
    """
    Local file-based communication between 3 agents:
    - Network Builder → creates networks, outputs results
    - Ontology Judge → validates ontologically
    - Mapper → proposes Sigma coordinates
    """

    def __init__(self, base_path: str = None):
        """
        Initialize FileSync.

        Args:
            base_path: Root directory for communication (defaults to ./shared)
        """
        if base_path is None:
            base_path = Path(__file__).parent.parent / "shared"

        self.base = Path(base_path)
        self.networks_path = self.base / "networks"
        self.judgments_path = self.base / "judgments"
        self.mappings_path = self.base / "mappings"

        # Create directories
        for path in [self.networks_path, self.judgments_path, self.mappings_path]:
            path.mkdir(parents=True, exist_ok=True)

    # ========== NETWORK OPERATIONS (Builder → Mapper) ==========

    def write_network_result(self, result: Dict[str, Any], filename: str = "network.json") -> Path:
        """
        Write network simulation result.

        Args:
            result: Network output (metrics, spikes, weights, etc.)
            filename: Result filename

        Returns:
            Path to written file
        """
        result_file = self.networks_path / filename

        # Add timestamp
        if 'timestamp' not in result:
            result['timestamp'] = datetime.now().isoformat()

        result_file.write_text(json.dumps(result, indent=2), encoding='utf-8')

        # Write marker
        marker = self.networks_path / f"{filename}.ready"
        marker.write_text(datetime.now().isoformat())

        return result_file

    def read_network_result(self, filename: str = "network.json") -> Optional[Dict[str, Any]]:
        """Read network result (used by Mapper)."""
        result_file = self.networks_path / filename
        marker = self.networks_path / f"{filename}.ready"

        if not marker.exists():
            return None

        result = json.loads(result_file.read_text(encoding='utf-8'))
        marker.unlink()  # Remove marker after reading
        return result

    def has_network_result(self, filename: str = "network.json") -> bool:
        """Check if network result is ready."""
        marker = self.networks_path / f"{filename}.ready"
        return marker.exists()

    # ========== JUDGMENT OPERATIONS (Judge → Mapper) ==========

    def write_judgment(self, judgment: Dict[str, Any]) -> Path:
        """
        Write ontological judgment.

        Args:
            judgment: Judgment from Ontology Judge

        Returns:
            Path to judgment file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        judgment_file = self.judgments_path / f"judgment_{timestamp}.json"

        if 'timestamp' not in judgment:
            judgment['timestamp'] = datetime.now().isoformat()

        judgment_file.write_text(json.dumps(judgment, indent=2), encoding='utf-8')

        # Write latest symlink
        latest = self.judgments_path / "latest_judgment.json"
        latest.write_text(json.dumps(judgment, indent=2), encoding='utf-8')

        # Write marker
        marker = self.judgments_path / "latest_judgment.json.ready"
        marker.write_text(datetime.now().isoformat())

        return judgment_file

    def read_judgment(self) -> Optional[Dict[str, Any]]:
        """Read latest judgment (used by Mapper)."""
        latest = self.judgments_path / "latest_judgment.json"
        marker = self.judgments_path / "latest_judgment.json.ready"

        if not marker.exists():
            return None

        judgment = json.loads(latest.read_text(encoding='utf-8'))
        marker.unlink()
        return judgment

    def has_judgment(self) -> bool:
        """Check if judgment is ready."""
        marker = self.judgments_path / "latest_judgment.json.ready"
        return marker.exists()

    # ========== MAPPING OPERATIONS (Mapper → Judge & Builder) ==========

    def write_mapping(self, mapping: Dict[str, Any]) -> Path:
        """
        Write Sigma coordinate mapping proposal.

        Args:
            mapping: Mapping from Mapper (proposed Σ coordinates)

        Returns:
            Path to mapping file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        mapping_file = self.mappings_path / f"mapping_{timestamp}.json"

        if 'timestamp' not in mapping:
            mapping['timestamp'] = datetime.now().isoformat()

        mapping_file.write_text(json.dumps(mapping, indent=2), encoding='utf-8')

        # Write latest
        latest = self.mappings_path / "latest_mapping.json"
        latest.write_text(json.dumps(mapping, indent=2), encoding='utf-8')

        # Write marker
        marker = self.mappings_path / "latest_mapping.json.ready"
        marker.write_text(datetime.now().isoformat())

        return mapping_file

    def read_mapping(self) -> Optional[Dict[str, Any]]:
        """Read latest mapping (used by Judge)."""
        latest = self.mappings_path / "latest_mapping.json"
        marker = self.mappings_path / "latest_mapping.json.ready"

        if not marker.exists():
            return None

        mapping = json.loads(latest.read_text(encoding='utf-8'))
        marker.unlink()
        return mapping

    def has_mapping(self) -> bool:
        """Check if mapping is ready."""
        marker = self.mappings_path / "latest_mapping.json.ready"
        return marker.exists()

    # ========== UTILITY ==========

    def wait_for_network(self, timeout: int = 300, poll_interval: int = 5) -> Dict[str, Any]:
        """Wait for network result with timeout."""
        elapsed = 0
        while elapsed < timeout:
            if self.has_network_result():
                return self.read_network_result()
            time.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"No network result after {timeout}s")

    def wait_for_judgment(self, timeout: int = 300, poll_interval: int = 5) -> Dict[str, Any]:
        """Wait for judgment with timeout."""
        elapsed = 0
        while elapsed < timeout:
            if self.has_judgment():
                return self.read_judgment()
            time.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"No judgment after {timeout}s")

    def wait_for_mapping(self, timeout: int = 300, poll_interval: int = 5) -> Dict[str, Any]:
        """Wait for mapping with timeout."""
        elapsed = 0
        while elapsed < timeout:
            if self.has_mapping():
                return self.read_mapping()
            time.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"No mapping after {timeout}s")

    def clear_all(self):
        """Clear all markers (for debugging/reset)."""
        for marker in self.networks_path.glob("*.ready"):
            marker.unlink()
        for marker in self.judgments_path.glob("*.ready"):
            marker.unlink()
        for marker in self.mappings_path.glob("*.ready"):
            marker.unlink()


if __name__ == "__main__":
    # Test FileSync
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        sync = FileSync(base_path=tmpdir)

        print("Testing FileSync...")

        # Test network flow
        sync.write_network_result({"type": "LIF", "tau": 1.52})
        assert sync.has_network_result()
        net = sync.read_network_result()
        assert net['tau'] == 1.52
        print("[OK] Network flow")

        # Test judgment flow
        sync.write_judgment({"valid": True, "reasoning": "Coherent with EAR"})
        assert sync.has_judgment()
        judg = sync.read_judgment()
        assert judg['valid'] == True
        print("[OK] Judgment flow")

        # Test mapping flow
        sync.write_mapping({"sigma": "Σ₄₂₂₊", "confidence": 0.8})
        assert sync.has_mapping()
        mapp = sync.read_mapping()
        assert mapp['sigma'] == "Σ₄₂₂₊"
        print("[OK] Mapping flow")

        print("\n[SUCCESS] FileSync test complete!")
