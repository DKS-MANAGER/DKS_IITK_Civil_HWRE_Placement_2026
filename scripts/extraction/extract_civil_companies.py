#!/usr/bin/env python3
"""Extract all civil-relevant company rows from placement_data.csv."""
import csv
import json
import os

CSV_PATH = r"Civil_Placement_IITK\placement_data.csv"
OUTPUT_DIR = r"DKS_IITK_Civil_HWRE_Placement_2026\scripts"

# 25 civil-relevant companies (case-insensitive matching)
CIVIL_COMPANIES = [
    "ASC Infratech Pvt Ltd",
    "Godrej Properties",
    "Hilti Technology Solutions India",
    "Larsen & Toubro Limited",
    "Reliance New Energy",
    "Rodic Consultants",
    "SPECTRUM Techno Consultants Pvt Ltd",
    "Thornton Tomasetti",
    "Vassarlabs IT Solutions Pvt Ltd",
    "Bharat Petroleum Corp. Ltd",
    "Dimension Renewables Pvt. Ltd",
    "GIST",
    "HPCL",
    "ITC Limited",
    "JSW",
    "Petronet LNG Limited",
    "Reliance Industries Limited",
    "Smarttrak AI",
    "TuTr Hyperloop Pvt. Ltd",
    "Delta Electronics",
    "ISGEC",
    "KBR",
    "Quest Global Engineering Services Pvt. Ltd",
    "Saint-Gobain Research India",
    "Tata Steel",
]

def normalize(name):
    """Normalize company name for matching."""
    return name.strip().lower().replace(".", "").replace(",", "").replace("  ", " ")

def main():
    if not os.path.exists(CSV_PATH):
        print(f"CSV not found at {CSV_PATH}")
        return

    with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    print(f"Total rows: {len(rows)}")
    print(f"Fields: {fieldnames}")

    # Build normalized lookup
    norm_targets = {normalize(c): c for c in CIVIL_COMPANIES}

    results = {}
    for row in rows:
        company_raw = row.get("Company Name", "").strip()
        company_norm = normalize(company_raw)
        for target_norm, target_name in norm_targets.items():
            if target_norm in company_norm or company_norm in target_norm:
                if target_name not in results:
                    results[target_name] = []
                results[target_name].append(row)
                break

    # Print summary
    print(f"\nMatched {len(results)} / {len(CIVIL_COMPANIES)} companies:")
    for name in CIVIL_COMPANIES:
        count = len(results.get(name, []))
        status = f"{count} rows" if count > 0 else "NOT FOUND"
        print(f"  {name}: {status}")

    # Write full data to JSON
    output_path = os.path.join(OUTPUT_DIR, "civil_companies_data.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nWrote detailed data to {output_path}")

    # Write detailed per-company text
    detail_path = os.path.join(OUTPUT_DIR, "civil_companies_detail.txt")
    with open(detail_path, "w", encoding="utf-8") as f:
        for name in CIVIL_COMPANIES:
            company_rows = results.get(name, [])
            f.write(f"\n{'='*80}\n")
            f.write(f"COMPANY: {name}\n")
            f.write(f"ROWS: {len(company_rows)}\n")
            f.write(f"{'='*80}\n")
            for i, row in enumerate(company_rows):
                f.write(f"\n--- Row {i+1} ---\n")
                for field in fieldnames:
                    val = row.get(field, "").strip()
                    if val:
                        f.write(f"  {field}: {val[:500]}\n")
    print(f"Wrote detailed text to {detail_path}")

if __name__ == "__main__":
    main()
