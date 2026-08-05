---
title: "Configure basic authentication for a claims-based web application in SharePoint Server - SharePoint Server"
description: "Learn how to configure basic authentication for a web application that uses claims-based authentication in SharePoint Server."
ms.topic: how-to
---
Note

Configure basic authentication for a claims-based web application in SharePoint Server

# Configure basic authentication for a claims-based web application in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can configure basic authentication for one or more zones in a SharePoint Server claims-based web application. A web application is an Internet Information Services (IIS) web site that SharePoint Server creates and uses. Zones represent different logical paths for gaining access to the network services that are available within the same web application. Within each web application, you can create up to five zones. A different web site in IIS represents each zone. Use zones to enforce different access and policy conditions for large groups of users. To configure basic authentication for one or more zones in a SharePoint Server web application, use IIS Manager console, instead of SharePoint Server Central Administration.

Before you begin

## Before you begin

Before you perform this procedure, confirm the following:

Your system is running SharePoint Server.

Basic authentication requires previously assigned Windows account credentials for user access.

You understand basic authentication for web traffic.

Basic authentication enables a web browser to provide credentials when the browser makes a request during an HTTP transaction. Because user credentials are not encrypted for network transmission but are sent over the network in plaintext, we do not recommend that you use basic authentication over an unsecured HTTP connection. To use basic authentication, you should enable Secure Sockets Layer (SSL) encryption for the web site; otherwise, the credentials can be intercepted by a malicious user.

Configure IIS to enable basic authentication

## Configure IIS to enable basic authentication

Use the IIS Manager console to configure IIS to enable basic authentication for one or more of the following zones for a claims-based web application:

Default

Intranet

Extranet

The Default zone is the zone that is first created when a web application is created. The other zones are created by extending a web application. For more information, see Extend claims-based web applications in SharePoint.

**To configure IIS to enable basic authentication**

Verify that you a member of the Administrators group on the server on which you are configuring IIS.

Click **Start**, point to **Administrative Tools**, and then click **Internet Information Services (IIS) Manager** to start IIS Manager console.

Expand **Sites** in the console tree, and then click the IIS web site that corresponds to the web application zone on which you want to configure basic authentication.

In **Features View**, in **IIS**, double-click **Authentication**.

In **Features View**, in **Authentication**, right-click **Basic Authentication**, and then click **Enable**.

Right-click **Basic Authentication**, and then click **Edit**.

In the **Edit Basic Authentication Settings** dialog, in the **Default domain** text box, type the appropriate default domain.

The default domain is the name of a domain against which you want users to be authenticated when they do not provide a domain name.

In the **Realm** text box, type the appropriate realm, and then click **OK**.

The realm is a DNS domain name or an IP address that will use the credentials that are authenticated against your internal Windows domain. Configuring a realm name for basic authentication is optional.

The web site is now configured to use basic authentication.

You can also configure basic authentication when you create a web application in SharePoint Server Central Administration by selecting **Basic authentication (password is sent in clear text)** in the **Claims Authentication Types** section of the **Create New Web Application** dialog.

[!SECURITY NOTE]
In the **Claims Authentication Types** section of the **Create New Web Application** dialog, you can select **Integrated Windows authentication**, **Basic authentication (password is sent in clear text)**, or both. If you select both, SharePoint Server will offer both authentication types to the client web browser. The client web browser then determines the type of authentication to use. If you only select **Basic authentication (password is sent in clear text)**, make sure that you enable SSL for this web application.

See also

## See also

Concepts

#### Concepts

Configure Digest authentication for a claims-based Web application

Other Resources

#### Other Resources

Plan for user authentication methods in SharePoint Server

Extend claims-based web applications in SharePoint

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
