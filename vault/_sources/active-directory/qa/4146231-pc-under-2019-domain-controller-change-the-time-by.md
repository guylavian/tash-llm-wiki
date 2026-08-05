---
title: "PC under 2019 domain controller change the time by svchost."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4146231/pc-under-2019-domain-controller-change-the-time-by
question_id: 4146231
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# PC under 2019 domain controller change the time by svchost.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4146231/pc-under-2019-domain-controller-change-the-time-by (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello 

I have a domain controller Windows 2019. 

This domain is in Egypt, and as you know, the daylight feature has been activated this year. 

I updated the domain so that the time zone can be changed without changing the region to Riyadh or Kuwait  

There are several Windows 10 devices under this domain, but without the update that is responsible for updating Time Zone because those PC is old. 

 This update depends on other updates that will make the pcs too slow, so we create a policy group was created to clone the registry files that are responsible for updating Egypt Time Zone and Dynamic DST from the domain to Clint PCs for a week till all PCs are updated by GP, It is confirmed that the recording files in the domain related to Time Zone Egypt and Dynamic DST have been copied and updated on the devices within that domain 

 but occasionally some PCs return to their old status and cancel the daylight option and switch it to OFF !!  

After returning to Regedit and following the paths of the change, I found that a change had been made in: 

Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones\Egypt Standard Time\Dynamic DST\2023 with different value from domain  

also, check the event viewer and we found this msg: The system time has changed to ‎2023‎-‎07‎-‎18T11:35:49.353327200Z from ‎2023‎-‎07‎-‎18T11:35:49.352900300Z.

Change Reason: An application or system component changed the time.

Process: '\Device\HarddiskVolume4\Windows\System32\svchost.exe' (PID 1684).

I want to know what makes the PCs change and turned the daylight off.

Thank You

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2023-07-18*

Good day Rami! I am glad to be able to provide assistance to you today. I would suggest to post this query to our neighbor forum from the link below as this is best suited in there. They are more oriented on with regards to this type queries/issues and there will be IT Pros/System Admins/Server Admins/AD Admins who are available that will be able to fulfill your query out there.

https://learn.microsoft.com/en-us/answers/

Regards,

Paul R.
