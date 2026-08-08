---
title: "Exchange 2019 SMTP Help"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191004/exchange-2019-smtp-help
question_id: 1191004
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 SMTP Help

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191004/exchange-2019-smtp-help (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Afternoon All,

I have a new Exchange 2019 install and have installed my certificate I got from an external CA. I can get POP3 to work for incoming mail and outgoing SMTP when using STARTTLS but I want to use SSL/TLS for the SMTP. However, when I select with port 587 or 465 I get the following error:

Send test email message: Your server does not support the connection encryption type you have specified. Try changing the encryption method. Contact your mail server administrator or Internet service provider (ISP) for additional assistance.

I have confirmed that my client machine of Windows 11 is using TLS 1.2 and Exchange 2019 is using TLS 1.2 as well. Does anyone know how to fix this?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-20*

Hi @Brandon Hoskins ,

You could refer to this article: https://woshub.com/outlook-server-not-support-connection-encryption-type/

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-20*

Check this thread for help - https://social.technet.microsoft.com/Forums/en-US/6e486936-e4a2-4da8-87ef-903d67e4bb84/outlook-2016-cannot-connect-to-email-server-with-ssltls?forum=outlook
