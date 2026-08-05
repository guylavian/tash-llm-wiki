---
title: "Windows Server 2012 R2 ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/85750/windows-server-2012-r2-adfs
question_id: 85750
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Windows Server 2012 R2 ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/85750/windows-server-2012-r2-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have installed Windows 2012 R2 server and installed ADFS. When I attempt to access https://fqdn/federationmetadata/2007-06/federationmetadata.xml I get the cannot access check TLS 1.0, 1.1, 1.2 settings. When I use https://localhost/federationmetadata/2007-06/federationmetadata.xml I can see the xml data.  

I have tried everything I can find using Google with no luck. The only thing we haven't tried is a SSL certificate with wildcard entries.  

Please help.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

We have workshops to help move off ADFS https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480 & https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
