import os
import re

def check_file(file_path):
    print(f"=== Checking {file_path} ===")
    if not os.path.exists(file_path):
        print("  File not found!")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    dir_path = os.path.dirname(file_path)
    matches = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    broken_count = 0
    for text, link in matches:
        if link.startswith('http://') or link.startswith('https://') or link.startswith('#') or link.startswith('mailto:'):
            continue
        clean_link = link.split('#')[0].split('?')[0]
        if not clean_link:
            continue
        target = os.path.normpath(os.path.join(dir_path, clean_link))
        if not os.path.exists(target):
            print(f"  [BROKEN] [{text}]({link}) -> Resolved: {target}")
            broken_count += 1
    print(f"  Total broken links found: {broken_count}\n")

check_file("README.md")
check_file("03_non_core/README.md")
check_file("04_company-prep/README.md")
check_file("_SYSTEM/REPO_MAP.md")
