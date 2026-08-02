---
title: "Share an OLE DB or ODBC connection using Excel Services (SharePoint Server 2013) - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-share-an-ole-db-or-odbc-connection-using-excel-services-sharepoint-server-2013
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/share-an-ole-db-or-odbc-connection-using-excel-services-sharepoint-server-2013
family: administration
documentKind: "how-to"
abstract: "Learn how to use Excel to create and share OLE DB or ODBC connections that people can use to create data models, reports, scorecards, and dashboards."
---

# Share an OLE DB or ODBC connection using Excel Services (SharePoint Server 2013) - SharePoint Server

Note

Share an OLE DB or ODBC connection using Excel Services (SharePoint Server 2013)

# Share an OLE DB or ODBC connection using Excel Services (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can use Excel to create OLE DB or ODBC connections and then share those connections with others. An OLE DB or ODBC connection is useful for connecting to data sources, such as Excel workbooks, legacy databases, or non-Microsoft databases. When you can upload a data connection to an Excel Services trusted data connection library in SharePoint Server 2013, the data connection is available for you and others to use to create data models, reports, scorecards, and dashboards. Depending on the particular data source that is used, people can easily refresh data in Excel Services workbooks so that the most current information is displayed.

Before you begin

## Before you begin

Before you begin this task, review the following information about prerequisites:

You must be using Excel 2016 and SharePoint Server 2013.

Excel Services must be configured to include a trusted data connections library and a trusted documents library. Ideally, you'll have a Business Intelligence Center site configured that you can use for your data connections and workbooks. For more information, see Configure a Business Intelligence Center in SharePoint Server 2013.

You must have at least Contribute permissions assigned in SharePoint Server 2013.

You will need info from a SharePoint admin about how data authentication is configured for the databases your organization uses. This can affect how you connect to different data sources.

You will need info about the data source that you want to use. In particular, you must know the data source name, user name, and password to connect to the data source.

If you plan to publish workbooks that contain data models to SharePoint Server 2013, Excel Services must be configured to support data models. For more information, see Configure Excel Services in SharePoint Server 2013 Preview.

Step 1: Use Excel to create OLE DB or ODBC data connections

## Step 1: Use Excel to create OLE DB or ODBC data connections

You can use Excel to create an OLE DB or ODBC connection. This enables you to connect to lots of different data sources. Examples include Microsoft SQL Server, Microsoft Access, and Oracle databases, although there are many others. You can create an OLE DB or ODBC data connection by using one of several methods:

You can create a connection by using the Data Connection Wizard in Excel. (This is the recommended method to use.)

You can create a connection by using a Microsoft Query Wizard in Excel.

Use the following procedures to create OLE DB or ODBC data connections

**To create a connection by using the Data Connection Wizard in Excel**

In Excel, on the **Data** tab, in the **Get External Data** group, select **From Other Sources**, and then select **From Data Connection Wizard**.

The Data Connection Wizard opens.

In the **What kind of data source do you want to connect to?** list, select a data source, and then select **Next**.

Depending on the kind of data source that you selected, specify the necessary information for that data source.

Tip

The info that you specify varies according to the data source. For example, a Data Feed data source requires a link or location to a data feed and logon credentials, whereas an Excel workbook data source requires you to locate where the workbook is stored. For specific details regarding the connection that you want to create, contact a database admin.

On the **Select Database and Table** page, in the **Select the database that contains the data that you want** list, select the database that you want to use. Do not select **Next** yet.

On the **Select Database and Table** page, select the table (or tables) that you want to use, and then select **Next**.

On the **Save Data Connection File and Finish** page, take the following steps:

In the **File Name** box, keep or change the default file name.

In the **Description** box, enter a brief description for the data connection.

In the **Friendly Name** box, keep the default name, or enter a new name for file.

In the **Search Keywords** box, enter some words or phrases that will help users find the data connection when it is published to SharePoint Server 2013.

Next to **Excel Services**, select **Authentication Settings...**.

Select **None**, and then select **OK**.

To close the **Save Data Connection File and Finish** page, select **Finish**.

On the **Import Data** page, select **Only Create Connection**, and then select **OK**.

Repeat steps 1-7 until you have created all the data connections that you want.

If you cannot create the connection that you want by using the Data Connection Wizard in Excel, you can try to create the connection by using a Microsoft Query wizard. This is useful for connecting to older databases. However, the connection that you create might not be supported in Excel Services. Contact a SharePoint admin to verify that the connection that you create is supported so that people can refresh data in Excel Services files. The following procedure describes how to create a connection by using a Microsoft Query wizard.

**To create a connection by using a Microsoft Query wizard in Excel**

In Excel, on the **Data** tab, in the **Get External Data** group, select **From Other Sources**, and then select **From Microsoft Query**.

The **Choose Data Source** dialog appears.

To specify the data source that you want to use, select the **Databases**, **Queries**, or **OLAP Cubes** tab.

Tip

The info that you specify varies according to the data source. For example, if you select an Access database or an Excel file, you'll be prompted to navigate to the database or file on your computer. Or, if you choose to use a data source that is not listed, you'll be prompted to create a data source and then specify the kind of data source, location, and credentials to connect to it. Contact a database administrator for specific details regarding the connection that you want to create.

On the **Import Data** page, select **Only Create Connection**, and then select **OK**.

Repeat steps 1-3 until you have created all the data connections that you want.

By default, the data connection is saved in the **My Data Sources** folder in the **Documents** library on your computer.

Step 2: Upload data connections to SharePoint Server

## Step 2: Upload data connections to SharePoint Server

After data connections are created, the next step is to upload it to a data connection library. We recommend that you use a Business Intelligence Center site to store and manage business intelligence content, such as data connections.

Note

If you are not using a Business Intelligence Center site, make sure that you use a data connection library that is specified as a trusted location in Excel Services. For more information, see Manage Excel Services trusted data connection libraries (SharePoint Server 2013).

**To upload a data connection to SharePoint Server**

Open a web browser and navigate to the SharePoint site that contains the data connection library that you want to use.

If you are using a Business Intelligence Center, the website address (URL) resembles http://servername/sites/bicenter.

To view the lists and libraries that are available for that site, select **Site Contents**.

To open that library, select **Data Connections**.

To open the **Add a document** dialog, select **New Item**.

To open the **Choose File to Upload** dialog, select **Browse**.

Assuming the data connection is saved in its default location, select **Libraries**, then select **Documents**, and then double-click **My Data Sources**.

Select the ODC file that you want to upload, and then select **Open**.

In the **Add a document** dialog, select **OK**.

A **Data Connections** form opens.

In the **Data Connections** form, specify the following settings:

In the **Content Type** section, confirm that **Office Data Connection File** is selected.

In the **Name** box, keep or change the filename of the ODC file.

In the **Title** box, keep or change the title of the ODC file.

In the **Description** box, enter a description of the data connection.

In the **Keywords** box, enter one or more words or phrases. This info is used by search queries to discover the data connection.

Select **Save**.

The data connection is added to the library. Repeat this procedure for each data connection that you want to share.

See also

## See also

Concepts

#### Concepts

Share data connections by using Excel and Excel Services (SharePoint Server 2013)

Data sources supported in Excel Services (SharePoint Server 2013)

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
