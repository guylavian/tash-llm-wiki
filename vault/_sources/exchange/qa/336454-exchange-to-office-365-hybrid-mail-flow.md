---
title: "Exchange to Office 365 - Hybrid mail flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/336454/exchange-to-office-365-hybrid-mail-flow
question_id: 336454
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange to Office 365 - Hybrid mail flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/336454/exchange-to-office-365-hybrid-mail-flow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have a problem sending an emails using the Outbound to office 365 connector in on-prem exchange . it is throwing an error when i am sending a email to office 365 mailbox which is migrated.  

error :  

Server at domain.mail.onmicrosoft.com (52.47.64.127) returned '451 4.4.397 Error communicating with target host. -> 421 4.2.1 Unable to connect -> SocketConnectionRefused: Socket error code 10061'  

Any idea, how can i resolve this.   

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-30*

Hi @pavan kumar   ,  

Can you successfully send mail to other external recipients?  

All user met this issue or only sepecific user meet?  

According to the research on error information:  

1.Is there a firewall? If so, please make sure that there is no firewall blocking access to the O365. Check the firewall to ensure that all ports required by Exchange are opened, especially 25 and 587. And there is no policy to prevent the necessary communication. If possible, please try to temporarily shut down.

2.Please following the steps to check the DNS loopups:  

Open the EAC -> Servers -> Servers -> Edit -> DNS lookups -> Make sure that already set up the DNS lookups.

3.Please make sure that the delivery, address space and source server of send connector are correct.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
