---
title: "Exchange Server 2010 - Delete mail from all mailboxes from a specific user."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/260576/exchange-server-2010-delete-mail-from-all-mailboxe
question_id: 260576
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Server 2010 - Delete mail from all mailboxes from a specific user.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/260576/exchange-server-2010-delete-mail-from-all-mailboxe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Morning,  

We have a user, Auto Email, that sends out various reports to many users. Some of which people reply to that triggers a function in the database. The problem is there are now thousands of these emails that need purging, I need to :-  

I need to delete all email sent from this account from all user mailboxes prior to 01/01/2021.  

I need to delete all email sent to this account from all user mailboxes prior to 01/01/2021.  

Is there a way this can be done in Powershell ?  

Any help greatly appriciated   

B

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-11*

Ok, try this then  :)  ( I dont have a 2010 server to test against). You may have to mess with it a bit and try diff things out  

```
Get-mailbox -result unlimited | Search-mailbox  -searchQuery {((Received -lt '01/21/2021') -and (from: Autoemail))} -TargetMailbox targetmailbox  -TargetFolder Inbox - 
LogOnly
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-11*

Thanks @Andy David - MVP   ,    

I tried and failed, maybe I should give up !

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-11*

Thanks @Andy David - MVP       

Thanks for the reply.    

I have tried running the first one (i have created a new mailbox called tesetdelete) and put that where you have said target mailbox ?? It then asks for Folder ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-11*

Goord morning,    

I get this far :-    

    

I cant see what this error means ?    

Also this look like its going to delete from the mailbox "Autoemail", I wanted to delete from all company mailboxes anything received from the account "AutoEmail" ?    

Sorry for my dumbness

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-08*

Hi @Ben Cary   ,    

As Troy said, you could use Search-Mailbox to find these mails and use -DeleteContent to delete them:    

Delete received messages:    

```
Search-Mailbox -Identity User01 -SearchQuery ‘Received    

Delete Sent messages:    

```
Search-Mailbox -Identity User01 -SearchQuery ‘SentNote these cmdlets will permanently delete these messages, they won’t go to the recovery items folder.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
