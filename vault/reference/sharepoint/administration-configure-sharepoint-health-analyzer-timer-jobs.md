---
title: "Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-sharepoint-health-analyzer-timer-jobs
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-sharepoint-health-analyzer-timer-jobs
family: administration
documentKind: "how-to"
abstract: "Learn to configure health data collection timer jobs by using the SharePoint Central Administration website or Windows PowerShell."
---

# Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016 - SharePoint Server

Note

Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016

# Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Health Analyzer uses timer jobs to collect health data and then writes the data to the logging folder and to the Logging database. This data is used in reports to display health of the farm servers. You can reschedule these timer jobs, run them immediately, or enable or disable them.

On that page, you can also configure usage data collection, event selection, and usage data collection settings. For more information, see Configure usage and health data collection in SharePoint Server.

Use Central Administration to configure health data collection timer jobs

## Use Central Administration to configure health data collection timer jobs

You can use Central Administration to configure health data collection timer jobs.

**To configure health data collection timer jobs by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

Note

The health data collection timer job settings are farm-wide and cannot be set for individual servers in the farm.

In Central Administration, on the home page, select **Monitoring**.

On the **Monitoring** page, in the **Reporting** section, select **Configure usage and health data collection**.

On the **Configure usage and health data collection** page, in the **Health Data Collection** section, select **Enable health data collection**.

In the **Health Data Collection** section, select **Health Logging Schedule**. The **Job Definitions** page opens. It lists all the timer jobs that collect health data.

On the **Job Definitions** page, select the timer job that you want to configure.

On the **Edit Timer Job** page, in the **Recurring Schedule** section, change the timer job schedule, and then select **OK**.

Use Windows PowerShell to configure health data collection timer jobs

## Use Windows PowerShell to configure health data collection timer jobs

You can configure the health data collection timer job schedule by using PowerShell.

**To configure health data timer jobs by using Windows PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

On the **Start** menu, select **All Programs**.

Select **SharePoint 2016**.

Select **SharePoint 2016 Management Shell**.

At the PowerShell command prompt, type the following command:

```
Set-SPTimerJob -Identity <SPTimerJobPipeBind> -Schedule <ScheduleString>
```

The value of the **Identity** parameter specifies the timer job. If you do not use the **Identity** parameter, all timer jobs are configured. To see a list of all the timer jobs, type the following command:

```
Get-SPTimerJob | Format-Table -property id,title
```

*<SPTimerJobPipeBind>* can be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a timer job (for example, TimerJob1); or an instance of a valid **SPTimerJob** object.

Use the value of the **Schedule** parameter to specify the schedule, where  *<ScheduleString>* is one of the following:

**Every 5 minutes between 0 and 59**

**Hourly between 0 and 59**

**Daily at 15:00:00**

**Weekly between Fri 22:00:00 and Sun 06:00:00**

**Monthly at 15 15:00:00**

**Yearly at Jan 1 15:00:00**

To see examples of timer job schedules, type the following command:

```
Get-SPTimerJob | Format-Table -property id,title,schedule
```

For more info, see Get-SPTimerJob and Set-SPTimerJob.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Concepts

#### Concepts

Overview of monitoring in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
