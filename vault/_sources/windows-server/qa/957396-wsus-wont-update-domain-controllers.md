---
title: "wsus wont update domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/957396/wsus-wont-update-domain-controllers
question_id: 957396
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# wsus wont update domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/957396/wsus-wont-update-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi    

my local  wsus server dont join domain .i have 10 additional  server.    

all the additional  server see wsus but dont automatically update and must manually update additional   form local wsus .local wsus 2019 windows and domains 2012.    

228627-windowsupdate.log

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-08-06*

Much of the time, people forget that Domain Controllers have their own OU. Make sure you attach the GPO that carries your WSUS Location information to your Domain Controllers OU.    

https://www.ajtek.ca/wsus/how-to-setup-manage-and-maintain-wsus-part-4-creating-your-gpos-for-an-inheritance-setup/    

and     

https://www.ajtek.ca/wsus/how-to-setup-manage-and-maintain-wsus-part-5-linking-your-gpos-inheritance-is-your-friend/
