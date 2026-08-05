---
title: "Initial deployment administrative and service accounts in SharePoint Server - SharePoint Server"
description: "Learn about the administrative and service accounts you need to initially install SharePoint Server."
ms.topic: install-set-up-deploy
---
Note

Initial deployment administrative and service accounts in SharePoint Server

# Initial deployment administrative and service accounts in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article provides information about the administrative and service accounts that you need for an initial SharePoint Server deployment. Additional accounts and permissions are required to fully implement all aspects of a production farm.

Note

For a complete list of permissions for SharePoint Servers 2016 and 2019, see Account permissions and security settings in SharePoint Servers 2016 and 2019. > For a complete list of permissions for SharePoint Server 2013, see Account permissions and security settings in SharePoint 2013.

Important

Do not use service account names that contain the symbol $ with the exception of using a Group Managed Service Account for SQL Server.

Required accounts in SharePoint Server

## Required accounts in SharePoint Server

To deploy SharePoint Server on a server farm, you must provide credentials for several different accounts.

The following table describes the accounts that you can use to install and configure SharePoint Server.

| **Account** | **Purpose** | **Requirements** |
| --- | --- | --- |
| SQL Server service account | The SQL Server service account is used to run SQL Server. It is the service account for the following SQL Server services:  
  MSSQLSERVER  
  SQLSERVERAGENT  
  If you do not use the default SQL Server instance, in the Windows Services console, these services will be shown as the following:  
  MSSQL<InstanceName>  
  SQLAgent<InstanceName> | Use either a domain user account or preferably, a Group Managed Service Account.  
 If you plan to back up to or restore from an external resource, permissions to the external resource must be granted to the appropriate account. If you use a domain user account or Group Managed Service Account for the SQL Server service account, grant permissions to that domain user account. However, if you use the Network Service or the Local System account, grant permissions to the external resource to the machine account (<domain_name>\<SQL_hostname>).  
 The instance name is arbitrary and was created when SQL Server was installed. |
| Farm administrator user account | The farm administrator user account is a uniquely identifiable account assigned to a SharePoint admin. It is used to run the following:  
  Setup  
  SharePoint Products Configuration Wizard | Domain user account.  
  Member of the Administrators group on each SharePoint server in the farm.  
  Member of the following SQL Server role (optional): **sysadmin** fixed server role.  
  If you run Windows PowerShell cmdlets that affect a database, this account must be a member of the **db_owner** fixed database role for the database or a member of the **sysadmin** fixed server role on SQL. |
| Farm service account | The farm service account is used to perform the following tasks:  
  Act as the application pool identity for the SharePoint Central Administration website.  
  Run the Microsoft SharePoint Foundation Workflow Timer Service. | Domain user account.  
  Additional permissions are automatically granted for the server farm account on Web servers and application servers that are joined to a server farm.  
  The server farm account is automatically added as a SQL Server login on the computer that runs SQL Server. The account is added to the following SQL Server security roles:  
 * **dbcreator** fixed server role  
 * **securityadmin** fixed server role  
 * **db_owner** fixed database role for all SharePoint databases in the server farm  
 This account should not be used interactively by an administrator. |

Note

We recommend that you install SharePoint Server by using least-privilege administration.

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
