# Contributing to DeFi Map

Thank you for your interest in contributing to DeFi Map! This is a community-curated list of DeFi protocols, and we welcome contributions from everyone.

## How to Contribute

### Adding a New Protocol

1. Find the appropriate chain file (e.g., `ethereum.md`, `arbitrum.md`)
2. Add your entry under the correct category section
3. Submit a pull request

### Fixing Broken Links

If you find a broken link, please [open an issue](https://github.com/YutaSugimura/DeFi-Map/issues/new?template=fix-links.yml) or submit a PR with the fix.

### Adding a New Chain

If a blockchain network is missing entirely, open an issue first to discuss whether it should be included.

## Inclusion Criteria

To be listed, a protocol should meet the following criteria:

- **Live and operational** — The protocol must be deployed and actively running on mainnet
- **Established usage** — Demonstrable TVL or active user base
- **Official website** — A working, publicly accessible website is required
- **Non-malicious** — No known scams, rugs, or exploits with unresolved user losses

## Categories

Every entry belongs to one of the canonical categories below. Chain files use only the categories they need, always in this order:

1. Lending & Borrowing
2. DEX
3. Derivatives
4. Prediction Markets
5. Liquid Staking & Restaking
6. Stablecoins
7. RWA (Real World Assets)
8. Yield
9. Bridge
10. Infrastructure
11. Insurance

Do not invent new categories in a PR — if none of these fit, open an issue first.

## Entry Format

Each chain file lists protocols in per-category tables. Each entry is one table row:

```markdown
| Protocol | Description | Links |
| --- | --- | --- |
| [Protocol Name](https://protocol-url.com/) | Brief one-line description | [docs](https://docs.protocol-url.com/) · [github](https://github.com/protocol-org) |
```

- The protocol name should link to the official website
- The description goes in the second column, with no trailing period
- The Links column holds `docs` and `github` links separated by ` · ` (middle dot)
- Only include `docs` and `github` links if they exist — use `—` (em dash) when there are none

## PR Guidelines

- **Semantic PR title** — Use a prefix like `feat:`, `fix:`, `docs:`, or `chore:` (e.g., `feat: add Aave to Arbitrum`)
- **One chain per PR** — Keep changes focused; one PR per chain file is preferred
- **Verify links** — Make sure all URLs are valid and point to the correct pages
- **Curated order** — Entries are ordered by prominence (TVL, adoption) within their category, most significant first; add new entries where they fit, not alphabetically

## Link Checker

This repository runs an automated link checker. If your PR fails the link check, please verify that all URLs in your changes are correct and accessible.

## Code of Conduct

Be respectful and constructive in all interactions. We aim to maintain a welcoming and inclusive community for everyone.
