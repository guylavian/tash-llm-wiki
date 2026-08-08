---
title: "Deploy SharePoint Server with Azure SQL Managed Instance - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-deploy-azure-sql-managed-instance-with-sharepoint-servers
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/deploy-azure-sql-managed-instance-with-sharepoint-servers
family: administration
documentKind: "install-set-up-deploy"
abstract: "Learn how to deploy SharePoint Servers 2016, 2019, and Subscription Edition with Azure SQL Managed Instance (MI)."
---

# Deploy SharePoint Server with Azure SQL Managed Instance - SharePoint Server

Note

Deploy SharePoint Server with Azure SQL Managed Instance

# Deploy SharePoint Server with Azure SQL Managed Instance

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server 2016, SharePoint Server 2019, and SharePoint Server Subscription Edition support Azure SQL Managed Instance (MI). SQL MI is a deployment option of Azure SQL Database and is compatible with the current version of SQL Server (on-premises), Enterprise Edition Database Engine.

Important

SharePoint Server farms must be hosted in Microsoft Azure to support Azure SQL MI. The SharePoint Server farm and the managed instance must be hosted in the same Azure region. SharePoint Server farms don't support managed instances when hosted in customer datacenters.

Deploying SharePoint Server with an Azure SQL MI lets you move your SQL Server on-premises application to the cloud with little or no application and database changes. The following procedure shows how to deploy SharePoint Server 2016, 2019, or Subscription Edition with an Azure SQL MI.

Environment

## Environment

Create a resource group with a vNet and then create two subnets. You can use the SQL Managed Instance Virtual Network Environment template to create an Azure Virtual Network with two subnets.

Create subnet 1 (Default) and then create two Virtual Machines (VMs). First, set up VM 1 as an Active Directory Directory Services domain controller and configure your domain. For more information, see Step-By-Step: Setting up Active Directory in Windows Server 2016.

Install SharePoint Server 2016 or SharePoint Server 2019 or SharePoint Server Subscription Edition in VM 2:

Run **`PrerequitsiteInstaller.exe`**.

Run **`Setup.exe`**.

If you're using SharePoint Server 2016 or SharePoint Server 2019, install the May 2019 (or newer) sts core patch for SharePoint Server 2016 (KB 4464549) or for SharePoint Server 2019 (KB 4464556).

If you're using SharePoint Server 2016 or SharePoint Server 2019, install the April 2019 (or newer) wssloc MUI/language pack patch for SharePoint Server 2016 (KB 4461507) or for SharePoint Server 2019 (KB 4462221).

Note

You can join other VMs to Active Directory in subnet 1.

No updates need to be installed for SharePoint Server Subscription Edition.

Create an Azure SQL MI in subnet 2 within this resource group (ManagedInstance).

Important

No other resources can reside in subnet 2 except for SQL MI.

Create or join the SharePoint farm, hosting the databases on SQL MI, with SQL authentication.

To create the SharePoint farm, open the **SharePoint Management Shell** and run the following Windows PowerShell commands:

```
   $FarmCredential = Get-Credential -Message "Provide the user name and password for the SharePoint farm service account." 
   $DBCredential = Get-Credential -Message "Provide the user name and password for the Azure SQL Managed Instance database login." 
   $FarmPassphrase = Read-Host -AsSecureString -Prompt "Provide the SharePoint farm passphrase" 

   New-SPConfigurationDatabase -DatabaseServer <DBServer> -DatabaseName <ConfigDB> -FarmCredentials $FarmCredential -DatabaseCredentials $DBCredential -Passphrase $FarmPassphrase -LocalServerRole <ServerRole> 
```

To join additional VMs to the SharePoint farm, open the **SharePoint Management Shell** on the additional VMs and run the following Windows PowerShell commands:

```
   $DBCredential = Get-Credential -Message "Provide the user name and password for the Azure SQL Managed Instance database login." 
   $FarmPassphrase = Read-Host -AsSecureString -Prompt "Provide the SharePoint farm passphrase" 

   Connect-SPConfigurationDatabase -DatabaseServer <DBServer> -DatabaseName <ConfigDB> -DatabaseCredentials $DBCredential -Passphrase $FarmPassphrase -LocalServerRole <ServerRole> 
```

Where:

- *<DBServer>* is the name you gave the Azure SQL MI in Step 4.

- *<ConfigDB>* is the name of the SharePoint configuration database to be created.

- *<ServerRole>* is the SharePoint MinRole server role for this server in the SharePoint farm.

Run the **SharePoint Products Configuration Wizard** to complete the configuration. Next, open Central Administration to complete the **Farm Configuration Wizard**.

Note

SharePoint Server doesn't support connecting to databases hosted in Azure SQL MI using Windows authentication.

Note

Access Services isn't supported with Azure SQL MI.

Update SQL password

## Update SQL password

Create a second admin account in the SQL MI Portal.

Run the following commands in SharePoint PowerShell to change the username and password for the second admin account:

```
$servers = Get-SPServer
foreach ($server in $servers) {
   $instance = $server.ServiceInstances | Where-Object {$_.TypeName -eq "Microsoft SharePoint Foundation Database"}
   if ($null -ne $instance) {
      break;
   }
}
$instance.SecureDBCredential.Username = "<username>"
$instance.SecureDBCredential.Password = "<password>"
$instance.SecureDBCredential.Update()
$instance.Update()
$SPDBs = Get-SPDatabase
foreach ($DB in $SPDBs)
{
   $DB.Username = "<username>"
   $DB.Password = "<password>"
   $DB.Update()
}
```

Modify the original account password in the SQL MI Portal.

Using the above script in SharePoint PowerShell, change the username and password to original account with new password.

Set the second admin account as **Inactive** or delete the second admin account.

See also

## See also

Other Resources

#### Other Resources

Azure SQL Database managed instance

SQL Server instance migration to Azure SQL Database managed instance

Quickstart: Create an Azure SQL Database managed instance

Quickstart: Configure Azure VM to connect to an Azure SQL Database Managed Instance

Quickstart: Restore a database to a Managed Instance

Additional resources

## Additional resources

- Last updated on 
		2025-02-21
