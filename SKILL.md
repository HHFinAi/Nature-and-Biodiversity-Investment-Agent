---
name: nature-biodiversity-investment-agent
description: "Run Nature and Biodiversity Investment Agent for buy-side sustainable-finance research with instrument-aware prompts, evidence lineage, reproducible calculations and human-review gates. No trade execution."
license: MIT
metadata:
  author: HHFinAi
  version: "0.1.0"
---

# Nature and Biodiversity Investment Agent

Connects location-specific ecosystem dependencies, measured outcomes, rights and financial transmission without inventing a universal biodiversity score or assuming tradability.

Read `AGENTS.md`, `prompts/system.md`, `agent.json` and `docs/INSTITUTIONAL_QUALITY.md`. Select one of the explicit routes and validate the request. Run `python -m sf_agent init --request your-request.json --out runs/new-run` from this folder; read `next`, perform the research with available tools, return and submit the artifact against the current revision. Stop on missing material inputs. Never self-approve, send orders or claim verified impact without the necessary evidence.

The package contains separate bounded skills under `skills/`. Keep all adjacent code, prompts, schemas and references available. The runtime orchestrates and validates; it does not call an LLM, retrieve data or install itself into a host. The host must supply actual authorized research tools. Copying only this file does not install the full agent. See the README for runnable examples and the exact capabilities/limits.
