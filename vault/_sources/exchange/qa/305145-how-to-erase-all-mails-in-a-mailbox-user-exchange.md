---
title: "How to erase all mails in a mailbox user - exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305145/how-to-erase-all-mails-in-a-mailbox-user-exchange
question_id: 305145
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to erase all mails in a mailbox user - exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305145/how-to-erase-all-mails-in-a-mailbox-user-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We need erase all the mails in a mail account in exchange online , office365 . Without erase or delete the user because the OneDrive information not need erase

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

@ManuelMiranda-6129    

Make sure your account have "Mailbox Search" and "Mailbox Import Export" permission.    

    

Then connect to Exchange online with PowerShell.    

Then you will could use command below to check how many emails in this mailbox:    

```
Search-Mailbox YourMailbox -EstimateResultOnly
```

    

Then, use command below to delete emails from the mailbox that you want:    

```
Search-Mailbox YourMailbox -DeleteContent
```

I tested in my lab, it take a long time to delete those emails.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-09*

Just remove the Exchange Online license/service plan from the user. This will "disconnect" the mailbox and delete it together with all content after 30 days or so.    

Alternatively you can use the Search-Mailbox cmdlet with the -DeleteContent switch to achieve this. but I'd caution against using this approach unless you're confident in your PowerShell skills - a simple error can cause data to be deleted across all mailboxes in your tenant. Here's the cmdlet help just in case: https://learn.microsoft.com/en-us/powershell/module/exchange/search-mailbox?view=exchange-ps
