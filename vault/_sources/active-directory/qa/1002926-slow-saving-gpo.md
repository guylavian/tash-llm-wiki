---
title: "Slow saving GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1002926/slow-saving-gpo
question_id: 1002926
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Slow saving GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1002926/slow-saving-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

At one of our clients, I've having trouble when I edit a GPO using GPMC on a W2K16 AD domain (3 DCs on the same site) : every time I save it, it takes more than 30s! I never see this behaviour before.    

I've no problem to apply a GPO on workstations or servers, but only to save it.    

I've tried to connect to different DC, same thing.    

Replication accross DC are correct.    

DFSR is enable.    

Any ideas where this problem could come from? I'm going crazy.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-12*

Hello Garry,    

Yes already checked, according to the recommendations of MS. Replications work well between DCs.    

DCs are VM with 10Gb of bandwidth so no slow network link.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-12*

Hi @WebGTA      

Have you checked the status of the sysvol share on the domain controller holding the PDC role.  By default the GPMC will try and make GPO changes on the PDC of the domain, if there is a connectivity issue, slow network link, or issues with sysvol, then this might explain the delays you are seeing.    

Gary.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-12*

You can enable Procmon and Netmon to check the processes and Network Traffic to analyse the packets, this should give you clear view of the time delay and lag.    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-12*

Thank's for reply.    

Whatever the GPO: a new one, a copy, it's always the same problem.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-12*

Hi,    

Can you make a copy of the GPO and try to edit the new GPO and save? Also check the permissions on the GPO any unresolved SID's?    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
