---
title: "Configure PerformancePoint Services - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-performancepoint-services
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-performancepoint-services
family: administration
documentKind: "how-to"
abstract: "Configure PerformancePoint Services in SharePoint Server."
---

# Configure PerformancePoint Services - SharePoint Server

Note

Configure PerformancePoint Services

# Configure PerformancePoint Services

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article describes how to create and configure a PerformancePoint Services service application.

To properly configure PerformancePoint Services, do the following steps in the order listed:

Install ADOMD.NET from the SQL Server 2012 Feature Pack

Configure the PerformancePoint Services application pool account

Start the PerformancePoint service (SharePoint Server 2013 only) (SharePoint Server 2013 only)

Create a PerformancePoint Services service application

Configure PerformancePoint service application associations

Note

PerformancePoint Services has been removed from SharePoint Server Subscription Edition. We recommend to explore Microsoft Power BI as an alternative to PerformancePoint Services.

Configure the PerformancePoint Services application pool account

## Configure the PerformancePoint Services application pool account

The application pool for the PerformancePoint Services service application requires a SharePoint Server managed account (generally an Active Directory account) to run. This account must have access to the content databases where PerformancePoint data will be stored.

If you run the service application using the same application pool account as the web application where the content databases are located, this required database access is configured automatically. However, we recommend that you use a different account for the PerformancePoint Services application pool, especially in a large or complex farm. This allows for greater control over data and resource access.

If you choose to use the same managed account for PerformancePoint Services as is being used for the web application, you can skip the procedures in this section. If you choose to create a new managed account, you must do the following:

Register a managed account in SharePoint Server. (You will need an Active Directory user account for this step. Have your Active Directory administrator create it.)

Grant access for this account to the content databases that will contain PerformancePoint data. This process includes running a Microsoft PowerShell script from the SharePoint 2016 Management Shell.

The first step is to register a managed account. Use the following procedure to register the Active Directory account that you want to use for the PerformancePoint Services application pool.

**To register a managed account**

In the SharePoint Server Central Administration Web site, click **Security**.

In the **General Security** section, click **Configure managed accounts**.

Click **Register Managed Account**.

In the **Service account credentials** section, type the user name and password for the Active Directory account that you want to register.

Optionally, if the account password is set to expire after a certain length of time, configure the automatic password change settings to have SharePoint Server change the password.

Click **OK**.

Once you have registered the managed account, you must grant that account access to the content databases where PerformancePoint data will be stored. Use the following procedure to grant database access to the account. Follow this procedure for each web application that contains a content database where PerformancePoint Services data will reside.

**To grant content database access to an account**

Open the **SharePoint 2016 Management Shell** as administrator.

At the Microsoft PowerShell command prompt, type the following, pressing Enter after each line:

```
$w = Get-SPWebApplication -identity <web application>
$w.GrantAccessToProcessIdentity("<service account>")
```

Once you have finished granting content database access to the managed account, the next step is to create a PerformancePoint Services service application.

Start the PerformancePoint service (SharePoint Server 2013 only)

## Start the PerformancePoint service (SharePoint Server 2013 only)

If you are using SharePoint Server 2013, you must start the PerformancePoint service on the application server where you want to run PerformancePoint Services. (In SharePoint Server 2016 this is handled automatically by MinRole.) You can start the service on multiple application servers for better performance, if you want, but the service must be started on at least one server. Use the following procedure to start the PerformancePoint service.

**To start the PerformancePoint Service**

In Central Administration, in the **System Settings** section, click **Manage services on server**.

Note the server specified in the **Server** box. If you want to run the PerformancePoint service on a different server, click the current server, and then click **Change Server** and select the server that you want.

Click **Start** next to **PerformancePoint Service**.

Create a PerformancePoint Services service application

## Create a PerformancePoint Services service application

Use the following procedure to create the service application.

**To create a PerformancePoint Services service application**

In Central Administration, in the **Application Management** section, click **Manage Service Applications**.

Click **New**, and then click **PerformancePoint Service Application**.

Type a name for the service application and select the **Add this service application's proxy to the farm's default proxy list** check box.

Select the **Create new application pool** option and type a name for the application pool.

Under the **Configurable** option, select the managed account to run the application pool.

Click **Create**.

Click **OK**.

When you configure the service application in SharePoint Server 2016, the PerformancePoint Service will autoprovision on all servers in the farm that are running under the Front-end role.

Configure PerformancePoint service application associations

## Configure PerformancePoint service application associations

For PerformancePoint Services to function, the PerformancePoint Services service application proxy must be associated with the default web application. Use the following procedure to confirm that the association is configured between the web application and the PerformancePoint Services proxy.

**To configure service application associations**

In Central Administration, click **Application Management**.

In the **Service Applications** section, click **Configure service application associations**.

Under the **Application Proxy Group** column, click **default**.

Ensure that the **PerformancePoint Services** box is selected.

Click **OK**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
