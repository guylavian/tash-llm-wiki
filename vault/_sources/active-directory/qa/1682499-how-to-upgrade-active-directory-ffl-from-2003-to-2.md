---
title: "How to Upgrade Active Directory FFL from 2003 to 2016 ??"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1682499/how-to-upgrade-active-directory-ffl-from-2003-to-2
question_id: 1682499
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to Upgrade Active Directory FFL from 2003 to 2016 ??

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1682499/how-to-upgrade-active-directory-ffl-from-2003-to-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

We have an Active Directory environment with 2003 FFL and 2008 DFL. We plan to upgrade FFL to Windows Server 2016. What are the key considerations and the process we need to follow to upgrade both FFL and DFL to the latest version?

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-20*

Hello,

Thank you for posting in Q&A forum.

When upgrading the FFL (Functional Level) of the Active Directory environment from Windows Server 2003 to Windows Server 2016, the following key factors and steps need to be considered:

Before upgrading, be sure to back up Active Directory data to prevent accidental data loss.

Ensure that all domain controllers comply with the system requirements of Windows Server 2016 and have installed the latest updates and patches.

Ensure that applications and services are compatible with Windows Server 2016 to avoid compatibility issues after upgrading.

Upgrade DFL and FFL using the Active Directory User and Computer Management Tool (ADUC).

Right click on the domain in the Active Directory User and Computer Management tool, select "Upgrade Domain Functional Level", and then select the target functional level.

Monitor the status and event logs of the domain controller during the upgrade process to ensure there are no errors or warnings. And test the functionality of the domain controller, including user authentication, group policy application, etc., to ensure that everything runs normally.

Best regards，

Jill Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.
