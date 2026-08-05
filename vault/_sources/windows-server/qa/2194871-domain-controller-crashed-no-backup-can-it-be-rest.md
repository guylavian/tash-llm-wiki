---
title: "Domain controller crashed, no backup can it be restored thru ntds folder or can a new forest/domain created and import data from old ntds folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194871/domain-controller-crashed-no-backup-can-it-be-rest
question_id: 2194871
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 4
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Domain controller crashed, no backup can it be restored thru ntds folder or can a new forest/domain created and import data from old ntds folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194871/domain-controller-crashed-no-backup-can-it-be-rest (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Domain controller crashed, no backup can it be restored thru ntds folder or can a new forest/domain created and import data from old ntds folder

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-28*

Hello Mohammad Mazhar Ullah,  

Thank you for posting on the Microsoft Community Forum.  

Do you have only one Domain Controller in this domain? 

If so, after a domain control crash, if you do not have the original backup, you cannot directly restore it through NTDS or import it from an old NTDS file after creating a new forest/domain. 

You can only try to rebuild an environment similar to the previous domain controller after creating a new forest/domain. 

I suggest that you had better backup the domain controllers in the environment in future and restoring them after backup if needed.  

This is an article about backing up domain controller: 

AD Forest Recovery - Backing up a full server | Microsoft Learn

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
