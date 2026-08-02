---
title: "How to check the adfs version"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/380494/how-to-check-the-adfs-version
question_id: 380494
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How to check the adfs version

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/380494/how-to-check-the-adfs-version (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to check the adfs version  

I see the official documents are adfs2012, 2016, 2019  

But there are also adfs1.0, 2.0, 3.0  

What is the difference between them?  

Or is there a corresponding relationship?  

Where should I check my version in the system

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 3 · updated: 2021-05-03*

AD FS is a Windows Role since Windows Server 2012 R2. It comes with the OS. Therefore, the different versions are just the refering to the different OSes on which the role is installed.   

AD FS 1.0 was the ADFS role in the product since Windows Server 2003 R2.  

Starting 2008 all the way to 2012, AD FS 2.0 was a RTW (release to the web) and you had to download the binairies. If you installed the default binaries of the OS, it would installed AD FS 1.  

AD FS 3 is often used to refer to AD FS on Windows Server 2012 R2.  

AD FS 4 is often used to refer to AD FS on Windows Server 2016.  

In a nutsell, on a supported OS, checking the version of AD FS is basically checking the version of the OS.
