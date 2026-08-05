---
title: "Configure Windows Server Update Services (WSUS) Content Servers"
type: reference
domain: windows-server
slug: networking-configure-wsus-content-servers
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/networking/branchcache/deploy/configure-wsus-content-servers
family: networking
documentKind: "how-to"
abstract: "Learn how to configure Windows Server Update Services (WSUS) Content Servers to store update files on the local computer."
---

# Configure Windows Server Update Services (WSUS) Content Servers

# Configure Windows Server Update Services (WSUS) Content Servers

After installing the BranchCache feature and starting the BranchCache service, WSUS servers must be configured to store update files on the local computer.

When you configure WSUS servers to store update files on the local computer, both the update metadata and the update files are downloaded by and stored directly upon the WSUS server. This ensures that BranchCache client computers receive Microsoft product update files from the WSUS server rather than directly from the Microsoft Update Web site.

For more information about WSUS synchronization, see [Setting up Update Synchronizations](../../../administration/windows-server-update-services/manage/setting-up-update-synchronizations.md)
