---
title: "Add apps for SharePoint to a SharePoint site - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-add-apps-for-sharepoint-to-a-sharepoint-site
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/add-apps-for-sharepoint-to-a-sharepoint-site
family: administration
documentKind: "how-to"
abstract: "Site owners can add apps for SharePoint to SharePoint sites so that they and other users of the site can use the app."
---

# Add apps for SharePoint to a SharePoint site - SharePoint Server

Note

Add apps for SharePoint to a SharePoint site

# Add apps for SharePoint to a SharePoint site

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Site owners can add apps for SharePoint from the SharePoint Store or an App Catalog to their sites. Adding an app installs an instance of that app to the site. This article covers how to add apps to your sites.

Be sure you've configured your environment for SharePoint apps before you get started.

Add apps for SharePoint to SharePoint sites

## Add apps for SharePoint to SharePoint sites

Site owners can add apps for SharePoint from the following sources to their sites:

from the list of apps already available for a site (default apps, such as standard lists and libraries, and apps that have been purchased already).

from the App Catalog.

from the SharePoint Store.

Note that a user logged in as the system account cannot install an app.

When you add an app for SharePoint, the app requests permissions that it needs to function (for example, access to Search, or to create a list). If you don't have those permissions, the app won't install. Contact your administrator to get the needed permissions or have someone with those permissions add the app.

The following procedures provide steps for adding apps from these sources.

**To add an app from the list of available apps in a site**

Verify that the user account that is performing this procedure is a member of the site Owners group.

On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**

If the Get started with your site control does not appear on the home page, click the **Settings** icon, and click **View Site Contents**, and then on the **Site Contents** page, click **Add an App**.

In the Your Apps list, click the app you want to add.

Follow the instructions to Trust the app (if it is a custom component) or Name the app (if it is a SharePoint component).

The app for SharePoint is added and appears in the **Apps** section of your Site Contents list.

**To add an app from an App Catalog**

Verify that the user account that is performing this procedure is a member of the site Owners group.

On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**

If the Get started with your site control does not appear on the home page, click the Settings icon, and click **View Site Contents**, and then on the Site Contents page, click **Add an App**.

Click **From** *Name*.

Where *Name* is the name of your organization's App Catalog. For example, "From Contoso".

Tip

Apps marked as Featured in the App Catalog will also appear in the main list of Apps.

Click the app you want to add.

In the Grant Permission to an App dialog, if you trust the app, click **Allow Access**.

The app for SharePoint is added and appears in Apps section of your Site Contents list.

**To add an app from the SharePoint Store**

Verify that the user account that is performing this procedure is a member of the site Owners group.

On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**

If the Get started with your site control does not appear on the home page, click the Settings icon, and click **View Site Contents**, and then on the Site Contents page, click **Add an App**.

Click **SharePoint Store**.

Browse the SharePoint Store to find an app that you want.

Click the app you want to add.

Click Details, and then click **Buy It**.

Follow the steps to log in and purchase the app, if required.

In the **Grant Permission to an App** dialog, if you trust the app, click **Allow Access**.

The app for SharePoint is added and appears in the Apps section of your Site Contents list.

See also

## See also

Concepts

#### Concepts

Install and manage apps for SharePoint Server

Other Resources

#### Other Resources

Import-SPAppPackage

Install-SPApp

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
