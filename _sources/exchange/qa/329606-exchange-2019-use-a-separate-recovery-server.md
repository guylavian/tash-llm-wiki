---
title: "Exchange 2019 use a separate recovery server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/329606/exchange-2019-use-a-separate-recovery-server
question_id: 329606
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 use a separate recovery server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/329606/exchange-2019-use-a-separate-recovery-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

In our earlier Exchange environments, 2013 and backwards we have always set up an Exchange server for database and single items recovery. Those Exchange servers have not had the Client Access features installed and it has not been a part of the actual production environment. It has had only one purpose ant that was recovery for different reasons and we never installed the Client Access Features on it.  

In Exchange 2019 it doesn't seem to be possible to leave out or uninstall the client access features and the server accepts clients just because it is there which we do not like. We don't wont this server to signal to clients that it exists or to accept any Outlook, OWA or ActiveSync requests.  

Is this possible?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-24*

Thank you very much, you made my day :)  

Regards  

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-24*

Hi,  

Thank you for the answer. Just to see if I understand correctly.  

On the recovery server I will set the same URLs, like autodiscover.domain.com//autodiscover/autodiscover.xml and https://mail.domain.om/mapi etc, as the Production DAG servers which basically points to a Load Balancer.  

And because of that it will redirected from the recovery server if a clients wants to connect to it. Am I right or do I missunderstand something.  

Regards  

Michael
