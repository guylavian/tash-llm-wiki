---
title: "ADFS FBL Raise Fail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/432454/adfs-fbl-raise-fail
question_id: 432454
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS FBL Raise Fail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/432454/adfs-fbl-raise-fail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I tried to raise the ADFS FBL with Test-AdfsFarmBehaviorLevelRaise  

Test-AdfsFarmBehaviorLevelRaise : Database upgrade cannot be performed on xxx Error: Connecting to remote server xxx failed with the following error message : WinRM cannot process the request. The following error with errorcode  

0x8009030e occurred while using Kerberos authentication: A specified logon session does not exist. It may already have been terminated.  

I checked that Windows Remote Manager service is running.  

I checked that TCP 5985 is not blocked.  

I am running the command on the primary server and it is a single node farm. I have checked the ADFS service is in good health before I run this command.  

Any advice on how I can raise the FBL?  

I am using a local admin account to raise the FBL. Is it that problem? If I can only use a local admin account, do I need to add certain permissions?

## Answers

_No answers on this thread._
