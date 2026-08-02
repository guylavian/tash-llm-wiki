---
title: "Setup a mailflow for Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181978/setup-a-mailflow-for-exchange-online
question_id: 1181978
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Setup a mailflow for Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181978/setup-a-mailflow-for-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

Greetings!

We had to setup mailflow for Exchange Online.

Email had been relayed from Office 365 (Exchange Online) via Smart host defined to our organization’s  email server (Exchange Server 2013). Please provide step by step screenshot's along with kb article. 

While ******@Contoso.com (Exchange Online) sending an email to ******@contoso.com (Exchange Server 2013) and marking another copy to ******@gmail.com

Domain                                 Email Address

Contoso.Com                 ******@contoso.com (Sender) Exchange Online

Contoso.Com                 ******@contoso.com (Recipient) Exchange Server 2013

Gmail.com                      ******@gmail.com (Recipient)                   

Please suggest. Your quick help will be highly appreciated!

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-02-20*

Hi,

Email had been relayed from Office 365 (Exchange Online) via Smart host defined to our organization’s  email server (Exchange Server 2013).

If the mail flow has been configured correctly, you would be able to send from ******@Contoso.com (Exchange Online) sending an email to ******@contoso.com (Exchange Server 2013).

To send a copy to ******@gmail.com, you can create an Outlook inbox rule in ******@contoso.com's mailbox.

The rule would be like:

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
