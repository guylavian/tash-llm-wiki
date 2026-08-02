---
title: "Block access to open Active Directory users and computers for normal user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1075830/block-access-to-open-active-directory-users-and-co
question_id: 1075830
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Block access to open Active Directory users and computers for normal user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1075830/block-access-to-open-active-directory-users-and-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,    

As tested that every domain user has access to open Active Directory users and computers MMC, if RSAT tool install in any windows client machine. I checked in several forum that it's a normal behavior, but still need to ask that if there is any mechanism that we can prevent to view the User and computer mmc.    

Any suggestion is much appreciated.    

Thanks    

Mukesh Bisht

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-11-04*

You could restrict access to snap-ins    

https://support.microsoft.com/en-us/topic/you-must-explicitly-enable-mmc-snap-ins-that-you-want-to-use-before-you-enable-the-restrict-users-to-the-explicitly-permitted-list-of-snap-ins-group-policy-setting-in-windows-xp-and-in-windows-vista-81f45479-19cb-931c-f4fb-648cf21f5618    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-06*

Thanks for your response, yes we can do with GP MMC policy, but there are other ways to access the user details, I want to restrict by all the ways and only delegated users can access the AD data.    

Regards,    

Mukesh Bisht
