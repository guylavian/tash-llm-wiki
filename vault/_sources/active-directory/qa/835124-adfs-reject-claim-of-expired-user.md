---
title: "ADFS - Reject claim of expired user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/835124/adfs-reject-claim-of-expired-user
question_id: 835124
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS - Reject claim of expired user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/835124/adfs-reject-claim-of-expired-user (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I came across a scenario where there is a 3rd party Claim Provider Trust configured in ADFS.  

The issue is that ADFS is not checking if the user account is expired in AD.  

Any idea on how to this?  

Thanks for the help

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-05-05*

You could query the accountExpires attribute in AD, but the format is NTTE (NT system time, in (10^-7)s intervals from 0h 1-Jan 1601) and can't be parsed easily without using a custom attribute store. There's no easy way to do that, because quite frankly the authentication should have failed.  

Which brings me to the following question: if the user exists in AD, why not using AD as a claim provider and grabbing additional info after auth to where you currently auth the user?
