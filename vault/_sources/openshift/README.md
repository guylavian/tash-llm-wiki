# `_sources/openshift/` — raw notes (the immutable ground truth)

OpenShift (Kubernetes-based) is currently a **notes-first** domain: there is no
harvested corpus *yet*. The Markdown notes in this folder **are** the raw tier — the
ground truth the `openshift` synthesis pages are built on. They are distilled,
**paraphrased** facts from the public upstream documentation (provenance, not
transcripts — no long verbatim, per copyright + the wiki rule):

- **Kubernetes** — <https://kubernetes.io/docs/home/> (Concepts: Workloads, Services
  & Networking, Storage, Configuration, Cluster Administration).
- **Red Hat OpenShift Container Platform 4** — <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22>
  (and the per-version trees 4.8 → 4.22; OpenShift adds Routes, BuildConfigs/S2I,
  ImageStreams, Operators/OLM, Security Context Constraints, the OAuth server, and the
  MachineConfig/Operator day-2 model on top of upstream Kubernetes).

Treat these like the immutable `reference/<domain>/` notes for a corpus-backed domain:

- **One file per concept cluster** (`kubernetes-workloads.md`,
  `kubernetes-networking.md`, `openshift-platform.md`, …).
- **Cite it from synthesis pages** with `note:_sources/openshift/<file>.md` in the
  page's `sources:` block (path relative to `wiki/`). Carry the upstream URL as a
  `web:` source on the synthesis page where one applies.
- **Excluded from the content scanners** — `lint.py`/`index.py`/`crosslink.py` scan
  only `topics/ entities/ questions/`; files here are never linted or page-counted.
- **Provenance, not transcripts.** Each note records its source (doc + section) and
  the load-bearing facts in our own words.

> **Promotion to corpus-backed (the "all the docs like keycloak" path).** The full
> 800-body harvest is an **external, networked** step — exactly how the keycloak corpus
> was built (harvested offline into `corpora.bak/`, then folded in with
> `corpus_to_vault`). The recipe lives in `_meta/ADD-DOMAIN.md` → *Corpus-backed*: clone
> `kubernetes/website` (`content/en/docs`) and `openshift/openshift-docs` on a networked
> box, drop the subtree into `_sources/openshift/_raw/`, then run
> `python3 -m wikikb docs_to_corpus … --apply` → `python3 -m wikikb corpus_to_vault
> --domain openshift --apply`, and flip `shape:` to `corpus-backed` in `taxonomy.md`.
> Until then this notes-first spine is queryable and grows via INGEST.

Source clusters distilled into this tier:
- **Kubernetes Concepts → Workloads** → `kubernetes-workloads.md`
- **Kubernetes Concepts → Services, Load Balancing & Networking** → `kubernetes-networking.md`
- **Kubernetes Concepts → Storage** → `kubernetes-storage.md`
- **OpenShift Container Platform 4 — platform additions over Kubernetes** → `openshift-platform.md`

Grow via the wiki **INGEST** op in `../../CLAUDE.md`; the domain was onboarded via
**Operation: ADD DOMAIN** (worked example: `../../_meta/ADD-DOMAIN.md`).
