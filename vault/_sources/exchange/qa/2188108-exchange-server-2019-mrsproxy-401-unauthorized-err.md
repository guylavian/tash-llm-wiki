---
title: "Exchange Server 2019 mrsProxy 401 UnAuthorized Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188108/exchange-server-2019-mrsproxy-401-unauthorized-err
question_id: 2188108
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-server", "windows-business-windows-server-user-experience-session-connectivity"]
---
# Exchange Server 2019 mrsProxy 401 UnAuthorized Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188108/exchange-server-2019-mrsproxy-401-unauthorized-err (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

I am trying to migrate from an exchange server 2019 on prem server to exchange online. However I keep getting the 401 unauthorized error. I get it at every point. If i do HCW i get it, test migration availability, setup migration endpoint in m365. Also to note I am using Mimecast as my email gateway. Also get same error from BitTitan's MigrationWiz. 

Settings that are set:

MRS Proxy Enabled

Basic / Windows authentication Enabled

Credentials are correct for accounts

Enhanced Protection Disabled

Account has Organization Management and Impersonation.

Here is the error i get with the Hybrid Configuration Wizard. Similar error received when doing other migration attemtpts. 

"HCW8078 - Migration Endpoint could not be created.  

Microsoft.Exchange.Net.CommunicationErrorTransientException  

The call to 'net.tcp://ds0pr14mb5616.namprd14.prod.outlook.com:9821/Microsoft.Exchange.MailboxReplicationService DS0PR14MB5616.namprd14.prod.outlook.com (15.20.8026.17 ServerCaps:FFFFFFFF, ProxyCaps:1FFFFFFFFFFFFFFFC7DD2DFDBF5FFFFFCB07EFFF, MailboxCaps:, legacyCaps:FFFFFFFF)' failed. Error details: The Mailbox Replication Service was unable to connect to the remote server using the credentials provided. Please check the credentials and try again. The call to 'https://mail.domain.com/EWS/mrsproxy.svc' failed. Error details: The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Basic realm="mail.domain.com"'. --> The remote server returned an error: (401) Unauthorized.. --> The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Basic realm="mail.domain.com"'. --> The remote server returned an error: (401) Unauthorized.."

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-19*

Thank you Jacen, 

I have psoted the same question to: Exchange Server 2019 mrsProxy 401 UnAuthorized Error (Trying to Migrate to Exchange Online) - Microsoft Q&A

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-19*

Hello，

Thank you for posting in the Microsoft Community forum.

I understand that your question is related to Exchange Server. Given the technical nature of your inquiry, I recommend redirecting your question to our specialized forum dedicated to this topic:

Exchange Server - Microsoft Q&A

Thank you for your understanding and cooperation.

Best regards

Jacen
