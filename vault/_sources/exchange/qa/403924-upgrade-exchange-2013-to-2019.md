---
title: "Upgrade exchange 2013 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/403924/upgrade-exchange-2013-to-2019
question_id: 403924
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Upgrade exchange 2013 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/403924/upgrade-exchange-2013-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, i have a exchange 2013 DAG and want to install a Exchange 2019 DAG next to thev2013 DAG, but have Some clients with Outlook 2010. I,am gonna leave the autodiscover to Exchange 2013 and also the mailboxes of these 2010 clients. The rest of the mailboxes i will move them to the 2019 environment. Then i will upgrade the 2010 clients and move these mailboxes and at the end i set autodiscover to Exchange 2019.  

Is this scenario gonna work?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-24*

Hi @Marco Buyn       

In my opinion, it should work fine for you.    

According to this link: What's new when upgrading from Exchange 2013 to Exchange 2019?    

Exchange 2013 can proxy the requests to Exchange 2019.    

    

As far as the autodiscover SCP and DNS records are configured to point to the Exchange 2013 server, the Outlook clients should be able to connect.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
