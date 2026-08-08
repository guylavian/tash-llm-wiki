---
title: "Move or rename service application databases in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-move-or-rename-service-application-databases
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/move-or-rename-service-application-databases
family: administration
documentKind: "upgrade-and-migration-article"
abstract: "Learn how to move or rename service application databases in SharePoint Server."
---

# Move or rename service application databases in SharePoint Server - SharePoint Server

Note

Move or rename service application databases in SharePoint Server

# Move or rename service application databases in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn how to move or rename service application databases in SharePoint Server.

The main reason to move service application databases to another farm database server is to load balance the farm. Or you might need to move it to newer hardware.

Renaming service application databases is often done to remove the GUID from the database name after you've used SharePoint Products Configuration Wizard and SharePoint Server Product Configuration Wizard to create the service application databases in your farm. You might also need to align the database names with your organization's naming standards.

Both moving and renaming service application databases follow the same basic process, but there are a few more steps when you are moving service application databases.

Move or rename SharePoint Server service application databases using Microsoft SQL Server Management Studio or Microsoft PowerShell.

Point the SharePoint service application to the moved or renamed database using either the SharePoint Central Administration website or PowerShell.

Depending on how many service application databases you move or rename, pointing the service application to the database can be complex. Different service applications require different methods to point to the moved or renamed database.

These service application databases use the following steps:

App Management Service

Managed Metadata Service

PerformancePoint Service

Secure Store Service

SharePoint Translation Service

State Service

Subscription Settings Service

Word Automation Services

Stop or disable the service application.

Detach the database.

Move or rename the database.

Attach the database.

Point the service application to the moved or renamed database.

Restart the service application.

The Business Data Connectivity Service and User Profile Service applications databases require the following steps to move or rename the databases:

Stop or disable the service application.

Detach the database.

Move or rename the database.

Attach the database.

Point the service application to the moved or renamed database.

Delete the service application.

Recreate the service application.

Restart the service application.

The Search Service application databases require the following steps:

Pause the service application.

Set the Search service application to Read-Only.

Backup the service application.

Set the max degree of parallelism to 1 in the new server that hosts SQL Server.

Restore the Search service application to a new database server.

Set the Search Service application to read/write.

Start the service application.

Point the Search service application to the moved or renamed databases.

General steps to move or rename service application databases by using SQL Server

## General steps to move or rename service application databases by using SQL Server

To move a service application database, you must use SQL Server. To rename a service application database, you must use SQL Server and File Explorer.

Caution

Don't attempt to move and rename a database in one procedure. You should either move a database or rename a database, not perform both actions at the same time.

When you move or rename service application databases, the first step is to stop the service application for the database that you are changing. You can stop or start services by using Central Administration or PowerShell.

Step 1: To stop the service application by using Central Administration

### Step 1: To stop the service application by using Central Administration

Use an account that is a member of the Farm Administrators SharePoint group.

In Central Administration click **System Settings**.

On the System Settings page, in the **Servers** section, click **Manage services on server**.

Find the service application that you want to stop, click **Stop** or **Disable** in the **Action** column for the service, and then click **OK**.

To stop a service by using PowerShell

### To stop a service by using PowerShell

Use an account with these memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Note

For additional information about Microsoft PowerShell permissions, see Permissions.

Start the SharePoint Management Shell.

You need to know the service GUID for the next step. Use the **Get-SPServiceInstance** cmdlet to retrieve a list of all services in the farm together with their GUIDs.

At the PowerShell command prompt, type the following command:

```
Stop-SPServiceInstance -Identity <ServiceGUID>
```

Where  *<ServiceGUID>* is the GUID of the service.

For more information, see Stop-SPServiceInstance.

Move a database by using SQL Server Management Studio and File Explorer

### Move a database by using SQL Server Management Studio and File Explorer

Moving a database requires that you first detach the database from the SQL Server, move the files to the new location by using File Explorer, and then attach the database to the new instance of SQL Server.

Step 2: To detach a database from SQL Server

#### Step 2: To detach a database from SQL Server

Use an account that has the **db_owner** fixed database role for all of the databases that you're moving.

In SQL Server Management Studio, connect to the SQL Server instance that the service application database is attached to, and then expand the **Databases** node.

Right-click the database, point to **Tasks**, and then click **Detach**. Repeat this step for each database that you want to move.

Step 3: To move the database files to a new location by using File Explorer

#### Step 3: To move the database files to a new location by using File Explorer

Use an account that has read permission on the source location and write permission on the target location.

In File Explorer, find the .mdf, .ndf, and .ldf files for the service application databases and select the ones you want to move. The database files are typically found here,  `C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLServer\MSSQL\Data`

Either copy or move the database files to the new location.

Step 4: To attach a database to a new instance of SQL Server

#### Step 4: To attach a database to a new instance of SQL Server

Use an account that has the **db_owner** fixed database role for all of the databases that you're moving.

In SQL Server Management Studio, open the destination SQL Server instance.

Right-click the **Databases** node, point to **Tasks**, and then click **Attach**.

In the **Attach Database** dialog, browse to where you moved the .mdf, .ndf, and .ldf files, select the .mdf file for the database that you want to attach, and then click **OK**. Repeat this step for each database that you're moving.

Rename a database by using SQL Server Management Studio

### Rename a database by using SQL Server Management Studio

Renaming a service application database is a two step process, first stop the service, just as if you were going to move the database. You then rename the database by using SQL Server Management Studio.

**Step 3: To rename a database by using SQL Server**

In SQL Server Management Studio, connect to the source SQL Server instance, and then expand the **Databases** node.

Right-click the database that you want to rename, click **Rename**, and then type the new name. Repeat this step for each database that you're renaming.

Point a SharePoint Server service application to a moved or renamed database

### Point a SharePoint Server service application to a moved or renamed database

Pointing to the moved or renamed database is the next step. You can do this with either Central Administration or PowerShell. Using Central Administration to point service applications to the moved or renamed databases is the same for most of the SharePoint Server service applications. Using PowerShell to point service applications to the moved or renamed databases differs for each service application. This section provides guidance for each service application and database.

Step 5: To point the service application to a moved or renamed database by using Central Administration

#### Step 5: To point the service application to a moved or renamed database by using Central Administration

Use an account that is a member of the Farm Administrators SharePoint group.

In Central Administration, under **Application Management**, click **Manage service applications**.

On the Manage Service application page, click the empty area in the row next to the service application name. The ribbon becomes active, click **Properties** and the **Edit Service Application** dialog appears.

Change the database server or database name, and then click **OK**.

To point the Managed Metadata service application to a moved or renamed database by using PowerShell

#### To point the Managed Metadata service application to a moved or renamed database by using PowerShell

Use an account with these memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Note

For additional information about Microsoft PowerShell permissions, see Permissions.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
$app = Get-SPServiceApplication -Name "<ServiceApplicationName>"
Set-SPMetadataServiceApplication -Identity "<Name/GUID of service application>" $app -DatabaseName "<DatabaseName>" -DatabaseCredentials PSCredential object>
```

Where:

*<ServiceApplicationName>* is the name of the Managed Metadata service application.

*<DatabaseName>* is the name of the renamed database.

To point the PerformancePoint service application to a renamed or moved database by using PowerShell

#### To point the PerformancePoint service application to a renamed or moved database by using PowerShell

Use an account with these memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Note

For additional information about Microsoft PowerShell permissions, see Permissions.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Set-SPPerformancePointServiceApplication -Identity "<ServiceApplicationName>" -SettingsDatabase "<DatabaseServerName\DatabaseName>"
```

Where:

*<ServiceApplicationName>* is the name of the PerformancePoint service application.

*<DatabaseServerName\DatabaseName>* is the location of and the name of the renamed or moved database. Do not include the location if you are just renaming the database.

The State Service database stores temporary state information data. You can use PowerShell to point the State Service service application to a moved database by performing one of the following procedures:

Add a new database in the new location, or create a database with a new name. Then add the new database to the service application, and delete the old database. For details, see To add a new database to the State service application, and remove an old database by using Microsoft PowerShell.

Dismount the old database, move it by using SQL Server, and then remount the State Service database. For details, see To point the State service application to a moved database by using Microsoft PowerShell.

The following procedures all include the steps shown in the bullet list. So, they do not require that these steps are already performed:

Stopping a service application

Moving a database by using SQL Server Management Studio and Windows

To add a new database to the State Service service application and remove an old database by using PowerShell

#### To add a new database to the State Service service application and remove an old database by using PowerShell

Use an account with these memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Note

For additional information about Microsoft PowerShell permissions, see Permissions.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command to create a new database:

```
New-SPStateServiceDatabase -Name "<NewDatabaseName>"
```

Then type the following command to remove the old database:

```
Remove-SPStateServiceDatabase -Name "<OldDatabaseName>"
```

Where:

*<NewDatabaseName>* is the name of the new database that you want to create.

*<OldDatabaseName>* is the name of the old database that you want to disassociate with the State service and detach from SQL Server.

To point the State Service service application to a moved database by using PowerShell

#### To point the State Service service application to a moved database by using PowerShell

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command to dismount the database:

```
Dismount-SPStateServiceDatabase -Identity <DatabaseID>
```

Where  *<DatabaseID>* is the State Service database to remove from the service application. The type must be a valid GUID in the form 12345678-90ab-cdef-1234-567890bcdefgh, a valid name of a state database, or an instance of a valid **SPStateServiceDatabase** object.

For more information, see Dismount-SPStateServiceDatabase.

Move the database. For details, see Move a database by using SQL Server Management Studio and File Explorer.

At the PowerShell command prompt, type the following command to mount the renamed or moved database:

```
Mount-SPStateServiceDatabase -Name "<DatabaseName>" -DatabaseServer "<ServerName>"
```

Where:

*<DatabaseName>* is the name of the database to associate with the State service.

*<ServerName>* is the name of the SQL Server that hosts the State service database.

To point the Usage and Health data collection service application to a moved database by using PowerShell

#### To point the Usage and Health data collection service application to a moved database by using PowerShell

Use an account with these memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Note

For additional information about Microsoft PowerShell permissions, see Permissions.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Set-SPUsageApplication -Identity "<ServiceApplicationName>" -DatabaseName "<DbName>" -DatabaseServer "<SQLServerName>"
```

Where:

*<ServiceApplicationName>* is the name of the usage and health data collection service application.

*<DatabaseName>* is the name of the database.

*<SQLServerName>* is the name of the database server.

To point the Word Automation service application to a renamed or moved database by using PowerShell

#### To point the Word Automation service application to a renamed or moved database by using PowerShell

Use an account with these memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Note

For additional information about Microsoft PowerShell permissions, see Permissions.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
$app = Get-SPServiceApplication -Name "<ServiceApplicationName>"
Set-SPWordConversionServiceApplication -Identity $app -DatabaseName "<DatabaseName>" -DatabaseServer "<DatabaseServer>"
```

Where:

*<ServiceApplicationName>* is the name of the Word Automation service application.

*<DatabaseName>* is the name of the renamed or moved database.

*<DatabaseServer>* is the location of the renamed or moved database. Do not include this parameter if you are pointing to a renamed database in the same location.

To point the Subscription Settings Services service application to a moved database by using PowerShell

#### To point the Subscription Settings Services service application to a moved database by using PowerShell

Use an account with these memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Note

For additional information about Microsoft PowerShell permissions, see Permissions.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Set-SPSubscriptionSettingsServiceApplication -Identity "<ServiceApplicationName>" -DatabaseName "<DatabaseName>" -DatabaseServer "<DatabaseServer>"
```

Where:

*<ServiceApplicationName>* is the name of the Subscription Settings service application.

*<DatabaseName>* is the name of the renamed database.

*<DatabaseServer>* is the name of the renamed database.

Step 6: To start the service application by using Central Administration

#### Step 6: To start the service application by using Central Administration

Use an account that is a member of the Farm Administrators SharePoint group.

In Central Administration click **System Settings**.

On the System Settings page, in the **Servers** section, click **Manage services on server**.

Find the service application that you want and click **Start** in the **Action** column for the service, and then click **OK**.

Steps to move or rename the Business Data Connectivity Service and User Profile Service application databases

## Steps to move or rename the Business Data Connectivity Service and User Profile Service application databases

When moving or renaming the Business Data Connectivity service application and User Profile service application databases requires extra steps. The extra steps required for both service application databases is that after you move or rename the databases we recommend that you delete the service application and then re-create it.

The following procedures show how to move or delete the Business Data Connectivity service application.

To stop the Business Data Connectivity service application

### To stop the Business Data Connectivity service application

Use an account that is a member of the Farm Administrators SharePoint group.

In Central Administration click **System Settings**.

On the System Settings page, in the **Servers** section, click **Manage services on server**.

Find the service application that you want to stop, click **Stop** or **Disable** in the **Action** column for the service, and then click **OK**.

To stop a service by using PowerShell

### To stop a service by using PowerShell

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
Stop-SPServiceInstance -Identity <ServiceGUID>
```

Where  *<ServiceGUID>* is the GUID of the service. If you don't know the service GUID, you can retrieve a list of all services in the farm together with their GUIDs by using the **Get-SPServiceInstance** cmdlet.

For more information, see Stop-SPServiceInstance and Get-SPServiceInstance.

Step 2: To detach a database from SQL Server

### Step 2: To detach a database from SQL Server

Use an account that has the **db_owner** fixed database role for all of the databases that you're moving.

In SQL Server Management Studio, connect to the source SQL Server instance, and then expand the **Databases** node.

Right-click the database, point to **Tasks**, and then click **Detach**. Repeat this step for each database that you want to move.

Step 3: To move the database files to a new location by using File Explorer or Windows Explorer

### Step 3: To move the database files to a new location by using File Explorer or Windows Explorer

Use an account that has read permission on the source location and write permission on the target location.

In File Explorer, find the .mdf, .ndf, and .ldf files for the service application databases and select the ones you want to move. The database files are typically found here,  `C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLServer\MSSQL\Data`

Either copy or move the database files to the new location.

Step 4: To attach a database to a new instance of SQL Server

### Step 4: To attach a database to a new instance of SQL Server

Use an account that has the **db_owner** fixed database role for all of the databases that you're moving.

In SQL Server Management Studio, open the destination SQL Server instance.

Right-click the **Databases** node, point to **Tasks**, and then click **Attach**.

In the **Attach Database** dialog, browse to where you moved the .mdf, .ndf, and .ldf files, select the .mdf file for the database that you want to attach, and then click **OK**. Repeat this step for each database that you're moving.

Point the Business Data Connectivity service application to a moved database

### Point the Business Data Connectivity service application to a moved database

The method for pointing a service application to a moved database that works for most service applications is to delete the service application and then re-create the service application. When you re-create the service application, use the new name or new location.

To document service application settings

### To document service application settings

Before you delete and re-create a service application, document the settings for the service application. To do this, use the recommended PowerShell cmdlets that are described in the article Document farm configuration settings in SharePoint Server.

To delete the service application by using Central Administration

### To delete the service application by using Central Administration

Use an account that is a member of the Farm Administrators SharePoint group.

In Central Administration, click **Application Management**, and then, click **Manage service applications**.

On the **Service Applications** page, place your cursor next to Business Data Connectivity service and then click the empty row.

The ribbon becomes active.

On the ribbon, click **Delete**.

In the Delete Service Application dialog, select the check box next to **Delete data associated with the Service Applications** if you want to delete the service application database. If you want to retain the database, leave this check box cleared.

Click **OK** to delete the service application, or click **Cancel** to stop the operation.

To create the service application

### To create the service application

To create a Business Data Connectivity service application, follow the procedure in Configure a Business Data Connectivity service application in SharePoint Server.

To start the service application

### To start the service application

- To start a service application, see Start or stop a service in SharePoint Server.

Steps to move or rename the Search Service application databases in SharePoint Server 2013 and SharePoint Server 2016

## Steps to move or rename the Search Service application databases in SharePoint Server 2013 and SharePoint Server 2016

To move the Search service application databases, you must use SQL Server, SQL Server Management Studio, and Windows Explorer. To point to the moved databases, you must use PowerShell. Complete the following steps in the listed order.

**Important:**

The account, or accounts, that you use to do the operations must have these memberships and permissions:

Member of the Farm Administrators SharePoint group.

Member of the Administrators group on the local server.

Read permission on the source location and write permission on the target location.

**db_owner** fixed database role for all of the databases that you are moving.

**db_creator** and **securityadmin** roles for all of the databases that you are moving.

The Search Service account must have the following roles:

**db_owner** fixed database role on the Administration, Link, and Crawl databases.

**SPSearchDBAdmin** database role on the Analytics Reporting database.

In some environments, you must coordinate the rename and move procedures with the database administrator. Be sure to follow applicable policies and guidelines for managing databases.

To pause the Search service application by using PowerShell

### To pause the Search service application by using PowerShell

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
$ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplicationName>
Suspend-SPEnterpriseSearchServiceApplication -Identity $ssa
```

Where  *<SearchServiceApplicationName>* is the name of the Search service application associated with the database move.

To change the read-only mode for Search service application databases

### To change the read-only mode for Search service application databases

Use an account that is a member of the **db_owner** fixed database role for the content database.

Open SQL Server Management Studio and connect to the database server.

In Object Explorer, expand **Databases**.

Set the following databases to read-only mode:

Search Administration

Analytics Reporting

Crawl

Link

Right-click the database that you want to set to read/write or read-only, and then click **Properties**.

In the **Database Properties** dialog, on the **Options** properties page, in the **State** section, select **True** or **False** in the list next to Database Read-Only, and then click **OK**.

Click **Yes**.

To back up the Search service application databases

### To back up the Search service application databases

Use an account that is a member of the SQL Server **db_backupoperator** fixed database role on the database server where each database is stored.

Start SQL Server Management Studio and connect to the database server where the Search service application databases are stored.

In Object Explorer, expand **Databases**.

Right-click the database that you want to back up, point to **Tasks**, and then click **Back Up**.

In the **Back Up Database** dialog, in the **Source** area, select the kind of backup that you want to perform from the **Backup type** list.

For more information about the type of backup to use, see Recovery Models (SQL Server).

In the **Backup component** area, click **Database**.

Either use the default name or specify a name for the backup set in the **Name** box.

Specify the expiration date for the backup set.

This date determines when the backup set can be overwritten by subsequent backups that have the same name. By default, the backup set is set to never expire (0 days).

In the **Destination** area, specify where you want to store the backup.

Click **OK** to back up the database.

Repeat steps 1-10 for the following databases:

Search Administration

Analytics Reporting

Crawl

Link

To set the value of max degree of parallelism to 1 in the new server that hosts SQL Server

### To set the value of max degree of parallelism to 1 in the new server that hosts SQL Server

Start SQL Server Management Studio and connect to the new server that hosts SQL Server where you'll move the Search service application databases.

In **Object Explorer**, right-click the database server and then click **Properties**.

Click **Advanced**.

In the **Max Degree of Parallelism** box, select **1** to limit the number of processors to use in parallel plan execution.

For more information, see Configure the max degree of parallelism Server Configuration Option.

To restore the Search service application databases to a new database server

### To restore the Search service application databases to a new database server

Use an account that is a member of the SQL Server **sysadmin** fixed server role on the database server where each database is stored.

Start SQL Server Management Studio and connect to the database server.

In **Object Explorer**, expand **Databases**.

Right-click the database that you want to restore, point to **Tasks**, point to **Restore**, and then click **Database**.

In the **Restore Database** dialog, on the **General** page, select the database to restore to from the **To database** list.

Select the restore source from the **From database** list.

In the **Select the backup sets to restore section** area, select the check box next to the database.

On the **Options** tab, select the recovery state from the **Recover state** section.

For more information about which recovery type to use, see Recovery Models (SQL Server) in SQL Server Books Online.

Click **OK** to restore the database.

Repeat steps 1-9 for each database that is associated with the service application.

To set the Search service application databases to read/write

### To set the Search service application databases to read/write

- Follow the steps in To change the read-only mode for Search service application databases.

To point the Search service application to moved databases by using PowerShell

### To point the Search service application to moved databases by using PowerShell

Start the SharePoint Management Shell.

Point the Search Service Application database to the new location. At the PowerShell command prompt, type the following commands:

```
$ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplicationName>
$ssa | Set-SPEnterpriseSearchServiceApplication [-DatabaseName "<NewDbName>"] -DatabaseServer "<NewServerName>"
```

Where:

*<NewDbName>* is the name of the database.

*<NewServerName>* is the new database location.

Point the Analytics Reporting database to the new location. At the PowerShell command prompt, type the following commands:

```
Add-SPServerScaleOutDatabase -ServiceApplication $ssa -DatabaseServer <OriginalServerName> [-DatabaseName <NewDbName>]
$temp = Get-SPServerScaleOutDatabase -ServiceApplication $ssa
Remove-SPServerScaleOutDatabase -Database $temp[0] -ServiceApplication $ssa
```

Where:

- *<OriginalServerName>* is the name of the original SQL server.

Point the CrawlStore database to the new location. At the PowerShell command prompt, type the following commands:

```
$CrawlDatabase0 = ([array]($ssa | Get-SPEnterpriseSearchCrawlDatabase))[0]
$CrawlDatabase0 | Set-SPEnterpriseSearchCrawlDatabase [-DatabaseName "<NewDbName>"] -DatabaseServer "<NewServerName>"
```

Point the LinkStore database to the new location. At the PowerShell command prompt, type the following commands:

```
$LinksDatabase0 = ([array]($ssa | Get-SPEnterpriseSearchLinksDatabase))[0]
$LinksDatabase0 | Set-SPEnterpriseSearchLinksDatabase [-DatabaseName "<NewDbName>"] -DatabaseServer "<NewServerName>"
```

Set all Search service instances to Online. Run the following commands for each search service in the farm, until the Search service instance is reported as Online. At the PowerShell command prompt, type the following commands:

```
Get-SPEnterpriseSearchServiceInstance -Identity <Search Server> Do {write-host -NoNewline .;Sleep 10; $searchInstance = Get-SPEnterpriseSearchServiceInstance -Identity <Search Server>} while ($searchInstance.Status -ne "Online")
```

Where  *<Search Server>* is the name of the server that hosts the search components.

Resume the Search service application. At the PowerShell command prompt, type the following commands:

```
$ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplicationName>
Resume-SPEnterpriseSearchServiceApplication -Identity $ssa
```

Where  *<SearchServiceApplicationName>* is the name of the Search service application associated with the database move.

Restart each server that hosts a search component.

Steps to move or rename the Search Service application databases in SharePoint Server 2019

## Steps to move or rename the Search Service application databases in SharePoint Server 2019

To move the Search service application databases, you must use SQL Server, SQL Server Management Studio, and Windows Explorer. To point to the moved databases, you must use PowerShell. Complete the following steps in the listed order.

**Important:**

The account, or accounts, that you use to do the operations must have these memberships and permissions:

Member of the Farm Administrators SharePoint group.

Member of the Administrators group on the local server.

Read permission on the source location and write permission on the target location.

**db_owner** fixed database role for all of the databases that you are moving.

**db_creator** and **securityadmin** roles for all of the databases that you are moving.

The Search Service account must have the following roles:

**db_owner** fixed database role on the Administration, Link, and Crawl databases.

**SPSearchDBAdmin** database role on the Analytics Reporting database.

In some environments, you must coordinate the rename and move procedures with the database administrator. Be sure to follow applicable policies and guidelines for managing databases.

To pause the Search service application by using PowerShell

### To pause the Search service application by using PowerShell

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
$ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplicationName>
Suspend-SPEnterpriseSearchServiceApplication -Identity $ssa
```

Where  *<SearchServiceApplicationName>* is the name of the Search service application associated with the database move.

To change the read-only mode for Search service application databases

### To change the read-only mode for Search service application databases

Use an account that is a member of the **db_owner** fixed database role for the content database.

Open SQL Server Management Studio and connect to the database server.

In Object Explorer, expand **Databases**.

Set the following databases to read-only mode:

Search Administration

Analytics Reporting

Crawl

Link

Right-click the database that you want to set to read/write or read-only, and then click **Properties**.

In the **Database Properties** dialog, on the **Options** properties page, in the **State** section, select **True** or **False** in the list next to Database Read-Only, and then click **OK**.

Click **Yes**.

To back up the Search service application databases

### To back up the Search service application databases

Use an account that is a member of the SQL Server **db_backupoperator** fixed database role on the database server where each database is stored.

Start SQL Server Management Studio and connect to the database server where the Search service application databases are stored.

In Object Explorer, expand **Databases**.

Right-click the database that you want to back up, point to **Tasks**, and then click **Back Up**.

In the **Back Up Database** dialog, in the **Source** area, select the kind of backup that you want to perform from the **Backup type** list.

For more information about the type of backup to use, see Recovery Models (SQL Server).

In the **Backup component** area, click **Database**.

Either use the default name or specify a name for the backup set in the **Name** box.

Specify the expiration date for the backup set.

This date determines when the backup set can be overwritten by subsequent backups that have the same name. By default, the backup set is set to never expire (0 days).

In the **Destination** area, specify where you want to store the backup.

Click **OK** to back up the database.

Repeat steps 1-10 for the following databases:

Search Administration

Analytics Reporting

Crawl

Link

To set the value of max degree of parallelism to 1 in the new server that hosts SQL Server

### To set the value of max degree of parallelism to 1 in the new server that hosts SQL Server

Start SQL Server Management Studio and connect to the new server that hosts SQL Server where you'll move the Search service application databases.

In **Object Explorer**, right-click the database server and then click **Properties**.

Click **Advanced**.

In the **Max Degree of Parallelism** box, select **1** to limit the number of processors to use in parallel plan execution.

For more information, see Configure the max degree of parallelism Server Configuration Option.

To restore the Search service application databases to a new database server

### To restore the Search service application databases to a new database server

Use an account that is a member of the SQL Server **sysadmin** fixed server role on the database server where each database is stored.

Start SQL Server Management Studio and connect to the database server.

In **Object Explorer**, expand **Databases**.

Right-click the database that you want to restore, point to **Tasks**, point to **Restore**, and then click **Database**.

In the **Restore Database** dialog, on the **General** page, select the database to restore to from the **To database** list.

Select the restore source from the **From database** list.

In the **Select the backup sets to restore section** area, select the check box next to the database.

On the **Options** tab, select the recovery state from the **Recover state** section.

For more information about which recovery type to use, see Recovery Models (SQL Server) in SQL Server Books Online.

Click **OK** to restore the database.

Repeat steps 1-9 for each database that is associated with the service application.

To set the Search service application databases to read/write

### To set the Search service application databases to read/write

- Follow the steps in To change the read-only mode for Search service application databases.

To point the Search service application to moved databases by using PowerShell

### To point the Search service application to moved databases by using PowerShell

Start the SharePoint Management Shell.

Note

These instructions assume you will use the same PowerShell session for all commands.

At the PowerShell command prompt, type the following command to associate the Search Administration database with the Search service.

```
 $ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplication>
 $ssa | Set-SPEnterpriseSearchServiceApplication -DatabaseName <SearchAdministrationServiceDatabase> -DatabaseServer <SearchServiceDatabaseServer>
```

Where:

*<SearchServiceApplication>* is the name of the Search service application associated with the database.

*<SearchAdministrationServiceDatabase>* is the name of the Search service application Administration database.

*<SearchServiceDatabaseServer>* is the name of the new databse server hosting the Search service application databases.

At the PowerShell command prompt, type the following command to associate the Search Analytics database with the Search service.

```
Add-SPServerScaleOutDatabase -ServiceApplication $ssa -DatabaseServer <SearchServiceDatabaseServer> -DatabaseName <SearchServiceAnalyticsDatabase>
$temp = Get-SPServerScaleOutDatabase -ServiceApplication $ssa
Remove-SPServerScaleOutDatabase -ServiceApplication $ssa -Database $temp[0]
```

Where:

*<SearchServiceAnalyticsDatabase>* is the name of the Search service application Analytics database.

*<SearchServiceDatabaseServer>* is the name of the new databse server hosting the Search service application databases.

At the PowerShell command prompt, type the following command to associate the Search Crawl database with the Search service.

```
New-SPEnterpriseSearchCrawlDatabase -SearchApplication $ssa -DatabaseName <SearchServiceCrawlDatabase> -DatabaseServer <SearchServiceDatabaseServer>
$crawlDBToDelete = $ssa | Get-SPEnterpriseSearchCrawlDatabase -Identity "<OldCrawlStoreDatabase>"
Remove-SPEnterpriseSearchCrawlDatabase -Identity $crawlDBToDelete
```

Where:

*<SearchServiceCrawlDatabase>* is the name of the Search service application Crawl database.

*<SearchServiceDatabaseServer>* is the name of the new databse server hosting the Search service application databases.

*<OldCrawlStoreDatabase>* is the name of the old Search service application Crawl database.

At the PowerShell command prompt, type the following command to associate the Search Links database with the Search service.

```
New-SPEnterpriseSearchLinksDatabase -DatabaseName <SearchServiceLinksDatabase> -SearchApplication $ssa -DatabaseServer <SearchServiceDatabaseServer>
$oldLinksStoreDB = ([array]($ssa | Get-SPEnterpriseSearchLinksDatabase))[0]
$newLinksStoreDB = ([array]($ssa | Get-SPEnterpriseSearchLinksDatabase))[1]
Move-SPEnterpriseSearchLinksDatabases -SearchApplication $ssa -TargetStores @($newLinksStoreDB) -Confirm:$false
```

Where:

*<SearchServiceLinksDatabase>* is the name of the Search service application Links database.

*<SearchServiceDatabaseServer>* is the name of the new database server hosting the Search service application databases.

At the PowerShell command prompt, type the following command to resume the Search Service application.

```
Resume-SPEnterpriseSearchServiceApplication -Identity $ssa
```

At the PowerShell command prompt, type the following command to remove the old Search Links database from the Search service.

```
Remove-SPEnterpriseSearchLinksDatabase -Identity $oldLinksStoreDB -SearchApplication $ssa -Confirm:$false
```

Where:

- `$oldLinksStoreDB` is the variable from step 5.

See also

## See also

Concepts

#### Concepts

Move all databases in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
