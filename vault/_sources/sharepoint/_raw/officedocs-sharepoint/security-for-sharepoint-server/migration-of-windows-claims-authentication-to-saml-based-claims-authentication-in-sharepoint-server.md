---
title: "Migration of Windows claims authentication to SAML based claims authentication in SharePoint Server - SharePoint Server"
description: "Learn how to migrate Windows claims authentication to SAML based claims authentication in SharePoint Server."
ms.topic: upgrade-and-migration-article
---
Note

Migrate Windows claims to SAML claims

# Migrate Windows claims to SAML claims

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Identifies the steps required to migrate a web application that is going from Windows claims authentication to SAML-based authentication in SharePoint Server.

Identity migration

## Identity migration

To run the identity migration, follow these steps:

**NOTE**:   These steps apply only to existing web applications.

- Generate a skip list- A skip list is comma-separated values file (.csv file) that has records to exclude during the identity migration. For example, it is necessary to exclude certain service applications or certain domain accounts

- Run the migration against the web application that has one or more content databases.

Migration of a web application

## Migration of a web application

To migrate a web application to include all the content databases by using Windows PowerShell.

- Check that you have the following memberships:

- The securityadmin fixed server role on the SQL Server instance.

- The db_owner fixed database role on all databases that are to be updated.

- The Administrators group on the server on which you are running Windows PowerShell cmdlets.

- Read about_Execution_Policies.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint cmdlets.

**NOTE**:   If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about Windows PowerShell permissions, see Permissions and Add-SPShellAdmin.

- To migrate a web application to include all content databases, type the following at the Windows PowerShell command prompt.

```
$skipFile = "FileName.csv"
$wa = Get-SPWebApplication -Identity "Name of web application"
$tp = Get-SPTrustedIdentityTokenIssuer "RegularUsers"
Convert-SPWebApplication -Identity $wa -From CLAIMS-WINDOWS -To CLAIMS-TRUSTED-DEFAULT -TrustedProvider $tp -SourceSkipList $skipFile
```

To migrate specific web applications and content databases by using Windows PowerShell.

- Check that you have the following memberships:

- The securityadmin fixed server role on the SQL Server instance.

- The db_owner fixed database role on all databases that are to be updated.

- The Administrators group on the server on which you are running Windows PowerShell cmdlets.

- Read about_Execution_Policies.

An administrator can use the Add-SPShellAdmin cmdlet to grant permissions to use SharePoint cmdlets.

**NOTE**:   If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about Windows PowerShell permissions, see Permissions and Add-SPShellAdmin.

- To migrate specific web applications and content databases, type the following at the Windows PowerShell command prompt.

```
$skipFile = "FileName.csv"
$wa = Get-SPWebApplication -Identity "Name of web application"
$database = Get-SPContentDatabase -Identity "DB_Name"
Convert-SPWebApplication -Identity $wa -Database $database -From CLAIMS-WINDOWS -To CLAIMS-TRUSTED-DEFAULT -SourceSkipList $skipFile
```

If you want to reverse the migration process, type the following at the Windows PowerShell command prompt.

```
$skipFile = "FileName.csv"
$wa = Get-SPWebApplication -Identity "Name of web application"
Convert-SPWebApplication -Identity $wa -From CLAIMS-TRUSTED-DEFAULT -To CLAIMS-WINDOWS -SourceSkipList $skipFile -Database $database 
```

**NOTE**:   For more information, see Get-SPContentDatabase, Get-SPWebApplication, and Convert-SPWebApplication.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
