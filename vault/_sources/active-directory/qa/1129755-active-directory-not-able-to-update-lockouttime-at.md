---
title: "Active Directory - not able to update lockouttime attribute."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1129755/active-directory-not-able-to-update-lockouttime-at
question_id: 1129755
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory - not able to update lockouttime attribute.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1129755/active-directory-not-able-to-update-lockouttime-at (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

While Updating lockouttime attribute(as a large integer) for an user in active directory, getting below error.    

Operation failed. Error code : 0x57    

The parameter is incorrect    

00000057: SysErr: DSID-031A12C8, problem 22(Invalid argument), data 0.    

any help is appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-21*

Hi,    

As mentioned above it's not possible to set the lockout time attribute to a specific value, by setting the value to 0 (zero) the time is cleared.  Another option to try, which is available on other system based attributes, by setting the value to -1, it will set the current time and date.  I don't have a system to test it but it's worth a try.    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-15*

Hello there,    

You can't set this attribute to an arbitrary value in AD. This is a    

Microsoft imposed limitation.    

To unlock the account, set this attribute to "0"    

To lock the account simulate bad logins until you have reached the defined account lockout threshold    

Hope this resolves your Query !!    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-15*

Thanks @Aung Zaw Min Thwin    for your answer.      

https://learn.microsoft.com/en-us/windows/win32/adschema/a-lockouttime      

Above documentation says it has a update privilege with domain administrator. if it can be updated to only to 0, then is there any other attribute which i can use to lock an account manually.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-15*

In short, this attribute can be only set as 0 to unlock.
