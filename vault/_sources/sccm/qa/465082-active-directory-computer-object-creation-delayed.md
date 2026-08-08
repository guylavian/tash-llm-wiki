---
title: "Active Directory - Computer Object Creation Delayed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/465082/active-directory-computer-object-creation-delayed
question_id: 465082
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-deployment", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Active Directory - Computer Object Creation Delayed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/465082/active-directory-computer-object-creation-delayed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I currently have an interesting phenomenon in an environment I manage. Devices are deployed using Configuration Manager CB 2010 incl. all hotfixes. The Tasksequences do not return any errors and the device is fully functional when the TS ends. Any domain user can login to the machine without problems.  

However, there is no device object in Active Directory. Like none. Searching for the computername in the advanced search yields no results. Running a gpresult on the device confirms this as there are no policies applied.   

We thought it may be replecation, but even when manually triggering DC replication, the device object simply does not appear. After about 30 Minutes, miraculously the device object appears in the OU designated in the CM TS.  

I'm almost certain it has nothing to do with CM as the device itself is fully functional. But I have no idea where to start looking in AD for a hint to why the device object is created with so much delay.  

Can anyone give us some pointers?  

Cheers,  

Fred

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-06*

May be normal and expected depending on which one is checked first. Replication from one DC to the next is 15 minutes by default in it's own site, and inter-site replication defaults to 180 minutes.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-06*

How is the TS configured to join the domain? With a separate Join Domain task or using the standard Apply Network Settings task?
