---
title: "EXCHANGE 2019 On premise - Removing address from FROM field - Outlook Web Access"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/123190/exchange-2019-on-premise-removing-address-from-fro
question_id: 123190
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# EXCHANGE 2019 On premise - Removing address from FROM field - Outlook Web Access

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/123190/exchange-2019-on-premise-removing-address-from-fro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of our customer have add an address in the from field in Outlook web Access, unfortunately he have no rights to send from this address.  

He now ask me how to remove this address because it's confusing with another one.  

I just can't find how to do that...   

In order to reproduce the issue :  

1/ go to outlook web access   

2/ start typing a new mail  

3/ click on the 3 dot and show from  

4/ right click on your mail adress and select remove  

5/ type any other address where you have no send rights  

6/ try to send - receive the error  

7/ and now when you do show from try to remove the adress from the list.  

If you have any solution i'm clearly interested.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-12*

Hi,    

Could you please provide more information on this why you want to remove the FROM field. Usually, From Address is the primary SMTP address of the mailbox. For instance, if user A primary SMTP address is userA@Company portal   .com and this will be the address populated in FROM field. If userA needs to send email as userB, then userA needs to be assigned "Send-As" permission on UserB. Once permission is assigned, userA can change the FROM field to userB and send email. If the permission is not assigned, then the user will get an error "You don't have rights to send as this user" which is expected.    

You can also just remove the address in FROM field (leave it blank) and type the same email address in which you have logged in "TO" field and send a self test email.
