---
title: "Server 2012 R2 std. generates Event id 37 Kerberos-Key-Distribution-Center log every 5-10 mins after applied Nov-2021 win update & kb5008603"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/630388/server-2012-r2-std-generates-event-id-37-kerberos
question_id: 630388
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Server 2012 R2 std. generates Event id 37 Kerberos-Key-Distribution-Center log every 5-10 mins after applied Nov-2021 win update & kb5008603

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/630388/server-2012-r2-std-generates-event-id-37-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After installed KB890830 and KB5007247 on two DC,  Microsoft-Windows-Kerberos-Key-Distribution-Center warning log is triggered nearly  every 5 mins.     

Also installed below fix manually.    

https://support.microsoft.com/en-us/topic/kb5008603-authentication-fails-on-domain-controllers-in-certain-kerberos-scenarios-on-windows-server-2012-r2-1beea7a1-9a3c-48dd-a56d-c3cc3f5d0d50    

Bus still appears those log    

    

Please advise how to fix. Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-23*

Hello, I have the same issue, someone know a fix to remediate this situation?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-22*

This is described here:  

https://support.microsoft.com/en-gb/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041  

Like many patches of Microsoft lately - this patch needs action after installing it.  

-  Update all devices that host the Active Directory domain controller role by installing the November 9, 2021 update.  

-  After the November 9, 2021 update has been installed on all Active Directory domain controllers for at least 7 days, we strongly suggest that you enable Enforcement mode on all Active Directory domain controllers.  

-  Starting with the July 12, 2022 Enforcement Phase update, Enforcement mode will be enabled on all Windows domain controllers and will be required.  

So these warnings are normal until all your DCs has the enforcement mode enabled. Or it is forced on July.  

As it is rolled out like this - this seems to need some testing beforehand ;)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-19*

Both DC has installed with latest windows update and installed kb5008603 manually.    

Event id 37 Kerberos-Key-Distribution-Center warning log were gone after those client computers were turned on next day.  Found that log record were related to different client computer. So it liked that appeared every several minutes. Actually, every client computer name are triggered in every hour. (Not every several minutes)    

Also found that less event ID 37 log were still appeared next day as those clients were not power off PC after work. The warning log won't appear again after restarted those client computers.    

But still have another Event ID 35 warning log. It's related to both DC only.     

Same issue as    

https://community.spiceworks.com/topic/2338789-event-id-35-and-37-kerberos-on-server-2019
