#!/usr/bin/env python3
from __future__ import annotations

"""Synchronize repo source files into ``report/code``."""

import shutil
from pathlib import Path

SYNC_MAP = {
    "scripts/baseline_neural.py": "report/code/baseline_neural.py",
    "scripts/submit_zero.py": "report/code/submit_zero.py",
    "scripts/submit_variants.py": "report/code/submit_variants.py",
    "scripts/submit_ridge.py": "report/code/submit_ridge.py",
    "scripts/submit_blend.py": "report/code/submit_blend.py",
    "scripts/checks/check_data.py": "report/code/checks/check_data.py",
    "scripts/checks/check_cutoff.py": "report/code/checks/check_cutoff.py",
    "scripts/checks/compare_boundaries.py": "report/code/checks/compare_boundaries.py",
    "core/__init__.py": "report/code/core/__init__.py",
    "core/constants.py": "report/code/core/constants.py",
    "core/paths.py": "report/code/core/paths.py",
    "core/reconstruction.py": "report/code/core/reconstruction.py",
    "core/submissions.py": "report/code/core/submissions.py",
    "core/tail_models.py": "report/code/core/tail_models.py",
}


def find_repo_root(start: Path) -> Path:
    """Walk upward from ``start`` until the project root is found."""
    here = start.resolve()
    if here.is_file():
        here = here.parent

    for candidate in [here, *here.parents]:
        if (candidate / "requirements.txt").exists() and (candidate / "data" / "raw").exists():
            return candidate

    raise FileNotFoundError(f"Could not locate repo root above: {start}")


def main() -> None:
    root = find_repo_root(Path(__file__))
    for src_rel, dst_rel in SYNC_MAP.items():
        src = root / src_rel
        dst = root / dst_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"synced {src_rel} -> {dst_rel}")


if __name__ == "__main__":
    main()
