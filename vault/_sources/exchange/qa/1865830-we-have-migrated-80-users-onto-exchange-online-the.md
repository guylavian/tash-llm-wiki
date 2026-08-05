---
title: "We have migrated 80 users onto Exchange Online, the users have shared mailboxes, since the shared mailboaxes have automapped and various users have been added, seems alot of emails are getting stuck in the outbox ? if they have Send AS and Send on Behalf"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1865830/we-have-migrated-80-users-onto-exchange-online-the
question_id: 1865830
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# We have migrated 80 users onto Exchange Online, the users have shared mailboxes, since the shared mailboaxes have automapped and various users have been added, seems alot of emails are getting stuck in the outbox ? if they have Send AS and Send on Behalf

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1865830/we-have-migrated-80-users-onto-exchange-online-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have migrated 80 users onto Exchange Online, the users have shared mailboxes, since the shared mailboaxes have automapped and various users have been added, seems alot of emails are getting stuck in the outbox ? if they have Send AS and Send on Behalf AS. Users also have been deleagted rights.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-15*

Hi @Clinton Ivins  ,

Welcome to the Microsoft Q&A platform!

Based on your description, please let me confirm if your issue is that emails are getting stuck in outbox when the shared mailbox has automapped and those users have Send As and Send on behalf delegated right.

If so, please try to create a new Outlook profile for the user to see if it works. And please refer to Remove automapping for a shared mailbox - Outlook | Microsoft Learn to disabling auto-mapping and adding the shared mailboxes manually. Also, please make sure Outlook is running in online mode, not cached mode, to see if that resolves the issue.

If I misunderstand something wrong, please feel free to correct me. If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
