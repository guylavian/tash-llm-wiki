---
title: "Microsoft HMA for On-Premise Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1805512/microsoft-hma-for-on-premise-exchange
question_id: 1805512
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Microsoft HMA for On-Premise Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1805512/microsoft-hma-for-on-premise-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are currently operating on Exchange 2019 and planning to enable HMA for the On-Premise environment. I am seeking clarification on the following points. Could someone assist me in resolving this?

1.Are shared mailboxes supported with HMA?

2.Do applications that need to connect to Exchange through EWS to send emails have to support modern authentication? What should be done if an application does not support modern authentication? Is there a workaround available?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-10*

Hi，Chandra Sekhar

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, I will answer them in order:

1. Are shared mailboxes supported with HMA?

Shared mailboxes in Exchange 2019 support Modern Authentication (HMA). You can enable HMA for shared mailboxes to enhance security.

2.Do applications that need to connect to Exchange through EWS to send emails have to support modern authentication? What should be done if an application does not support modern authentication? Is there a workaround available?

I am a little confused about this question?

Is your environment hybrid? If it is a hybrid environment, you can only use Hybrid Modern Authentication instead of Modern Authentication.

Here is the official evidence from Microsoft: Enable Modern Auth in Exchange Server on-premises | Microsoft Learn

If you're using Exchange 2019 only, any application that needs to connect to Exchange via EWS to send mail must support Modern Authentication.

If your application doesn't support modern authentication, you can either change the application or use the Microsoft Graph API.

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

Best
