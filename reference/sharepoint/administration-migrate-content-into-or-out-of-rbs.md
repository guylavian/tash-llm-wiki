---
title: "Migrate content into or out of RBS in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-migrate-content-into-or-out-of-rbs
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/migrate-content-into-or-out-of-rbs
family: administration
documentKind: "upgrade-and-migration-article"
abstract: "Learn how to migrate content into or out of Remote BLOB Storage (RBS), or to a different RBS provider for SharePoint Server."
---

# Migrate content into or out of RBS in SharePoint Server - SharePoint Server

Note

Migrate content into or out of RBS in SharePoint Server

# Migrate content into or out of RBS in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

After installing RBS and setting a content database to use RBS, all existing content in that database can be migrated into the database's active provider. You use the same Microsoft PowerShell command to migrate content into or out of RBS, or to another RBS provider. When RBS is implemented, SQL Server itself is regarded as an RBS provider.

You can migrate content databases at any time. But we recommend that you perform migrations during low usage periods so that this activity does not cause decrease in performance for users. Migration moves all content from the specified content database into the storage mechanism of the newly named provider.

Migrate a content database

## Migrate a content database

This operation can be performed on any front-end or application server in the farm. You only have to perform the operation one time on one front-end or application server for each content database that you want to migrate.

**To migrate a content database by using Microsoft PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the commands in the following steps.

To obtain the content database RBS settings object:

```
$rbs=(Get-SPContentDatabase <ContentDbName>).RemoteBlobStorageSettings
```

Where  *<ContentDbName>* is the name of the content database.

- To view a list the RBS providers installed on the Web server:

```
$rbs.GetProviderNames()
```

- To set the active RBS provider:

```
$rbs.SetActiveProviderName(<NewProvider>)
```

Where  *<NewProvider>* is the name of the provider that you want to make active for this content database. If you want to migrate the content database out of RBS completely and back into SQL Server inline storage, set this value to  `()`.

- Migrate the data from RBS to the new provider or to SQL Server:

```
$rbs.Migrate()
```

See also

## See also

Concepts

#### Concepts

Set a content database to use RBS with FILESTREAM in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
