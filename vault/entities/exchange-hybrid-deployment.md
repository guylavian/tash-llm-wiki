---
title: Exchange Hybrid Deployment Basics
type: entity
domain: exchange
slug: exchange-hybrid-deployment
summary: What a Microsoft 365/Office 365 hybrid deployment adds to on-premises Exchange — the cloud-based Hybrid Configuration Wizard, Microsoft Entra Connect for multi-forest sync, and Hybrid Modern Auth (HMA).
sources:
  - kb:exchange-exchange-servertoc-p0001-0040
  - kb:exchange-exchange-servertoc-p0641-0680
  - web:https://learn.microsoft.com/en-us/answers/questions/116123/azure-ad-connect-on-win-essentials-2019-exchange-n (Microsoft Q&A, fetched 2026-07-25)
  - web:https://learn.microsoft.com/en-us/answers/questions/1186480/migrating-from-azure-ad-connect-to-azure-ad-connec (Microsoft Q&A, fetched 2026-07-25)
provenance_extracted: 10
provenance_inferred: 2
provenance_ambiguous: 0
tags: [migration, security]
status: draft
updated: 2026-07-25
graph_community: "Exchange Server — Implementation Review (Evaluation-Lens MOC)"
---

# Exchange Hybrid Deployment Basics

**Hybrid deployment coexists an on-premises Exchange organization with Exchange
Online, configured through the cloud-based Hybrid Configuration Wizard (HCW) and
secured end-to-end with Hybrid Modern Auth (HMA).**

## Body

The **Hybrid Configuration Wizard (HCW)** moved to a cloud-based small downloadable
app (rather than a bundled on-prem tool); this lets Microsoft update it quickly for
service changes and improve in-wizard troubleshooting/diagnostics. The same wizard
serves anyone hybridizing from Exchange 2013 or later
(`exchange-exchange-servertoc-p0001-0040.md:374-390`). Multi-forest hybrid is
simplified by **Microsoft Entra Connect** (formerly Azure AD Connect/AADConnect),
whose management agents synchronize multiple on-premises AD forests into a single
Microsoft 365/Office 365 tenant (`exchange-exchange-servertoc-p0001-0040.md:392-396`).
Mailbox moves to Exchange Online transparently redirect ActiveSync clients via
**HTTP 451 redirect** — the device profile is updated with the Exchange Online URL
so the client stops contacting the on-prem server
(`exchange-exchange-servertoc-p0001-0040.md:398-402`).

**Hybrid Modern Auth (HMA)** extends OAuth 2.0-based modern authentication to the
on-premises leg of a hybrid organization. If an org was already using Modern Auth
with ADFS and later configures Exchange Hybrid, Microsoft's guidance is to
**transition to HMA** rather than run both models
(`exchange-exchange-servertoc-p0681-0720.md:17-21` — cross-referenced from the HMA
migration note; the underlying HMA prerequisites/configuration live in
`exchange-exchange-servertoc-p0641-0680.md:636-684`, which notes an Exchange Hybrid
organization *without* HMA should adopt HMA with Microsoft Entra ID).

## Community Q&A (upstream)

Two Microsoft Q&A community threads ask the practical follow-on question the
vendor docs above don't directly answer: once directory sync is running, is
on-premises Exchange still required at all, and is it safe to decommission it?
Both threads have **zero accepted answers and zero upvotes** — treat everything
below as community guidance to verify, not a support statement.

A **Volunteer Moderator**-authored answer states plainly that Exchange is *not*
required purely to sync AD attributes — Azure AD Connect (now Microsoft Entra
Connect) itself performs the attribute sync, and the answerer reports "a few
customers running Azure AD Connect with no Exchange on-premise" (web:116123). A
second, unranked community reply in the same thread adds an important condition:
the answer differs for **Exchange hybrid** vs. **cloud-only (Microsoft 365 with no
hybrid mail flow)** — for a hybrid deployment specifically, the reply points to
Microsoft's own guide, *"How and when to decommission your on-premises Exchange
servers in a hybrid deployment,"* as the authoritative procedure, and notes
Microsoft's stated recommendation to keep an Exchange server installed when
objects are actively directory-synced from on-premises to Microsoft 365
(web:116123).

A second thread asks the practical decommission question directly: after
migrating from (classic) Azure AD Connect to **Azure AD Connect cloud sync**, is
it safe to just uninstall the old on-premises Exchange 2013 server? A
**MicrosoftVendor-affiliated** community answer (the strongest-weighted authorship
on this specific question) recommends *not* uninstalling outright: shut the
on-premises server down first, run Exchange Online for a while to confirm
everything keeps working correctly, and only then uninstall (web:1186480). A
second community reply in the same thread largely agrees in substance — once the
Exchange server is no longer used for any mail protocol and all mailboxes/mail
routing live in Exchange Online/Microsoft 365, it can safely be removed, with AD
used only for on-premises user account management going forward (web:1186480).

Read together, the two threads converge on the same practical sequence — shut
down first, verify cloud-only operation holds, then uninstall, rather than
uninstalling in one step — but the MicrosoftVendor-affiliated answer is the one
that actually recommends the staged shutdown-then-verify order; the plain
community reply only confirms uninstall is *eventually* safe, not the staging
(inferred — this sequencing conclusion isn't stated as a single rule by either
thread on its own).

## Contradictions / caveats

The (inferred) framing above stitches together two related notes
(what's-new-in-SE's hybrid summary and the HMA migration guidance); read both
source notes directly before treating this as a step-by-step migration runbook —
this page is an orientation summary, not a procedure.

## See also
- [[exchange-overview]]
- [[exchange-client-access-namespace]]
- [[exchange-implementation-review]]
- [[exchange-ad-dependency-migration-restore]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[exchange-exchange-servertoc-p0001-0040|Exchange Server — pages 1-40]]
- [[exchange-exchange-servertoc-p0641-0680|Exchange Server — pages 641-680]]
<!-- crosslink:end -->
