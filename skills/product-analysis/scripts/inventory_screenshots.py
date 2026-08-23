#!/usr/bin/env python3
"""Create a deterministic inventory for local product screenshot groups."""

from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff"}


def natural_key(path: Path) -> list[object]:
    relative = str(path).casefold()
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", relative)]


def collect(root: Path) -> list[Path]:
    return sorted(
        (path for path in root.rglob("*") if path.is_file() and path.suffix.casefold() in IMAGE_EXTENSIONS),
        key=natural_key,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Screenshot directory to inventory")
    parser.add_argument("--output", type=Path, help="Optional CSV output path")
    args = parser.parse_args()

    root = args.directory.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    rows = []
    for index, path in enumerate(collect(root), start=1):
        stat = path.stat()
        rows.append(
            {
                "screenshot_id": f"S{index:03d}",
                "group": str(path.parent.relative_to(root)) or ".",
                "file_name": path.name,
                "relative_path": str(path.relative_to(root)),
                "bytes": stat.st_size,
                "modified_local": datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(timespec="seconds"),
                "ordering_note": "natural filename order; verify against visible in-page chronology",
            }
        )

    fields = ["screenshot_id", "group", "file_name", "relative_path", "bytes", "modified_local", "ordering_note"]
    if args.output:
        output = args.output.expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    writer = csv.DictWriter(__import__("sys").stdout, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
