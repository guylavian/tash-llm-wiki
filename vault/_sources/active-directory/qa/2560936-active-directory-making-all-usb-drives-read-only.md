---
title: "active directory making all usb drives read-only"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2560936/active-directory-making-all-usb-drives-read-only
question_id: 2560936
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# active directory making all usb drives read-only

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2560936/active-directory-making-all-usb-drives-read-only (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A new client has an old 2003 SBS (not r2) and a few vista and windows 7 workstations sometime this week it changed the usb settings on all computers to Read Only and they use usb drive to transfer files to outside employees  

if i change  Reg HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\StorageDevicePolicies from 1 to 0 it will be switched back shortly there after however the flash drives will work during that time  

i checked the Group Policies and do not see any changes in the last 2+ years  

only thing that has changed in this network in the last 2 weeks is replacing an old xp with a new win 7

there was also some updates done and i will review if any of them should have made the change but i do not think that is it  

what would be a way i could override the servers wanting to move everyone on the domain to read only removable storage

ps the server usb drives will work - but no workstation

## Answer (community) — community member

*upvotes: 0 · updated: 2013-09-14*

Hi Alan, 

The issue you have posted would be better suited in the
TechNet Forums. I would recommend posting your query in the link below.

**http://social.technet.microsoft.com/Forums/en-US/home?forum=smallbusinessserver**​

Have a Nice day!
