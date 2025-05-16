#!/usr/bin/env python3

import argparse
from core import parser, matcher, timeline, visualizer

def main():
    cli = argparse.ArgumentParser(description="ChainGuardian - Analyse et Timeline d'incident")
    cli.add_argument("--logs", required=True, nargs="+", help="Fichiers de logs (JSON, CSV, etc.)")
    args = cli.parse_args()

    entries = []
    for log in args.logs:
        entries += parser.parse_log_file(log)

    matched = matcher.match_mitre_patterns(entries)
    chronologie = timeline.build_timeline(matched)
    output = visualizer.generate_html_timeline(chronologie)

    print(f"[✓] Timeline générée : {output}")

if __name__ == "__main__":
    main()