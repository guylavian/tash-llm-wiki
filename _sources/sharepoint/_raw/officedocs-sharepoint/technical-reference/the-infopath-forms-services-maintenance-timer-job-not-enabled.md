---
title: "The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: The InfoPath Forms Services Maintenance timer job is not enabled, in SharePoint Server."
ms.topic: troubleshooting
---
Note

The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server)

# The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** The InfoPath Forms Services Maintenance timer job is not enabled.

**Summary:** The InfoPath Forms Services Maintenance timer job is not enabled.

The InfoPath Forms Services Maintenance timer job is used by InfoPath Forms Services to improve performance by caching form template data on each front-end web server.

**Cause:** The timer job may have been disabled on the Job Definitions page on the SharePoint Central Administration website or the Microsoft PowerShell **Disable-SPTimerJob** cmdlet was used.

Note

Infopath form service is removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft Power Apps as a potential alternative to Infopath form service.

**Resolution: Enable the timer job by using the Central Administration web site**

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

Start Central Administration.

On Central Administration, click **Monitoring**.

Click **Review Job definitions**.

Click **InfoPath Forms Services Maintenance**.

Click **Enable**.

**Resolution: Enable the timer job by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Enable-SPTimerJob "<FormsMaintenanceJobDefinition>"
```

Where:

- *<FormsMaintenanceJobDefintion>* is the actual name of the timer job to enable.

For more information, see Enable-SPTimerJob.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
