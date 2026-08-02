---
title: "Drives are at risk of running out of free space (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-drives-are-at-risk-of-running-out-of-free-space
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/drives-are-at-risk-of-running-out-of-free-space
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Drives are at risk of running out of free space, for SharePoint Server."
---

# Drives are at risk of running out of free space (SharePoint Server) - SharePoint Server

Note

Drives are at risk of running out of free space (SharePoint Server)

# Drives are at risk of running out of free space (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Drives are at risk of running out of free space.

**Summary:** This rule checks disk space as a proportion of the RAM that is installed on the SharePoint Server. Servers with large amounts of RAM are more likely to experience a failure of this rule.

**Cause:** When disk space is less than five times the RAM on the server, this health rule triggers a warning. For example, if your SharePoint Server has 16GB of RAM installed, the rule checks for 80GB of free space on the disk.

**Resolution: Free disk space on the server**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On Server Manager, click **Tools**, and then click **Disk Cleanup**.

**Resolution: Decrease the number of days to store log files**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Monitoring**, in the **Reporting** section, click **Configure diagnostic logging**.

On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
