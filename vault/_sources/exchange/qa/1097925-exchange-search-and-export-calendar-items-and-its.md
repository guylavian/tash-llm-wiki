---
title: "exchange search and export calendar items and it's scheduled time"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1097925/exchange-search-and-export-calendar-items-and-its
question_id: 1097925
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# exchange search and export calendar items and it's scheduled time

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1097925/exchange-search-and-export-calendar-items-and-its (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi We have a requirement to search and export calendar items to an excel along with the meeting's scheduled time not the time when it was sent or received. So basically we want to know what all meetings were scheduled during 2016-2019 and those meeting's actual scheduled time not when this was sent. Is it possible?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-25*

Hi @GoodResource   ,    

You can export the calendars one by one:    

Please assign your self full access of the room mailbox and then make sure the Room calendar is visible in your calendar folder in Outlook client.     

Once you see under Calendar -> then you can make use of Export feature in Outlook and get the required data is CSV using below steps:     

Make sure room Calendar is checked     

Click on File -> Import/Export -> Next     

Export to a File -> Next     

Comma Separated Values -> Next     

Select the Room Calendar -> Next     

Select the location to save the file     

At last, it will ask you the Date Range -> Next     

There is no direct Powershell in Exchange to export all room meeting calendar in CSV, If your requirement is a batch export, this is not possible.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-22*

Hi @GoodResource   ,    

You could try to export the calendar using the following cmdlet:    

```
Export-Mailbox-Identity –StartDate ‘01/01/2016’ –EndDate ‘31/12/2019’ –IncludeFolders ‘\Calendar’ –FilePath \\PSTFile\FolderName\FileName.pst
```

Refer to:    

https://www.nucleustechnologies.com/blog/export-import-calendar-items-from-office-365-using-powershell/    

Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
