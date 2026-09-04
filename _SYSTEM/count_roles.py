#!/usr/bin/env python3
"""Count words and assess content depth for all role files."""
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

roles = {
    'Consulting': ['non-core/consulting/consulting-overview.md','non-core/consulting/case-frameworks.md','non-core/consulting/case-bank.md'],
    'Product Manager': ['non-core/product-management/pm-overview.md','non-core/product-management/product-sense.md','non-core/product-management/pm-metrics-strategy.md'],
    'Business Analyst': ['non-core/business-analyst/ba-overview.md','non-core/business-analyst/sql-practice.md'],
    'Data Analyst': ['non-core/data-analyst/da-overview.md','non-core/data-analyst/statistics-practice.md'],
    'Product Analyst': ['non-core/product-analyst/pa-overview.md'],
    'Operations': ['non-core/operations/operations-overview.md'],
    'Supply Chain': ['non-core/supply-chain/supply-chain-overview.md'],
    'Finance': ['non-core/finance/finance-overview.md'],
    'Risk': ['non-core/risk/risk-overview.md'],
    'Strategy': ['non-core/strategy/strategy-overview.md'],
    'Program/Project Mgmt': ['non-core/program-management/pgm-overview.md'],
    'Business Operations': ['non-core/business-operations/biz-ops-overview.md'],
    'Technology': ['non-core/technology/tech-overview.md'],
    'Civil Engineer': ['core/fundamentals/civil-engineering-foundations.md','core/fundamentals/engineering-mechanics.md','core/fundamentals/strength-of-materials.md'],
    'Structural Engineer': ['core/structures/structures.md','core/structural-analysis/structural-analysis.md','core/rcc/rcc-design.md','core/steel/steel-design.md'],
    'Geotechnical Engineer': ['core/geotechnical/geotechnical.md'],
    'Transportation Engineer': ['core/transportation/transportation-engineering.md','core/transportation/transportation-software.md'],
    'Water Resources Engineer': ['core/hwre/water_resources/water-resources-engineering.md','core/hwre/hydrology/hydrology.md','core/hwre/open_channel_flow/open-channel-flow.md','core/hwre/hydraulics/hydraulics.md'],
    'Hydraulics/CFD Engineer': ['core/hwre/hydraulics/hydraulics.md','core/hwre/hydraulics/turbulence-modeling.md','software-and-tech/cfd/cfd-tech.md'],
    'Hydrologist': ['core/hwre/hydrology/hydrology.md','core/hwre/hydrology/sediment-transport.md'],
    'Environmental Engineer': ['core/environmental/environmental-engineering.md','core/hwre/wastewater/wastewater-engineering.md'],
    'GIS/Survey Engineer': ['core/geoinformatics/geoinformatics.md','software-and-tech/gis/gis-tech.md'],
    'Infrastructure/PM': ['core/infrastructure/infrastructure-engineering-management.md'],
    'BIM Engineer': ['software-and-tech/bim/bim-tech.md'],
    'Construction Engineer': ['core/infrastructure/infrastructure-engineering-management.md','software-and-tech/construction/construction-tech.md'],
}

def count_words(filepath):
    full = os.path.join(base, filepath)
    if not os.path.exists(full):
        return 0
    with open(full, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if content.startswith('\ufeff'):
        content = content[1:]
    return len(content.split())

lines = []
lines.append(f"{'ROLE':<30} {'FILES':>5} {'TOTAL':>7} {'AVG':>6} {'STATUS':<10}")
lines.append("=" * 70)

for role, files in roles.items():
    total = 0
    file_words = []
    for f in files:
        w = count_words(f)
        total += w
        file_words.append((os.path.basename(f), w))
    avg = total // len(files)
    status = 'STRONG' if total > 5000 else 'ADEQUATE' if total > 2500 else 'THIN' if total > 1000 else 'WEAK'
    lines.append(f"{role:<30} {len(files):>5} {total:>7} {avg:>6} {status:<10}")
    for name, w in file_words:
        lines.append(f"    {name:<45} {w:>6}")

output = '\n'.join(lines)
out_path = os.path.join(base, '_SYSTEM', 'role_wordcount.txt')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(output)
print(output)
