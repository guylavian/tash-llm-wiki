---
title: "Active directory and screen lockout"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/955424/active-directory-and-screen-lockout
question_id: 955424
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active directory and screen lockout

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/955424/active-directory-and-screen-lockout (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I work for a production organization and we have a number of terminal screen's that our on-the-floor employees use to send ordering info, clock in/out and so on. I am looking for a way to set these machines to never log out or go to a lock screen. I have disabled about everything in windows and much googling can not find a way to stop them from logging out after inactivity. Is there something in active directory users and computers or GPO that I can setup or change?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-04*

Im sorry but I have done this on all of them and still logging out after inactivity. That's why I'm thinking of something in active directory I can set?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-08-04*

Ok, well that sounds like you may just need to turn off the secure screensaver    

    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-04*

Nope each computer is its own workstation but with the same login/domain user. so something like user- rds pass- rds    

Once the screen times out you have to enter the login info again this is what I am trying to stop from happening. All terminal screens are connected to our local domain.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-08-04*

we have a number of terminal screen's    

Are you asking about remote desktop?
