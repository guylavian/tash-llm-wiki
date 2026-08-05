---
title: "Set up SharePoint services for hybrid environments - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-set-up-sharepoint-services-for-hybrid-environments
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/set-up-sharepoint-services-for-hybrid-environments
family: hybrid
documentKind: "how-to"
abstract: "Learn how to set up the SharePoint Server services you'll need for a hybrid environment."
---

# Set up SharePoint services for hybrid environments - SharePoint Server

Note

Set up SharePoint Server services for hybrid environments

# Set up SharePoint Server services for hybrid environments

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**This article is part of a roadmap of procedures for configuring SharePoint hybrid solutions. Be sure you're following a roadmap when you do the procedures in this article.**

Set up SharePoint Server services for hybrid

## Set up SharePoint Server services for hybrid

SharePoint Server services such as My Sites, User Profiles, and Managed Metadata can be challenging to deploy and can require a lot of planning. If you plan to make use of these services in depth, we highly recommend that you follow the detailed planning information for My Sites, User Profiles, and Managed Metadata.

However, SharePoint Server hybrid scenarios, such as hybrid Search require several services to be running in SharePoint Server, but they do not require them to be extensively configured. In this article, we're going to look at the easy path to getting these services running on your farm for use in a hybrid configuration. You can do more extensive configuration of these services later if you want to use more of the available features.

Note that if you're using SharePoint Server 2013, you need to turn on some services manually. (We call this out in the appropriate procedures later in the article.) If you're using SharePoint Server 2016, these services are handled automatically by MinRole.

Services for hybrid deployments in SharePoint Server

## Services for hybrid deployments in SharePoint Server

SharePoint Server hybrid configurations all require the following services to be running on your farm:

Managed Metadata service application

User Profile Service application

My Sites

If you're setting up OneDrive, these are the only services you need. If you're setting up a hybrid Search or hybrid sites features, there are some additional requirements that we'll cover in the next section.

If you've already configured these services, there's no need to add additional instances of them for hybrid, but be sure to see Configure hybrid specific settings for important configuration information for the User Profile Service for SharePoint and BCS hybrid deployments.

Let's look at how to set up each.

**Managed Metadata service**

**To turn on the Managed Metadata Web Service (SharePoint Server 2013 only)**

In Central Administration, under **System Settings**, select **Manage services on server**.

On the server dropdown, select **Change Server**.

Select the server where you want to run the Managed Metadata Web Service.

In the **Service** list, select **Start** for the **Managed Metadata Web Service**.

You need to create a Managed Metadata service application.

**To create a Managed Metadata service application**

In Central Administration, under **Application Management**, select **Manage service applications**.

Select **New**, and then select **Managed Metadata Service**.

In the **Name** box, enter a name for the service application.

In the **Database Name** box, enter a name for the database.

Under **Application Pool**, from the **Use existing application pool list**, select **SharePoint Web Services Default**.

Select **OK**.

That's all the configuration that you need to do for the Managed Metadata service if you're configuring a hybrid scenario. If you want to make further use of the Managed Metadata service, see Plan for managed metadata in SharePoint Server.

**My Sites**

The first thing we need to do is to create a web application for the My Sites site. We recommend that My Sites be in a separate web application, although the web application can be in an application pool that is shared with other collaboration sites, or it can be in a separate application pool but in a shared IIS website.

The default settings for this web application will work fine for a hybrid environment, or you can customize any that you need to for your organization.

**To create a web application**

In Central Administration, in the **Application Management** section, select **Manage web applications**.

On the ribbon, select **New**.

On the **Create New Web Application** page, in the **Authentication** section, select the authentication mode that will be used for this web application.

In the **IIS Web Site** section, you can configure the settings for your new web application by selecting one of the following two options:

Select **Use an existing web site**, and then select the website on which to install your new web application.

Select **Create a new IIS web site**, and then enter the name of the website in the **Name** box.

You can also provide the port number, host header, or path for the new IIS website.

In the **Security Configuration** section, select an authentication provider, whether to allow anonymous access, and whether to use Secure Sockets Layer (SSL).

In the **Application Pool** section, do one of the following:

If you want to use an existing application pool, select **Use existing application pool**, and then select the application pool from the dropdown.

If you want to create a new application pool, select **Create a new application pool**, enter the name of the application pool, and either select the account that the application pool will run under or create a new managed account for the application pool to run under.

In the **Database Name and Authentication** section, select the database server, database name, and authentication method for your new web application.

If you use database mirroring, in the **Failover Server** section, in the **Failover Database Server** box, enter the name of a specific failover database server that you want to associate with a content database.

In the **Service Application Connections** section, select the service application connections that will be available to the web application.

In the **Customer Experience Improvement Program** section, select **Yes** or **No**.

Select **OK** to create the new web application.

When the **Application Created** page appears, select **OK**.

Next, we need to create the site collection that will host users' My Sites.

**To create a My Site Host site collection**

On Central Administration, in the **Application Management** section, select **Create site collections**.

On the **Create Site Collection** page, in the **Web Application** section, select the web application that you just created for My Sites.

In the **Title and Description** section, enter the title and description for the site collection.

In the **Web Site Address** section, select the path of the URL for the My Site host. In most cases, you can use the root directory (/).

In the **Template Selection** section, select the **Enterprise** tab, and then select **My Site Host**.

In the **Primary Site Collection Administrator** section, enter the user name (in the form  *<DOMAIN>*\ *<user name>*) for the user who will be the site collection administrator.

In the **Secondary Site Collection Administrator** section, enter the user name for the secondary administrator of the site collection.

If you are using quotas to manage storage for site collections, in the **Quota Template** section, select a template in the **Select a quota template** list.

Select **OK**.

The **Top-Level Site Successfully Created** page will appear when the My Site Host site collection is created. Although you can select the link to browse to the root of the site collection, doing this results in an error because the user profile cannot be loaded. This behavior is to be expected; user profiles are not imported at this point.

**User Profile Service**

If you're running SharePoint Server 2013, then you need to turn on the User Profile Service on at least one server in your farm.

**To turn on the User Profile Service (SharePoint Server 2013 only)**

In Central Administration, under **System Settings**, select **Manage services on server**.

On the Server dropdown, select **Change Server**.

Select the server where you want to run the User Profile Service.

In the **Service** list, select **Start** for the **User Profile Service**.

Note

Do not turn on the User Profile Synchronization Service. We'll do that later after we've configured the User Profile service application.

Next, let's create a User Profile service application.

**To create a User Profile service application**

In Central Administration, under **Application Management**, select **Manage service applications**.

Select **New**, and then select **User Profile Service Application**.

Enter a name for the service application in the **Name** box.

Under **Application Pool**, select **SharePoint Web Services Default** from the **Use existing application pool list**.

In the **My Site Host URL** box, enter the URL of the My Site Host that you created.

Optionally change other settings to meet the needs of your organization. The default settings work fine for hybrid environments.

Select **OK**.

If you're using SharePoint Server 2013, the next step is to turn on the User Profile Synchronization Service. Be sure that you turn it on on the server that you specified as the Profile Synchronization Instance when you created the service application.

**To turn on the User Profile Synchronization Service (SharePoint Server 2013 only)**

In Central Administration, under **System Settings**, select **Manage services on server**.

On the Server dropdown, select **Change Server**.

Select the server that you specified as the Profile Synchronization Instance.

In the **Service** list, select **Start** for the **User Profile Synchronization Service**.

Enter the credentials for the account shown, and select **OK**.

Note

This service can take several minutes or longer to start. Refresh the page occasionally until you see a status of **Started**.

Next, we'll configure the App Management Service.

**App Management Service**

If you're using SharePoint Server 2013, you need to turn on the App Management Service on at least one server in your farm.

**To turn on the App Management Service (SharePoint Server 2013 only)**

In Central Administration, under **System Settings**, select **Manage services on server**.

On the Server dropdown, select **Change Server**.

Select the server where you want to run the Managed Metadata Web Service.

In the **Service** list, select **Start** for the **App Management Service**.

You need to create an App Management service application.

**To create a App Management service application**

In Central Administration, under **Application Management**, select **Manage service applications**.

Select **New**, and then select **App Management Service**.

In the **Service Application Name** box, enter a name for the service application.

Under **Application Pool**, from the **Use existing application pool list**, select **SharePoint Web Services Default**.

Select **OK**.

Configure hybrid specific settings

### Configure hybrid specific settings

Hybrid uses the Microsoft SharePoint in Microsoft 365 Foundation Subscription Settings Service which is turned off by default in SharePoint Server. Use the following procedure to turn it on.

**To turn on the Microsoft SharePoint Foundation Subscription Settings Service (SharePoint Server 2013)**

In Central Administration, under **System Settings**, select **Manage services on server**.

For the **Microsoft SharePoint Foundation Subscription Settings Service**, select **Start**.

**To turn on the Microsoft SharePoint Foundation Subscription Settings Service** (SharePoint Server 2016 and SharePoint 2019)

In Central Administration, under **System Settings**, select **Manage services in this farm**.

For the **Microsoft SharePoint Foundation Subscription Settings Service**, select **Enable Auto Provision**

You must also have a Subscription Settings service application and proxy. These must be created by using Microsoft PowerShell. Use the example script provided at New-SPSubscriptionSettingsServiceApplication.

**Active Directory Domain Services synchronization connection**

For hybrid, we need a synchronization connection with Active Directory Domain Services for the User Profile service. If you haven't already configured one, use the following procedure to do so.

**To configure a synchronization connection**

In Central Administration, under **Application Management**, select **Manage service applications**.

Select the User Profile service application.

Select **Configure Synchronization Connections**.

Select **Create New Connection**.

In the **Connection Name** box, enter a name for the connection.

In the **Forest name** box, enter the name of your domain, for example, contoso.com.

Enter the user name and password of your domain administrator.

Select **Populate Containers**.

Expand the domain node, and select the check box for the object where your users are located.

Select **OK**.

Next, we'll verify some user properties in the User Profile Service.

The **Work email** user property needs to contain the email address that you configured for each user in Active Directory Directory Services. Also, the **User Principal Name** property must be mapped to the **userPrincipalName** attribute. Use the following procedure to verify both of these mappings.

**To verify user profile properties**

In Central Administration, under **Application Management**, select **Manage service applications**.

Select the User Profile service application.

Select **Manage User Properties**.

In the **Property Name** column, confirm that **User Principal Name** is mapped to **userPrincipalName** in the **Mapped Attribute** column.

In the **Property Name** column, confirm that **Work email** is mapped to **mail** in the **Mapped Attribute** column.

If either of these properties is not mapped as described, you need to update the mapping.

**Synchronize user profiles**

After you verify the user property mappings, we need to synchronize the UPN domain suffix and email address that we configured in Active Directory Domain Services. To do this, you have to start a profile synchronization.

**To start profile synchronization manually**

On the SharePoint in Microsoft 365 Central Administration website, in the **Application Management** section, select **Manage service applications**.

Select the User Profile service application.

On the **Manage Profile Service** page, in the **Synchronization** section, select **Start Profile Synchronization**.

On the **Start Profile Synchronization** page, select **Start Incremental Synchronization** to synchronize the profiles that you have updated.

Select **OK**.

Note

Refresh the **Manage Profile Service** page to view the profile synchronization status.

That's all the configuration that you need to do for the App Management Service. Next, move on to the next step in your roadmap.

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
