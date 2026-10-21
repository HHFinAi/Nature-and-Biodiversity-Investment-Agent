"""Crop-area/yield decomposition and a separately labelled farm-economic stress."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from public_case_support import value, run_cli


def decompose(output_growth_percent, area_growth_percent):
    a, p = area_growth_percent / 100, output_growth_percent / 100
    if min(a, p) <= -1:
        raise ValueError('growth cannot eliminate more than all output or area')
    y = (1 + p) / (1 + a) - 1
    # Symmetric allocation of the multiplicative interaction; accounting, not causality.
    return {'yield_growth_percent': y * 100,
            'area_contribution_pp': (a + .5 * a * y) * 100,
            'yield_contribution_pp': (y + .5 * a * y) * 100}


def farm_stress(a, price_change):
    baseline_revenue = 100
    cost = a['illustrative_per_hectare_cost_index']
    gain = a['illustrative_yield_improvement']
    if not -1 < price_change or gain <= -1 or not 0 <= cost < 100:
        raise ValueError('invalid farm stress')
    revenue = baseline_revenue * (1 + gain) * (1 + price_change)
    profit = revenue - cost - a['illustrative_extra_cost_index']
    return {'price_change_percent': price_change * 100, 'revenue_index': revenue,
            'profit_index': profit, 'profit_change_percent': (profit / (100 - cost) - 1) * 100}


def calculate(inputs, sources):
    a, rows = inputs['assumptions'], []
    for crop in ('grains', 'soy', 'corn'):
        get = lambda name, unit: value(sources, 'CONAB_OCT26', crop + '_' + name, unit)
        p, area = get('production', 'million_tonnes'), get('area', 'million_crop_hectares')
        pg, ag = get('output_growth', 'percent_yoy'), get('area_growth', 'percent_yoy')
        dec = decompose(pg, ag)
        rows.append({'crop': crop, 'production_million_tonnes': p, 'crop_area_million_hectares': area,
                     'implied_tonnes_per_crop_hectare': round(p / area, 6),
                     'output_growth_percent': pg, 'crop_area_growth_percent': ag,
                     **{k: round(v, 6) for k, v in dec.items()}})
    gain = a['illustrative_yield_improvement']
    return {'prepared_on': inputs['prepared_on'], 'agency_forecast_decomposition': rows,
            'fixed_output_crop_area_reduction_percent': round((1 - 1 / (1 + gain)) * 100, 6),
            'farm_scenarios': [farm_stress(a, p) for p in (0, a['illustrative_price_change'], -.1)],
            'price_change_at_unchanged_profit_percent': round(((100 + a['illustrative_extra_cost_index']) / (100 * (1 + gain)) - 1) * 100, 6)}


def render(d):
    lines = ['# Brazil: production growth is not a yield forecast', '',
             'Original calculations from CONAB first-survey forecasts dated 15 October 2026. All changes below are approximate because the source growth rates and levels are rounded.', '',
             '| Crop | Forecast output (Mt) | Crop area (m ha) | Output growth | Area growth | Implied yield growth |',
             '|---|---:|---:|---:|---:|---:|']
    for x in d['agency_forecast_decomposition']:
        lines.append(f"| {x['crop']} | {x['production_million_tonnes']:.1f} | {x['crop_area_million_hectares']:.1f} | {x['output_growth_percent']:.1f}% | {x['crop_area_growth_percent']:.1f}% | {x['yield_growth_percent']:.2f}% |")
    lines += ['', 'Crop area sums planted/harvested cycles. It is not unique physical land, forest conversion or measured habitat loss. Total-grain yield also reflects crop mix.', '',
              '| Illustrative price change | Revenue per hectare index | Operating profit index | Profit change |',
              '|---:|---:|---:|---:|']
    for x in d['farm_scenarios']:
        lines.append(f"| {x['price_change_percent']:.1f}% | {x['revenue_index']:.2f} | {x['profit_index']:.2f} | {x['profit_change_percent']:.2f}% |")
    lines += ['', f"Under the labelled 10% yield-improvement scenario, a {d['price_change_at_unchanged_profit_percent']:.2f}% price change is the threshold for unchanged operating profit after the assumed extra cost.", '',
              f"At fixed output, the arithmetic crop-area requirement falls {d['fixed_output_crop_area_reduction_percent']:.2f}%. This is not a prediction of actual land sparing: prices, demand, expansion incentives and location evidence are missing.", '',
              'See [method and investor implications](README.md), [primary source](sources.json) and [scenario inputs](inputs.json).', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    run_cli(Path(__file__).parent, calculate, render)
