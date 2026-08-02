---
title: "Back Up and Restore ADFS Claim Descriptions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/51579/back-up-and-restore-adfs-claim-descriptions
question_id: 51579
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Back Up and Restore ADFS Claim Descriptions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/51579/back-up-and-restore-adfs-claim-descriptions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There,  

Is there a way to import Claim Descriptions into ADFS from a backup. I realise I can backup/export them to a file using Get-ADFSClaimDescription | Out-File “.\claimDesc.txt” but I'm not aware of a way to re-import them.  

I intend to make a number of Claim description additions and if anything goes south I'd like a backout plan that involves an easy rollback process.  

Is this possible?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-24*

Take a look on the AD FS Rapid Restore Tool. We use it to mirror our production enviroment to lab.    

Microsoft Learn    

Microsoft Download
