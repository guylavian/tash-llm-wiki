---
title: "Mail flow issue from exchange to Office 365 (exchange online)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/171780/mail-flow-issue-from-exchange-to-office-365-exchan
question_id: 171780
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Mail flow issue from exchange to Office 365 (exchange online)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/171780/mail-flow-issue-from-exchange-to-office-365-exchan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In our exchange environment, we have three mailbox server in MZ zone and Symantec Messaging Gateway (SMG) and PGP (for Encryption) as email security appliance. After enable exchange hybrid, we facing issue while sending mail from exchange to office 365 (exchange online). In our exchange server we allowed internet through proxy that's why we are unable to route mail from exchange to office 365 directly. So, we try to route through SMG but loop luck (Loop detected).     

Recently , we deploy Edge server to route mail from exchange to office 365 but always mail goes to SMG. mail not routing through EDGE.    

 Any Idea?    

Note: Others mail flow working as expected.    

Our mail flow diagram:    

    

Looking for help.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-24*

@Nur Hossain      

We don't know how the SMG works. Does there exist send connector on your Exchange server to send emails to that application? If so, try to remove that send connector. You need to prevent outgoing email through the left part, make all you outgoing email through Edge server rather than "Exchange on-premises → SMG →PGP → Internet"    

There only can exist Edge server between Exchange on-premises and Exchange online. So, if email through the left part, it will cannot send to Exchange online. You can try to add your application before the EOP, if they are supported.    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
