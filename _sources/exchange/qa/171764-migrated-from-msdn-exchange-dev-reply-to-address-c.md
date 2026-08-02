---
title: "[Migrated from MSDN Exchange Dev]Reply-To address change automatically"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/171764/migrated-from-msdn-exchange-dev-reply-to-address-c
question_id: 171764
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Reply-To address change automatically

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/171764/migrated-from-msdn-exchange-dev-reply-to-address-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Reply-To address change automatically  

[Original post]  

I am getting emails from ******@a.com domain. A transport rule is applied this mails to redirect to external address ******@c.com and and a copy to my mailbox  ******@b.com.  

When then mails received at external address mailbox , In the message header shows Mail from: ******@a.com and the reply-To address shows ******@b.com  

Is any way we can change the Reply-To address to  ******@a.com?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-23*

Hi,    

Did the sender set the Reply-To address to ******@b.com when sending the message?     

And to my knowledge,the Reply-To address cannot be modified via transport rules.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
