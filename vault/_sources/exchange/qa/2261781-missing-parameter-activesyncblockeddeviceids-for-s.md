---
title: "Missing parameter ActiveSyncBlockedDeviceIDs for Set-CASMailbox command"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261781/missing-parameter-activesyncblockeddeviceids-for-s
question_id: 2261781
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Missing parameter ActiveSyncBlockedDeviceIDs for Set-CASMailbox command

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261781/missing-parameter-activesyncblockeddeviceids-for-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an automated powershell script which monitors devices and blocks or allows mailbox access based on certain criteria.   

This script has been working fine till date, but for one of our customers we get an error message that 'ActiveSyncBlockedDeviceIDs is an un recognised parameter for command Set-CASMailbox'  

The command used is as follows :   

Set-CASMailbox -Identity <emailAddress> -ActiveSyncAllowedDeviceIDs @{Add = <easDeviceId> } -WarningAction 'SilentlyContinue'  

We tried running the same directly from powershell as well, but still got the same error.   

Things we checked :  

mailbox has active license, has EAS enabled, user is able to successfully send and receive mails. 

Please advise on the above. Is there any case where blocking is not allowed or is it an actual issue?  

Permission given to Oauth app - Exchange.ManageAsApp  

Assigned role - Exchage Administrator

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-04-28*

Works here. Does it only fail for that customer?
