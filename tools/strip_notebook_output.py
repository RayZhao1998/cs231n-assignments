#!/usr/bin/env python3
"""Strip execution outputs and counts from Jupyter notebooks.

Usage:
    python tools/strip_notebook_output.py <notebook> [<notebook> ...]

The script rewrites the given notebook files in-place if at least one
modification (output removal or execution count reset) is required.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def strip_notebook(path: Path) -> bool:
    """Remove outputs and execution counts from a single notebook."""
    try:
        with path.open("r", encoding="utf-8") as fh:
            notebook = json.load(fh)
    except json.JSONDecodeError as exc:
        print(f"Failed to parse {path}: {exc}", file=sys.stderr)
        return False

    modified = False
    cells = notebook.get("cells", [])

    for cell in cells:
        if cell.get("cell_type") != "code":
            continue

        if cell.get("outputs"):
            cell["outputs"] = []
            modified = True

        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            modified = True

        metadata = cell.get("metadata")
        if isinstance(metadata, dict):
            for key in ("execution", "collapsed"):
                if metadata.pop(key, None) is not None:
                    modified = True

    if not modified:
        return True

    with path.open("w", encoding="utf-8") as fh:
        json.dump(notebook, fh, ensure_ascii=False, indent=1)
        fh.write("\n")

    return True


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: strip_notebook_output.py <notebook> [<notebook> ...]", file=sys.stderr)
        return 1

    exit_code = 0
    for filename in argv[1:]:
        path = Path(filename)
        if not path.exists():
            print(f"Notebook not found: {path}", file=sys.stderr)
            exit_code = 1
            continue

        if not strip_notebook(path):
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
