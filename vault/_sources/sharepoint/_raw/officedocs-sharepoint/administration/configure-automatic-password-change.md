---
title: "Configure automatic password change in SharePoint Server - SharePoint Server"
description: "Learn about how to configure the automatic password changes in SharePoint Server."
ms.topic: how-to
---
Note

Configure automatic password change in SharePoint Server

# Configure automatic password change in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Automatic password change enables SharePoint Server to automatically generate long, encrypted passwords on a schedule that you can determine.

Configure managed accounts

## Configure managed accounts

You have to register managed accounts together with the farm to make the accounts available to multiple services. You can register a managed account by using the Register Managed Account page in the SharePoint Central Administration website. There are no options on the Register Managed Account page to create an account in Active Directory Domain Services, or on the local computer. The options can be used to register an existing account on the SharePoint Server farm. Perform the steps in the following procedure to use Central Administration to configure managed account settings.

**To configure managed account settings by using Central Administration**

Verify that the user account that is performing this procedure is a farm administrator.

On the Central Administration, select **Security**.

Under **General Security**, click **Configure managed accounts**.

On the Managed Accounts page, click **Register Managed Account**.

In the **Account Registration** section of the Register Managed Account page, enter the service account credentials.

In the **Automatic Password Change** section, select the **Enable automatic password change** check box to allow SharePoint Server to manage the password for the selected account. Next, enter a numeric value that indicates the number of days before password expiration that the automatic password change process will be initiated.

In the **Automatic Password Change** section, select the **Start notifying by e-mail** check box, and then enter a numeric value that indicates the number of days before the initiation of the automatic password change process that an e-mail notification will be sent. You can then configure a weekly or monthly e-mail notification schedule.

Click **OK**.

Configure automatic password change settings

## Configure automatic password change settings

Use the Password Management Settings page of Central Administration to configure farm-level settings for automatic password changes. Farm administrators can configure the notification e-mail address that will be used to send all password change notification e-mails in addition to monitoring and scheduling options. Perform the steps in the following procedure to use Central Administration to configure automatic password change settings.

**To configure automatic password change settings by using Central Administration**

Verify that the user account that is performing this procedure is a farm administrator.

On the Central Administration Home page, click **Security**.

Under **General Security**, click **Configure password change settings**.

In the **Notification E-Mail Address** section of the Password Management Settings page, enter the e-mail address of one person or group to be notified of any imminent password change or expiration events.

If automatic password change isn't configured for a managed account, enter a numeric value in the **Account Monitoring Process Settings** section that indicates the number of days before password expiration that a notification will be sent to the e-mail address configured in the **Notification E-Mail Address** section.

In the **Automatic Password Change Settings** section, enter a numeric value that indicates the number of seconds that automatic password change will wait (after notifying services of a pending password change) before starting the change. Enter a numeric value that indicates the number of times a password change will be tried before the process stops.

Click **OK**.

Troubleshooting automatic password change

## Troubleshooting automatic password change

Use the following guidance to avoid the most common issues that can occur when you configure automatic password change.

Password mismatch

### Password mismatch

If the automatic password change process fails because there's a password mismatch between Active Directory Domain Services (AD DS) and SharePoint Server, the password change process can result in access denial at logon, an account lockout, or AD DS read errors. If any of these issues occur, make sure that your AD DS passwords are configured correctly and that the AD DS account has read access for setup. Use Microsoft PowerShell to fix any password mismatch issues that might occur, and then resume the password change process.

**To correct for a password mismatch by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

From the PowerShell command prompt, type the following:

```
Set-SPManagedAccount [-Identity] <SPManagedAccountPipeBind> -ExistingPassword <SecureString> -UseExistingPassword $true
```

For more information, see Set-SPManagedAccount.

Service account provisioning failure

### Service account provisioning failure

If service account provisioning or reprovisioning fails on one or more servers in the farm, check the status of the Timer Service. If the Timer Service has stopped, restart it. Consider using the following Stsadm command to immediately start Timer Service administration jobs:  `stsadm -o execadmsvcjobs`

If restarting the Timer Service doesn't resolve the issue, use PowerShell to repair the managed account on each server in the farm that has experienced a provisioning failure.

**To resolve a service account provisioning failure**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

From the PowerShell command prompt, type the following:

```
Repair-SPManagedAccountDeployment
```

For more information, see Repair-SPManagedAccountDeployment.

If the previous procedure doesn't resolve a service account provisioning failure, it's likely because the farm encryption key can't be decrypted. If this is the issue, use PowerShell to update the local server pass phrase to match the pass phrase for the farm.

**To update the local server pass phrase**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

From the PowerShell command prompt, type the following:

```
Set-SPPassPhrase -PassPhrase <SecureString> -ConfirmPassPhrase <SecureString> -LocalServerOnly $true
```

For more information, see Set-SPPassPhrase.

Imminent password expiration

### Imminent password expiration

If the password is about to expire, but automatic password change hasn't been configured for this account, use PowerShell to update the account password to a new value that can be chosen by the administrator or automatically generated. After you have updated the account password, make sure that the Timer Service is started and the Administrator Service is enabled on all servers in the farm. Then, the password change can be propagated to all of the servers in the farm.

Note

When an administrator performs a password change for the servers in the SharePoint search topology, there is an implied query downtime when the services are restarted. The query downtime is typically in the range of 3-5 minutes.

**To update the account password**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running the PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For more information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

To update the account password to a new automatically generated value, from the PowerShell command prompt, type the following:

```
Set-SPManagedAccount [-Identity] <SPManagedAccountPipeBind> -AutoGeneratePassword $true
```

For more information, see Set-SPManagedAccount.

Requirement to change the farm account to a different account

### Requirement to change the farm account to a different account

If you must change the farm account to a different account, use the following Stsadm command:  `stsadm.exe -o updatefarmcredentials -userlogin DOMAIN\username -password password`

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
