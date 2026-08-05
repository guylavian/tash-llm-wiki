---
title: "Lost connectivity between Exchange 2013 on prem and Office 365 in a hybrid environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187616/lost-connectivity-between-exchange-2013-on-prem-an
question_id: 1187616
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Lost connectivity between Exchange 2013 on prem and Office 365 in a hybrid environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187616/lost-connectivity-between-exchange-2013-on-prem-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So we went Hybrid about 3 or 4 years ago, but the client is slow to move, and then the pandemic hit and everything came to a standstill.  They are hybrid, but except for a couple of mailboxes in the cloud (which I migrated when testing, everything, including mail flow, was working), they are fully on prem for everything still.  We are planning our migration now.  But for the last few years, when I had to renew my Exchange certificates, I only had an issue the first time, forgetting that the mail flow connectors to 365 need the certificate updated.  There was no mail flow between on prem and the cloud and I was receiving STARTTLS errors on my on prem server.  After updating the certificate (setting the new cert for SMTP and rerunning the HCW), I had no more issues.  Every year after, I had no issues.  Last year came, and ever since I updated the certificate, I have had no mail flow.  I have no new errors on my exchange server.  I had a ticket with Office 365, and they said it was an on prem issue.  I reran the hybrid configuration wizard and recreated the connectors, still no luck.  I'm at somewhat of a loss right now.  Any help would be greatly appreciated.  Below are some of the articles I have used for troubleshooting (among many others), all have either not helped, or any tests I was told to perform resulted in no issues discovered.  Everything looks fine.

 

https://answers.microsoft.com/en-us/msoffice/forum/all/451440-tls-negotiation-failed/b000a553-fbf8-43d5-93ed-b721f25a6b2d

 

https://learn.microsoft.com/en-US/exchange/troubleshoot/email-delivery/cannot-receive-mail-with-new-certificate If I remember correctly, this is what I did to fix my initial STARTTLS error

 

Also, this is the exact message I have when I run a message trace in exchange online, for mail that does not get delivered to my on prem server through the hybrid connectors from one of our cloud mailboxes to an on prem mailbox:

 

Reason: [{LED=450 4.4.317 Cannot connect to remote server [Message=451 4.4.0 TLS negotiation failed with error SocketError] [LastAttemptedServerName=xxx] [LastAttemptedIP=xxx] [SmtpSecurity=-2;-2] [DM6NAM12FT012.eop-nam12.prod.protection.outlook.com 2023-03-07T18:46:06.378Z 08DB1DF24DB12D84]};{MSG=4. OutboundProxyTargetIP: xxx. OutboundProxyTargetHostName: xxx

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-08*

Are the hybrid Exchange Servers forcing TLS 1.2? They need to be:

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-1-getting-ready-for-tls-1-2/ba-p/607649
