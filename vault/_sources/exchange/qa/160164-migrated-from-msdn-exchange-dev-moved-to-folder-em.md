---
title: "[Migrated from MSDN Exchange Dev] Moved to folder emails via OWA, reappearing in inbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/160164/migrated-from-msdn-exchange-dev-moved-to-folder-em
question_id: 160164
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Moved to folder emails via OWA, reappearing in inbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/160164/migrated-from-msdn-exchange-dev-moved-to-folder-em (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/9da30412-41a8-4639-997d-b9164e6c93bb/moved-to-folder-emails-via-owa-reappearing-in-inbox?forum=exchangesvrdevelopment   

Dear community,  

I manage an Exchange 2016 Standard Environment On-Premise CU18. The Exchange is in a hybrid configuration with Exchange Online. Please, note that the issue has persisted, even before the hybrid configuration was implemented.  

One of my users uses only OWA to connect to hers mail. The particular mailbox is hosted on the on-premise machine. Sometimes (i.e. once a month) when she moves a number of emails to subfolders of Inbox the move appears to be successful and the emails visualize into the desired subfolders. But after a few minutes or seconds the whole heap of emails that had been moved into folders are reappearing in the Inbox folder.   

There are no mobile devices that are synchronizing with the mailbox. There are no delegation permissions for that mailbox.  

Thank you in advance.  

Kind regards,  

Flame

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-12*

Does this issue occur with other on-premises Exchange mailboxes?    

Please make sure the user is using the most recent version of the browser. We can try to use other browsers, such as Microsoft Edge and IE 11 to see if the issue can be reproduced.    

Try to move this user mailbox to other database:    

```
New-MoveRequest -Identity "" -TargetDatabase ""
```

Additionally, since you have deployed the hybrid configuration, you can move this mailbox to O365. Then check if this issue still occurs.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
