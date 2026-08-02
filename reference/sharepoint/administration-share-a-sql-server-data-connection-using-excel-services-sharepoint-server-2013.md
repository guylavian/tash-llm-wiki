---
title: "Share a SQL Server data connection using Excel Services (SharePoint Server 2013) - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-share-a-sql-server-data-connection-using-excel-services-sharepoint-server-2013
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/share-a-sql-server-data-connection-using-excel-services-sharepoint-server-2013
family: administration
documentKind: "how-to"
abstract: "Learn how to use Excel to create and share connections to SQL Server data that people can use to create data models, reports, scorecards, and dashboards."
---

# Share a SQL Server data connection using Excel Services (SharePoint Server 2013) - SharePoint Server

Note

Share a SQL Server data connection using Excel Services (SharePoint Server 2013)

# Share a SQL Server data connection using Excel Services (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can use Excel to create connections to databases such as SQL Server, and then share those connections with others. When you can upload a data connection to an Excel Services trusted data connection library in SharePoint Server 2013, the data connection is available for you and others to use to create data models, reports, scorecards, and dashboards. Depending on the particular data source that is used, people can easily refresh data in Excel Services workbooks so that the most current information is displayed.

Before you begin

## Before you begin

Before you begin this task, review the following information about prerequisites:

You must be using Excel 2016 and SharePoint Server 2013.

Excel Services must be configured to include a trusted data connections library and a trusted documents library. Ideally, you'll have a Business Intelligence Center site configured that you can use for your data connections and workbooks. For more information, see Configure a Business Intelligence Center in SharePoint Server 2013.

You must have at least Contribute permissions assigned in SharePoint Server 2013.

You will need information from a SharePoint admin about how data authentication is configured for the databases your organization uses. This can affect how you connect to different data sources.

If you plan to publish workbooks that contain data models to SharePoint Server 2013, Excel Services must be configured to support data models. For more information, see Configure Excel Services in SharePoint Server 2013 Preview.

Step 1: Use Excel to create connections to SQL Server data

## Step 1: Use Excel to create connections to SQL Server data

You can use Excel to create a connection one or more tables that are stored in SQL Server. This kind of connection is an Office Data Connection (ODC) file that can be used to create reports, scorecards, and dashboards by using applications such as Excel.

**To create a SQL Server tabular data connection by using Excel**

In Excel, on the **Data** tab, in the **Get External Data** group, click **From Other Sources**, and then select **From SQL Server**.

The Data Connection Wizard opens.

On the **Connect to Database Server** page, in the **Server name** box, specify the name of the server where the SQL Server data that you want to use resides. Do not click **Next** yet.

In the **Log on credentials** section, take one of the following steps:

If your organization is using Windows Authentication, choose **Use Windows Authentication**, and then choose the **Next** button.

If your organization is using specific user credentials, choose **Use the following User Name and Password**, specify an appropriate user name and password, and then choose the **Next** button.

On the **Select Database and Table** page, in the **Select the database that contains the data that you want** list, select the database that you want to use. Do not click **Next** yet.

On the **Select Database and Table** page, take one of the following steps:

To create a connection that uses a single table, select **Connect to a specific table**. Select the table that you want to use, and then click **Next**.

To create a connection that uses more than one table, select both **Connect to a specific table** and **Enable selection of multiple tables**. Select the tables that you want to use, click **Select Related Tables**, and then click **Next**.

On the **Save Data Connection File and Finish** page, take the following steps:

In the **File Name** box, keep or change the default file name.

In the **Description** box, type a brief description for the data connection.

In the **Friendly Name** box, keep the default name or type a new name for file.

In the **Search Keywords** box, type some words or phrases that will help users find the data connection when it is published to SharePoint Server 2013.

Next to **Excel Services**, click **Authentication Settings...**, and then take one of the following steps:

If you want this connection to use Windows Authentication or the Effective User Name feature, select **Use the authenticated user's account**, and then click **OK**.

If you want this connection to use Secure Store Service, select **Use a stored account**. In the **Application ID** box, specify the Secure Store target application ID, and then click **OK**.

If Excel Services is configured to use the unattended service account, select **None**, and then click **OK**.

Important

If you do not know which option to choose, contact a SharePoint admin.

Click **Finish** to close the **Save Data Connection File and Finish** page.

On the **Import Data** page, click **Only Create Connection**, and then click **OK**.

Repeat steps 1-7 until you have created all the data connections that you want.

Close Excel.

By default, the data connection is saved in the **My Data Sources** folder in the **Documents** library on your computer.

Step 2: Upload data connections to SharePoint Server

## Step 2: Upload data connections to SharePoint Server

After data connections are created, the next step is to upload it to a data connection library. We recommend that you use a Business Intelligence Center site to store and manage business intelligence content, such as data connections.

Note

If you are not using a Business Intelligence Center site, make sure that you use a data connection library that is specified as a trusted location in Excel Services. For more information, see Manage Excel Services trusted data connection libraries (SharePoint Server 2013).

**To upload a data connection to SharePoint Server**

Open a web browser and navigate to the SharePoint site that contains the data connection library that you want to use.

If you are using a Business Intelligence Center, the website address (URL) resembles http://servername/sites/bicenter.

Click **Site Contents** to view the lists and libraries that are available for that site.

Click **Data Connections** to open that library.

Click **New Item** to open the **Add a document** dialog.

Click **Browse** to open the **Choose File to Upload** dialog.

Assuming the data connection is saved in its default location, click **Libraries**, click **Documents**, and then double-click **My Data Sources**.

Select the ODC file that you want to upload, and then click **Open**.

In the **Add a document** dialog, click **OK**.

A **Data Connections** form opens.

In the **Data Connections** form, specify the following settings:

In the **Content Type** section, confirm that **Office Data Connection File** is selected.

In the **Name** box, keep or change the file name of the ODC file.

In the **Title** box, keep or change the title of the ODC file.

In the **Description** box, type a description of the data connection.

In the **Keywords** box, type one or more words or phrases. This information is used by search queries to discover the data connection.

Then click **Save**.

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
