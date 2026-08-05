---
title: "Exchange 2013 - Outlook is not showing all items"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/314733/exchange-2013-outlook-is-not-showing-all-items
question_id: 314733
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 - Outlook is not showing all items

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/314733/exchange-2013-outlook-is-not-showing-all-items (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have the following problem with shared mailbox:  

When checking number of items in main "INBOX" folder from Exchange Server side (running Get-MailboxFolderStatistics command) it returns value of 1000 items in just this folder (not including subfolders). However, every user that has access to this mailbox can see only few of them. New e-mails sent to this mailbox are being delivered and displayed correctly in the inbox folder.  

Troubleshooting done:  

-  View settings from Outlook side have been reset   

-  Tried OWA - same result  

-  Granted myself with fullaccess rights and checked - saw the same amount of e-mails as other users.  

-  Checked mailbox with MFCMAPI - all affected items (not displayed ones) are assigned to PR_Assoc_Content_Count instead of PR_Content_Count  

-  Exported affected folder to a freshly created mailbox and checked there - same number of items is displayed from Exchange server side and only few of them visible in the inbox folder.  

Any ideas what could be the problem here?  

Thank you in advance.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-03-15*

Sure its not just normal? How many exactly are not showing?    

https://learn.microsoft.com/en-us/previous-versions/office/exchange-server-2007/aa996762(v=exchg.80)?redirectedfrom=MSDN    

A mailbox can have hidden items that are never visible to the user and that are only used by applications. The Get-MailboxFolderStatistics cmdlet can return hidden items for the following values: FolderSize, FolderAndSubfolderSize, ItemsInFolder, and ItemsInFolderAndSubfolders.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-16*

Hi @Natan1881  ,    

Agree with Andy that it's an expected behavior that the items count returned by the Get-MailboxFolderStatistics cmdlet is different with what are visible to the users. This is because the output returned by the cmdlet also includes hidden items. To add to the link shared by Andy, you can also check the link below which applies to Exchange 2013:    

 Get-MailboxFolderStatistics    

You run the Get-MailboxFolderStatistics cmdlet for other mailboxes as well to verify this.    

If you still have concern on this given the information above, I'd suggest confirming if the users have any idea about the missing messages, like if they are all old messages prior to a certain date. Feel free to post back should you need further assistance on this.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
