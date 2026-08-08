---
title: "adding second adfs server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/51537/adding-second-adfs-server
question_id: 51537
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adding second adfs server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/51537/adding-second-adfs-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I like to confirm below steps as we are planning to add second adfs server and create a farm.   

Currently we have adfs running on server 2012r2 ... with adfs1.domain.com   

and dns entry as adfs.domain.com (using for dropbox,zoom, adobe etc etc)  

now to add second server build server 2012r2  name adfs2  

export communications SSL from adfs1 and import in adfs2  

run wizard for new install and add to farm ?  

we have WID no SQL db  

once its done in dns add point adfs2 also ?  

What about Token - encrypting / signing situation ?   

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-24*

now to add second server build server 2012r2 name adfs2  

export communications SSL from adfs1 and import in adfs2  

run wizard for new install and add to farm ?

Basically your describe steps are right.  

Did you create a FARM when you set up the first AD FS server?

we have WID no SQL db

That is no problem. WID supports up to +- 20 AD FS instances.

What about Token - encrypting / signing situation ?

Export and import the required ssl certificate(s) from the first AD FS serverbefore you start the configuration wizard on the second AD FS server.

Note: It is recommended to use a hardware or vitual load balancers for your szenario. The Windows LNB ist not right product for it.
