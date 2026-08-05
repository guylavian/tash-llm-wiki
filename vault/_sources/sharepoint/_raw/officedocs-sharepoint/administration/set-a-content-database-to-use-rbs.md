---
title: "Set a content database to use RBS with FILESTREAM in SharePoint Server - SharePoint Server"
description: "Learn how to set a SharePoint Server content database to use Remote BLOB Storage (RBS) with FILESTREAM."
ms.topic: how-to
---
Note

Set a content database to use RBS with FILESTREAM in SharePoint Server

# Set a content database to use RBS with FILESTREAM in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article describes how to set a content database to use Remote BLOB Storage (RBS) that uses the FILESTREAM provider. If you are using a third-party provider, these instructions might not apply. For more information, contact the manufacturer of the provider. These instructions assume that you have already installed RBS for use with SharePoint Server. To install and configure RBS, see Install and configure RBS with FILESTREAM in a SharePoint Server farm.

Before you begin

## Before you begin

You must perform this procedure on every content database that you want to set to use RBS.

Before you begin this operation, review the following information about prerequisites:

The user account that you use to perform this procedure is a member of the Administrators group on the Web.

The user account that you use to perform this procedure is a member of the SQL Server **dbcreator** and **securityadmin** fixed server roles on the computer that is running SQL Server 2014 Service Pack 1 (SP1), SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, or SQL Server 2014.

Set a content database to use RBS

## Set a content database to use RBS

To set a content database to use RBS, you must provision a binary large object (BLOB) store in SQL Server, add the content database information to the RBS configuration on a front-end or application server, and then test the RBS data store.

These instructions assume that you have installed SQL Server Management Studio on the database server. You can perform the following procedures on any front-end or application server in the farm.

Note

These instructions assume that you are using the FILESTREAM RBS provider. If you are using a different RBS provider, refer to that provider's instructions to perform these operations.

To set a content database to use RBS

### To set a content database to use RBS

Verify that the user account that you use to perform this procedure is a member of the Administrators group on the Web server, and is a member of the SQL Server **dbcreator** and **securityadmin** fixed server roles on the computer that is running SQL Server 2014 SP1, SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, or SQL Server 2014.

Open SQL Server Management Studio.

In the **Connect to Server** dialog, specify the server type, server name, and authentication method of the database server that you want to connect to, and then click **Connect**.

Expand **Databases**.

Right-click the content database for which you want to create a BLOB store, and then click **New Query**.

In the **Query** pane, copy and execute the following SQL queries in the sequence that is provided.

```
use [ContentDbName]
if not exists (select * from sys.symmetric_keys where name = N'##MS_DatabaseMasterKey##')
create master key encryption by password = N'Admin Key Password !2#4'
```

```
use [ContentDbName]
if not exists (select groupname from sysfilegroups where groupname=N'RBSFilestreamProvider')
alter database [ContentDbName] add filegroup RBSFilestreamProvider contains filestream
```

```
use [ContentDbName]
alter database [ContentDbName] add file (name = RBSFilestreamFile, filename = 'c:\RBSStore') to filegroup RBSFilestreamProvider
```

Where  *[ContentDbName]* is the content database name and  *c:\RBSStore* is the volume\directory that will contain the RBS data store. Be aware that you can provision a RBS store only one time. If you attempt to provision the same RBS data store multiple times, you will receive an error.

Tip

For best performance, simplified troubleshooting, and as a general best practice, we recommend that you create the RBS data store on a volume that does not contain the operating system, paging files, database data, log files, or the tempdb file.

Right-click **Start**, click **Run**, type cmd into the **Run** text box, and then click **OK**.

Copy and paste the following command at the command prompt:

```
msiexec /qn /i rbs.msi REMOTEBLOBENABLE=1 FILESTREAMPROVIDERENABLE=1 DBNAME=<ContentDbName> FILESTREAMSTORENAME=FilestreamProvider_1 ADDLOCAL=EnableRBS,FilestreamRunScript DBINSTANCE=<DBInstanceName>>
```

Where  *<ContentDbName>* is the name of the content database, and  *<DBInstanceName>* is the name of the SQL Server. The operation should finish within approximately one minute.

To test the RBS data store

### To test the RBS data store

Connect to a document library on any front-end or application server.

Upload a file that is at least 100 kilobytes (KB) to the document library.

On the computer that contains the RBS data store, click **Start**, and then click **Computer**.

Navigate to the RBS data store directory.

Locate the folder that has the most recent modification date, other than the $FSLOG folder. Open this folder and locate the file that has the most recent modification date. Verify that this file has the same size and contents as the file that you uploaded. If does not, make sure that RBS is installed and enabled correctly.

See also

## See also

Concepts

#### Concepts

Overview of RBS in SharePoint Server

Migrate content into or out of RBS in SharePoint Server

Other Resources

#### Other Resources

Install and configure RBS with SharePoint 2013 and SQL Server 2012

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
