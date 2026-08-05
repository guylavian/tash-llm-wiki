---
title: "Can I migrate Domain Controller from server 2016 to server 2022 with same server name and IP?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1691241/can-i-migrate-domain-controller-from-server-2016-t
question_id: 1691241
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Can I migrate Domain Controller from server 2016 to server 2022 with same server name and IP?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1691241/can-i-migrate-domain-controller-from-server-2016-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI, I have 2 Server 2016 Domain Controllers. I will migrate to 2 new 2022 servers. Can I use same name and IP for new servers?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-05*

Hello,

 

Thank you for posting in Q&A forum.

Yes, of course. You will need to create new domain controller first.

Please rename your current DC and disallocate or change the IP address first. After that please assign the name and previous IP address to new DC.

Meanwhile, please make sure you have backuped all data on the DC to avoid any potential risk.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.
