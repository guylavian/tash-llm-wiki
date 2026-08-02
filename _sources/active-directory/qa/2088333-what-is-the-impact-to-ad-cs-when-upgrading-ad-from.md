---
title: "What is the impact to AD CS when upgrading AD from 2012 to 2022?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2088333/what-is-the-impact-to-ad-cs-when-upgrading-ad-from
question_id: 2088333
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# What is the impact to AD CS when upgrading AD from 2012 to 2022?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2088333/what-is-the-impact-to-ad-cs-when-upgrading-ad-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently I have 2 domain controllers on Windows 2012, there is one CA server also on Windows 2012. I am planning to upgrade the OS of domain controllers to Windows 2022. I have doubt on the AD CS, and I can't find any information on the Internet regarding impact on AD CS if Domain Controllers are upgraded to Windows 2022 but the CA is still on Windows 2012.

Can anyone provide some insights on this scenario?

Do I have to upgrade the CA OS also to 2022? What happen if I don't upgrade the CA's OS, for whatever reason?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-10-05*

In short, you don't have to upgrade your Certificate Authority (CA) server to Windows Server 2022 if you're upgrading your domain controllers to Windows Server 2022. Active Directory Certificate Services (AD CS) on a Windows Server 2012 machine will still work and interact with domain controllers running Windows Server 2022.

However, it is recommended to eventually upgrade the CA to ensure long-term support and security updates, as well as compatibility with newer features that may be introduced in Windows Server 2022, especially considering that Windows Server 2012 is no longer supported by Microsoft. Keeping the CA on an older, unsupported version might expose you to security risks and compatibility issues down the line, though there shouldn't be an immediate functional impact just from upgrading the domain controllers.

In any case, you should consider testing the CA functionality in a non-production environment to ensure that the certificate issuance and revocation processes still work as expected after upgrading the domain controllers.

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
