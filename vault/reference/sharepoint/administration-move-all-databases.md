---
title: "Move all databases in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-move-all-databases
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/move-all-databases
family: administration
documentKind: "upgrade-and-migration-article"
abstract: "Learn how to move all databases associated with SharePoint Server to a new database server."
---

# Move all databases in SharePoint Server - SharePoint Server

Note

Move all databases in SharePoint Server

# Move all databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can use the SharePoint Central Administration website, or SQL Server tools to move all databases that are associated with SharePoint Server to a new database server.

Before you begin

## Before you begin

The procedures in this article explain how to move the following kinds of databases that are hosted on a single database server:

Configuration database

Central Administration content database

Content databases

Service application databases

Important

To move database files within the same instance of SQL Server we recommend that you use the **FILENAME** clause of the **ALTER DATABASE** statement. For more information, see Move User Databases.

Note

To move a database to another instance of SQL Server or to another server, we recommend that you use procedures found in Database Detach and Attach (SQL Server) or Back Up and Restore of SQL Server Databases.

The following are the minimum permissions that are required to perform this process:

You must be a member of the Farm Administrators SharePoint group.

On the computer that is running the SharePoint Central Administration Web site, you must be a member of the Administrators group.

On the database server from which the databases are being moved, you must be a member of the following:

The Administrators group

The **db_backupoperator** fixed database role

On the database server to which the databases are being moved, you must be a member of the following:

The Administrators group

The **db_owner** fixed database role

In some environments, you must coordinate the move procedures with the database administrator. Be sure to follow applicable policies and guidelines for managing databases.

Important

When you move databases, all farm sites and assets are unavailable to users until the process is complete. Complete this operation outside normal business hours.

Move all databases

## Move all databases

To move all databases from one database server to another database server, you have to work in both SharePoint Server and SQL Server.

Before you begin this operation, review the steps in this process:

Prepare the new database server.

Close all open SharePoint Management Shell windows.

Stop all services that are related to SharePoint Server and Internet Information Services (IIS).

Detach the databases from the current SQL Server instance.

Copy or move all files that are associated with the databases (.mdf, .ndf, and .ldf), to the new destination server that runs SQL Server.

Make sure that all of the SQL Server logins, fixed server roles, fixed database roles, and permissions for the databases are configured correctly on the new destination database server.

Note

It is important that the destination server where you move the databases has the same database information that the current SQL Server instance has. For details about how to do this, see How to transfer logins and passwords between instances of SQL Server. For more information, see Server-Level Roles and Database-Level Roles.

Attach the databases to the new destination server that runs SQL Server.

Use SQL Server connection aliases to point to the new database server and update all web servers.

If you do not want to use SQL Server connection aliases use one of the following procedures to update the database connections for your SharePoint Server farm.

Scenario 1: Use this procedure to update the database connections if you use SharePoint Server and SQL Server Always On Availability Groups for high availability or disaster recovery.

Scenario 2: Use this procedure if you must use manual steps or if you move the databases from a SharePoint Server Single-server farm role installation to a new Single-server farm role installation.

- Restart all services that you stopped in step 3.

To prepare the new database server

### To prepare the new database server

Use the procedures in Configure SQL Server security for SharePoint Server to configure the new database server.

The new database server must run either the same version of Windows Server and SQL Server as the existing database server, or one of the following versions:

For SharePoint Server 2019:

Windows Server 2019

Windows Server 2016

SQL Server 2016

SQL Server 2017

For SharePoint Server 2016:

Windows Server 2012 R2

Windows Server 2016

SQL Server 2014 Service Pack 1 (SP1)

SQL Server 2016

For SharePoint 2013:

Windows Server 2008 R2

Windows Server 2008 R2 Service Pack 1 (SP1)

Windows Server 2012

SQL Server 2008

SQL Server 2012

SQL Server 2014

The version of the existing SharePoint Server and Windows Server must also support the version of the new SQL Server where the DBs are being moved. For more information, see Hardware and software requirements for SharePoint Server 2016 and Hardware and software requirements for SharePoint 2013.

To close all open sessions of SharePoint Management Shell

### To close all open sessions of SharePoint Management Shell

- Close all open SharePoint Management Shell windows, and all open command prompt windows.

To stop the farm

### To stop the farm

- On all SharePoint Servers in the farm, stop the following services:

SharePoint Administration

SharePoint Timer

SharePoint Tracing

SharePoint User Code Host

SharePoint VSS Writer

World Wide Web Publishing Service

SharePoint Server Search 16

- On all SharePoint Servers in the farm, at a command prompt, type **iisreset /stop**.

To detach databases

### To detach databases

In SQL Server Management Studio on the original database server, detach the databases that you want to move from the instance to which they are attached. If you are running many databases, you may want to run a Transact-SQL script to detach databases.

A database cannot be detached if any one of the following is true:

The database is being mirrored.

A database snapshot exists on the database.

For more information, see: Database Detach and Attach (SQL Server), Detach a Database, and sp_detach_db (Transact-SQL).

To move database files to the new server

### To move database files to the new server

Verify that the user account that is performing this procedure is a member of the following:

On the database server from which the databases are being moved, you must be a member of the following:

The Administrators group

The **db_backupoperator** fixed database role

On the database server to which the databases are being moved, you must be a member of the following:

The Administrators group

The **db_owner** fixed database role

Use Windows Explorer to locate the .mdf, .ldf, and .ndf files that are associated with each database that you are moving.

Copy or move the files to the destination directory on the new computer that is running SQL Server.

To set up permissions on the new server

### To set up permissions on the new server

- Verify that the user account that is performing this procedure is a member of the following:

The Administrators group

The **db_owner** fixed database role

On the destination database server, start Management Studio and transfer your logon credentials and permissions from the original instance to the destination instance. We recommend that you transfer permissions by running a script. An example script is available in How to transfer logins and passwords between instances of SQL Server.

For more information about how to transfer SQL Server metadata between instances, see Managing Metadata When Making a Database Available on Another Server Instance.

To attach databases to the new instance of SQL Server

### To attach databases to the new instance of SQL Server

- Verify that the user account that is performing this procedure is a member of the following:

The Administrators group

The **db_owner** fixed database role

- On the destination database server, attach the databases to the new instance. For more information, see Attach a Database and sp_attach_db (Transact-SQL).

The following procedures provide methods to connect to the new SQL Server instance or update the database connections. Use the procedure that works best for your SharePoint Server farm environment.

Important

If you're using SharePoint Server and SQL Server Always On Availability Groups before moving the databases, you should point to the AG Listner. If you're moving from a single-server farm to an AlwayOn Availability Group then you should use the cliconfg.exe.

To point the web application to the new database server by setting up SQL Server connection aliases

### To point the web application to the new database server by setting up SQL Server connection aliases

This procedure must be performed on all servers in the SharePoint Server farm that connect to the instance of SQL Server that hosts the databases.

Verify that the user account that is performing this procedure is a member of the following:

The Administrators group

The **db_owner** fixed database role

Start the SQL Server Client Network Utility (cliconfg.exe). This utility is typically located in the C:\Windows\SysWOW64 and C:\Windows\System32 folder.

On the **General** tab, verify that TCP/IP is enabled.

On the **Alias** tab, click **Add**. The Add Network Library Configuration window appears.

In the **Server alias** box, enter the name of the current instance of SQL Server.

In the **Network libraries** area, click **TCP/IP**.

In the **Connection parameters** area, in the **Server name** box, enter the new server name and instance to associate with the alias, and then click **OK**. This is the name of the new server that is hosting the SharePoint Server databases.

Repeat steps 3 through 8 on all servers in the farm that connect to the new instance of SQL Server.

Optional. If your environment relies on System Center 2012 - Data Protection Manager (DPM) or a third-party application that uses the Volume Shadow Copy Service framework for backup and recovery, you must install the SQL Server connectivity components on each web server or application server by running SQL Server setup. For more information, see Install SQL Server 2014 from the Installation Wizard (Setup) and Windows Server Installation and Upgrade.

You can use these Microsoft PowerShell cmdlets to deploy, manage, and remove availability groups in SQL Server with SharePoint Server:

**Add-DatabaseToAvailabilityGroup**

**Remove-DatabaseFromAvailabilityGroup**

**Get-AvailabilityGroupStatus**

Use the following procedure to update the database connections if you use SharePoint Server and SQL Server Always On Availability Groups for high availability or disaster recovery.

**Scenario 1: To update the database connections by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following commands:

```
Add-DatabaseToAvailabilityGroup -AGName "<AGGroupName>" -DatabaseName "<DatabaseName>" [-FileShare "<\\server\share>"]
```

Where:

<AGGroupName> is the name of the Availability Group.

<DatabaseName> is the name of the database that you are adding to the Availability Group

If the optional **-FileShare** parameter is used, <\server\share> is the name of the server and the share that you use.

- Repeat these steps for all databases that you move, including the Configuration and Central Administration Content databases.

Use the next procedure for the following scenarios:

If you must use manual steps

If you move the databases from a SharePoint Server 2016 Single-Server Farm role type to a new Single-Server Farm role type or from a SharePoint 2013 single-server installation to a new single-server installation.

Note

The Single-Server Farm role replaces the Standalone Install mode available in previous SharePoint Server releases. For more information, see Overview of MinRole Server Roles in SharePoint Server 2016.

If you use Availability Groups then you must manually add the databases to the availability groups as appropriate to their high availability/disaster recovery support. For more information, see Add a Database to an Availability Group (SQL Server)

If you use SQL Mirroring then make sure your mirroring is setup appropriately. For more information, see Setting Up Database Mirroring (SQL Server) and Database Mirroring (SQL Server).

**Scenario 2: To update the database connections by using Microsoft PowerShell**

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following commands:

```
$db = Get-SPDatabase -Identity <guid>
```

Where <GUID> is the ID of the database that you move.

Note

Use **Get-SPDatabase** without parameters to see a list of all databases with GUIDs.

```
$db.ChangeDatabaseInstance("<DBServerName>")
```

Where <DBServerName> is the name or alias of the new SQL Server or is the Always On Availability Group listener DNS name.

```
$db.Update()
```

- If you use SQL Server database mirroring then you must remember to populate the FailoverServiceInstance property on the SharePoint database.

```
$db.failoverserviceinstance("<DBServerName>")
```

Where <DBServerName> is the name or alias of the mirrored SQL Server.

```
$db.update()
```

- Repeat these steps for all databases that you move, including the Configuration and Central Administration Content databases.

To restart the services in the farm

### To restart the services in the farm

Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.

On all SharePoint Servers in the farm, at a command prompt, type **iisreset /start**.

In the Microsoft Management Console Services snap-in, start all of the services that are related to SharePoint Server and IIS. These include the following services:

SharePoint Administration

SharePoint Timer

SharePoint Tracing

SharePoint User Code Host

SharePoint VSS Writer

World Wide Web Publishing Service

SharePoint Server Search

See also

## See also

Concepts

#### Concepts

Database types and descriptions in SharePoint Server

Other Resources

#### Other Resources

Quick reference guide: SharePoint Server 2016 databases

Databases that support SharePoint 2013

Add a database server to an existing farm in SharePoint 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
