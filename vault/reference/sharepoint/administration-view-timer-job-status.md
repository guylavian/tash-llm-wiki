---
title: "View timer job status in SharePoint Server 2016 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-view-timer-job-status
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/view-timer-job-status
family: administration
documentKind: "how-to"
abstract: "Learn to view SharePoint timer job status by using the SharePoint Central Administration website or Windows PowerShell."
---

# View timer job status in SharePoint Server 2016 - SharePoint Server

Note

View timer job status in SharePoint Server 2016

# View timer job status in SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

A timer job runs a specific Windows service for SharePoint Server 2016. The timer job contains a definition of the service to run and specifies how frequently the service is started. The SharePoint Timer Service runs timer jobs. Many features in SharePoint Server 2016 rely on timer jobs to run services according to a schedule. You can view the status of timer jobs that have been run by using the Central Administration website or PowerShell.

Note

Because SharePoint Server 2016 runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server 2016 supports the accessibility features of supported browsers. For more information, see the following resources: > Plan browser support> Accessibility guidelines in SharePoint> Accessibility in SharePoint> Keyboard shortcuts> Touch.

View timer job status by using Central Administration

## View timer job status by using Central Administration

You can view timer job status by using Central Administration.

**To view timer job status by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

In Central Administration, on the home page, click **Monitoring**.

On the **Monitoring** page, in the **Timer Jobs** section, click **Check job status**.

Timer job status is divided into three groups: **Scheduled**, **Running**, and **History**. To page through the timer job status data rows, click the paging arrows at the bottom of these groups.

To view the timer job status for a specific group, click the title of the group. Or, in the Quick Launch, click **Scheduled Jobs**, **Running Jobs**, or **Job History**.

View timer job status by using Windows PowerShell

## View timer job status by using Windows PowerShell

You can view timer job status by using PowerShell.

**To view timer job status by using Windows PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

- Start the SharePoint 2016 Management Shell.

- On the Start screen, click SharePoint 2016 Management Shell.

- At the PowerShell command prompt, type the following command:

```
Get-SPTimerJob -Identity <SPTimerJobPipeBind> | Format-Table DisplayName,Id,LastRunTime,Status
```

Where  *<SPTimerJobPipeBind>* can be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a timer job (for example, TimerJob1); or an instance of a valid SPTimerJob object.

You can use the value of the **Identity** parameter to specify a timer job. If you do not use the **Identity** parameter, all timer jobs are returned.

To view the history of a specific timer job, type the following command:

```
(Get-SPTimerJob -Identity <SPTimerJobPipeBind>).HistoryEntries | Format-Table -Property Status,StartTime,EndTime,ErrorMessage
```

Where  *<SPTimerJobPipeBind>* can be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a timer job (for example, TimerJob1); or an instance of a valid SPTimerJob object.

For more information, see Get-SPTimerJob.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Note

Please be aware that Get-SPTimerJob commandlet will show you logs in GMT time zone whereas SharePoint Central Administration will show all events in local time.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
