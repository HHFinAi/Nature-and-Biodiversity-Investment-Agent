"""Nature-finance scenario arithmetic, not ecological certification or GIS."""
from __future__ import annotations
from .maths import COMMON_OPERATIONS, checked, fraction, number, operation, positive, require

@operation({"portfolio_weight": "decimal_fraction", "located_weight": "decimal_fraction", "screened_weight": "decimal_fraction", "high_dependency_weight": "decimal_fraction"}, "coverage_metrics")
def exposure_coverage(portfolio_weight: float, located_weight: float, screened_weight: float, high_dependency_weight: float) -> dict:
    total = fraction(portfolio_weight, "portfolio_weight")
    require(total > 0, "portfolio_weight must be positive")
    located = fraction(located_weight, "located_weight")
    screened = fraction(screened_weight, "screened_weight")
    high = fraction(high_dependency_weight, "high_dependency_weight")
    require(0 <= high <= screened <= located <= total, "coverage boundaries inconsistent")
    return {"located_share": located / total, "screened_share": screened / total,
            "unassessed_share": (total - screened) / total,
            "high_dependency_share_of_total": high / total,
            "high_dependency_share_of_screened": high / screened if screened else None}

@operation({"observed_outcome": "$outcome", "counterfactual_outcome": "$outcome", "attribution_share": "decimal_fraction"}, "$outcome")
def additional_outcome(observed_outcome: float, counterfactual_outcome: float, attribution_share: float) -> float:
    """Signed arithmetic under supplied counterfactual; not causal identification."""
    observed = number(observed_outcome, "observed_outcome")
    counterfactual = number(counterfactual_outcome, "counterfactual_outcome")
    share = fraction(attribution_share, "attribution_share")
    return (observed - counterfactual) * share

@operation({"revenue": "$money", "exposed_share": "decimal_fraction", "disruption_share": "decimal_fraction", "contribution_margin": "decimal_fraction", "mitigation_share": "decimal_fraction", "adaptation_opex": "$money", "adaptation_capex": "$money"}, "cashflow_scenario_metrics")
def nature_cashflow_stress(revenue: float, exposed_share: float, disruption_share: float,
                           contribution_margin: float, mitigation_share: float,
                           adaptation_opex: float, adaptation_capex: float) -> dict:
    revenue = checked(revenue, "revenue", 0)
    exposure = fraction(exposed_share, "exposed_share")
    disruption = fraction(disruption_share, "disruption_share")
    margin = fraction(contribution_margin, "contribution_margin")
    mitigation = fraction(mitigation_share, "mitigation_share")
    opex = checked(adaptation_opex, "adaptation_opex", 0)
    capex = checked(adaptation_capex, "adaptation_capex", 0)
    lost_revenue = revenue * exposure * disruption * (1 - mitigation)
    cashflow_loss = lost_revenue * margin + opex + capex
    return {"lost_revenue": lost_revenue, "operating_cashflow_loss": lost_revenue * margin + opex,
            "incremental_capex": capex, "free_cashflow_change": -cashflow_loss}

@operation({"verified_incremental_outcomes": "$outcome", "eligible_cost": "$money"}, "money_per_outcome")
def cost_per_outcome(verified_incremental_outcomes: float, eligible_cost: float) -> float:
    return checked(eligible_cost, "eligible_cost", 0) / positive(verified_incremental_outcomes, "verified_incremental_outcomes")

@operation({"contracted_units": "$outcome", "delivery_fraction": "decimal_fraction", "unit_price": "money_per_outcome", "verification_cost": "$money", "other_cost": "$money"}, "$money")
def conditional_project_revenue(contracted_units: float, delivery_fraction: float, unit_price: float,
                                verification_cost: float, other_cost: float) -> float:
    """Contract-conditioned arithmetic. Does not establish issuance, fungibility, or demand."""
    units = checked(contracted_units, "contracted_units", 0)
    delivery = fraction(delivery_fraction, "delivery_fraction")
    price = checked(unit_price, "unit_price", 0)
    cost = checked(verification_cost, "verification_cost", 0) + checked(other_cost, "other_cost", 0)
    return units * delivery * price - cost

OPERATIONS = dict(COMMON_OPERATIONS)
OPERATIONS.update({f.__name__: f for f in (exposure_coverage, additional_outcome, nature_cashflow_stress, cost_per_outcome, conditional_project_revenue)})
