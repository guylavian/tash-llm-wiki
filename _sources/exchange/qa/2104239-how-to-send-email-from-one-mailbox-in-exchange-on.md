---
title: "How to send email from one mailbox in Exchange On Prem to another mailbox in Exchange Online in a hybrid Exchange environment?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2104239/how-to-send-email-from-one-mailbox-in-exchange-on
question_id: 2104239
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to send email from one mailbox in Exchange On Prem to another mailbox in Exchange Online in a hybrid Exchange environment?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2104239/how-to-send-email-from-one-mailbox-in-exchange-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We use HCW to deploy hybrid switching, and AADC has also been deployed. Email A was created on Exchange Online. Email B was created on the on-pre Exchange.

Now, I can send an email to B. But I cannot send an email from B to A. It displays' We will not be able to send this email to A because the email address is no longer valid '

A friend told me that this is because A was created on Exchange online, so B cannot find it. On the other hand, B is created locally and synchronized to the cloud by AADC, so A knows about it and can send emails to it.

Is it true? In my opinion, once a hybrid exchange environment has been deployed, the exchange online and exchange on-prem should be able to talk with each other. So there should not be an issue when you send email across online and on-prem.

If my friend is true, what should i do the synchronized the mailbox from online to on-prem?

If my friend is wrong, which part of the setting could be wrong?

thank you!!!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-16*

Hi,@Nicholas

Thanks for posting your question in the Microsoft Q&A forum.

Your understanding is correct that in a hybrid Exchange environment, Exchange Online and Exchange on-premises should be able to communicate with each other seamlessly. If you're able to send emails from Exchange Online (Email A) to Exchange on-premises (Email B), but not the other way around, it suggests there might be an issue with the configuration.

When you are in a Hybrid deployment, then you have to create the AD Account locally, ideally using EAC using the option to create an Office365 account. Then let the account sync to the cloud and licence it. If the entire account and mailbox was created in the cloud (so there is no local AD account) then it will not work correctly.

You can refer to this link for details:https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/ndr/recipientnotfound-ndr?source=recommendations

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
