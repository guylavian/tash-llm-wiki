---
title: "Can one ADFS proxy associate with multiple ADFS server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/57750/can-one-adfs-proxy-associate-with-multiple-adfs-se
question_id: 57750
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Can one ADFS proxy associate with multiple ADFS server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/57750/can-one-adfs-proxy-associate-with-multiple-adfs-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I need to upgrade ADFS from windows 2008 R2 to Windows 2019. We have 10+ Relying party trust on the old ADFS. To minimize the impact, I plan to prepare a new ADFS so I can migrate them one by one to reduce the down time. Below are my questions.  

-  To direct the authentication to the new ADFS server, I need to register a new DNS name. Is it correct?  

-  We have one ADFS proxy on DMZ. Can one ADFS proxy to redirect the authentication to different ADFS server or do I have to create another ADFS proxy?  

If this isn't a right way to migrate Relying party trust, please advise the best way.  

Thanks in advance!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-03*

One WAP server can only use one ADFS farm.    

Is your ADFS on Windows Server 2008 R2 a farm deployment or a stand alone deployment?    

If that's a farm deployment, you can actually do a parallel run upgrade. It is the same process as in: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn486815(v=ws.11)    

If that's a stand alone deployment, you will have do an actual migration. In that case you will need to bring a new infra with WAP and ADFS. And if the challenge is that you just have one public IP for the WAP, you could in theory publish the new WAP in a pass-through rule on the old WAP. DNS will have to follow, it will also break certificate based authentication (just in case you are using it).
