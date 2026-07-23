# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DeFi-Map is an Awesome List-style documentation repository cataloging DeFi (Decentralized Finance) projects across Ethereum and related blockchain networks. It is almost entirely Markdown files — the only code is a stdlib-only validation script (`scripts/check_format.py`) run by CI; no build system, no dependencies.

## Repository Structure

- `README.md` — Main index linking to all chain-specific documentation
- `address.md` — Smart contract addresses and block explorer links
- `ethereum.md` — DeFi projects on Ethereum Mainnet
- `arbitrum.md`, `base.md`, `ink.md`, `optimism.md`, `starknet.md` — DeFi projects on Layer 2 solutions
- `avalanche.md`, `bsc.md`, `hyperliquid.md`, `plasma.md`, `polygon.md`, `provenance.md`, `solana.md`, `sui.md` — DeFi projects on Alt L1 & Sidechains

## CI/CD

Three GitHub Actions workflows:

- **PR Title Check** (`check-pr-title.yml`): Enforces semantic PR titles via `amannn/action-semantic-pull-request` (requires prefixes like `feat:`, `fix:`, etc.)
- **Link Check** (`linkchecker.yml`): Validates all Markdown links using `tcort/github-action-markdown-link-check`. Runs daily at 9 AM UTC, on push to main, and on all PRs.
- **Format Check** (`validate.yml`): Runs `scripts/check_format.py` on PRs and pushes to main — validates entry-row format, canonical category names/order, and that README protocol counts match the chain files.

## Contribution Conventions

- Each chain file lists protocols in per-category tables; each entry is one row: `| [Protocol Name](https://url/) | Brief description | [docs](url) · [github](url) |` (use `—` when no docs/github links exist)
- Categories come from the canonical taxonomy in `CONTRIBUTING.md` (Lending & Borrowing → DEX → Derivatives → ... ), always in that order; entries within a category are curated by prominence, not alphabetically
- README protocol counts and the "N+" tagline are enforced by CI — update them when adding/removing entries
- Internal links use plain relative paths (e.g. `ethereum.md`) so the link checker can validate them
- Two issue form templates in `.github/ISSUE_TEMPLATE/`: `list-dapp.yml` (add new DApp) and `fix-links.yml` (report broken links)
- Licensed under CC0 (public domain)
