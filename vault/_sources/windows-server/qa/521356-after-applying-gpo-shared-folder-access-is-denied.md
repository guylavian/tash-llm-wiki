---
title: "After applying GPO, shared folder access is denied in Windows Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/521356/after-applying-gpo-shared-folder-access-is-denied
question_id: 521356
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# After applying GPO, shared folder access is denied in Windows Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/521356/after-applying-gpo-shared-folder-access-is-denied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two servers (Windows Server 2016, no domain is set)  

Among them, B Server will mount the specific folder of A Server in the system,  

And use the net use command to run the robocopy synchronization command through the Administrator account.  

However, after applying the GPO, the network drive connection is denied access.  

Tried the following operations, but still can't solve the problem:  

(1) Disconnect the network drive and run the command again, it will display "5 error in the system, access denied"  

(2) It is speculated that there is a problem with the SMB account-related settings, so restore the two server's SMB account-related settings to the default values. "System error 5 access denied" will still be displayed after restarting  

I don't know if there are other GPOs that need to be modified to synchronize the shared folders between the two hosts.  

Or are there other problems causing it?  

Thank you in advance for your help!

## Answers

_No answers on this thread._
