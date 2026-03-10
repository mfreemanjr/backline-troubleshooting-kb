# tools/build_scripts_index.py
import re
from pathlib import Path
import mkdocs_gen_files

# Root of the docs
ROOT = Path(__file__).resolve().parents[1] / "docs"

# Languages we consider as "scripts" in code fences
LANGS = r"bash|sh|zsh|powershell|ps1|python|perl|ruby|go|ps|cmd|bat"


def looks_like_script(text: str) -> bool:
    """
    A page is considered a 'script page' if:
      - it has 'tags: [script, ...]' on a line, OR
      - it contains a fenced code block in one of the known script languages.
    """
    tag_m = re.search(r"(?mi)^tags:\s*\[(.*?)\]", text)
    if tag_m and "script" in tag_m.group(1).lower():
        return True
    return bool(re.search(rf"```(?:{LANGS})\b", text))


def first_h1(text: str, fallback: str) -> str:
    m = re.search(r"(?m)^#\s+(.+)$", text)
    return (m.group(1).strip() if m else fallback)


def summary_line(text: str) -> str:
    """
    Optional single-line summary convention on a page:
      > Summary: My one-line summary here.
    """
    m = re.search(r"(?mi)^\s*>\s*Summary:\s*(.+)$", text)
    return m.group(1).strip() if m else ""


# --- Collect rows for the index table ---
rows = []

for md in ROOT.rglob("*.md"):
    # Skip the generated page to avoid recursion
    rel = md.relative_to(ROOT).as_posix()
    if rel == "scripts/index.md":
        continue

    text = md.read_text(encoding="utf-8", errors="ignore")

    if looks_like_script(text):
        title = first_h1(text, md.stem)
        summary = summary_line(text)

        tags = ""
        tm = re.search(r"(?mi)^tags:\s*\[(.*?)\]", text)
        if tm:
            tags = ", ".join([t.strip() for t in tm.group(1).split(",")])

        rows.append((title, summary, tags, rel))

# Sort rows by title (case-insensitive)
rows.sort(key=lambda r: r[0].lower())

# --- Build the markdown content ---
out = []
out.append("# Script Index")
out.append("")
out.append("> This page is generated at build time.")
out.append("> To improve discoverability on a page that contains scripts, add:")
out.append("> ")
out.append("> - `tags: [script, <more-tags>]`")
out.append("> - `> Summary: One sentence describing the script`")
out.append("")
out.append("| Script | Summary | Tags |")
out.append("|---|---|---|")

for title, summary, tags, rel in rows:
    out.append(f"| {title} | {summary} | {tags} |")

# --- Write the generated page using mkdocs_gen_files.open() ---
text = "\n".join(out) + "\n"
out_path = "scripts/index.md"

# Optional: Make the "Edit this page" button land on the generator (or another curation doc)
mkdocs_gen_files.set_edit_path(out_path, "tools/build_scripts_index.py")

# Ensure the virtual file is created for MkDocs
with mkdocs_gen_files.open(out_path, "w") as f:
    f.write(text)