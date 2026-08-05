---
title: "Exchange 2016 onprem - Slow upload over MAPI"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1510865/exchange-2016-onprem-slow-upload-over-mapi
question_id: 1510865
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 onprem - Slow upload over MAPI

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1510865/exchange-2016-onprem-slow-upload-over-mapi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I would really appreciate expert advise.

We noticed slow upload of email attachments over MAPI.

Upload speed is constantly limited(even after hours) to approximetly 1MB/s.

Outlook client freezes for seconds, when trying to send email with attachment.

We are trying to eliminate the cause:

-  Attachment size doesn't improve the speed.

-  Client location has no influence. We placed test client in same VLAN as servers.

-  IMAP works much better.

-  After hours/overnight performance also degradated and limited to about 1MB/s.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-25*

Hi @Milan Resko  

Kindly note that to better troubleshoot this issue, we may need to collect Outlook logs and capture network packets for analysis, which is not suitable via forum posts.

If it is possible please consider opening a support ticket to contact support via email or phone so we can take a close look into this issue:

Global Customer Service phone numbers

Does this issue occur on specific mailboxes or all mailboxes?

If it only occurs on specific mailboxes, do these mailboxes have something in common?

For example, assigned "Full Access" permission to many users or currently logged in from many clients, or are all hosted in a specific database.

Besides, please also run the Test-MapiConnectivity cmdlet in Exchange Management Shell to have a check if it will return errors:

```
Test-MapiConnectivity -Server "Server01"
Test-MapiConnectivity -Identity "midwest\john"
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
