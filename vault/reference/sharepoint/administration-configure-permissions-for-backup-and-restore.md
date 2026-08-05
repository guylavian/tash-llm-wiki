---
title: "Configure backup and restore permissions in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-permissions-for-backup-and-restore
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-permissions-for-backup-and-restore
family: administration
documentKind: "how-to"
abstract: "Learn how to configure permissions for backup and restore operations in SharePoint Server."
---

# Configure backup and restore permissions in SharePoint Server - SharePoint Server

Note

Configure backup and restore permissions in SharePoint Server

# Configure backup and restore permissions in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can configure backup and restore permissions for SharePoint Server by using the SharePoint Central Administration website or Microsoft PowerShell. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requirements, and service level agreements that you have made with your organization.

Before you begin

## Before you begin

Before you back up or restore SharePoint Server, you must make sure that the timer service account, SQL Server service account, and users who run the backup or restore operations have the correct permissions or are members of the correct Windows security groups or SharePoint groups. You must configure these permissions and group memberships when you first deploy SharePoint Server. You have to update permissions and group memberships when you add new farm components to the environment and if you want to add users who will perform backup and restore operations.

Permissions for the SharePoint Timer service and SQL Server account in SharePoint Server

## Permissions for the SharePoint Timer service and SQL Server account in SharePoint Server

The SharePoint Timer Server and the SQL Server service account in SharePoint Server perform backup and restore operations on behalf of users. These service accounts require Full Control permissions on any backup folders.

Group memberships required to run backup and restore operations in Central Administration

## Group memberships required to run backup and restore operations in Central Administration

You must make sure all user accounts that use Central Administration to back up or restore your farm and farm components have the group memberships that are described in the following table.

| **Farm component** | **Member of Administrators group on the local computer** | **Member of Farm Administrators SharePoint group** |
| --- | --- | --- |
| Farm | Yes | No |
| Service Application | Yes | No |
| Content Database | Yes | No |
| Site Collection | No | Yes |
| Site, list, document library | No | Yes |

Setting permissions to run SharePoint backup and restore operations by using PowerShell

## Setting permissions to run SharePoint backup and restore operations by using PowerShell

You must make sure that all user accounts that use PowerShell to back up or restore your farm and farm components are added to the **SharePoint_Shell_Access** role for a specified database and have the permissions described in the table later in this section.

You can run the **Add-SPShellAdmin** cmdlet to add a user account to this role. You must run the command for each user account. Moreover, you must run the command for all databases to which you want to grant access.

Note

You only have to grant a user account access to back up and restore a specific farm component one time. You will have to perform this task again only when you add new farm components to your environment or when you want to add users to perform backup and restore operations.

Important

The **Add-SPShellAdmin** cmdlet grants the SPDataAccess role but this is not enough to complete the restore operation. This is because the **restore-spsite** cmdlet uses direct insert statements to add content rather than stored procedures which accommodate other interactions. The **Add-SPShellAdmin** cmdlet worked fine in SharePoint 2010 because as part of the SPDataAccess schema it added dbo permissions. For SharePoint Servers 2019, 2016 and 2013 the **db_owner** fixed database role permissions are required to complete restore operations from the SharePoint Management Shell.

**To add a user to or remove a user from the SharePoint_Shell_Access role by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Add-SPShellAdmin -Username <User account> -Database <Database ID>
```

Where:

- *<Database ID>* is the GUID assigned to the database.

To add a user account to all the databases in the farm, type the following command:

```
ForEach ($db in Get-SPDatabase) {Add-SPShellAdmin -Username <User account> -Database $db}
```

Where:

- *<User account>* is the user whose account you want to add.

To remove a user account from all the databases in the farm, type the following command:

```
ForEach ($db in Get-SPDatabase) {Remove-SPShellAdmin -Username <User account> -Database $db}
```

Where:

- *<User account>* is the user whose account you want to remove.

To view the user accounts currently added to the databases in the farm, type the following command:

```
ForEach ($db in Get-SPDatabase) {Get-SPShellAdmin -Database $db}
```

For more information, see Add-SPShellAdmin.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

You might also have to grant additional permissions to the users who run the backup or restore operation by using PowerShell. The following table shows the permissions that are required.

| **Farm component** | **Member of Administrators group on the local computer** | **Member of Farm Administrators SharePoint group** | **Full control on backup folder** |
| --- | --- | --- | --- |
| Farm | Yes | No | Yes |
| Service Application | Yes | No | Yes |
| Content Database | Yes | No | Yes |
| Site Collection | No | Yes | Yes |
| Site, list, document library | Yes | No | Yes |

See also

## See also

Concepts

#### Concepts

Plan for backup and recovery in SharePoint Server

Prepare to back up and restore farms in SharePoint Server

Overview of backup and recovery in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
