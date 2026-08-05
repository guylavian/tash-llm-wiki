---
title: "Extend claims-based web applications in SharePoint - SharePoint Server"
description: "Learn how to extend an existing claims-based SharePoint Server web application into a new zone to surface content to different types of users."
ms.topic: how-to
---
Note

Extend claims-based web applications in SharePoint

# Extend claims-based web applications in SharePoint

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can extend a web application that uses claims-based authentication by using Central Administration. When you extend a web application, you expose the same content to different sets of users by using an additional IIS web site to host the same content.

Extend a claims-based web application by using Central Administration

## Extend a claims-based web application by using Central Administration

Use the procedure described in this section to extend a claims-based SharePoint Server web application using the Central Administration.

**To extend a claims-based web application**

Start SharePoint 2016 Central Administration.

On the Central Administration Home page, in the **Application Management** section, click **Manage web applications**.

Select the web application you want to extend and, in the **Contribute** group of the ribbon, click **Extend**.

On the **Extend Web Application to Another IIS Web Site** page, in the **IIS Web Site** section, configure the settings for your extended web application by selecting one of the following two options:

Click **Use an existing IIS web site**, and then select the web site on which to extend your existing web application.

Click **Create a new IIS web site**, and then type the name of the web site in the **Name** box.

In the **IIS Web Site** section, in the **Port** box, type the port number you want to use to access the web application. If you're creating a new web site, this box contains a suggested port number. If you're using an existing web site, this box contains the current port number.

Note

The default port number for HTTP access is 80, and the default port number for HTTPS access is 443. To enable users to access the web application without typing in a port number, use the appropriate default port number.

Optional: In the **IIS Web Site** section, in the **Host Header** box, type the host name (for example, `www.contoso.com`) that you want to use to access the web application.

Note

In general, this box is empty unless you want to configure two or more IIS web sites to use the same port on the same server and DNS has been configured to point multiple server names to the same server.

In the **IIS Web Site** section, in the **Path** box, type the path to the site directory on the server. If you're creating a new web site, this box contains a suggested path. If you're using an existing web site, this box contains the current path of that web site.

In the **Security Configuration** section, select the authentication method that you want to use for the web application and choose whether or not to use **Use Secure Sockets Layer (SSL)**.

Important

Secure Sockets Layer (SSL) is a requirement for web applications that are deployed in scenarios that support server-to-server authentication and app authentication. For more information, see Plan for server-to-server authentication in SharePoint Server.

Under **Authentication provider**, select **NTLM** or **Negotiate (Kerberos)**.

Kerberos is the recommended security configuration to use with Integrated Windows authentication. Kerberos requires special configuration by the domain administrator. NTLM authentication will work with any application pool account.

In the **Security Configuration** section, click **Yes** or **No** for the **Use Secure Sockets Layer (SSL)** options. If you choose **Yes**, you must request and install an SSL certificate to configure SSL. For more information about how to set up SSL, see How to Setup SSL on IIS 7.0.

In the **Public URL** section, type the URL for the domain name for all sites that users will access in this web application. This URL will be the base URL for links on pages within the web application. The default URL is the current server name and port.

In the **Public URL** section, select the zone to use for the web application in the drop-down menu.

Click **OK** to extend the existing web application.

Extended web applications and cross-site publishing

## Extended web applications and cross-site publishing

If you're using cross-site publishing, be careful about extending the web application. Depending on which site collection you extend the web application for, it can break the friendly URLs to your catalog items. Here's what you should do:

On your authoring site, don't extend the web application. It will break the friendly URLs to your catalog items. For example, the URL to your catalog item won't point to the friendly URL `https://www.contoso.com/Computers/model101`, but to the catalog item in your authoring site, for example `https://www.contoso.com/sites/catalog/Lists/Products/DispForm.aspx?ID=1&amp;Source=http%3A%2F%`.

On your publishing site, if you want to extend the web application, for example to support different authentication providers, you have to extend the web application  *before*  you connect your publishing site to a catalog as described in Connect a publishing site to a catalog in SharePoint Server. If you have already connected your publishing site to a catalog, do the following:

Disconnect the publishing site from the catalog.

Extend the web application for your publishing site.

Repeat the procedure of connecting your publishing site to the catalog.

See also

## See also

Other Resources

#### Other Resources

New-SPWebApplicationExtension

Create claims-based web applications in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-04-27
