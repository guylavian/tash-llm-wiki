---
title: "Manage Excel Services data model settings (SharePoint Server 2013) - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-manage-excel-services-data-model-settings
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/manage-excel-services-data-model-settings
family: administration
documentKind: "how-to"
abstract: "Configure instances of SQL Server 2012 Analysis Services for Data Model functionality in Excel Services."
---

# Manage Excel Services data model settings (SharePoint Server 2013) - SharePoint Server

Note

Manage Excel Services data model settings (SharePoint Server 2013)

# Manage Excel Services data model settings (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

The steps in this article apply to SharePoint Server 2013 Enterprise.

Excel Services can use instances of SQL Server 2012 SP1 Analysis Services (SSAS) perform advanced data analysis calculations. This article describes how to register, edit, and unregister instances of SQL Server 2012 Analysis Services for use by Excel Services in performing these calculations.

Before you begin this operation, review the following information about prerequisites:

To perform these procedures, you must be member of the Farm Administrators group or an Administrator for the Excel Services service application that you are configuring.

The instance of SQL Server 2012 Analysis Services that you plan to use must be installed in SQL Server PowerPivot for SharePoint mode.

Register an Analysis Services server

## Register an Analysis Services server

Use the following procedure to register an instance of SQL Server 2012 SP1 Analysis Services (SSAS) with Excel Services.

**To register an Analysis Services server**

On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Excel Services service application that you want to manage.

On the Manage Excel Services page, click **Data Model**.

Click **Add Server**.

In the **Server Name** box, type the name of the instance of SQL Server 2012 SP1 Analysis Services (SSAS) that you want to add.

Optionally, in the **Description** box, type a description for the server.

Click **OK**.

Edit Analysis Services server details

## Edit Analysis Services server details

Use the following procedure to edit the server name or description for an instance of SQL Server 2012 SP1 Analysis Services (SSAS) that has been registered with Excel Services.

**To edit Analysis Services server details**

On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Excel Services service application that you want to manage.

On the Manage Excel Services page, click **Data Model**.

Hover over the server that you want to edit, click the arrow that appears, and then click **Edit**.

Update the **Server Name** and **Description** as needed, and then click **OK**.

Unregister an Analysis Services server

## Unregister an Analysis Services server

Use the following procedure to remove an instance of SQL Server 2012 SP1 Analysis Services (SSAS) from Excel Services.

**To unregister an Analysis Services server**

On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Excel Services service application that you want to manage.

On the Manage Excel Services page, click **Data Model**.

Hover over the server that you want to edit, click the arrow that appears, and then click **Delete**.

Click **OK** on the delete confirmation dialog.

See also

## See also

Other Resources

#### Other Resources

Configure Excel Services in SharePoint

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
