---
title: "Simultaneously opened Exchange Web Outlook (Owa) multiple users at different tabs the same browser"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/152341/simultaneously-opened-exchange-web-outlook-owa-mul
question_id: 152341
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Simultaneously opened Exchange Web Outlook (Owa) multiple users at different tabs the same browser

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/152341/simultaneously-opened-exchange-web-outlook-owa-mul (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

At the time I have Exchange 2010 and Exchnge 2016 (on different subnets) installed on our servers with set up Owa - Web UI Outlook.  

One famous mail service ___mail.com allows to open Simultaneously its Web UI for multiple users at different tabs of the same browser and allows to switch to each users maulbox simply changing tab.  

For example, the same browser:  

1 tab = mailbox of user Peter, some message is openned;  

2 tab = mailbox of user John, he looks Inbox folder;  

3 tab = mailbox of user Alex, he clean Spam folder.  

How is to reach such behaviourwithin Owa ?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

So sad.  

But I saw page at some site where editing of javascript at the server side (meaning Exchange) reaches this result.  

https://y0av.me/2011/04/10/owa2010users/  

Unfortunatelly link provided here targets to other sence site.  

I think I found a way around this problem, if you don’t mind editing one of the javascript source files at the server end:  

http://blog.leederbyshire.com/2012/11/09/how-to-enable-exchange-2010-multiple-outlook-web-app-sessions/

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-06*

@Иванов Иван      

Hi,    

Agree with michev and just in addition,if you would like to achieve it via OWA,the manager need to be assigned "full access" permission to the other users' mailboxes.    

For example,if you would like user1 to be able to manage user2's mailbox,you should:    

-  Access Exchange Admin Center    

-  Edit user2's mailbox    

-  Locate "mailbox delegation" and add user1 to "Full Access"    

    

Then user1 is able to open user2's mailbox via his OWA using the "Open another mailbox" feature.    

    

This method doesn't need the manager to know or input other users' passwords and I think it's more recommended when taking security issues into consideration.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-05*

You cannot, that's now how Exchange/OWA works. Best you can do is use the "open another mailbox" functionality, which still uses your own credentials.  

Use private mode/multiple browsers or add-ins such as Firefox's "container tabs"
