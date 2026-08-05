---
title: "Exchange Server 2019 IN azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/215067/exchange-server-2019-in-azure
question_id: 215067
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2019 IN azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/215067/exchange-server-2019-in-azure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,  

How to calculate an azure VM pricing with Exchange Server 2019?  

do I need an extra license for Exchange Server 2019?  

https://azure.microsoft.com/en-us/pricing

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-01*

@IKRAMUL ISLAM CHOWDHURY  

How to calculate an azure VM pricing with Exchange Server 2019?

Here is the hardware requirements for Exchange 2019, you could use those information to create/buy a suitable virtual machine based on your needs. About Memory, 8G could let Mailbox server running, but to ensure that the server runs smoothly, you need to allocate 128G of memory for it as suggested in that article.

If you want to deploy a complex environment, those two articles could help you calculate the hardware requirements for your VM:

-  https://techcommunity.microsoft.com/t5/exchange-team-blog/announcing-the-exchange-server-2019-sizing-calculator/ba-p/644180

-  https://www.microsoft.com/en-us/download/details.aspx?id=102123

do I need an extra license for Exchange Server 2019?

Yes, you need to buy license for Exchange 2019. The Azure VM is just a VM deployed in the cloud, it doesn't effect the using of Exchange 2019. Deploy Exchange in Azure VM is same to install it on your local AD. You need to buy license for your Exchange server.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
