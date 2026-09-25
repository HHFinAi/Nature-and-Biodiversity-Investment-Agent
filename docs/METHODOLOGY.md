# Methodology, units and model boundaries

## Model posture
All functions are transparent, deterministic arithmetic under caller-supplied assumptions. They do not estimate missing values, fit probabilities or validate the economic model. A number can pass unit and recomputation checks while its assumptions or causal interpretation remain wrong. Inspect `sf_agent/analytics.py` and the operation registry below.

Money uses one declared three-letter currency per calculation. FX conversions must be explicit and sourced. Percentages are decimal fractions unless a field explicitly says basis points. Scalar source metrics bind to their disclosed period, entity and unit. A series supplied as an assumption must have its period convention and underlying source work explained; the v0.1 schema does not independently reconcile a time-series spreadsheet. `scale` records explicit conversion arithmetic, but a reviewer must validate the declared units and factor.

Common helpers: `npv` uses cashflows[0] at time zero followed by annual periods; it is not XNPV and ignores irregular dates. `dscr` divides supplied cash available by positive debt service and does not normalize accounting definitions. `holding_period_return` uses consistent dirty-price money amounts, income, funding and transaction costs without annualizing or adding default probabilities. `scale` applies an explicit positive conversion factor; its semantics require human review.

## Standards maintenance
`references/standards.json` is a dated metadata register, not an embedded legal database or a substitute for the source text. Edition dates known only to the month are normalized to day 01 for indexing and must not be used as exact legal effective dates. Webpage update dates are distinguished from methodology editions. Reviewed references are checked as of September 24, 2026. Applicable adopted law, proposed reforms, voluntary guidance, reporting methodology and instrument contracts must remain separate. Reverify whenever material, before historical analysis and when the configured review age expires. The runtime blocks stale considered references at approval, but does not itself recheck a website.

## Financial and sustainability judgments
Make separate conclusions for financial attractiveness, sustainability/impact evidence and mandate compatibility. Use independent evidence for market prices, legal rights and outcomes. Report unassessed exposure and confidence limits rather than imputing zero. Document how uncertainty changes the investment decision; do not solve uncertainty by adding an unsupported discount or ESG score. “All checks pass” records an analyst's attestation and required inputs, not an independent suitability determination.

## Domain operation registry

## Nature-specific boundaries
`exposure_coverage` preserves unassessed exposure and reports high dependency relative to total and screened weights separately; a zero screened denominator produces null, not zero dependency. It does not locate assets or run GIS overlays. `additional_outcome` is `(observed − counterfactual) × attribution_share`; a negative result remains negative. It is not causal inference, ecological equivalence or verification. Outcome units must be specified and cannot be silently substituted for carbon units, hectares or other species metrics.

`nature_cashflow_stress` calculates lost revenue as revenue × exposed share × disruption share × (1 − mitigation share). It applies the stated contribution margin, adaptation opex and capex to a free-cash-flow change. All returned monetary fields use the declared currency. It omits tax, working-capital feedback, probability estimation and nonlinear/ecosystem interactions. `cost_per_outcome` divides eligible cost by a positive verified incremental outcome count; the function does not verify that count. `conditional_project_revenue` computes delivered contract units × price less verification/other costs; no demand, issuance, fungibility or market liquidity is established.

| Operation | Input unit contract | Output unit/structure |
|---|---|---|
| `npv` | `cashflows: $money`, `annual_discount: decimal` | `$money` |
| `dscr` | `cash_available: $money`, `debt_service: $money` | `multiple` |
| `scale` | `value: $input_unit`, `factor: conversion_factor` | `$output_unit` |
| `holding_period_return` | `initial_dirty_price: $money`, `exit_dirty_price: $money`, `cash_income: $money`, `funding_cost: $money`, `transaction_cost: $money` | `decimal_return` |
| `exposure_coverage` | `portfolio_weight: decimal_fraction`, `located_weight: decimal_fraction`, `screened_weight: decimal_fraction`, `high_dependency_weight: decimal_fraction` | `coverage_metrics` |
| `additional_outcome` | `observed_outcome: $outcome`, `counterfactual_outcome: $outcome`, `attribution_share: decimal_fraction` | `$outcome` |
| `nature_cashflow_stress` | `revenue: $money`, `exposed_share: decimal_fraction`, `disruption_share: decimal_fraction`, `contribution_margin: decimal_fraction`, `mitigation_share: decimal_fraction`, `adaptation_opex: $money`, `adaptation_capex: $money` | `cashflow_scenario_metrics` |
| `cost_per_outcome` | `verified_incremental_outcomes: $outcome`, `eligible_cost: $money` | `money_per_outcome` |
| `conditional_project_revenue` | `contracted_units: $outcome`, `delivery_fraction: decimal_fraction`, `unit_price: money_per_outcome`, `verification_cost: $money`, `other_cost: $money` | `$money` |

`$money` resolves to the declared currency; `$outcome` resolves to the named outcome measurement unit. Compound `money_per_outcome` resolves to currency/outcome unit. Multi-output metric dictionaries have field-level meanings described above and in the implementation. Code validates input units and recomputed results, not the scientific or economic validity of those inputs.
