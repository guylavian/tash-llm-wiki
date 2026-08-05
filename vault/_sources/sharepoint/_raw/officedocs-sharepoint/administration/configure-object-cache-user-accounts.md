---
title: "Configure object cache user accounts in SharePoint Server - SharePoint Server"
description: "Learn how to configure the Portal Super User and Portal Super Reader accounts that are used by the object cache in SharePoint Server."
ms.topic: how-to
---
Note

Configure object cache user accounts in SharePoint Server

# Configure object cache user accounts in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The object cache stores properties about items in SharePoint Server. Items in this cache are used by the publishing feature when it renders web pages. The goals of the object cache are to reduce the load on the computer on which SQL Server is running, and to improve request latency and throughput. The object cache makes its queries as one of two out-of-box user accounts: the Portal Super User and the Portal Super Reader. These user accounts must be properly configured to ensure that the object cache works correctly. The Portal Super User account must be an account that has Full Control access to the web application. The Portal Super Reader account must be an account that has Full Read access to the web application.

Important

The Portal Super User and Portal Super Reader accounts must be separate accounts, and they must not be accounts that will ever be used to log in to the site.

This article explains why these object cache user accounts must be configured and describes how to configure the accounts. For information about the object cache, see Cache settings operations in SharePoint Server.

In SharePoint Server, querying for items is linked with the user account that makes the query. Various parts of the publishing feature make queries for which the results are cached in the object cache. These results are cached based on the user making the query. To optimize the cache hit rate and memory requirements, the queries must be based on whether a user can see draft items. When a publishing control requests the object cache to make a query to get data for the control, the cache makes the query, not as the user making the request, but instead it makes the query twice: once as the Portal Super User account and once as the Portal Super Reader account. The results of these two queries are stored in the object cache. The results for the Portal Super User account include draft items, and the results for the Portal Super Reader account include only published items. The object cache then checks the access control lists (ACLs) for the user who initiated the request and returns the appropriate results to that user based on whether that user can see draft items. By adding the Portal Super User and Portal Super Reader accounts to the web application, the cache must store results for only two users. This increases the number of results that are returned for a query and decreases the amount of memory that is needed to store the cache.

By default, the Portal Super User account is the site's System Account, and the Portal Super Reader account is NT Authority\Local Service. There are two main issues with using the out-of-box accounts.

The first issue is that some items get checked out to System Account, so when a query that includes these items is made, the checked out version of the item is returned instead of the latest published version. This is a problem because it is not what a user would expect to have returned, so the cache has to make a second query to fetch the correct version of the file. This negatively affects server performance for every request that includes these items. The same problem would occur for any user who has items checked out, if that user's account was set to be the Portal Super User account. This is why the accounts configured to be the Portal Super User and the Portal Super Reader should not be user accounts that are used to log into the site. This ensures that the user does not inadvertently check items out and cause problems with performance.

The default Portal Super Reader account is NT Authority\Local Service, which is not correctly resolved in a claims authentication application. As a result, if the Portal Super Reader account is not explicitly configured for a claims authentication application, browsing to site collections under this application will result in an "Access Denied" error, even for the site administrator. This error will occur on any site that uses any feature that explicitly uses the object cache, such as the SharePoint Server Publishing Infrastructure, metadata navigation, the Content Query Web Part, or navigation.

Configure object cache user accounts by using Central Administration and Windows PowerShell

## Configure object cache user accounts by using Central Administration and Windows PowerShell

You can configure the user accounts for the object cache by the the SharePoint Central Administration website and Microsoft PowerShell. You must first create the accounts in Central Administration and then add the accounts to the web application by using PowerShell. You must add the user accounts to each web application.

Caution

At the end of this procedure, you must reset Internet Information Services (IIS) to apply the changes to the web application. Be sure to perform this procedure when there will be minimal disruption to users that are connected to the site. For more information about IISReset, see IIS Reset Activity.

**To create the user accounts by using Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.

In Central Administration, in the **Application Management** section, click **Manage web applications**, and then click the name of the web application that you want to configure.

On the **Web Applications** tab, in the **Policy** group, click **User Policy**.

In the Policy for Web Application window, click **Add Users**.

From the **Zones** list, select **All zones**, and then click **Next**.

In the **Users** box, type the user name for the Portal Super User account and then click **Check Names** to ensure that the account name can be resolved by the authentication providers on the application server.

In the **Choose Permissions** section, check the **Full Control - Has full control** box and then click **Finish**.

Repeat Steps 5 through 7 for the Portal Super Reader account.

In the **Choose Permissions** section, check the **Full Read - Has full read-only access** box.

Click **Finish**.

Make note of how the names for the Object Cache Super Reader and Object Cache Super User accounts are displayed in the **User Name** column. The displayed strings will be different depending on whether you are using claims authentication for the web application.

**To add the user accounts to the web application by using Microsoft PowerShell**

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running PowerShell cmdlets.

Add memberships that are required beyond the minimums above.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and Add-SPShellAdmin.

- Paste the following code into a text editor, such as Notepad:

```
$wa = Get-SPWebApplication -Identity "<WebApplication>"
$wa.Properties["portalsuperuseraccount"] = "<SuperUser>"
$wa.Properties["portalsuperreaderaccount"] = "<SuperReader>"
$wa.Update()
```

- Replace the following placeholders with values:

*<WebApplication>* is the name of the web application to which the accounts will be added.

*<SuperUser>* is the account to use for the Portal Super User account as you saw it displayed in the **User Name** column  mentioned in Step 11 of the previous procedure.

*<SuperReader>* is account to use for the Portal Super Reader account as you saw it displayed in the **User Name** column  mentioned in Step 11 of the previous procedure.

Save the file, naming it SetUsers.ps1.

Note

You can use a different file name, but you must save the file ANSI-encoded as a text file whose extension is **.ps1**.

Close the text editor.

Open **SharePoint Management Shell**.

Change to the directory where you saved the file.

At the PowerShell command prompt, type the following command: ./SetUsers.ps1

Reset Internet Information Services (IIS). For more information about IISReset, see Start or Stop the Web Server (IIS 8).

See also

## See also

Concepts

#### Concepts

Cache settings operations in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
