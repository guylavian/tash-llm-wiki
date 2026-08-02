---
title: "Exchange 2010 to Exchange 2016 mailbox move - OWA/Outlook not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/431637/exchange-2010-to-exchange-2016-mailbox-move-owa-ou
question_id: 431637
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2010 to Exchange 2016 mailbox move - OWA/Outlook not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/431637/exchange-2010-to-exchange-2016-mailbox-move-owa-ou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have installed Exchange 2016 servers on our existing Exchange 2010 environment.  

There's a load balancer (host: owa.domain.com) that routes traffic to Ex2010 CAS servers.  

Now, we just did a cutover so that owa.domain.com now points to Exchange 2016 servers.  

After the cutover, we found the following:  

-  Ex2010 mailbox working fine on owa/outlook  

-  We migrated one mailbox from Ex2010 to Ex2016 database, after migration we cannot access the mailbox using https://owa.domain.com / outlook.  

-  But, after the mailbox migration, the mailbox can be accessed if we access it using the Ex2016 server name (https://Ex2016/owa)  

To summarize, the mailboxes hosted on Ex2016 server/db are only accessible if we access it via https://Ex2016/owa url , but its not working if we use the load balanced host - https://owa.domain.com  

Can anyone please help to fix the issue so that we can also the Ex2016 mailboxes using owa.domain.com url ?  

Thanks in advance.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-06-17*

Hi @Kai Yao   ,    

Thanks for your response.    

We found that the Load Balancer +WAF was blocking the client connections. This is because at the LB/WAF, only the urls/cookies/headers related to Exchange 2010 were allowed. Since Ex2016 has additional urls/cookies/headers on the requests (made by client), these requests were being blocked at LB.    

I asked MS support to provide a list of URLs/Cookie names/ headers that are used in Ex2016 owa/ecp communication, but they said no such list is available. Currently we are manually whitelisting each new URLs/cookie/headers in the LB to make it work.    

If you have any other suggestions, i would be happy to test it.    

Thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-14*

Hi @Rupam       

When you access the URL owa.domain.com/owa, did you see the legacy Exchange 2010 OWA interface?    

And what is the detailed error message when you fail to login?    

Please try adding ?ExchClientVer=15 to the URL (owa.domain.com/owa?ExchClientVer=15) and see if you are directed to the Exchange 2016 OWA interface.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
