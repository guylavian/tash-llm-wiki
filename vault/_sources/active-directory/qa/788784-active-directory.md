---
title: "active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/788784/active-directory
question_id: 788784
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/788784/active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have application run locally on some computers in my network  

I need to run them from active directory.  

I don't have to source application on the server so I need to run them automatically from the active directory once login & when user press exit it goes to the login page again.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-27*

Here you go.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/single-application-sharing-with-terminal-server    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-27*

OK if I put the path of the exe file in the destination PC in the "run this program in start up" in AD GP  

it will open from the PC or from the Server?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-27*

@Ahmed Darwish  ,    

How about the following method?    

Put the software on the network drive.    

\myserver\Start.exe    

Then deploy it using GPO.    

https://social.technet.microsoft.com/Forums/en-US/fa56dd0d-8c49-4a18-bd13-c140fb33039e/create-gpo-to-deploy-shortcut-in-desktop-folder?forum=winserverGP

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-27*

actually I don't know   

as I said I have application run locally in multiple PC's & I want the user once he login it open this application through GP in active directory.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-27*

Hi @Ahmed Darwish  ,    

Do you meant that you want to use an AD integration for a login?
