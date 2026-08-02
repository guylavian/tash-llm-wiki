---
title: "unable to fetch users from Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/538332/unable-to-fetch-users-from-active-directory
question_id: 538332
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# unable to fetch users from Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/538332/unable-to-fetch-users-from-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All  

One of my IAM application fetches users from Active Directory using Object GUID. I have 60000 users in AD.  

For example the application fetches users by GUID=6a*, GUID=6b*, but for some GUIDs like 7a* the application is unable to fetch the users. i can see users in AD by 7a*  

is there any limitation from AD side for the application to fetch users like for example we cannot export more than 5000 users from AD security group using the syntax Get-ADGroupMember. It looks issue from application side but wanna confirm from AD side as well.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-02*

i can see users in AD by 7a*  

Based on this it sounds like the application has some issue.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
