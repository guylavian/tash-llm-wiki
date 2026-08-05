---
title: "Is it possible to restore the Domain Controller from vhdx backup as a regular backup?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2128096/is-it-possible-to-restore-the-domain-controller-fr
question_id: 2128096
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Is it possible to restore the Domain Controller from vhdx backup as a regular backup?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2128096/is-it-possible-to-restore-the-domain-controller-fr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to restore the Primary Domain Controller (which holds all 5 roles) from a regular backup as a file server (the entire vhdx disk)? I did it with Acronis home edition. I have a laboratory environment, 4 domain controllers in different sites, one domain in the forest. I have restored all 4 domain controllers in this way. Right now I have the only SYSVol failed replication error when I run dcdiag/q. As far as I know, the PDC needs to be restored from System State in authoritarian mode. However, I found an article that says that it is possible to restore the PDC in this way, you only need to set the value 1 for msDFSR-Options after recovery and restart the DFSR service. But nothing seems to have helped, even after restarting all 4 controllers.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-12-08*

Follow https://community.spiceworks.com/t/how-to-re-build-sysvol-dfsr-replication-group-without-demoting-promoting-dc/1012727

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
