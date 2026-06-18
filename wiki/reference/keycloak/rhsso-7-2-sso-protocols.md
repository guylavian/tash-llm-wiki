---
title: "Chapter 7. SSO Protocols - Red Hat Single Sign-On 7.2 Server Administration Guide"
type: reference
domain: keycloak
slug: rhsso-7-2-sso-protocols
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.2/html/server_administration_guide/sso_protocols
guide: server_administration_guide
version: 7.2
family: rhsso
documentKind: "Documentation"
---

# Chapter 7. SSO Protocols - Red Hat Single Sign-On 7.2 Server Administration Guide

Chapter 7. SSO Protocols
The chapter gives a brief overview of the authentication protocols and how the Red Hat Single Sign-On authentication server and the applications it secures interact with these protocols.
7.1. OpenID Connect
OpenID Connect (OIDC) is an authentication protocol that is an extension of OAuth 2.0. While OAuth 2.0 is only a framework for building authorization protocols and is mainly incomplete, OIDC is a full-fledged authentication and authorization protocol. OIDC also makes heavy use of the Json Web Token (JWT) set of standards. These standards define an identity token JSON format and ways to digitally sign and encrypt that data in a compact and web-friendly way.
There are really two types of use cases when using OIDC. The first is an application that asks the Red Hat Single Sign-On server to authenticate a user for them. After a successful login, the application will receive an identity token and an access token. The identity token contains information about the user such as username, email, and other profile information. The access token is digitally signed by the realm and contains access information (like user role mappings) that the application can use to determine what resources the user is allowed to access on the application.
The second type of use cases is that of a client that wants to gain access to remote services. In this case, the client asks Red Hat Single Sign-On to obtain an access token it can use to invoke on other remote services on behalf of the user. Red Hat Single Sign-On authenticates the user then asks the user for consent to grant access to the client requesting it. The client then receives the access token. This access token is digitally signed by the realm. The client can make REST invocations on remote services using this access token. The REST service extracts the access token, verifies the signature of the token, then decides based on access information within the token whether or not to process the request.
7.1.1. OIDC Auth Flows
OIDC has different ways for a client or application to authenticate a user and receive an identity and access token. Which path you use depends greatly on the type of application or client requesting access. All of these flows are described in the OIDC and OAuth 2.0 specifications so only a brief overview will be provided here.
7.1.1.1. Authorization Code Flow
This is a browser-based protocol and it is what we recommend you use to authenticate and authorize browser-based applications. It makes heavy use of browser redirects to obtain an identity and access token. Here’s a brief summary:
- Browser visits application. The application notices the user is not logged in, so it redirects the browser to Red Hat Single Sign-On to be authenticated. The application passes along a callback URL (a redirect URL) as a query parameter in this browser redirect that Red Hat Single Sign-On will use when it finishes authentication.
- Red Hat Single Sign-On authenticates the user and creates a one-time, very short lived, temporary code. Red Hat Single Sign-On redirects back to the application using the callback URL provided earlier and additionally adds the temporary code as a query parameter in the callback URL.
- The application extracts the temporary code and makes a background out of band REST invocation to Red Hat Single Sign-On to exchange the code for an identity, access and refresh token. Once this temporary code has been used once to obtain the tokens, it can never be used again. This prevents potential replay attacks.
It is important to note that access tokens are usually short lived and often expired after only minutes. The additional refresh token that was transmitted by the login protocol allows the application to obtain a new access token after it expires. This refresh protocol is important in the situation of a compromised system. If access tokens are short lived, the whole system is only vulnerable to a stolen token for the lifetime of the access token. Future refresh token requests will fail if an admin has revoked access. This makes things more secure and more scalable.
Another important aspect of this flow is the concept of a public vs. a confidential client. Confidential clients are required to provide a client secret when they exchange the temporary codes for tokens. Public clients are not required to provide this client secret. Public clients are perfectly fine so long as HTTPS is strictly enforced and you are very strict about what redirect URIs are registered for the client. HTML5/JavaScript clients always have to be public clients because there is no way to transmit the client secret to them in a secure manner. Again, this is ok so long as you use HTTPS and strictly enforce redirect URI registration. This guide goes more detail into this in the Managing Clients chapter.
Red Hat Single Sign-On also supports the optional Proof Key for Code Exchange specification.
7.1.1.2. Implicit Flow
This is a browser-based protocol that is similar to Authorization Code Flow except there are fewer requests and no refresh tokens involved. We do not recommend this flow as there remains the possibility of access tokens being leaked in the browser history as tokens are transmitted via redirect URIs (see below). Also, since this flow doesn’t provide the client with a refresh token, access tokens would either have to be long-lived or users would have to re-authenticate when they expired. This flow is supported because it is in the OIDC and OAuth 2.0 specification. Here’s a brief summary of the protocol:
- Browser visits application. The application notices the user is not logged in, so it redirects the browser to Red Hat Single Sign-On to be authenticated. The application passes along a callback URL (a redirect URL) as a query parameter in this browser redirect that Red Hat Single Sign-On will use when it finishes authentication.
- Red Hat Single Sign-On authenticates the user and creates an identity and access token. Red Hat Single Sign-On redirects back to the application using the callback URL provided earlier and additionally adding the identity and access tokens as query parameters in the callback URL.
- The application extracts the identity and access tokens from the callback URL.
7.1.1.3. Resource Owner Password Credentials Grant (Direct Access Grants)
This is referred to in the Admin Console as Direct Access Grants. This is used by REST clients that want to obtain a token on behalf of a user. It is one HTTP POST request that contains the credentials of the user as well as the id of the client and the client’s secret (if it is a confidential client). The user’s credentials are sent within form parameters. The HTTP response contains identity, access, and refresh tokens.
7.1.1.4. Client Credentials Grant
This is also used by REST clients, but instead of obtaining a token that works on behalf of an external user, a token is created based on the metadata and permissions of a service account that is associated with the client. More info together with example is in Service Accounts chapter.
7.1.2. Red Hat Single Sign-On Server OIDC URI Endpoints
Here’s a list of OIDC endpoints that the Red Hat Single Sign-On publishes. These URLs are useful if you are using a non-Red Hat Single Sign-On client adapter to talk OIDC with the auth server. These are all relative URLs and the root of the URL being the HTTP(S) protocol, hostname, and usually path prefixed with /auth: i.e. https://localhost:8080/auth
- /realms/{realm-name}/protocol/openid-connect/token
- This is the URL endpoint for obtaining a temporary code in the Authorization Code Flow or for obtaining tokens via the Implicit Flow, Direct Grants, or Client Grants.
- /realms/{realm-name}/protocol/openid-connect/auth
- This is the URL endpoint for the Authorization Code Flow to turn a temporary code into a token.
- /realms/{realm-name}/protocol/openid-connect/logout
- This is the URL endpoint for performing logouts.
- /realms/{realm-name}/protocol/openid-connect/userinfo
- This is the URL endpoint for the User Info service described in the OIDC specification.
In all of these replace {realm-name} with the name of the realm.
7.2. SAML
SAML 2.0 is a similar specification to OIDC but a lot older and more mature. It has its roots in SOAP and the plethora of WS-* specifications so it tends to be a bit more verbose than OIDC. SAML 2.0 is primarily an authentication protocol that works by exchanging XML documents between the authentication server and the application. XML signatures and encryption is used to verify requests and responses.
There is really two types of use cases when using SAML. The first is an application that asks the Red Hat Single Sign-On server to authenticate a user for them. After a successful login, the application will receive an XML document that contains something called a SAML assertion that specify various attributes about the user. This XML document is digitally signed by the realm and contains access information (like user role mappings) that the application can use to determine what resources the user is allowed to access on the application.
The second type of use cases is that of a client that wants to gain access to remote services. In this case, the client asks Red Hat Single Sign-On to obtain an SAML assertion it can use to invoke on other remote services on behalf of the user.
7.2.1. SAML Bindings
SAML defines a few different ways to exchange XML documents when executing the authentication protocol. The Redirect and Post bindings cover browser based applications. The ECP binding covers REST invocations. There are other binding types but Red Hat Single Sign-On only supports those three.
7.2.1.1. Redirect Binding
The Redirect Binding uses a series of browser redirect URIs to exchange information. This is a rough overview of how it works.
- The user visits the application and the application finds the user is not authenticated. It generates an XML authentication request document and encodes it as a query param in a URI that is used to redirect to the Red Hat Single Sign-On server. Depending on your settings, the application may also digitally sign this XML document and also stuff this signature as a query param in the redirect URI to Red Hat Single Sign-On. This signature is used to validate the client that sent this request.
- The browser is redirected to Red Hat Single Sign-On. The server extracts the XML auth request document and verifies the digital signature if required. The user then has to enter in their credentials to be authenticated.
- After authentication, the server generates an XML authentication response document. This document contains a SAML assertion that holds metadata about the user like name, address, email, and any role mappings the user might have. This document is almost always digitally signed using XML signatures, and may also be encrypted.
- The XML auth response document is then encoded as a query param in a redirect URI that brings the browser back to the application. The digital signature is also included as a query param.
- The application receives the redirect URI and extracts the XML document and verifies the realm’s signature to make sure it is receiving a valid auth response. The information inside the SAML assertion is then used to make access decisions or display user data.
7.2.1.2. POST Binding
The SAML POST binding works almost the exact same way as the Redirect binding, but instead of GET requests, XML documents are exchanged by POST requests. The POST Binding uses JavaScript to trick the browser into making a POST request to the Red Hat Single Sign-On server or application when exchanging documents. Basically HTTP responses contain an HTML document that contains an HTML form with embedded JavaScript. When the page is loaded, the JavaScript automatically invokes the form. You really don’t need to know about this stuff, but it is a pretty clever trick.
7.2.1.3. ECP
ECP stands for "Enhanced Client or Proxy", a SAML v.2.0 profile which allows for the exchange of SAML attributes outside the context of a web browser. This is used most often for REST or SOAP-based clients.
7.2.2. Red Hat Single Sign-On Server SAML URI Endpoints
Red Hat Single Sign-On really only has one endpoint for all SAML requests.
http(s)://authserver.host/auth/realms/{realm-name}/protocol/saml
All bindings use this endpoint.
7.3. OpenID Connect vs. SAML
Choosing between OpenID Connect and SAML is not just a matter of using a newer protocol (OIDC) instead of the older more mature protocol (SAML).
In most cases Red Hat Single Sign-On recommends using OIDC.
SAML tends to be a bit more verbose than OIDC.
Beyond verbosity of exchanged data, if you compare the specifications you’ll find that OIDC was designed to work with the web while SAML was retrofitted to work on top of the web. For example, OIDC is also more suited for HTML5/JavaScript applications because it is easier to implement on the client side than SAML. As tokens are in the JSON format, they are easier to consume by JavaScript. You will also find several nice features that make implementing security in your web applications easier. For example, check out the iframe trick that the specification uses to easily determine if a user is still logged in or not.
SAML has its uses though. As you see the OIDC specifications evolve you see they implement more and more features that SAML has had for years. What we often see is that people pick SAML over OIDC because of the perception that it is more mature and also because they already have existing applications that are secured with it.
7.4. Docker Registry v2 Authentication
Docker authentication is disabled by default. To enable see Profiles.
Docker Registry V2 Authentciation is an OIDC-Like protocol used to authenticate users against a Docker registry. Red Hat Single Sign-On’s implementation of this protocol allows for a Red Hat Single Sign-On authentication server to be used by a Docker client to authenticate against a registry. While this protocol uses fairly standard token and signature mechanisms, it has a few wrinkles that prevent it from being treated as a true OIDC implementation. The largest deviations include a very specific JSON format for requests and responses as well as the ability to understand how to map repository names and permissions to the OAuth scope mechanism.
7.4.1. Docker Auth Flow
The Docker API documentation best describes and illustrates this process, however a brief summary will be given below from the perspective of the Red Hat Single Sign-On authentication server.
This flow assumes that a docker login
command has already been performed
- The flow begins when the Docker client requests a resource from the Docker registry. If the resource is protected and no auth token is present in the request, the Docker registry server will respond to the client with a 401 + some information on required permissions and where to find the authorization server.
-
The Docker client will construct an authentication request based on the 401 response from the Docker registry. The client will then use the locally cached credentials (from a previously run
docker login
command) as part of a HTTP Basic Authentication request to the Red Hat Single Sign-On authentication server. - The Red Hat Single Sign-On authentication server will attempt to authenticate the user and return a JSON body containing an OAuth-style Bearer token.
- The Docker client will get the bearer token from the JSON response and use it in the Authorization header to request the protected resource.
- When the Docker registry recieves the new request for the protected resource with the token from the Red Hat Single Sign-On server, the registry validates the token and grants access to the requested resource (if appropriate).
7.4.2. Red Hat Single Sign-On Docker Registry v2 Authentication Server URI Endpoints
Red Hat Single Sign-On really only has one endpoint for all Docker auth v2 requests.
http(s)://authserver.host/auth/realms/{realm-name}/protocol/docker-v2
