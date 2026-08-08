---
title: "the Sysvol_DFSR folder cannot be sync in couple of the 8 domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1014064/the-sysvol-dfsr-folder-cannot-be-sync-in-couple-of
question_id: 1014064
fetched: 2026-07-25
answer_count: 20
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# the Sysvol_DFSR folder cannot be sync in couple of the 8 domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1014064/the-sysvol-dfsr-folder-cannot-be-sync-in-couple-of (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi everyone,    

Working hard Monday~~ I hope you can help on this. We are still running in Windows 2012 domain, but I did the "DFSR" procedures couple months ago so I can add any newer OS of DC soon. We have total 8 DCs in the network.    

Now my colleague just reported this issue to me. He just updated the logon script. He could see the update propagate to most of the DCs but not two of them, each on different locations. I ran the repladmin command but did not see any errors. I also check their dns settings in the network properties and the info is correct.    

I rebooted one of the DCs. However it still not show up the changes in the sysvol_dfsr folder. May I ask what could cause the issue and how do I make the sysvol_dfsr folder in sync again?Thank you for your help in advance.    

Takami Chiro

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

HI DSPatrick,    

Thank you for your prompt response again :)    

I will check the event log first. I will keep you posted and see if this works.    

Thank you!    

Takami Chiro

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-09-19*

Yes, that's correct. Check the DFS Replication event logs for errors / clues as first step. Then if needed follow the steps listed here.    

In Step 1, "modify the following distingusihed name" , what do I need to change to?    

msDFSR-Enabled=FALSE    

do I need to make any change on all the DCs or just the one having the issue?    

just the one(s) having issues.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

Hi DSPatrick,    

Thank you for your quick response! I just reviewed the instruction... I would like to ask:    

1.) Only perform this on a server with the issue?    

2.) In Step 1, "modify the following distingusihed name" , what do I need to change to? Besides, do I need to make any change on all the DCs or just the one having the issue?    

Thank you for your help~    

Takami Chiro

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-09-19*

I'd check the DFS Replication event log for errors / clues. If need you can perform a non authoritative sync on the problematic ones    

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
