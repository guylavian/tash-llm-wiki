---
title: "Install and configure RBS with a 3rd party provider for SharePoint Server - SharePoint Server"
description: "Learn how to install and configure Remote BLOB Storage (RBS) that uses a third-party RBS Provider for SharePoint Server."
ms.topic: install-set-up-deploy
---
Note

Install and configure RBS with a 3rd party provider for SharePoint Server

# Install and configure RBS with a 3rd party provider for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server uses the RBS feature to store BLOBs outside the content database. For more information about RBS, see Overview of RBS in SharePoint Server.

Important

This solution uses a third-part provider. Before continuing, make sure that you read the instructions from the manufacturer of the provider. If you want to install and configure RBS using the FILESTREAM provider, use the procedure in Install and configure RBS with FILESTREAM in a SharePoint Server farm.

Do not directly access BLOBs when you are using third-party providers. Always access these BLOBs by using SharePoint Server.

Before you begin

## Before you begin

You only have to install and configure RBS with the specific third-part provider one time for the farm. However, if you want to enable RBS using the FILESTREAM provider, use the procedure in Install and configure RBS with FILESTREAM in a SharePoint Server farm.

Before you begin this operation, review the following information about prerequisites:

The user account provisioning RBS stores must be a member of the **db_owner** fixed database role on each database that you are configuring RBS for.

The user account installing the client library must be a member of the Administrators group on all of the computers where you are installing the library.

The user account enabling RBS must have sufficient permissions to run PowerShell.

Install the RBS client library on each front-end or application server

## Install the RBS client library on each front-end or application server

You must install RBS client library on all Web servers in the SharePoint farm. The RBS client library is installed only one time per Web server, but RBS is configured separately for each associated content database. The client library consists of a client-side DLL that is linked into a user application, and also a set of stored procedures to be installed on SQL Server.

Caution

Do not install RBS by running the RBS_x64.msi file and starting the Install SQL Remote BLOB Storage wizard. The wizard sets certain default values that are not recommended for SharePoint Server.

To install the RBS client library on the on the first front-end or application server

### To install the RBS client library on the on the first front-end or application server

Confirm that the user account performing these steps is a member of the Administrators group on the computer where you are installing the library.

On any front-end or application server, for SharePoint Server 2016, download the Microsoft SQL Server 2014 Feature Pack. Run the self-extracting download package to create an installation folder for the X64 RBS.msi file.

For SharePoint 2013, download the RBS.msi file.

Copy and paste the following command into the Command Prompt window. Replace  *WSS_Content* with the database name, and replace  *DBInstanceName* with the SQL Server instance name. You should run this command by using the specific database name and SQL Server instance name only one time. The operation should finish within approximately one minute.

```
msiexec /qn /lvx* rbs_install_log.txt /i RBS-x64.msi TRUSTSERVERCERTIFICATE=true FILEGROUP=PRIMARY DBNAME="WSS_Content" DBINSTANCE="DBInstanceName
```

To install the RBS client library on all additional front-end and application servers

### To install the RBS client library on all additional front-end and application servers

Confirm that the user account performing these steps is a member of the Administrators group on the computer where you are installing the library.

On any web server, for SharePoint Server 2016, download the Microsoft SQL Server 2014 Feature Pack. Run the self-extracting download package to create an installation folder for the X64 RBS.msi file.

For SharePoint 2013, [download the RBS_amd64.msi file]((/install-and-configure-rbs).

Copy and paste the following command into the Command Prompt window. Replace  *WSS_Content* with the database name, and replace  *DBInstanceName* with the name of the SQL Server instance. The operation should finish within approximately one minute.

```
msiexec /qn /lvx* rbs_install_log.txt /i RBS_x64.msi DBNAME="WSS_Content" DBINSTANCE="DBInstanceName" ADDLOCAL=Client,Docs,Maintainer,ServerScript,FilestreamClient,FilestreamServer
```

Repeat this procedure for all Web servers in the SharePoint farm.

Run the following command on each application server in the SharePoint farm:

```
Msiexec /qn /1vx* rbs_install_log.txt /I RBS_x64.msi ADDLOCAL="Client"
```

To confirm the RBS client library installation

### To confirm the RBS client library installation

The rbs_install_log.txt log file is created in the same location as the RBS_x64.msi file. Open the rbs_install_log.txt log file by using a text editor and scroll toward the bottom of the file. Within the last 20 lines of the end of the file, an entry should read as follows: **Product: SQL Remote Blob Storage - Installation completed successfully**.

On the computer that is running SQL Server 2014 Service Pack 1 (SP1) or SQL Server 2008, verify that the RBS tables were created in the content database. Several tables should be listed under the content database that have names that are preceded by the letters "mssqlrbs".

Install the third-party provider

## Install the third-party provider

The steps that you use to install the third-part provider will vary between manufacturers. Be sure to follow the instructions from the manufacturer of the provider.

Enable RBS for each content database

## Enable RBS for each content database

You must enable RBS on one front-end server in the SharePoint farm. It is not important which front-end server that you select for this activity, as long as RBS was installed on it by using the previous procedure. You must perform this procedure one time for each content database.

Note

You can only enable RBS by using Microsoft PowerShell.

**To enable RBS by using PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command:

```
$cdb = Get-SPContentDatabase <ContentDatabaseName>
$rbss = $cdb.RemoteBlobStorageSettings
$rbss.Installed()
$rbss.Enable()
$rbss.SetActiveProviderName($rbss.GetProviderNames()[0])
$rbss
```

Where *<ContentDatabaseName>* is the name of the content database.

For more information, see Get-SPContentDatabase.

Test the RBS installation

## Test the RBS installation

You should test the RBS installation on one Web server in the SharePoint farm to make sure that that the system works correctly.

**To test the RBS data store**

On the computer that contains the RBS data store, click **Start**, and then click **Computer**.

Browse to the RBS data store directory.

Confirm that the folder is empty.

On the SharePoint farm, upload a file to a document library.

On the computer that contains the RBS data store, click **Start**, and then click **Computer**.

Browse to the RBS data store directory.

Browse to the file list and open the file that has the most recent changed date. This should be the file that you uploaded.

See also

## See also

Concepts

#### Concepts

Overview of RBS in SharePoint Server

Deciding to use RBS in SharePoint Server

Other Resources

#### Other Resources

Remote Blob Store (RBS) (SQL Server)

Enable and Configure FILESTREAM

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
