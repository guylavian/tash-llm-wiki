---
title: "Exchange Server 2019 - How to use new Greenlandic Timezone (UTC-2)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2154628/exchange-server-2019-how-to-use-new-greenlandic-ti
question_id: 2154628
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019 - How to use new Greenlandic Timezone (UTC-2)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2154628/exchange-server-2019-how-to-use-new-greenlandic-ti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are running Exchange Server 2019 patched to CU14 Nov24SUv2 on Windows Server 2019.

Windows Server has been updated with the patch for the new Greenlandic Timezone UTC-2  

https://techcommunity.microsoft.com/blog/dstblog/greenland-2023-time-zone-update-now-available/3937743

But in Exchange Server OWA, it still says (UTC-3) Greenland

How do We get the new Greenlandic Timezone in Exchange Server 2019?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-06*

Hello, @Jesper Rex Andersen,

Welcome to the Microsoft Q&A platform!

This issue stems from the fact that Exchange Server (including OWA) doesn’t automatically “pick up” changes made to the Windows time zone definitions. Although your Windows Server 2019 now knows about Greenland’s new offset (UTC‑2), Exchange has its own bundled and cached time zone data that was compiled into your CU (in your case, CU14) and isn’t updated simply by the underlying OS patch. 

In other words, Exchange uses its internal time zone “database” (hard‐coded in files and DLLs) to build the OWA time zone list. That data was set when your CU was released and does not automatically refresh when Microsoft updates the Windows time zones. Microsoft is aware of these kinds of discrepancies—when an OS update modifies a time zone (like Greenland from UTC‑3 to UTC‑2), Exchange’s own definitions remain unchanged until they are updated in a future CU.

Below is what you can do to try to resolve your issue:

Officially, Microsoft must ship an updated CU (or a hotfix) for Exchange 2019 that incorporates the new Greenland time zone definitions. In the meantime, you may want to check Microsoft’s release notes and announcements to see when a fix is expected. 

As a workaround, while not supported or recommended for production, some administrators have attempted to manually update the Exchange time zone definitions by modifying the XML/js files or registry settings that OWA uses. However, this is not documented or supported by Microsoft and may cause unforeseen issues. 

The recommended course of action is to monitor Microsoft’s Exchange updates and plan an upgrade (or apply a CU when available) that contains the updated time zone information.

For information on Exchange updates, please refer to Updates for Exchange Server, Cumulative Updates for Exchange Server, Exchange Server 2016 CU, Cumulative Update Exchange 2016 | Microsoft Learn.

Should you need more help on this, you can feel free to post back. 

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
