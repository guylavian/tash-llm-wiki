---
title: "non authoritative DFSR SYSVOL recovery moving from FRS to DFSR"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5768606/non-authoritative-dfsr-sysvol-recovery-moving-from
question_id: 5768606
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# non authoritative DFSR SYSVOL recovery moving from FRS to DFSR

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5768606/non-authoritative-dfsr-sysvol-recovery-moving-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

||
| -------- |
Migration has not yet reached a consistent state on all domain controllers. State information might be stale due to Active Directory Domain Services latency.

Migration has not yet reached a consistent state on all domain controllers. State information might be stale due to Active Directory Domain Services latency.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2026-02-10*

Hi Brian, 

Thank you for contacting Microsoft Q&A community. Please allow me to assist you on this:  

When migrating SYSVOL replication from FRS to DFSR, you may encounter a situation where migration does not reach a consistent state on all domain controllers, and the state information appears stale due to Active Directory Domain Services latency. This can result in domain controllers remaining stuck in the "Preparing" or "Start" phase, and event logs may show errors such as "DFSR Migration was unable to transition to the 'PREPARED' state" and "The process creation has been blocked".

To address this, ensure that Active Directory replication has fully converged across all domain controllers. You can force an immediate retry by executing the command `dfsrdiag /pollad` on all DCs. If the issue persists, check for access rights and sharing violations, as these can prevent DFSR from copying SYSVOL contents and transitioning states. Also, verify disk space availability and resolve any sharing violations reported in the event logs. 

Additionally, please help me provide the error message and detail background information if any.

If you believe this information adds some value, please accept the answer so that your experience with the issue would help contribute to the whole community.

T&R,

Kate.
