---
title: "Hybrid site following - SharePoint Server"
description: "When a user follows a site, a link to that site is added to the user's Followed Sites list. If you're using both SharePoint Server and SharePoint in Microsoft 365, your users will have different followed lists for sites in each location. With SharePoint hybrid, you can consolidate the info from both locations into the SharePoint in Microsoft 365 list in Microsoft 365."
ms.topic: article
---
Note

Hybrid site following

# Hybrid site following

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When a user follows a site, a link to that site is added to the user's Followed Sites list. If you're using both SharePoint Server and SharePoint in Microsoft 365, your users will have different followed lists for sites in each location. With SharePoint hybrid, you can consolidate the info from both locations into the SharePoint in Microsoft 365 list in Microsoft 365.

How hybrid site following works

## How hybrid site following works

When you enable hybrid site following:

The **Sites** link in a SharePoint Server site is redirected to Office 365 (SharePoint Server 2013).

The **Sites** tile in the app launcher  is redirected to Microsoft 365 (SharePoint Server 2016 and SharePoint Server 2019).

When a user follows a site in SharePoint Server, it's added to the followed list in both SharePoint Server and Microsoft 365.

While the SharePoint Server followed list continues to be updated, users are directed to the followed list in Microsoft 365, which contains followed sites from both locations.

The SharePoint in Microsoft 365 newsfeed functionality is unaffected. Users will continue to have separate newsfeeds in SharePoint Server and Microsoft 365, and each will show activities for sites and documents for SharePoint Server and Microsoft 365, respectively. Also, follow documents functionality remains unaffected, and follow people functionality remains in SharePoint Server only.

Existing followed sites lists in SharePoint Server aren't migrated to Microsoft 365 when you turn on this feature (though any sites in the Microsoft 365 list will remain there). Users will have to follow their SharePoint Server sites again once the feature is turned on.

Setting up hybrid site following

## Setting up hybrid site following

Hybrid site following is part of Hybrid Sites Features, and is available on both SharePoint Server 2013 and SharePoint Server 2016. For info about the other features included with Hybrid Sites Features, see Hybrid sites features and OneDrive.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
