---
title: "Exchange2013/Outlook2019 - Self Permissions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/403579/exchange2013-outlook2019-self-permissions
question_id: 403579
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange2013/Outlook2019 - Self Permissions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/403579/exchange2013-outlook2019-self-permissions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Current issue... MailboxUser1, years ago gave MailboxUser2 permission as publishing editor to access their Inbox\subfolder they created and all was good at that time.    

Then MailboxUser2 moves to a lower position in the same department but, still has access to MailboxUser1 which they shouldn’t at this time.  As the years pass MailboxUser1 didn’t think to check their permissions on any of their folders in their mailbox but, MailboxUser2 can still see MailboxUser1’s Inbox\subfolder when they click on File -> Open & Export -> Other User's Folder. YIKES!!    

I’m trying to figure out two things…  

-  Is there a way to disable users from giving other mailbox users access to their mailbox?  I know they can share their Calendars w/a button on the ribbon but, I want to disable them from being able to right-click on a folder (i.e. Inbox or Sent Items) & giving permissions themselves.  

-  Who else has done this w/their mailbox with past/present users and they don’t remember?  Is there a script I can run in Exchange Shell that will tell me the privilege's the users give?  I only know  of the following script & it doesn’t show what they have given.  

Get-MailboxFolderPermission -Identity MailboxUser1:\inbox  

FolderName    |         User    |                 AccessRights  

Inbox               |                   Default     |             {None}  

Inbox               |               Anonymous     |     {None}  

We are using Exchange 2013 CU23/Windows 2019 Server/Outlook 2019

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-24*

Hi @Anonymous       

-  Looks like we may need to add this registry setting through group policy that would disable users from editing their folder permission on Outlook clients.  How do I do this for users that use OWA?    

-  I was hoping there was a wildcard for this script that would list the subfolders & their permissions.  We have 480 users & I don't want to login as each user (or look over there shoulder) to see if they've created subfolders and if they have given permissions to other users.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-21*

Hi @Penny Miller   ,    

To remove the folder permission on MailboxUser2, you could use Remove-MailboxFolderPermission.    

For your first question, I checked the Exchange docs but still couldn't find anything about blocking folder permission giving.    

You may want to use the registry to disable users from editing their folder permission on Outlook clients:    

Do not allow users to change permissions on folders    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

For the second question, you need to use the full path of the subfolder:    

```
Get-MailboxFolderPermission -Identity MailboxUser1:\inbox\subfolder
```

    

I found an article about removing specific user with the target folder's permissions.     

PowerShell Script to Remove Mailbox Folder Permissions    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

    

But it's hard to traverse all the folders' permissions to all users.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
