---
title: "Enable SharePoint home page in SharePoint Server 2019 farms - SharePoint Server"
type: reference
domain: sharepoint
slug: sites-enable-sharepoint-home-page-in-sharepoint-server-2019-farms
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/sites/enable-sharepoint-home-page-in-sharepoint-server-2019-farms
family: sites
documentKind: "how-to"
abstract: "How to enable SharePoint home page in SharePoint Server 2019 farms."
---

# Enable SharePoint home page in SharePoint Server 2019 farms - SharePoint Server

Note

Enable SharePoint home page in SharePoint Server 2019 farms

# Enable SharePoint home page in SharePoint Server 2019 farms

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

What is SharePoint home?

## What is SharePoint home?

SharePoint home is a modern UX page, available out-of-box- in SharePoint Server 2019 with appropriate configurations, where a user can easily find and access their SharePoint sites and portals. It is a personalized experience that allows users to view activities in the sites they follow, discover news across their sites and much more. SharePoint home replaces the Sites.aspx experience in SharePoint Server 2016. The Sites tile in the app launcher is also renamed as SharePoint. To access SharePoint home, click the **App Launcher** and then click **SharePoint**.

A user can also click on the word “SharePoint” in the top bar to visit SharePoint home page.

The SharePoint home page experience includes the following features:

**Search box:** When a user clicks in the search box a list of *best-match* sites is available in the drop-down list to provide a “zero-time search” experience.

**Featured links:** These are links that are important and useful for your organization. Anyone who is an admin of the My Site Host site can set these links.

**Create Site:** With the Self-Service Site Creation (SSSC) feature you can give users the ability to create a new modern site collection, Communication or Team sites. For more information, see Configure self-service site creation in SharePoint Server 2019.

**News from sites:** Display recent news from Following and Suggested sites.

**Following:** Display sites that you are following in a card format. Users will see top activities in those sites and can unfollow sites.

**Suggested:** These sites that have the most activity that you’re not following.

For more information, see the “2019” section in Find news, sites, and portals in SharePoint.

Requirements to enable the SharePoint home page

## Requirements to enable the SharePoint home page

Managed Metadata Service Application

Search Service Application

Enterprise Search Center site

My Site Host site

User Profile Service Application

Import profiles from Active Directory, if required

Distributed Cache (Optional) Note that content following normally requires distributed cache. SharePoint home will show followed sites and may not require distributed cache directly. If your SharePoint home doesn't show content following, then deploy distributed cache in your farm.

Note

Distributed Cache is required to be running on at least one SharePoint Server in the farm.

With this configuration in-place, the App Launcher and SharePoint Home Page button will appear.

SharePoint home page in a hybrid environment

## SharePoint home page in a hybrid environment

SharePoint home page works best when Search and List of Followed sites are stored in a user’s My Site. In a SharePoint Server hybrid environment, the SharePoint home page is not rendered on SharePoint Server 2019. Instead, when you click SharePoint from the App Launcher, you’re re-directed to the SharePoint home page in the cloud.

Troubleshooting SharePoint home page

## Troubleshooting SharePoint home page

If you find any issues with the SharePoint home page, first check items in the following list.

SharePoint home page looks different for users. This is expected and depends on user activity and timing of the changes.

Check the User Profile Service application to make sure it's provisioned, started, and working.

Check that the affected user has a working user profile.

Ensure the SharePoint home page site collection is configured with a pointer to the Enterprise Search Center.

Check the Search Service application and crawling status.

If you're running Distributed Cache, check for any service issues.

When following a site that isn't shown on the SharePoint home page, check that “following” is functional in your farm.

See also

## See also

Concepts

#### Concepts

Create a User Profile service application in SharePoint Server

Configure profile synchronization by using SharePoint Active Directory Import in SharePoint Server

Manage the Distributed Cache service in SharePoint Server

Congiure self-service site creation in SharePoint Server 2019

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
