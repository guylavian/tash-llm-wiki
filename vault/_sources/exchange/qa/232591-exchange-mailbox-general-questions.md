---
title: "Exchange mailbox general questions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/232591/exchange-mailbox-general-questions
question_id: 232591
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange mailbox general questions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/232591/exchange-mailbox-general-questions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

Q1: Does the mailbox always reside in the same Database after mailbox is disabled? I mean mailbox database before disabling the mailbox and after disabling the mailbox is always same?  

Q2: What is the meaning of OriginatingServer property in both powershell cmdles?  

Get-mailboxdatabase and Get-mailboxstatistics  

Please answer and explain specific to above mentioned questions with Microsoft support articles.  

Thanks in advance!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-18*

Hi @G-ONE  ,    

Q1: Does the mailbox always reside in the same Database after mailbox is disabled? I mean mailbox database before disabling the mailbox and after disabling the mailbox is always same?    

Yes. According to the official article below, "When a mailbox is disabled or deleted, Exchange retains the mailbox in the mailbox database and switches the mailbox to a disabled state. " This indicates the mailbox is reside in the same database after it's disabled.    

Disable or delete a mailbox    

Q2: What is the meaning of OriginatingServer property in both powershell cmdles?    

Get-mailboxdatabase and Get-mailboxstatistics    

Agree with Andy that the OriginatingServer property tells which server or dc the data is retrieved. I tried to search a lot but so far cannot find an official document stating it. Below is a relevant thread for your reference:    

How come my Exchange Server OriginatingServer (GC) change by itself ?    

The “OriginatingServer” property indicates which DC the data is read from and is used primarily for troubleshooting. It is updated with each AD call so that it could change during different runs of “get-” cmdlets    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
