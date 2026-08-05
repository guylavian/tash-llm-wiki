---
title: "Exchange emails analysis with BI solution"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1306882/exchange-emails-analysis-with-bi-solution
question_id: 1306882
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange emails analysis with BI solution

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1306882/exchange-emails-analysis-with-bi-solution (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Friends,

I would like your help regarding the following request.

 

I would like to set up a BI solution to analyse the emails that our company receive on generic mailbox.

 

The fields needed are :

1.       Sender adress

2.       Recipient adress

3.       Date email sent

4.       Email unique ID

5.       N° of Attachment received by email (based on original email ID)

6.       Format of attachment (PDF, JPG,..)

I would need to keep historical data to make comparison with previous year/month/week…

 

Is is feasible ? For my colleagues it is not possible to collect attachment figures.

Any advise to share on this topic ?

 

Many thanks in advance.  

Regards

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-06-19*

Hi @Anonymous  ,

Is is feasible ? For my colleagues it is not possible to collect attachment figures.

From the perspective of Exchange server side, agreed with your colleagues that no, it's not feasible to get the attachment data like the number of attachments per mail or the format of attachment.

Supposing you are using on-premises Exchange server where message data is usually retrieved from message tracking logs, attachments related data are not recorded in the logs. See Fields in the message tracking log files.

By the way, considering that Power BI is currently not supported in Q&A, if you would like further help in terms of BI, you can also visit the dedicated community below:  

Microsoft Power BI Community

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
