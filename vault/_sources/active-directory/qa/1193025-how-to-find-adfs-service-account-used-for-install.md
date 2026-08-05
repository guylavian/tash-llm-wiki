---
title: "How to find ADFS service account used for install"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193025/how-to-find-adfs-service-account-used-for-install
question_id: 1193025
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How to find ADFS service account used for install

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193025/how-to-find-adfs-service-account-used-for-install (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I am extremely new to ADFS, how can I determine what service account was used to setup & configure ADFS server? I am trying to renew the token signing & decryption certificates with the Update-ADFSCertificate PowerShell cmdlet and I get an error so I want to rename and re-create the ADFS certificate sharing container and I need to make sure the same service account is used. I am also wondering why even though the Set-Adfsautomaticrollover is set to TRUE and the threshold is 20 days and since my current cert expires on 4/11/2023 and the 20 days have come no new cert was created. From what I found online I need to run the Update-ADFSCertificate command, is this correct or does it really automatically create a new one? 

One last thing,

when renaming and re-creating the ADFS certificate sharing container will this break any of my connections?

## Answers

_No answers on this thread._
