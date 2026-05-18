#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

try:
    import arxiv
except ImportError:
    sys.exit("Missing dependency. Install with: pip install -r requirements.txt")

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_JSON = REPO_ROOT / "data" / "papers.json"
OUTPUTS_DIR = REPO_ROOT / "outputs"

CONFIG = {
    "queries": [
        "parameter-efficient fine-tuning",
        "LoRA fine-tuning",
        "adapter tuning",
        "prompt tuning large language model",
        "low-rank adaptation",
    ],
    "max_results_per_query": 50,
    "max_retries": 3,
    "retry_backoff_seconds": 5,
    "client_delay_seconds": 3.0,
    "summary_chars": 300,
}


def parse_args():
    ap = argparse.ArgumentParser(
        description="Fetch new arXiv papers matching PEFT keywords."
    )
    ap.add_argument(
        "--days", type=int, default=7,
        help="lookback window in days (default: 7)",
    )
    ap.add_argument(
        "--dry-run", action="store_true",
        help="print to stdout, do not write file",
    )
    return ap.parse_args()


def load_existing_arxiv_ids():
    if not PAPERS_JSON.exists():
        return set()
    data = json.loads(PAPERS_JSON.read_text(encoding="utf-8"))
    return {p["arxiv"].split("v")[0] for p in data if p.get("arxiv")}


def arxiv_id_of(result):
    raw = result.entry_id.rsplit("/", 1)[-1]
    return raw.split("v")[0]


def short_summary(text):
    text = " ".join(text.split())
    n = CONFIG["summary_chars"]
    return text[:n] + ("..." if len(text) > n else "")


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "x"


_client = None


def get_client():
    global _client
    if _client is None:
        _client = arxiv.Client(
            page_size=100,
            delay_seconds=CONFIG["client_delay_seconds"],
            num_retries=CONFIG["max_retries"],
        )
    return _client


CS_CATEGORY_FILTER = "(cat:cs.LG OR cat:cs.CL OR cat:cs.CV OR cat:cs.AI)"


def build_search_query(q):
    phrase = f'(ti:"{q}" OR abs:"{q}")'
    return f"{phrase} AND {CS_CATEGORY_FILTER}"


def search_query(query, since):
    search = arxiv.Search(
        query=build_search_query(query),
        max_results=CONFIG["max_results_per_query"],
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    out = []
    for r in get_client().results(search):
        if r.published.replace(tzinfo=None) < since:
            break
        out.append(r)
    return out


def search_with_retry(query, since):
    last_err = None
    for attempt in range(CONFIG["max_retries"]):
        try:
            return search_query(query, since)
        except Exception as e:
            last_err = e
            print(
                f"  [retry {attempt + 1}/{CONFIG['max_retries']}] "
                f"{query!r}: {e}",
                file=sys.stderr,
            )
            time.sleep(CONFIG["retry_backoff_seconds"] * (attempt + 1))
    print(
        f"  ! {query!r} permanently failed: {last_err}",
        file=sys.stderr,
    )
    return []


def render_paper(r):
    aid = arxiv_id_of(r)
    authors = ", ".join(a.name for a in r.authors)
    return "\n".join([
        f"### {r.title.strip()}",
        f"- **Authors**: {authors}",
        f"- **arXiv**: [{aid}]({r.entry_id})",
        f"- **Published**: {r.published.strftime('%Y-%m-%d')}",
        f"- **Categories**: {', '.join(r.categories)}",
        "",
        f"> {short_summary(r.summary)}",
    ])


def render_drafts(results):
    today = dt.date.today().isoformat()
    drafts = []
    for r in results:
        aid = arxiv_id_of(r)
        first_last = r.authors[0].name.split()[-1] if r.authors else "anon"
        slug = slugify(first_last)
        drafts.append({
            "id": f"{slug}-{r.published.year}",
            "title": r.title.strip(),
            "authors": [a.name for a in r.authors],
            "venue": "arXiv",
            "year": r.published.year,
            "arxiv": aid,
            "paper_url": f"https://arxiv.org/abs/{aid}",
            "code_url": None,
            "category": ["other"],
            "domain": ["nlp"],
            "backbone": [],
            "key_idea": "TODO: one-sentence summary",
            "trainable_params_ratio": "",
            "open_source": "none",
            "tags": ["new"],
            "added_date": today,
        })
    return drafts


def main():
    args = parse_args()
    today = dt.date.today()
    since = dt.datetime.combine(
        today - dt.timedelta(days=args.days), dt.time.min
    )

    print(f"Window: last {args.days} days (since {since.date()})")
    existing = load_existing_arxiv_ids()
    print(
        f"papers.json already has {len(existing)} arxiv IDs (will dedup)"
    )

    seen = {}
    for q in CONFIG["queries"]:
        print(f"  query: {q!r}")
        added_here = 0
        for r in search_with_retry(q, since):
            aid = arxiv_id_of(r)
            if aid in existing or aid in seen:
                continue
            seen[aid] = r
            added_here += 1
        print(f"    +{added_here} new")

    new_results = sorted(
        seen.values(), key=lambda r: r.published, reverse=True
    )
    print(f"\nFound {len(new_results)} unique new papers.")

    if not new_results:
        return

    parts = [
        f"# New arXiv PEFT papers — {today.isoformat()}",
        "",
        f"_Window: last {args.days} days. Queries:_",
        *[f"- `{q}`" for q in CONFIG["queries"]],
        "",
        f"Total new (deduped against papers.json): **{len(new_results)}**.",
        "",
        "## Candidates",
        "",
    ]
    for r in new_results:
        parts.append(render_paper(r))
        parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(
        "## Suggested papers.json entries (DRAFT — review before merging)"
    )
    parts.append("")
    parts.append("```json")
    parts.append(
        json.dumps(render_drafts(new_results), indent=2, ensure_ascii=False)
    )
    parts.append("```")
    output = "\n".join(parts) + "\n"

    if args.dry_run:
        print("\n--- DRY RUN OUTPUT ---")
        print(output)
        return

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUTS_DIR / f"new_papers_{today.isoformat()}.md"
    out_path.write_text(output, encoding="utf-8")
    print(f"Wrote: {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
