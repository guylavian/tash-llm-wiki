---
title: "Test-AdfsFarmBehaviorLevelRaise error WinRM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/597581/test-adfsfarmbehaviorlevelraise-error-winrm
question_id: 597581
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 4
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Test-AdfsFarmBehaviorLevelRaise error WinRM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/597581/test-adfsfarmbehaviorlevelraise-error-winrm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I tried to raise the ADFS FBL with Test-AdfsFarmBehaviorLevelRaise:  

Database configuration successfully retrieved.  

Verified that the server is the primary node in the WID farm.

Test-AdfsFarmBehaviorLevelRaise : Database upgrade cannot be performed on *. Error: Connecting to remote server * failed with the following error message : WinRM cannot process the request. The following error occurred while using Kerberos authentication: Cannot find the computer ***. Verify that the computer exists on the network and that the name provided is spelled correctly.

The configuration database cannot be upgraded. Database upgrade cannot be performed on *. Error: Connecting to remote server *.  

Successfully verified that new built-in relying party trusts can be created.

*** - primary server.

I checked that Windows Remote Manager service is running.  

I checked that TCP 5985 is not blocked.

I am running the command on the primary server. I have checked the ADFS service is in good health before I run this command.  

I am using a domain account to raise the FBL.

Any advice on how I can raise the FBL?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-10-22*

Are you running it from an elevated PowerShell console?
