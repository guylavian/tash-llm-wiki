---
title: "Migrate ADFS from Windows 2012 R2 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2141553/migrate-adfs-from-windows-2012-r2-to-2019
question_id: 2141553
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrate ADFS from Windows 2012 R2 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2141553/migrate-adfs-from-windows-2012-r2-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Windows 2012 R2 server with ADFS installed on it. However, I am unsure about the farm config as the cmdlet "Get-AdfsFarmInformation" does not work, and instead spits out an error about the cmdlet not being recognised. I am unsure whether this was installed as a standalone ADFS server.

The Microsoft guide for upgrade ADFS here https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server depends on adding a second server to the ADFS farm, but I'm unsure if the current ADFS on 2012 R2 was ever set up as a farm or a standalone server, how can I check? If it is standalone, how do I go about migration?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-09*

Hello,

Thank you for posting in Q&A forum.

How to verify if ADFS server is standalone

1.Open ADFS Management Console and go to "Overview" page, if there's "Join Farm" option, it means the server is standalone.

If it's standalone, please follow below steps to migrate to Windows Server 2019:

1.Install WinServer 2019 and ADFS role on the new machine.

2.Export the ADFS configuration and certificates from existing server.

3.Import the configuration and certificates to new server.

REF: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/create-a-stand-alone-federation-server

REF: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/upgrading-to-ad-fs-in-windows-server

To help other customers who may be facing the same issue, please don't forget to vote if the reply is helpful.

Best Regards

Zunhui
