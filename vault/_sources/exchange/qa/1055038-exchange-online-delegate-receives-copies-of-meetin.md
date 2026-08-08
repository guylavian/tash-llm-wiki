---
title: "Exchange Online - delegate receives copies of meeting-related messages sent to me - Untick for all users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1055038/exchange-online-delegate-receives-copies-of-meetin
question_id: 1055038
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online - delegate receives copies of meeting-related messages sent to me - Untick for all users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1055038/exchange-online-delegate-receives-copies-of-meetin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys    

I am trying to set all of our users <50 to 'Untick the delegate receives copies of meeting-related messages sent to me' for all of their 'already set' deletes     

I am using Exchange Online PowerShell:    

Set-CalendarProcessing -Identity "user"-ForwardRequestsToDelegates $false    

but this does not seem to affect the tick in the box for any of my test user's delegates.    

Can someone tell me where i am going wrong please?

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-20*

Hi Andy     

I don't know what I did / what happened before , but i have now got this working with the    

 Set-MailboxFolderPermission USER1:\calendar -User USER2 -AccessRights Editor -SharingPermissionFlags None    

So thanks Andy    

Baz

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-20*

Thanks Andy     

I tested the command below and it removed the targeted delegate from my delegates.    

However, I just wanted to remove the tick from the 'delegate receives copies of meeting-related messages sent to me" box    

Have i understood this incorrectly    

    

Just FYI... The situation is a thus...    

We have a lady that enters all of our holiday into our calendars. Historically our users have manually added her as a delegate for their calendar.    

she is now complaining that she gets all meeting invite acceptance and declines etc... As we did not untick the box (as by default it is on)    

i was hoping to be able to avoid asking our users to manually untick  .. involving the users always involves pain...

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-19*

Ahh .. That I did not spot.    

So, with that being known.... there is no way of administering this for my users?    

I guess I will have to send out an email asking them to untick themselves :-(    

Cheers

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-19*

that command doesnt work for user mailboxs, just resource mailboxes:    

https://learn.microsoft.com/en-us/powershell/module/exchange/set-calendarprocessing?view=exchange-ps    

    

I have found the only way to ensure that box gets unchecked without affecting existing delegate perms is to uncheck in Outlook
