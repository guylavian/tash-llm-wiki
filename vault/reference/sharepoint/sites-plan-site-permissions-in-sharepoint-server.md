---
title: "Plan site permissions in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: sites-plan-site-permissions-in-sharepoint-server
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/sites/plan-site-permissions-in-sharepoint-server
family: sites
documentKind: "concept-article"
abstract: "Learn about how to plan site permissions for SharePoint Server to provide secure access to sites and content."
---

# Plan site permissions in SharePoint Server - SharePoint Server

Note

Plan site permissions in SharePoint Server

# Plan site permissions in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article helps you plan access control at the site collection, site, subsite, and site content (list or library, folder, item or document) levels.

This article does not address planning the security of your entire server or server farm. For more information about planning other aspects of security, such as authentication methods and authentication modes, see Plan authentication in SharePoint Server.

Plan for site permissions

## Plan for site permissions

When you create permissions, you must balance the ease of administration and performance against the requirement to control access to individual items. If you use fine-grained permissions extensively, you will spend more time managing the permissions, and users may experience slower performance when they try to access site content.

Use the following guidelines to plan site permissions:

Follow the principle of least-privileged: Users should have only the permission levels or individual permissions they must have to perform their assigned tasks.

Use standard groups (such as Members, Visitors, and Owners) and control permissions at the site level.

Make most users members of the Members or Visitors groups. By default, users in the Members group can contribute to the site by adding or removing items or documents, but cannot change the structure, site settings, or appearance of the site. The Visitors group has read-only access to the site, which means that they can see pages and items, and open items and documents, but cannot add or remove pages, items, or documents.

Limit the number of people in the Owners group. Only those users that you trust to change the structure, settings, or appearance of the site should be in the Owners group.

- Use permission levels instead of assign individual permissions.

Note

You can create additional SharePoint groups and permission levels if that you must have more control over the actions that the users can take. For example, if you do not want the Read permission level on a specific subsite to include the Create Alerts permission, break the inheritance and customize the Read permission level for that subsite. >  SharePoint Foundation 2013 and SharePoint Server use **Check Permissions** to determine a user or group's permissions on all resources in a site collection. You can now find both the user's directly assigned permissions and the permissions assigned to any groups of which the user is a member by checking permissions for a specific site or site content.

Plan for permission inheritance

## Plan for permission inheritance

It is much easier to manage permissions when there is a clear hierarchy of permissions and inherited permissions. It becomes more difficult when some lists in a site have fine-grained permissions applied, and when some sites have subsites with unique permissions and others with inherited permissions. As much as possible, arrange sites and subsites, and lists and libraries so they can share most permissions. Separate sensitive data into their own lists, libraries, or subsites.

For example, it's much easier to manage a site that has permission inheritance as described in the following table.

| **Securable object** | **Description** | **Unique or inherited permissions** |
| --- | --- | --- |
| SiteA | Group home page | Unique |
| SiteA/SubsiteA | Sensitive group | Unique |
| SiteA/SubsiteA/ListA | Sensitive data | Unique |
| SiteA/SubsiteA/LibraryA | Sensitive documents | Unique |
| SiteA/SubsiteB | Group shared project information | Inherited |
| SiteA/SubsiteB/ListB | Non-sensitive data | Inherited |
| SiteA/SubsiteB/LibraryB | Non-sensitive documents | Inherited |

However, it is not as easy to manage a site that has permission inheritance as shown in the following table.

| **Securable object** | **Description** | **Unique or inherited permissions** |
| --- | --- | --- |
| SiteA | Group home page | Unique |
| SiteA/SubsiteA | Sensitive group | Unique |
| SiteA/SubsiteA/ListA | Non-sensitive data | Unique, but same permissions as SiteA |
| SiteA/SubsiteA/LibraryA | Non-sensitive documents, but with one or two sensitive documents | Inherited, with unique permissions at the document level |
| SiteA/SubsiteB | Group shared project information | Inherited |
| SiteA/SubsiteB/ListB | Non-sensitive data, but with one or two sensitive items | Inherited, with unique permissions at the item level |
| SiteA/SubsiteB/LibraryB | Non-sensitive documents, but with a special folder that contain sensitive documents | Inherited, with unique permissions at the folder and document level |

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
