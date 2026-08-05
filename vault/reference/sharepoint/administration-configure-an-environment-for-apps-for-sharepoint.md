---
title: "Configure an environment for apps for SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-an-environment-for-apps-for-sharepoint
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-an-environment-for-apps-for-sharepoint
family: administration
documentKind: "how-to"
abstract: "Configure domain names, service applications, and URLs for apps for SharePoint Server."
---

# Configure an environment for apps for SharePoint Server - SharePoint Server

Note

Configure an environment for apps for SharePoint Server

# Configure an environment for apps for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

To enable users to install and use apps for SharePoint in their sites, configure your environment to support them. This article describes how to configure your environment to support apps. Use the Plan for apps for SharePoint Server article to review options and determine the values to use for configuration settings in this article.

Learn about managing apps using the App Catalog for SharePoint in Microsoft 365.

Before you begin

## Before you begin

Purchase a domain name from a domain name provider for your apps, for example, ContosoApps.com.

Ensure that you are a member of the Farm Administrators group to perform the steps in this article. For some steps, you must also be a domain administrator.

If you have a multi-tenant environment, you need to do some steps by using Microsoft PowerShell. Make sure you have permissions to administer SharePoint Server using Windows PowerShell.

Configure the domain names in DNS

## Configure the domain names in DNS

You must configure a new domain in Domain Name Services (DNS) to host the apps. To help improve security, the domain name should not be a subdomain of the domain that hosts the SharePoint Server sites. For example, if the SharePoint Server sites are at Contoso.com, consider ContosoApps.com instead of App.Contoso.com as the domain name.

When an app is provisioned, it provisions a unique DNS domain name (for example, Apps- *12345678ABCDEF*.ContosoApps.com, where  *12345678ABCDEF* is a unique identifier for the app). You need a wildcard Canonical Name (CNAME) entry for your DNS domain to support these unique names.

Depending on your configuration (for example, if you are using WINS forward lookup), you might have to create a new forward lookup zone first, or you can start with a wildcard CNAME entry in the same zone as the SharePoint Server site domain. In the following procedures, you create a forward lookup zone, and then create a wildcard alias record for the DNS domain name that allows for individual apps to create unique domain names within your app domain. In these procedures, we use DNS Manager for Windows Server 2012 R2. If you have a different type of DNS server, follow the procedures in the documentation for that server type.

**To create a forward lookup zone for the app domain name**

Verify that the user account that performs this procedure is a domain administrator on the domain controller.

Click **Start**, point to **Administrative Tools**, and then click **DNS**.

In DNS Manager, right-click **Forward Lookup Zones**, and then click **New Zone…**.

In the New Zone Wizard, click **Next**.

In the **Zone Type** page, accept the default of **Primary zone**, and then click **Next**.

In the **Active Directory Zone Replication Scope** page, select the appropriate replication method for your environment (the default is **To all DNS servers in this domain**), and then click **Next**.

In the **Zone Name** page, in the **Zone name** box type the name for your new app domain name (for example, ContosoApps.com), and then click **Next**.

On the **Dynamic Update** page, select the appropriate type of dynamic updates for your environment (the default is **Do not allow dynamic updates**), and then click **Next**.

On the **Completing the New Zone Wizard** page, review the settings, and then click **Finish**.

You have now created a forward lookup zone (and a domain name) to use for apps in your environment.

**To create a wildcard Alias (CNAME) record for the new domain name**

Verify that the user account that performs this procedure is a domain administrator on the domain controller.

In DNS Manager, under Forward Lookup Zones, right-click the new app domain name, and then click **New Alias (CNAME)**.

In the New Resource Record dialog, in the **Alias name (uses parent domain if left blank)** box, type *.

The Fully qualified domain name (FQDN) box displays *. followed by the domain name that you created for apps. For example, *.ContosoApps.com or *.Contoso-Apps.com.

Next to the **Fully qualified domain name (FQDN) for target host** box, type the FQDN of the server that hosts the SharePoint Server sites.

For example, SharePoint.Contoso.com.

Or:

Next to the **Fully qualified domain name (FQDN) for target host** box, click **Browse** and navigate to the Forward Lookup Zone for the domain that hosts the SharePoint Server sites.

For example, Contoso.com.

And then navigate to the record that points to the server that hosts the SharePoint Server site.

For example, SharePoint.

**New Resource Record dialog shows the wildcard alias for the app domain and the FQDN of the server that hosts the SharePoint sites.**

Click **OK**.

You can verify the new domain name and alias by pinging them.

**To verify the new domain name**

Verify that the user account that is performing this procedure is a domain administrator on the domain controller.

Click **Start**, and then click **Command Prompt**.

At the command prompt, type **ping** followed by a subdomain of the domain that you created, and then press **ENTER**.

For example, **ping Apps-12345678ABCDEF.contosoapps.com**

If the ping command returns the correct IP address, then your wildcard for the domain name was configured successfully.

Create a new wildcard SSL certificate

## Create a new wildcard SSL certificate

If you are using Secure Sockets Layer (SSL) for the SharePoint Server sites in your environment, or if you use any apps that use data external to the SharePoint Server sites, you should use SSL for your apps. To use SSL, you create an SSL certificate for your app domain (for example, ContosoApps.com).

The domain should be added in the form of a wildcard (for example, *.ContosoApps.com). You need a wildcard certificate instead of individual certificates because each installed app has its own subdomain.

In order to allow support for SSL offloading with SharePoint Server App Domains, enable support for multiple app domains by using the following Microsoft PowerShell commands:

```
$contentService = [Microsoft.SharePoint.Administration.SPWebService]::ContentService
$contentService.SupportMultipleAppDomains = $true
$contentService.Update()
iisreset
```

Configure the Subscription Settings and App Management service applications

## Configure the Subscription Settings and App Management service applications

Apps rely on the App Management and Microsoft SharePoint Foundation Subscription Settings service applications. Use the following procedures to configure them.

**To turn on the Microsoft SharePoint Foundation Subscription Settings Service**

In Central Administration, under **System Settings**, click **Manage services in this farm**.

For the **Microsoft SharePoint Foundation Subscription Settings Service**, click **Enable Auto Provision**

Next, create a Subscription Settings service application and proxy by using Microsoft PowerShell. Use the example script provided at New-SPSubscriptionSettingsServiceApplication.

You also need an App Management service application. The following procedures provide the steps to configure it.

**To create a App Management service application**

In Central Administration, under **Application Management**, click **Manage service applications**.

Click **New**, and then click **App Management Service**.

Type a name for the service application in the **Service Application Name** box.

Under **Application Pool**, choose **SharePoint Web Services Default** from the **Use existing application pool list**.

Click **OK**.

Specify the app domain and app prefix

## Specify the app domain and app prefix

In this section, you specify the app domain and app prefix to use for apps in your environment. The app URL points to your app domain and a prefix that determines how each app is named.

Use the following procedure to configure app URLs.

**To configure app URLs**

In Central Administration, click **Apps**.

On the **Apps** page, click **Configure App URLs**.

In the **App domain** box, type the isolated domain that you created for hosting apps (for example, ContosoApps.com).

In the **App prefix** box, type a name to use for the URL prefix for apps.

(For example, you could use "apps" as the prefix, and you would see a URL for each app such as "apps- *12345678ABCDEF*.ContosoApps.com".)

Click **OK**.

If you will install apps and you have changed the App prefix (also known as the site subscription name), you must perform more steps that involve restarting the World Wide Web Publishing Service (WWW Service) that hosts the apps.

Important

Restarting the WWW Service will also restart the IIS Admin Service and the Windows Process Activation Service. This will also shut down all Web sites and applications that depend on these services and they may lose existing state and will be unavailable until the services successfully restart. You should plan to perform these steps during a planned maintenance time. >  To complete the App prefix rename tasks, perform these steps: >  Stop the SharePoint Timer service. >  Restart the World Wide Web Publishing Service that hosts the apps. >  Start the SharePoint Timer service.

Multi-tenant settings (Optional)

## Multi-tenant settings (Optional)

If you host multiple tenants in your environment, you must use Microsoft PowerShell to configure app URLs for each tenant. Use the following procedure to configure them.

**To configure app URLs by using Windows PowerShell**

Open the SharePoint Management Shell.

At the Microsoft PowerShell command prompt, type the following commands and press **ENTER** after each one:

```
Set-SPAppDomain <appDomain>

Set-SPAppSiteSubscriptionName -Name "app" -Confirm:$false
```

Where:

- *<appDomain>* is the domain name that you created.

If you will install apps and you have changed the App prefix (also known as the site subscription name), you must perform additional steps that involve restarting the World Wide Web Publishing Service (WWW Service) that hosts the apps.

Important

Restarting the WWW Service will also restart the IIS Admin Service and the Windows Process Activation Service. This will also shut down all Web sites and applications that depend on these services and they may lose existing state and will be unavailable until the services successfully restart. You should plan to perform these steps during a planned maintenance time. >  To complete the App prefix rename tasks, perform these steps: >  Stop the SharePoint Timer service. >  Restart the World Wide Web Publishing Service that hosts the apps. >  Start the SharePoint Timer service.

For more information, see Set-SPAppSiteSubscriptionName and Set-SPAppDomain.

Configure the Internet-facing endpoints feature (Optional)

## Configure the Internet-facing endpoints feature (Optional)

The SharePoint Store contains apps for SharePoint intended for use with sites that require Internet-facing endpoints. By default, these apps are not available (greyed out and cannot be purchased) because they are incompatible with most sites. However, if your farm is configured to allow internet-facing end points, you can turn on the Internet-facing endpoints feature to show these apps in the SharePoint Store. You turn on this feature in Central Administration.

**To configure Internet-facing endpoints for apps**

In Central Administration, click **Application Management**.

On the **Application Management** page, click **Manage Web applications**.

On the **Manage Web Applications** page, select the web application that you want to change.

On the ribbon, click **Manage Features**.

In the feature list, next to **Apps that require accessible internet facing endpoints**, click **Activate**.

Click **OK**.

In some cases, for example, when you have an on-premises SharePoint Server farm where updates are installed infrequently, you will need to run a cmdlet to update the URL used to point to the SharePoint Store:

```
Set-SPAppStoreConfiguration -Url http://office.microsoft.com -Enable $true
```

See also

## See also

Concepts

#### Concepts

Plan for apps for SharePoint Server

Install and manage apps for SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
