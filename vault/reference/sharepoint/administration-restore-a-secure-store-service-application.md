---
title: "Restore Secure Store Service applications in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-restore-a-secure-store-service-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/restore-a-secure-store-service-application
family: administration
documentKind: "how-to"
abstract: "Learn how to restore the Secure Store Service application in SharePoint Server."
---

# Restore Secure Store Service applications in SharePoint Server - SharePoint Server

Note

Restore Secure Store Service applications in SharePoint Server

# Restore Secure Store Service applications in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can restore the Secure Store service application by using the SharePoint Central Administration website or PowerShell. The restore tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization.

Before you begin

## Before you begin

The Secure Store Service provides the capability of securely storing credential sets and associating credentials to specific identities or a group of identities.

Before you begin this operation, review the following information about the Secure Store service application:

Every time that you enter a new passphrase, SharePoint Server creates a new Master Key and re-encrypts the credentials sets with that key. The passphrase gives you access to the Master Key created by SharePoint Server that is used to encrypt the credential sets.

You will need the passphrase that was recorded when the Secure Store Service was backed up to restore the Secure Store Service.

Using Central Administration to restore the Secure Store Service in SharePoint Server

## Using Central Administration to restore the Secure Store Service in SharePoint Server

Use the following procedure to restore the Secure Store Service by using Central Administration.

**To restore the Secure Store Service by using Central Administration**

Verify that the user account performing this procedure is a member of the Farm Administrators group.

Start Central Administration.

In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.

On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, select the backup job that contains the backup that you want, or a farm-level backup, from the list of backups, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup.

Note

If the correct backup job does not appear, in the **Backup Directory Location** text box, type the path of the correct backup folder, and then click **Refresh**. You cannot use a configuration-only backup to restore the Secure Store Service.

On the Restore from Backup — Step 2 of 3: Select Component to Restore page, expand **Shared Services Applications** and select the check box that is next to the Secure Store Service application backup group, and then click **Next**.

On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Farm\Shared Services\Shared Services Applications\<Secure Store Service name>** appears in the **Restore the following component** list.

In the **Restore Options** section, under **Type of restore**, select the **Same configuration** option. A dialog will appear that asks you to confirm the operation. Click **OK**.

Click **Start Restore**.

You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take a several seconds for the recovery to start.

If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the path that you specified in step 3.

After the restore operation has successfully completed, you must refresh the passphrase.

In Central Administration, on the home page, in the **Application Management** section, click **Manage service applications**.

On the Service Applications page, click the Secure Store Service name. You might receive an error that says "Unable to obtain master key."

On the Secure Store Service page, on the ribbon, click **Refresh Key**.

In the **Refresh Key** dialog, type the passphrase in the **Pass Phrase** box, and then click **OK**.

Using PowerShell to restore the Secure Store Service in SharePoint Server

## Using PowerShell to restore the Secure Store Service in SharePoint Server

You can use PowerShell to restore the Secure Store Service.

**To restore the Secure Store Service by using PowerShell**

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
Restore-SPFarm -Directory <BackupFolder> -Item <SecureStoreServicename> -RecoveryMethod Overwrite [-BackupId <GUID>] [-Verbose]
```

Where:

*<BackupFolder>* is the path for the backup folder where the service application was backed up.

*<SecureStoreServicename>* is the name of the Secure Store Service application.

If you have multiple backups use the  `BackupId` parameter to specify which backup to use. To view all of the backups for the farm, type the following command at the PowerShell command prompt:

```
Get-SPBackupHistory -Directory <BackupFolder> -ShowBackup
```

Note

If you do not specify a value for the  `BackupId` parameter, the most recent backup will be used. You cannot restore the Secure Store Service from a configuration-only backup.

After the restore operation has successfully completed, you must refresh the passphrase. At the PowerShell command prompt, type the following command:

```
Update-SPSecureStoreApplicationServerKey -Passphrase <Passphrase>
```

Where  *<Passphrase>*, is the one that you currently use.

Should errors occur while updating the Secure Store passphrase, see Refresh the Secure Store encryption key.

For more information, see Restore-SPFarm and Update-SPSecureStoreApplicationServerKey.

Note

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.

See also

## See also

Concepts

#### Concepts

Back up the Secure Store Service in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
