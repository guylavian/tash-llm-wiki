---
title: "Manage Excel Services trusted data providers (SharePoint Server 2013) - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-manage-excel-services-trusted-data-providers
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/manage-excel-services-trusted-data-providers
family: administration
documentKind: "how-to"
abstract: "Add, configure, or delete Excel Services trusted data providers in SharePoint Server."
---

# Manage Excel Services trusted data providers (SharePoint Server 2013) - SharePoint Server

Note

Manage Excel Services trusted data providers (SharePoint Server 2013)

# Manage Excel Services trusted data providers (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

The steps in this article apply to SharePoint Server 2013 Enterprise.

Trusted data providers are data providers from which Excel Services accesses data. A data provider is a database type combined with a protocol for accessing data (for example, SQL Server combined with ODBC).

Excel Services does not access data that does not come from a trusted data provider.

Excel Services contains entries for common data providers. Add additional data providers as needed.

Add a trusted data provider

## Add a trusted data provider

Use the following procedure to add a trusted data provider in Excel Services.

**To add a trusted data provider**

In the Central Administration page, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.

On the Manage Excel Services page, click **Trusted Data Providers**.

On the Excel Services Application Trusted Data Providers page, click **Add Trusted Data Provider**.

On the Excel Services Application Add Trusted Data Provider page, in the **Provider** section, type the provider ID of the trusted data provider in the **Provider ID** box (for example, type SQL Server). Look in a valid connection string to find the provider ID.

Under **Provider Type**, select one of the following:

**OLE DB** Select this option to access data by using Object Linking and Embedding (OLE).

**ODBC** Select this option to access data by using Open Database Connectivity (ODBC).

**ODBC DSN** Select this option to access data by using Open Database Connectivity with Data Source Name (ODBC DSN).

In the **Description** box, you can also type a description of the purpose for this trusted data provider.

Click **OK**.

Configure a trusted data provider

## Configure a trusted data provider

Use the following procedure to configure a trusted data provider in Excel Services.

**To configure a trusted data provider**

In the Central Administration page, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.

On the Manage Excel Services page, click **Trusted Data Providers**.

On the Excel Services Application Trusted Data Providers page, click **Edit** on the menu of the data provider that you want to configure.

Delete a trusted data provider

## Delete a trusted data provider

Use the following procedure to delete a trusted data provider from Excel Services.

**To delete a trusted data provider**

In the Central Administration page, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.

On the Manage Excel Services page, click **Trusted Data Providers**.

On the Excel Services Application Trusted Data Providers page, click **Delete** on the menu of the data provider that you want to delete.

Click **OK** in the message box that asks whether you want to continue with the deletion.

See also

## See also

Other Resources

#### Other Resources

Configure Excel Services in SharePoint

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
