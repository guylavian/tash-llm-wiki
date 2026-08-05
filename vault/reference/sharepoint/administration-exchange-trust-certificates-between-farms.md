---
title: "Exchange trust certificates between farms in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-exchange-trust-certificates-between-farms
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/exchange-trust-certificates-between-farms
family: administration
documentKind: "how-to"
abstract: "Learn how to exchange trust certificates between the publishing farm and the consuming farm in SharePoint Server."
---

# Exchange trust certificates between farms in SharePoint Server - SharePoint Server

Note

Exchange trust certificates between farms in SharePoint Server

# Exchange trust certificates between farms in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In SharePoint Server, a farm can connect to and consume a service application that is published on another SharePoint Server farm. For this to occur, the farms must exchange trust certificates.

Both farms must participate in this exchange for service application sharing to work.

For more information about how to share service applications across farms see Share service applications across farms in SharePoint Server.

You must use Microsoft PowerShell commands to export and copy the certificates between farms. After the certificates are exported and copied, you can use either PowerShell commands or Central Administration to manage the trusts within the farm.

The instructions here assume the following criteria:

- That the servers that are used for these procedures are running PowerShell.

- That the administrator will select and use the same server in each farm for all steps in the process.

- If User Account Control (UAC) is turned on, you must run the PowerShell commands with elevated privileges.

Before you begin this operation, review Share service applications across farms in SharePoint Server for information about prerequisites.

Exporting and copying certificates

## Exporting and copying certificates

An administrator of the consuming farm must provide two trust certificates to the publishing farm: a root certificate and a security token service (STS) certificate. An administrator of the publishing farm must provide a root certificate to the consuming farm.

You can only export and copy certificates by using Windows PowerShell 3.0 or later.

To export the root certificate from the consuming farm

### To export the root certificate from the consuming farm

On a server that is running SharePoint Server on the consuming farm, verify that you have the following memberships:

- **securityadmin** fixed server role on the SQL Server instance.

- **db_owner** fixed database role on all databases that are to be updated.

- Administrators group on the server on which you are running the PowerShell cmdlets.

- Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

In the SharePoint Management Shell, run the following commands:

```
$CFrootCert = (Get-SPCertificateAuthority).RootCertificate

[System.IO.File]::WriteAllBytes('C:\ConsumingFarmRoot.cer', $CFrootCert.Export("Cert"))
```

Where `C:\ConsumingFarmRoot.cer` is the path of the root certificate.

To export the STS certificate from the consuming farm

### To export the STS certificate from the consuming farm

Verify that you have the following memberships:

- **securityadmin** fixed server role on the SQL Server instance.

- **db_owner** fixed database role on all databases that are to be updated.

- Administrators group on the server on which you are running the PowerShell cmdlets.

- Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

In the SharePoint Management Shell, run the following commands:

```
$stsCert = (Get-SPSecurityTokenServiceConfig).LocalLoginProvider.SigningCertificate

[System.IO.File]::WriteAllBytes('C:\ConsumingFarmSTS.cer', $stsCert.Export("Cert"))
```

Where `C:\ConsumingFarmSTS.cer` is the path of the STS certificate.

To export the root certificate from the publishing farm

### To export the root certificate from the publishing farm

On a server that is running SharePoint Server on the publishing farm, verify that you have the following memberships:

- **securityadmin** fixed server role on the SQL Server instance.

- **db_owner** fixed database role on all databases that are to be updated.

- Administrators group on the server on which you are running the PowerShell cmdlets.

- Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

In the SharePoint Management Shell, run the following commands:

```
$PFrootCert = (Get-SPCertificateAuthority).RootCertificate

[System.IO.File]::WriteAllBytes('C:\PublishingFarmRoot.cer', $PFrootCert.Export("Cert"))
```

Where `C:\PublishingFarmRoot.cer` is the path of the root certificate.

To copy the certificates

### To copy the certificates

- Copy the root certificate and the STS certificate from the server in the consuming farm to the server in the publishing farm.

- Copy the root certificate from the server in the publishing farm to a server in the consuming farm.

Managing trust certificates by using PowerShell

## Managing trust certificates by using PowerShell

Managing trust certificates in a farm involves establishing trust. This section describes how to establish trust on both the consuming and publishing farms by using PowerShell commands.

Establishing trust on the consuming farm

### Establishing trust on the consuming farm

To establish trust on the consuming farm, you must import the root certificate that was copied from the publisher farm and create a trusted root authority.

To import the root certificate and create a trusted root authority on the consuming farm

#### To import the root certificate and create a trusted root authority on the consuming farm

Verify that you have the following memberships:

- **securityadmin** fixed server role on the SQL Server instance.

- **db_owner** fixed database role on all databases that are to be updated.

- Administrators group on the server on which you are running the PowerShell cmdlets.

- Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

In the SharePoint Management Shell, run the following commands:

```
$trustCert = Get-PfxCertificate "<C:\PublishingFarmRoot.cer>"

New-SPTrustedRootAuthority "<PublishingFarm>" -Certificate $trustCert
```

Where:

- *<C:\PublishingFarmRoot.cer>* is the path of the root certificate that you copied to the consuming farm from the publishing farm.

- *<PublishingFarm>* is a unique name that identifies the publishing farm. Each trusted root authority must have a unique name.

Establishing trust on the publishing farm

### Establishing trust on the publishing farm

To establish trust on the publishing farm, you must import the root certificate that was copied from the consuming farm and create a trusted root authority. You must then import the STS certificate that was copied from the consuming farm and create a trusted service token issuer.

To import the root certificate and create a trusted root authority on the publishing farm

#### To import the root certificate and create a trusted root authority on the publishing farm

Verify that you have the following memberships:

- **securityadmin** fixed server role on the SQL Server instance.

- **db_owner** fixed database role on all databases that are to be updated.

- Administrators group on the server on which you are running the PowerShell cmdlets.

- Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

In the SharePoint Management Shell, run the following commands:

```
$trustCert = Get-PfxCertificate "<C:\ConsumingFarmRoot.cer>"

New-SPTrustedRootAuthority "<ConsumingFarm>" -Certificate $trustCert
```

Where:

- *<C:\ConsumingFarmRoot.cer>* is the name and location of the root certificate that you copied to the publishing farm from the consuming farm.

- *<ConsumingFarm>* is a unique name that identifies the consuming farm. Each trusted root authority must have a unique name.

To import the STS certificate and create a trusted service token issuer on the publishing farm

### To import the STS certificate and create a trusted service token issuer on the publishing farm

Verify that you have the following memberships:

- **securityadmin** fixed server role on the SQL Server instance.

- **db_owner** fixed database role on all databases that are to be updated.

- Administrators group on the server on which you are running the PowerShell cmdlets.

- Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

In the SharePoint Management Shell, run the following commands:

```
$stsCert = Get-PfxCertificate "<c:\ConsumingFarmSTS.cer>"

New-SPTrustedServiceTokenIssuer "<ConsumingFarm>" -Certificate $stsCert
```

Where:

- *<C:\ConsumingFarmSTS.cer>* is the path of the STS certificate that you copied to the publishing farm from the consuming farm.

- *<ConsumingFarm>* is a unique name that identifies the consuming farm. Each trusted service token issuer must have a unique name.

For more information about these PowerShell cmdlets, see the following articles:

- Get-SPCertificateAuthority

- Get-SPSecurityTokenServiceConfig

- New-SPTrustedRootAuthority

- New-SPTrustedServiceTokenIssuer

- Get-PfxCertificate

For information about how to use a script to automate part of this process, see Exchange trust certificates between farms.

Managing trust certificates by using Central Administration

## Managing trust certificates by using Central Administration

You can manage trusts on a farm only after the relevant certificates have already been exported and copied to the farm.

To establish trust by using Central Administration

### To establish trust by using Central Administration

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

On the SharePoint Central Administration website, click **Security**.

On the Security page, in the **General Security** section, click **Manage trust**.

On the Trust Relationship page, on the ribbon, click **New**.

On the Establish Trust Relationship page, do the following steps:

Supply a name that describes the purpose of the trust relationship.

Browse to and select the Root Authority Certificate for the trust relationship. This must be the Root Authority Certificate that was exported from the other farm by using Microsoft PowerShell, as described in Exporting and copying certificates.

If you are performing this task on the publishing farm, select the check box for **Provide Trust Relationship**. Type in a descriptive name for the token issuer and browse to and select the STS certificate that was copied from the consuming farm, as described in Exporting and copying certificates.

Click **OK**.

After a trust relationship is established, you can modify the Token Issuer description or the certificates that are used by clicking the trust, and then clicking **Edit**. You can delete a trust by clicking it, and then clicking **Delete**.

See also

## See also

Concepts

### Concepts

Plan for user authentication methods in SharePoint Server

Other Resources

### Other Resources

Create a web application in SharePoint Server

Configure SAML-based claims authentication with AD FS in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
