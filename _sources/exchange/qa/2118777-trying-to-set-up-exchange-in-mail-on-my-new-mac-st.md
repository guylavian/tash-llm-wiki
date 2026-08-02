---
title: "Trying to set up Exchange in Mail on my new Mac Studio; it’ll send but not receive."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118777/trying-to-set-up-exchange-in-mail-on-my-new-mac-st
question_id: 2118777
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Trying to set up Exchange in Mail on my new Mac Studio; it’ll send but not receive.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118777/trying-to-set-up-exchange-in-mail-on-my-new-mac-st (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I’m trying to set up Exchange in Mac Mail on my new Mac Studio; it’ll send but not receive. 

For reference, I have a MacBook Pro, two iPads and an iPhone and Exchange works fine on all of them.

A general Google search indicated it might have to do with ports. Could that be right? Where would I find that info?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-14*

Hi @PeteMay,

Welcome to the Microsoft Q&A platform!

According to your description, you are experiencing a problem where your new Mac Studio cannot receive emails, while other devices work fine. The problem may indeed be related to port settings or other configuration details.

Here are a few steps you can try to solve the problem:

-  Make sure your Mac Studio is connected to the Internet.

-  Make sure your mail application is updated to the latest version.

-  Double-check your Exchange account settings in the mail application. Make sure the incoming mail server settings (IMAP/POP) and ports are configured correctly. You can usually find these settings on the support page of your email provider.

-  Look for any status icons or messages in the mail application that may indicate a problem. For example, a lightning bolt or warning symbol next to the account inbox can provide clues.

-  Sometimes deleting and re-adding the Exchange account can solve sync problems.

For port settings, you can usually find this information on the support page of your email provider, or contact their support team. Common ports for Exchange are:

-  IMAP: Port 993 (SSL) or 143 (non-SSL)

-  POP: Port 995 (SSL) or 110 (non-SSL)

-  SMTP: Port 587 (TLS) or 465 (SSL)

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
