"""Optional Matplotlib chart; no plotting dependency in model or CI."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def render(preview=None):
    root = Path(__file__).resolve().parent / 'brazil-agriculture'
    rows = json.loads((root / 'results.json').read_text())['agency_forecast_decomposition']
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'svg.fonttype': 'none',
                         'svg.hashsalt': 'hhfinai-brazil-20261021', 'axes.spines.top': False, 'axes.spines.right': False})
    fig, ax = plt.subplots(figsize=(10, 5.5))
    for shift, key, label, color in [(-.25, 'output_growth_percent', 'Output', '#17365d'),
                                    (0, 'crop_area_growth_percent', 'Crop area', '#267d8d'),
                                    (.25, 'yield_growth_percent', 'Implied yield', '#be6d20')]:
        bars = ax.bar([i + shift for i in range(3)], [r[key] for r in rows], width=.24, label=label, color=color)
        ax.bar_label(bars, fmt='%.2f', padding=3, fontsize=9)
    ax.axhline(0, color='#888888', linewidth=.7)
    ax.set_xticks(range(3), ['Total grains', 'Soy', 'Corn'])
    ax.set(title='Brazil: the first 2026/27 survey is area-led', ylabel='Year-on-year change (%)', ylim=(-3.5, 6.8))
    ax.legend(ncol=3, frameon=False, loc='upper left')
    fig.text(.08, .025, 'Source: CONAB, 15 Oct 2026. Yield = (1 + output growth) / (1 + area growth) − 1.\nRounded agency forecasts, not harvest outcomes. Crop hectares are not unique physical land.', fontsize=9, color='#526170')
    fig.tight_layout(rect=(0, .11, 1, 1))
    fig.savefig(root / 'chart.svg', metadata={'Date': None})
    if preview:
        preview.mkdir(parents=True, exist_ok=True)
        fig.savefig(preview / 'brazil-agriculture.png', dpi=120)
    plt.close(fig)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--preview-dir', type=Path)
    render(p.parse_args().preview_dir)
