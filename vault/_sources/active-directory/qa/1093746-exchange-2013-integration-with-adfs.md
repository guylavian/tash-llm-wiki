---
title: "Exchange 2013 integration with ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1093746/exchange-2013-integration-with-adfs
question_id: 1093746
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 integration with ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1093746/exchange-2013-integration-with-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have ADFS and Exchange server 2013. We are trying to integrate the setup as per the document https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019    

We can see that the assertions sent have proper UPN and primarysid. OWA access reports 401 on the browser. No event logs, IIS reports 401 client access.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-23*

@Amit Singh   Thanks for the response.    

I get this error only when I enable ADFS authentication. There is no issues with OWA or ECP when the basic authentication is On.    

I have followed the exact steps recorded in the document to turn on ADFS authentication in exchange. - https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019    

I have gone through all the possible logs in IIS. No records on why 401 error comes with ADFS. The assertion looks perfect. Im sending UPN and primarysid as suggested in the document.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-18*

Try to clear the cache of the browser, at the same time, recycle the OWA application pool, or restart IIS, and see if there is any difference.    

Also, check these threads and articles for help - https://support.microsoft.com/de-de/topic/authentication-loop-between-msft-sts-microsoft-com-adfs-and-owa-in-exchange-server-2019-and-2016-83385bac-7ee1-7c01-5f09-83bdceb40600    

https://community.spiceworks.com/topic/2291254-exchange-connectivity-issues-and-401-errors?page=1#entry-8992353

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-18*

@LilyLi2-MSFT   Thanks for the response.     

I'm following the same document and have configured as documented.    

When I access OWA, it gives me 401 error after ADFS authentication.    

When ECP is accessed, it ends up in loop.    

Assertions look good. No errors in the event viewer about the federation itself.     

I seem to have exact issue as described in the other thread. But that seems to be an unanswered one.    

Anything comes to your mind when you see the above description?    

I cant seem to find ways to enable OWA access logs.    

Any help is appreciated.    

Thanks
