---
title: "Export pst issue Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1008696/export-pst-issue-exchange-2019
question_id: 1008696
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Export pst issue Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1008696/export-pst-issue-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have exchange 2019 and want to export pst of ex employees. These issues are encountered when exporting a .pst file.    

-  User mailbox size in Exchange is 2 - 3 GB but after exporting .pst file it shows 15 - 20 GB    

-  Some mailboxes while starting the export pst file, the status shows in progress but after 2 to 3 days nothing happens.    

Before that everything was working fine even did not change anything on the server side.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-16*

To get the update status of the export pst file I found this EMS cmdlet Get-MailboxExportRequest -status failed. Get-MailboxExportRequestStatistics -IncludeReport | Format-List > \ex01\pstfiles\report.txt which has detailed the root cause of the error and hopefully resolves the issue.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-16*

Hi @Innocent Heartvoice   ,    

mailbox export to a pst file    

Do you mean to export emails through Outlook client ? Can I know which version of Outlook client you use? Have you received any errors when did you export it?    

----------    

used EMS New-MailboxExportRequest -Mailbox AylaKol -FilePath "\SERVER01\PSTFileShare\xxxxxx.pst"  and encountered problems    

Please have a check the following points before you export emails using this command:    

-  Go to the “EAC – permissions ”, check if the administrator has the Mailbox Import Export role .    

     

-  Check the shared folder where you want to export your PST files are shared with above administrator and Exchange Trusted Sub System.      

-  These two users must have full permissions on the folder and on the share .    

    

-  You could use the Get Mailbox Export Request cmdlet to see if the export progress was successful.    

    

In addition , I would suggest you also could refer to the following link to export specify the user mailbox use eDiscovery search.    

Create an In-Place eDiscovery search in Exchange Server | Microsoft Learn    

Exchange Server: Export eDiscovery search results to a PST file | Microsoft Learn    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
