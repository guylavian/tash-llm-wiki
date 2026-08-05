---
title: "Add a database server to an existing farm in SharePoint 2013 - SharePoint Server"
description: "Learn how to add a new database server to an existing SharePoint farm."
ms.topic: how-to
---
Note

Add a database server to an existing farm in SharePoint 2013

# Add a database server to an existing farm in SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can add more database servers at any time to respond to business or operations requirements. Because a database server contains the farm content, which can consist of diverse types of data and can have a fast growing document collection, the size of the farm databases can grow quickly. Storage capacity is often the key reason to add more database servers. Other reasons can include adding new features, improving performance and high availability.

Before you begin

## Before you begin

Normally, all that is required to add a database server to an existing SharePoint farm is to set up and configure a new database server and join it to the farm by referencing the new server when you add a feature or move database content to the new server. SharePoint 2013 automatically allocates and assigns new database resources as necessary when they are required.

Note

In the case of high availability, this is typically implemented as part of the initial farm topology design and deployment and is not included in this article. For more information about high availability for SQL Server 2008 R2 and SQL Server 2012, see High Availability Solution Overview and High Availability Solutions (SQL Server).

The procedures in this article are intended to show how to configure a new database server for a specific task in SharePoint 2013.

Prepare the new database server

## Prepare the new database server

Before you can use the new database server, you must prepare it so that it can be used in a SharePoint 2013 farm. Use the following steps as guidance to provision the new server.

Important

IT policy may require a database administrator (DBA) to complete some or all steps in these procedures.

**To provision the database server**

Verify that the user account that is performing this procedure is a member of the SQL Server database **dbcreator** fixed server role, the Farm Administrators SharePoint group, and Administrators group on the server.

Review Hardware and software requirements for SharePoint 2013

Install the operating system, and make sure that the following conditions are satisfied:

The disk configuration is the same as the existing server.

The operating system is updated to the same service pack or hotfix level as the existing server.

Install the same version of SQL Server that is installed on the existing farm database server.

For information about how to install and configure SQL Server 2008 R2 with Service Pack 1 (SP1) or SQL Server 2012 before you add them to an existing server farm, see SQL Server Installation (SQL Server 2008 R2)orQuick-Start Installation of SQL Server 2012.

Configure SQL Server, and confirm the following:

The database collation is LATIN1_General_CI_AS_KS_WS.

A logon account is created for the SharePoint 2013 Setup user account. This account will be the database owner for the new database.

- Install the same SQL Server service packs and hotfixes that are installed on the existing database server.

Configure and use the new database server

## Configure and use the new database server

Use the following procedures as a guide to configure a new database server to host specific SharePoint databases. This includes the following:

Create a new web application.

Move a site collection to the new server.

You can use either the SharePoint Central Administration website or Microsoft PowerShell to create a new web application. You must use PowerShell to move a site collection.

**To create a new web application**

Verify that the user account that is performing this procedure is a member of the SQL Server database **dbcreator** fixed server role and the Farm Administrators SharePoint group.

Use the Application Management page in the SharePoint Central Administration website to create a new web site.

Configure either classic mode authentication (Windows authentication) or claims-based authentication.

Configure IIS to use either the existing web site or create a new web site and configure the following settings:

Specify the port number that you want to use to access the web application.

Provide the URL you want to use to access the web application (optional).

Provide the path of the site directory on the server where the web site is hosted.

- Configure authentication and encryption for your web by using the following options.

Negotiate (Kerberos) or NTLM authentication

Anonymous access to the web site

Secure Sockets Layer (SSL)

Provide a URL for the domain name for all sites that users will access in this web application.

Use the existing application pool or create a new one.

Configure security for the application pool (predefined or configurable).

Identify the database server, database name, and authentication method for your new web application.

For detailed instruction, see Create a web application (SharePoint 2013).

**To move a site collection by using PowerShell**

The SharePoint 2013 content database stores all site content for a farm, this includes the site collection. Content databases can store more than one site collection. Whether you move a site collection between database servers or between databases the procedure is the same. If the site collection grows too large then it can be moved to a new content database using the same procedure.

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. For additional information about PowerShell permissions, see Add-SPShellAdmin.

- Verify that the following conditions are true:

The destination content database exists.

The source content database and destination content database reside on the same instance of SQL Server.

The source content database and destination content database are attached to the same web application.

Determine the size of the source site collection and verify that the destination hard disk has at least three times more free space than is required for the site collection.

Use the **Get-SPSiteAdministration** cmdlet to determine the size of a site collection. For more information, see Get-SPSiteAdministration

Use the **Move-SPSite** cmdlet to move a site collection from the source content database to the new content database. For more information, see Move-SPSite.

For detailed instructions, see Move site collections between databases in SharePoint Server.

See also

## See also

Other Resources

#### Other Resources

Deploy Windows Server 2008 R2

Install and Deploy Windows Server 2012

SQL Server Installation (SQL Server 2008 R2)

Install SQL Server 2012

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
