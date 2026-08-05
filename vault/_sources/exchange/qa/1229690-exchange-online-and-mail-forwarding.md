---
title: "Exchange Online and mail forwarding"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1229690/exchange-online-and-mail-forwarding
question_id: 1229690
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Online and mail forwarding

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1229690/exchange-online-and-mail-forwarding (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all.
I have a little question about mail forwarding. 
Scenario: i have a exchange online mailbox - for example ******@contoso1.com. Now I want register a new domain - for example contoso2.com - and then configure a simple mail forwading from ******@contoso2.com to ******@contoso1.com. So when an email is sent to ******@contoso2.com it must be forwarded/saved in the ******@contoso1.com mailbox.
Two questions:

-  do I need an Exchange Online license even if ******@contoso2.com is just an email address and not a real mailbox?

-  if the answer to the first question is no, how do I configure forwarding?
Thank's a lot :D

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-04-13*

Create ******@contoso.com as a shared mailbox ( No license required)
Set forwarding on the shared mailbox to go to ******@contoso1.com

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-15*

Thanks for the replies Andy and Rafael.
I thought it was much more complicated but it is much simpler. I tested both solutions and they work perfectly :D

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-14*

Hi @ Giuseppe Lucente ,  

You can follow these steps to set up forwarding:  

1.In ******@contoso2.com's mailbox, click the settings icon in the upper-right corner.

2.Click View all Outlook settings and go to Mail Rules.

3.Then add a rule to forward all messages to another mailbox.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
