---
title: "Problem with Office 365 Exchange. Recipients receive some messages twice"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2144466/problem-with-office-365-exchange-recipients-receiv
question_id: 2144466
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Problem with Office 365 Exchange. Recipients receive some messages twice

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2144466/problem-with-office-365-exchange-recipients-receiv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Problem with Office 365 Exchange. Recipients receive some messages twice, even though they are sent only once. Can you help me?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-13*

Hi Doležal, There might be possibility of these above reasons mentioned by Xiantao. Also you can verify if the user checks email from multiple devices. It can sometimes cause synchronization issues and duplicate emails.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-13*

Hi Doležal, There might be possibility of these above reasons mentioned by Xiantao. Also you can verify if the user checks email from multiple devices  like phone, tablet, etc. It can sometimes cause synchronization issues and duplicate emails.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-13*

Hi, @Doležal Radim

Can you provide more information for further troubleshooting?

1.Can you describe the process of sending and receiving emails? For example, who is the sender and who is the recipient?

2.Is there a duplicate message in the sender's Sent Items? Are there any unread messages in it?

3.Can you view the message tracking and check if the mail flow is correct?

4.Does the recipient exist in a distribution group? Are there mail flow rules that are causing the issue?

There are a number of reasons for this problem, including:

1.There are mail rules or forwarding settings in the client or admin centre.

2.Emails may get stuck in the outbox due to poor internet connection, server issues, or technical glitches. When these emails are retried to be sent, they can result in multiple copies being sent if not properly managed.

3.If the recipient has more than one mail account configured in the mail client, make sure that the same email will not be received in more than one account.

4.Synchronisation issues between the email server and Outlook can cause the application to resend emails.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
