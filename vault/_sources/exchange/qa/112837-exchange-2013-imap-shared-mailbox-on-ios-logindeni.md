---
title: "Exchange 2013 iMap Shared Mailbox on IOS Logindenied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/112837/exchange-2013-imap-shared-mailbox-on-ios-logindeni
question_id: 112837
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 iMap Shared Mailbox on IOS Logindenied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/112837/exchange-2013-imap-shared-mailbox-on-ios-logindeni (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,    

I have an issue with adding a shared mailbox to an iPad. It seems like It doesn't seem the matter what username syntax I use (Domain\user\sharedmailbox, user@keyman  \sharedmailbox@keyman  ) I get the same login denied in the iMap logs.    

```
2020-09-30T09:47:58.290Z,00000000000000A0,0,10.135.0.23:993,90.187.51.145:58423,,51,0,53,OpenSession,,  
2020-09-30T09:47:58.346Z,00000000000000A0,1,10.135.0.23:993,90.187.51.145:58423,,1,12,140,capability,,R=ok  
2020-09-30T09:47:59.050Z,00000000000000A0,2,10.135.0.23:993,90.187.51.145:58423,domaion\user\sharedmailbox,614,31,30,authenticate,PLAIN,"R=""2 NO AUTHENTICATE failed."";Msg=""AuthFailed:LogonDenied,User: domain\user\sharedmailbox"";ErrMsg=AuthFailed:LogonDenied"  
2020-09-30T09:47:59.110Z,00000000000000A0,3,10.135.0.23:993,90.187.51.145:58423,domain\user\sharedmailbox,0,0,0,CloseSession,
```

I am definetly using the correct password for the user as loggin in to OWA or using iMap for the users mailbox works perfectly.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-01*

Hi @kardon       

I did some testing and this worked for using the Thunderbird client and IMAP:    

user@keyman  .com\sharedmailbox@keyman  .com as the logon user name.    

Note also that in my testing,  the Primary Email Address of each account matches the UPN, just in case that makes a difference.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

@kardon      

Configure Shared mailbox on mobile/tablet only supported for Office 365 account now, it doesn't work for Exchange on-premises mailbox. If you want to access Exchange on-premises shared mailbox on mobile/tablet, you may need to change browser to computer mode, then access shared mailbox from OWA.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-30*

Have you tried just sharedmailbox@keyman  .com ?
