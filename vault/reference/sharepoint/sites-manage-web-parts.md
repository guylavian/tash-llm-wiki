---
title: "Manage web parts in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: sites-manage-web-parts
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/sites/manage-web-parts
family: sites
documentKind: "article"
abstract: "Helps you prepare to manage security for web parts pages and controls that are used with SharePoint Server."
---

# Manage web parts in SharePoint Server - SharePoint Server

Note

Manage web parts in SharePoint Server

# Manage web parts in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In SharePoint Server, a web parts page is a collection of web parts that combines list data, timely information, or useful graphics into a dynamic web page. The layout and content of a web parts page can be set for all users and then, optionally, personalized for individual users. A site owner or a site member with the appropriate permissions can create and customize web parts pages by using a browser to add, reconfigure, or remove web parts.

You can use web parts on web parts pages, wiki pages, content pages, and publishing pages.

The web parts infrastructure in SharePoint Server exists on a layer above the ASP.NET web parts infrastructure. To effectively protect SharePoint sites, server administrators must be familiar with security guidelines and best practices for ASP.NET. For more information, see Security Guidelines: ASP.NET.

Note

The apps for SharePoint add functionality to a site. Site owners can add apps for SharePoint to SharePoint sites so that they and other users of the site can use the application. For more information, see Add apps for SharePoint to a SharePoint site.

Security for web parts pages and controls

## Security for web parts pages and controls

Protecting web parts pages and controls is a collaborative effort. Developers, site administrators, and server administrators must work together to improve security for web parts and web parts pages. Developers should validate Web Part input to prevent server attacks. Server administrators must configure Internet Information Services (IIS) to use an appropriate authentication method.

Server administrators also configure and deploy web parts solutions to a web server or web farm. After the solution is deployed, site administrators or server administrators define the permission levels and permissions that allow access to web parts pages.

The following table shows the security roles that are responsible for configuring permissions on Web Parts pages and Web Parts.

**Table: Security roles to configure Web Parts and Web Parts pages**

| **Role** | **Category** | **Applies to** | **Description** | **Recommended guidelines** |
| --- | --- | --- | --- | --- |
| Developer | Input Validation | Web Part code | Input validation refers to how your application filters, scrubs, or rejects input before additional processing. This includes verification that the input that your application receives is valid and safe. | Building Secure ASP.NET Pages and Controls 
 Creating Web Parts For SharePoint |
| Server administrator | Authentication | IIS | Authentication is the process where an entity validates the identity of another entity, typically through credentials such as a user name and password. | Plan for user authentication methods in SharePoint Server |
| Site administrator/ Server administrator | Authorization | Site collections | Authorization is the process that provides access controls for Web sites, lists, folders, or items by determining which users can perform specific actions on a given object. The authorization process assumes that the user has already been authenticated. | Authorization and Authentication |
| Server administrator | Configuration Management | .NET Framework configuration | Configuration management encompasses a broad range of settings that allow an administrator to manage the Web application and its environment. These settings are stored in XML configuration files, some of which control computer-wide settings, while others control application-specific configurations. You can define special security constraints in configuration files and computer-level code access security permissions. | Code Access Security 
 Microsoft Windows SharePoint Services and Code Access Security 
 Using Code Access Security with ASP.NET |

Thank you to Waqas Sarwar, Microsoft MVP, for providing the following article about web part security in SharePoint Server 2016, SharePoint 2016 Central Admin - Security - Manage Web Part security.

The following articles about managing web parts in SharePoint Server are available in this section:

| **Content** | **Description** |
| --- | --- |
| Configure and deploy web parts in SharePoint Server | How to secure and deploy web parts in SharePoint Server. |
| Edit existing web parts in SharePoint Server | How to edit web parts and web part properties in SharePoint Server, |

See also

## See also

Concepts

#### Concepts

Configure and deploy web parts in SharePoint Server

Edit existing web parts in SharePoint Server

Security for SharePoint Server

Plan for user authentication methods in SharePoint Server

Other Resources

#### Other Resources

Add, edit, minimize, or delete a Web Part from a page

Using web parts on pages

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
