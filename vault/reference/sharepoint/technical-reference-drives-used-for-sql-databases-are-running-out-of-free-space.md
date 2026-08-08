---
title: "Drives used for SQL databases are running out of free space (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-drives-used-for-sql-databases-are-running-out-of-free-space
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/drives-used-for-sql-databases-are-running-out-of-free-space
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Drives used for SQL databases are running out of free space, for SharePoint Server."
---

# Drives used for SQL databases are running out of free space (SharePoint Server) - SharePoint Server

Note

Drives used for SQL databases are running out of free space (SharePoint Server)

# Drives used for SQL databases are running out of free space (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Drives used for SQL databases are running out of free space.

**Summary:** The databases have one or more files that exceed the available free disk drive space. If this happens, operations will fail. A drive should have enough free space for the largest database file on it to autogrow twice. If the largest database file autogrows at 64MB increments, the drive needs 128MB of free space. If the largest database file is 512 GB and it autogrows in 1% increments, the drive needs 10.24 GB of free space.

**Cause:** The databases have large files that may exceed the available free space.

**Resolution: Free disk space on the database server computer.**

Verify that the user account that is performing the following step is a member of the Administrators group on the local database server computer.

In **Server Manager**, click **Tools**, and then click **Defragment and Optimize Drives**.

Run the Optimize Drives tool to free disk space on the server computer.

If the event persists, move some large files to another disk drive to free up space.

**Resolution: Decrease the number of days to store log files.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the Central Administration Home page, click **Monitoring**.

On the Monitoring page, in the **Reporting** section, click **Configure diagnostic logging**.

On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2024-04-12
