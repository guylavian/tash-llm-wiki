---
title: "Kerberos encryption types - an account persists in using RC4"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/50334/kerberos-encryption-types-an-account-persists-in-u
question_id: 50334
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-sql-virtual-machines", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Kerberos encryption types - an account persists in using RC4

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/50334/kerberos-encryption-types-an-account-persists-in-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I enabled RC4, AES128 and AES256 across all enabled computers and users in a domain/forest and now all tickets are encrypted with AES256, except those issued for SQL access. SQL 2016 servers run on Windows 2019 and SQL compatibility level is set to 130. I tried disabling RC4 for accounts running SQL service and SQL reporting service, but the end users kept receiving RC4 tickets and connecting successfully. When I disabled RC4 for the SQL computer, the end users were unable to connect to the SQL server.  

Is there something in SQL that needs to be configured for AES to be used for Kerberos ticket encryption?  

Thanks  

Zoran

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-26*

Hi,  

First and foremost, if the server and the computers are in different domain, this behavior is expected as trust by default supports RC4.  

If that is the case, you may need to enable AES from trust properties.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-07-22*

I did some more testing and managed to eliminate SQL as a possible cause. I created a new gMSA account, registered SQL SPN and used it to run SQL service and SQL agent on a test server. Now when I restricted both gMSA and the server account to AES256, it still worked. So it seems it's something with the old SQL service account which has been around probably since Windows 2000, but it's not the only one from that time, but it's the only one causing this issue.   

Replacing this account across the domain is a bit tricky as it has 1000+ SPNs registered, configured Kerberos delegation for dozens of apps etc, so preferred way would be to fix it at this stage.  

Is there something in the account's setting that could prevent it from using AES for Kerberos encryption?  

Thanks
