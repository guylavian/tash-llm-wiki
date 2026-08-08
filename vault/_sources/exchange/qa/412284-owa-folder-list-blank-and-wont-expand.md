---
title: "OWA folder list blank and won't expand"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/412284/owa-folder-list-blank-and-wont-expand
question_id: 412284
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# OWA folder list blank and won't expand

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/412284/owa-folder-list-blank-and-wont-expand (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have one user having a very strange issue in OWA.  (We are using Exchange 2010.)  When in OWA, all the user sees in the left hand pane is "Favorites" and their Display name.  The display name cannot be expanded to show the folders.  The mailbox loads just fine in Outlook.  We've tried multiple browsers, clearing cache, nothing seems to work.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-28*

Hi @Marg, Joe  ，    

As per your concern about the default Inbox permissions, as said by Andy, by default Inbox has the permission settings as follows:    

    

If reverting back these permissions doesn't work, I'd recommend try repairing this user's mailbox and see if it can help:    

```
New-MailboxRepairRequest -Mailbox ******@contoso.com -CorruptionType FolderView
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-27*

It's the user's Exchange mailbox, so they should have full access.   However you got me thinking about permissions and I noticed that the permissions on his Inbox are different than other users.  I'm wondering if this user attempted to tweak the permissions on his inbox and it messed everything up.  I know how to edit mailbox permissions within Exchange, but is there a way to reset folder permissions to whatever the default should be?    

Here are the perms on his Inbox...

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-27*

And the user has full access or delegated to a folder only? Can they access it by opening another mailbox in OWA?  

If all else remove the access and re-add it back
