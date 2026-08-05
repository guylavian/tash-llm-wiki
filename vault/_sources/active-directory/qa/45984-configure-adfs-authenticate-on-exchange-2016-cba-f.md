---
title: "Configure ADFS authenticate on Exchange 2016 CBA for iPhone?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/45984/configure-adfs-authenticate-on-exchange-2016-cba-f
question_id: 45984
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Configure ADFS authenticate on Exchange 2016 CBA for iPhone?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/45984/configure-adfs-authenticate-on-exchange-2016-cba-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have build Exchange 2016 with ADFS for CBA.  

Install done and all function work fine.  

but Active Sync on iphone not work.  

Anybody have solution or experience this case?  

DC: Windows 2016  

Exchange: Windows 2016, Exchange 2016   

ADFS: Windows 2016 ADFS  

ETC: Windows 2016 Windows Reverse proxy server

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-18*

If you are using a reverse proxy (e.g., Microsoft Web Application Proxy) to publish Exchange services, ensure that it is correctly configured and forwarding requests to the Exchange server and ADFS.
