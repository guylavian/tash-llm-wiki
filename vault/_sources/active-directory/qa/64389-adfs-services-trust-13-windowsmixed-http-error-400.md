---
title: "/adfs/services/trust/13/windowsmixed HTTP ERROR 400"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/64389/adfs-services-trust-13-windowsmixed-http-error-400
question_id: 64389
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# /adfs/services/trust/13/windowsmixed HTTP ERROR 400

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/64389/adfs-services-trust-13-windowsmixed-http-error-400 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

we have the following end point enabled on our ADFS 2012 server  

/adfs/services/trust/13/windowsmixed  

the full url is https://xxxx.xxxx.xxx/adfs/services/trust/13/windowsmixed , however when we try to browse the url on the any browser we get an error   

This page isn’t workingIf the problem continues, contact the site owner.  

HTTP ERROR 400  

what do we to check from ADFS server side for this error and how to fix it.  

Regards  

Aamir Masthan

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-11*

400 is Bad Request. This endpoint is not intended to be used by a browser doing a GET. This is to request a token using the WS-Trust standard (you could do it programmatically using the WSTrustChannelFactory).    

This endpoint is not even enabled by default in recent version of ADFS.    

What are you trying to achieve?
