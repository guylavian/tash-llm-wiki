---
title: "Exchange 2016 and Inbox sharing of subfolders"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348211/exchange-2016-and-inbox-sharing-of-subfolders
question_id: 348211
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 and Inbox sharing of subfolders

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348211/exchange-2016-and-inbox-sharing-of-subfolders (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 on premise server. Is it possible to share a user's mailbox, specifically the Inbox and all its subfolders without having to specifically go into each subfolder and grant permissions?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-08*

@Ben Lan      

There are two ways to access the folders of their mailbox, each of which has advantages and disadvantages:    

-  Mailbox full access permission: user could access all folders in another mailbox.    

-  Mailbox folder permission: Based on folder which need to add permission for all subfolders.    

So, you need to add them one by one or find a script as provided by AndyDavid to help you do it in batch.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-07*

In that case you will have to grant each folder delegate access and walk through the folders  

You can look at samples on how to do that:  

https://www.michev.info/Blog/Post/2063/managing-mailbox-permissions-on-the-folder-level-in-bulk

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-07*

Yes full access will do that but I am trying to have access to ONLY the inbox and its subfolders. Full access show ALL of the Outlook default folders. Plus in the other tabs for Calendar, Contacts, To Do Lists it displays the user's info and this is not a desired result. Reason being is they have MULTIPLE calendars, to do lists, etc and having those appear without a need for them clutters the view.  

There a many subfolders and it would be tedious to have to go into each one and provide permissions individually.   

I thought that I would be able to provide access by using the ADD-MAILBOXFOLDERPERMISSION but this only provides access to the folder specified and not the subfolders.
