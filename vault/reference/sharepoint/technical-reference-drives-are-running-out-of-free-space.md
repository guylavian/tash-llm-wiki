---
title: "Drives are running out of free space (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-drives-are-running-out-of-free-space
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/drives-are-running-out-of-free-space
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Drives are running out of free space, for SharePoint Server."
---

# Drives are running out of free space (SharePoint Server) - SharePoint Server

Note

Drives are running out of free space (SharePoint Server)

# Drives are running out of free space (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Drives are running out of free space.

**Summary:** Disk drives on one or more of the servers in the SharePoint Server farm are running out of disk space.

Note

This rule checks disk space as a proportion of the RAM that is installed on the computer. When disk space is less than twice the RAM on the computer, the health rule triggers an error. When disk space is less than five times the RAM on the server, the health rule triggers a warning. Servers with large amounts of RAM are more likely to experience a failure of this rule.

**Resolution: Free disk space on the server**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

In Server Manager, click **Tools**, and then click **Disk Cleanup**.

**Resolution: Decrease the number of days to store log files**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Monitoring**, in the **Reporting** section, click **Configure diagnostic logging**.

On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
