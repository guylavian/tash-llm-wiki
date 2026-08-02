---
title: "active directory user name issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194311/active-directory-user-name-issue
question_id: 1194311
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# active directory user name issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194311/active-directory-user-name-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello 

i have a user that log into is pc with the name "user1"

when i go look into the users folder i see the username is not the same 

i see "user2" in the ad i see the login is user1 but in the registries i see in profile list user2 

why is that ?

i know we change the login info before but the email is the same as before 

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-30*

ok i will check that 

but its not related to exchange account created that was using the other user as email ?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-30*

If you have changed the user name for the user in question before, I think the folder for the user is kept with the old name...or perhaps the attributes haven't fully synced. Here is a bit on how AD logons work. 

https://theitbros.com/samaccountname-and-userprincipalname/
