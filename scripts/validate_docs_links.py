"""Link audit for docs/ directory. Checks that all relative markdown links resolve."""
import os
import re
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DOCS = os.path.join(BASE, "docs")

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```.*$", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`]*`")

def resolve(base_dir, target):
    """Resolve a markdown link target to an absolute path, stripping anchors."""
    target = target.split("#")[0].strip()
    if not target:
        return None
    if target.startswith(("http://", "https://", "mailto:")):
        return None  # external, skip
    return os.path.normpath(os.path.join(base_dir, target))

def main():
    broken = []
    total = 0
    for root, dirs, files in os.walk(DOCS):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, encoding="utf-8", errors="replace") as fh:
                content = fh.read()
            # Strip fenced code blocks and inline code spans so example links are ignored
            content = FENCE_RE.sub("", content)
            content = INLINE_CODE_RE.sub("", content)
            for m in LINK_RE.finditer(content):
                target = m.group(1)
                resolved = resolve(root, target)
                if resolved is None:
                    continue
                total += 1
                if not os.path.exists(resolved):
                    broken.append((os.path.relpath(fpath, DOCS), target))

    print(f"Total internal links checked: {total}")
    if broken:
        print(f"BROKEN LINKS: {len(broken)}")
        for src, tgt in broken:
            print(f"  {src} -> {tgt}")
        return 1
    print("RESULT: 0 broken links")
    return 0

if __name__ == "__main__":
    sys.exit(main())