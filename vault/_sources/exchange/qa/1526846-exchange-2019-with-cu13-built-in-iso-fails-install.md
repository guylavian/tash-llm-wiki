---
title: "Exchange 2019 with CU13 built in ISO fails install with error 500"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1526846/exchange-2019-with-cu13-built-in-iso-fails-install
question_id: 1526846
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 with CU13 built in ISO fails install with error 500

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1526846/exchange-2019-with-cu13-built-in-iso-fails-install (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have built a new lab.  New domain.  New everything.  

I installed Exchange 2019 and after a successful install I get error 500 logging in.  

I have tried everything listed on the internet.  

I have rebuilt the server.  

Anyone have a definitive answer why Microsoft dorked up the ISO?  I have installed Exchange 2019 before.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-08*

Hi @ComputerHabit  

The possible cause of the 500 error (if you are seeing it when you access Exchange Admin Center) may be the Oauth certificate was not published, which may take some time.

If Exchange Management Shell is working and you can get results from the cmdlet Get-ExchangeServer, you should have installed Exchange successfully.

I started adding another Exchange install. I thought it odd it kept telling me it could't find the default connector *.

This is a warning message that you can ignore and continue the installation.

It simply tells you do not have a send connector to send outbound messages to internet, which you can create later after you install Exchange.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
