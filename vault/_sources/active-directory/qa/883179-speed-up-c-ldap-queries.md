---
title: "Speed up C++ LDAP queries"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/883179/speed-up-c-ldap-queries
question_id: 883179
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-cpp", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Speed up C++ LDAP queries

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/883179/speed-up-c-ldap-queries (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently developing a Node.js addon to make it possible to query from Typescript whether a specific AD user is member of a given AD group.    

We got the final application already installed on some systems but it turns out that sometimes the LDAP query resolutions is very slow.    

Therefore I'm now looking for more improvement options that I could suggest to the customers or implement into my code to make the code more versatile.    

Internally I'm using an `IDirectorySearch` object to run the search.    

I already tried out options like "ADS_SEARCHPREF_ASYNCHRONOUS", "ADS_SEARCHPREF_CACHE_RESULTS" to make queries faster but I never had success.    

Things that I can imagine that could possibly speedup queries:    

-  Install a separate microsoft service on the machine on which my software is running which then caches ldap or syncs with it. Is there something like this?    

-  A way to find the server that has all required information for my search in-memory - Since I need to bind rootDSE before I can execute a search on active directory, is there a way to control which server that itself identifies as rootDSE I will query? What attributes does that server have to offer?    

One query in my case looks like this:    

"&(ObjectClass=User)(memberOf:1.2.840.113556.1.4.1941:= <some identifying props>))"    

In some cases queries take up to 40 seconds which is not acceptable for an on-prem web app.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-06-13*

Hi there,    

Capture a network trace, we can look into it to troubleshoot further.    

Follow these general tips to improve search performance    

-Always ensure that the server being tested has a copy of every partition in the tree. Retest after adding all of them.    

-If possible, use one-level searches instead of subtree ones. They are usually faster.    

-Whenever doing a subtree search, avoid using a presence filter.    

-If you have a thousand or more alias objects, avoid alias dereferencing in the search.    

New sessions setup for LDAP services take longer than expected if targeting host names https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/ldap-session-takes-longer-target-host-names    

-If search performance is still slow, determine if indexes need to be added.    

--------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–
