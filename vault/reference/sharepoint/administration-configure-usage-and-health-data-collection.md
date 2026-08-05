---
title: "Configure usage and health data collection in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-usage-and-health-data-collection
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-usage-and-health-data-collection
family: administration
documentKind: "how-to"
abstract: "Learn how to configure usage and health data collection in SharePoint Server."
---

# Configure usage and health data collection in SharePoint Server - SharePoint Server

Note

Configure usage and health data collection in SharePoint Server

# Configure usage and health data collection in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server writes usage and health data to the logging folder and to the logging database. You can use the SharePoint Central Administration website to configure health data collection settings.

Before you begin

## Before you begin

Note

Administrators typically use the SharePoint Central Administration website and the SharePoint Management Shell to manage deployments. For information about accessibility for administrators, see Accessibility for SharePoint 2013. >  Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: > Plan browser support in SharePoint Server 2016> Accessibility features in SharePoint> Keyboard shortcuts> Touch

Configure usage and health data collection by using Central Administration

## Configure usage and health data collection by using Central Administration

The usage and health data settings are farm-wide and cannot be set for individual servers in the farm.

**To configure usage and health data collection by using Central Administration:**

Verify that user account performing this procedure is a member of the Farm Administrators group.

In Central Administration, on the home page, click **Monitoring**.

On the Monitoring page, in the **Reporting** section, click **Configure usage and health data collection**.

On the Configure usage and health data collection page, in the **Usage Data Collection** section, select the **Enable usage data collection** check box.

In the **Event Selection** section, select the check boxes of the events that you want to log.

Logging uses system resources and can affect performance and disk usage. Only log those events for which you want regular reports.

For impromptu reports or investigations, enable logging for events, and then disable logging for the events after the report or investigation is complete. For more information, see Configure usage data collection for events by using Windows PowerShell.

In the **Usage Data Collection Settings** section, type the path of the folder to which you want usage and health information to be written in the **Log file location** box. The path that you specify must exist on each server in the farm.

These settings are applied to all events.

In the **Health Data Collection** section, select the **Enable health data collection** check box. To change the collection schedules, click **Health Logging Schedule**. You can see a list of timer jobs that collect health data. Click any of the timer jobs to change its schedule, or disable that timer job. If you disable a timer job, it stops collecting corresponding health data. For more information, see Default timer jobs in SharePoint Server 2016.

To change log collection schedules, click **Log Collection Schedule**, and then click any of the timer jobs to change its schedule, or disable that timer job. If you disable a timer job, it stops collecting corresponding log data.

In the **Logging Database Server** section, to change the authentication method, select either the **Windows authentication** or **SQL authentication** option.

To change the **Database Server** and **Database Name** values, you must use PowerShell. For more information, see Log usage data in a different logging database by using Windows PowerShell.

Configure usage data collection by using Windows PowerShell

## Configure usage data collection by using Windows PowerShell

**To configure usage data collection by using Windows PowerShell:**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

On the **Start** menu, click **All Programs**.

Click **SharePoint 2016**.

Click **SharePoint 2016 Management Shell**.

At the PowerShell command prompt, type the following command:

```
Set-SPUsageService [-LoggingEnabled {1 | 0}] [-UsageLogLocation <Path>] [-Verbose]
```

Where  *<Path>* is a path that exists on each computer in the farm.

To view the progress of the command, use the **Verbose** parameter.

Enable usage data logging by typing.

```
Set-SPUsageService -LoggingEnabled 1
```

For more information, see Set-SPUsageService.

Configure usage data collection for events by using Windows PowerShell

## Configure usage data collection for events by using Windows PowerShell

The event types that are listed on the Configure usage and health data collection page in Central Administration are the same as Usage Definitions in PowerShell. You can use only PowerShell to configure usage definitions individually. Moreover, you can configure only the **DaysRetained** parameter.

**To configure usage data logging for events by using Windows PowerShell:**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

On the **Start** menu, click **All Programs**.

Click **SharePoint 2016**.

Click **SharePoint 2016 Management Shell**.

At the PowerShell command prompt, type the following command:

```
Set-SPUsageDefinition -Identity <SPUsageDefinitionPipeBind> [-Enable] [-DaysRetained <0-31>] [-Verbose]
```

Where  *<SPUsageDefinitionPipeBind>* specifies the usage definition object that you want to update. The type must be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a usage definition (for example, SiteSubscriptionConfig1); or an instance of a valid **SPUsageDefinition** object. You can use the PowerShell **Get-SPUsageDefinition** cmdlet to obtain this GUID. For more information, see Get-SPUsageDefinition.

Use the **Enable** parameter to enable usage logging for this usage definition. Use the **DaysRetained** parameter to specify how long the usage data is retained in the log before it is deleted. The range is 0 to 31 days. To view the progress of the command, use the **Verbose** parameter.

For more information, see Set-SPUsageDefinition.

Log usage data in a different logging database by using Windows PowerShell

## Log usage data in a different logging database by using Windows PowerShell

You can use PowerShell to change this setting.

**To log usage data in a different logging database by using Windows PowerShell:**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

On the **Start** menu, click **All Programs**.

Click **SharePoint 2016**.

Click **SharePoint 2016 Management Shell**.

At the PowerShell command prompt type the following command:

```
Set-SPUsageApplication -DatabaseServer <DatabaseServerName> -DatabaseName <DatabaseName> [-DatabaseUserName <UserName>] [-DatabasePassword <Password>] [-Verbose]
```

Where:

*<DatabaseServerName>* is the name of host server for the logging database. You must specify a value for the **DatabaseServer** parameter, even if the new database is located on the same database server as the old one.

*<DatabaseName>* is the name of the logging database.

*<UserName>* is the user name to use for connecting to the logging database. Use this parameter only if SQL Server Authentication is used to access the logging database.

*<Password>* is the password for the user specified in **DatabaseUserName**. You must specify both  *<UserName>* and  *<Password>* if the database owner is a different user account than the one with which you logged on.

To view the progress of the command, use the **Verbose** parameter.

For more information, see Set-SPUsageApplication.

See also

## See also

Concepts

#### Concepts

Overview of monitoring in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
