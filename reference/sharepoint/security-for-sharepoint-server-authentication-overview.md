---
title: "Authentication overview for SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: security-for-sharepoint-server-authentication-overview
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/authentication-overview
family: security-for-sharepoint-server
documentKind: "overview"
abstract: "Learn about how user authentication, app authentication, and server-to-server authentication work in SharePoint Server."
---

# Authentication overview for SharePoint Server - SharePoint Server

Note

Authentication overview for SharePoint Server

# Authentication overview for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server requires authentication for the following types of interactions:

Users who access on-premises SharePoint resources

Apps that access on-premises SharePoint resources

On-premises servers that access on-premises SharePoint resources, or vice versa

Learn about SharePoint authentication in Microsoft 365.

Note

In SharePoint Server Subscription Edition, we now support OIDC 1.0 authentication. For more information on how to work with this new authentication type, see OpenID Connect 1.0 authentication.

User authentication in SharePoint Server

## User authentication in SharePoint Server

User authentication is the validation of a user's identity against an authentication provider, which is a directory or database that contains the user's credentials and can verify that the user submitted them correctly. User authentication occurs when a user attempts to access a SharePoint resource.

SharePoint Server supports claims-based authentication.

The result of a claims-based authentication is a claims-based security token, which the SharePoint Security Token Service (STS) generates.

SharePoint Server supports Windows, forms-based, Security Assertion Markup Language(SAML) and Open ID Connect (OIDC)-based claims authentication. For information about how Windows, forms-based and SAML based authentication methods work, see the following videos. For information about how OIDC authentication works, check OIDC setup guide.

Note

This information in the videos applies to SharePoint Server 2013, SharePoint Server 2016, SharePoint Server 2019 and SharePoint Server Subscription Edition.

**Windows claims authentication in SharePoint Server 2013 and 2016 video**

**Forms-based claims authentication in SharePoint Server 2013 and 2016 video**

**SAML-based claims authentication in SharePoint Server 2013 and 2016 video**

For more information, see Plan for user authentication methods in SharePoint Server.

App authentication in SharePoint Server

## App authentication in SharePoint Server

App authentication is the validation of a remote SharePoint app's identity and the authorization of the app and an associated user of a secured SharePoint resource request. App authentication occurs when an external component of a SharePoint Store app or an App Catalog app, such as a web server that is located on the intranet or the Internet, attempts to access a secured SharePoint resource.

For example, suppose that a user opens a SharePoint page that contains an IFRAME of a SharePoint app, and that IFRAME needs an external component, such as a server on the intranet or the Internet, to access a secured SharePoint resource in order to render the page. The external component of the SharePoint app must be authenticated and authorized so that SharePoint provides the requested information and the app can render the page for the user.

If the SharePoint app doesn't require a SharePoint secured resource to render the page for the user, app authentication isn't needed. For example, a SharePoint app that provides weather forecast information and only has to access a weather information server on the Internet doesn't have to use app authentication.

App authentication is a combination of two processes:

Authentication

Verifying that the application has registered correctly with a commonly trusted identity broker

Authorization

Verifying that the application and the associated user for the request has the appropriate permissions to perform its operation, such as accessing a folder or list or executing a query

To perform app authentication, the application obtains an access token either from the Microsoft Azure Access Control Service (ACS) or by self-signing an access token using a certificate that SharePoint Server trusts. The access token asserts a request for access to a specific SharePoint resource and contains information that identifies the app and the associated user, instead of the validation of the user's credentials. The access token isn't a sign in token.

For SharePoint Store apps, an example of the authentication process is as follows:

A user opens a SharePoint web page that contains an IFRAME that has to be rendered by a SharePoint Store app, which is hosted on the Internet and uses ACS as its trust broker. To render the IFRAME for the user, the SharePoint Store app must access a SharePoint resource.

The SharePoint STS requests and receives a context token from ACS.

SharePoint sends the requested web page together with the context token to the user's web browser.

The user's web browser sends a request for the IFRAME's content and the context token to the SharePoint Store app server on the Internet.

The SharePoint Store app server requests and receives an access token from ACS.

The SharePoint Store app server sends the SharePoint resource request and the access token to the SharePoint server.

The SharePoint server authorizes the access, checking both the app's permissions, which were specified when the app was installed, and the associated user's permissions.

If permitted, SharePoint sends the requested data to the SharePoint Store app server on the Internet.

The SharePoint Store app server on the Internet sends the IFRAME results to the web browser, which renders the IFRAME portion of the page for the user.

Notice how the SharePoint Store app has accessed SharePoint server resources without having to obtain the user's credentials. The access was authenticated through ACS, which is trusted by the server running SharePoint Server, and authorized through the set of app and user permissions.

For SharePoint App Catalog apps, an example of the authentication process is as follows:

A user opens a SharePoint web page that contains an IFRAME that has to be rendered by an App Catalog app that is hosted on the intranet and uses a self-signed certificate for its access tokens. To render the IFRAME for the user, the App Catalog app must access a SharePoint resource.

SharePoint sends the requested page along with the IFRAME to the user's web browser.

The user's web browser sends a request for the IFRAME's content to the App Catalog app server on the intranet.

The App Catalog app server authenticates the user and generates an access token, signed with its self-signed certificate.

The App Catalog app server sends the SharePoint resource request and the access token to the SharePoint server.

The SharePoint server authorizes the access, checking both the app's permissions, which were specified when the app was installed, and the associated user's permissions.

If permitted, the SharePoint server sends the requested data to the App Catalog app server on the intranet.

The App Catalog app server sends the IFRAME results to the web browser, which renders the IFRAME portion of the page for the user.

Note

App Catalog apps can use either ACS or a self-signed certificate for their access tokens.

For more information, see Plan for app authentication in SharePoint Server.

Server-to-server authentication in SharePoint Server

## Server-to-server authentication in SharePoint Server

Server-to-server authentication is the validation of a server's request for resources that is based on a trust relationship established between the STS of the server that runs SharePoint Server and the STS of another server that supports the OAuth server-to-server protocol, such as on-premises running SharePoint Server, Exchange Server 2016, Skype for Business 2016, or Azure Workflow Service, and SharePoint Server running in Microsoft 365. Based on this trust relationship, a requesting server can access secured resources on the SharePoint server on behalf of a specified user account, subject to server and user permissions.

For example, a server running Exchange Server 2016 can request resources of a server running SharePoint Server for a specific user account. This provision contrasts with app authentication, in which the app doesn't have access to user account credential information. The user can be currently signed in to the server making the resource request or not, depending on the service and the request.

When a server running SharePoint Server attempts to access a resource on a server or a server attempts to access a resource on a server running SharePoint Server, the incoming access request must be authenticated so that the server accepts the incoming access request and subsequent data. Server-to-server authentication verifies that the server running SharePoint Server and the user whom it's representing are trusted.

The token that is used for a server-to-server authentication is a server-to-server token, not a sign in token. The server-to-server token contains information about the server that requests access and the user account on whose behalf the server is acting.

For on-premises servers, an example basic process is as follows:

A user opens a SharePoint web page that requires information from another server (for example, display the list of tasks from both SharePoint Server and Exchange Server 2016).

SharePoint Server generates a server-to-server token.

SharePoint Server sends the server-to-server token to the other server.

The other server validates the SharePoint server-to-server token.

The other server sends a message to SharePoint Server to indicate that the sent server-to-server token was valid.

The service on the server running SharePoint Server accesses the data on the server.

The service on the server running SharePoint Server renders the page for the user.

When both servers are running in Microsoft 365, an example process is as follows:

A user opens a SharePoint web page that requires information from another server (for example, display the list of tasks from both SharePoint and Exchange Online).

SharePoint requests and receives a server-to-server token from ACS.

SharePoint sends the server-to-server token to the Microsoft 365 server.

The Microsoft 365 server verifies the user identity in the server-to-server token with ACS.

The Microsoft 365 server sends a message to SharePoint to indicate that the sent server-to-server token was valid.

The service on SharePoint accesses the data on the Microsoft 365 server.

The service on SharePoint renders the page for the user.

For more information, see Plan for server-to-server authentication in SharePoint Server.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
