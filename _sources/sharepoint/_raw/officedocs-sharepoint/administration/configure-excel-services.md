---
title: "Configure Excel Services (SharePoint Server 2013) - SharePoint Server"
description: "Deploy Excel Services to your SharePoint Server farm by creating an Excel Services service application by using Central Administration."
ms.topic: how-to
---
Note

Configure Excel Services (SharePoint Server 2013)

# Configure Excel Services (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

The steps in this article apply to SharePoint Server 2013 Enterprise.

Excel Services is enabled by creating an Excel Services Application service application in Central Administration. This article walks you through the steps of deploying Excel Services in your SharePoint Server 2013 farm.

Before you begin

## Before you begin

Before you deploy Excel Services, we recommend that you review Overview of Excel Services in SharePoint Server 2013 and its associated Excel Services planning articles.

Before you begin this operation, review the following information about prerequisites:

A domain account is required to run the Excel Services application pool.

You must be a member of the Farm Administrators group to perform the procedures in this article.

Video demonstration

## Video demonstration

This video shows the steps involved in creating an Excel Services service application, as described in this article.

**Video: Configure Excel Services in SharePoint Server 2013**

Configure the application pool account

## Configure the application pool account

For better security, we recommend that you use a separate domain account to run the Excel Services application pool. Have your domain administrator create a domain account to use in running the Excel Services application pool. No specific domain privileges are required for this account.

Before you can use an account to run an application pool, you must register it as a managed account in SharePoint Server. Use the following procedure to register the account.

**To register a managed account**

On the SharePoint Central Administration website home page, in the left navigation, click **Security**.

On the Security page, under **General Security**, click **Configure managed accounts**.

On the Managed Accounts page, click **Register Managed Account**.

Type the user name and password of the domain account that you are registering.

Optionally, select the **Enable automatic password change** check box if you want SharePoint Server to manage password changes for this account.

Click **OK**.

Grant content database access to the managed account

### Grant content database access to the managed account

You must also grant access to the SharePoint content database for the account that you will use to run the Excel Services application pool. Use the following procedure for each web application that will be associated with Excel Services.

**To grant content database access to the managed account**

On a SharePoint Server application server, click **Start**, click **All Programs**, click **Microsoft SharePoint 2013 Products**, right-click **SharePoint 2013 Management Shell**, and then click **Run as Administrator**.

At the Microsoft PowerShell Command Prompt, type the following (press Enter after each line):

```
$w = Get-SPWebApplication -identity http://<WebApplication>
$w.GrantAccessToProcessIdentity("<Domain>\<Username>")
```

Important

If in the future you add additional content databases, you must rerun these cmdlets to ensure that Excel Services has access to the new databases.

Once you have granted content database access to the application pool account, the next step is to start the Excel Calculation Services service.

Start the Excel Calculation Services service

## Start the Excel Calculation Services service

In order to use Excel Services, you must start the Excel Calculation Services service on at least one application server in the farm. Use the following procedure to start the service.

**To start the Excel Calculation Services service**

On the Central Administration home page, in the **System Settings** section, click **Manage services on server**.

To select the server where you want to start the service, above the **Service** list, click the **Server** drop-down list, and then click **Change Server** and choose the appropriate server.

In the **Service** list, click **Start** next to **Excel Calculation Services**.

After the Excel Calculation Services service has been started, the next step is to create an Excel Services service application.

Create an Excel Services service application

## Create an Excel Services service application

Use the following procedure to create an Excel Services service application.

**To create an Excel Services service application**

On the Central Administration home page, under **Application Management**, click **Manage service applications**.

On the Manage Service Applications page, click **New**, and then click **Excel Services Application**.

In the **Name** section, type a name for the service application in the text box.

Select the **Create new application pool** option and type a name for the application pool in the text box.

Select the **Configurable** option, and from the drop-down list, select the account that you created to run the application pool.

Click **OK**.

Additional steps

## Additional steps

Once you have created the service application, you are ready to start using Excel Services. See the following articles for additional configuration steps.

Manage Excel Services global settings (SharePoint Server 2013)

Manage Excel Services trusted file locations (SharePoint Server 2013)

Manage Excel Services trusted data providers (SharePoint Server 2013)

Manage Excel Services trusted data connection libraries (SharePoint Server 2013)

Manage Excel Services user defined function assemblies (SharePoint Server 2013)

Manage Excel Services data model settings (SharePoint Server 2013)

See also

## See also

Other Resources

#### Other Resources

Excel Services cmdlets in SharePoint Server 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
