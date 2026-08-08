#!/usr/bin/env python3
"""extract.py — archived HTML -> the Markdown body that lands in the raw tier.

stdlib only by default. `trafilatura` is used WHEN IT IS INSTALLED and ignored otherwise, via a
lazy import inside the function — the same optional-accelerator shape the dense-retrieval layer
uses (`embed.py`), and the reason the air-gap check in selftest.py (no module-scope third-party
import anywhere in `wikikb/`) still passes.

WHY BOTH, RATHER THAN PICKING ONE:

  * trafilatura is the best general-purpose boilerplate remover in Python and there is no reason to
    reimplement it. When it is present it wins, on every page.
  * but this project's contract is copy-and-run on a sealed box with zero pip installs, and
    trafilatura pulls lxml (compiled) plus five more packages. Making the SCRAPER the one feature
    that requires a build toolchain would quietly break the deployment model everything else here
    protects.

So: `trafilatura` when available, a bounded stdlib reader otherwise. The stdlib path is not a
placeholder — it drops the known chrome (script/style/nav/header/footer/aside/form, plus elements
whose class/id looks like navigation or a cookie banner) and renders the surviving structure as
Markdown. It is worse than trafilatura on a hostile page and adequate on documentation, which is
what this wiki harvests.

WHAT THE OUTPUT IS FOR — it becomes an IMMUTABLE reference note. So the extractor's job is fidelity
and not beauty: keep headings (they are the structure a synthesis page cites), keep code blocks
(they are half of what a technical doc is worth), keep link targets inline, and never invent
structure that was not in the source.
"""
import html as _html
import os
import re
from html.parser import HTMLParser

# Whole subtrees whose text is never content.
DROP_TREES = {"script", "style", "noscript", "svg", "canvas", "iframe", "template", "form",
              "nav", "header", "footer", "aside", "select", "button", "figure"}
# Chrome that is marked by class/id rather than by tag. Deliberately conservative: a false positive
# here silently deletes real content from an immutable note, which is far worse than some leftover
# navigation text a reader can skim past.
CHROME_RE = re.compile(r"(^|[\s_-])(nav|navbar|navigation|menu|sidebar|site-?header|site-?footer|"
                       r"breadcrumb|cookie|consent|banner|toolbar|pagination|social|share|"
                       r"skip-?link|search-?box)([\s_-]|$)", re.I)
HEADINGS = {"h1": "#", "h2": "##", "h3": "###", "h4": "####", "h5": "#####", "h6": "######"}
BLOCKS = {"p", "div", "section", "article", "main", "ul", "ol", "li", "table", "tr", "blockquote",
          "pre", "dl", "dt", "dd", "hr", "br"} | set(HEADINGS)
# Elements with no end tag. They must NOT move the drop-depth counter: a `<br>` inside a dropped
# <nav> would otherwise increment a depth that never comes back down (or, via handle_startendtag,
# decrement one it never raised), and the subtree boundary would land in the wrong place.
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param",
        "source", "track", "wbr"}
# Elements that CANNOT be chrome, whatever their class says, because they CONTAIN the document.
# Discovered 2026-08-07 on Check Point's MadCap Flare docs, whose skin puts
# `class="_Skins_Skin_HTML5_Side_Navigation_new"` on <html> itself: CHROME_RE matched
# `_Navigation_`, the drop counter went up on the first tag of the file and never came down, and
# every one of those pages extracted to ZERO characters — reported as `too-thin` (a JS-rendered
# page) when the archived HTML was in fact complete. A false positive on a leaf costs a paragraph;
# a false positive on the root costs the document, so the root is exempt by construction.
NEVER_CHROME = {"html", "body", "main", "article"}

MAX_CHARS = int(os.environ.get("WIKIKB_SCRAPE_MAX_CHARS") or 400_000)


class _Reader(HTMLParser):
    """HTML -> Markdown-ish text. One pass, no tree: a documentation page is a stream of blocks and
    building a DOM to walk it once would buy nothing.

    Nesting is tracked with a depth counter per dropped subtree rather than a tag stack, because
    real-world HTML has unclosed tags and a strict stack desynchronizes on the first one — a
    counter degrades to "drops slightly too much" instead of "drops the rest of the document".
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.title = None
        self._in_title = False
        self._drop = 0
        self._pre = 0
        self._href = None
        self._link_text = []
        self._list_stack = []          # ("ul"|"ol", counter)

    # --- helpers ---
    def _emit(self, s):
        if self._drop:
            return
        if self._href is not None:
            self._link_text.append(s)
        else:
            self.out.append(s)

    def _nl(self, n=1):
        if self._drop:
            return
        self.out.append("\n" * n)

    @staticmethod
    def _is_chrome(attrs):
        a = dict(attrs)
        for k in ("class", "id", "role"):
            v = a.get(k) or ""
            if v and CHROME_RE.search(v):
                return True
        return (a.get("aria-hidden") or "").lower() == "true"

    # --- parser callbacks ---
    def handle_startendtag(self, tag, attrs):
        """`<br/>` and friends. HTMLParser's default fires starttag THEN endtag, which would move
        the drop-depth counter twice for an element that has no real nesting — so the self-closing
        form is handled as a start only."""
        self.handle_starttag(tag, attrs)

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if self._drop:
            # EVERY non-void start tag raises the depth, not just another droppable one. Counting
            # only droppable tags was the original bug: `<nav><a>Home</a>…` dropped `nav` (depth 1),
            # ignored `<a>`, then let `</a>` decrement the depth to 0 — so the rest of the nav bar
            # was emitted as content. The counter has to track NESTING, not interest.
            if tag not in VOID:
                self._drop += 1
            return
        if tag not in NEVER_CHROME and (tag in DROP_TREES or self._is_chrome(attrs)):
            self._drop = 1
            return
        if tag == "title":
            self._in_title = True
        elif tag in HEADINGS:
            self._nl(2)
            self.out.append(HEADINGS[tag] + " ")
        elif tag == "p":
            self._nl(2)
        elif tag == "br":
            self._nl(1)
        elif tag == "hr":
            self._nl(2)
            self.out.append("---")
            self._nl(2)
        elif tag in ("ul", "ol"):
            self._list_stack.append([tag, 0])
            self._nl(2)
        elif tag == "li":
            self._nl(1)
            if self._list_stack:
                kind, n = self._list_stack[-1]
                indent = "  " * (len(self._list_stack) - 1)
                if kind == "ol":
                    self._list_stack[-1][1] = n + 1
                    self.out.append("%s%d. " % (indent, n + 1))
                else:
                    self.out.append("%s- " % indent)
            else:
                self.out.append("- ")
        elif tag == "pre":
            self._pre += 1
            self._nl(2)
            self.out.append("```\n")
        elif tag == "code" and not self._pre:
            self._emit("`")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "blockquote":
            self._nl(2)
            self.out.append("> ")
        elif tag == "a":
            href = dict(attrs).get("href") or ""
            # Only real, absolute targets survive. A relative href resolved against nothing is a
            # broken link in a note that will outlive the page it came from; an in-page anchor is
            # noise. Both degrade to plain text, never to a wrong URL.
            self._href = href if href.startswith(("http://", "https://")) else ""
            self._link_text = []
        elif tag in ("td", "th"):
            self._emit(" | ")
        elif tag == "tr":
            self._nl(1)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self._drop:
            self._drop -= 1
            return
        if tag == "title":
            self._in_title = False
        elif tag in HEADINGS or tag == "p":
            self._nl(2)
        elif tag in ("ul", "ol"):
            if self._list_stack:
                self._list_stack.pop()
            self._nl(2)
        elif tag == "pre":
            self._pre = max(0, self._pre - 1)
            self.out.append("\n```")
            self._nl(2)
        elif tag == "code" and not self._pre:
            self._emit("`")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "blockquote":
            self._nl(2)
        elif tag == "a" and self._href is not None:
            text = "".join(self._link_text).strip()
            href, self._href, self._link_text = self._href, None, []
            if text and href:
                self.out.append("[%s](%s)" % (text, href))
            elif text:
                self.out.append(text)

    def handle_data(self, data):
        if self._in_title and not self.title:
            t = re.sub(r"\s+", " ", data).strip()
            if t:
                self.title = t[:200]
            return
        if self._drop or not data:
            return
        self._emit(data if self._pre else re.sub(r"[ \t\r\n]+", " ", data))


def _clean(text):
    """Collapse the whitespace a stream renderer inevitably produces, and drop the one-word
    leftovers that survive chrome removal on link-heavy pages."""
    text = _html.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines, out = text.split("\n"), []
    for ln in lines:
        s = ln.rstrip()
        if out and not s and not out[-1]:
            continue
        out.append(s)
    return "\n".join(out).strip()


def _stdlib_extract(html_text):
    r = _Reader()
    try:
        r.feed(html_text)
        r.close()
    except Exception:                          # noqa: BLE001 — a malformed page yields whatever was
        pass                                    # parsed before the break, never an aborted harvest
    return r.title, _clean("".join(r.out))


def _trafilatura_extract(html_text, url=None):
    """trafilatura when installed. Lazily imported INSIDE the function — a module-scope import would
    both break the air-gap check and make this module unimportable wherever it is absent."""
    try:
        import trafilatura                                       # noqa: PLC0415 — deliberate
    except ImportError:
        return None
    try:
        md = trafilatura.extract(html_text, url=url, output_format="markdown",
                                 include_links=True, include_tables=True,
                                 include_comments=False, favor_recall=True)
        if not md or not md.strip():
            return None
        title = None
        try:
            meta = trafilatura.extract_metadata(html_text)
            title = getattr(meta, "title", None) if meta else None
        except Exception:                                        # noqa: BLE001
            title = None
        return title, _clean(md)
    except Exception:                                            # noqa: BLE001 — never let an
        return None                                              # extractor bug abort a harvest


def to_markdown(html_text, url=None):
    """(title, markdown, extractor). Falls back stdlib-ward on anything trafilatura declines.

    The extractor NAME is returned, not just the text, because it goes into the harvested note's
    sidecar: two notes for the same site extracted by different code paths will differ, and an
    operator comparing them needs to see why without re-running anything.
    """
    if not html_text or not html_text.strip():
        return None, "", "none"
    got = _trafilatura_extract(html_text, url)
    if got and got[1].strip():
        title, md = got
        if not title:
            title = _stdlib_extract(html_text)[0]
        return title, md[:MAX_CHARS], "trafilatura"
    title, md = _stdlib_extract(html_text)
    return title, md[:MAX_CHARS], "stdlib"


def available():
    """Which extractor a harvest would actually use right now — reported by `GET /scrape/sources`
    so "why is this note so noisy" is answerable without reading the harvest logs."""
    try:
        import trafilatura                                       # noqa: F401,PLC0415
        return "trafilatura"
    except ImportError:
        return "stdlib"
