---
title: "ADFS 2012 to ADFS windows 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/560223/adfs-2012-to-adfs-windows-2019
question_id: 560223
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 2012 to ADFS windows 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/560223/adfs-2012-to-adfs-windows-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

Need some advise here.  

We have 2 ADFS Datacenter and each Datacenter as 3 ADFS Server, 3 ADFS proxy and 1 DB server.  

and we have around 10 RPT  

Now we are planning to upgrade to ADFS 2019.  

So how to upgrade without any major Downtime  

I mean how to use DB to the new ADFS 2019  

Do we have to backup DB and restore it windows server 2019, so that we get the same RPT without any break  

Please advise.  

Regards  

Aamir Masthan

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-13*

Do you mean ADFS on Windows Server 2012 or Windows Server 2012 R2. You can add Windows Server 2019 ADFS servers to an existing 2012 R2 farm following the same procedure as this: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server
