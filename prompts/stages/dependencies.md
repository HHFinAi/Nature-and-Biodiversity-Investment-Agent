# Dependencies and financial transmission

**Agent:** Nature and Biodiversity Investment Agent · **Stage:** `dependencies` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Identify dependencies on water availability/quality, pollination, soil, flood regulation, ecosystem stability and other relevant services at asset or supply-chain level. Separate dependency, exposure, vulnerability and actual loss. Test substitutability, geographic concentration, supplier flexibility, insurance, adaptation and residual risk. Map water interruption, crop variability, supply restriction or ecosystem decline to volumes, prices, margins, capex and working capital using stated assumptions. Do not convert a qualitative sector dependency flag into a numerical loss or probability without an explicit model and validation. Evaluate mitigation feasibility and timing, not just announced spending. Preserve correlations and overlap with physical climate risk to avoid double counting.

## Required deliverables
- `ecosystem_services`: substantive analysis, supported claim IDs, limitations and decision implications.
- `operational_dependencies`: substantive analysis, supported claim IDs, limitations and decision implications.
- `financial_channels`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- TNFD-LEAP: https://tnfd.global/publication/additional-guidance-on-assessment-of-nature-related-issues-the-leap-approach/

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
