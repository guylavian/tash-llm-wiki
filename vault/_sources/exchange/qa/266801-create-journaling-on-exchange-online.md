---
title: "Create Journaling on Exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/266801/create-journaling-on-exchange-online
question_id: 266801
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Create Journaling on Exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/266801/create-journaling-on-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I configure journaling on exchange online, but always get error :  "error  

The JournalEmailAddress can only be a mail user, a mail contact or an external address."  

Please tell me, how to fix?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-11*

You can’t use exchange on-line mailbox as journal mailbox. The Journal Email Address can only be a mail user, a mail contact or an external address. Normally, you can use any external mailboxes. There are no any special requirements.    

If you really want to use exchange online mailbox to receive these Journaling emails, the workaround is that you can forward all emails from the external mailbox to the Office 365 mailbox.    

Actually, use Office 365 mailboxes to receive Journaling emails has disobeyed the purpose of the Journaling feature. To better protect customer's profit, we don't recommend this method.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-10*

As the message suggests, you can only use external address, you cannot journal to any address within your Office 365 organization, or any other O365 organization for that matter. Read the documentation for more details: https://learn.microsoft.com/en-us/exchange/security-and-compliance/journaling/journaling#journaling-mailbox
