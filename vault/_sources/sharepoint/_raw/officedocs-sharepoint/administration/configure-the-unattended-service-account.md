---
title: "Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account - SharePoint Server"
description: "Configure Visio Services in SharePoint Server to refresh data by using the unattended service account."
ms.topic: how-to
---
Note

Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account

# Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Configuring an unattended service account for Visio Services consists of the following steps:

Create an account to use for data access

Create a logon for the data access account on the data source

Create a Secure Store target application that uses the data access account credentials

Configure Visio Services to use the Secure Store target application for the unattended service account

Create an Office Data Connection (ODC) file by using Visio and publish it to a SharePoint data connection library

Use the ODC file as a data source in Visio

The first step is to create an account to use for data access. Have your domain administrator create an Active Directory account that you can use to access your data sources.

Important

Visio Services requires an Active Directory account for the unattended service account. You cannot use a non-Windows account.

Once the account has been created, follow these steps to create a logon for the data access account in SQL Server. (If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data read permissions for the data access account.)

**To create a SQL Server logon for the data access account**

In SQL Server Management Studio, connect to the database engine.

In Object Explorer, expand **Security**.

Right-click **Logins**, and then click **New Login**.

In the **Login name** box, type the name of the Active Directory account that you created for data access.

In the **Select a page** section, click **User Mapping**.

Select the **Map** check box for the database that you want to provide access to, and then in the **Database role membership for: <database>** section, select the **db_datareader** check box.

Click **OK**.

After you have created a logon for the data access account and granted the account access to your data source, you must create a target application in Secure Store to contain the credentials for the data access account.

**To create a target application for the unattended service account**

On the the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.

Click the Secure Store Service service application.

On the ribbon, click **New**.

In the **Target Application ID** box, type an ID for the target application (for example, VisioServicesUnattended).

In the **Display Name** box, type a name for the target application.

In the **Contact E-mail** box, type an email address.

In the **Target Application Type** drop-down list, select **Group**.

Click **Next**.

Leave the default credential fields, and then click **Next**.

On the "Specify the membership settings" page:

In the **Target Application Administrators** box, type the account of the user who will administer this account.

Note

You can type multiple names or the name of an Active Directory group that contains the users whom you want to administer this target application.

In the **Members** box, type Everyone.

Note

The unattended service account is intended for granting broad database access. You can restrict the users who have access to the unattended service account to a specific Active Directory group if you want, but be aware that only one unattended service account can be created per Visio Services service application.

Click **OK**.

After the target application has been created, you must set the target application to use the credentials for the data access account that you created. Use the following procedure to set the credentials.

**To set the credentials for the target application**

On the Secure Store Service Application page, in the **Target Application ID** column, point to the target application that you just created, click the arrow that appears, and then click **Set Credentials**.

In the **Windows User Name** box, type the Active Directory account that you created for data access.

Type and confirm the password for the account.

Click **OK**.

The target application configuration is now complete. The next step is to designate this target application for use as the unattended service account in Visio Services. Use the following procedure to configure the unattended service account in Visio Services Global Settings.

**To configure Visio Services Global Settings**

On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click the Visio Services service application.

On the Manage the Visio Graphics Service page, click **Global Settings**.

On the Visio Graphics Service Settings page, in the **External Data** section, in the **Application ID** box, type the ID of the Secure Store target application that you just created.

Click **OK**.

Once you have configured the External Data setting in Visio Services Global Settings, the unattended service account is configured and ready to use.

The next step is to create an ODC file that specifies the unattended service account. You can create the ODC file in Visio as part of your diagram creation process.

Use the following procedure to create an ODC file and create a data-connected drawing.

**To create an ODC file and link data to shapes in Visio**

In Visio, open a diagram or create a new diagram.

On the ribbon, click the **Data** tab, and then click **Link Data to Shapes**.

On the Connect to Database Server page, type the name of your database server, and then click **Next**.

On the Select Database and Table page, select the database to which you want to connect, and then click **Next**.

On the Save Data Connection File and Finish page:

Click **Authentication Settings**.

On the **Visio Services Authentication Settings** dialog, choose the **None** option and click **OK**.

Click **Browse**.

Browse to a data connection library.

Note

Visio Services does not require that ODC files be saved to a data connection library. However, for easiest administration, we recommend using data connection libraries to store all your data connection files.

Type a name for the ODC file, and then click **Save**.

Click **Finish**.

If the **Web File Properties** dialog appears, click **Cancel**.

On the Select Data Connection page, click **Finish**.

Connect the data to the shapes in your diagram.

When you are ready to save the drawing, click **File**, click **Save**, and then browse to a SharePoint document library.

Type a file name, and then click **Save**.

Once the diagram has been published, it is available to view by using Visio Services. When the data in the diagram is refreshed, it uses the ODC file that you specified. The **None** option specified in the ODC file will cause Visio Services to use the unattended service account.

Once the ODC file has been saved to the data connection library, you can connect directly to it when linking data to shapes in Visio. This allows you to share a single data connection file among multiple Visio diagrams.

Use the following procedure to connect to an existing ODC file.

**To create a data-connected diagram by using an ODC file**

In Visio, open a diagram or create a new diagram.

On the ribbon, click the **Data** tab, and then click **Link Data to Shapes**.

On the Data Selector page of the wizard, click **Previously created connection**, and then click **Next**.

On the Select Data Connection page, click **Browse**.

On the **Existing Connections** dialog, click **Browse for More**.

In the **Data Selector** dialog, in the **URL** box, type the URL of the data connection library where you saved the ODC file, and then press Enter.

Select the ODC file and then click **Open**.

On the Select Data Connection page, click **Finish**.

Connect the data to the shapes in your diagram.

When you are ready to save the drawing, click **File**, click **Save**, and then browse to a SharePoint document library.

Type a file name, and then click **Save**.

See also

## See also

Concepts

#### Concepts

Configure Visio Services data refresh in SharePoint Server by using external data connections

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
