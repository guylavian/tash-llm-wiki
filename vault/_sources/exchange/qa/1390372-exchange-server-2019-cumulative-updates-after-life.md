---
title: "Exchange Server 2019 cumulative updates after lifecycle"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1390372/exchange-server-2019-cumulative-updates-after-life
question_id: 1390372
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Server 2019 cumulative updates after lifecycle

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1390372/exchange-server-2019-cumulative-updates-after-life (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

The primary end date for Exchange Server 2019 is January 9, 2024.

From this date onwards will Microsoft continue to release cumulative releases?.

Or we will have to think about switching to the new version when it is released in the second half of 2025.

Best regards.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-16*

Hi @Vicente Gallart | NUNSYS  ,

According to the Microsoft Lifecycle Policy, Exchange Server 2019 follows the Fixed Lifecycle Policy .Mainstream support for Exchange Server 2019 will end on January 9, 2024, and extended support will end on October 14, 2025.During the mainstream support phase, Microsoft provides security updates, non-security updates, and new features and functionality for Exchange Server 2019. During the extended support phase, Microsoft only provides security updates for Exchange Server 2019.

Therefore, after January 9, 2024, Microsoft will no longer release cumulative updates for Exchange Server 2019 that include non-security fixes or new features. If you want to keep your Exchange Server environment up to date and secure, as mentioned in the aforementioned blog by Andy, it’s suggested to always keep your current Exchange 2019 servers up-to-date, and then upgrade to the next version of Exchange Server when it is released in the second half of 2025.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-13*

You will need to think about moving to a new version:

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-roadmap-update/ba-p/3421389
