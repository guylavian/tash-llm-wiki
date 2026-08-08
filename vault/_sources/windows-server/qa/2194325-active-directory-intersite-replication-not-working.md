---
title: "active directory intersite replication not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194325/active-directory-intersite-replication-not-working
question_id: 2194325
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# active directory intersite replication not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194325/active-directory-intersite-replication-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi

i have many sites where replication working fine. recently added new site name xyz and ad\domain controller configure. some how new computer or user created on new ad its not replicating other sites. if we configure new object other server its replicating to new site new ad.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-26*

Hello satyamahapatra1，  

Thank you for posting in Microsoft Community forum.

Please check AD replication in the forest by running commands below on the PDC.

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt  

repadmin /showrepl * /csv >c:\repsum.csv

Check the results of these commands.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
