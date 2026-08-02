---
title: "User Profile service overview - SharePoint Server"
type: reference
domain: sharepoint
slug: install-user-profile-service-overview
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/user-profile-service-overview
family: install
documentKind: "interactive-tutorial"
abstract: "Learn about the User Profile service architecture and how SharePoint Server uses it to enable features such as audiences and My Sites."
---

# User Profile service overview - SharePoint Server

Note

User Profile service overview

# User Profile service overview

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365.

The User Profile service stores information about users in a central location. It enables My Sites, social computing features such as social tagging and newsfeeds, and creating and distributing profiles across multiple sites and farms. It is also required by most SharePoint hybrid scenarios.

Learn about Managing user profiles in the SharePoint admin center in Microsoft 365.

The User Profile service application

## The User Profile service application

The User Profile service application in SharePoint Server provides a central location where service administrators configure and administer the following features:

**User profiles** - contain detailed information about people in an organization. A user profile organizes and displays all of the properties related to each user, together with social tags, documents, and other items related to that user.

**Profile synchronization** - provides a reliable way to synchronize groups and user profile information that is stored in the SharePoint Server profile database together with information that is stored in Active Directory Domain Services.

In SharePoint Server 2013, you can synchronize directly with other directories across the enterprise.

In SharePoint Server 2016, you can synchronize with other directories by using an external identity manager such as Microsoft Identity Manager 2016.

**Audiences** - enables organizations to target content to users based on their job or task, as defined by their membership in a SharePoint Server group or distribution list, by the organizational reporting structure, or by the public properties in their user profiles.

**My Site Host** - a dedicated site for hosting My Sites. A My Site Host is needed in order to deploy the social features of SharePoint Server.

**My Site** - a personal site that gives users in your organization a central location to manage and store documents, links, and information about colleagues.

**Social tags and notes** - enables users to add social tags to documents, to other SharePoint Server items, and to other items, such as external web pages and blog posts. Users can also leave notes on profile pages of a My Site or any SharePoint Server page. Administrators can delete all tags for employees when they leave the company or remove a tag they do not want.

These features make it possible for users in an organization to share information and to stay informed about what happens within the organization. Social tags, for example, enable users to tag and track the information in which they are most interested. Users can be alerted when people with which they work author new blog posts or when there is a change in organizational metadata.

Like other service applications in SharePoint Server, farm administrators can delegate the administration of all or part of the User Profile service application to one or more service application administrators. This delegation enables the User Profile service application to be managed by the appropriate business group. One administrator can manage all areas of the User Profile service application or areas can be isolated and managed by different administrators. For example, one administrator can manage My Sites while a different administrator manages social tags and notes. The User Profile service application can be restricted and made available only to certain departments or sets of sites based on business need, security restrictions, and budgets.

User profile databases

## User profile databases

When you create a User Profile service application, SharePoint Server creates three databases for storing user profile information and associated data:

**Profile database** - used to store user profile information.

**Synchronization database** - used to store configuration and staging information for synchronizing profile data from external sources such as the Active Directory Domain Services (AD DS).

**Social tagging database** - used to store social tags and notes created by users. Each social tag and note is associated with a profile ID.

Related service applications

## Related service applications

The User Profile service application relies on other service applications to implement the full range of social computing features in SharePoint Server. These related service applications include the following components:

**Managed metadata service** - makes it possible to use managed metadata and share content types across site collections and web applications. Configure the managed metadata service before you configure the User Profiles service application.

**Search Service application** - needed to enable the People Search feature.

See also

## See also

Concepts

#### Concepts

Administer the User Profile service in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
