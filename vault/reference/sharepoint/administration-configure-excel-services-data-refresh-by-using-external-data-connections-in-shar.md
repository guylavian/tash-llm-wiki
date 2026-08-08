---
title: "Configure Excel Services data refresh by using external data connections in SharePoint Server 2013 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-excel-services-data-refresh-by-using-external-data-connections-in-shar
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-excel-services-data-refresh-by-using-external-data-connections-in-shar
family: administration
documentKind: "how-to"
abstract: "Configure Excel Services in SharePoint Server data refresh by using Secure Store and an external Office Data Connection (ODC) file."
---

# Configure Excel Services data refresh by using external data connections in SharePoint Server 2013 - SharePoint Server

Note

Configure Excel Services data refresh by using external data connections in SharePoint Server 2013

# Configure Excel Services data refresh by using external data connections in SharePoint Server 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Excel Services in SharePoint Server 2013 provides three methods of using Secure Store Service to refresh the external data source in a workbook:

You can use an unattended service account. For more information, see Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2013.

You can specify a Secure Store target application in a workbook. (This is known as an embedded connection.) For more information, see Configure Excel Services data refresh by using embedded data connections.

You can use an Office Data Connection (ODC) file that specifies a Secure Store target application. This article describes how to do this.

By using an ODC file for your data connection, you separate your Excel workbooks from the data connection information. This allows you to share a single ODC file among multiple workbooks and also allows you to centrally manage your data connections.

Using Excel Services with an ODC file consists of the following steps:

Configure a data access account

Create a Secure Store target application

Create and publish an ODC file

Configure an Excel workbook to use the published ODC file as a data connection

Configure a data access account

## Configure a data access account

You must have an account that can be granted access to the data source to which you want to connect your Excel workbook. This can be an Active Directory account, a SQL Server logon, or other set of credentials as required by your data source. This account will be stored in Secure Store.

After you have created the account, the next step is to grant that account read access to the required data. (in this article, we use the example of accessing a SQL Server database through an Active Directory account. If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data read permissions for the data access account.)

Follow these steps to create a SQL Server logon and grant Read access to the database.

**To create a SQL Server logon for the data access account**

In SQL Server Management Studio, connect to the database engine.

In Object Explorer, expand **Security**.

Right-click **Logins**, and then click **New Login**.

In the **Login name** box, type the name of the Active Directory account that you created for data access.

In the **Select a page** section, click **User Mapping**.

Select the **Map** check box for the database that you want to provide access to, and then, in the **Database role membership for: <database>** section, select the **db_datareader** check box.

Click **OK**.

Now that you have created a data access account and granted it access to a data source, the next step is to create a Secure Store target application.

Create a Secure Store target application

## Create a Secure Store target application

You must create a target application in Secure Store that contains the credentials that you created for data access. This target application can then be specified in an ODC file and will be used by Excel Services when it refreshes data in the workbook.

When you create the target application, you have to specify which users will be authorized to use the credentials stored in Secure Store. You can list users individually, or you can use an Active Directory group. We recommend that you use an Active Directory group for ease of administration.

Note

The users that you list in the target application do not have direct access to the stored credentials. Instead, Excel Services uses the credentials on their behalf to refresh data in data-connected workbooks that specify this target application.

Use the following procedure to create a Secure Store target application.

**To create a target application**

On the the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.

Click the Secure Store Service service application.

On the ribbon, click **New**.

In the **Target Application ID** box, type a unique identifier for this target application (for example, ExcelServicesDataAccess).

In the **Display Name** box, type a friendly name or short description.

In the **Contact E-mail** box, type the email address for a contact for this target application.

In the **Target Application Type** drop-down list, select **Group**.

Click **Next**.

On the Credential Fields page, if you are using Windows credentials, leave the default credential fields. If you are using credentials other than Windows credentials, modify the **Field Type** drop-down list to comply with the credentials that you are using. Click **Next**.

On the Specify the membership settings page:

In the **Target Application Administrators** box, type the account of the user who will administer this target application.

Note

You can specify multiple users or an Active Directory group.

In the **Members** box, type the users to whom you want to grant the ability to refresh data.

Note

You can specify multiple users or an Active Directory group.

- Click **OK**.

Use the following procedure to set the credentials for the target application.

**To set the credentials for the target application**

On the Secure Store Service Application page, in the **Target Application ID** column, point to the target application that you just created, click the arrow that appears, and then click **Set Credentials**.

Type the user name and password of the data access account.

Click **OK**.

Once you have set the credentials for the target application, the target application is ready to use. The next step is to create an ODC file that specifies this target application for Excel Services data refresh.

Create and publish an ODC file

## Create and publish an ODC file

Now that the Secure Store target application is configured, the next step is to create the ODC file and publish it to a trusted data connection library. Use the following procedure to create an ODC file that specifies the target application that you just created.

Note

The following procedures use Excel 2016. The procedures for Excel 2010 are similar.

**To create and publish an ODC file**

In Excel, on the **Data** tab, in the **Get External Data** section, click **From Other Sources**, and then select your data source.

Complete the wizard to create a data connection to your data source.

On the **Data** tab, click **Connections**.

On the **Workbook Connections** dialog, select the connection that you just created, and then click **Properties**.

On the **Connection Properties** dialog, on the **Definition** tab, click **Authentication Settings**.

On the **Excel Services Authentication Settings** dialog, select the **Use a stored account** option, and in the **Application ID** box, type the Application ID of the Secure Store target application that you created.

Note

In Excel 2010, select the **SSS** option.

Click **OK**.

On the **Connection Properties** dialog, click **Export Connection File**.

Save the ODC file to a trusted data connection library on your farm.

Configure an Excel workbook to use the published ODC file as a data connection

## Configure an Excel workbook to use the published ODC file as a data connection

In order for a workbook to use the ODC file that you just created, you must connect to it as a data source. Once it is connected, you can publish the workbook to a SharePoint Server 2013 document library and it will maintain its connection to the ODC file. Excel Services then uses the connection information specified in the ODC file when it refreshes data in the workbook.

Use the following procedure to connect to the ODC file in Excel.

**To use an ODC file as a data source in Excel**

In Excel, on the **Data** tab, in the **Get External Data** section, click **Existing Connections**.

On the **Existing Connections** dialog, click **Browse for More**.

On the **Select Data Source** dialog, in the URL box, type the URL for the trusted data connection library where you saved the ODC file, and then press Enter.

Note

It may take several moments for the list to refresh with content from the specified location.

On the list of **Data Connections**, select the ODC file that you saved, and then click **Open**.

On the **Import Data** dialog, select the **PivotTable Report** or **PivotChart and PivotTable Report** option, and then click **OK**.

On the **Data** tab, click **Connections**.

On the **Workbook Connections** dialog, select the connection that you just opened, and then click **Properties**.

On the **Connection Properties** dialog, on the **Definition** tab, select the **Always use connection file** check box, and then click **OK**.

Note

This ensures that the connection file that you connected to will be used rather than the embedded connection information.

Click **Close**.

Once you have completed the data connection wizard, you can create your report and then publish it to a document library. When the workbook is rendered using Excel Services, Excel Services uses the connection information specified in the ODC file to refresh the data.

Note

You must publish the workbook to an Excel Services trusted file location.

See also

## See also

Concepts

#### Concepts

Configure the Secure Store Service in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
