"""Link audit for prep/ directory. Checks that all relative markdown links resolve."""
import os
import re
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "prep")

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```.*$", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`]*`")


def resolve(base_dir, target):
    target = target.split("#")[0].strip()
    if not target:
        return None
    if target.startswith(("http://", "https://", "mailto:")):
        return None
    return os.path.normpath(os.path.join(base_dir, target))


def main():
    broken = []
    total = 0
    checked_files = 0
    for root, dirs, files in os.walk(BASE):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            checked_files += 1
            fpath = os.path.join(root, fname)
            with open(fpath, encoding="utf-8", errors="replace") as fh:
                content = fh.read()
            content = FENCE_RE.sub("", content)
            content = INLINE_CODE_RE.sub("", content)
            for m in LINK_RE.finditer(content):
                target = m.group(1)
                resolved = resolve(root, target)
                if resolved is None:
                    continue
                total += 1
                if not os.path.exists(resolved):
                    broken.append((os.path.relpath(fpath, BASE), target, os.path.relpath(resolved, BASE)))
    print(f"Files scanned: {checked_files}")
    print(f"Total internal links checked: {total}")
    if broken:
        print(f"BROKEN LINKS: {len(broken)}")
        for src, tgt, resolved in broken:
            print(f"  {src} -> {tgt} (expected: {resolved})")
        return 1
    print("RESULT: 0 broken links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
