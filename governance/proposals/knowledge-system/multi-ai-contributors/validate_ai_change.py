#!/usr/bin/env python3
"""Offline scope/claim checker; not GitHub authorization or approval.
Usage: python validate_ai_change.py assignment.json changed-files.txt [active-claims.json]
"""
import fnmatch
import json
import re
import sys
from pathlib import Path

FROZEN_PREFIXES = ("meridian/fixture/", "architecture/canonical/", "decisions/catalogue/",
                   "editorial/style/", "editorial/outlines/")
IMMUTABLE_FILES = ("REPOSITORY-GOVERNANCE.md",)

def match(path, pattern):
    return fnmatch.fnmatchcase(path, pattern)

def check(record, paths, active=None):
    errors = []
    keys = ("work_item", "agent_id", "human_sponsor", "repository", "base_sha",
            "allowed_paths", "forbidden_paths", "lease_status")
    missing = [k for k in keys if not record.get(k)]
    if missing:
        return ["Missing required: " + ", ".join(missing)]
    if not re.fullmatch(r"[a-fA-F0-9]{40}", record["base_sha"]):
        errors.append("Invalid 40-character base SHA")
    if record["lease_status"] != "ACTIVE":
        errors.append("Work claim is not ACTIVE")
    if len(paths) != len(set(paths)):
        errors.append("Duplicate changed file paths")
    for path in paths:
        if not path or path.startswith("/") or "\\" in path or ".." in path.split("/"):
            errors.append(f"Invalid path: {path}")
            continue
        if path in IMMUTABLE_FILES or any(path.startswith(x) for x in FROZEN_PREFIXES):
            errors.append(f"Frozen-path change blocked: {path}")
        if not any(match(path, p) for p in record["allowed_paths"]):
            errors.append(f"Path not in assigned scope: {path}")
        if any(match(path, p) for p in record["forbidden_paths"]):
            errors.append(f"Path explicitly forbidden: {path}")
        for claim in active or []:
            if claim.get("lease_status") != "ACTIVE" or claim.get("work_item") == record["work_item"]:
                continue
            if any(match(path, p) for p in claim.get("allowed_paths", [])):
                errors.append(f"Overlapping active claim: {path} by {claim.get('work_item', '?')}")
    return errors

def main():
    if len(sys.argv) not in (3, 4):
        print(__doc__)
        return 2
    record = json.loads(Path(sys.argv[1]).read_text())
    files = Path(sys.argv[2]).read_text().splitlines()
    claims = json.loads(Path(sys.argv[3]).read_text()) if len(sys.argv) == 4 else []
    errors = check(record, files, claims)
    print(json.dumps({"status": "BLOCK" if errors else "SCOPE_CHECK_PASS",
                      "errors": errors, "checked_files": len(files)}, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
