#!/usr/bin/env python3
"""Validate DeFi-Map formatting rules.

Checks (stdlib only, run from the repo root):
- README chain table: every linked file exists, protocol counts match the
  actual number of entry rows in each chain file, the Type column uses a
  known value, and the "N+" tagline matches the real total (rounded down
  to the nearest 10) and chain count.
- Chain files: canonical category names in canonical order, well-formed
  entry rows (3 cells, valid protocol link, description without trailing
  period, valid Links cell).
"""
import re
import sys
from pathlib import Path

CANONICAL_ORDER = [
    "Lending & Borrowing",
    "DEX",
    "Derivatives",
    "Prediction Markets",
    "Liquid Staking & Restaking",
    "Stablecoins",
    "RWA (Real World Assets)",
    "Yield",
    "Bridge",
    "Infrastructure",
    "Insurance",
]

CHAIN_TYPES = {"L1", "L2", "Alt L1", "Sidechain"}

PROTOCOL_CELL_RE = re.compile(r"^\[[^\]]+\]\(https?://\S+\)$")
LINK_RE = re.compile(r"^\[[a-zA-Z]+\]\(https?://\S+\)$")
README_ROW_RE = re.compile(r"^\| \[(?P<name>[^\]]+)\]\((?P<file>[a-z]+\.md)\) \| (?P<type>[^|]+) \| (?P<count>\d+) \|$")
TAGLINE_RE = re.compile(r"^> A curated list of (?P<total>\d+)\+ DeFi protocols across (?P<chains>\d+) blockchain networks\.$")

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def split_row(line: str) -> list[str] | None:
    if not (line.startswith("| ") and line.endswith(" |")):
        return None
    return line[2:-2].split(" | ")


def check_chain_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# DeFi on "):
        err(f"{path}: first line must be a '# DeFi on ...' title")

    section_indices: list[int] = []
    rows = 0
    current = None
    for n, line in enumerate(lines, 1):
        if line.startswith("## "):
            current = line[3:].strip()
            if current not in CANONICAL_ORDER:
                err(f"{path}:{n}: unknown category {current!r} (see CONTRIBUTING.md#categories)")
                continue
            idx = CANONICAL_ORDER.index(current)
            if section_indices and idx <= section_indices[-1]:
                err(f"{path}:{n}: category {current!r} out of canonical order")
            section_indices.append(idx)
        elif line.startswith("| ["):
            rows += 1
            cells = split_row(line)
            if cells is None or len(cells) != 3:
                err(f"{path}:{n}: entry row must have exactly 3 cells")
                continue
            protocol, desc, links = cells
            if not PROTOCOL_CELL_RE.match(protocol):
                err(f"{path}:{n}: Protocol cell must be '[Name](https://url/)'")
            if not desc.strip():
                err(f"{path}:{n}: Description cell is empty")
            elif desc.rstrip().endswith("."):
                err(f"{path}:{n}: Description must not end with a period")
            if links != "—" and not all(LINK_RE.match(p) for p in links.split(" · ")):
                err(f"{path}:{n}: Links cell must be '—' or '[label](url)' items separated by ' · '")
    return rows


def main() -> int:
    readme = Path("README.md").read_text(encoding="utf-8").splitlines()

    chain_rows = [m for line in readme if (m := README_ROW_RE.match(line))]
    if not chain_rows:
        err("README.md: no chain table rows found")

    total = 0
    for m in chain_rows:
        path = Path(m.group("file"))
        if not path.is_file():
            err(f"README.md: linked file {path} does not exist")
            continue
        if m.group("type") not in CHAIN_TYPES:
            err(f"README.md: unknown Type {m.group('type')!r} for {path} (expected one of {sorted(CHAIN_TYPES)})")
        actual = check_chain_file(path)
        claimed = int(m.group("count"))
        if claimed != actual:
            err(f"README.md: {path} claims {claimed} protocols but has {actual}")
        total += actual

    taglines = [m for line in readme if (m := TAGLINE_RE.match(line))]
    if len(taglines) != 1:
        err("README.md: expected exactly one '> A curated list of N+ DeFi protocols across M blockchain networks.' tagline")
    else:
        expected = total // 10 * 10
        if int(taglines[0].group("total")) != expected:
            err(f"README.md: tagline says {taglines[0].group('total')}+ protocols; should be {expected}+ (actual total {total})")
        if int(taglines[0].group("chains")) != len(chain_rows):
            err(f"README.md: tagline says {taglines[0].group('chains')} networks; chain table has {len(chain_rows)}")

    if errors:
        print(f"FAILED — {len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK — {len(chain_rows)} chains, {total} protocols, all format checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
