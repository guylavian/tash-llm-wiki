---
title: "cannot Raise Active Directory Domain and Forest Functional on windows server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/876230/cannot-raise-active-directory-domain-and-forest-fu
question_id: 876230
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# cannot Raise Active Directory Domain and Forest Functional on windows server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/876230/cannot-raise-active-directory-domain-and-forest-fu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

cannot Raise Active Directory Domain and Forest Functional on windows server 2019 and getting following warning in the text box,  

"You cannot raise the domain functional level because this domain includes active directory domain controller that are no running the appropriate version of the windows"  

current domain functional level is windows server 2008 R2

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-06-03*

You can't raise the DFL any higher than the lowest OS domain controller.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-05*

Problem has been solved after changing schema version value data 69 to 88 from Registry Edit    

Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters    

Please see the screenshot

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-05*

My domain control is running on windows server 2019, As per attachment I cannot raise the domain functional level even my DC running on Windows server 2019
