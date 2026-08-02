---
title: "Hybrid Exchange mailbox migration issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1021229/hybrid-exchange-mailbox-migration-issues
question_id: 1021229
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Hybrid Exchange mailbox migration issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1021229/hybrid-exchange-mailbox-migration-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm having issues with migrating a particular user from Exchange on prem up into Exchange Online.    

A couple of weeks ago our IT helpdesk assigned this on prem user an Exchange Online license to their O365 account by mistake, and ever since the license was removed there have been issues.    

Namely, the user does not appear in the Exchange Online GAL any more - all other on prem users do.    

The user cannot be emailed anymore from and Exchange online user.    

Having looked into this, I ran the following command to remove any remnants of the erroneous EO mailbox from the users O365 account    

Set-User onpremuser@keyman  .com -PermanentlyClearPreviousMailboxInfo    

Checking the account afterwards, all looks good to me    

Get-User onpremuser@keyman  .com | Select-Object Name,Recipient    

Name            PreviousRecipientTypeDetails RecipientType RecipientTypeDetails    

----            ---------------------------- ------------- --------------------    

onpremuser None                         User          User         

Having then tried to set up a migration job for the user to move the mailbox to Exchange online, the batch fails with the following error:    

"A recipient wasn't found for "onpremuser@keyman  .com" on the target. Create a recipient of the appropriate type for this migration on the target and try again."    

So how do you migrate an on prem mailbox in this situation, if assigning an EO license (which I'm assuming is what would create the missing recipient) would then stop the user accessing their on prem mailbox - as was the case originally?    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-17*

This has been resolved after several weeks of troubleshooting with MS Support.    

As a last resort the user account needed to be permanently deleted in AAD and O365, then re-synced via AAD Connect.    

Following this, the MailUser object was successfully created in Exchange Online

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-29*

Still investigating this issue.    

All attributes synced by AAD Connect look good to me having looked at the article @JimmySalian-2011   shared - https://learn.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-object-not-syncing - thanks    

One thing I have noticed when checking the users account in O365 is that there is a legacy value in the sign in field when Get-MsolUser is run, that doesn't match the UPN.    

Two questions:    

-  can this field be amended?    

-  Is this field relevant anymore as I understand MSonline PS module is being deprecated?    

Get-MsolUser -UserPrincipalName User@keyman  .com | fl UserP*,Sign*    

UserPrincipalName: User@keyman  .com    

SignInName : ******@legacydomain.com    

I can find no reference to ******@legacydomain.com in the attributes synced to AAD    

The user is sure that Sign in name hasn't been used for years.    

The legacy domain does still exist however as an accepted domain associated with a completely separate Azure tenant to the one I'm working with.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-27*

When a user is created on-premises and synced to Office 365. E1/E3 license assigned which auto-creates a mailbox. Then you create it on on-premises and try to migrate it and you're stuck. If it's a new user, you could just delete the Office 365 user and remove this user from the recycle bin. It will get recreated next sync and then you can migrate the mailbox and assign a license.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-26*

@Matthew Pollock       

I check in my lab, the synced AD account show as "MailUser" type in "Get-User" command.    

So, I would suggest you move this AD account from a sync OU to an unsynchronized OU. Check whether the AAD account disappear.    

The remove the 'msExchMailboxGuid' and 'targetAddress' value from this AD account (Backup it first) , after that move back to sync OU and sync again.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-25*

Hi Matt,    

Check this link for troubleshooting sync issues, very useful to understand the process of CS and MV and how AAD Connect works.    

tshoot-connect-object-not-syncing    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
