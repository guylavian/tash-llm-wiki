---
title: "Transfer Mailbox LegacyExchangeDN in Office 365 New Mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186477/transfer-mailbox-legacyexchangedn-in-office-365-ne
question_id: 1186477
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Transfer Mailbox LegacyExchangeDN in Office 365 New Mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186477/transfer-mailbox-legacyexchangedn-in-office-365-ne (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Hi Have a mailbox Called  "Marketting-Old" which his 120 GB (Primary+Archive). Because of some reasons, I want to keep this mailbox and move the users to a Freshly created New Mailbox "Marketting-New".

If I am keeping my exiting mailbox in the system, How can I make sure all Internal senders' email can be delivered to new mailbox?

To make sure your answer is closer to my real problem, please read my below points else your answer might be incomplete or not helpful:

-  I have already Transferred UPN, PrimarySMTPAddress, aliases, Name, DisplayName attributes from old mailbox.

-  My internal users sending emails are still going to old mailbox even smtp addresses and other attributes (except LEDN as X500) moved to new mailbox and Outlook cache cleared at user end.

-  My new mailbox is able to send and receive emails from 3rd parties' senders without any issues.

-  Real issue revolves around the legacyExchangeDN transfer as X500 from Old mailbox to new mailbox and system not allowing me to add this address as a X500.
   I have not found any AAD, MSOL, EXO command to delete/rename/replace LEDN on old mailbox so now your thoughts are appreciated on "How can i fix this issue?".

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-06*

Hi @Kanta Prasad  ，

Real issue revolves around the legacyExchangeDN transfer as X500 from Old mailbox to new mailbox and system not allowing me to add this address as a X500.

As far as I know, it's supported to transfer the LegacyExchangeDN from an INACTIVE mailbox to another mailbox as a X500. See: Restore an inactive mailbox:

```
Set-Mailbox  -EmailAddresses @{Add="X500:"}
```

I was wondering why you want to keep the old mailbox alive? If you are intending to keep the old mailbox data, what about disabling it and then restore the content into the new maillbox, or exporting the old mails to PST files and then disable it?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
