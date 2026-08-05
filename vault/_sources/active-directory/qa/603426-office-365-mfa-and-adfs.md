---
title: "Office 365 , MFA and ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/603426/office-365-mfa-and-adfs
question_id: 603426
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Office 365 , MFA and ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/603426/office-365-mfa-and-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

sorry for my englisch. I have questation about Office 365 and MFA and ADFS.  I have set  MFA in the Office 365 , but after i try connect to office 365 , the authentication process return MicrosoftOnline no strong authentication. We must reconfigure ADFS for MFA ? I want only MFA for claud application, thanx

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-10-26*

You can use either Azure MFA or configure the MFA adapter for AD FS and force it "locally", before hitting Office 365. The "supportsMFA" switch controls whether Office 365 will "respect" the on-premises MFA claim. Here's a more detailed article: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ad-fs-and-azure-mfa
