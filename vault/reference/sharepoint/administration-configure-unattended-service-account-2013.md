---
title: "Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2013 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-unattended-service-account-2013
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-unattended-service-account-2013
family: administration
documentKind: "how-to"
abstract: "Configure Excel Services in SharePoint Server to use the unattended service account for authentication to external data."
---

# Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2013 - SharePoint Server

Note

Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2013

# Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Excel Services in SharePoint Server 2013 provides three methods of using Secure Store Service to refresh the external data source in a workbook:

You can use an unattended service account. This article describes how to do this.

You can specify a Secure Store target application in a workbook. (This is known as an embedded connection.) For more information, see Configure Excel Services data refresh by using embedded data connections.

You can use an Office Data Connection (ODC) file that specifies a Secure Store target application. For more information, see Configure Excel Services data refresh by using external data connections.

Using the unattended service account involves configuring an Active Directory account and granting it access to your data, storing the credentials for this account in Secure Store, and configuring Excel Services to use the stored credentials when it needs to refresh the data in a workbook.

The following steps are required to configure the unattended service account in Excel Services.

Configure a data access account

Configure Excel Services Global Settings

Configure a workbook to use the unattended service account

Configure a data access account

## Configure a data access account

The unattended service account requires an Active Directory account for data access. Have your domain administrator create an Active Directory account that you can use for data access.

After the account has been created, you must grant this account read access to the data source that you will be using in your data-connected Excel workbook. Use the following procedure to create a logon for the data access account in SQL Server. (If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data-read permissions for the data access account.)

**To create a SQL Server logon for the data access account**

In SQL Server Management Studio, connect to the database engine.

In Object Explorer, expand **Security**.

Right-click **Logins**, and then click **New Login**.

In the **Login name** box, type the name of the Active Directory account that you created for data access.

In the **Select a page** section, click **User Mapping**.

Select the **Map** check box for the database that you want to provide access to, and then, in the **Database role membership for: <database>** section, select the **db_datareader** check box.

Click **OK**.

Now that you have created a logon for the data access account and granted the account access to your data source, you must create a target application in Secure Store to contain the credentials for the data access account.

Configure Excel Services Global Settings

## Configure Excel Services Global Settings

The unattended service account configuration is part of the Excel Services Global Settings. Use the following procedure to configure the unattended service account in Excel Services.

**To configure Excel Services Global Settings**

On the the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Excel Services service application.

On the Manage the Excel Services page, click **Global Settings**.

On the Excel Services Settings page, in the **External Data** section:

Select the **Create a new Unattended Service Account** option.

Type the user name and password of the account that you created for data access.

- Click **OK**.

With the Excel Services Global Settings configured, setup of the unattended service account is complete. The next section describes how to configure the Excel Services authentication settings in a data-connected Excel workbook to refresh the data with the unattended service account after the workbook has been published to a SharePoint document library.

Configure a workbook to use the unattended service account

## Configure a workbook to use the unattended service account

You must configure the Excel Services Authentication Settings in the workbook before you publish it to SharePoint Server 2013. Doing so enables the workbook to use the unattended service account to refresh data when the workbook is rendered in Excel Services. Use the following procedure to configure the authentication settings.

**To configure Excel Services authentication settings**

In a data-connected Excel workbook, on the **Data** tab, click **Connections**.

On the **Workbook Connections** dialog, select the data connection that you want to update, and then click **Properties**.

On the **Connection Properties** dialog, on the **Definition** tab, click **Authentication Settings**.

On the **Excel Services Authentication Settings** dialog, select the **None** option, and then click **OK**.

On the **Connection Properties** dialog, click **OK**.

Note

If you see a warning that the link to the external connection file will be removed, click **Yes**.

On the **Workbook Connections** dialog, click **Close**.

With the Excel Services Authentication Settings set to **None**, Excel Services uses the unattended service account to refresh the data in the workbook after you have published it to SharePoint Server 2013.

See also

## See also

Concepts

#### Concepts

Use Excel Services with Secure Store Service in SharePoint Server 2016

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
