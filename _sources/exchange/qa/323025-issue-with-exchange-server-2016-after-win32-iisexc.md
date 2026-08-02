---
title: "Issue with Exchange Server 2016 after Win32/IISExchgSpawnCMD.A"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/323025/issue-with-exchange-server-2016-after-win32-iisexc
question_id: 323025
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
---
# Issue with Exchange Server 2016 after Win32/IISExchgSpawnCMD.A

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/323025/issue-with-exchange-server-2016-after-win32-iisexc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all, First, thanks in advance for reading my post, and I welcome any and all responses. Tolerance would be appreciated as this is very new to me but I am the only one available to try to get this problem corrected. On to the issue; our on-premises Exchange 2016 server was compromised and showed infection with several viruses. The most difficult to deal with was Win32/IISExchgSpawnCMD.A . I am confident that all traces of the viruses have been removed, but am still unable to get mail flowing to/from our server at this time. MS connectivity tool tells me that port 25 is blocked. I suspect there is a DNS issue - in looking through the log files /TransportRoles/Frontend/Connectivity I can see a clear demarcation between before and after. Before the server FQDN was giving a local address (10.0.0.x) and after it gives the public address (216.131.x.x). The hosts file has an entry for our local server, the NIC has the local server address as well (it is our internal DNS server). I am at a loss as to where to go to correct this problem. Can anyone offer tips on what/where to fix this problem? Dennis

## Answers

_No answers on this thread._
