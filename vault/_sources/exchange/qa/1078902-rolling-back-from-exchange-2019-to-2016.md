---
title: "Rolling back from Exchange 2019 to 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1078902/rolling-back-from-exchange-2019-to-2016
question_id: 1078902
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Rolling back from Exchange 2019 to 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1078902/rolling-back-from-exchange-2019-to-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

a customer of us has installed a new Exchange 2019 DAG Cluster in a existing Exchange 2013 DAG cluster environment.     

While testing we saw that they use an important Tool which is not working together with Exchange 2019.     

At the moment there are only test Mailboxes in the 2019 databases.    

Is it possible to uninstall the Exchange 2019 Servers and afterwards install Exchange 2016 DAG Cluster?     

In the installation process of the first Exchange 2019 server there was a warning, that it is not possible to install Exchange 2016 afterwards (but i can't rember exactly)    

Thankyou in Advance and kind regards Boris

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-08*

Hello,    

just to be sure:    

At the moment all productive mailboxes are still on the Exchange 2013 Cluster.    

And there was no Exchange 2016 server installed before Exchange 2019    

I thought, that new Exchange 2019 attributes for the mailboxes will added after migration? And after that no rollback is possible.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-08*

Hi @Birneder, Boris  ,    

Are you directly from Exchange 2013 to 2019 bypassing 2016?    

If so, then agree with Andy.     

Therefore, for "Is it possible to uninstall the Exchange 2019 Servers and afterwards install Exchange 2016 DAG Cluster?", I am sorry to tell you that this is not possible.    

About rolling back from Exchange 2019 in an Exchange 2013 and Exchange 2019 co-existence environment, please refer to this article: Rolling back from Exchange 2019 - Microsoft Community Hub    

In this article, to avoid more unknown issues, Exchange 2016 was not introduced, but migrated to Exchange Online.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-07*

If you went straight from 2013 to 2019 and there were no existing 2016 servers, then no, you can't now install 2016 servers into the AD Forest once you ran the 2019 PrepareAD step.
