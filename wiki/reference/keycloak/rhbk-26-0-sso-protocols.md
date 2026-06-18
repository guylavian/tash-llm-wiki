---
title: "Chapter 10. SSO protocols - Red Hat build of Keycloak 26.0 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-sso-protocols
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_administration_guide/sso_protocols
guide: server_administration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 10. SSO protocols - Red Hat build of Keycloak 26.0 Server Administration Guide

Chapter 10. SSO protocols
This section discusses authentication protocols, the Red Hat build of Keycloak authentication server and how applications, secured by the Red Hat build of Keycloak authentication server, interact with these protocols.
10.1. OpenID Connect
OpenID Connect (OIDC) is an authentication protocol that is an extension of OAuth 2.0.
OAuth 2.0 is a framework for building authorization protocols and is incomplete. OIDC, however, is a full authentication and authorization protocol that uses the Json Web Token (JWT) standards. The JWT standards define an identity token JSON format and methods to digitally sign and encrypt data in a compact and web-friendly way.
In general, OIDC implements two use cases. The first case is an application requesting that a Red Hat build of Keycloak server authenticates a user. Upon successful login, the application receives an identity token and an access token. The identity token contains user information including user name, email, and profile information. The realm digitally signs the access token which contains access information (such as user role mappings) that applications use to determine the resources users can access in the application.
The second use case is a client accessing remote services.
- The client requests an access token from Red Hat build of Keycloak to invoke on remote services on behalf of the user.
- Red Hat build of Keycloak authenticates the user and asks the user for consent to grant access to the requesting client.
- The client receives the access token which is digitally signed by the realm.
- The client makes REST requests on remote services using the access token.
- The remote REST service extracts the access token.
- The remote REST service verifies the tokens signature.
- The remote REST service decides, based on access information within the token, to process or reject the request.
10.1.1. OIDC auth flows
OIDC has several methods, or flows, that clients or applications can use to authenticate users and receive identity and access tokens. The method depends on the type of application or client requesting access.
10.1.1.1. Authorization Code Flow
The Authorization Code Flow is a browser-based protocol and suits authenticating and authorizing browser-based applications. It uses browser redirects to obtain identity and access tokens.
- A user connects to an application using a browser. The application detects the user is not logged into the application.
- The application redirects the browser to Red Hat build of Keycloak for authentication.
- The application passes a callback URL as a query parameter in the browser redirect. Red Hat build of Keycloak uses the parameter upon successful authentication.
- Red Hat build of Keycloak authenticates the user and creates a one-time, short-lived, temporary code.
- Red Hat build of Keycloak redirects to the application using the callback URL and adds the temporary code as a query parameter in the callback URL.
- The application extracts the temporary code and makes a background REST invocation to Red Hat build of Keycloak to exchange the code for an identity and access and refresh token. To prevent replay attacks, the temporary code cannot be used more than once.
A system is vulnerable to a stolen token for the lifetime of that token. For security and scalability reasons, access tokens are generally set to expire quickly so subsequent token requests fail. If a token expires, an application can obtain a new access token using the additional refresh token sent by the login protocol.
Confidential clients provide client secrets when they exchange the temporary codes for tokens. Public clients are not required to provide client secrets. Public clients are secure when HTTPS is strictly enforced and redirect URIs registered for the client are strictly controlled. HTML5/JavaScript clients have to be public clients because there is no way to securely transmit the client secret to HTML5/JavaScript clients. For more details, see the Managing Clients chapter.
Red Hat build of Keycloak also supports the Proof Key for Code Exchange specification.
10.1.1.2. Implicit Flow
The Implicit Flow is a browser-based protocol. It is similar to the Authorization Code Flow but with fewer requests and no refresh tokens.
The possibility exists of access tokens leaking in the browser history when tokens are transmitted via redirect URIs (see below).
Also, this flow does not provide clients with refresh tokens. Therefore, access tokens have to be long-lived or users have to re-authenticate when they expire.
We do not advise using this flow. This flow is supported because it is in the OIDC and OAuth 2.0 specification.
The protocol works as follows:
- A user connects to an application using a browser. The application detects the user is not logged into the application.
- The application redirects the browser to Red Hat build of Keycloak for authentication.
- The application passes a callback URL as a query parameter in the browser redirect. Red Hat build of Keycloak uses the query parameter upon successful authentication.
- Red Hat build of Keycloak authenticates the user and creates an identity and access token. Red Hat build of Keycloak redirects to the application using the callback URL and additionally adds the identity and access tokens as a query parameter in the callback URL.
- The application extracts the identity and access tokens from the callback URL.
10.1.1.3. Resource owner password credentials grant (Direct Access Grants)
Direct Access Grants are used by REST clients to obtain tokens on behalf of users. It is a HTTP POST request that contains:
- The credentials of the user. The credentials are sent within form parameters.
- The id of the client.
- The clients secret (if it is a confidential client).
The HTTP response contains the identity, access, and refresh tokens.
10.1.1.4. Client credentials grant
The Client Credentials Grant creates a token based on the metadata and permissions of a service account associated with the client instead of obtaining a token that works on behalf of an external user. Client Credentials Grants are used by REST clients.
See the Service Accounts chapter for more information.
10.1.1.5. Refresh token grant
By default, Red Hat build of Keycloak returns refresh tokens in the token responses from most of the flows. Some exceptions are implicit flow or client credentials grant described above.
Refresh token is tied to the user session of the SSO browser session and can be valid for the lifetime of the user session. However, that client should send a refresh-token request at least once per specified interval. Otherwise, the session can be considered "idle" and can expire. See the timeouts section for more information.
Red Hat build of Keycloak supports offline tokens, which can be used typically when client needs to use refresh token even if corresponding browser SSO session is already expired.
10.1.1.5.1. Refresh token rotation
It is possible to specify that the refresh token is considered invalid once it is used. This means that client must always save the refresh token from the last refresh response because older refresh tokens, which were already used, would not be considered valid anymore by Red Hat build of Keycloak. This is possible to set with the use of Revoke Refresh token option as specified in the timeouts section.
Red Hat build of Keycloak also supports the situation that no refresh token rotation exists. In this case, a refresh token is returned during login, but subsequent responses from refresh-token requests will not return new refresh tokens. This practice is recommended for instance in the FAPI 2 draft specification in the securing apps section. In Red Hat build of Keycloak, it is possible to skip refresh token rotation with the use of client policies. You can add executor suppress-refresh-token-rotation
to some client profile and configure client policy to specify for which clients would be the profile triggered, which means that for those clients the refresh token rotation is going to be skipped.
10.1.1.6. Device authorization grant
This is used by clients running on internet-connected devices that have limited input capabilities or lack a suitable browser. Here’s a brief summary of the protocol:
- The application requests Red Hat build of Keycloak a device code and a user code. Red Hat build of Keycloak creates a device code and a user code. Red Hat build of Keycloak returns a response including the device code and the user code to the application.
- The application provides the user with the user code and the verification URI. The user accesses a verification URI to be authenticated by using another browser. You could define a short verification_uri that will be redirected to Red Hat build of Keycloak verification URI (/realms/realm_name/device)outside Red Hat build of Keycloak - fe in a proxy.
- The application repeatedly polls Red Hat build of Keycloak to find out if the user completed the user authorization. If user authentication is complete, the application exchanges the device code for an identity, access and refresh token.
10.1.1.7. Client initiated backchannel authentication grant
This feature is used by clients who want to initiate the authentication flow by communicating with the OpenID Provider directly without redirect through the user’s browser like OAuth 2.0’s authorization code grant. Here’s a brief summary of the protocol:
- The client requests Red Hat build of Keycloak an auth_req_id that identifies the authentication request made by the client. Red Hat build of Keycloak creates the auth_req_id.
- After receiving this auth_req_id, this client repeatedly needs to poll Red Hat build of Keycloak to obtain an Access Token, Refresh Token and ID Token from Red Hat build of Keycloak in return for the auth_req_id until the user is authenticated.
An administrator can configure Client Initiated Backchannel Authentication (CIBA) related operations as CIBA Policy
per realm.
Also please refer to other places of Red Hat build of Keycloak documentation like Backchannel Authentication Endpoint and Client Initiated Backchannel Authentication Grant in the securing apps section.
10.1.1.7.1. CIBA Policy
An administrator carries out the following operations on the Admin Console
:
-
Open the
Authentication
tab.CIBA Policy -
Configure items and click
Save
.
The configurable items and their description follow.
| Configuration | Description |
|---|---|
| Backchannel Token Delivery Mode | Specifying how the CD (Consumption Device) gets the authentication result and related tokens. There are three modes, "poll", "ping" and "push". Red Hat build of Keycloak only supports "poll". The default setting is "poll". This configuration is required. For more details, see CIBA Specification. |
| Expires In | The expiration time of the "auth_req_id" in seconds since the authentication request was received. The default setting is 120. This configuration is required. For more details, see CIBA Specification. |
| Interval | The interval in seconds the CD (Consumption Device) needs to wait for between polling requests to the token endpoint. The default setting is 5. This configuration is optional. For more details, see CIBA Specification. |
| Authentication Requested User Hint | The way of identifying the end-user for whom authentication is being requested. The default setting is "login_hint". There are three modes, "login_hint", "login_hint_token" and "id_token_hint". Red Hat build of Keycloak only supports "login_hint". This configuration is required. For more details, see CIBA Specification. |
10.1.1.7.2. Provider Setting
The CIBA grant uses the following two providers.
- Authentication Channel Provider: provides the communication between Red Hat build of Keycloak and the entity that actually authenticates the user via AD (Authentication Device).
-
User Resolver Provider: get
UserModel
of Red Hat build of Keycloak from the information provided by the client to identify the user.
Red Hat build of Keycloak has both default providers. However, the administrator needs to set up Authentication Channel Provider like this:
kc.[sh|bat] start --spi-ciba-auth-channel-ciba-http-auth-channel-http-authentication-channel-uri=https://backend.internal.example.com
The configurable items and their description follow.
| Configuration | Description |
|---|---|
| http-authentication-channel-uri | Specifying URI of the entity that actually authenticates the user via AD (Authentication Device). |
10.1.1.7.3. Authentication Channel Provider
CIBA standard document does not specify how to authenticate the user by AD. Therefore, it might be implemented at the discretion of products. Red Hat build of Keycloak delegates this authentication to an external authentication entity. To communicate with the authentication entity, Red Hat build of Keycloak provides Authentication Channel Provider.
Its implementation of Red Hat build of Keycloak assumes that the authentication entity is under the control of the administrator of Red Hat build of Keycloak so that Red Hat build of Keycloak trusts the authentication entity. It is not recommended to use the authentication entity that the administrator of Red Hat build of Keycloak cannot control.
Authentication Channel Provider is provided as SPI provider so that users of Red Hat build of Keycloak can implement their own provider in order to meet their environment. Red Hat build of Keycloak provides its default provider called HTTP Authentication Channel Provider that uses HTTP to communicate with the authentication entity.
If a user of Red Hat build of Keycloak user want to use the HTTP Authentication Channel Provider, they need to know its contract between Red Hat build of Keycloak and the authentication entity consisting of the following two parts.
- Authentication Delegation Request/Response
- Red Hat build of Keycloak sends an authentication request to the authentication entity.
- Authentication Result Notification/ACK
- The authentication entity notifies the result of the authentication to Red Hat build of Keycloak.
Authentication Delegation Request/Response consists of the following messaging.
- Authentication Delegation Request
- The request is sent from Red Hat build of Keycloak to the authentication entity to ask it for user authentication by AD.
POST [delegation_reception]
- Headers
| Name | Value | Description |
|---|---|---|
| Content-Type | application/json | The message body is json formatted. |
| Authorization | Bearer [token] | The [token] is used when the authentication entity notifies the result of the authentication to Red Hat build of Keycloak. |
- Parameters
| Type | Name | Description |
|---|---|---|
| Path | delegation_reception | The endpoint provided by the authentication entity to receive the delegation request |
- Body
| Name | Description |
|---|---|
| login_hint |
It tells the authentication entity who is authenticated by AD. |
| scope |
It tells which scopes the authentication entity gets consent from the authenticated user. |
| is_consent_required |
It shows whether the authentication entity needs to get consent from the authenticated user about the scope. |
| binding_message |
Its value is intended to be shown in both CD and AD’s UI to make the user recognize that the authentication by AD is triggered by CD. |
| acr_values |
It tells the requesting Authentication Context Class Reference from CD. |
- Authentication Delegation Response
The response is returned from the authentication entity to Red Hat build of Keycloak to notify that the authentication entity received the authentication request from Red Hat build of Keycloak.
- Responses
| HTTP Status Code | Description |
|---|---|
| 201 | It notifies Red Hat build of Keycloak of receiving the authentication delegation request. |
Authentication Result Notification/ACK consists of the following messaging.
- Authentication Result Notification
- The authentication entity sends the result of the authentication request to Red Hat build of Keycloak.
POST /realms/[realm]/protocol/openid-connect/ext/ciba/auth/callback
- Headers
| Name | Value | Description |
|---|---|---|
| Content-Type | application/json | The message body is json formatted. |
| Authorization | Bearer [token] | The [token] must be the one the authentication entity has received from Red Hat build of Keycloak in Authentication Delegation Request. |
- Parameters
| Type | Name | Description |
|---|---|---|
| Path | realm | The realm name |
- Body
| Name | Description |
|---|---|
| status |
It tells the result of user authentication by AD. |
- Authentication Result ACK
The response is returned from Red Hat build of Keycloak to the authentication entity to notify Red Hat build of Keycloak received the result of user authentication by AD from the authentication entity.
- Responses
| HTTP Status Code | Description |
|---|---|
| 200 | It notifies the authentication entity of receiving the notification of the authentication result. |
10.1.1.7.4. User Resolver Provider
Even if the same user, its representation may differ in each CD, Red Hat build of Keycloak and the authentication entity.
For CD, Red Hat build of Keycloak and the authentication entity to recognize the same user, this User Resolver Provider converts their own user representations among them.
User Resolver Provider is provided as SPI provider so that users of Red Hat build of Keycloak can implement their own provider in order to meet their environment. Red Hat build of Keycloak provides its default provider called Default User Resolver Provider that has the following characteristics.
-
Only support
login_hint
parameter and is used as default. -
username
of UserModel in Red Hat build of Keycloak is used to represent the user on CD, Red Hat build of Keycloak and the authentication entity.
10.1.2. OIDC Logout
OIDC has four specifications relevant to logout mechanisms:
Again since all of this is described in the OIDC specification we will only give a brief overview here.
10.1.2.1. Session Management
This is a browser-based logout. The application obtains session status information from Red Hat build of Keycloak at a regular basis. When the session is terminated at Red Hat build of Keycloak the application will notice and trigger its own logout.
10.1.2.2. RP-Initiated Logout
This is also a browser-based logout where the logout starts by redirecting the user to a specific endpoint at Red Hat build of Keycloak. This redirect usually happens when the user clicks the Log Out
link on the page of some application, which previously used Red Hat build of Keycloak to authenticate the user.
Once the user is redirected to the logout endpoint, Red Hat build of Keycloak is going to send logout requests to clients to let them invalidate their local user sessions, and potentially redirect the user to some URL once the logout process is finished. The user might be optionally requested to confirm the logout in case the id_token_hint
parameter was not used. After logout, the user is automatically redirected to the specified post_logout_redirect_uri
as long as it is provided as a parameter. Note that you need to include either the client_id
or id_token_hint
parameter in case the post_logout_redirect_uri
is included. Also the post_logout_redirect_uri
parameter needs to match one of the Valid Post Logout Redirect URIs
specified in the client configuration.
Depending on the client configuration, logout requests can be sent to clients through the front-channel or through the back-channel. For the frontend browser clients, which rely on the Session Management described in the previous section, Red Hat build of Keycloak does not need to send any logout requests to them; these clients automatically detect that SSO session in the browser is logged out.
10.1.2.3. Front-channel Logout
To configure clients to receive logout requests through the front-channel, look at the Front-Channel Logout client setting. When using this method, consider the following:
-
Logout requests sent by Red Hat build of Keycloak to clients rely on the browser and on embedded
iframes
that are rendered for the logout page. -
By being based on
iframes
, front-channel logout might be impacted by Content Security Policies (CSP) and logout requests might be blocked. - If the user closes the browser prior to rendering the logout page or before logout requests are actually sent to clients, their sessions at the client might not be invalidated.
Consider using Back-Channel Logout as it provides a more reliable and secure approach to log out users and terminate their sessions on the clients.
If the client is not enabled with front-channel logout, then Red Hat build of Keycloak is going to try first to send logout requests through the back-channel using the Back-Channel Logout URL. If not defined, the server is going to fall back to using the Admin URL.
10.1.2.4. Backchannel Logout
This is a non-browser-based logout that uses direct backchannel communication between Red Hat build of Keycloak and clients. Red Hat build of Keycloak sends a HTTP POST request containing a logout token to all clients logged into Red Hat build of Keycloak. These requests are sent to a registered backchannel logout URLs at Red Hat build of Keycloak and are supposed to trigger a logout at client side.
10.1.3. Red Hat build of Keycloak server OIDC URI endpoints
The following is a list of OIDC endpoints that Red Hat build of Keycloak publishes. These endpoints can be used when a non-Red Hat build of Keycloak client adapter uses OIDC to communicate with the authentication server. They are all relative URLs. The root of the URL consists of the HTTP(S) protocol, hostname, and optionally the path: For example
https://localhost:8080
- /realms/{realm-name}/protocol/openid-connect/auth
- Used for obtaining a temporary code in the Authorization Code Flow or obtaining tokens using the Implicit Flow, Direct Grants, or Client Grants.
- /realms/{realm-name}/protocol/openid-connect/token
- Used by the Authorization Code Flow to convert a temporary code into a token.
- /realms/{realm-name}/protocol/openid-connect/logout
- Used for performing logouts.
- /realms/{realm-name}/protocol/openid-connect/userinfo
- Used for the User Info service described in the OIDC specification.
- /realms/{realm-name}/protocol/openid-connect/revoke
- Used for OAuth 2.0 Token Revocation described in RFC7009.
- /realms/{realm-name}/protocol/openid-connect/certs
- Used for the JSON Web Key Set (JWKS) containing the public keys used to verify any JSON Web Token (jwks_uri)
- /realms/{realm-name}/protocol/openid-connect/auth/device
- Used for Device Authorization Grant to obtain a device code and a user code.
- /realms/{realm-name}/protocol/openid-connect/ext/ciba/auth
- This is the URL endpoint for Client Initiated Backchannel Authentication Grant to obtain an auth_req_id that identifies the authentication request made by the client.
- /realms/{realm-name}/protocol/openid-connect/logout/backchannel-logout
- This is the URL endpoint for performing backchannel logouts described in the OIDC specification.
In all of these, replace {realm-name} with the name of the realm.
10.2. SAML
SAML 2.0 is a similar specification to OIDC but more mature. It is descended from SOAP and web service messaging specifications so is generally more verbose than OIDC. SAML 2.0 is an authentication protocol that exchanges XML documents between authentication servers and applications. XML signatures and encryption are used to verify requests and responses.
In general, SAML implements two use cases.
The first use case is an application that requests the Red Hat build of Keycloak server authenticates a user. Upon successful login, the application will receive an XML document. This document contains an SAML assertion that specifies user attributes. The realm digitally signs the document which contains access information (such as user role mappings) that applications use to determine the resources users are allowed to access in the application.
The second use case is a client accessing remote services. The client requests a SAML assertion from Red Hat build of Keycloak to invoke on remote services on behalf of the user.
10.2.1. SAML bindings
Red Hat build of Keycloak supports three binding types.
10.2.1.1. Redirect binding
Redirect binding uses a series of browser redirect URIs to exchange information.
- A user connects to an application using a browser. The application detects the user is not authenticated.
- The application generates an XML authentication request document and encodes it as a query parameter in a URI. The URI is used to redirect to the Red Hat build of Keycloak server. Depending on your settings, the application can also digitally sign the XML document and include the signature as a query parameter in the redirect URI to Red Hat build of Keycloak. This signature is used to validate the client that sends the request.
- The browser redirects to Red Hat build of Keycloak.
- The server extracts the XML auth request document and verifies the digital signature, if required.
- The user enters their authentication credentials.
- After authentication, the server generates an XML authentication response document. The document contains a SAML assertion that holds metadata about the user, including name, address, email, and any role mappings the user has. The document is usually digitally signed using XML signatures, and may also be encrypted.
- The XML authentication response document is encoded as a query parameter in a redirect URI. The URI brings the browser back to the application. The digital signature is also included as a query parameter.
- The application receives the redirect URI and extracts the XML document.
- The application verifies the realm’s signature to ensure it is receiving a valid authentication response. The information inside the SAML assertion is used to make access decisions or display user data.
10.2.1.2. POST binding
POST binding is similar to Redirect binding but POST binding exchanges XML documents using POST requests instead of using GET requests. POST binding uses JavaScript to make the browser send a POST request to the Red Hat build of Keycloak server or application when exchanging documents. HTTP responds with an HTML document which contains an HTML form containing embedded JavaScript. When the page loads, the JavaScript automatically invokes the form.
POST binding is recommended due to two restrictions:
- Security — With Redirect binding, the SAML response is part of the URL. It is less secure as it is possible to capture the response in logs.
- Size — Sending the document in the HTTP payload provides more scope for large amounts of data than in a limited URL.
10.2.1.3. ECP
Enhanced Client or Proxy (ECP) is a SAML v.2.0 profile which allows the exchange of SAML attributes outside the context of a web browser. It is often used by REST or SOAP-based clients.
10.2.2. Red Hat build of Keycloak Server SAML URI Endpoints
Red Hat build of Keycloak has one endpoint for all SAML requests.
http(s)://authserver.host/realms/{realm-name}/protocol/saml
All bindings use this endpoint.
10.3. OpenID Connect compared to SAML
The following lists a number of factors to consider when choosing a protocol.
For most purposes, Red Hat build of Keycloak recommends using OIDC.
OIDC
- OIDC is specifically designed to work with the web.
- OIDC is suited for HTML5/JavaScript applications because it is easier to implement on the client side than SAML.
- OIDC tokens are in the JSON format which makes them easier for Javascript to consume.
- OIDC has features to make security implementation easier. For example, see the iframe trick that the specification uses to determine a users login status.
SAML
- SAML is designed as a layer to work on top of the web.
- SAML can be more verbose than OIDC.
- Users pick SAML over OIDC because there is a perception that it is mature.
- Users pick SAML over OIDC existing applications that are secured with it.
10.4. Docker registry v2 authentication
Docker authentication is disabled by default. To enable docker authentication, see the Enabling and disabling features chapter.
Docker Registry V2 Authentication is a protocol, similar to OIDC, that authenticates users against Docker registries. Red Hat build of Keycloak’s implementation of this protocol lets Docker clients use a Red Hat build of Keycloak authentication server authenticate against a registry. This protocol uses standard token and signature mechanisms but it does deviate from a true OIDC implementation. It deviates by using a very specific JSON format for requests and responses as well as mapping repository names and permissions to the OAuth scope mechanism.
10.4.1. Docker authentication flow
The authentication flow is described in the Docker API documentation. The following is a summary from the perspective of the Red Hat build of Keycloak authentication server:
-
Perform a
docker login
. - The Docker client requests a resource from the Docker registry. If the resource is protected and no authentication token is in the request, the Docker registry server responds with a 401 HTTP message with some information on the permissions that are required and the location of the authorization server.
-
The Docker client constructs an authentication request based on the 401 HTTP message from the Docker registry. The client uses the locally cached credentials (from the
docker login
command) as part of the HTTP Basic Authentication request to the Red Hat build of Keycloak authentication server. - The Red Hat build of Keycloak authentication server attempts to authenticate the user and return a JSON body containing an OAuth-style Bearer token.
- The Docker client receives a bearer token from the JSON response and uses it in the authorization header to request the protected resource.
- The Docker registry receives the new request for the protected resource with the token from the Red Hat build of Keycloak server. The registry validates the token and grants access to the requested resource (if appropriate).
Red Hat build of Keycloak does not create a browser SSO session after successful authentication with the Docker protocol. The browser SSO session does not use the Docker protocol as it cannot refresh tokens or obtain the status of a token or session from the Red Hat build of Keycloak server; therefore a browser SSO session is not necessary. For more details, see the transient session section.
10.4.2. Red Hat build of Keycloak Docker Registry v2 Authentication Server URI Endpoints
Red Hat build of Keycloak has one endpoint for all Docker auth v2 requests.
http(s)://authserver.host/realms/{realm-name}/protocol/docker-v2/auth
