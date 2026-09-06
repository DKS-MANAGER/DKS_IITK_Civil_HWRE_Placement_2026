"""Fix relative links in tools/ pages by prepending ../ where needed."""
import os
import re

TOOLS_DIR = r"DKS_IITK_Civil_HWRE_Placement_2026/software-and-tech/tools"

def fix_links(text):
    def repl(m):
        target = m.group(1)
        # skip external, anchors, and already-corrected links
        if target.startswith("http") or target.startswith("#") or target.startswith("../"):
            return m.group(0)
        return f"](../{target})"
    return re.sub(r"\]\(([^)]+\.md)(?:#[^)]*)?\)", repl, text)

fixed = 0
for f in os.listdir(TOOLS_DIR):
    if not f.endswith(".md"):
        continue
    p = os.path.join(TOOLS_DIR, f)
    with open(p, encoding="utf-8", errors="ignore") as fh:
        text = fh.read()
    new_text = fix_links(text)
    if new_text != text:
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(new_text)
        fixed += 1
        print(f"FIXED {f}")
print(f"Total files fixed: {fixed}")