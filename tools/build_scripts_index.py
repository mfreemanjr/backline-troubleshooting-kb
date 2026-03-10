# tools/build_scripts_index.py
import re
from pathlib import Path
import mkdocs_gen_files

ROOT = Path(__file__).resolve().parents[1] / "docs"

# Heuristic detection of 'script pages'
LANGS = r"bash|sh|zsh|powershell|ps1|python|perl|ruby|go|ps|cmd|bat"


def looks_like_script(text: str) -> bool:
    # Tagged as script or contains a code fence in known languages
    tag_m = re.search(r'(?mi)^tags:\s*\[(.*?)\]', text)
    if tag_m and 'script' in tag_m.group(1).lower():
        return True
    return bool(re.search(rf"```(?:{LANGS})\b", text))


def first_h1(text: str, fallback: str) -> str:
    m = re.search(r'(?m)^#\s+(.+)$', text)
    return (m.group(1).strip() if m else fallback)


def summary_line(text: str) -> str:
    # Optional single-line summary convention:  > Summary: ...
    m = re.search(r'(?mi)^\s*>\s*Summary:\s*(.+)$', text)
    return m.group(1).strip() if m else ""


rows.sort(key=lambda r: r[0].lower())

out = []
out.append('# Script Index')
out.append('')
out.append('> This page is generated at build time. Add `tags: [script, ...]` and a `> Summary:` line to pages containing scripts to improve discoverability.')
out.append('')
out.append('| Script | Summary | Tags |')
out.append('|---|---|---|')
for title, summary, tags, rel in rows:
    out.append(f'| {title} | {summary} | {tags} |')

# ---- write via mkdocs_gen_files.open() ----
text = "\n".join(out) + "\n"
out_path = "scripts/index.md"

# Optional: where the "Edit this page" button should point
mkdocs_gen_files.set_edit_path(out_path, "tools/build_scripts_index.py")

with mkdocs_gen_files.open(out_path, "w") as f:
    f.write(text)