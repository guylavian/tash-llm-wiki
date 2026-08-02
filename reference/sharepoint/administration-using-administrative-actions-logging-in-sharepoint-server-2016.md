---
title: "Using Administrative Actions logging in SharePoint Server 2016 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-using-administrative-actions-logging-in-sharepoint-server-2016
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/using-administrative-actions-logging-in-sharepoint-server-2016
family: administration
documentKind: "article"
abstract: "The Administrative Actions logging feature is included in the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1). This feature enables logging of SharePoint Server 2016 administrative actions."
---

# Using Administrative Actions logging in SharePoint Server 2016 - SharePoint Server

Note

Using Administrative Actions logging in SharePoint Server 2016

# Using Administrative Actions logging in SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The Administrative Actions logging feature is included in the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1). This feature enables logging of SharePoint Server 2016 administrative actions.

Overview

## Overview

Administrative changes to SharePoint Server settings can sometimes cause errors or have unintended effects. To aid in troubleshooting administrative changes, logging around key SharePoint administrative actions is available in Feature Pack 1. Logging is available for both Central Administration and Windows PowerShell actions.

Turning on Administrative Actions logging

## Turning on Administrative Actions logging

Administrative Actions logging is turned on by default when you install SharePoint Server 2016 November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1).

After you install Feature Pack 1, Administrative Actions will show up as a checked option under "Events to log" in the **Configure usage and health data collection** page of SharePoint 2016 Central Administration.

How to find the Administrative actions local log file location

## How to find the Administrative actions local log file location

Administrative actions log files are stored on your server. To view the local location of these logs:

On the SharePoint 2016 Central Administration home page, click **Monitoring**.

In the Reporting section, click **Configure usage and health data collection**.

You will see the log file location listed under **Usage Data Collection Settings**.

How to find the Administrative actions Usage Database log files

## How to find the Administrative actions Usage Database log files

Administrative actions logs are written to the SharePoint Usage Database. To find your logging database server:

On the SharePoint 2016 Central Administration home page, click ** Monitoring **.

In the Reporting section, click **Configure usage and health data collection**.

You will find the logging database server and database name under: **Logging Database Server settings**.

Retrieving logs from the SharePoint Usage Database

## Retrieving logs from the SharePoint Usage Database

Administrative actions logs are kept in the SharePoint Usage Database for a maximum of 31 days.

Open Microsoft SQL Server Management Studio. ** Note: ** You must be logged in as Administrator.

Connect to the Server name indicated as the "Database Server," in the Logging **Database Server settings** above.

Connect to your applicable logging database. This is the database you have specified as the "Database Name" in the **Logging Database Server settings**, typically WSS_Logging.

Query the "AdministrativeActions" partitions.

Note

Select the number of applicable "AdministrativeActions" partitions. There should be 32 partitions created, partitions 0 through 31. WSS_logging is the default logging **Database Name**. Modify the query if your logging **Database Name** is different.

**Sample Query**

```
SELECT TOP 1000 [PartitionId]
      ,[RowId]
      ,[LogTime]
      ,[MachineName]
      ,[FarmId]
      ,[SiteSubscriptionId]
      ,[UserLogin]
      ,[CorrelationId]
      ,[Action]
      ,[Target]
      ,[Details]
      ,[RowCreatedTime]
  FROM (
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition0]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition1]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition2]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition3]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition4]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition5]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition6]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition7]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition8]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition9]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition10]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition11]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition12]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition13]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition14]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition15]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition16]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition17]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition18]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition19]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition20]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition21]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition22]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition23]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition24]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition25]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition26]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition27]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition28]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition29]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition30]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition31]
) as A
```

Using Windows PowerShell to retrieve logs

## Using Windows PowerShell to retrieve logs

You can also retrieve Administrative Actions logs using the Windows PowerShell cmdlet, ** Merge-SPUsageLog **.

Important

Remote cmdlet execution must be enabled to use **Merge-SPUsageLog**. To configure the computer to receive remote commands, see Enable-PSRemoting.

The **Merge-SPUsageLog** cmdlet gathers, filters, and aggregates logs based on the your specified criteria. We recommend that you filter by using the StartTime and EndTime parameters to optimize performance of this cmdlet.

**Merge-SPUsageLog** generates objects into PowerShell pipeline from logs that meet the criteria. You should at least specify a usage type, for example "Administrative Actions".

```
Merge-SPUsageLog -Identity <SPUsageDefinitionPipeBind> [-AssignmentCollection <SPAssignmentCollection>] [-DiagnosticLogPath <String>] [-EndTime <DateTime>] [-OverWrite <SwitchParameter>] [-Servers <String[]>] [-StartTime <DateTime>] 
 
```

| **Parameter** | **Required** | **Type** | **Description** |
| --- | --- | --- | --- |
| Identity | Required | Microsoft.SharePoint.PowerShell.SPUsageDefinitionPipeBind | Specifies the name of usage log file. |
| AssignmentCollection | Optional | Microsoft.SharePoint.PowerShell.SPAssignmentCollection | Manages objects for the purpose of proper disposal. Use of objects, such as SPWeb or SPSite, can use large amounts of memory and use of these objects in Windows PowerShell scripts requires proper memory management. Using the SPAssignment object, you can assign objects to a variable and dispose of the objects after they are needed to free up memory. When SPWeb, SPSite, or SPSiteAdministration objects are used, the objects are automatically disposed of if an assignment collection or the Global parameter is not used.  
 > [!NOTE]> When the Global parameter is used, all objects are contained in the global store. If objects are not immediately used, or disposed of by using the Stop-SPAssignment command, an out-of-memory scenario can occur. |
| DiagnosticLogPath | Optional | System.String | Specifies the file to write diagnostic information to. A relative path is supported. |
| EndTime | Optional | System.DateTime | Specifies the end time of the log entries returned. The type must be a valid DateTime format that is culture-specific to the administrative language, that is, 2/16/2007 12:15:12 for English-US. The default value is the current time.  
 If you want to specify UTC time, you must add a "Z" to the end of the parameter. For example, "2016-06-15 03:29:18.199 Z". If the "Z" is not specify, local computer time will be displayed instead of UTC. |
| OverWrite | Optional | System.Management.Automation.SwitchParameter | Overwrites the diagnostic log file if it already exists at the specified path. |
| Servers | Optional | System.String[] | The server address or addresses to filter on. To obtain a list of valid addresses in the farm use Get-SPServer 
 Select Address. |
| StartTime | Optional | System.DateTime | Specifies the start time of the log entries returned. The type must be a valid DateTime format that is culture-specific to the administrative language, such as "2/16/2007 12:15:12" for English-US. The default value is one hour prior to the current time on the local computer.  
 If you want to specify UTC time, you must add a "Z" to the end of the parameter. For example, "2016-06-15 03:29:18.199 Z". If the "Z" is not specify, local computer time will be displayed instead of UTC. |

**Example 1:** This example merges the last hour of log data for "Administrative Actions" usage provider from all farm computers.

```
Merge-SPUsageLog -Identity "Administrative Actions" 
```

**Example 2:** This example merges the log entries for the "Administrative Actions" usage provider from "06/09/2016 16:00" until now from servers named "A-0606" and "A-0505".

```
Merge-SPUsageLog -Identity "Administrative Actions" -Servers "A-0606","A-0505" -StartTime "06/09/2008 16:00" 
```

**Example 3:** This example retrieves Administrative Actions logs starting from Aug 11th, and then selects the following fields to display: User, ActionName, and TimeStamp. The results are sorted by TimeStamp. This example uses the Windows PowerShell pipeline. For more information about how to use the pipeline, see about_Pipelines

```
Get-SPUsageDefinition -Identity "Administrative Actions" | Merge-SPUsagelog  -StartTime "08/11/2016 3:50 AM" | Select User, ActionName, Timestamp | Sort Timestamp  
 
```

Types of administrative actions logged

## Types of administrative actions logged

The following tables details the types of Administrative Actions that are captured in the logs.

| **Action category** | **Action sub-category** | **Log actions(s)** | **Description** |
| --- | --- | --- | --- |
| Configure Accounts | Add, Remove, Update | Administration.Security.User.Add          Administration.Security.User.Remove          Administration.Security.User.Update          Administration.Security.User.Role.Update | Logs administrative account configuration and information changes including the addition, removal, and updates of farm and site collections administrators. Also, logs role updates. |
| Configure managed accounts | New, Remove, Update | Administration.Security.ManagedAccount.New Administration.Security.ManagedAccount.Remove Administration.Security.ManagedAccount.Update | Logs changes in the configuration of managed accounts, creation and removal of managed accounts, and updates to existing managed accounts. |
| Configure Service Account | Update | Administration.Security.ServiceAccount.Update | Logs updates to the designated service accounts in the farm. |
| Configure Password change settings | Update | Administration.Security.AccountPasswordSetting.Update | Logs updates to password management settings. |
| Specify Authentication Providers | Update | Administration.Security.AuthenticationProviderSetting.Update | Logs updates to authentication provider settings. |
| Manage Trust | Edit, Remove, Update | Administration.Security.ManageTrust.SPTrustedRootAuthority.Edit Administration.Security.ManageTrust.SPTrustedRootAuthority.New Administration.Security.ManageTrust.SPTrustedRootAuthority.Remove Administration.Security.ManageTrust.SPTrustedSecurityTokenIssuer.Edit Administration.Security.ManageTrust.SPTrustedSecurityTokenIssuer.New Administration.Security.ManageTrust.SPTrustedSecurityTokenIssuer.Remove | Administration.Security.ManageTrust.SPTrustedRootAuthority logs edits to, and removals of the trust relationship settings in the farm, and the creation of new trust relationships. Administration.Security.ManageTrust.SPTrustedSecurityTokenIssuer logs edits to, and removals of the token issuer settings, and the creation of new token issuer trust relationships. |
| Manage Web Part Security | Update | Administration.Security.WebPart.Update | Logs updates to Web Part pages and Web parts on your selected web application. |
| Farm backup and restore operations | Backup, Restore, Update | Administration.Farm.BackupRestore.Backup Administration.Farm.BackupRestore.Restore Administration.Farm.BackupRestore.Settings.Update | Logs farm restore and backup operations, including updates to your default backup and restore settings. |
| Server Administration | Add, Remove, Update | Administration.Farm.Server.Add Administration.Farm.Server.Remove Administration.Farm.Server.Role.Update | Logs removals and additions of servers to the farm, including role updates of farm servers. |
| Configuration database changes | New, Remove | Administration.Farm.ConfigurationDatabase.New Administration.Farm.ConfigurationDatabase.Remove | Logs the addition of the new configuration database or the removal of an existing one. |
| Site Collection Administration | Add, Backup, Export, Import, Remove, Restore, Update | Administration.SiteCollection.Add Administration.SiteCollection.Remove Administration.SiteCollection.BackupRestore.Backup Administration.SiteCollection.BackupRestore.Restore Administration.SiteCollection.Owner.Update Administration.SiteCollection.SecondContact.Update Administration.SiteCollection.Quota.Update Administration.SiteCollection.ImportExport.Export Administration.SiteCollection.ImportExport.Import | Logs the most common operations around site collection administration, including the addition and removal of a site collection, backup and restore operations of a site collection, changes to ownership, secondary contact, and quota, and import and export operations of the site collection. |
| Site Collection Content Database | Add, New, Remove, Set | Administration.ContentDatabase.Add Administration.ContentDatabase.New Administration.ContentDatabase.Remove Administration.ContentDatabase.Set | Logs common SharePoint content database operations such as: adding a content database to the farm, creating a new content database, removing a content database, and setting the global properties of a content database. |
| Quota Changes | New, Remove, Update | Administration.Quota.New Administration.Quota.Remove Administration.Quota.Update | Logs setting a site new collection quota, making updates to an existing site collection quota, and removing a site collection quota. |
| Feature Administration | Install, Disable, Uninstall, Enable | Administration.Feature.Disable Administration.Feature.Enable Administration.Feature.Install Administration.Feature.Uninstall | Logs site collection feature administration actions to disable, enable, install, and uninstall features. |
| Web Application Administration | Edit, New, Remove | Administration.WebApplication.Edit Administration.WebApplication.New Administration.WebApplication.Remove | Logs common web application administrations actions including edits to an existing web application, the creation of a new web application, and the removal of an existing web application. |
| Web Application Administration User Policy | Add, New, Remove, Update | Administration.WebApplication.UserPolicy.Add Administration.WebApplication.UserPolicy.New Administration.WebApplication.UserPolicy.Remove Administration.WebApplication.UserPolicy.Update | Logs operations related to the management of user permission policies of web applications including: adding users to an existing web application user policy, creating a new user policy, removing users from an existing user policy, and making updates to a user permission policy. |
| Service Application | Edit, New, Remove | Administration.ServiceApplication.Edit Administration.ServiceApplication.New Administration.ServiceApplication.Remove | Logs edits to Service Applications, the creation of a new Service Application, and the removal of an existing Service Application. |
| Form & Feature Template Administration | Convert, Disable, Enable, Install, New, Set, Start, Stop, Test, Update, Upgrade, Uninstall | Administration.FormTemplate.Convert Administration.FormTemplate.Disable Administration.FormTemplate.Enable Administration.FormTemplate.Install Administration.FormTemplate.New Administration.FormTemplate.Set Administration.FormTemplate.Start Administration.FormTemplate.Stop Administration.FormTemplate.Update Administration.FormTemplate.Test Administration.FormTemplate.Upgrade Administration.FormTemplate.Uninstall Administration.Feature.FormTemplate.Install Administration.Feature.FormTemplate.Uninstall | Logs operations related to the management of InfoPath templates in site collections, including: template conversion, disablement (deactivation), enablement, installation, creation of a new template, setting a template, starting and stopping of templates, updates, testing, upgrade, and uninstalling of a template. |
| Content Database | Add, New, Remove, Set | Administration.ContentDatabase.Add Administration.ContentDatabase.New Administration.ContentDatabase.Remove Administration.ContentDatabase.Set |  |
| Configure Groups | Add, Remove, Update | Administration.Security.Group.Add Administration.Security.Group.Remove Administration.Security.Group.Update | Logs actions related to group creation, deletion, and management, such as: adding, removing, and updating groups. |
| User & Group Migration | Move | Administration.Security.User.Move Administration.Security.Group.Move | Logs activities relating the migration of group and user logins. |

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
