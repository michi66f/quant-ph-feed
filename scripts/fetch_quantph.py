import json
import os
import re
from dataclasses import asdict, dataclass
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Dict, List, Optional, Set, Tuple

import feedparser
import requests

ARXIV_FEED_URL = "https://arxiv.org/rss/quant-ph"
ARXIV_API_URL = "https://export.arxiv.org/api/query"

DATA_DIR = "data"
SEEN_PATH = os.path.join(DATA_DIR, "seen_ids.json")
OUT_JSONL_DIR = os.path.join(DATA_DIR, "jsonl")
OUT_MD_DIR = os.path.join(DATA_DIR, "md")

TZ = ZoneInfo("Asia/Tokyo")

# RSS/Atom entry link examples:
# - https://arxiv.org/abs/2501.01234
# - https://arxiv.org/abs/2501.01234v2
ARXIV_ID_RE = re.compile(r"/abs/(\d{4}\.\d{4,5})(v\d+)?$")


@dataclass
class Paper:
    arxiv_id: str               # without version, e.g. 2501.01234
    version: str                # e.g. v1
    title: str
    authors: List[str]
    abstract: str
    primary_category: str
    categories: List[str]
    published: str              # ISO string
    updated: str                # ISO string
    abs_url: str
    pdf_url: str


def ensure_dirs() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(OUT_JSONL_DIR, exist_ok=True)
    os.makedirs(OUT_MD_DIR, exist_ok=True)


def load_seen_ids() -> Set[str]:
    if not os.path.exists(SEEN_PATH):
        return set()
    with open(SEEN_PATH, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if isinstance(obj, list):
        return set(obj)
    if isinstance(obj, dict) and "seen" in obj and isinstance(obj["seen"], list):
        return set(obj["seen"])
    return set()


def save_seen_ids(seen: Set[str]) -> None:
    with open(SEEN_PATH, "w", encoding="utf-8") as f:
        json.dump({"seen": sorted(seen)}, f, ensure_ascii=False, indent=2)


def now_jst() -> datetime:
    return datetime.now(tz=TZ)


def week_key(dt: datetime) -> str:
    # ISO week key like 2026-W02
    iso_year, iso_week, _ = dt.isocalendar()
    return f"{iso_year}-W{iso_week:02d}"


def extract_arxiv_ids_from_rss(feed_url: str) -> List[str]:
    feed = feedparser.parse(feed_url)
    ids: List[str] = []
    for entry in getattr(feed, "entries", []):
        link = getattr(entry, "link", "") or ""
        m = ARXIV_ID_RE.search(link)
        if not m:
            continue
        base_id = m.group(1)
        ids.append(base_id)
    # de-dup while preserving order
    seen: Set[str] = set()
    out: List[str] = []
    for x in ids:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def fetch_arxiv_api_by_id_list(arxiv_ids: List[str]) -> List[Paper]:
    if not arxiv_ids:
        return []

    # arXiv API supports id_list=comma,separated,ids
    params = {
        "id_list": ",".join(arxiv_ids),
        "max_results": str(len(arxiv_ids)),
    }
    r = requests.get(ARXIV_API_URL, params=params, timeout=30)
    r.raise_for_status()

    # API returns Atom; feedparser can parse it
    api_feed = feedparser.parse(r.text)

    papers: List[Paper] = []
    for entry in getattr(api_feed, "entries", []):
        # entry.id like: http://arxiv.org/abs/2501.01234v2
        entry_id = getattr(entry, "id", "") or ""
        m = ARXIV_ID_RE.search(entry_id.replace("http://", "https://"))
        if not m:
            # sometimes entry.id is abs URL without /abs/ pattern in edge cases
            # try entry.link
            link = getattr(entry, "link", "") or ""
            m = ARXIV_ID_RE.search(link)
        if not m:
            continue

        base_id = m.group(1)
        version = m.group(2) or "v1"

        title = (getattr(entry, "title", "") or "").replace("\n", " ").strip()
        abstract = (getattr(entry, "summary", "") or "").replace("\n", " ").strip()

        authors = []
        for a in getattr(entry, "authors", []) or []:
            name = (a.get("name") or "").strip()
            if name:
                authors.append(name)

        # categories: entry.tags is list of dicts with term
        categories = []
        primary_category = ""
        tags = getattr(entry, "tags", []) or []
        for t in tags:
            term = (t.get("term") or "").strip()
            if term:
                categories.append(term)
            if t.get("scheme", "").endswith("/arxiv.org/schemas/atom") and t.get("term"):
                # not reliable; keep simple
                pass

        # arXiv-specific primary_category is often in entry.arxiv_primary_category
        apc = getattr(entry, "arxiv_primary_category", None)
        if isinstance(apc, dict):
            primary_category = (apc.get("term") or "").strip()
        if not primary_category and categories:
            primary_category = categories[0]

        published = getattr(entry, "published", "") or ""
        updated = getattr(entry, "updated", "") or ""

        abs_url = f"https://arxiv.org/abs/{base_id}{version}"
        pdf_url = f"https://arxiv.org/pdf/{base_id}{version}.pdf"

        papers.append(
            Paper(
                arxiv_id=base_id,
                version=version,
                title=title,
                authors=authors,
                abstract=abstract,
                primary_category=primary_category,
                categories=categories,
                published=published,
                updated=updated,
                abs_url=abs_url,
                pdf_url=pdf_url,
            )
        )

    # Keep the same order as input IDs where possible
    by_id: Dict[str, Paper] = {p.arxiv_id: p for p in papers}
    ordered: List[Paper] = []
    for aid in arxiv_ids:
        if aid in by_id:
            ordered.append(by_id[aid])
    # Append any extras (unlikely)
    seen_ordered = {p.arxiv_id for p in ordered}
    for p in papers:
        if p.arxiv_id not in seen_ordered:
            ordered.append(p)
    return ordered


def format_markdown_block(p: Paper) -> str:
    # NotebookLM向けに読みやすい “論文カード” 形式
    author_str = ", ".join(p.authors[:8])
    if len(p.authors) > 8:
        author_str += ", et al."

    cats = "; ".join(p.categories) if p.categories else p.primary_category

    lines = []
    lines.append(f"- Date (JST ingest): {now_jst().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"- arXiv: {p.arxiv_id}{p.version}")
    lines.append(f"- Title: {p.title}")
    lines.append(f"- Authors: {author_str}")
    lines.append(f"- Categories: {p.primary_category} (primary); {cats}")
    lines.append(f"- Links: abs={p.abs_url}  pdf={p.pdf_url}")
    lines.append("")
    lines.append("Abstract:")
    lines.append(p.abstract)
    lines.append("")
    lines.append("Notes:")
    lines.append("- Keywords (auto):")
    lines.append("- Why it matters (auto):")
    lines.append("- Related cluster (auto):")
    lines.append("")
    return "\n".join(lines)


def append_jsonl(path: str, papers: List[Paper]) -> None:
    with open(path, "a", encoding="utf-8") as f:
        for p in papers:
            f.write(json.dumps(asdict(p), ensure_ascii=False) + "\n")


def append_markdown(path: str, papers: List[Paper]) -> None:
    with open(path, "a", encoding="utf-8") as f:
        for p in papers:
            f.write(format_markdown_block(p))
            f.write("\n---\n\n")


def chunk(lst: List[str], n: int) -> List[List[str]]:
    return [lst[i : i + n] for i in range(0, len(lst), n)]


def main() -> None:
    ensure_dirs()

    seen = load_seen_ids()

    # 1) RSSで候補ID取得
    candidate_ids = extract_arxiv_ids_from_rss(ARXIV_FEED_URL)

    # 2) 未取得のみ
    new_ids = [aid for aid in candidate_ids if aid not in seen]
    if not new_ids:
        print("No new arXiv IDs found in RSS.")
        return

    print(f"Found {len(new_ids)} new IDs from RSS.")

    # 3) APIで確定（id_listは長くなりすぎないよう分割）
    all_new_papers: List[Paper] = []
    for batch in chunk(new_ids, 40):
        papers = fetch_arxiv_api_by_id_list(batch)
        all_new_papers.extend(papers)

    if not all_new_papers:
        print("No papers parsed from arXiv API response.")
        return

    # 4) 出力先を週キーで分ける（JST）
    wk = week_key(now_jst())
    jsonl_path = os.path.join(OUT_JSONL_DIR, f"quantph_{wk}.jsonl")
    md_path = os.path.join(OUT_MD_DIR, f"quantph_{wk}.md")

    append_jsonl(jsonl_path, all_new_papers)
    append_markdown(md_path, all_new_papers)

    # 5) seen更新（base_idで追跡）
    for p in all_new_papers:
        seen.add(p.arxiv_id)
    save_seen_ids(seen)

    print(f"Wrote {len(all_new_papers)} papers to:")
    print(f"- {jsonl_path}")
    print(f"- {md_path}")


if __name__ == "__main__":
    main()
