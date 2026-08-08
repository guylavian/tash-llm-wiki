---
title: "Is My Exchange Setup Hybrid and Ready for CU14 with Extended Protection?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1643503/is-my-exchange-setup-hybrid-and-ready-for-cu14-wit
question_id: 1643503
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Is My Exchange Setup Hybrid and Ready for CU14 with Extended Protection?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1643503/is-my-exchange-setup-hybrid-and-ready-for-cu14-wit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi 

I am currently using Exchange Server 2019 CU13 on-premises to relay emails from apps to O365 and to set up Exchange attributes on user accounts. There are no mailboxes on-premises since they are all in the cloud. 

After reading the docs, I noticed a note about a hybrid configuration, but I cannot see the Hybrid agent installed on any server on-premises. 

So this makes me think if my setup is hybrid at all? 

Could it be that the we just using ECP to write the Exchange attributes and then be synced via ADsyc? 

If my setup isn't hybrid, is it safe to install CU14 with Extended Protection?

Thanks, M

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-04*

Most likely you are using regular hybrid and not the agent. 

You can confirm by running:

Get-HybridConfiguration 

on-prem Exchange powershell
