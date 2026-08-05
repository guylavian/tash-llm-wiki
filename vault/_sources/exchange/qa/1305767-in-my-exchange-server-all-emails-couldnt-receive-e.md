---
title: "In my exchange server, all emails couldn't receive email from external"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1305767/in-my-exchange-server-all-emails-couldnt-receive-e
question_id: 1305767
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# In my exchange server, all emails couldn't receive email from external

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1305767/in-my-exchange-server-all-emails-couldnt-receive-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I tried to send an email external to my exchange server email. But after many tries it is still not received. I wonder what can be missing in my configuration. Notice that I'm using Hybrid mode.   

 This is the email notification to my external email that I can't send the email. Here is the link if you need https://go.microsoft.com/fwlink/?LinkId=389361.

 

This is also the result of test connectivity of Outbound SMTP Email (https://testconnectivity.microsoft.com/)

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-06-15*

Hi @Dino，

From the description, do you mean in your hybrid deployment, users hosted in Exchange on-premises cannot receive mails sent by external users?  

How did you configure the MX record? Is it pointed to your on-premises organization or it's pointed to the EOP service?

Actually, as indicated in the name, the Outbound SMTP test is used to troubleshoot outbound issues like your users cannot send mails out as expected. For your situation, you may need to run the Inbound SMTP test instead.

Besides, you can go through the document below and see if you've missed anything when configuring the hybrid deployment.  

Transport routing in Exchange hybrid deployments -Inbound messages from the Internet

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
