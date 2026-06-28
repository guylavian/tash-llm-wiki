"""index.py — T2. Build the in-memory routable index (FR-1, FR-5, NFR-4, NFR-6).

Reuses tools/wikidoc._split_frontmatter (do not reimplement — design.md, REPO CONTEXT).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

# --- reuse the frontmatter splitter from the wikidoc tool (import, don't reimplement) ----
def _load_split_frontmatter():
    here = Path(__file__).resolve()
    for p in here.parents:
        tools = p / "tools"
        if (tools / "wikidoc.py").exists():
            sys.path.insert(0, str(tools))
            from wikidoc import _split_frontmatter  # type: ignore
            return _split_frontmatter
    raise ImportError("tools/wikidoc.py not found for _split_frontmatter reuse")


_split_frontmatter = _load_split_frontmatter()

# Source-only dirs — NEVER indexed/served (REPO CONTEXT, FR-1). POSIX-normalised compare.
SOURCE_ONLY = ("wiki/reference/", "/raw/", "raw/", "/harvest/", "harvest/")
ROUTABLE_GLOBS = ("references/*.md", "references/**/*.md", "**/references/**/*.md")
_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9._-]*")
_H2_RE = re.compile(r"^##\s+(.*?)\s*$")


def posix(path: str | Path) -> str:
    return str(path).replace("\\", "/")


def _anchor(title: str) -> str:
    a = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return a or "section"


def tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


@dataclass(frozen=True)
class Section:
    anchor: str
    title: str
    start_line: int
    end_line: int
    text: str
    summary: str


@dataclass(frozen=True)
class Entry:
    path: str                      # repo-relative POSIX (NFR-6)
    frontmatter: Mapping
    domain: str
    title: str
    type: str
    inject: str
    applies_to: tuple
    sections: tuple


@dataclass(frozen=True)
class Index:
    entries: tuple
    postings: Mapping
    built_at: str


def is_source_only(rel_posix: str) -> bool:
    r = rel_posix if rel_posix.startswith("/") else "/" + rel_posix
    return any(h in r for h in SOURCE_ONLY)


def _split_sections(body: str) -> list[Section]:
    lines = body.splitlines()
    # find H2 boundaries
    heads = [(i, m.group(1)) for i, ln in enumerate(lines) for m in [_H2_RE.match(ln)] if m]
    sections: list[Section] = []
    # preamble before first H2 -> __intro__
    first = heads[0][0] if heads else len(lines)
    if any(ln.strip() for ln in lines[:first]):
        sections.append(_mk("__intro__", "(intro)", 0, first, lines))
    for idx, (ln_i, title) in enumerate(heads):
        end = heads[idx + 1][0] if idx + 1 < len(heads) else len(lines)
        anchor = _anchor(title)
        # de-dupe anchors
        base, n = anchor, 2
        existing = {s.anchor for s in sections}
        while anchor in existing:
            anchor = f"{base}-{n}"; n += 1
        sections.append(_mk(anchor, title, ln_i, end, lines))
    return sections


def _mk(anchor: str, title: str, start: int, end: int, lines: list[str]) -> Section:
    text = "\n".join(lines[start:end])
    # summary = heading + first non-empty content line, <=200c (FR-10, OQ-3); NEVER full body
    body_lines = [ln.strip() for ln in lines[start + 1:end] if ln.strip()]
    first_line = body_lines[0] if body_lines else ""
    summary = (f"{title} | {first_line}")[:200]
    return Section(anchor=anchor, title=title, start_line=start, end_line=end,
                   text=text, summary=summary)


def build_index(repo_root: str, built_at: str = "") -> Index:
    root = Path(repo_root)
    seen: set[str] = set()
    entries: list[Entry] = []
    for glob in ROUTABLE_GLOBS:
        for fp in root.glob(glob):
            if not fp.is_file():
                continue
            rel = posix(fp.relative_to(root))
            if rel in seen:
                continue
            seen.add(rel)
            if is_source_only(rel):                      # FR-1: exclude source-only
                continue
            try:
                text = fp.read_text(encoding="utf-8")     # NFR-6 UTF-8
            except (OSError, UnicodeDecodeError):
                continue
            fm, body = _split_frontmatter(text)
            if not isinstance(fm, dict) or "__yaml_error__" in fm:
                continue
            if fm.get("routable") is not True:            # FR-1: routable==true only
                continue
            sections = _split_sections(body)
            if not sections:
                continue
            at = fm.get("applies_to") or []
            entries.append(Entry(
                path=rel, frontmatter=fm,
                domain=str(fm.get("domain", "")), title=str(fm.get("title", rel)),
                type=str(fm.get("type", "")), inject=str(fm.get("inject", "section")),
                applies_to=tuple(str(v) for v in at),
                sections=tuple(sections),
            ))
    entries.sort(key=lambda e: e.path)                    # NFR-3 stable base order
    postings = _build_postings(entries)
    return Index(entries=tuple(entries), postings=postings, built_at=built_at)


def _build_postings(entries: list[Entry]) -> dict:
    postings: dict[str, set] = {}
    for ei, e in enumerate(entries):
        kw = " ".join(str(x) for x in (e.frontmatter.get("keywords") or []))
        for si, s in enumerate(e.sections):
            toks = set(tokenize(f"{e.title} {kw} {s.title} {s.summary}"))
            for t in toks:
                postings.setdefault(t, set()).add((ei, si))
    return {t: tuple(sorted(v)) for t, v in postings.items()}


# ---- path safety (NFR-4) --------------------------------------------------------------
def resolve_safe(repo_root: str, rel_path: str) -> Path | None:
    """Resolve rel_path under repo_root; return None if it escapes (.. / abs / symlink-out)."""
    if not rel_path:
        return None
    rp = rel_path.replace("\\", "/")
    if rp.startswith("/") or (len(rp) > 1 and rp[1] == ":"):  # absolute (posix/win)
        return None
    root = Path(repo_root).resolve()
    target = (root / rp).resolve()                        # resolves symlinks too
    try:
        target.relative_to(root)
    except ValueError:
        return None
    return target
