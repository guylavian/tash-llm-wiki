---
title: "Exchange Server 2019 installation (Mailbox servers and Edge Transport Servers)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1184472/exchange-server-2019-installation-mailbox-servers
question_id: 1184472
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange Server 2019 installation (Mailbox servers and Edge Transport Servers)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1184472/exchange-server-2019-installation-mailbox-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 5 mailbox servers  and 3 edge transport servers installed in our environment ( Exchange 2019 and Windows server 2019). After installed, we run the Get-ExchangeServer command, on any Mailbox servers, we can get all 5 Mailbox servers with no Edge Transport servers. On any Edge Transport Servers, we only get the Edge Transport Server itself, with no Mailbox Servers. Above outcomes were not normal.

We'd like to see the edge transport servers can be listed via running the Get-ExchangeServer command from any mailbox server, and vice versa. Any suggestions are appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-28*

Thank you @Aholic Liang-MSFT  

We finnally fix it via having the Edge Subscription. 

Do you have any ideas about this problem: access to ECP/OWA failed with the error "http 500 internal server error"? 

 And If didn't prepare AD before install Exhange Server which was the cause? You know we have two sites under one root domain to deploy Exchange servers, and site 1 had prepared AD, so we didn't prepare AD when install Exchange server in site 2. Because of we use the same deploy account.
