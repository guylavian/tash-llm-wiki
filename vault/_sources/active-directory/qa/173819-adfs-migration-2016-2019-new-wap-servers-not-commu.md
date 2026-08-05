---
title: "ADFS Migration 2016 => 2019 - new WAP servers not communicating with new ADFS servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/173819/adfs-migration-2016-2019-new-wap-servers-not-commu
question_id: 173819
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# ADFS Migration 2016 => 2019 - new WAP servers not communicating with new ADFS servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/173819/adfs-migration-2016-2019-new-wap-servers-not-commu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have a problem with ADFS migration, especially the WAP servers are making problems.  

Current situation:  

ADFS-DB on SQL Server  

2* Windows Server 2016 with ADFS role (LB with KEMP)  

2* Windows Server 2016 with WAP role (LB with KEMP)  

New (so far):  

2* Windows Server 2019 with ADFS role (also in the ADFS farm, working fine)  

2* Windows Server 2019 with WAP role (this is where the problem starts)  

Initial WAP configuration was fine, when LB points internal still to 2016 ADFS servers.   

The communication of the new Sever 2019 WAP servers is problematic as soon as I point the internal load balancer to the new 2019 ADFS servers. After one minute errors 224 and 394 occurs and I am also not able to reestablish the trust.  

The federation server proxy configuration could not be updated with the latest configuration on the federation service.   

Additional Data   

Error:    

Retrieval of proxy configuration data from the Federation Server using trust certificate with thumbprint '<thumbprint>' failed with status code 'InternalServerError'.   

Summarized:  

New WAPs against old ADFS servers = Working  

Old WAPs against new ADFS servers = Working  

New WAPs against new ADFS servers = Broken  

Also tested it without KEMP LB, same results.  

I searched a lot and found solutions pointing to primary ADFS server but in this environment we have SQL DB so in my understanding there is no primary ADFS server.  

Any ideas? Any kind of hardening is not in place (SSL/TLS settings).  

Kind regards  

Patrick

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-26*

It seems token Decrypting certificate mismatch on ADFS.

Export Token-Decrypting cert from 2016 → Import + Set as Primary on 2019 ADFS

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-27*

Hello @Patrick-350  , possibilities are that the Kemp (LB) is a culprit or the proxy trust is broken. Does it work when bypassing the Kemp from WAP to ADFS?
