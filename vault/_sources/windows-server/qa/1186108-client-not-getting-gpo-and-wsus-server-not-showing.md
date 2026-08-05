---
title: "Client not getting GPO and WSUS server not showing computer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186108/client-not-getting-gpo-and-wsus-server-not-showing
question_id: 1186108
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Client not getting GPO and WSUS server not showing computer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186108/client-not-getting-gpo-and-wsus-server-not-showing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Applied the GPO: nothing showed on the gpo result theres 2 gpo applied but techincally it should be 1 - I moved the PC to the correct OU for the GPO to get applied after I ran "gpupdate /force" the "wsus" GPO should only applied to this client but the other one "WSUS-Update" it came from my 1st site; this client is in 2nd site

I set the update server from  http://wsus.Qasim.local:8530

This is the second WSUS in Site 2

Second WSUS server is synced from the site 1 wsus server. It got all the updates.  

Now for the: set the intranet update service for detecting updates server should I put the updates receiving from Main WSUS or the second WSUS server?  

Main WSUS is in site 1 and second wsus server is using the main wsus server as upstream to get teh updates.  

site 1 wsus server gets its update from "mircosoft server"  

Highlighted is the only one am filling

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-03-04*

I'd recommend reading through my guide. It will explain how to setup your GPOs for an inheritance setup which is what you're attempting to do with the multiple sites.

https://www.ajtek.ca/wsus/how-to-setup-manage-and-maintain-wsus-part-5-linking-your-gpos-inheritance-is-your-friend/

I've linked directly to part 5 which deals with the applying of the GPOs, however I'd recommend reading the entire series as each part builds from the last.
