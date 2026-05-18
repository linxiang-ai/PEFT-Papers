#!/usr/bin/env python3
import json
import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_JSON = REPO_ROOT / "data" / "papers.json"
PAPERS_DIR = REPO_ROOT / "papers"

NOTICE = "> ⚠️ Auto-generated from `data/papers.json`. Do not edit manually."

QUANTIZATION_KEYWORDS = (
    "quantiz",
    "qlora",
    "loftq",
    "sub-4-bit",
    "low-bit",
    "n-bit",
    "4-bit",
    "8-bit",
)

METHOD_GROUPS = [
    ("lora-family", "LoRA Family", lambda p: "lora-family" in p["category"]),
    ("adapter", "Adapter Family", lambda p: "adapter-family" in p["category"]),
    ("prompt-tuning", "Prompt Tuning", lambda p: "soft-prompt" in p["category"]),
    ("selective", "Selective Methods", lambda p: "selective" in p["category"]),
    ("hybrid", "Hybrid Methods", lambda p: "hybrid" in p["category"]),
]

DOMAIN_GROUPS = [
    ("nlp", "NLP"),
    ("vision", "Vision"),
    ("multimodal", "Multimodal"),
    ("diffusion", "Diffusion"),
    ("speech", "Speech"),
]

MAJOR_VENUES = ("NeurIPS", "ICML", "ICLR", "ACL", "EMNLP", "CVPR", "arXiv")
VENUE_SLUG = {"arXiv": "arxiv"}


def is_quantization(p):
    text = (p.get("key_idea", "") + " " + p["title"]).lower()
    return any(k in text for k in QUANTIZATION_KEYWORDS)


def authors_str(authors):
    if len(authors) == 1:
        return authors[0]
    return f"{authors[0]} et al."


def code_field(url):
    if not url:
        return None
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+?)(?:/.*)?/?$", url)
    label = f"{m.group(1)}/{m.group(2)}" if m else url
    return f"[{label}]({url})"


def paper_field(p):
    if p.get("arxiv"):
        return f"[arXiv:{p['arxiv']}]({p['paper_url']})"
    return f"[link]({p['paper_url']})"


def render_card(p):
    lines = [
        f"### {p['title']}",
        f"- **Authors**: {authors_str(p['authors'])}",
        f"- **Venue**: {p['venue']} {p['year']}",
        f"- **Paper**: {paper_field(p)}",
    ]
    code = code_field(p.get("code_url"))
    if code:
        lines.append(f"- **Code**: {code}")
    lines.append(f"- **Idea**: {p['key_idea']}")
    params = p.get("trainable_params_ratio")
    src = p["open_source"]
    if params:
        lines.append(f"- **Params**: {params} | **Open-source**: {src}")
    else:
        lines.append(f"- **Open-source**: {src}")
    return "\n".join(lines)


def sort_key(p):
    return (-p["year"], p["id"])


def write_md(path, title, papers):
    path.parent.mkdir(parents=True, exist_ok=True)
    parts = [
        f"# {title}",
        "",
        NOTICE,
        "",
        f"_{len(papers)} papers, sorted by year (desc)._",
        "",
    ]
    for p in sorted(papers, key=sort_key):
        parts.append(render_card(p))
        parts.append("")
    path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def clear_existing_md():
    for sub in ("by-method", "by-year", "by-domain", "by-venue"):
        d = PAPERS_DIR / sub
        if d.exists():
            for f in d.glob("*.md"):
                f.unlink()
    must = PAPERS_DIR / "must-read.md"
    if must.exists():
        must.unlink()


def main():
    papers = json.loads(PAPERS_JSON.read_text(encoding="utf-8"))
    clear_existing_md()
    n_files = 0

    for slug, title, pred in METHOD_GROUPS:
        matched = [p for p in papers if pred(p)]
        if matched:
            write_md(PAPERS_DIR / "by-method" / f"{slug}.md", title, matched)
            n_files += 1

    quant = [p for p in papers if is_quantization(p)]
    if quant:
        write_md(
            PAPERS_DIR / "by-method" / "quantization-peft.md",
            "Quantization-aware PEFT",
            quant,
        )
        n_files += 1

    by_year = defaultdict(list)
    for p in papers:
        by_year[p["year"]].append(p)
    for year in sorted(by_year, reverse=True):
        write_md(
            PAPERS_DIR / "by-year" / f"{year}.md",
            f"Papers — {year}",
            by_year[year],
        )
        n_files += 1

    for slug, name in DOMAIN_GROUPS:
        matched = [p for p in papers if slug in p["domain"]]
        if matched:
            write_md(
                PAPERS_DIR / "by-domain" / f"{slug}.md",
                f"{name} PEFT",
                matched,
            )
            n_files += 1

    venue_buckets = defaultdict(list)
    other = []
    for p in papers:
        if p["venue"] in MAJOR_VENUES:
            venue_buckets[p["venue"]].append(p)
        else:
            other.append(p)
    for venue in MAJOR_VENUES:
        if venue not in venue_buckets:
            continue
        slug = VENUE_SLUG.get(venue, venue.lower())
        write_md(
            PAPERS_DIR / "by-venue" / f"{slug}.md",
            f"{venue} papers",
            venue_buckets[venue],
        )
        n_files += 1
    if other:
        write_md(
            PAPERS_DIR / "by-venue" / "other.md",
            "Other venues",
            other,
        )
        n_files += 1

    must_read = [
        p for p in papers if set(p.get("tags", [])) & {"must-read", "foundational"}
    ]
    if must_read:
        write_md(
            PAPERS_DIR / "must-read.md",
            "Must-read PEFT papers",
            must_read,
        )
        n_files += 1

    print(f"Generated {n_files} markdown files covering {len(papers)} papers.")


if __name__ == "__main__":
    main()
