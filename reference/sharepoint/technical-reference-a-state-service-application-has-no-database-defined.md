---
title: "A State Service Application has no database defined (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-a-state-service-application-has-no-database-defined
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/a-state-service-application-has-no-database-defined
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: A State Service Application has no database defined."
---

# A State Service Application has no database defined (SharePoint Server) - SharePoint Server

Note

A State Service Application has no database defined (SharePoint Server)

# A State Service Application has no database defined (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** A State Service Application has no database defined.

**Summary:** A State Service service application has no State Service database defined. This may result in errors when using some SharePoint components such as InfoPath Web browser forms and the Microsoft SharePoint Server Chart Web Part.

**Cause:** One or more of the following might be causing this:

The farm administrator deleted all databases associated with the State Service service application.

The farm administrator never created or associated a database with the State Service service application.

**Resolution: Create a new database or use an existing database for the State Service service application by using Microsoft PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you're running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.

Note

If you don't have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

For more information about how to interact with Windows Server 2012, see Common Management Tasks and Navigation in Windows.

If no database already exists that you can use, type the following command at the PowerShell command prompt:

```
New-SPStateServiceDatabase -Name <DatabaseName> -DatabaseServer <ServerName> [-DatabaseCredentials <Credential>] [-ServiceApplication <ID>]
```

Where:

*<DatabaseName>* is name of the database as a String.

*<ServerName>* is name of the database server.

*<Credential>* is SQL Server authentication credentials for the database. If this parameter isn't used, Windows authentication will be used.

*<ID>* is the identifier for the State Service service application as a string or a GUID. If there's only one State Service service application, you don't have to specify this parameter.

In some environments, you must connect to an existing, empty SQL database. In this case, type the following command at the Windows PowerShell command prompt:

```
Mount-SPStateServiceDatabase -Name <DatabaseName> -DatabaseServer <ServerName> [-DatabaseCredentials <Credential>] [-ServiceApplication <ID>]
```

Where:

*<DatabaseNname>* is name of the database as a String.

*<ServerName>* is name of the database server.

*<Credential>* is the SQL Server authentication credentials for the database. If this parameter isn't used, Windows authentication will be used.

*<ID>* is the identifier for the State Service service application as a string or a GUID. If there's only one State Service service application, you don't have to specify this parameter.

For more information, see Mount-SPStateServiceDatabase or New-SPStateServiceDatabase.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
