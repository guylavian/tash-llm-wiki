---
title: "Configure the Managed Metadata service - SharePoint Server"
description: "Learn how to configure a Managed Metadata service application in SharePoint Server."
ms.topic: how-to
---
Note

Configure the Managed Metadata service

# Configure the Managed Metadata service

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In this article we cover how to configure a Managed Metadata service application in SharePoint Server. Be sure you've planned your configuration before you follow the procedures below.

To configure a Managed Metadata service application, you perform the following steps:

Register a managed account in SharePoint Server to run the Managed Metadata service application pool.

Start the Managed Metadata Web Service (SharePoint Server 2013 only).

Create a Managed Metadata service application.

Configure the Managed Metadata service connection

Start the Managed Metadata Web Service (SharePoint Server 2013 only)

## Start the Managed Metadata Web Service (SharePoint Server 2013 only)

If you are using SharePoint Server 2013, you must start the Managed Metadata Web Service on at least one server in your farm. (This service is started automatically in SharePoint Server 2016.)

**To start the Managed Metadata Web Service**

On the SharePoint Central Administration Web site home page, click **Manage services on server**.

Click **Server** and then select the server where you want to start the Managed Metadata Web Service.

In the **Service** list, click **Start** for the **Managed Metadata Web Service**.

Configure a Managed Metadata service application in SharePoint Server

## Configure a Managed Metadata service application in SharePoint Server

To run the application pool, you must have a standard domain account. No specific permissions are required for this account. Once the account has been created in Active Directory, follow these steps to register it with SharePoint Server.

**To register a managed account**

On the SharePoint Central Administration Web site home page, in the left navigation, click **Security**.

On the Security page, in the **General Security** section, click **Configure managed accounts**.

On the Managed Accounts page, click **Register Managed Account**.

In the **User name** box, type the name of the account.

In the **Password** box, type the password for the account.

If you want SharePoint Server to handle changing the password for the account, select the **Enable automatic password change** box and specify the password change parameters that you want to use.

Click **OK**.

Once you have configured the registered account, you must create a Managed Metadata service application. Use the following procedure to create the service application.

**To create a Managed Metadata service application**

On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.

On the Manage Service Applications page, click **New**, and then click **Managed Metadata Service**.

In the **Name** box, type a name for the service application (for example, Managed Metadata Service).

In the **Database Server** box, type the instance of SQL Server where you want to create the Managed Metadata database.

In the **Database Name** box, type the name that you want to use for the Managed Metadata database.

In the **Failover Database Server** box, type the name of your failover database server if you're using one.

Select the **Create new application pool** option and type a name for the application pool in the text box.

Select the **Configurable** option, and, from the drop-down list, select the account for which you created the managed account earlier.

If you're configuring a Content Type Hub, type the URL for that site collection in the **Content Type Hub** box.

Click **OK**.

The Managed Metadata service application has now been configured. The next step is to configure the settings for the Managed Metadata service connection.

Configure the Managed Metadata service connection

## Configure the Managed Metadata service connection

Each managed metadata service application has an associated managed metadata service connection. Using the service connection, you can configure the following four options:

**This service application is the default storage location for Keywords** - Determines if this service application is used as the default location for enterprise keywords.

If you are using more than one Managed Metadata service application, only select this option for one service application per web application.

If you do not want to use the enterprise keywords functionality, make sure this check box is not selected for any of your Managed Metadata service connections.

**This service application is the default storage location for column specific term sets** - Determines if this service application is used to store custom term sets that are created at the site collection level.

If you are using more than one Managed Metadata service application, only select this option for one service application per web application.

If you do not want to allow custom term sets, make sure this check box is not selected for any of your Managed Metadata service connections.

**Consumes content types from the content type gallery at http://<site>** - Determines if this service application makes the content types that are that are defined in the specified content type gallery available to users of sites in this web application. This option is available only if the service has a hub defined to share content types.

**Push-down Content Type Publishing updates from the Content Type Gallery to sub-sites and lists using the content type** - Determines if change in content types are published to sub-sites and lists that use the content type.

Use the following procedure to set these options:

**To configure a managed metadata service connection**

In Central Administration, under **Application Management**, click **Manage service applications**.

Find the managed metadata service connection for the service application that you want to configure. (Look for **Managed Metadata Service Connection** in the **Type** column.)

Highlight that row, and then click **Properties**.

Select the check boxes for the options that you want to enable, and then click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
