---
title: "update to Windows 21H2 and Active Directory Users and Computers disappeared"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/873476/update-to-windows-21h2-and-active-directory-users
question_id: 873476
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# update to Windows 21H2 and Active Directory Users and Computers disappeared

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/873476/update-to-windows-21h2-and-active-directory-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two users who have rights to reset/unlock user accounts using RSAT tools which have been renamed to Administrative Tools now. Since our update to 21H2, ADUC has disappeared from the admin tools area listed in the Windows menu.   

When I navigate to Optional Features, there are no choices listed at all the search is blank when I type in RSAT as instructed by many sources on the internet. I still see Administrative tools in the start menu, but just no  option for ADUC and not option to re-install/enable Admin tools in optional features.   

Does anyone know what happened and how to get ADUC back for our non-admin users?   

Thank you.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-06-03*

It shows up here for me

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-06-01*

Try Settings\Apps & features\Optional Features\Add feature  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-03*

Hello DSPatrick,   

I did log in as local admin, and found that things were now listed in the Optional Features, that was a great help. Now, in that list there is no listing for ADUC so the saga continues. Thank you for your tip about the local admin. :-)  

Best,   

MG

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-02*

Make sure the user adding features is a local administrator.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-02*

Hello DSPatrick, as stated above, when I go to optional features, there are no features listed to add, or to pick from a list.     

    

ADUC was available under Administrative Tools when 20h1 was installed, post update to 21H2, No longer listed as an option in the menu.     

Thanks for your comment.     

Best,     

MG
