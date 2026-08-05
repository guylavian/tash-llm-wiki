---
title: "user athenticate to far domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/740381/user-athenticate-to-far-domain-controller
question_id: 740381
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# user athenticate to far domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/740381/user-athenticate-to-far-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a standard wtitable DC and some RODC on different subnet.   

Under site and services I've setup all the different subnet and associate each RODC to the correct subnet  

If I open a RODC  property (from domain user and computer), password replication policy, advanced, I see a lot of user from the main office that has been authenticated to the remote RODC.  

Why this happen?  

Thank you  

Alessandro

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-26*

Is there a way to reset the list of logged user on a rodc? Just to check if it happen again

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-18*

I've discovered that a subnet was not associated to the site, and I've corrected.  

Is there a way to reset the list of logged user on a rodc? Just to check if it happen again

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-17*

Read on here about troubleshooting.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/how-domain-controllers-are-located#troubleshooting-the-domain-locator-process    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
