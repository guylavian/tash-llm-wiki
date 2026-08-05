---
title: "Removal of the Exchange License didn’t immediately mail disable the user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/161211/removal-of-the-exchange-license-didn-t-immediately
question_id: 161211
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Removal of the Exchange License didn’t immediately mail disable the user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/161211/removal-of-the-exchange-license-didn-t-immediately (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We are conducting a hybrid migration into an organziation that previusly has exchange online mailboxes. The migration is from Exchange Server 2010. We already migrated almost 70 mailboxes with the last one we had an issue. What we were doing is removing the Exchange Online license to the user, wait about 5 or 10 minutes until the mailbox was disconnected, and then we can do the mailbox migration (using the regular procedure).  

But the issue is that when we removed the Exchange Online license for this last user, tha mailbox is not disconnected.  

We have waited about more than an hour, but nothing happened.  

Why is not being disconnected? What can we do?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-13*

Hello,  

the mailbox was rolling back to previus status, license was applied again in order the user can arrange Teams meetings and so on. The license was removed using the Admin Portal of Office 365, but not the complete license like Business Standard, the license that was removed was only Exchange Online (plan1) because the user already has information in onedrive or sharepoint.   

We have not try another method, so we are going to try the PowerShell method, if it is possible to remove only the Exchange Online (plan 1) license.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

Hi @Cristian Ruiz   ,    

Is there any update about your issue, what's the status of the mailbox now?    

How did you remove the license for the user? Have you tried re-licensing the user then use another method like powershell to remove it again?    

Remove Microsoft 365 licenses from user accounts with PowerShell    

The command below will list all the unlicensed users. Check whether the user is listed in the result. First, connect to your Microsoft 365 tenant.    

```
Get-MsolUser -All -UnlicensedUsersOnly
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
