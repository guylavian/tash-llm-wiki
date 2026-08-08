---
title: "Configure Secure Store for use with PerformancePoint Services - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-secure-store-for-use-with-performancepoint-services
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-secure-store-for-use-with-performancepoint-services
family: administration
documentKind: "how-to"
abstract: "Configure PerformancePoint Services to use a Secure Store target application for external data refresh."
---

# Configure Secure Store for use with PerformancePoint Services - SharePoint Server

Note

Configure Secure Store for use with PerformancePoint Services

# Configure Secure Store for use with PerformancePoint Services

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

PerformancePoint Services supports two methods of using Secure Store Service to connect to external data:

You can specify a Secure Store target application in PerformancePoint Dashboard Designer. This article describes how to do this.

You can use an unattended service account. For more information, see Configure the unattended service account for PerformancePoint Services.

To configure PerformancePoint Services data access to use a Secure Store target application, you use the following process:

Configure a data access account

Create a Secure Store target application

Configure a data connection to use a Secure Store target application

Configure a data access account

## Configure a data access account

You must have a Windows Active Directory account that can be granted access to the data source to which you want to connect in Dashboard Designer. This account will be stored in Secure Store.

Once you have created the account, the next step is to grant that account read access to the required data. (In this article, we use the example of accessing a SQL Server database. If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data-read permissions for the data access account.)

Follow these steps to create a SQL Server logon and grant Read access to the database.

**To create a SQL Server logon for the data access account**

In SQL Server Management Studio, connect to the database engine.

In Object Explorer, expand **Security**.

Right-click **Logins**, and then click **New Login**.

In the **Login name** box, type the name of the Active Directory account that you created for data access.

In the **Select a page** section, click **User Mapping**.

Select the **Map** check box for the database that you want to provide access to, and then, under **Database role membership for: <database>**, select the **db_datareader** check box.

Click **OK**.

Now that you have created a data access account and granted it access to a data source, the next step is to create a Secure Store target application.

Create a Secure Store target application

## Create a Secure Store target application

You must create a target application in Secure Store that contains the credentials that you created for data access. This target application can then be specified in the data source settings in Dashboard Designer.

When you create the target application, you have to specify which users will be authorized to use the credentials stored in Secure Store. You can list users individually, or you can use an Active Directory group. We recommend that you use an Active Directory group for ease of administration.

Note

The users that you list in the target application do not have direct access to the stored credentials. Instead, Dashboard Designer uses the credentials on their behalf to connect to the database, and PerformancePoint Services uses the credentials on their behalf when refreshing data in a published dashboard.

Use the following procedure to create a Secure Store target application.

**To create a target application**

On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.

Click the Secure Store service application.

On the ribbon, click **New**.

In the **Target Application ID** box, type a unique identifier for this target application (for example, PerformancePointServicesDataAccess).

In the **Display Name** box, type a friendly name or short description.

In the **Contact E-mail** box, type the e-mail address for a contact for this target application.

In the **Target Application Type** drop-down list, select **Group**.

Click **Next**.

On the Credential Fields page, leave the default values of Windows User Name and Windows Password and click **Next**.

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

Once you have set the credentials for the target application, the target application is ready to use. The next step is to specify this target application in Dashboard Designer as part of the data source settings.

Configure a data connection to use a Secure Store target application

## Configure a data connection to use a Secure Store target application

You must configure your PerformancePoint Services data connection to use the Secure Store. After doing so, you can connect to the external data source in Dashboard Designer and create your dashboard. Use the following procedure to configure a PerformancePoint Services data connection.

**To configure a data connection to use a Secure Store target application**

In Dashboard Designer, on the Create tab, click Data Source.

On the **Select a Data Source Template** dialog, choose your data source and click OK.

In the Data Source Settings section, choose the Use a stored account option.

In the Application ID box, type the target application ID of the Secure Store target application that you created.

In the Connection Settings section, connect to your external data source.

Click **Test Data Source** to test the connection.

Create and publish your dashboard.

Note

For detailed information about creating dashboards, see Create Dashboards by using PerformancePoint Services (SharePoint Server 2016).

With the target application specified in Dashboard Designer, PerformancePoint Services uses the credentials associated with that target application to refresh the data in the dashboard after you have published it to SharePoint Server.

See also

## See also

Concepts

#### Concepts

Configure the Secure Store Service in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
