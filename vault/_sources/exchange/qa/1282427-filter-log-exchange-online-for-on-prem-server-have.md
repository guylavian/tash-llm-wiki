---
title: "filter log exchange online for on prem server have sent some mails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1282427/filter-log-exchange-online-for-on-prem-server-have
question_id: 1282427
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-hybrid-management", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# filter log exchange online for on prem server have sent some mails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1282427/filter-log-exchange-online-for-on-prem-server-have (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Morning , i have this question beacause i don't have found a solution , is possible to filter in exchange online a server on prem have sended some mail throught a SMTP in my enviroment ? inside this smtp don't have log enabled. in my infrastructure i have a application server with a service configured for use a internal smtp and that use 365 to send mails , my scope is to filter only mail sended from this only server, is possible ?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-12*

Hi @Anonymous  , 

my scope is to filter only mail sended from this only server, is possible ?

Do you mean you want to retrieve all mails sent from the application server? If so, as far as I know, from the perspective of Exchange Online, what we can do at present is to do a Content Search using some keywords or conditions. Are those mails sent through a specific email address? If this is the case, you can try creating a content search to find mails sent from the particular email address.  

Get started with Content search  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-11*

What do you mean by "filter"?

If you want to allow only that one machine to use your transport then alter the permission on the transport to restrict access to just that machines' IP address.
