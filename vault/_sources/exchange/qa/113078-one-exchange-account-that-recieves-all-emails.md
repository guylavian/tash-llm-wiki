---
title: "One Exchange Account that Recieves All Emails?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/113078/one-exchange-account-that-recieves-all-emails
question_id: 113078
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# One Exchange Account that Recieves All Emails?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/113078/one-exchange-account-that-recieves-all-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Team- a consultant once set up and Exchange email account that all other emails in the domain forward to- kind of a catch-all account that all emails go to.  It's an extremely time-efficient way to grab lost emails, or show that certain emails were indeed sent, etc.  Does anyone know how to set this up?

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-01*

@Scott Mohr       

What about configuring the journaling? It can be used to record all or targeted email messages.    

There are two journaling options:    

-  Standard journaling: Journal all messages that are sent to and received by mailboxes on a specific mailbox database. To journal all messages in your organization, you need to configure journaling on all mailbox databases on all Exchange servers.    

-  Premium journaling: Use journal rules to journal messages based on recipients (all recipients or specified recipients), and scope (internal messages, external messages, or all messages).     

You can check this for more details: Journaling in Exchange Server.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-30*

A Catch-all mailbox is generally used for catching messages that aren't sent to a real or valid user:    

https://www.techieshelp.com/create-a-catch-all-mailbox-in-exchange-2013/#:~:text=So%20what%20is%20a%20%E2%80%9CCatch,exist%20in%20your%20Exchange%20organization.    

If you want ALL messages then:    

A mailflow rule will do that    

Create a mailbox ( and set the quota to a large value)    

 and BCC all messages to it.    

Adjust as necessary
