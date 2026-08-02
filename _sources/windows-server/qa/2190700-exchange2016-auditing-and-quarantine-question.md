---
title: "Exchange2016 Auditing and Quarantine question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190700/exchange2016-auditing-and-quarantine-question
question_id: 2190700
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-performance-windows-desktop-shell-experience"]
---
# Exchange2016 Auditing and Quarantine question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190700/exchange2016-auditing-and-quarantine-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone ,

first of all I am sorry if this has been answered before but I really could not find the answer or

similar topic.

I have a big issue that persists over some years but I left it because I did not need that functionality,

but know I really need it.

I have 4 Exchange server 2016 , with more than 5000 users. And I live in a country where people have multiple nationality.

I have all servers set up to the last CU and SU . 

The Problem is as following :

I needed to set up the audit on Exchange , and sadly it does not work like intended . If you put in a parameter you get an empty answer . If you put in the Command Search-AdminAuditLog whitout parameter it is working to an extend. 

So I researched this issue and saw that a fix is there with a CU , but this didnt solve the problem as I was up to date. So I had to do the recommended work around , with the regional settings. 
https://learn.microsoft.com/en-us/exchange/troubleshoot/compliance/search-adminauditlog-mailboxauditlog-return-no-result

With this the admin audit search worked but I got another big problem with this. And this issue I could not see it at any other place documented.

The Users on the several Exchange servers got put their mailbox into Quarantine (not all users). 

So when an user send an email to an person that was affected got an reply that the message could not be delivered, because the inbox is in quarantine.  

Upon further investigation I found out that the users had a common setting in the regional / local settings EN-150 . 

Taking an user out of it , makes him go in after a while automatically.

And I had to revert the changes I did with the configuration of the regional settings on the servers , so that the users do not get quarantined anymore. 

But now I still cannot do any audit search. 

So I desperately need help in this regard if possible please.

Thanks a lot in Advance

Best Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-06*

You're welcome!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-04*

Thank you very much . I will do that.
