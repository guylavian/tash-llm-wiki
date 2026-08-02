---
title: "Workstations joining Secondary Domain Controller but not Primary Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/602511/workstations-joining-secondary-domain-controller-b
question_id: 602511
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Workstations joining Secondary Domain Controller but not Primary Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/602511/workstations-joining-secondary-domain-controller-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. We have a situation where the replication between 2 domain controllers are amiss. (Primary and Secondary)  

We then first remove the alternative dns pointing to secondary domain controllers but whenever we rejoin any workstation/servers they are still appearing on the secondary domain controller.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-25*

Hi @Christian James Chu       

The newly created computer object should replicate to the other DC, this is expected behaviour, can you explain what you think the problem is?    

You can run the following command to give you a quick view of the health of the AD replication    

```
repadmin /replsummary
```

Gary.
