---
title: "Exchange 2019 - acting as hybrid only- disable information store service ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289771/exchange-2019-acting-as-hybrid-only-disable-inform
question_id: 1289771
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 - acting as hybrid only- disable information store service ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289771/exchange-2019-acting-as-hybrid-only-disable-inform (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

Moving an org from on-prem to online we will be keeping 2 x 2019 servers on prem for SMTP relay and recipient management in a hybrid config.

Given that 0 mailboxes are expected to be on prem, what is the impact, if any, of disabling the information store service ? While there are obviously no mailboxes to service, i cant seem to find any official guidance on this scenario.... as to if disabling IS will have other unforeseen impacts - and the support status of it.

any comments - or links to MS articles on this would be great - but my googleFu could not find any.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-24*

Have recently started piloting an "transport and management only" mode of an Exchange Server '19 Mailbox Role with all databases deleted and information store service deactivated.  

My first impression is that I have only left the Exchange Management Shell. Am refused by /ecp with HTTP500.  

Seems to be what Microsoft expects from that state. Both conditions listed under cause are true for me:  

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/http-500-error-during-eac-sign-in

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-02*

If you want to use admin audit logging on those mgmt servers ( I assume you do!), then you will need to leave the databases mounted and the IS service running since those log entries are stored in an arbitration mailbox. 

https://learn.microsoft.com/en-us/exchange/policy-and-compliance/admin-audit-logging/admin-audit-logging?view=exchserver-2019

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-24*

Hi @Ben Wosjke  ,

Given that 0 mailboxes are expected to be on prem, what is the impact, if any, of disabling the information store service ?

I've also tried searching a lot but cannot find any official document explicitly stating the impact on this scenario. But based on my understanding, since on-prem has no mailboxes at all, it won't have any impact.

From the article below, we can learn that Microsoft Exchange Information Store is used to manage the mailbox databases on the server. "If this service is stopped, mailbox databases on the server are unavailable." And according to the "Dependencies" field of the table, there's no other service that depends on the Information Store Service, which means disabling MSExchangeIS won't affect other Exchange services on the server.  

Overview of Exchange services on Exchange servers  

As regards to SMTP relay, as mentioned above, MSExchangeIS is used to manage mailbox databases, so it won't affect the mail flow given 0 mailbox is on prem. I tried testing in my on-prem environment as well using telnet and as can be seen from the message tracking log, storedrive is not involved for the sender side:  

(The STOREDRIVER in the last line is because the recipient's mailbox is hosted on the on-prem server.)  

When it comes to recipient management, actually you can manage recipients even if the Exchange sever is shut down. More details, you may refer to the document below:  

Manage recipients in Exchange Hybrid environments using Management tools

Taken in the round, personally I don't think disabling MSExchangeIS will do any harm to your current environment. But to be on the safe side, you can start by testing it in non-working hours.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
