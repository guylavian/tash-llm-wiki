---
title: "Teams authentication with ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/561598/teams-authentication-with-adfs
question_id: 561598
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-teams-teams-business-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Teams authentication with ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/561598/teams-authentication-with-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I have questation about authentication in Teams. We have set ADFS with certificate support.   

I try connect to portal.office.com where is displayed organization window with select between forms and certificate authentication. This work also in teams.microsoft.com.  

But if I try authenticate in application Teams, the ADFS display only form based authentication. Not display certificate options... Is this set some in teams ? I want use certificate authentication...  

thanx

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-10-25*

Hi all,  

the trouble is difference certificate read proces betwen web client and onpremise teams app. Teams onpremise proces is "sandoxes" and cannot acess to local filesystem... thanx all
