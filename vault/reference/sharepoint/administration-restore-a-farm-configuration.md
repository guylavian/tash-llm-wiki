---
title: "Restore farm configurations in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-restore-a-farm-configuration
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/restore-a-farm-configuration
family: administration
documentKind: "how-to"
abstract: "Learn how to restore configuration information (such as antivirus, IRM, outbound email, and some customizations) for SharePoint Server."
---

# Restore farm configurations in SharePoint Server - SharePoint Server

Note

Restore farm configurations in SharePoint Server

# Restore farm configurations in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can restore a farm configuration in SharePoint Server by using the SharePoint Central Administration website or Microsoft PowerShell. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization.

Before you begin

## Before you begin

Farm-level configuration recovery is performed only after a failure that involves the configuration database but does not involve other farm data, such as a content database or Web application. If restoring the farm configuration does not solve the problems, you must restore the complete farm. For more information about how to restore the complete farm, see Restore farms in SharePoint Server. You can restore the configuration from a farm backup that used either the **Backup content and configuration settings** option or the **Backup only configuration settings** option.

Note

In earlier versions of SharePoint, you could not restore the configuration database and, therefore, you could not restore the configuration of a farm. Now you do not have to restore the configuration database because you can restore the farm configuration directly.

Using PowerShell to restore a farm's configuration in SharePoint

## Using PowerShell to restore a farm's configuration in SharePoint

You can use PowerShell to restore a farm's configuration.

**To restore a farm's configuration by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Restore-SPFarm -Directory <RestoreShare> -RestoreMethod Overwrite -ConfigurationOnly
```

Where *<RestoreShare>* is network location where the backup file is stored. For more information, see Restore-SPFarm.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

Using Central Administration to restore a farm's configuration in SharePoint

## Using Central Administration to restore a farm's configuration in SharePoint

You can use Central Administration to restore a farm's configuration.

**To restore a farm's configuration by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group on the computer that is running Central Administration.

**Verification:** Optionally, include steps that users should perform to verify that the operation was successful.

You must also be a member of the **sysadmin** fixed server role on the database server where each database is stored.

In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.

On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, select the backup job that contains the farm backup from the list of backups, and then click **Next**.

Note

You can view additional information about the backups by expanding the row that contains the backup.

Note

If the correct backup job does not appear, in the **Backup Directory Location** text box, enter the UNC path of the correct backup folder, and then click **Refresh**.

On the Restore from Backup — Step 2 of 3: Select Component to Restore page, select the check box that is next to the farm, and then click **Next**.

On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that "Farm" appears in the **Restore the following content** list.

In the **Restore Only Configuration Settings** section, make sure that the **Restore content and configuration settings** option is selected.

In the **Restore Options** section, select the **Type of Restore** option. Use the **Same configuration** setting. A dialog will appear that asks you to confirm the operation. Click **OK**.

Note

If the **Restore Only Configuration Settings** section does not appear, then the backup that you selected is a configuration-only backup.

Click **Start Restore**.

You can view the general status of all recovery jobs at the top of the Backup and Restore Status page in the **Readiness** section. You can view the status of the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the recovery to start.

If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 2.

See also

## See also

Concepts

#### Concepts

Back up farm configurations in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
