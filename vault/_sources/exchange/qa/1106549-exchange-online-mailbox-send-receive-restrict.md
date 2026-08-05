---
title: "Exchange Online Mailbox send/receive restrict"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1106549/exchange-online-mailbox-send-receive-restrict
question_id: 1106549
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Mailbox send/receive restrict

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1106549/exchange-online-mailbox-send-receive-restrict (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We have a requirement where we want to use a generic account for Teams live events/webinar scheduling. Since that account has to have a Exchange Online mailbox enabled, we do not want any type of emailing activities on the mailbox. Account should only be allowed to schedule live events/webinars/meetings. It should not be able to send/receive other emails with attachments. I know if i restrict it from size limitation, it won't be able to send/create meeting invites. Is there any other way to achieve the same?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-29*

Hi @GoodResource   ，    

According to your description, you only want to restrict the user from sending and receiving mails with attachments. Please correct me if I misunderstand your question.    

If I understand your question correctly, you seem can create 2 transport rules to meet your request, below rules I have created in my lab for your reference:    

-  Create a rule to restrict the specific user from sending mails with attachments:    

     

-  create a rule to restrict the specific user from receiving mails with attachments:    

     

Note: attachment's file extension you could add whatever you want.    

Enable these 2 rules at the same time, you will restrict the specific user from sending/ receiving mails with attachments.    

If an Answer is helpful, please click "Accept Answer" and upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-28*

I suppose you can create a mail flow rule that restricts messages based on the message type (The message properties > include the message type > calendaring).
