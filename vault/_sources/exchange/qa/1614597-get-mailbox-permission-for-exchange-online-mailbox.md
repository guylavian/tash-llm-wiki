---
title: "Get mailbox permission for exchange online mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1614597/get-mailbox-permission-for-exchange-online-mailbox
question_id: 1614597
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Get mailbox permission for exchange online mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1614597/get-mailbox-permission-for-exchange-online-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team, Please help me with a Powershell command to export mailbox permission on shared mailboxes where we do have a mailbox list available in CSV format. This is for contoso.com exchange online mailboxes based in office 365. Your quick response will be highly appreciated!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-12*

Hi @Gurudas  

In this blog, it shows the detailed steps about how to export mailbox permission on shared mailboxes. The script will scan the mailbox databases and check the mailboxes one by one. It will dump everything it does to a text file and export the permissions to the CSV file. The progress can take time, depending on the Exchange organization size.

Reference:

https://www.alitajran.com/export-mailbox-permissions-to-csv-file/

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
