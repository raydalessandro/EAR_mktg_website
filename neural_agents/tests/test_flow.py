#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Flow — Neural Mapping Agents

Tests the 3-agent communication flow:
1. Mapper generates test code
2. Network Builder executes simulation
3. Mapper analyzes results, proposes Σ
4. Ontology Judge validates mapping
5. Mapper processes judgment
"""

import sys
import time
from pathlib import Path
from datetime import datetime

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Add agents to path
sys.path.insert(0, str(Path(__file__).parent))

from network_builder.protocol import NetworkBuilderProtocol
from ontology_judge.protocol import OntologyJudgeProtocol
from mapper.protocol import MapperProtocol


def test_communication_layer():
    """Test FileSync communication independently."""
    print("\n" + "="*80)
    print("TESTING COMMUNICATION LAYER — FileSync")
    print("="*80 + "\n")

    from shared.file_sync import FileSync
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        sync = FileSync(base_path=tmpdir)

        print("Testing network flow...")
        sync.write_network_result({"type": "LIF", "tau": 1.52})
        assert sync.has_network_result(), "Network marker not found"
        net = sync.read_network_result()
        assert net['tau'] == 1.52, "Network mismatch"
        print("[OK] Network flow")

        print("\nTesting judgment flow...")
        sync.write_judgment({"judgment": "VALID", "reasoning": "OK"})
        assert sync.has_judgment(), "Judgment marker not found"
        judg = sync.read_judgment()
        assert judg['judgment'] == "VALID", "Judgment mismatch"
        print("[OK] Judgment flow")

        print("\nTesting mapping flow...")
        sync.write_mapping({"sigma": "Σ₄₂₂₊", "phenomenon": "burst"})
        assert sync.has_mapping(), "Mapping marker not found"
        mapp = sync.read_mapping()
        assert mapp['sigma'] == "Σ₄₂₂₊", "Mapping mismatch"
        print("[OK] Mapping flow")

        print("\n[SUCCESS] Communication layer test complete!\n")


def test_full_cycle():
    """Test complete mapping cycle with all 3 agents."""
    print("\n" + "="*80)
    print("TESTING FULL CYCLE — 3 Agents")
    print("="*80 + "\n")

    # Initialize agents
    print("Initializing agents...")
    builder = NetworkBuilderProtocol()
    judge = OntologyJudgeProtocol()
    mapper = MapperProtocol()
    print("[OK] All agents initialized\n")

    # PHASE 1: Mapper proposes test
    print("\n" + "-"*80)
    print("PHASE 1: Mapper → Proposes Test")
    print("-"*80 + "\n")

    phenomenon = 'burst_criticality'
    test_code = mapper.generate_test_code(phenomenon)

    mapper.sync.write_mapping({
        'phenomenon': phenomenon,
        'code': test_code,
        'timestamp': datetime.now().isoformat()
    })

    time.sleep(0.5)

    # PHASE 2: Builder executes
    print("\n" + "-"*80)
    print("PHASE 2: Network Builder → Executes Simulation")
    print("-"*80 + "\n")

    mapping_proposal = builder.sync.read_mapping()
    code = mapping_proposal['code']
    result = builder.execute_and_report(code)

    time.sleep(0.5)

    # PHASE 3: Mapper analyzes & proposes Σ
    print("\n" + "-"*80)
    print("PHASE 3: Mapper → Analyzes Results & Proposes Σ")
    print("-"*80 + "\n")

    network_result = mapper.sync.read_network_result()
    analysis = mapper.analyze_network_result(network_result)
    mapping = mapper.propose_mapping(analysis)

    if mapping.get('status') != 'proposed':
        print("[ERROR] Mapper could not propose mapping")
        return

    mapper.sync.write_mapping(mapping)

    time.sleep(0.5)

    # PHASE 4: Judge validates
    print("\n" + "-"*80)
    print("PHASE 4: Ontology Judge → Validates Mapping")
    print("-"*80 + "\n")

    mapping_to_judge = judge.sync.read_mapping()
    judgment = judge.judge_mapping(mapping_to_judge)

    time.sleep(0.5)

    # PHASE 5: Mapper processes judgment
    print("\n" + "-"*80)
    print("PHASE 5: Mapper → Processes Judgment")
    print("-"*80 + "\n")

    final_judgment = mapper.sync.read_judgment()
    action = mapper.process_judgment(final_judgment)

    # Summary
    print("\n" + "="*80)
    print("CYCLE SUMMARY")
    print("="*80 + "\n")

    print(f"Phenomenon: {phenomenon}")
    print(f"Proposed Σ: {mapping.get('sigma', 'N/A')}")
    print(f"Judgment: {judgment['judgment']}")
    print(f"Reasoning: {judgment['reasoning']}")
    print(f"Next Action: {action.get('action', 'N/A')}")

    print("\n[SUCCESS] Full cycle test complete!\n")

    return {
        'phenomenon': phenomenon,
        'mapping': mapping,
        'judgment': judgment,
        'action': action
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Test neural mapping agents")
    parser.add_argument('--test', choices=['comm', 'cycle', 'all'],
                        default='cycle', help="Test to run")

    args = parser.parse_args()

    if args.test == 'comm' or args.test == 'all':
        test_communication_layer()

    if args.test == 'cycle' or args.test == 'all':
        test_full_cycle()

    if args.test == 'all':
        print("\n" + "="*80)
        print("ALL TESTS COMPLETE ✅")
        print("="*80 + "\n")
