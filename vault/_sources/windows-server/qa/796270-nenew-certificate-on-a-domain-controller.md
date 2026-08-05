---
title: "nenew certificate on a domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/796270/nenew-certificate-on-a-domain-controller
question_id: 796270
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# nenew certificate on a domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/796270/nenew-certificate-on-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

We use 3rd party certificate on all of your servers including domain controller. The certificates on the domain controllers are about to expire and we have renewed the certificate.   

Is there a process to import certificates on Domain controllers ? or its a simple as DC MMC -> certificate -> computer account -> Personal -> certificate -> Import ?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-04-01*

Hi,  

You should import the new certificate in same store as old certificate.  

It can be as you mentioned :   

```
MMC -> certificate -> computer account -> Personal -> certificate
```

Or   

```
MMC -> certificate -> services account--> Active Directory domainservices -> Personal -> certificate
```

Please don't forget to mark helpful reply as answer
