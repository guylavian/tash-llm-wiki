---
title: "Manage Excel Services trusted data connection libraries (SharePoint Server 2013) - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-manage-excel-services-trusted-data-connection-libraries
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/manage-excel-services-trusted-data-connection-libraries
family: administration
documentKind: "how-to"
abstract: "Add, configure, or delete trusted data connection libraries in Excel Services in SharePoint Server."
---

# Manage Excel Services trusted data connection libraries (SharePoint Server 2013) - SharePoint Server

Note

Manage Excel Services trusted data connection libraries (SharePoint Server 2013)

# Manage Excel Services trusted data connection libraries (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

The steps in this article apply to SharePoint Server 2013 Enterprise.

Trusted data connection libraries are SharePoint Server 2013 data connection libraries that Excel Services has been configured to trust. Excel Services does not use data connection files that are not stored in a trusted data connection library.

To perform the procedures in this article, you must be member of the Farm Administrators group or an Administrator for the Excel Services service application that you are configuring.

Add a trusted data connection library

## Add a trusted data connection library

Use the following procedure to add a trusted data connection library.

**To add a trusted data connection library**

In the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.

On the Manage Excel Services page, click **Trusted Data Connection Libraries**.

On the Excel Services Application Trusted Data Connection Libraries page, click **Add Trusted Data Connection Library**.

On the Excel Services Application Add Trusted Data Connection Library page, in the **Location** section, type the address of the trusted data connection library in the **Address** box.

In the **Description** box, you can also type a description of the purpose for this trusted data connection library.

Click **OK**.

Configure a trusted data connection library

## Configure a trusted data connection library

Use the following procedure to configure an existing trusted data connection library.

**To configure a trusted data connection library**

In the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.

On the Manage Excel Services page, click **Trusted Data Connection Libraries**.

On the Excel Services Application Trusted Data Connection Libraries page, either click the data connection library that you want to configure or point to the data connection library, click the arrow that appears, and then click **Edit**.

Delete a trusted data connection library

## Delete a trusted data connection library

Use the following procedure to delete a trusted data connection library.

Note

Deleting a trusted data connection library does not affect the library itself or its contents. It only removes the library as a trusted data connection library in Excel Services.

**To delete a trusted data connection library**

In the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.

On the Manage Excel Services page, click **Trusted Data Connection Libraries**.

On the Excel Services Application Trusted Data Connection Libraries page, point to the data connection library that you want to delete, click the arrow that appears, and then click **Delete**.

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
