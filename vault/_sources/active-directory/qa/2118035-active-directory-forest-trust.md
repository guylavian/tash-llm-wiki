---
title: "Active Directory Forest Trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118035/active-directory-forest-trust
question_id: 2118035
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Forest Trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118035/active-directory-forest-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear team,

I wanted to know if it's possible to configure a 2-way trust between two Active Directory forest, one having the forest functional level 2008, and the other having the latest forest functional level 2025.

Regards,

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-12*

Hello Micheal Mallo,  

Thank you for posting in Q&A forum.

I think you can. Please follow the steps in the similar thread to set up conditional forwarders OR secondary zone.

https://learn.microsoft.com/en-us/answers/questions/61615/setup-of-trust-relationship-between-2-domains

After you create conditional forwarders OR secondary zone, then you can create forest trust based on the steps below.

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc780479(v=ws.10)?redirectedfrom=MSDN

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc740018(v=ws.10)?redirectedfrom=MSDN

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
