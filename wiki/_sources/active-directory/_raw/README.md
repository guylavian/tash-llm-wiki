# `_raw/` — drop the harvested docs tree here

This is the **staging drop zone** for a bulk docs harvest before it's folded into the
immutable `reference/active-directory/` tier. Nothing here is linted, linked, or
counted — it's pre-ingest raw material.

## How to fill it (Active Directory → Microsoft Learn docs)

The Windows Server / AD documentation is open-source Markdown on GitHub. On a
**networked** machine:

```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/MicrosoftDocs/windowsserverdocs.git
cd windowsserverdocs
git sparse-checkout set WindowsServerDocs/identity
```

Then copy the `WindowsServerDocs/identity/` folder into **this** directory:

```
wiki/_sources/active-directory/_raw/identity/
    ├── ad-ds/      # core Active Directory Domain Services
    ├── ad-cs/      # Certificate Services (PKI)
    ├── ad-fs/      # Federation Services
    └── …
```

## Then fold it in (offline, two stdlib commands)

```bash
# 1. docs tree -> corpus (index.jsonl + body files)
python3 wiki/_meta/bin/docs_to_corpus.py \
    --src wiki/_sources/active-directory/_raw/identity \
    --domain active-directory --apply

# 2. corpus -> immutable in-vault reference notes
python3 wiki/_meta/bin/corpus_to_vault.py --domain active-directory --apply
```

After that, flip the domain's `shape:` to `corpus-backed` in
`_meta/taxonomy.md`, then `index.py` → `crosslink.py --apply` → `lint.py`.
Full walkthrough: `../../../_meta/ADD-DOMAIN.md`.

> PDFs (CIS/STIG baselines, vendor guides, internal design docs) can also be
> dropped here — those get distilled into paraphrased `_sources/active-directory/`
> notes (copyright: no long verbatim) rather than folded as a corpus.
