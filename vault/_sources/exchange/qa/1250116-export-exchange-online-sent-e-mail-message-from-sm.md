---
title: "Export Exchange Online sent e-mail message from SMTP transfer agent queue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1250116/export-exchange-online-sent-e-mail-message-from-sm
question_id: 1250116
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Export Exchange Online sent e-mail message from SMTP transfer agent queue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1250116/export-exchange-online-sent-e-mail-message-from-sm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to export an e-mail message sent by an user from Exchange Online SMTP agent queue?
I need the complete message with full headers.
I am able to extract it from user mailbox but I don't get SMTP headers.
The message has been externally delivered to another domain but I need to legally demonstrate that it has been modified after sending it.
Another way could be a simple checksum/hash in Exchange logs but I didn't find anything like that.
Thanks
Marco

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-04-21*

Hi @ Marco Pozzi，

The message headers of the emails can only be viewed from the recipient's inbox, and we can't get the details from our own Exchange Online.

In my research and testing, in Exchange Online, we can only go through message trace to see if the email applied to a transport rule and modified the headers internally.

Thank you for your understanding and patience！

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
