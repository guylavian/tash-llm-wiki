---
title: "Exchange 2019 System Mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/279145/exchange-2019-system-mailboxes
question_id: 279145
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 System Mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/279145/exchange-2019-system-mailboxes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to know about system mailboxes in multiple servers and databases scenario. And my question applies to exchange 2016/exchange 2019. First of all are the system mailboxes created (arbitration,monitoring etc.) per organization, per server or per database???  

 I mean if I have 5 exchange 2019 servers would system mailboxes be created only once when installing first server or would each server have some system mailboxes of its own?  

 Same question for databases. When we create a new database does each one create system mailboxes of its own? If we want o remove a database or uninstall a server what do we do with system mailboxes?  

 If we move them would that create duplicated or unnecessary mailboxes in remaining database/server?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-19*

Arbitration mailbox: Need to move before removing the database/server, can be created: Recreate missing arbitration mailboxes    

Check by the following command:    

```
Get-Mailbox -Arbitration | Fl Name, DisplayName, Database,Servername
```

Health mailbox(monirtoring mailbox): Don't need to move them, detailed information see here: https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-2013-2016-monitoring-mailboxes/ba-p/611004    

Check monitoring mailboxes associated with a specific server/database by the following command:    

```
Get-Mailbox -Monitoring | ?{$_.DisplayName -like "*-/-*"}| Fl Name, DisplayName, Database,Servername
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Still no one has answered the main question? Are system mailboxes at organization level or database or server level?  

AND if there are some at each level, then how to identify which of them is at which level? I.e. how to know which system mailbox is organization level and which database level...since both will be in the database.  

One would think that anything that appears more than once is not organization level but they all appear to be very similar in exchange 2019 so how to know?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Thanks for your response, is there any way I can identify the system mailboxes created by each database?  

How do I tell them apart?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-18*

The only mailboxes you need to move are the arbitration mailbox as they are organizational mailboxes.  

Any system and/or Monitoring mailboxes created by each database do not need to be moved as they are tied to that database and go away if the database is removed.   

Exchange will throw an error if you try to remove any database with an arbitration or user mailbox on it.  

https://blog.rmilne.ca/2018/03/19/arbitration-mailboxes-lay-of-the-land/  

https://blog.rmilne.ca/2016/09/15/when-to-move-arbitration-mailboxes/
