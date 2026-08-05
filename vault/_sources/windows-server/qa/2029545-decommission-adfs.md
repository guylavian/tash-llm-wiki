---
title: "Decommission ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2029545/decommission-adfs
question_id: 2029545
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Decommission ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2029545/decommission-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Please provide each steps for fully  decommission adfs  from production .

i am not able to find each step

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-03*

Hello

Thank you for posting in Q&A forum

below is decommissioning AD FS guide:

Consider taking an optional final backup before decommissioning AD FS servers.

Remove any AD FS entries from any of the load balancers (internal as well as external) you might have configured in your environment.

Delete any corresponding DNS entries of the respective farm names for AD FS servers in your environment.

On the primary AD FS server run Get-ADFSProperties and look for CertificateSharingContainer. Keep a note of this DN, as you'll need to delete it near the end of the installation (after a few reboots and when it isn't available anymore)

If your AD FS configuration database is using a SQL Server database instance as the store, ensure to delete the database before uninstalling AD FS servers.

Uninstall the WAP (Proxy) servers.

Sign in to each WAP server, open the Remote Access Management Console and look for published web applications.

Remove any related to AD FS servers that aren't being used anymore.

When all the published web applications are removed, uninstall WAP with the following command Uninstall-WindowsFeature Web-Application-Proxy,CMAK,RSAT-RemoteAccess.

Uninstall the AD FS servers.

Starting with the secondary nodes, uninstall AD FS with Uninstall-WindowsFeature ADFS-Federation,Windows-Internal-Database command. After this run del C:\Windows\WID\data\adfs* command to delete any database files

Delete AD FS Secure Socket Layer (SSL) certificates from each server storage.

Re-image AD FS servers with full disk formatting.

You can now safely delete your AD FS account.

Remove the content of the CertificateSharingContainer DN using ADSI Edit after uninstallation.

Active Directory Federation Services (AD FS) decommission guide | Microsoft Learn

Best regards

Yanhong

=====================================

If the answer is helpful, please click "Accept answer" and upvote it
