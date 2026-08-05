---
title: "The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: The State Service Delete Expired Sessions timer job is not enabled, for SharePoint Server."
ms.topic: troubleshooting
---
Note

The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server)

# The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The State Service Delete Expired Sessions timer job is not enabled.

**Summary:** The State Service uses a timer job to delete data for expired sessions from the State Service databases. If this timer job is not enabled, the server that hosts the State Service database will run out of disk space and the SharePoint farm will cease to function

**Cause:** The State Service Delete Expired Sessions timer job is not enabled.

**Resolution: Enable the timer job by using the SharePoint Central Administration website**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

Note

The timer job settings are farm-wide and cannot be set for individual servers in the farm.

Start Central Administration.

In Central Administration, click **Monitoring**.

On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.

On the Job Definitions page, click the State Service Delete Expired Sessions timer job.

On the Edit Timer Job page, specify the schedule that you want, and then click **Enable**.

**Resolution: Enable the timer job by using Microsoft PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Enable-SPTimerJob StateServiceExpiredSessionJobDefinition
```

For more information, see Enable-SPTimerJob. We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
