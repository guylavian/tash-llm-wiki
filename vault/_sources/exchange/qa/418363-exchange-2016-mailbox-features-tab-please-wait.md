---
title: "Exchange 2016 Mailbox Features tab please wait"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/418363/exchange-2016-mailbox-features-tab-please-wait
question_id: 418363
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Mailbox Features tab please wait

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/418363/exchange-2016-mailbox-features-tab-please-wait (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I access certain user mailbox's mailbox features, i get please wait sometimes up to 15-20 minutes before it'll show up.   Most users show up within 5-10 seconds.  I don't see any errors in eventlogs.  Any idea where I could hunt down the issue?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-06-02*

I suspect its because they are remote. If the powershell commands to view these mailboxes are quick enough, I would use that instead for those accounts

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-02*

Hi @John Tsai  

If the issue only happens on a certain mailbox, I would recommend recreating the mailbox for the user to see if it works for you.

Below are the steps:  

1.export the mailbox to a PST file via EAC or Outlook

EAC: Procedures for mailbox exports to .pst files in Exchange Server

Outlook: Back up your email

2.disable the mailbox  

EAC:  

  

EMS:  

run the following command:

```
Disable-Mailbox -identity 
```

3.create a new mailbox for the user  

EAC:  

EMS:  

run the following command:

```
Enable-Mailbox -Identity 
```

4.import the PST file to the mailbox via EAC or Outlook

EAC: Procedures for mailbox imports from .pst files in Exchange Server

Outlook: Import email, contacts, and calendar from an Outlook .pst file

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
