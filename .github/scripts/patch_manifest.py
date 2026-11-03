#!/usr/bin/env python3
"""Patch kernel manifest default.xml to pin kernel/common to a revision.

Usage: patch_manifest.py <manifest_path> <revision> [upstream]
"""
import html
import os
import re
import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: patch_manifest.py <manifest_path> <revision> [upstream]", file=sys.stderr)
        sys.exit(1)

    manifest_path = sys.argv[1]
    revision = re.sub(r"\^{}\s*$", "", sys.argv[2].strip())
    upstream = sys.argv[3].strip() if len(sys.argv) > 3 else ""

    if not revision:
        print("ERROR: revision must not be empty", file=sys.stderr)
        sys.exit(1)
    if upstream and not re.fullmatch(r"[A-Za-z0-9._/-]+", upstream):
        print(f"ERROR: invalid upstream ref: {upstream}", file=sys.stderr)
        sys.exit(1)
    if not os.path.isfile(manifest_path):
        print(f"ERROR: manifest file not found: {manifest_path}", file=sys.stderr)
        sys.exit(1)

    with open(manifest_path, "r", encoding="utf-8") as fh:
        content = fh.read()

    pattern = r'(<project\s+[^>]*?(?:path=["\x27]common["\x27][^>]*?name=["\x27]kernel/common["\x27]|name=["\x27]kernel/common["\x27][^>]*?path=["\x27]common["\x27])[^>]*?)(/?>)'

    def replace_project(match):
        tag_start, tag_end = match.groups()
        tag_start = re.sub(r'\s+(?:revision|upstream|dest-branch)=["\x27][^"\x27]*["\x27]', "", tag_start)
        attrs = f' revision="{html.escape(revision, quote=True)}"'
        if upstream:
            attrs += f' upstream="{html.escape(upstream, quote=True)}"'
        return f"{tag_start}{attrs}{tag_end}"

    updated, count = re.subn(pattern, replace_project, content)
    if count != 1:
        print(f"ERROR: expected exactly one kernel/common project in {manifest_path}; found {count}", file=sys.stderr)
        sys.exit(1)

    with open(manifest_path, "w", encoding="utf-8") as fh:
        fh.write(updated)
    suffix = f" (upstream {upstream})" if upstream else ""
    print(f"Successfully patched {manifest_path}: pinned kernel/common to {revision}{suffix}")


if __name__ == "__main__":
    main()
