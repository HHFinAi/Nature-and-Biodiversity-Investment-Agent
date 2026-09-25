# Rights, safeguards and benefit sharing

**Agent:** Nature and Biodiversity Investment Agent · **Stage:** `rights` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Review land/resource tenure, customary rights, affected stakeholders, access, consent requirements, resettlement, grievance mechanisms and benefit-sharing contracts. Determine when free, prior and informed consent applies rather than treating a generic consultation statement as sufficient. Examine who bears restrictions and who receives payments, information asymmetry, enforcement and remedy. Separate company or sponsor claims from documented community evidence and third-party verification. Do not collect or publish personal health data or sensitive coordinates. Treat unresolved material rights or safeguarding gaps as blocking; attractive projected returns or ecological claims cannot erase them. Refer disputed legal rights and ecological/social safeguards to qualified specialists.

## Required deliverables
- `tenure_and_consent`: substantive analysis, supported claim IDs, limitations and decision implications.
- `community_safeguards`: substantive analysis, supported claim IDs, limitations and decision implications.
- `remediation_and_benefits`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- IFC-BIO: https://www.ifc.org/en/insights-reports/2022/biodiversity-finance-reference-guide

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
