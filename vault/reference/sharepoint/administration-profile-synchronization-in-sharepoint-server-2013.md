---
title: "Overview of profile synchronization in SharePoint Server 2016 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-profile-synchronization-in-sharepoint-server-2013
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/profile-synchronization-in-sharepoint-server-2013
family: administration
documentKind: "interactive-tutorial"
abstract: "Learn about profile synchronization, also known as profile sync,in SharePoint Server 2016."
---

# Overview of profile synchronization in SharePoint Server 2016 - SharePoint Server

Note

Overview of profile synchronization in SharePoint Server 2016

# Overview of profile synchronization in SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

A user profile is a collection of properties that describes a SharePoint user. Features such as My Sites and People Search use user profiles to provide a rich, personalized experience for the users in your organization. You can create user profiles by importing data from directory services, such as Active Directory Domain Services (AD DS). You can augment user profiles by importing data from business systems, such as SAP or SQL Server. The process of importing profile data from external systems and writing data back to these systems is called profile synchronization.

Options for profile synchronization

## Options for profile synchronization

Previous versions of SharePoint Server had a built-in copy of ForeFront Identity Manager (FIM) that ran inside SharePoint Server. That version of FIM powered the User Profile Synchronization for products like SharePoint Server 2010 and SharePoint Server 2013. But in SharePoint Server 2016, FIM has been removed in favor of Microsoft Identity Manager (MIM), which is the successor to the FIM technology. MIM is a separate server technology (not built-in to SharePoint Server). That means, if you have MIM running in your company, more than one SharePoint Server 2016 farm can rely upon it.

It's also important to note, here, that Active Directory Import (sometimes called Active Directory Direct Import) is still included with SharePoint Server 2016, and is a User Profile Synchronization alternative that does not need a separate server installation. This means that SharePoint Server 2016 offers two options for User Profile Sync.

A third option, if you're using Microsoft 365, is to use hybrid profiles as part of a SharePoint hybrid deployment. With hybrid profiles, SharePoint Server 2016 on-premises profiles aren't necessary, as users are automatically redirected to their profile in SharePoint in Microsoft 365.

Which option is right for you?

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Microsoft Identity Manager 2016** | **Active Directory Import** | **Hybrid profiles** |
| **Pros** | Supports customized import.  
  Supports bidirectional flow.  
  Imports user profile photos automatically.  
  Supports non-Active Directory LDAP sources.  
  Supports multi-forest scenarios. | Very fast, high performance.  
  Configurable inside of Central Administration. (Less complex.) | Single profile for users who use both SharePoint Server and SharePoint in Microsoft 365.  
  Can include Delve, depending on your Office 365 configuration. |
| **Cons** | A separate MIM server is recommended for use with your SharePoint Server farm.  
  Customization can lead to more complex architecture, deployment, and management. | Import is unidirectional (changes go from AD DS to SharePoint Server).  
  Import from a single Active Directory forest only.  
  Does not import user photos automatically.  
  Supports Active Directory LDAP only.  
  Multi-forest scenarios are not supported. | Can require a custom solution to move on-premises properties to Microsoft 365. |

These three options are mutually exclusive. Each is further described in the following sections.

Importing profiles by using SharePoint Active Directory Import

### Importing profiles by using SharePoint Active Directory Import

You can create new profiles and import profile properties by synchronizing with AD DS by using SharePoint Active Directory Import. When you do this, SharePoint Server 2016 does the following:

Creates a user profile for each new user in the AD DS containers that are being synchronized, and fills in the properties of each new profile with data from the directory service.

Deletes the profile of any user who was removed from the directory service.

For properties that are being imported, updates the property in the SharePoint user profile if the corresponding value in AD DS has changed.

You can synchronize the same users from two directory services. The connection to the logon forest provides the users. The connection to the resource forest merely augments the properties of existing profiles, similarly to a connection to a business system.

**Synchronization options**

You can perform two kinds of synchronization: full and incremental. Full synchronization can take a long time—for directories that contain hundreds of thousands of users, it could take several days. Incremental synchronization only synchronizes data that has changed in AD DS or SharePoint Server 2016, and is more efficient. You must perform a full synchronization the first time that you synchronize. After that, you can use incremental synchronization unless there have been changes to mapped properties or connections.

You can configure a timer job to run an incremental synchronization on a set schedule, ranging from every few minutes through monthly. You can also start either a full synchronization or an incremental synchronization manually.

Importing profiles using an external identity manager

### Importing profiles using an external identity manager

If you need capabilities that go beyond what SharePoint Active Directory Import can do, you can use Microsoft Identity Manager 2016 (MIM). MIM installs on a separate server and is separately managed from SharePoint Server.

To learn how to configure MIM for use with SharePoint Server 2016, see the following resources:

Install Microsoft Identity Manager for User Profiles in SharePoint Server

Use a sample MIM solution in SharePoint Server

Hybrid profiles

### Hybrid profiles

Hybrid profiles can be configured as part of an overall SharePoint Hybrid deployment. Hybrid features help you integrate the user experience between SharePoint Server and Microsoft 365 by linking common features together or by automatically redirecting users to Microsoft 365 to use a given feature.

With hybrid profiles, your users' profiles are handled entirely in Microsoft 365. If there is data in your on-premises network that you want to include in your Microsoft 365 profiles, you can create a custom solution to copy this data to Microsoft 365.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
