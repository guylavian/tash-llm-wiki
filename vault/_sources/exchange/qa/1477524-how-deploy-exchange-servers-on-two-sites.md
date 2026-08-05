---
title: "How deploy exchange servers on two sites?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1477524/how-deploy-exchange-servers-on-two-sites
question_id: 1477524
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# How deploy exchange servers on two sites?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1477524/how-deploy-exchange-servers-on-two-sites (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We plan to deploy four Exchange servers 2019 at two sites in a forest domain，two servers per site.Each site has independent firewalls and Spam gateway,Each site has its own internet access，two sites connected via SDWAN.

Each site has some clients and users。Now we hope that the client can send and receive emails through the exchange server on their respective site,and Email needs to be saved on all exchange servers。I have deployed a DAG that includes all servers，what should I do next? 

Thanks all！！

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-05*

Hi @Frankie Wu  

It is the expected behavior that clients will query the Active Directory and first try to connect to the Exchange server located in the same site.

For more details please refer to this documentation: How Exchange accesses information in Active Directory

Now we hope that the client can send and receive emails through the exchange server on their respective site,and Email needs to be saved on all exchange servers。

You can create databases on the corresponding Exchange server for users in that site, then add database copies to the other Exchange server in the other site, which provides high availability for you.

For sending emails, please create a send connector and add both servers as source servers.

For receiving emails, if the purpose is to have both servers receive emails directly from external, to me it is not possible without a load balancer.

Without load balancer, the external messages will first be sent to the server which your public MX record points to, then be routed to where the mailbox is hosted (on this server or be routed to the other server).

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
