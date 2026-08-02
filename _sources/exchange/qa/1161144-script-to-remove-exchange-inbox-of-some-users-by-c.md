---
title: "Script to remove Exchange inbox of some users by CSV"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161144/script-to-remove-exchange-inbox-of-some-users-by-c
question_id: 1161144
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Script to remove Exchange inbox of some users by CSV

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161144/script-to-remove-exchange-inbox-of-some-users-by-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am working in a Migration Project and I need to remove the inbox of some users and Re-launch the migration again.

Could you send me a script where can i do that? I am so sorry but I am very new in Powershell.

Best Regards

Thx

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Please use the below-mentioned command to remove bulk mailboxes in exchange.

Command to remove the bulk mailboxes by using the above CSV file .

`import-csv c:\remove.csv | Remove-Mailbox -Confirm:$false` 

Also, check this thread for help - https://learn.microsoft.com/en-us/answers/questions/359416/exchange-bulk-import-from-csv-file-to-remove-devic

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-17*

Hi @Jacobo Garrido  ,
You can use the New-ComplianceSearch and New-ComplianceSearchAction cmdlets to search for and delete an email message from all mailboxes in your organization.
Here is a detailed guide about it：Search for and delete messages in Exchange Server | Microsoft Learn
(Please note：A maximum of 10 items per mailbox can be removed at once.)

Alternatively, you can refer to the following guide to create a retention policy and apply it to specified mailboxes to delete messages older than one day：

Create a Retention Policy in Exchange Online | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
