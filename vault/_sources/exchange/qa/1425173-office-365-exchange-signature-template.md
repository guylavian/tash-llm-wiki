---
title: "Office 365 Exchange Signature Template"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1425173/office-365-exchange-signature-template
question_id: 1425173
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
---
# Office 365 Exchange Signature Template

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1425173/office-365-exchange-signature-template (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am doing some work for a company that is wanting to create a standardized email signature for all their employees. In doing some research I found a Microsoft article that suggested using an appended disclaimer and add tokens that can pull the requested information.

https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/disclaimers-signatures-footers-or-headers

So I followed the information and came up with the following:

<b>%%DisplayName%%</b><br>

Company Name<br>

%%Title%%<br>

%%Phone%%<br>

%%MobilePhone%%<br>

The information contained in this e-mail is legally privileged and confidential information intended only for the use of the individual or entity to whom it is addressed. If the reader of this message is not the intended recipient, you are hereby notified that any viewing, dissemination, distribution, or copy of this e-mail message is strictly prohibited. If you have received and/or are viewing this e-mail in error, please immediately notify the sender by reply e-mail, and delete this e-mail from your system. Thank you.

What is happening now is it will pull the display name and company name, and the bottom disclaimer but nothing else. I have added the title phone and mobile phone to AD and made sure it synced to Azure. I can look at the user in 365 admin and it is showing the correct information as well. What am I missing here?

## Answers

_No answers on this thread._
