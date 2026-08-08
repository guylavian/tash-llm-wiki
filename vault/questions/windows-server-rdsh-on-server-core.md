---
title: "Can we run the RD Session Host role on a Server Core install to shrink our terminal server's attack surface?"
type: question
question_tier: conceptual
domain: windows-server
slug: windows-server-rdsh-on-server-core
summary: No — the RD Session Host role service is not included in the Server Core installation option (only RD Connection Broker, RD Licensing, and RD Virtualization Host are); a session-based RDS deployment needs Server with Desktop Experience, though the other RDS roles (Broker/Gateway/Web Access/Licensing) can still run on Server Core.
sources:
  - kb:administration-server-core-roles-and-services
  - kb:administration-what-is-server-core
  - kb:remote-rds-roles
provenance:
  extracted: 6
  inferred: 1
  ambiguous: 0
tags: [win-administration, remote-services]
status: draft
updated: 2026-07-23
graph_community: "Windows Server — Overview"
---

# Can we run the RD Session Host role on a Server Core install to shrink our terminal server's attack surface?

**No. The Server Core installation option's Remote Desktop Services role
explicitly does not include the RD Session Host role service — only RD
Connection Broker, RD Licensing, and RD Virtualization Host are listed as
available.**

## Body

The Server Core roles/role-services reference table lists, under **Remote Desktop
Services**: "Remote Desktop Connection Broker," "Remote Desktop Licensing," and
"Remote Desktop Virtualization Host" as the role services included
(`reference/windows-server/administration-server-core-roles-and-services.md:78-80`).
**RD Session Host is not in that list.** The article is explicit that this
omission is intentional and searchable: "if you search for **Remote Desktop
Session Host**, you won't find it on this page. That's because the RD Session
Host is **not** included in the Server Core image"
(`reference/windows-server/administration-server-core-roles-and-services.md:19`).

### Why this tracks with Server Core's design intent

The parent "What is Server Core?" article frames Server Core's target use case as
roles that don't need a GUI: "a Hyper-V server doesn't need a graphical user
interface (GUI), because you can manage virtually all aspects of Hyper-V either
from the command line... or remotely" (`reference/windows-server/administration-what-is-server-core.md:23`).
RD Session Host is the opposite case — its entire purpose is hosting **interactive,
GUI-based** desktop/app sessions for end users, so excluding it from a
no-desktop-shell image is consistent with why Server Core exists **(inferred** —
the source doesn't state the Session Host exclusion's rationale directly, but this
follows from the stated design principle applied to the one role whose function
*is* the GUI).

### What was asked vs. the actual correct approach

The premise — "run RD Session Host on Server Core for a smaller attack surface" —
isn't achievable as stated, because the role service simply isn't installable
there. But the goal (hardening a Remote Desktop deployment) doesn't require giving
it up entirely:

- Deploy the **RD Session Host** on **Server with Desktop Experience** (the only
  supported option for that specific role service), and apply ordinary hardening
  there (patch cadence via [[wsus]] or [[windows-admin-center]], restricted
  application allowlisting, RDP hardening).
- The **other** RDS roles that front the session hosts — **RD Connection Broker**,
  **RD Licensing**, and **RD Virtualization Host** — *can* run on Server Core today,
  shrinking the attack surface of the roles that don't strictly need a GUI, per
  the same role-service table
  (`reference/windows-server/administration-server-core-roles-and-services.md:78-80`).
  Note the table's own footnote: RD Connection Broker "is no longer available in
  Windows Server Core starting with Windows Server 2019, version 1803"
  (`reference/windows-server/administration-server-core-roles-and-services.md:135`)
  — confirm current-version availability before relying on this for a specific
  Windows Server release.
- Independent of install option, [[remote-desktop-services]]'s own hardening
  guidance still applies: install CA-issued (not self-signed) certificates on
  RD Gateway / RD Web Access / RD Connection Broker before going to production.

## Contradictions / caveats

The RD Connection Broker Server Core availability changed across versions (removed
starting Windows Server 2019 version 1803, per the footnote above) — verify against
the specific target OS version before planning a Server-Core-hosted broker/licensing
tier.

## See also
- [[server-core]]
- [[remote-desktop-services]]
- [[windows-server-implementation-review]]

## References

**RH ground-truth — n/a (Microsoft Learn corpus, not Red Hat)**

**Microsoft Learn reference tier (`kb:`)**
- `kb:administration-server-core-roles-and-services` — "Roles, Role Services, and Features included in Windows Server - Server Core"
- `kb:administration-what-is-server-core` — "What is Server Core?"
- `kb:remote-rds-roles` — "Remote Desktop Services roles"

**Wiki**
- [[server-core]]
- [[remote-desktop-services]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[administration-server-core-roles-and-services|Roles, Role Services, and Features included in Windows Server]]
- [[administration-what-is-server-core|What is Server Core?]]
- [[remote-rds-roles|Remote Desktop Services roles]]
<!-- crosslink:end -->
