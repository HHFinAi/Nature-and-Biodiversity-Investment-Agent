# Locate assets and nature interfaces

**Agent:** Nature and Biodiversity Investment Agent · **Stage:** `locate` · **Audience:** buy-side analysts, portfolio managers and investment committees.

## Required context and inputs
Read the adopted system prompt, operating contract, selected route, request, evidence register and completed upstream artifacts. Confirm subject and instrument boundaries, as-of date and what the sources actually establish. Resolve this stage's requirements against the preceding work packet; do not treat downstream conclusions as prior evidence.

## Analytical task
Map owned assets, financed projects and material supplier locations before spatial inference. Record coordinates or regional precision, activity, ecosystem, supply-chain tier, ownership boundary, dataset provider/version/date, matching method and licence. Distinguish site-level evidence from headquarters location and country-level proxy exposure. Reconcile disclosed locations to revenue, procurement or portfolio weights; retain unassessed coverage rather than assuming no exposure. Flag sensitive habitats and ecological dependencies only at the resolution supported by the data. No GIS engine or proprietary spatial layers are bundled: external mapping must be documented and reviewed. Redact sensitive endangered-species locations and community details before public release. Return NEEDS_DATA when location uncertainty prevents the claimed conclusion.

## Required deliverables
- `location_inventory`: substantive analysis, supported claim IDs, limitations and decision implications.
- `dataset_precision`: substantive analysis, supported claim IDs, limitations and decision implications.
- `coverage_and_gaps`: substantive analysis, supported claim IDs, limitations and decision implications.

Return `schema_version`, `run_id`, `input_digest`, `stage_id`, `status`, producer identity/type, summary, typed claims, calculation records, standards considered, required sections, gaps, issues and subjective confidence with its basis. Every required section must reference actual claims, not an empty list. Add allowlisted calculations when they materially support the stage; never invent a numeric result. 

## Evidence / method anchors
- TNFD-LEAP: https://tnfd.global/publication/additional-guidance-on-assessment-of-nature-related-issues-the-leap-approach/
- TNFD-FI: https://tnfd.global/publication/additional-disclosure-guidance-for-financial-institutions/

Method references are not proof of subject facts or automatic legal compliance. Use the dated register in `references/standards.json`; document non-applicable standards rather than pretending every standard governs every instrument.

## Failure and verification checks
Return NEEDS_DATA/BLOCKED with precise missing inputs when material evidence is absent. A polished paragraph is not a substitute for evidence. Check entity, period, currency, unit, denominator, restatement, point-in-time availability and contradictory evidence. Explain the strongest plausible alternative interpretation and whether it changes the decision. Record material concerns in the issue register. Do not call the human approval action. Confidence is subjective and must state its scope, not pretend to be a calibrated probability.
