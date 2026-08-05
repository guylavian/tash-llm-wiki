---
title: "All State Service databases are paused for a State Service Application (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-all-state-service-databases-are-paused-for-a-state-service-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/all-state-service-databases-are-paused-for-a-state-service-application
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: All State Service databases are paused for a State Service Application."
---

# All State Service databases are paused for a State Service Application (SharePoint Server) - SharePoint Server

Note

All State Service databases are paused for a State Service Application (SharePoint Server)

# All State Service databases are paused for a State Service Application (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** All State Service databases are paused for a State Service Application

**Summary:** All of the databases associated with a State Service service application are paused. This may result in errors when using some SharePoint Server 2016 and SharePoint 2013 components such as InfoPath Web browser forms and the Microsoft SharePoint Chart Web Part.

**Cause:** This might be caused by the administrator pausing all databases for the service application.

**Resolution: Resume the State Service service application databases by using Microsoft PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you don't have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

For more information about how to interact with Windows Server 2012 R2, see Common Management Tasks and Navigation in Windows.

To identify the paused database, type the following command at the PowerShell command prompt:

```
Get-SPStateServiceDatabase
```

If you want to resume a paused database, type the following command at the Windows PowerShell command prompt:

```
Resume-SPStateServiceDatabase -Identity <DatabaseID>
```

Where:

- *<DatabaseID>* is the identifier for the State Service service application database as a GUID.

If you want to create a new database instead of using an existing database, type the following command at the Windows PowerShell command prompt:

```
New-SPStateServiceDatabase -Name <DatabaseName> -ServiceApplication <ID> -DatabaseServer <ServerName> [-DatabaseCredentials <Credential>] 
```

Where:

*<DatabaseName>* is name of the database as a string.

*<ID>* is the identifier for the affected State Service service application as a string or a GUID. If there's only one State Service service application, you don't have to specify this parameter.

*<ServerName>* is name of the database server.

*<Credential>* is SQL Server authentication credentials for the database server. If this parameter isn't specified, Windows authentication will be used.

For more information, see Resume-SPStateServiceDatabase or New-SPStateServiceDatabase.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
