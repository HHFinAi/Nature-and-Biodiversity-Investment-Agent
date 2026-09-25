# Nature business model and payment structure

**Agent:** Nature and Biodiversity Investment Agent · **Stage:** `finance` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Identify who pays for what, under which legally enforceable contract and verification regime. Separate equity/corporate-credit exposure from project finance, conservation outcomes, ecosystem-service payments and biodiversity credits. Underwrite contracted versus forecast revenue, buyer concentration, delivery/verification risk, operating and monitoring costs, capex, funding gap, tenure and terminal assumptions. Nature-credit registries, issuance, demand, transferability and ecological equivalence must be independently established; never assume a liquid exchange or interchangeable units. Distinguish an IBRD outcome bond's obligor from the country or park hosting a project. Require specific investment rights and exit constraints for private underwriting; otherwise classify research-only or no investment route.

## Required deliverables
- `revenue_contracts`: substantive analysis, supported claim IDs, limitations and decision implications.
- `costs_and_delivery`: substantive analysis, supported claim IDs, limitations and decision implications.
- `investability_boundary`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- IFC-BIO: https://www.ifc.org/en/insights-reports/2022/biodiversity-finance-reference-guide

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
