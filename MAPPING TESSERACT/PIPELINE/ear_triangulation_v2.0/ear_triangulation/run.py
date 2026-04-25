#!/usr/bin/env python3
"""
EAR Triangulation Engine v2.0 — CLI

Usage:
  python run.py map "Schwarzschild Metric"                    # Map one concept
  python run.py map "Schwarzschild Metric" --domain physics   # With domain hint
  python run.py batch concepts.txt                            # Map from file
  python run.py batch concepts.txt --domain physics           # Batch + domain
  python run.py propose                                       # Director proposes next batch
  python run.py propose --domain biology                      # Propose in specific domain
  python run.py auto 3                                        # Autonomous: 3 cycles
  python run.py auto 3 --domain physics                       # Autonomous + domain
  python run.py status                                        # Network status
  python run.py reviews                                       # List pending reviews
"""

import sys
import os
import json

# Ensure we run from the project directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from orchestrator import TriangulationEngine
from agents.director import Director, NetworkState, AutonomousLoop


def get_domain_arg(args: list) -> str:
    if "--domain" in args:
        idx = args.index("--domain")
        if idx + 1 < len(args):
            return args[idx + 1]
    return ""


def cmd_map(args):
    """Map a single concept."""
    if not args:
        print("Usage: python run.py map 'Concept Name' [--domain DOMAIN]")
        return
    
    concept = args[0]
    domain = get_domain_arg(args)
    
    engine = TriangulationEngine()
    result = engine.map_concept(concept, domain)
    
    final = result.get("final", {})
    print(f"\n{'='*40}")
    print(f"RESULT: {final.get('sigma', '?')} [{final.get('status', '?')}]")
    print(f"Route: {final.get('route', '?')} | Confidence: {final.get('confidence', 0):.2f}")
    print(f"Tokens: {result.get('stats', {}).get('total_tokens', 0)}")


def cmd_batch(args):
    """Map concepts from a file (one per line)."""
    if not args:
        print("Usage: python run.py batch concepts.txt [--domain DOMAIN]")
        return
    
    filepath = args[0]
    domain = get_domain_arg(args)
    
    with open(filepath) as f:
        concepts = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    
    print(f"Loaded {len(concepts)} concepts from {filepath}")
    
    engine = TriangulationEngine()
    engine.map_batch(concepts, domain)


def cmd_propose(args):
    """Ask Director to propose next concepts."""
    domain = get_domain_arg(args)
    count = 5
    
    config_path = "config.json"
    with open(config_path) as f:
        config = json.load(f)
    
    from core.llm_adapter import create_provider
    provider = create_provider(config["llm"].copy())
    
    network = NetworkState(
        network_path=config.get("network_path", "data/network_state.json")
    )
    
    with open(config["documents"]["kernel"]) as f:
        kernel_doc = f.read()
    with open(config["documents"]["rules"]) as f:
        rules_doc = f.read()
    with open(config["documents"]["archetypes"]) as f:
        archetypes_doc = f.read()
    
    director = Director(provider, network, kernel_doc, rules_doc, archetypes_doc)
    proposal = director.propose_batch(domain, count)
    
    print(json.dumps(proposal, indent=2))


def cmd_auto(args):
    """Run autonomous Director → Engine → Director loop."""
    cycles = int(args[0]) if args else 3
    domain = get_domain_arg(args)
    
    config_path = "config.json"
    with open(config_path) as f:
        config = json.load(f)
    
    from core.llm_adapter import create_provider
    provider = create_provider(config["llm"].copy())
    
    network = NetworkState(
        network_path=config.get("network_path", "data/network_state.json")
    )
    
    with open(config["documents"]["kernel"]) as f:
        kernel_doc = f.read()
    with open(config["documents"]["rules"]) as f:
        rules_doc = f.read()
    with open(config["documents"]["archetypes"]) as f:
        archetypes_doc = f.read()
    
    director = Director(provider, network, kernel_doc, rules_doc, archetypes_doc)
    engine = TriangulationEngine(config_path)
    loop = AutonomousLoop(engine, director)
    loop.run(cycles, domain)


def cmd_status(args):
    """Show current network status."""
    engine = TriangulationEngine()
    status = engine.get_status()
    
    print(f"\n{'='*50}")
    print("EAR TRIANGULATION ENGINE v2.0 — STATUS")
    print(f"{'='*50}")
    
    net = status["network"]
    print(f"\nNetwork: {net.get('total_nodes', 0)} nodes, "
          f"{net.get('total_constraints', 0)} constraints")
    print(f"Cells: {net.get('cells_occupied', 0)}/72 ({net.get('coverage_pct', 0)}%)")
    print(f"Pending reviews: {status['pending_reviews']}")
    
    if status["review_files"]:
        print("\nReview files:")
        for f in status["review_files"]:
            print(f"  → {f}")
    
    print(f"\nSession: {status['total_tokens_session']} tokens, {status['total_calls_session']} calls")


def cmd_reviews(args):
    """List pending review items."""
    from pathlib import Path
    
    review_dir = Path("results/review")
    if not review_dir.exists():
        print("No review directory found.")
        return
    
    files = sorted(review_dir.glob("*_review.json"))
    if not files:
        print("No pending reviews.")
        return
    
    print(f"\n{'='*50}")
    print(f"PENDING REVIEWS: {len(files)}")
    print(f"{'='*50}")
    
    for f in files:
        data = json.loads(f.read_text())
        concept = data.get("concept", "?")
        arbiter = data.get("arbiter", {})
        assessment = arbiter.get("overall_assessment", {})
        pv = assessment.get("possible_validation", False)
        conf = assessment.get("confidence", 0)
        synth_sigma = data.get("synth", {}).get("sigma", "?")
        
        status_icon = "🟡 possible_validation" if pv else "🔴 needs_review"
        print(f"\n  {concept}")
        print(f"    Synth sigma: {synth_sigma}")
        print(f"    Arbiter: {status_icon} (conf: {conf:.2f})")
        print(f"    File: {f.name}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    cmd = sys.argv[1]
    args = sys.argv[2:]
    
    commands = {
        "map": cmd_map,
        "batch": cmd_batch,
        "propose": cmd_propose,
        "auto": cmd_auto,
        "status": cmd_status,
        "reviews": cmd_reviews,
    }
    
    if cmd in commands:
        commands[cmd](args)
    else:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(commands.keys())}")


if __name__ == "__main__":
    main()
