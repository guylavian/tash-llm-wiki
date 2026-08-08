---
title: "Active Directory - Cross Forest account, log on as a service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/884948/active-directory-cross-forest-account-log-on-as-a
question_id: 884948
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Active Directory - Cross Forest account, log on as a service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/884948/active-directory-cross-forest-account-log-on-as-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey all    

Strange one, hoping you can provide some pointers.    

2 Forests, 2-way forest trust in place.    

Forest A has an account (Account1) that I am placing into a GPO in Forest B. That Forest B GPO is in order to specify account1 with log on as a service rights to an admin server in Forest B.    

When the end user in Forest B tries to run their application with this account1 from Forest A set to run the windows service, the service keeps crashing.    

Basically, whereas I can open my gpo in forest B, and I can browse to the account in Forest A from it no problem, it doesnt look like that account is being pushed down into secpol on the admin server.    

The forest B GPO in question has 4 other accounts in it, all of them are accounts from forest B and they are listed perfectly fine in the secpol of the admin server, but this forest A\account1 isnt showing in there.....    

I'm not sure if this is as it's meant to be, as in it wont show in secpol because it's cross forest, or whether i should be able to see it and the fact I cant indicates an issue pushing cross forest accounts out via gpo for that attribute, log on as a service.    

I think this should work fine, so i'm trying to workout where the fault may be.    

Coop

## Answers

_No answers on this thread._
