---
title: "Back up databases to snapshots in SharePoint Server - SharePoint Server"
description: "Learn how to back up databases to snapshots in SharePoint Server by using SQL Server Enterprise."
ms.topic: how-to
---
Note

Back up databases to snapshots in SharePoint Server

# Back up databases to snapshots in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can only back up databases to snapshots in SharePoint Server by using SQL Server Enterprise tools.

Before you begin

## Before you begin

We recommend that you regularly back up the complete farm. Regularly backing up the farm reduces data losses that might occur from hardware failures, power outages, or other problems. It is a simple process and helps make sure that all the farm data and configurations are available for recovery, if that is required. For more information, see Back up farms in SharePoint Server. However, IT requirements might require you to backup databases to snapshots. Although you can back up any farm database to a snapshot, you typically back up content databases.

Important

Database snapshots do not replace a backup and restore strategy. To fully protect your SharePoint Server environment we advise you to perform regular backups to protect your farm in case you need to restore data after a failure..

Before you begin this operation, review the following information:

You must first create a folder on the database server for your backup files. If you want to store the snapshots at another location, you can move the backup files to a backup folder on the network after the operation is completed.

A database snapshot provides a read-only, static view of a source database as it existed at snapshot creation, minus any uncommitted transactions. Uncommitted transactions are rolled back in a newly created database snapshot because the Database Engine runs recovery after the snapshot was created (transactions in the database are not affected). For more information about database snapshots, see Database Snapshots (SQL Server).

Use SQL Server tools to back up a database to a snapshot in SharePoint Server

## Use SQL Server tools to back up a database to a snapshot in SharePoint Server

If you want to back up databases to snapshots, you must use SQL Server tools. The databases that are associated with the farm are determined by the service applications and features that you have installed on the farm.

**To back up a database to a snapshot by using SQL Server tools**

Verify that the user account that is performing this procedure is a member of the SQL Server **db_owner** fixed database role.

Open SQL Server Management Studio and connect to the database server.

In Object Explorer, expand **Databases**.

Select the database that you want to back up, and then click **New Query**.

Copy the following text, and then paste it to the query pane.

```
CREATE DATABASE <snapshot name>
ON
(
NAME=<logical name of the database file>,
FILENAME = 'c:\WSS_Backup1.ss')
AS SNAPSHOT OF <database name>;
```

See also

## See also

Other Resources

#### Other Resources

Database Snapshots (SQL Server)

Database Snapshots with Always On Availability Groups (SQL Server)

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
