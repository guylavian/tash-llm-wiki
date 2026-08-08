---
title: "Configure digest authentication for a claims-based web application in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-digest-authentication-for-a-claims-based-web-application
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-digest-authentication-for-a-claims-based-web-application
family: administration
documentKind: "how-to"
abstract: "Learn how to configure digest authentication for a web application that uses claims-based authentication in SharePoint Server."
---

# Configure digest authentication for a claims-based web application in SharePoint Server - SharePoint Server

Note

Configure digest authentication for a claims-based web application in SharePoint Server

# Configure digest authentication for a claims-based web application in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can configure digest authentication for one or more zones in a SharePoint Server claims-based web application. A web application is an Internet Information Services (IIS) web site that SharePoint Server creates and uses. Zones represent different logical paths for gaining access to the same web application. Within each web application, you can create up to five zones. A different web site in IIS represents each zone. Use zones to enforce different access and policy conditions for large groups of users. To configure digest authentication for one or more zones in a SharePoint Server web application, use IIS Manager console, instead of SharePoint Server Central Administration.

Unlike basic authentication, digest authentication encrypts user credentials to increase security. User credentials are sent as an MD5 message digest in which the original user name and password cannot be determined. Digest authentication uses a challenge/response protocol that requires the authentication requestor to present valid credentials in response to a challenge from the server. To authenticate against the server, the client has to supply an MD5 message digest in a response that contains a shared secret password string. The MD5 Message-Digest Algorithm is described in RFC 1321. For access to RFC 1321, see The Internet Engineering Task Force (https://go.microsoft.com/fwlink/p/?LinkId=159913).

Before you begin

## Before you begin

Before you perform this procedure, confirm the following:

Your system is running SharePoint Server.

The user and IIS server must be members of, or trusted by, the same domain.

Users must have a valid Windows user account stored in Active Directory Domain Services (AD DS) on the domain controller.

The domain must use a Windows Server 2008 or Windows Server 2008 R2 domain controller.

Note

For SharePoint Server 2016, the domain must use a Windows Server 2012 R2 or Windows Server 2016 domain controller

You understand digest authentication for web traffic.

For more information, see What is Digest Authentication? (/previous-versions/windows/it-pro/windows-server-2003/cc778868(v=ws.10)).

Configure IIS to enable digest authentication

## Configure IIS to enable digest authentication

Use IIS Manager console to configure IIS to enable digest authentication for one or more of the following zones for a claims-based web application:

Default

Intranet

Extranet

The Default zone is the zone that is first created when a web application is created. The other zones are created by extending a web application. For more information, see Extend claims-based web applications in SharePoint.

**To configure IIS to enable digest authentication**

Verify that you are a member of the Administrators group on the server on which you are configuring IIS.

Click **Start**, point to **Administrative Tools**, and then click **Internet Information Services (IIS) Manager** to start IIS Manager console.

Expand **Sites** in the console tree, and then click the IIS web site that corresponds to the web application zone on which you want to configure digest authentication.

In **Features View**, in **IIS**, double-click **Authentication**.

In **Features View**, in **Authentication**, right-click **Digest Authentication**, and then click **Enable**.

Right-click **Digest Authentication**, and then click **Edit**.

In the **Edit Digest Authentication Settings** dialog, in the **Realm** text box, type the appropriate realm, and then click **OK**.

The realm is a DNS domain name or an IP address that will use the credentials that have been authenticated against your internal Windows domain. You must configure a realm name for digest authentication.

The web site is now configured to use digest authentication.

See also

## See also

Concepts

#### Concepts

Configure Basic authentication for a claims-based Web application

Other Resources

#### Other Resources

Plan for user authentication methods in SharePoint Server

Extend claims-based web applications in SharePoint

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
