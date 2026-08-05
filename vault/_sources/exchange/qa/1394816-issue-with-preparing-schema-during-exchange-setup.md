---
title: "Issue with Preparing Schema during Exchange Setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1394816/issue-with-preparing-schema-during-exchange-setup
question_id: 1394816
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue with Preparing Schema during Exchange Setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1394816/issue-with-preparing-schema-during-exchange-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm experiencing issues with the Prepare Schema step during Exchange Setup on both my Domain Controller and Exchange server. Running PS as Admin: "The Schema isn't up-to-date, my user account is a member of 'Schema Admins' or 'Enterprise Admins', and Setup encountered a problem while validating the state of Active Directory."  

I'm not sure why Prepare Schema is failing to communicate with AD. I've tried preparing schema and AD on the DC, and have verified that ports 53, 88, 135, 389, 445, 636, 3268, 3269 are open, group memberships are correct and AD DS services are running, and replication is healthy. The firewalls are temporarily disabled, and DNS and network configs are good. The error message states that Setup couldn't find the Enterprise Organization container, but the Forest and Domain levels are good, and the FSMO role is on the primary DC. Also, there are no previous ADSI CN=Microsoft Exchange System Objects. I'm using DC WS 2022 and Exchange 2019_CU12 or CU13.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-18*

Hi @Jason S  ,

Based on the description of your problem, it is recommended that you run the script on the Domain Controller and Exchange server and check if it could return more detailed information about this issue.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
