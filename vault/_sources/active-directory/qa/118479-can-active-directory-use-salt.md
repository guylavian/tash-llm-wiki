---
title: "Can Active Directory use SALT?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/118479/can-active-directory-use-salt
question_id: 118479
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Can Active Directory use SALT?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/118479/can-active-directory-use-salt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

An outside audit of our on-premise environment has dinged us for not using SALT in our on-premise Active Directory environment in conjunction with the normal encryption/hash used by AD. I have not been able to find a suitable answer about this, most posts are from 10 or more years ago with regards to AD user password storage. We are currently running a functional level of 2012.  

If AD can not use SALT, are there any good answers I can provide? I feel like it is not needed, we do not allow Domain Admins, etc.   

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-12*

Thanks, at least I have something that we can provide that is official.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-12*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-06*

Something here may help.    

https://www.microsoft.com/security/blog/2019/05/30/demystifying-password-hash-sync/    

https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-password-hash-synchronization    

--please don't forget to Accept as answer if the reply is helpful--
