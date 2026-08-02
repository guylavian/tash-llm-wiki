---
title: "GPO USB block but HDD.."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192596/gpo-usb-block-but-hdd
question_id: 2192596
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# GPO USB block but HDD..

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192596/gpo-usb-block-but-hdd (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I applied an AD GPO to block write access to removable drives, 

but on some PCs, the D: drive is also write-protected. Why is this happening?

The affected PCs are new hardware

while older PCs work correctly USB write access is blocked, but the D: drive is not affected.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-06*

Hello   

Thank you for posting in Microsoft Community forum.

1.Please check if the new PCs and the old PCs in the same container (such as the same OU).

2.Please check if the new PCs applied other GPO settings except blocking write access to removable drives.

3.Please check if the new PCs applied some setting about D: drive write-protected.

For checking Computer Configuration within gpresult, we can follow steps below.

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check gpo setting under "Computer Details".

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
