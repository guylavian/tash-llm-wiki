---
title: "Exchange Online Message Size"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1383552/exchange-online-message-size
question_id: 1383552
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online Message Size

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1383552/exchange-online-message-size (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our mailboxes are migrated to exchange online. We are a hybrid deployment.  Our message send and receive size is 50mb.  One of our users sent attachments to 2 internal mailboxes.  A shared mailbox and a standard user mailbox.  The attachments totaled 32mb.  The 2 internal mailboxes did not receive the email.

When the user sent the email to each mailbox individually (not CC'd), the users received the email.  Please explain what's happening and how to fix.  Thanks for your help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-10*

Hi @mara2021  

<<The 2 internal mailboxes did not receive the email.

Didn't receive NDR?

1.This looks like the message size limit has been reached. Does the message size decrease when you send them separately or is it the same as when you send them together? Try increasing the size to 100M. See if that helps.

https://learn.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits#message-limits

OR:  

2.When you send separately, are you using the same client? You mentioned that the message track does not show that it has been sent or delivered. It is also possible that it was not sent at all and was directly restricted by the client the first time it was sent. Outlook itself also seems to have limitations.

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
