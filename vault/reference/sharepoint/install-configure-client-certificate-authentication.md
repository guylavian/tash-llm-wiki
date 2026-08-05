---
title: "Configure client certificate authentication for SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: install-configure-client-certificate-authentication
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/configure-client-certificate-authentication
family: install
documentKind: "how-to"
abstract: "Learn how to configure SharePoint Server to support user authentication using a client certificate."
---

# Configure client certificate authentication for SharePoint Server - SharePoint Server

Note

Configure client certificate authentication for SharePoint Server

# Configure client certificate authentication for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Client certificate authentication enables web-based clients to establish their identity to a server by using a digital certificate, which provides additional security for user authentication. SharePoint Server does not provide built-in support for client certificate authentication, but client certificate authentication is available through Security Assertion Markup Language (SAML)-based claims authentication. You can use Active Directory Federation Services (AD FS) 2.0 as your security token service (STS) for SAML claims or any third-party identity management system that supports standard security protocols such as WS-Trust, WS-Federation, SAML 1.1, and SAML 2.0.

Note

For more information about SharePoint Server protocol requirements, see SharePoint Front-End Protocols.

Claims-based authentication in SharePoint Server allows you to use different STSs. If you configure AD FS as your STS, SharePoint Server can support any identity provider or authentication method that AD FS supports, which includes client certificate authentication.

Note

For more information about AD FS, see Active Directory Federation Services Overview and AD FS 2016.

For additional information on an overview of authentication in SharePoint, please see Plan for user authentication methods in SharePoint Server.

The following figure applies to SharePoint Server 2013 and SharePoint Server 2016, SharePoint Server is configured as a relying partner for an AD FS-based STS.

AD FS can authenticate user accounts for several different types of authentication methods, such as forms-based authentication, Active Directory Domain Services (AD DS), client certificates, and smart cards. When you configure SharePoint Server as a relying partner of AD FS, SharePoint Server trusts the accounts that AD FS validates and the authentication methods that AD FS uses to validate those accounts. This is how SharePoint Server supports client certificate authentication.

Configure client certificate authentication

## Configure client certificate authentication

The following topics explain how to configure SharePoint Server with client certificate authentication or smart card authentication when you use AD FS as your STS:

Configure AD FS to support claims-based authentication.

For more information, see Compound authentication and AD DS claims in AD FS.

Configure SharePoint Server to support SAML-based claims authentication using AD FS.

For more information, see Configure SAML-based claims authentication with AD FS in SharePoint Server and Improved interoperability with SAML 2.0.

Create a web application that uses SAML-based claims authentication.

For more information, see Create claims-based web applications in SharePoint Server.

Note

These steps will be similar for a third-party STS.

See also

## See also

Other Resources

#### Other Resources

Configure SAML-based claims authentication with AD FS in SharePoint Server

Planning and Architecture: AD FS 2.0

AD FS 2.0 Deployment Guide

Using Active Directory Federation Services 2.0 in Identity Solutions

Additional resources

## Additional resources

- Last updated on 
		2024-12-02
