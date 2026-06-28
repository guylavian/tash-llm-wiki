"""ranking.py — T3/T6. Ranker interface with the FR-3 hard pre-filter in the base class.

LexicalRanker (default, zero ML deps), EmbeddingRanker (Stage 1), HybridRanker, factory.
Determinism (NFR-3): stable sort, tie-break (path, section); no randomness anywhere.
"""
from __future__ import annotations

import logging
import math
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass

from .index import Index, tokenize

log = logging.getLogger("wiki_router.ranking")

_CODE_RE = re.compile(r"^(?=.*\d)[a-z0-9._-]{4,}$")  # error-code-ish: has a digit, len>=4


@dataclass(frozen=True)
class Hit:
    path: str
    section: str
    title: str
    domain: str
    type: str
    inject: str
    applies_to: list
    score: float
    source_provenance: list

    def to_dict(self) -> dict:
        return {
            "path": self.path, "section": self.section, "title": self.title,
            "domain": self.domain, "type": self.type, "inject": self.inject,
            "applies_to": list(self.applies_to), "score": round(self.score, 6),
            "source_provenance": self.source_provenance,
        }


@dataclass(frozen=True)
class Candidate:
    entry_index: int
    section_index: int

    def of(self, index: Index):
        e = index.entries[self.entry_index]
        return e, e.sections[self.section_index]


def all_candidates(index: Index) -> list[Candidate]:
    return [Candidate(ei, si)
            for ei, e in enumerate(index.entries)
            for si in range(len(e.sections))]


def candidates_for_query(index: Index, query: str) -> list[Candidate]:
    toks = set(tokenize(query))
    if not toks:
        return all_candidates(index)          # filters still apply (FR-3)
    keys: set = set()
    for t in toks:
        keys.update(index.postings.get(t, ()))
    if not keys:
        return all_candidates(index)
    return [Candidate(ei, si) for (ei, si) in sorted(keys)]


def _provenance(entry) -> list:
    return list(entry.frontmatter.get("source_provenance") or [])     # FR-5


def _hit(index: Index, cand: Candidate, score: float) -> Hit:
    e, s = cand.of(index)
    return Hit(path=e.path, section=s.anchor, title=e.title, domain=e.domain,
               type=e.type, inject=e.inject, applies_to=list(e.applies_to),
               score=score, source_provenance=_provenance(e))


class Ranker(ABC):
    name = "base"

    def __init__(self, index: Index):
        self.index = index

    def rank(self, query, candidates, *, version=None, domain=None, type=None, k=5) -> list[Hit]:
        cands = self._prefilter(candidates, version, domain, type)    # FR-3 hard gate (shared)
        scores = self._score(query, cands)                            # {cand_key: float}
        hits = [_hit(self.index, c, scores.get((c.entry_index, c.section_index), 0.0))
                for c in cands]
        hits.sort(key=lambda h: (-h.score, h.path, h.section))        # NFR-3 deterministic
        return hits[:k]

    def _prefilter(self, cands, version, domain, type):
        out = []
        for c in cands:
            e = self.index.entries[c.entry_index]
            if version is not None and version not in e.applies_to:   # AC-3.1 hard pre-filter
                continue
            if domain is not None and e.domain != domain:
                continue
            if type is not None and e.type != type:
                continue
            out.append(c)
        return out

    @abstractmethod
    def _score(self, query, cands) -> dict:
        ...


class LexicalRanker(Ranker):
    name = "lexical"
    W_KEYWORDS, W_TITLE, W_SECTION, W_SUMMARY, CODE_BONUS = 3.0, 2.0, 2.0, 1.0, 5.0

    def _score(self, query, cands) -> dict:
        q = tokenize(query)
        q_set = set(q)
        codes = {t for t in q_set if _CODE_RE.match(t)}
        scores: dict = {}
        for c in cands:
            e, s = c.of(self.index)
            kw = tokenize(" ".join(str(x) for x in (e.frontmatter.get("keywords") or [])))
            title = tokenize(e.title)
            sect = tokenize(s.title)
            summ = tokenize(s.summary)
            score = 0.0
            for t in q_set:
                tf = (self.W_KEYWORDS * kw.count(t) + self.W_TITLE * title.count(t)
                      + self.W_SECTION * sect.count(t) + self.W_SUMMARY * summ.count(t))
                if tf:
                    score += math.log1p(tf)
            # exact error-code match is a strong, deterministic signal (AC-8.2)
            field = set(kw) | set(title) | set(sect) | set(summ)
            score += self.CODE_BONUS * len(codes & field)
            scores[(c.entry_index, c.section_index)] = score
        return scores


class EmbeddingRanker(Ranker):
    name = "embedding"

    def __init__(self, index: Index, embedder, store):
        super().__init__(index)
        self.embedder = embedder          # callable: list[str] -> list[list[float]]
        self.store = store                # EmbeddingStore (id -> vector)

    def _score(self, query, cands) -> dict:
        if self.embedder is None or self.store is None or self.store.empty():
            return {}
        qv = self.embedder([query])[0]
        scores: dict = {}
        for c in cands:
            e, s = c.of(self.index)
            vec = self.store.get(f"{e.path}#{s.anchor}")
            scores[(c.entry_index, c.section_index)] = self.store.cosine(qv, vec) if vec is not None else 0.0
        return scores


class HybridRanker(Ranker):
    name = "hybrid"

    def __init__(self, index: Index, lexical: LexicalRanker, embedding: EmbeddingRanker,
                 w_lex=0.5, w_emb=0.5):
        super().__init__(index)
        self.lex, self.emb, self.w_lex, self.w_emb = lexical, embedding, w_lex, w_emb

    @staticmethod
    def _norm(d: dict) -> dict:
        if not d:
            return {}
        vals = list(d.values())
        lo, hi = min(vals), max(vals)
        if hi - lo < 1e-12:
            return {k: 0.0 for k in d}
        return {k: (v - lo) / (hi - lo) for k, v in d.items()}

    def _score(self, query, cands) -> dict:
        lex = self._norm(self.lex._score(query, cands))
        emb = self._norm(self.emb._score(query, cands))
        keys = set(lex) | set(emb)
        return {k: self.w_lex * lex.get(k, 0.0) + self.w_emb * emb.get(k, 0.0) for k in keys}


def make_ranker(config, index: Index) -> Ranker:
    """Factory. embedding/hybrid degrade to lexical when no local embed source (FR-9)."""
    want = config.ranker
    if want == "lexical":
        return LexicalRanker(index)
    from . import embedding as emb_mod
    embedder, store = emb_mod.resolve(config, index)
    if embedder is None or store is None or store.empty():
        log.warning("WIKI_RANKER=%s but no local embedding source resolved; "
                    "falling back to LexicalRanker (FR-9).", want)
        return LexicalRanker(index)
    er = EmbeddingRanker(index, embedder, store)
    if want == "embedding":
        return er
    return HybridRanker(index, LexicalRanker(index), er)
