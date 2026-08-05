---
title: "Install and configure RBS with FILESTREAM in a SharePoint Server farm - SharePoint Server"
description: "Learn how to use the FILESTREAM provider to enable Remote BLOB Storage (RBS) in a SharePoint Server farm."
ms.topic: install-set-up-deploy
---
Note

Install and configure RBS with FILESTREAM in a SharePoint Server farm

# Install and configure RBS with FILESTREAM in a SharePoint Server farm

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server uses the RBS feature to store binary large objects (BLOBs) outside the content database. For more information about RBS, see Overview of RBS in SharePoint Server.

Unless otherwise specified, the information in this article is specific to RBS using the FILESTREAM provider. For guidance specific to another provider, contact the provider manufacturer.

Tip

This solution uses the FILESTREAM RBS provider that is included with SQL Server 2019, SQL Server 2017, SQL Server 2016, SQL Server 2016 SP1, SQL Server 2014, Service Pack 1 SP1, SP2, and SQL Server 2008. If you want to install and configure RBS using a different provider, use the procedure in Install and configure RBS with a 3rd party provider for SharePoint Server.

Before you begin

## Before you begin

You only have to install and configure RBS with the FILESTREAM provider one time for the farm. However, if you want to enable RBS using different providers for specific content databases, you must configure RBS to use those providers. For more information about doing that, see Install and configure RBS with a 3rd party provider for SharePoint Server.

Before you begin this operation, review the following information about prerequisites:

The user account used to perform the steps in the Provision a BLOB store for each content database section must be a member of the **db_owner** fixed database role on each database that you are configuring RBS for.

The user account installing the client library in the steps in the Install the RBS client library on SQL Server and each Front-end or Application server section must be a member of the Administrators group on all of the computers where you are installing the library.

The user account enabling RBS in the Enable RBS for each content database section must have sufficient permissions to run Microsoft PowerShell.

Enable FILESTREAM on the database server

## Enable FILESTREAM on the database server

By default, the FILESTREAM feature is installed when you install SQL Server. But it is not enabled. You must enable and configure FILESTREAM on the computer that is running SQL Server that hosts the SharePoint Server databases. You must:

Enable FILESTREAM for Transact-SQL access

Enable FILESTREAM for file I/O streaming access.

Allow remote clients to have streaming access to FILESTREAM data if you need remote client access.

To enable FILESTREAM for file I/O and to allow clients access, follow the instructions in Enable and Configure FILESTREAM. You only have to configure these settings one time for each database server where you want to use RBS.

Provision a BLOB store for each content database

## Provision a BLOB store for each content database

After you have enabled and configured FILESTREAM, provision a BLOB store on the file system as described in the following procedure. You must provision a BLOB store for each content database that you want to use RBS with.

**To provision a BLOB store**

Confirm that the user account performing these steps is a member of the **db_owner** fixed database role on each database that you are configuring RBS for.

Open **SQL Server Management Studio**.

Connect to the instance of SQL Server that hosts the content database.

Expand **Databases**.

Click the content database for which you want to create a BLOB store, and then click **New Query**.

Paste the following SQL queries in **Query** pane, and then execute them in the sequence listed. In each case, replace  *[WSS_Content]* with the content database name, and replace  *c:\BlobStore* with the volume\directory in which you want the BLOB store created. The provisioning process creates a folder in the location that you specify. Be aware that you can provision a BLOB store only one time. If you attempt to provision the same BLOB store multiple times, you'll receive an error.

Tip

For best performance, simplified troubleshooting, and as a general best practice, we recommend that you create the BLOB store on a volume that does not contain the operating system, paging files, database data, log files, or the tempdb file.

```
use [WSS_Content]
if not exists 
(select * from sys.symmetric_keys 
where name = N'##MS_DatabaseMasterKey##')
create master key encryption by password = N'Admin Key Password !2#4'
```

```
use [WSS_Content]
if not exists 
(select groupname from sysfilegroups 
where groupname=N'RBSFilestreamProvider')
alter database [WSS_Content]
add filegroup RBSFilestreamProvider contains filestream
```

```
use [WSS_Content] 
alter database [WSS_Content]
add file (name = RBSFilestreamFile, filename = 'c:\Blobstore') to filegroup RBSFilestreamProvider
```

Install the RBS client library on SQL Server and each Front-end or Application server

## Install the RBS client library on SQL Server and each Front-end or Application server

You must install RBS client library on the SQL Server node and all Front-end or Application servers in the SharePoint farm. The RBS client library is installed only one time per web server, but RBS is configured separately for each associated content database. The client library consists of a client-side dynamic link library (DLL) that is linked into a user application, and a set of stored procedures that are installed on SQL Server.

Caution

Do not install the RBS client library by running the RBS_amd64.msi (or RBS.msi) file and starting the Install SQL Remote BLOB Storage wizard. The wizard sets certain default values that are not recommended for SharePoint Server.

To install the RBS client library on the SQL Server.

### To install the RBS client library on the SQL Server.

Confirm that the user account performing these steps is a member of the Administrators group on the computer where you are installing the library.

On SQL Server node, download the correct RBS client based on the SQL Server version and SharePoint level that you use.

SharePoint Server Subscription Edition supports the FILESTREAM provider that is included in SQL Server 2019 and later versions of SQL Server.

SharePoint Server 2019 supports the FILESTREAM provider that is included in SQL Server 2016 and SQL Server 2017.

SharePoint Server 2016 supports the FILESTREAM provider that is included in SQL Server 2014 and SQL Server 2016.

SharePoint 2013 supports the FILESTREAM providers that are included in all versions of SQL Server 2008 R2, SQL Server 2012, and SQL Server 2014.

You only need to download the RSB.msi file from the Feature Pack but make sure you download the correct processor type for your server, either x86 or x64.

For SharePoint Server Subscription Edition, choose the correct install from the following list:

- Microsoft SQL Server 2019 Integration Services Feature Pack

For SharePoint Server 2019, choose the correct install from the following list:

Microsoft SQL Server 2016 SP1 Feature Pack

Microsoft SQL Server 2016 SP2 Feature Pack

Microsoft SQL Server 2016 SP3 Feature Pack

Microsoft SQL Server 2017 Feature Pack

For SharePoint Server 2016, choose the correct install from the following list:

Microsoft SQL Server 2014 Feature Pack

Microsoft SQL Server 2014 SP2 Feature Pack

Microsoft SQL Server 2016 SP1 Feature Pack

For SharePoint 2013, choose the correct install from the following list:

Microsoft SQL Server 2008 R2 SP3 Feature Pack

Microsoft SQL Server 2012 SP4 Feature Pack

Microsoft SQL Server 2014 SP2 Feature Pack

Copy and paste the following command into the Command Prompt window. Replace  *WSS_Content* with the database name, and replace  *DBInstanceName* with the SQL Server instance name. You should run this command by using the specific database name and SQL Server instance name only one time. The action should finish within approximately one minute.

```
msiexec /qn /lvx* rbs_install_log.txt /i RBS_amd64.msi TRUSTSERVERCERTIFICATE=true FILEGROUP=PRIMARY DBNAME="WSS_Content" DBINSTANCE="DBInstanceName" FILESTREAMFILEGROUP=RBSFilestreamProvider FILESTREAMSTORENAME=FilestreamProvider_1
```

To install the RBS client library on all SharePoint Front-end and Application servers

### To install the RBS client library on all SharePoint Front-end and Application servers

Confirm that the user account performing these steps is a member of the Administrators group on the computer where you are installing the library.

On any web server, download the correct RBS client based on the SQL Server version and SharePoint level that you use. Use one of the following lists to choose the correct install.

SharePoint Server Subscription Edition supports the FILESTREAM provider that is included in SQL Server 2019 and later versions of SQL Server.

SharePoint Server 2019 supports the FILESTREAM provider that is included in SQL Server 2016 and SQL Server 2017.

SharePoint Server 2016 supports the FILESTREAM provider that is included in SQL Server 2014 and SQL Server 2016.

SharePoint 2013 supports the FILESTREAM providers that are included in all versions of SQL Server 2008 R2, SQL Server 2012, and SQL Server 2014.

You only need to download the RSB.msi file from the Feature Pack but make sure you download the x64 version.

For SharePoint Server Subscription Edition, choose the correct install from the following list:

- Microsoft SQL Server 2019 Integration Services Feature Pack

For SharePoint Server 2019, choose the correct install from the following list:

Microsoft SQL Server 2016 SP1 Feature Pack

Microsoft SQL Server 2016 SP2 Feature Pack

Microsoft SQL Server 2016 SP3 Feature Pack

Microsoft SQL Server 2017 Feature Pack

For SharePoint Server 2016, choose the correct install from the following list:

Microsoft SQL Server 2014 Feature Pack

Microsoft SQL Server 2014 SP2 Feature Pack

Microsoft SQL Server 2016 SP1 Feature Pack

For SharePoint 2013, choose the correct install from the following list:

Microsoft SQL Server 2008 R2 SP3 Feature Pack

Microsoft SQL Server 2012 SP4 Feature Pack

Microsoft SQL Server 2014 SP2 Feature Pack

Copy and paste the following command into the Command Prompt window. Replace  *WSS_Content* with the database name, and replace  *DBInstanceName* with the name of the SQL Server instance. The action should finish within approximately one minute.

```
msiexec /qn /lvx* rbs_install_log.txt /i RBS_amd64.msi DBNAME="WSS_Content" DBINSTANCE="DBInstanceName" ADDLOCAL=Client,Docs,Maintainer,ServerScript,FilestreamClient,FilestreamServer
```

Note

If you attempt to install SQL Server 2012 Remote Blob Store for an additional database on the same instance of SQL Server, you will receive an error. For more information, see KB2767183.

For subsequent content databases for which you want to enable RBS, change the `msiexec` command similar to below.

```
msiexec /qn /lvx* rbs_install_log_ContentDbName.txt /i RBS_amd64.msi REMOTEBLOBENABLE=1 FILESTREAMPROVIDERENABLE=1 DBNAME="WSS_Content_2" ADDLOCAL="EnableRBS,FilestreamRunScript" DBINSTANCE="DBInstanceName"
```

Repeat this procedure for all Front-end servers and Application servers in the SharePoint farm.

Note

If you install Visio web services on SharePoint Server application servers that do not have an RBS provider installed, a Visio error occurs when you attempt to open a Visio diagram from this server. You must install an RBS client on SharePoint Server servers that run the Visio Graphics Service if you want to open Visio diagrams on that server.

To confirm the RBS client library installation

### To confirm the RBS client library installation

The rbs_install_log.txt log file is created in the same location as the RBS_amd64.msi file. Open the rbs_install_log.txt log file by using a text editor and scroll toward the bottom of the file. Within the last 20 lines of the end of the file, an entry should read as follows: **Product: SQL Remote Blob Storage - Installation completed successfully**.

On the computer that is running Service Pack 1 (SP1) or SQL Server 2008, verify that the RBS tables were created in the content database. Several tables should be listed under the content database that have names that are preceded by the letters "mssqlrbs".

Enable RBS for each content database

## Enable RBS for each content database

You must enable RBS on one web server in the SharePoint farm. It is not important which web server that you select for this activity, as long as RBS was installed on it by using the previous procedure. You must perform this procedure one time for each content database.

Note

You can only enable RBS by using Microsoft PowerShell.

**To enable RBS by using Microsoft PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Start the SharePoint Management Shell.

At the Microsoft PowerShell command prompt, type the following command:

```
$cdb = Get-SPContentDatabase <ContentDatabaseName>
$rbss = $cdb.RemoteBlobStorageSettings
$rbss.Installed()
$rbss.Enable()
$rbss.SetActiveProviderName($rbss.GetProviderNames()[0])
$rbss
```

Where  *<ContentDatabaseName>* is the name of the content database.

For more information, see Get-SPContentDatabase.

Assign db_owner permissions to the web application

## Assign db_owner permissions to the web application

Important

Make sure that the web application that accesses the RBS-enabled content database is a member of the **db_owner** fixed database role for that database.

Test the RBS installation

## Test the RBS installation

You should test the RBS installation on one Front-end server in the SharePoint farm to make sure that the system works correctly.

**To test the RBS data store**

On the computer that contains the RBS data store, click **Start**, and then click **Computer**.

Browse to the RBS data store directory.

Confirm that the folder is empty.

On the SharePoint farm, upload a file that is at least 100 kilobytes (KB) to a document library.

On the computer that contains the RBS data store, click **Start**, and then click **Computer**.

Browse to the RBS data store directory.

Browse to the file list and open the file that has the most recent changed date. This should be the file that you uploaded.

See Also

## See Also

Overview of RBS in SharePoint Server

Deciding to use RBS in SharePoint Server

Install and configure RBS with SharePoint 2013 and SQL Server 2012

Install for SharePoint 2013

Remote Blob Store (RBS) (SQL Server)

Enable and Configure FILESTREAM

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
