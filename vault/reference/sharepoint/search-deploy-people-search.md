---
title: "Deploy people search in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: search-deploy-people-search
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/search/deploy-people-search
family: search
documentKind: "install-set-up-deploy"
abstract: "Learn how to make classic people search work in SharePoint Server."
---

# Deploy people search in SharePoint Server - SharePoint Server

Note

Deploy people search in SharePoint Server

# Deploy people search in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

People search is a SharePoint Server feature that allows users to get information about people in the organization and to get links to the documents that they have authored. Users can access this feature by entering a search query in the enterprise Search Center search box and clicking the link for the **People** search vertical.

A search vertical filters search results so that only a certain subset of all relevant results is displayed. SharePoint Server provides four preconfigured search verticals: **Everything**, **People**, **Conversations**, and **Videos**. You can see the links for these search verticals in the Search Navigation Web Part, which is below the search box in the enterprise Search Center, as shown in the following screen shot.

When a user enters a search query in the search box and then clicks one of the search-vertical links, the Search system returns search results that correspond to that search vertical only. For example, if the user enters Microsoft Azure in the search box and then selects the **People** search-vertical link, the Search system returns only search results that are people in your organization who are involved with Microsoft Azure.

This article describes the prerequisites that you must complete to make people search possible, and addresses other considerations related to making people search work.

People search prerequisites

## People search prerequisites

People search has the following prerequisites:

A Search service application must be running in the farm. For more information, see Create and configure a Search service application in SharePoint Server 2016. The farm must also have a Search Center that uses the Enterprise Search Center template. For more information, see Create a Search Center site in SharePoint Server.

A Managed Metadata service application must be running in the farm. For more information, see Overview of managed metadata service applications in SharePoint Server 2013.

User profile synchronization must be configured in the farm. If this has not been done yet, at a minimum you must complete the following procedures that are described in Synchronize user and group profiles in SharePoint Server 2013:

Phase 0: Configure the farm

Phase 1: Start the User Profile synchronization service

For more information, see Overview of profile synchronization in SharePoint Server 2013 and Plan profile synchronization for SharePoint Server 2013.

Set up people search

## Set up people search

To set up people search, you must configure My Sites settings and configure crawling.

Configure My Sites settings

### Configure My Sites settings

You configure My Sites for a User Profile service application to specify the My Site host location and other settings. For more information, see Plan for My Sites in SharePoint Server and Configure My Site settings for the User Profile service application.

After you configure My Sites settings, the next step is to configure crawling.

Configure crawling

### Configure crawling

When you configure My Sites, the default content access account for search is automatically given **Retrieve People Data for Search Crawlers** permissions in the User Profile service application. If you want to use a different content access account to crawl the profile store, you must make sure that the account has permissions to crawl the profile store. Use the following procedure to grant access to the profile store for a different account.

To grant access to an account to crawl the profile store

### To grant access to an account to crawl the profile store

Verify that the user account that is performing this procedure is an administrator for the Search service application.

Start SharePoint Central Administration.

For Windows Server 2008 R2:

- Click **Start**, click **SharePoint**, and then click **SharePoint Central Administration**.

For Windows Server 2012:

On the **Start** screen, click **SharePoint Central Administration**.

If **SharePoint Central Administration** is not on the **Start** screen:

Right-click **Computer**, click **All apps**, and then click **SharePoint Central Administration**.

For more information about how to interact with Windows Server 2012, see Common Management Tasks and Navigation in Windows Server 2012.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the row that contains the User Profile service application, and then in the ribbon, click **Administrators**.

In the **Administrators for User Profile Service Application** dialog, in the **To add an account** box, type a user account in the form *domain\user name*.

Click **Add**.

In the **Permissions** list, select the **Retrieve People Data for Search Crawlers** check box.

Click **OK**.

After you give the account access to crawl the profile store, you must create a crawl rule to specify that you want to use that account when you crawl the profile store. Use the following procedure to create a crawl rule for this purpose.

To create a crawl rule to authenticate to the User Profile service application

## To create a crawl rule to authenticate to the User Profile service application

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the Search service application for which you want to create a crawl rule.

On the **Search Administration** page, in the Quick Launch, in the **Crawling** section, click **Crawl Rules**.

On the **Manage Crawl Rules** page, click **New Crawl Rule**.

In the **Path** section, in the **Path** box, type the start address for the User Profile service application in the form sps3://  *My_Site_host_URL*, where  *My_Site_host_URL* is the URL for the Web application where you deployed the My Sites site collection.

If the web application where you deployed the My Sites site collection uses Secure Sockets Layer (SSL), then type the start address in the form sps3s:// *My_Site_host_URL*.

Click **Use regular expression syntax for matching this rule** if you want to use regular expression syntax in the path.

In the **Crawl Configuration** section, select **Include all items in this path**.

In the **Specify Authentication** section, select **Specify a different content access account**.

In the **Account** box that appears, type the user account to which you gave access to the profile store in the form  *domain\user name*.

Type the password for the account that you specified in the **Password** and **Confirm Password** boxes.

Clear the **Do not allow Basic Authentication** check box only if you want to allow the user account credentials to be sent as plaintext.

Note

You should not clear the **Do not allow Basic Authentication** check box unless you are using SSL to encrypt the website traffic. For more information, see Plan for user authentication methods in SharePoint Server.

Click **OK**.

For more information, see Manage crawl rules in SharePoint Server.

When you configure My Sites, the starting URL to crawl the profile store (sps3:// *My_Site_host_URL* or sps3s://  *My_Site_host_URL*) is automatically added to the preconfigured content source **Local SharePoint Sites**. We recommend that you remove the URL of the profile store from the preconfigured content source and then create a separate content source to crawl only the profile store. This allows you to crawl the profile store on a different schedule from other crawls.

Use the following procedure to remove the URL of the profile store from the preconfigured content source.

To remove the profile store URL from the preconfigured content source

## To remove the profile store URL from the preconfigured content source

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click **Search Service Application**.

On the **Search Administration** page, in the Quick Launch, in the **Crawling** section, click **Content Sources**.

On the **Manage Content Sources** page, click the link to the preconfigured content source (**Local SharePoint sites**).

In the **Start Addresses** section, remove the URL for the profile store (sps3://  *My_Site_host_URL* or sps3s://  *My_Site_host_URL*, where  *My_Site_host_URL* is the URL for the web application where you deployed the My Sites site collection).

Click **OK**.

Use the following procedure to create a content source that specifies how to crawl the profile store. For more information, see Add, edit, or delete a content source in SharePoint Server.

To create a content source that specifies how to crawl the profile store

## To create a content source that specifies how to crawl the profile store

Verify that the user account that is performing this procedure is an administrator for the Search service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click **Search Service Application**.

On the **Search Administration** page, in the Quick Launch, in the **Crawling** section, click **Content Sources**.

On the **Manage Content Sources** page, click **New Content Source**.

On the **Add Content Source** page, in the **Name** section, type a name for this content source.

In the **Content Source Type** section, ensure that **SharePoint Sites** is selected.

In the **Start Addresses** section, type the start address in the form sps3://  *My_Site_host_URL*, where  *My_Site_host_URL* is the URL for the web application where you deployed the My Sites site collection.

If the web application where you deployed the My Sites site collection uses SSL, then type the start address in the form sps3s:// *My_Site_host_URL*.

In the **Crawl Settings** section, leave the default value of **Crawl everything under the host name for each start address**.

In the **Crawl Schedules** section, do the following:

Select **Enable Continuous Crawls** or **Enable Incremental Crawls**.

A continuous crawl automatically provides maximum freshness for the content source without an incremental crawl schedule. For more information, see Manage continuous crawls in SharePoint Server.

If you select **Enable Incremental Crawls**, create an incremental crawl schedule.

Optionally create a schedule for full crawls.

If you selected **Enable Incremental Crawls**, in the **Content Source Priority** section, select the priority for this content source.

Note

The **Content Source Priority** section doesn't appear when you specify the content source type as **SharePoint Sites** and you select **Enable Continuous Crawls**.

Click **OK**.

Add data for people search

## Add data for people search

To get the best results from people search, you should add as much information as you can by adding user profiles to the profile store and adding information to My Sites.

Add user profiles to the profile store

### Add user profiles to the profile store

Before you can obtain meaningful people search results, you must add user profiles to the User Profile service application. You can do this in the following ways:

Import user profiles from the directory service. For more information, see the following articles:

Plan profile synchronization for SharePoint Server 2013

Synchronize user and group profiles in SharePoint Server 2013

Configure profile synchronization by using SharePoint Active Directory Import in SharePoint Server

Copy user profiles from one farm to another by using the User Profile Replication Engine (UPRE). For more information, see Use UPRE to replicate user profiles across multiple farms in SharePoint Server 2013.

Add user profiles manually.

Synchronize with an external data source by using the Business Data Connectivity service. For more information, see Phase 3: Configure connections and import data from business systems in the article Synchronize user and group profiles in SharePoint Server 2013.

Important

For a test environment, we recommend that you do not synchronize the profile store to a directory service or other external data source that is in a production environment. Instead, create a copy of the directory service and synchronize the copy with the profile store.

Use the following procedure to view the user profiles in the User Profile service application.

**To view a list of user profiles in the User Profile service application**

Verify that the user account that is performing this procedure is an administrator for the User Profile service application.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

On the **Manage Service Applications** page, click the User Profile service application.

On the **Manage Profile Service** page, in the **People** section, click **Manage User Profiles**.

On the **Manage User Profiles** page, in the **Find profiles** box, type the name of the domain of which the users are members.

Don't type the fully qualified domain name. For example, if users are members of the Contoso.com domain, type **Contoso** in the **Find profiles** box.

Click **Find**.

Add information to My Sites

### Add information to My Sites

My Sites keep information in the User Profile service application databases. The User Profile service application stores much of the information that appears in results for people search. People search results become more useful as users add more information to their My Sites.

The first time that a user accesses their My Site, also known as their personal site, a My Site is created for them and a profile is automatically added to the User Profile service application.

To add information to a user's My Site, log on as a user for whom a user profile was created in the User Profile service application, and then go to that user's My Site. In the user's My Site, you can provide information about the user's expertise and interests. To see how the information that you added affects the people search results that appear, perform a crawl of the profile store, and then search on the user's name.

Crawl the profile store

## Crawl the profile store

You are now ready to crawl the profile store. For information about how to start the crawl, see Start, pause, resume, or stop a crawl in SharePoint Server.

Note

We recommend that you crawl the profile store and wait about two hours after the crawl finishes before you start the first crawl of the preconfigured content source (that is, local SharePoint sites). After the crawl of the profile store finishes, the search system generates a list to standardize people's names. This is so that when a person's name has different forms in search results, the results are displayed in a single group corresponding to one name. For example, all documents authored by Anne Weiler or A. Weiler or alias AnneW can be displayed in the search results in a result block that is labeled "Documents by Anne Weiler". Similarly, all documents authored by any of those identities can be displayed under the heading "Anne Weiler" in the refinement panel if "Author" is one of the categories there.

For information about how to view the status of a crawl, see Start, pause, resume, or stop a crawl for a content source.

See also

## See also

Administer the User Profile service in SharePoint Server

Overview of profile synchronization in SharePoint Server 2013

Manage user profile synchronization in SharePoint Server

Plan for My Sites in SharePoint Server

Create and configure a Search service application in SharePoint Server 2016

Manage crawling in SharePoint Server

Add, edit, or delete a content source in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
