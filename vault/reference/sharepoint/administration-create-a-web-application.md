---
title: "Create a web application in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-create-a-web-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/create-a-web-application
family: administration
documentKind: "article"
abstract: "SharePoint Server web applications isolate content for specific types of users within your site collections."
---

# Create a web application in SharePoint Server - SharePoint Server

Note

Create a web application in SharePoint Server

# Create a web application in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The following articles provide information about how to create web applications.

**Introduction**

A SharePoint Server web application is composed of an Internet Information Services (IIS) web site that acts as a logical unit for the site collections that you create. Before you can create a site collection, you must first create a Web application. Each web application is represented by a different IIS web site with a unique or shared application pool. You can assign each web application a unique domain name. This helps prevent cross-site scripting attacks. When you create a new web application, you also create a new content database and define the authentication method used to connect to the database. In addition, you define an authentication method to be used by the IIS Web site in SharePoint Server.

| **                         ** | **Content** | **Description** |
| --- | --- | --- |
|  | Configure Basic authentication for a claims-based Web application | Explains how to configure basic authentication for a web application that uses claims-based authentication in SharePoint Server. |
|  | Configure Digest authentication for a claims-based Web application | Explains how to configure digest authentication for a web application that uses claims-based authentication in SharePoint Server. |
|  | Edit general settings on a web application in SharePoint 2013 | Illustrates how to change general settings for a SharePoint Server web application in Central Administration. |

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
