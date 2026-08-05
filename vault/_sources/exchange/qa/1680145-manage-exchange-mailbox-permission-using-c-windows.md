---
title: "manage Exchange Mailbox permission using C# windows application"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1680145/manage-exchange-mailbox-permission-using-c-windows
question_id: 1680145
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "developer-technologies-windows-forms", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# manage Exchange Mailbox permission using C# windows application

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1680145/manage-exchange-mailbox-permission-using-c-windows (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi folks,

i would like to design a windows application which will do below. is it possible to develop using C# ?

-  Connect to Exchange Online.

-  Add/Remove mailbox fullaccess.

-  Add/Remove SendAs or Sendonbehalf access.

-  Set mailbox forwarding

Thanks  

Shankar

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-20*

Hi @Meher, Shankar (CORP) , Welcome to Microsoft Q&A,

Regarding how to use c# to connect to Exchange Online and send emails, you need to check this document specifically: Enable or disable authenticated client SMTP submission (SMTP AUTH) in Exchange Online (These settings only apply to mailboxes that are hosted in Exchange Online (Office 365 or Microsoft 365).) This forum does not support other email addresses.

You need to Enable SMTP AUTH for specific mailboxes.

You can also check out this reference list.

Best Regards,

Jiale

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
