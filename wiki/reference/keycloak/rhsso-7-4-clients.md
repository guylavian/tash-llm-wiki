---
title: "Chapter 8. Managing Clients - Red Hat Single Sign-On 7.4 Server Administration Guide"
type: reference
domain: keycloak
slug: rhsso-7-4-clients
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.4/html/server_administration_guide/clients
guide: server_administration_guide
version: 7.4
family: rhsso
documentKind: "Documentation"
---

# Chapter 8. Managing Clients - Red Hat Single Sign-On 7.4 Server Administration Guide

Chapter 8. Managing Clients
Clients are entities that can request authentication of a user. Clients come in two forms. The first type of client is an application that wants to participate in single-sign-on. These clients just want Red Hat Single Sign-On to provide security for them. The other type of client is one that is requesting an access token so that it can invoke other services on behalf of the authenticated user. This section discusses various aspects around configuring clients and various ways to do it.
8.1. OIDC Clients
OpenID Connect is the preferred protocol to secure applications. It was designed from the ground up to be web friendly and work best with HTML5/JavaScript applications.
To create an OIDC client go to the Clients
left menu item. On this page you’ll see a Create
button on the right.
Clients
This will bring you to the Add Client
page.
Add Client
Enter in the Client ID
of the client. This should be a simple alpha-numeric string that will be used in requests and in the Red Hat Single Sign-On database to identify the client. Next select openid-connect
in the Client Protocol
drop down box. Finally enter in the base URL of your application in the Root URL
field and click Save
. This will create the client and bring you to the client Settings
tab.
Client Settings
Let’s walk through each configuration item on this page.
Client ID
This specifies an alpha-numeric string that will be used as the client identifier for OIDC requests.
Name
This is the display name for the client whenever it is displayed in a Red Hat Single Sign-On UI screen. You can localize the value of this field by setting up a replacement string value i.e. ${myapp}. See the Server Developer Guide for more information.
Description
This specifies the description of the client. This can also be localized.
Enabled
If this is turned off, the client will not be allowed to request authentication.
Consent Required
If this is on, then users will get a consent page which asks the user if they grant access to that application. It will also display the metadata that the client is interested in so that the user knows exactly what information the client is getting access to. If you’ve ever done a social login to Google, you’ll often see a similar page. Red Hat Single Sign-On provides the same functionality.
Access Type
This defines the type of the OIDC client.
- confidential
- Confidential access type is for server-side clients that need to perform a browser login and require a client secret when they turn an access code into an access token, (see Access Token Request in the OAuth 2.0 spec for more details). This type should be used for server-side applications.
- public
- Public access type is for client-side clients that need to perform a browser login. With a client-side application there is no way to keep a secret safe. Instead it is very important to restrict access by configuring correct redirect URIs for the client.
- bearer-only
- Bearer-only access type means that the application only allows bearer token requests. If this is turned on, this application cannot participate in browser logins.
Standard Flow Enabled
If this is on, clients are allowed to use the OIDC Authorization Code Flow.
Implicit Flow Enabled
If this is on, clients are allowed to use the OIDC Implicit Flow.
Direct Access Grants Enabled
If this is on, clients are allowed to use the OIDC Direct Access Grants.
Root URL
If Red Hat Single Sign-On uses any configured relative URLs, this value is prepended to them.
Valid Redirect URIs
This is a required field. Enter in a URL pattern and click the + sign to add. Click the - sign next to URLs you want to remove. Remember that you still have to click the Save
button! Wildcards (*) are only allowed at the end of a URI, i.e. http://host.com/*
You should take extra precautions when registering valid redirect URI patterns. If you make them too general you are vulnerable to attacks. See Threat Model Mitigation chapter for more information.
Base URL
If Red Hat Single Sign-On needs to link to the client, this URL is used.
Admin URL
For Red Hat Single Sign-On specific client adapters, this is the callback endpoint for the client. The Red Hat Single Sign-On server will use this URI to make callbacks like pushing revocation policies, performing backchannel logout, and other administrative operations. For Red Hat Single Sign-On servlet adapters, this can be the root URL of the servlet application. For more information see Securing Applications and Services Guide.
Web Origins
This option centers around CORS which stands for Cross-Origin Resource Sharing. If browser JavaScript tries to make an AJAX HTTP request to a server whose domain is different from the one the JavaScript code came from, then the request must use CORS. The server must handle CORS requests in a special way, otherwise the browser will not display or allow the request to be processed. This protocol exists to protect against XSS, CSRF and other JavaScript-based attacks.
Red Hat Single Sign-On has support for validated CORS requests. The way it works is that the domains listed in the Web Origins
setting for the client are embedded within the access token sent to the client application. The client application can then use this information to decide whether or not to allow a CORS request to be invoked on it. This is an extension to the OIDC protocol so only Red Hat Single Sign-On client adapters support this feature. See Securing Applications and Services Guide for more information.
To fill in the Web Origins
data, enter in a base URL and click the + sign to add. Click the - sign next to URLs you want to remove. Remember that you still have to click the Save
button!
8.1.1. Advanced Settings
OAuth 2.0 Mutual TLS Certificate Bound Access Tokens Enabled
Mutual TLS binds an access token and a refresh token with a client certificate exchanged during TLS handshake. This prevents an attacker who finds a way to steal these tokens from exercising the tokens. This type of token is called a holder-of-key token. Unlike bearer tokens, the recipient of a holder-of-key token can verify whether the sender of the token is legitimate.
If the following conditions are satisfied on a token request, Red Hat Single Sign-On will bind an access token and a refresh token with a client certificate and issue them as holder-of-key tokens. If all conditions are not met, Red Hat Single Sign-On rejects the token request.
- The feature is turned on
- A token request is sent to the token endpoint in an authorization code flow or a hybrid flow
- On TLS handshake, Red Hat Single Sign-On requests a client certificate and a client send its client certificate
- On TLS handshake, Red Hat Single Sign-On successfully verifies the client certificate
To enable mutual TLS in Red Hat Single Sign-On, see Enable mutual SSL in WildFly.
In the following cases, Red Hat Single Sign-On will verify the client sending the access token or the refresh token; if verification fails, Red Hat Single Sign-On rejects the token.
- A token refresh request is sent to the token endpoint with a holder-of-key refresh token
- A UserInfo request is sent to UserInfo endpoint with a holder-of-key access token
- A logout request is sent to Logout endpoint with a holder-of-key refresh token
Please see Mutual TLS Client Certificate Bound Access Tokens in the OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens for more details.
None of the keycloak client adapters currently support holder-of-key token verification. Instead, keycloak adapters currently treat access and refresh tokens as bearer tokens.
Proof Key for Code Exchange (PKCE)
When an attacker steals an authorization code that was issued to a legitimate client, PKCE prevents the attacker from receiving the tokens that apply to that code.
The administrator can select the following three options:
Proof Key for Code Exchange Code Challenge Method
- (blank) : Red Hat Single Sign-On does not apply PKCE unless the client sends PKCE’s parameters appropriately to Red Hat Single Sign-On’s authorization endpoint. It is the default setting.
- S256 : Red Hat Single Sign-On applies to the client PKCE whose code challenge method is S256.
- plain : Red Hat Single Sign-On applies to the client PKCE whose code challenge method is plain.
Please see RFC 7636 Proof Key for Code Exchange by OAuth Public Clients for more details.
Signed and Encrypted ID Token Support
Red Hat Single Sign-On can encrypt ID token according to Json Web Encryption (JWE) specification. The administrator can determine whether encrypting ID token or not per client. This feature is disabled as default.
The key for encrypting ID token is called Content Encryption Key (CEK). Red Hat Single Sign-On and a client need to negotiate which CEK is used and how to deliver it. The way to do so is called Key Management Mode.
JWE specification determines 5 types of Key Management Mode. Red Hat Single Sign-On supports Key Encryption among them.
In Key Encryption, the client generates a key pair of asymmetric cryptography. The public key is used to encrypt CEK. Red Hat Single Sign-On generates CEK per ID token, encrypts the ID token by this generated CEK and encrypts this CEK by this client’s public key. The client decrypts this encrypted CEK by their private key, and decrypt the ID token by decrypted CEK. Therefore, any party other than the client is not able to decrypt ID token.
The client needs to pass their public key for encrypting CEK onto Red Hat Single Sign-On. Red Hat Single Sign-On supports downloading public keys from the URL the client provides. The client needs to provide their public keys according to Json Web Keys (JWK) specification. The way to do so is defined in Signed JWT
of Confidential Client Credentials. The detailed procedure is as follows:
-
open the client’s
Credentials
tab -
select
Signed Jwt
fromClient Authenticator
pulldown menu -
set ON to
JWKS URL
switch -
input the client’s public key providing URL on
JWKS URL
textbox
Key Encryption’s algorithms are defined in Json Web Algorithm (JWA) specification. Red Hat Single Sign-On supports RSAES-PKCS1-v1_5(RSA1_5) and RSAES OAEP using default parameters (RSA-OAEP). The detailed procedure to select this algorithm is as follows:
-
open the client’s
Settings
tab -
open
Advanced Settings
-
select
RSA1_5
orRSA-OAEP
fromID Token Encryption Key Management Algorithm
pulldown menu
ID token encryption algorithms by CEK are also defined in JWA specification. Red Hat Single Sign-On supports AES_128_CBC_HMAC_SHA_256 authenticated encryption (A128CBC-HS256) and AES GCM using 128-bit key (A128GCM). The detailed procedure to select this algorithm is as follows:
-
open the client’s
Settings
tab -
open
Advanced Settings
-
select
A128CBC-HS256
orA128GCM
fromID Token Encryption Content Encryption Algorithm
pulldown menu
8.1.2. Confidential Client Credentials
If you’ve set the client’s access type to confidential
in the client’s Settings
tab, a new Credentials
tab will show up. As part of dealing with this type of client you have to configure the client’s credentials.
Credentials Tab
The Client Authenticator
list box specifies the type of credential you are going to use for your confidential client. It defaults to client ID and secret. The secret is automatically generated for you and the Regenerate Secret
button allows you to recreate this secret if you want or need to.
Alternatively, you can opt to use a signed Json Web Token (JWT) or x509 certificate validation (also called Mutual TLS) instead of a secret.
Signed JWT
When choosing this credential type you will have to also generate a private key and certificate for the client. The private key will be used to sign the JWT, while the certificate is used by the server to verify the signature. Click on the Generate new keys and certificate
button to start this process.
Generate Keys
When you generate these keys, Red Hat Single Sign-On will store the certificate, and you’ll need to download the private key and certificate for your client to use. Pick the archive format you want and specify the password for the private key and store.
You can also opt to generate these via an external tool and just import the client’s certificate.
Import Certificate
There are multiple formats you can import from, just choose the archive format you have the certificate stored in, select the file, and click the Import
button.
Finally note that you don’t even need to import certificate if you choose to Use JWKS URL
. In that case, you can provide the URL where client publishes its public key in JWK format. This is flexible because when client changes its keys, Red Hat Single Sign-On will automatically download them without need to re-import anything on Red Hat Single Sign-On side.
If you use client secured by Red Hat Single Sign-On adapter, you can configure the JWKS URL like https://myhost.com/myapp/k_jwks assuming that https://myhost.com/myapp is the root URL of your client application. See Server Developer Guide for additional details.
For the performance purposes, Red Hat Single Sign-On caches the public keys of the OIDC clients. If you think that private key of your client was compromised, it is obviously good to update your keys, but it’s also good to clear the keys cache. See Clearing the cache section for more details.
Signed JWT with Client Secret
If you select this option in the Client Authenticator
list box, you can use a JWT signed by client secret instead of the private key.
This client secret will be used to sign the JWT by the client.
X509 Certificate
By enabling this option Red Hat Single Sign-On will validate if the client uses proper X509 certificate during the TLS Handshake.
This option requires mutual TLS in Red Hat Single Sign-On, see Enable mutual SSL in WildFly.
X509 Certificate
The validator checks also the certificate’s Subject DN field with configured regexp validation expression. For some use cases, it is sufficient to accept all certificates. In that case, you can use (.*?)(?:$)
expression.
There are two ways for Red Hat Single Sign-On to obtain the Client ID from the request. The first option is the client_id
parameter in the query (described in Section 2.2 of the OAuth 2.0 Specification). The second option is to supply client_id
as a form parameter.
8.1.3. Service Accounts
Each OIDC client has a built-in service account which allows it to obtain an access token. This is covered in the OAuth 2.0 specifiation under Client Credentials Grant. To use this feature you must set the Access Type of your client to confidential
. When you do this, the Service Accounts Enabled
switch will appear. You need to turn on this switch. Also make sure that you have configured your client credentials.
To use it you must have registered a valid confidential
Client and you need to check the switch Service Accounts Enabled
in Red Hat Single Sign-On admin console for this client. In tab Service Account Roles
you can configure the roles available to the service account retrieved on behalf of this client. Remember that you must have the roles available in Role Scope Mappings (tab Scope
) of this client as well, unless you have Full Scope Allowed
on. As in a normal login, roles from access token are the intersection of:
- Role scope mappings of particular client combined with the role scope mappings inherited from linked client scopes
- Service account roles
The REST URL to invoke on is /auth/realms/{realm-name}/protocol/openid-connect/token
. Invoking on this URL is a POST request and requires you to post the client credentials. By default, client credentials are represented by clientId and clientSecret of the client in Authorization: Basic
header, but you can also authenticate the client with a signed JWT assertion or any other custom mechanism for client authentication. You also need to use the parameter grant_type=client_credentials
as per the OAuth2 specification.
For example the POST invocation to retrieve a service account can look like this:
POST /auth/realms/demo/protocol/openid-connect/token
Authorization: Basic cHJvZHVjdC1zYS1jbGllbnQ6cGFzc3dvcmQ=
Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials
The response would be this standard JSON document from the OAuth 2.0 specification.
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache
{
"access_token":"2YotnFZFEjr1zCsicMWpAA",
"token_type":"bearer",
"expires_in":60
}
Only the access token is returned by default. No refresh token is returned and also no user session is created on the Red Hat Single Sign-On side upon successful authentication by default. Due the lack of refresh token, there is a need to re-authenticate when the access token expires, however this does not mean any additional overhead on the Red Hat Single Sign-On server side because sessions are not created by default.
In this situation, logout is unnecessary. However, issued access tokens can be revoked by sending requests to the OAuth2 Revocation Endpoint as described in the OpenID Connect Endpoints section.
8.1.4. Audience Support
The typical environment where the Red Hat Single Sign-On is deployed generally consists of a set of confidential or public client applications (frontend client applications) which use Red Hat Single Sign-On for authentication.
There are also services (called Resource Servers in the OAuth 2 specification), which serve requests from frontend client applications and provide resources. These services typically require an Access token (Bearer token) to be sent to them to authenticate for a particular request. This token was previously obtained by the frontend application when it tries to log in against Red Hat Single Sign-On.
In the environment where the trust among services is low, you may encounter this scenario:
-
A frontend client called
my-app
is required to be authenticated against Red Hat Single Sign-On. -
A user is authenticated in Red Hat Single Sign-On. Red Hat Single Sign-On then issued tokens to the
my-app
application. -
The application
my-app
used the token to invoke the serviceevil-service
. The application needs to invokeevil-service
as the service is able to serve some very useful data. -
The
evil-service
application returned the response tomy-app
. However, at the same time, it kept the token previously sent to it. -
The
evil-service
application then invoked another service calledgood-service
with the previously kept token. The invocation was successful andgood-service
returned the data. This results in broken security as theevil-service
misused the token to access other services on behalf of the clientmy-app
.
This flow may not be an issue in many environments with the high level of trust among services. However in other environments, where the trust among services is lower, this can be problematic.
In some environments, this example work flow may be even requested behavior as the evil-service
may need to retrieve additional data from good-service
to be able to properly return the requested data to the original caller (my-app client). You may notice similarities with the Kerberos Credential Delegation. As with the Kerberos Credential Delegation, an unlimited audience is a mixed blessing as it is only useful when a high level of trust exists among services. Otherwise, it is recommended to limit audience as described next. You can limit audience and at the same time allow the evil-service
to retrieve required data from the good-service
. In this case, you need to ensure that both the evil-service
and good-service
are added as audiences to the token.
To prevent any misuse of the access token as in the example above, it is recommended to limit Audience on the token and configure your services to verify the audience on the token. If this is done, the flow above will change, like this:
-
A frontend client called
my-app
is required to be authenticated against Red Hat Single Sign-On. -
A user is authenticated in Red Hat Single Sign-On. Red Hat Single Sign-On then issued tokens to the
my-app
application. The client application already knows that it will need to invoke serviceevil-service
, so it usedscope=evil-service
in the authentication request sent to the Red Hat Single Sign-On server. See Client Scopes section for more details about the scope parameter. The token issued to themy-app
client contains the audience, as in"audience": [ "evil-service" ]
, which declares that the client wants to use this access token to invoke just the serviceevil-service
. -
The
evil-service
application served the request to themy-app
. At the same time, it kept the token previously sent to it. -
The
evil-service
application then invoked thegood-service
with the previously kept token. Invocation was not successful becausegood-service
checks the audience on the token and it sees that audience is onlyevil-service
. This is expected behavior and security is not broken.
If the client wants to invoke the good-service
later, it will need to obtain another token by issuing the SSO login with the scope=good-service
. The returned token will then contain good-service
as an audience:
"audience": [ "good-service" ]
and can be used to invoke good-service
.
8.1.4.1. Setup
To properly set up audience checking:
- Ensure that services are configured to check audience on the access token sent to them by adding the flag verify-token-audience in the adapter configuration. See Adapter configuration for details.
- Ensure that when an access token is issued by Red Hat Single Sign-On, it contains all requested audiences and does not contain any audiences that are not needed. The audience can be either automatically added due the client roles as described in the next section or it can be hardcoded as described below.
8.1.4.2. Automatically add audience
In the default client scope roles, there is an Audience Resolve protocol mapper defined. This protocol mapper will check all the clients for which current token has at least one client role available. Then the client ID of each of those clients will be added as an audience automatically. This is especially useful if your service (usually bearer-only) clients rely on client roles.
As an example, let us assume that you have a bearer-only client good-service
and the confidential client my-app
, which you want to authenticate and then use the access token issued for the my-app
to invoke the good-service
REST service. If the following are true:
-
The
good-service
client has any client roles defined on itself - Target user has at least one of those client roles assigned
-
Client
my-app
has the role scope mappings for the assigned role
then the good-service
will be automatically added as an audience to the access token issued for the my-app
.
If you want to ensure that audience is not added automatically, do not configure role scope mappings directly on the my-app
client, but instead create a dedicated client scope, for example called good-service
, which will contain the role scope mappings for the client roles of the good-service
client. Assuming that this client scope will be added as an optional client scope to the my-app
client, the client roles and audience will be added to the token just if explicitly requested by the scope=good-service
parameter.
The frontend client itself is not automatically added to the access token audience. This allows for easy differentiation between the access token and the ID token, because the access token will not contain the client for which the token was issued as an audience. So in the example above, the my-app
won’t be added as an audience. If you need the client itself as an audience, see the hardcoded audience option. However, using the same client as both frontend and REST service is not recommended.
8.1.4.3. Hardcoded audience
For the case when your service relies on realm roles or does not rely on the roles in the token at all, it can be useful to use hardcoded audience. This is a protocol mapper, which will add client ID of the specified service client as an audience to the token. You can even use any custom value, for example some URL, if you want different audience than client ID.
You can add protocol mapper directly to the frontend client, however than the audience will be always added. If you want more fine-grain control, you can create protocol mapper on the dedicated client scope, which will be called for example good-service
.
Audience Protocol Mapper
-
From the Installation tab of the
good-service
client, you can generate the adapter configuration and you can confirm that verify-token-audience option will be set to true. This indicates that the adapter will require verifying the audience if you use this generated configuration. -
Finally, you need to ensure that the
my-app
frontend client is able to requestgood-service
as an audience in its tokens. On themy-app
client, click the Client Scopes tab. Then assigngood-service
as an optional (or default) client scope. See Client Scopes Linking section for more details. -
You can optionally Evaluate Client Scopes and generate an example access token. If you do, notice that
good-service
will be added to the audience of the generated access token only ifgood-service
is included in the scope parameter in the case you assigned it as an optional client scope. -
In your
my-app
application, you must ensure that scope parameter is used with the valuegood-service
always included when you want to issue the token for accessing thegood-service
. See the parameters forwarding section, if your application uses the servlet adapter, or the javascript adapter section, if your application uses the javascript adapter.
If you are unsure what the correct audience and roles in the token will be, it is always a good idea to Evaluate Client Scopes in the admin console and do some testing around it.
Both the Audience and Audience Resolve protocol mappers add the audiences just to the access token by default. The ID Token typically contains only single audience, which is the client ID of the client for which the token was issued. This is a requirement of the OpenID Connect specification. On the other hand, the access token does not necessarily have the client ID of the client, which was the token issued for, unless any of the audience mappers added it.
8.2. SAML Clients
Red Hat Single Sign-On supports SAML 2.0 for registered applications. Both POST and Redirect bindings are supported. You can choose to require client signature validation and can have the server sign and/or encrypt responses as well.
To create a SAML client go to the Clients
left menu item. On this page you’ll see a Create
button on the right.
Clients
This will bring you to the Add Client
page.
Add Client
Enter in the Client ID
of the client. This is often a URL and will be the expected issuer
value in SAML requests sent by the application. Next select saml
in the Client Protocol
drop down box. Finally enter in the Client SAML Endpoint
URL. Enter the URL you want the Red Hat Single Sign-On server to send SAML requests and responses to. Usually applications have only one URL for processing SAML requests. If your application has different URLs for its bindings, don’t worry, you can fix this in the Settings
tab of the client. Click Save
. This will create the client and bring you to the client Settings
tab.
Client Settings
- Client ID
- This value must match the issuer value sent with AuthNRequests. Red Hat Single Sign-On will pull the issuer from the Authn SAML request and match it to a client by this value.
- Name
- This is the display name for the client whenever it is displayed in a Red Hat Single Sign-On UI screen. You can localize the value of this field by setting up a replacement string value i.e. ${myapp}. See the Server Developer Guide for more information.
- Description
- This specifies the description of the client. This can also be localized.
- Enabled
- If this is turned off, the client will not be allowed to request authentication.
- Consent Required
- If this is on, then users will get a consent page which asks the user if they grant access to that application. It will also display the metadata that the client is interested in so that the user knows exactly what information the client is getting access to. If you’ve ever done a social login to Google, you’ll often see a similar page. Red Hat Single Sign-On provides the same functionality.
- Include AuthnStatement
-
SAML login responses may specify the authentication method used (password, etc.) as well as timestamps of the login and the session expiration. This is enabled by default, which means that
AuthStatement
element will be included in login responses. Note that setting this to off would prevent the client from determining the maximum session length which could result into never expiring client session. - Sign Documents
- When turned on, Red Hat Single Sign-On will sign the document using the realm’s private key.
- Optimize REDIRECT signing key lookup
-
When turned on, the SAML protocol messages will include Red Hat Single Sign-On native extension that contains a hint with signing key ID. When the SP understands this extension, it can use it for signature validation instead of attempting to validate signature with all known keys. This option only applies to REDIRECT bindings where the signature is transferred in query parameters where there is no place with this information in the signature information (contrary to POST binding messages where key ID is always included in document signature). Currently this is relevant to situations where both IDP and SP are provided by Red Hat Single Sign-On server and adapter. This option is only relevant when
Sign Documents
is switched on. - Sign Assertions
-
The
Sign Documents
switch signs the whole document. With this setting the assertion is also signed and embedded within the SAML XML Auth response. - Signature Algorithm
- Choose between a variety of algorithms for signing SAML documents.
- SAML Signature Key Name
-
Signed SAML documents sent via POST binding contain identification of signing key in
KeyName
element. This by default contains Red Hat Single Sign-On key ID. However various vendors might expect a different key name or no key name at all. This switch controls whetherKeyName
contains key ID (optionKEY_ID
), subject from certificate corresponding to the realm key (optionCERT_SUBJECT
- expected for instance by Microsoft Active Directory Federation Services), or that the key name hint is completely omitted from the SAML message (optionNONE
). - Canonicalization Method
- Canonicalization method for XML signatures.
- Encrypt Assertions
- Encrypt assertions in SAML documents with the realm’s private key. The AES algorithm is used with a key size of 128 bits.
- Client Signature Required
-
Expect that documents coming from a client are signed. Red Hat Single Sign-On will validate this signature using the client public key or cert set up in the
SAML Keys
tab. - Force POST Binding
- By default, Red Hat Single Sign-On will respond using the initial SAML binding of the original request. By turning on this switch, you will force Red Hat Single Sign-On to always respond using the SAML POST Binding even if the original request was the Redirect binding.
- Front Channel Logout
- If true, this application requires a browser redirect to be able to perform a logout. For example, the application may require a cookie to be reset which could only be done via a redirect. If this switch is false, then Red Hat Single Sign-On will invoke a background SAML request to logout the application.
- Force Name ID Format
- If the request has a name ID policy, ignore it and used the value configured in the admin console under Name ID Format
- Name ID Format
- Name ID Format for the subject. If no name ID policy is specified in the request or if the Force Name ID Format attribute is true, this value is used. Properties used for each of the respective formats are defined below.
- Root URL
- If Red Hat Single Sign-On uses any configured relative URLs, this value is prepended to them.
- Valid Redirect URIs
-
This is an optional field. Enter in a URL pattern and click the + sign to add. Click the - sign next to URLs you want to remove. Remember that you still have to click the
Save
button! Wildcards (*) are only allowed at the end of a URI, i.e. http://host.com/*. This field is used when the exact SAML endpoints are not registered and Red Hat Single Sign-On is pulling the Assertion Consumer URL from the request. - Base URL
- If Red Hat Single Sign-On needs to link to the client, this URL would be used.
- Master SAML Processing URL
- This URL will be used for all SAML requests and the response will be directed to the SP. It will be used as the Assertion Consumer Service URL and the Single Logout Service URL. If a login request contains the Assertion Consumer Service URL, that will take precedence, but this URL must be validated by a registered Valid Redirect URI pattern
- Assertion Consumer Service POST Binding URL
- POST Binding URL for the Assertion Consumer Service.
- Assertion Consumer Service Redirect Binding URL
- Redirect Binding URL for the Assertion Consumer Service.
- Logout Service POST Binding URL
- POST Binding URL for the Logout Service.
- Logout Service Redirect Binding URL
- Redirect Binding URL for the Logout Service.
8.2.1. IDP Initiated Login
IDP Initiated Login is a feature that allows you to set up an endpoint on the Red Hat Single Sign-On server that will log you into a specific application/client. In the Settings
tab for your client, you need to specify the IDP Initiated SSO URL Name
. This is a simple string with no whitespace in it. After this you can reference your client at the following URL: root/auth/realms/{realm}/protocol/saml/clients/{url-name}
The IDP initiated login implementation prefers POST over REDIRECT binding (check saml bindings for more information). Therefore the final binding and SP URL are selected in the following way:
-
If the specific
Assertion Consumer Service POST Binding URL
is defined (insideFine Grain SAML Endpoint Configuration
section of the client settings) POST binding is used through that URL. -
If the general
Master SAML Processing URL
is specified then POST binding is used again throught this general URL. -
As the last resort, if the
Assertion Consumer Service Redirect Binding URL
is configured (insideFine Grain SAML Endpoint Configuration
) REDIRECT binding is used with this URL.
If your client requires a special relay state, you can also configure this on the Settings
tab in the IDP Initiated SSO Relay State
field. Alternatively, browsers can specify the relay state in a RelayState
query parameter, i.e. root/auth/realms/{realm}/protocol/saml/clients/{url-name}?RelayState=thestate
.
When using identity brokering, it is possible to set up an IDP Initiated Login for a client from an external IDP. The actual client is set up for IDP Initiated Login at broker IDP as described above. The external IDP has to set up the client for application IDP Initiated Login that will point to a special URL pointing to the broker and representing IDP Initiated Login endpoint for a selected client at the brokering IDP. This means that in client settings at the external IDP:
-
IDP Initiated SSO URL Name
is set to a name that will be published as IDP Initiated Login initial point, Assertion Consumer Service POST Binding URL
in theFine Grain SAML Endpoint Configuration
section has to be set to the following URL:broker-root/auth/realms/{broker-realm}/broker/{idp-name}/endpoint/clients/{client-id}
, where:- broker-root is base broker URL
- broker-realm is name of the realm at broker where external IDP is declared
- idp-name is name of the external IDP at broker
-
client-id is the value of
IDP Initiated SSO URL Name
attribute of the SAML client defined at broker. It is this client, which will be made available for IDP Initiated Login from the external IDP.
Please note that you can import basic client settings from the brokering IDP into client settings of the external IDP - just use SP Descriptor available from the settings of the identity provider in the brokering IDP, and add clients/client-id
to the endpoint URL.
8.2.2. SAML Entity Descriptors
Instead of manually registering a SAML 2.0 client, you can import it via a standard SAML Entity Descriptor XML file. There is an Import
option on the Add Client page.
Add Client
Click the Select File
button and load your entity descriptor file. You should review all the information there to make sure everything is set up correctly.
Some SAML client adapters like mod-auth-mellon need the XML Entity Descriptor for the IDP. You can obtain this by going to this public URL: root/auth/realms/{realm}/protocol/saml/descriptor
8.3. Client Links
For scenarios where one wants to link from one client to another, Red Hat Single Sign-On provides a special redirect endpoint: /realms/realm_name/clients/{client-id}/redirect
.
If a client accesses this endpoint via an HTTP GET
request, Red Hat Single Sign-On returns the configured base URL for the provided Client and Realm in the form of an HTTP 307
(Temporary Redirect) via the response’s Location
header.
Thus, a client only needs to know the Realm name and the Client ID in order to link to them. This indirection helps avoid hard-coding client base URLs.
As an example, given the realm master
and the client-id account
:
http://host:port/auth/realms/master/clients/account/redirect
Would temporarily redirect to: http://host:port/auth/realms/master/account
8.4. OIDC Token and SAML Assertion Mappings
Applications that receive ID Tokens, Access Tokens, or SAML assertions may need or want different user metadata and roles. Red Hat Single Sign-On allows you to define what exactly is transferred. You can hardcode roles, claims and custom attributes. You can pull user metadata into a token or assertion. You can rename roles. Basically you have a lot of control of what exactly goes back to the client.
Within the Admin Console, if you go to an application you’ve registered, you’ll see a Mappers
tab. Here’s one for an OIDC based client.
Mappers Tab
The new client does not have any built-in mappers, however it usually inherits some mappers from the client scopes as described in the client scopes section. Protocol mappers map things like, for example, email address to a specific claim in the identity and access token. Their function should each be self explanatory from their name. There are additional pre-configured mappers that are not attached to the client that you can add by clicking the Add Builtin
button.
Each mapper has common settings as well as additional ones depending on which type of mapper you are adding. Click the Edit
button next to one of the mappers in the list to get to the config screen.
Mapper Config
The best way to learn about a config option is to hover over its tooltip.
Most OIDC mappers also allow you to control where the claim gets put. You can opt to include or exclude the claim from both the id and access tokens by fiddling with the Add to ID token
and Add to access token
switches.
Finally, you can also add other mapper types. If you go back to the Mappers
tab, click the Create
button.
Add Mapper
Pick a Mapper Type
from the list box. If you hover over the tooltip, you’ll see a description of what that mapper type does. Different config parameters will appear for different mapper types.
8.4.1. Priority order
Mapper implementations have priority order. This priority order is not the configuration property of the mapper; rather, it is the property of the concrete implementation of the mapper.
Mappers are sorted in the admin console by the order in the list of mappers and the changes in the token or assertion will be applied using that order with the lowest being applied first. This means that implementations which are dependent on other implementations are processed in the needed order.
For example, when we first want to compute the roles which will be included with a token, we first resolve audiences based on those roles. Then, we process a JavaScript script that uses the roles and audiences already available in the token.
8.4.2. OIDC User Session Note Mappers
User session details are via mappers and depend on various criteria. User session details are automatically included when you use or enable a feature on a client. You can also click the Add builtin
button to include session details.
Impersonated user sessions provide the following details:
-
IMPERSONATOR_ID
: The ID of an impersonating user -
IMPERSONATOR_USERNAME
: The username of an impersonating user
Service account sessions provide the following details:
-
clientId
: The client ID of the service account -
clientAddress
: The remote host IP of the service account authenticated device -
clientHost
: The remote host name of the service account authenticated device
8.4.3. Script Mapper
The Script Mapper
allows you to map claims to tokens by running a user-defined JavaScript code. For more details about how to deploy scripts to the server, please take a look at JavaScript Providers.
Once you have your scripts deployed, you should be able to select the scripts you deployed from the list of available mappers.
8.5. Generating Client Adapter Config
The Red Hat Single Sign-On can pre-generate configuration files that you can use to install a client adapter for in your application’s deployment environment. A number of adapter types are supported for both OIDC and SAML. Go to the Installation
tab of the client you want to generate configuration for.
Select the Format Option
you want configuration generated for. All Red Hat Single Sign-On client adapters for OIDC and SAML are supported. The mod-auth-mellon Apache HTTPD adapter for SAML is supported as well as standard SAML entity descriptor files.
8.6. Client Scopes
If you have many applications you need to secure and register within your organization, it can become tedious to configure the protocol mappers and role scope mappings for each of these clients. Red Hat Single Sign-On allows you to define a shared client configuration in an entity called a client scope.
Client scopes also provide support for the OAuth 2 scope
parameter, which allows a client application to request more or fewer claims or roles in the access token, according to the application needs.
To create a client scope, follow these steps:
-
Go to the
Client Scopes
left menu item. This initial screen shows you a list of currently defined client scopes.
Client Scopes List
-
Click the
Create
button. Name the client scope and save. A client scope will have similar tabs to a regular clients. You can define protocol mappers and role scope mappings, which can be inherited by other clients, and which are configured to inherit from this client scope.
8.6.1. Protocol
When you are creating the client scope, you must choose the Protocol
. Only the clients which use same protocol can then be linked with this client scope.
Once you have created new realm, you can see that there is a list of pre-defined (builtin) client scopes in the menu.
-
For the SAML protocol, there is one builtin client scope,
roles_list
, which contains one protocol mapper for showing the roles list in the SAML assertion. -
For the OpenID Connect protocol, there are client scopes
profile
,email
,address
,phone
,offline_access
,roles
,web-origins
andmicroprofile-jwt
.
The client scope, offline_access
, is useful when client wants to obtain offline tokens. Learn about offline tokens in the Offline Access section or in the OpenID Connect specification, where scope parameter is defined with the value offline_access
.
The client scopes profile
, email
, address
and phone
are also defined in the OpenID Connect specification. These client scopes do not have any role scope mappings defined, but they have some protocol mappers defined, and these mappers correspond to the claims defined in the OpenID Connect specification.
For example, when you click to open the phone
client scope and open the Mappers
tab, you will see the protocol mappers, which correspond to the claims defined in the specification for the scope phone
.
Client Scope Mappers
When the phone
client scope is linked to a client, that client automatically inherits all the protocol mappers defined in the phone
client scope. Access tokens issued for this client will contain the phone number information about the user, assuming that the user has a defined phone number.
Builtin client scopes contain exactly the protocol mappers as defined per the specification, however you are free to edit client scopes and create/update/remove any protocol mappers (or role scope mappings).
The client scope roles
is not defined in the OpenID Connect specification and it is also not added automatically to the scope
claim in the access token. This client scope has some mappers, which are used to add roles of the user to the access token and possibly add some audiences for the clients with at least one client role as described in the Audience section.
The client scope web-origins
is also not defined in the OpenID Connect specification and not added to the scope
claim. This is used to add allowed web origins to the access token allowed-origins
claim.
The client scope microprofile-jwt
was created to handle the claims defined in the MicroProfile/JWT Auth Specification. This client scope defines a user property mapper for the upn
claim and also a realm role mapper for the groups
claim. These mappers can be changed as needed so that different properties can be used to create the MicroProfile/JWT specific claims.
8.6.3. Link Client Scope with the Client
Linking between client scope and client is configured in the Client Scopes
tab of the particular client. There are 2 ways of linking between client scope and client.
- Default Client Scopes
- This is applicable for both OpenID Connect and SAML clients. Default client scopes are always applied when issuing OpenID Connect tokens or SAML assertions for this client. The client will inherit Protocol mappers and Role Scope Mappings defined on the client scope. For the OpenID Connect Protocol, the Mappers and Role Scope Mappings are always applied, regardless of the value used for the scope parameter in the OpenID Connect authorization request.
- Optional Client Scopes
-
This is applicable only for OpenID Connect clients. Optional client scopes are applied when issuing tokens for this client, but only when they are requested by the
scope
parameter in the OpenID Connect authorization request.
8.6.3.1. Example
For this example, we assume that the client has profile
and email
linked as default client scopes, and phone
and address
are linked as optional client scopes. The client will use the value of the scope parameter when sending a request to the OpenID Connect authorization endpoint:
scope=openid phone
The scope parameter contains the string, with the scope values divided by space (which is also the reason why a client scope name cannot contain a space character in it). The value openid
is the meta-value used for all OpenID Connect requests, so we will ignore it for this example. The token will contain mappers and role scope mappings from the client scopes profile
, email
(which are default scopes) and phone
(an optional client scope requested by the scope parameter).
8.6.4. Evaluating Client Scopes
The tabs Mappers
and Scope
of the client contain the protocol mappers and role scope mappings declared solely for this client. They do not contain the mappers and scope mappings inherited from client scopes. However, it may be useful to see what the effective protocol mappers will be (protocol mappers defined on the client itself as well as inherited from the linked client scopes) and the effective role scope mappings used when you generate the token for the particular client.
You can see all of these when you click the Client Scopes
tab for the client and then open the sub-tab Evaluate
. From here you can select the optional client scopes that you want to apply. This will also show you the value of the scope
parameter, which needs to be sent from the application to the Red Hat Single Sign-On OpenID Connect authorization endpoint.
Evaluating Client Scopes
If you want to see how you can send a custom value for a scope
parameter from your application, see the parameters forwarding section, if your application uses the servlet adapter, or the javascript adapter section, if your application uses the javascript adapter.
8.6.4.1. Generating Example Tokens
To see an example of a real access token, generated for the particular user and issued for the particular client, with the specified value of scope
parameter, select the user from the Evaluate
screen. This will generate an example token that includes all of the claims and role mappings used.
8.6.5. Client Scopes Permissions
When issuing tokens for a particular user, the client scope is applied only if the user is permitted to use it. In the case that a client scope does not have any role scope mappings defined on itself, then each user is automatically permitted to use this client scope. However, when a client scope has any role scope mappings defined on itself, then the user must be a member of at least one of the roles. In other words, there must be an intersection between the user roles and the roles of the client scope. Composite roles are taken into account when evaluating this intersection.
If a user is not permitted to use the client scope, then no protocol mappers or role scope mappings will be used when generating tokens and the client scope will not appear in the scope value in the token.
8.6.6. Realm Default Client Scopes
The Realm Default Client Scopes
allow you to define set of client scopes, which will be automatically linked to newly created clients.
Open the left menu item Client Scopes
and then select Default Client Scopes
.
From here, select the client scopes that you want to add as Default Client Scopes
to newly created clients and Optional Client Scopes
to newly created clients.
Default Client Scopes
Once the client is created, you can unlink the default client scopes, if needed. This is similar to how you remove Default Roles.
8.6.7. Scopes explained
The term scope
is used in Red Hat Single Sign-On on few places. Various occurrences of scopes are related to each other, but may have a different context and meaning. To clarify, here we explain the various scopes
used in Red Hat Single Sign-On.
- Client scope
-
Referenced in this chapter. Client scopes are entities in Red Hat Single Sign-On, which are configured at the realm level and they can be linked to clients. The client scopes are referenced by their name when a request is sent to the Red Hat Single Sign-On authorization endpoint with a corresponding value of the
scope
parameter. The details are described in the section about client scopes linking. - Role scope mapping
-
This can be seen when you open tab
Scope
of a client or client scope. Role scope mapping allows you to limit the roles which can be used in the access tokens. The details are described in the Role Scope Mappings section.
