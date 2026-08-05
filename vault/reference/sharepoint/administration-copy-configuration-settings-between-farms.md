---
title: "Copy configuration settings between farms in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-copy-configuration-settings-between-farms
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/copy-configuration-settings-between-farms
family: administration
documentKind: "how-to"
abstract: "Learn how to copy configuration settings from one SharePoint Server farm to another."
---

# Copy configuration settings between farms in SharePoint Server - SharePoint Server

Note

Copy configuration settings between farms in SharePoint Server

# Copy configuration settings between farms in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can copy configuration settings between SharePoint Server farms by using Microsoft PowerShell.

Before you begin

## Before you begin

There are many ways in which you can copy configurations from one farm to another. Determine which method to use based on the configuration settings that you want to copy and how often you have to copy them.

Back up and restore a farm without the content databases attached. This method gives you farm settings and Web application settings, in addition to the settings for any service applications that you select.

Back up and restore configurations only. This method provides you with the core SharePoint Foundation settings only.

Note

This method does not include Web application or service application settings. If Web application settings are required in the restored farm, use one of the other methods.

Create a deployment script, based on your documented configuration. This method may be more work at first, but is easy to use to maintain standardization.

Backup and restore a farm without content databases to copy configuration settings in SharePoint Server

## Backup and restore a farm without content databases to copy configuration settings in SharePoint Server

To copy configuration settings by using a farm backup, we recommend that you first detach the content databases from the farm. This is not a step that we recommend that you take with a live production farm.

Note

Creating a farm backup without content databases does back up the service applications.

**To back up and restore a farm without content databases by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command to document the current Web application URLs and content database mappings.

```
Get-SPWebApplication | %{$_.Name;$_.Url;%{$_.ContentDatabases|%{$_.Name};Write-Host ""}}
```

Either unmount all content databases, as in the following example:

```
Get-SPContentDatabase | Dismount-SPContentDatabase
```

Or unmount a specific content database, as in the following example:

```
Get-SPContentDatabase WSS_Content | Dismount-SPContentDatabase
```

Back up the farm.

```
Backup-SPFarm -Directory \\servername\share -BackupMethod Full
```

Note

You can view the progress of the backup by looking at the  *\servername\share\spbr####*\spbackup.log file.

After the backup is complete, re-mount the content databases.

```
Mount-SPContentDatabase -Name <WSS_Content> -WebApplication <http://servername>
```

Replace the placeholders with each of the mappings documented in step 1.

Where:

*<WSS_Content>* is the <name and ID of the database>.

*<http://servername>* is <the URL of the Web Application>.

For more information, see Mount-SPContentDatabase.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Back up and recover configuration settings only

## Back up and recover configuration settings only

As part of farm backup, you can choose to back up only configuration settings. A configuration-only backup extracts and backs up many, but not all, configuration settings from a configuration database. By using built-in tools, you can back up the configuration of any configuration database, whether it is currently attached to a farm or not. For detailed information about how to back up a configuration, see Back up farm configurations in SharePoint Server.A configuration backup can be restored to the same — or any other — server farm. When a configuration is restored, it will overwrite any settings present in the farm that have values that are set within the configuration backup. If any settings present in the farm are not contained in the configuration backup, they will not be overwritten. For detailed information about how to restore a farm configuration, see Restore farm configurations in SharePoint Server.

See also

## See also

Concepts

#### Concepts

Overview of backup and recovery in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
