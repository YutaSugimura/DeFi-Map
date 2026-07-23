# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DeFi-Map is an Awesome List-style documentation repository cataloging DeFi (Decentralized Finance) projects across Ethereum and related blockchain networks. It contains only Markdown files — no application code, no build system, no dependencies.

## Repository Structure

- `README.md` — Main index linking to all chain-specific documentation
- `address.md` — Smart contract addresses and block explorer links
- `ethereum.md` — DeFi projects on Ethereum Mainnet
- `arbitrum.md`, `base.md`, `ink.md`, `optimism.md`, `starknet.md` — DeFi projects on Layer 2 solutions
- `avalanche.md`, `bsc.md`, `hyperliquid.md`, `plasma.md`, `polygon.md`, `provenance.md`, `solana.md`, `sui.md` — DeFi projects on Alt L1 & Sidechains

## CI/CD

Two GitHub Actions workflows:

- **PR Title Check** (`check-pr-title.yml`): Enforces semantic PR titles via `amannn/action-semantic-pull-request` (requires prefixes like `feat:`, `fix:`, etc.)
- **Link Check** (`linkchecker.yml`): Validates all Markdown links using `tcort/github-action-markdown-link-check`. Runs daily at 9 AM UTC, on push to main, and on all PRs.

## Contribution Conventions

- Each DeFi project entry follows a consistent format: `- [Protocol Name](https://url/) Brief description.` followed by indented sub-items (docs, github)
- `<!-- markdown-link-check-disable/enable -->` comments in `README.md` control the link checker — used around internal relative links
- Two issue form templates in `.github/ISSUE_TEMPLATE/`: `list-dapp.yml` (add new DApp) and `fix-links.yml` (report broken links)
- Licensed under CC0 (public domain)
