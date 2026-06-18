---
title: "Chapter 13. Managing OpenID Connect and SAML Clients - Red Hat build of Keycloak 26.0 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-assembly-managing-clients-server-administration-guide
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_administration_guide/assembly-managing-clients_server_administration_guide
guide: server_administration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 13. Managing OpenID Connect and SAML Clients - Red Hat build of Keycloak 26.0 Server Administration Guide

Chapter 13. Managing OpenID Connect and SAML Clients
Clients are entities that can request authentication of a user. Clients come in two forms. The first type of client is an application that wants to participate in single sign-on. These clients just want Red Hat build of Keycloak to provide security for them. The other type of client is one that is requesting an access token so that it can invoke other services on behalf of the authenticated user. This section discusses various aspects around configuring clients and various ways to do it.
13.1. Managing OpenID Connect clients
OpenID Connect is the recommended protocol to secure applications. It was designed from the ground up to be web friendly and it works best with HTML5/JavaScript applications.
13.1.1. Creating an OpenID Connect client
To protect an application that uses the OpenID connect protocol, you create a client.
Procedure
- Click Clients in the menu.
Click Create client.
Create client
- Leave Client type set to OpenID Connect.
Enter a Client ID.
This ID is an alphanumeric string that is used in OIDC requests and in the Red Hat build of Keycloak database to identify the client.
Supply a Name for the client.
If you plan to localize this name, set up a replacement string value. For example, a string value such as ${myapp}. See the Server Developer Guide for more information.
- Click Save.
This action creates the client and bring you to the Settings tab, where you can perform Basic configuration.
13.1.2. Basic configuration
The Settings tab includes many options to configure this client.
Settings tab
13.1.2.1. General Settings
- Client ID
- The alphanumeric ID string that is used in OIDC requests and in the Red Hat build of Keycloak database to identify the client.
- Name
- The name for the client in Red Hat build of Keycloak UI screen. To localize the name, set up a replacement string value. For example, a string value such as ${myapp}. See the Server Developer Guide for more information.
- Description
- The description of the client. This setting can also be localized.
- Always Display in Console
- Always list this client in the Account Console even if this user does not have an active session.
13.1.2.2. Access Settings
- Root URL
- If Red Hat build of Keycloak uses any configured relative URLs, this value is prepended to them.
- Home URL
- Provides the default URL for when the auth server needs to redirect or link back to the client.
- Valid Redirect URIs
Required field. Enter a URL pattern and click + to add and - to remove existing URLs and click Save. Exact (case sensitive) string matching is used to compare valid redirect URIs.
You can use wildcards at the end of the URL pattern. For example
http://host.com/path/*
. To avoid security issues, if the passed redirect URI contains the userinfo part or its path manages access to parent directory (/../
) no wildcard comparison is performed but the standard and secure exact string matching.The full wildcard
*
valid redirect URI can also be configured to allow any http or https redirect URI. Please do not use it in production environments.Exclusive redirect URI patterns are typically more secure. See Unspecific Redirect URIs for more information.
- Web Origins
Enter a URL pattern and click + to add and - to remove existing URLs. Click Save.
This option handles Cross-Origin Resource Sharing (CORS). If browser JavaScript attempts an AJAX HTTP request to a server whose domain is different from the one that the JavaScript code came from, the request must use CORS. The server must handle CORS requests, otherwise the browser will not display or allow the request to be processed. This protocol protects against XSS, CSRF, and other JavaScript-based attacks.
Domain URLs listed here are embedded within the access token sent to the client application. The client application uses this information to decide whether to allow a CORS request to be invoked on it. Only Red Hat build of Keycloak client adapters support this feature. See Securing applications and Services guide for more information.
- Admin URL
- Callback endpoint for a client. The server uses this URL to make callbacks like pushing revocation policies, performing backchannel logout, and other administrative operations. For Red Hat build of Keycloak servlet adapters, this URL can be the root URL of the servlet application. For more information, see Securing applications and Services guide.
13.1.2.3. Capability Config
- Client authentication
The type of OIDC client.
ON
For server-side clients that perform browser logins and require client secrets when making an Access Token Request. This setting should be used for server-side applications.
OFF
For client-side clients that perform browser logins. As it is not possible to ensure that secrets can be kept safe with client-side clients, it is important to restrict access by configuring correct redirect URIs.
- Authorization
- Enables or disables fine-grained authorization support for this client.
- Standard Flow
- If enabled, this client can use the OIDC Authorization Code Flow.
- Direct Access Grants
- If enabled, this client can use the OIDC Direct Access Grants.
- Implicit Flow
- If enabled, this client can use the OIDC Implicit Flow.
- Service account roles
-
If enabled, this client can authenticate to Red Hat build of Keycloak and retrieve access token dedicated to this client. In terms of OAuth2 specification, this enables support of
Client Credentials Grant
for this client. - Auth 2.0 Device Authorization Grant
- If enabled, this client can use the OIDC Device Authorization Grant.
- OIDC CIBA Grant
- If enabled, this client can use the OIDC Client Initiated Backchannel Authentication Grant.
13.1.2.4. Login settings
- Login theme
- A theme to use for login, OTP, grant registration, and forgotten password pages.
- Consent required
If enabled, users have to consent to client access.
For client-side clients that perform browser logins. As it is not possible to ensure that secrets can be kept safe with client-side clients, it is important to restrict access by configuring correct redirect URIs.
- Display client on screen
This switch applies if Consent Required is Off.
Off
The consent screen will contain only the consents corresponding to configured client scopes.
On
There will be also one item on the consent screen about this client itself.
- Client consent screen text
- Applies if Consent required and Display client on screen are enabled. Contains the text that will be on the consent screen about permissions for this client.
13.1.2.5. Logout settings
- Front channel logout
-
If Front Channel Logout is enabled, the application should be able to log out users through the front channel as per OpenID Connect Front-Channel Logout specification. If enabled, you should also provide the
Front-Channel Logout URL
. - Front-channel logout URL
- URL that will be used by Red Hat build of Keycloak to send logout requests to clients through the front-channel.
- Backchannel logout URL
- URL that will cause the client to log itself out when a logout request is sent to this realm (via end_session_endpoint). If omitted, no logout requests are sent to the client.
- Backchannel logout session required
- Specifies whether a session ID Claim is included in the Logout Token when the Backchannel Logout URL is used.
- Backchannel logout revoke offline sessions
- Specifies whether a revoke_offline_access event is included in the Logout Token when the Backchannel Logout URL is used. Red Hat build of Keycloak will revoke offline sessions when receiving a Logout Token with this event.
13.1.3. Advanced configuration
After completing the fields on the Settings tab, you can use the other tabs to perform advanced configuration.
13.1.3.1. Advanced tab
When you click the Advanced tab, additional fields are displayed. For details on a specific field, click the question mark icon for that field. However, certain fields are described in detail in this section.
13.1.3.2. Fine grain OpenID Connect configuration
Logo URL
URL that references a logo for the Client application.
Policy URL
URL that the Relying Party Client provides to the End-User to read about how the profile data will be used.
Terms of Service URL
URL that the Relying Party Client provides to the End-User to read about the Relying Party’s terms of service.
Signed and Encrypted ID Token Support
Red Hat build of Keycloak can encrypt ID tokens according to the Json Web Encryption (JWE) specification. The administrator determines if ID tokens are encrypted for each client.
The key used for encrypting the ID token is the Content Encryption Key (CEK). Red Hat build of Keycloak and a client must negotiate which CEK is used and how it is delivered. The method used to determine the CEK is the Key Management Mode. The Key Management Mode that Red Hat build of Keycloak supports is Key Encryption.
In Key Encryption:
- The client generates an asymmetric cryptographic key pair.
- The public key is used to encrypt the CEK.
- Red Hat build of Keycloak generates a CEK per ID token
- Red Hat build of Keycloak encrypts the ID token using this generated CEK
- Red Hat build of Keycloak encrypts the CEK using the client’s public key.
- The client decrypts this encrypted CEK using their private key
- The client decrypts the ID token using the decrypted CEK.
No party, other than the client, can decrypt the ID token.
The client must pass its public key for encrypting CEK to Red Hat build of Keycloak. Red Hat build of Keycloak supports downloading public keys from a URL provided by the client. The client must provide public keys according to the Json Web Keys (JWK) specification.
The procedure is:
- Open the client’s Keys tab.
- Toggle JWKS URL to ON.
- Input the client’s public key URL in the JWKS URL textbox.
Key Encryption’s algorithms are defined in the Json Web Algorithm (JWA) specification. Red Hat build of Keycloak supports:
- RSAES-PKCS1-v1_5(RSA1_5)
- RSAES OAEP using default parameters (RSA-OAEP)
- RSAES OAEP 256 using SHA-256 and MFG1 (RSA-OAEP-256)
The procedure to select the algorithm is:
- Open the client’s Advanced tab.
- Open Fine Grain OpenID Connect Configuration.
- Select the algorithm from ID Token Encryption Content Encryption Algorithm pulldown menu.
13.1.3.3. OpenID Connect Compatibility Modes
This section exists for backward compatibility. Click the question mark icons for details on each field.
OAuth 2.0 Mutual TLS Certificate Bound Access Tokens Enabled
Mutual TLS binds an access token and a refresh token together with a client certificate, which is exchanged during a TLS handshake. This binding prevents an attacker from using stolen tokens.
This type of token is a holder-of-key token. Unlike bearer tokens, the recipient of a holder-of-key token can verify if the sender of the token is legitimate.
If this setting is on, the workflow is:
- A token request is sent to the token endpoint in an authorization code flow or hybrid flow.
- Red Hat build of Keycloak requests a client certificate.
- Red Hat build of Keycloak receives the client certificate.
- Red Hat build of Keycloak successfully verifies the client certificate.
If verification fails, Red Hat build of Keycloak rejects the token.
In the following cases, Red Hat build of Keycloak will verify the client sending the access token or the refresh token:
- A token refresh request is sent to the token endpoint with a holder-of-key refresh token.
- A UserInfo request is sent to UserInfo endpoint with a holder-of-key access token.
- A logout request is sent to non-OIDC compliant Red Hat build of Keycloak proprietary Logout endpoint with a holder-of-key refresh token.
See Mutual TLS Client Certificate Bound Access Tokens in the OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens for more details.
Red Hat build of Keycloak client adapters do not support holder-of-key token verification. Red Hat build of Keycloak adapters treat access and refresh tokens as bearer tokens.
OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP)
DPoP binds an access token and a refresh token together with the public part of a client’s key pair. This binding prevents an attacker from using stolen tokens.
This type of token is a holder-of-key token. Unlike bearer tokens, the recipient of a holder-of-key token can verify if the sender of the token is legitimate.
If the client switch OAuth 2.0 DPoP Bound Access Tokens Enabled
is on, the workflow is:
- A token request is sent to the token endpoint in an authorization code flow or hybrid flow.
- Red Hat build of Keycloak requests a DPoP proof.
- Red Hat build of Keycloak receives the DPoP proof.
- Red Hat build of Keycloak successfully verifies the DPoP proof.
If verification fails, Red Hat build of Keycloak rejects the token.
If the switch OAuth 2.0 DPoP Bound Access Tokens Enabled
is off, the client can still send DPoP
proof in the token request. In that case, Red Hat build of Keycloak will verify DPoP proof and will add the thumbprint to the token. But if the switch is off, DPoP binding is not enforced by the Red Hat build of Keycloak server for this client. It is recommended to have this switch on if you want to make sure that particular client always uses DPoP binding.
In the following cases, Red Hat build of Keycloak will verify the client sending the access token or the refresh token:
- A token refresh request is sent to the token endpoint with a holder-of-key refresh token. This verification is done only for public clients as described in the DPoP specification. For confidential clients, the verification is not done as client authentication with proper client credentials is in place to ensure that request comes from the legitimate client. For public clients, both access tokens and refresh tokens are DPoP bound. For confidential clients, only access tokens are DPoP bound.
- A UserInfo request is sent to UserInfo endpoint with a holder-of-key access token.
- A logout request is sent to a non-OIDC compliant Red Hat build of Keycloak proprietary logout endpoint Logout endpoint with a holder-of-key refresh token. This verification is done only for public clients as described above.
See OAuth 2.0 Demonstrating Proof of Possession (DPoP) for more details.
Red Hat build of Keycloak client adapters do not support DPoP holder-of-key token verification. Red Hat build of Keycloak adapters treat access and refresh tokens as bearer tokens.
DPoP is Technology Preview and is not fully supported. This feature is disabled by default.
To enable start the server with --features=preview
or --features=dpop
Advanced Settings for OIDC
The Advanced Settings for OpenID Connect allows you to configure overrides at the client level for session and token timeouts.
| Configuration | Description |
|---|---|
| Access Token Lifespan | The value overrides the realm option with same name. |
| Client Session Idle | The value overrides the realm option with same name. The value should be shorter than the global SSO Session Idle. |
| Client Session Max | The value overrides the realm option with same name. The value should be shorter than the global SSO Session Max. |
| Client Offline Session Idle | This setting allows you to configure a shorter offline session idle timeout for the client. The timeout is amount of time the session remains idle before Red Hat build of Keycloak revokes its offline token. If not set, realm Offline Session Idle is used. |
| Client Offline Session Max | This setting allows you to configure a shorter offline session max lifespan for the client. The lifespan is the maximum time before Red Hat build of Keycloak revokes the corresponding offline token. This option needs Offline Session Max Limited enabled globally in the realm, and defaults to Offline Session Max. |
Proof Key for Code Exchange Code Challenge Method
If an attacker steals an authorization code of a legitimate client, Proof Key for Code Exchange (PKCE) prevents the attacker from receiving the tokens that apply to the code.
An administrator can select one of these options:
- (blank)
- Red Hat build of Keycloak does not apply PKCE unless the client sends appropriate PKCE parameters to Red Hat build of Keycloaks authorization endpoint.
- S256
- Red Hat build of Keycloak applies to the client PKCE whose code challenge method is S256.
- plain
- Red Hat build of Keycloak applies to the client PKCE whose code challenge method is plain.
See RFC 7636 Proof Key for Code Exchange by OAuth Public Clients for more details.
ACR to Level of Authentication (LoA) Mapping
In the advanced settings of a client, you can define which Authentication Context Class Reference (ACR)
value is mapped to which Level of Authentication (LoA)
. This mapping can be specified also at the realm as mentioned in the ACR to LoA Mapping. A best practice is to configure this mapping at the realm level, which allows to share the same settings across multiple clients.
The Default ACR Values
can be used to specify the default values when the login request is sent from this client to Red Hat build of Keycloak without acr_values
parameter and without a claims
parameter that has an acr
claim attached. See official OIDC dynamic client registration specification.
Note that default ACR values are used as the default level, however it cannot be reliably used to enforce login with the particular level. For example, assume that you configure the Default ACR Values
to level 2. Then by default, users will be required to authenticate with level 2. However when the user explicitly attaches the parameter into login request such as acr_values=1
, then the level 1 will be used. As a result, if the client really requires level 2, the client is encouraged to check the presence of the acr
claim inside ID Token and double-check that it contains the requested level 2.
For further details see Step-up Authentication and the official OIDC specification.
13.1.4. Confidential client credentials
If the Client authentication of the client is set to ON, the credentials of the client must be configured under the Credentials tab.
Credentials tab
The Client Authenticator drop-down list specifies the type of credential to use for your client.
Client ID and Secret
This choice is the default setting. The secret is automatically generated. Click Regenerate to recreate the secret if necessary.
Signed JWT
Signed JWT is "Signed JSON Web Token".
In this authenticator you can enforce the Signature algorithm used by the client (any algorithm is valid by default) and the Max expiration allowed for the JWT token (tokens received after this period will not be accepted because they are too old, note that tokens should be issued right before the authentication, 60 seconds by default).
When choosing this credential type you will have to also generate a private key and certificate for the client in the tab Keys
. The private key will be used to sign the JWT, while the certificate is used by the server to verify the signature.
Keys tab
Click on the Generate new keys
button to start this process.
Generate keys
- Select the archive format you want to use.
- Enter a key password.
- Enter a store password.
- Click Generate.
When you generate the keys, Red Hat build of Keycloak will store the certificate and you download the private key and certificate for your client.
You can also generate keys using an external tool and then import the client’s certificate by clicking Import Certificate.
Import certificate
- Select the archive format of the certificate.
- Enter the store password.
- Select the certificate file by clicking Import File.
- Click Import.
Importing a certificate is unnecessary if you click Use JWKS URL. In this case, you can provide the URL where the public key is published in JWK format. With this option, if the key is ever changed, Red Hat build of Keycloak reimports the key.
If you are using a client secured by Red Hat build of Keycloak adapter, you can configure the JWKS URL in this format, assuming that https://myhost.com/myapp is the root URL of your client application:
https://myhost.com/myapp/k_jwks
See Server Developer Guide for more details.
Signed JWT with Client Secret
If you select this option, you can use a JWT signed by client secret instead of the private key.
The client secret will be used to sign the JWT by the client.
Like in the Signed JWT authenticator you can configure the Signature algorithm and the Max expiration for the JWT token.
X509 Certificate
Red Hat build of Keycloak will validate if the client uses proper X509 certificate during the TLS Handshake.
X509 certificate
The validator also checks the Subject DN field of the certificate with a configured regexp validation expression. For some use cases, it is sufficient to accept all certificates. In that case, you can use (.*?)(?:$)
expression.
Two ways exist for Red Hat build of Keycloak to obtain the Client ID from the request:
-
The
client_id
parameter in the query (described in Section 2.2 of the OAuth 2.0 Specification). -
Supply
client_id
as a form parameter.
13.1.5. Client Secret Rotation
Please note that Client Secret Rotation support is in development. Use this feature experimentally.
For a client with Confidential Client authentication Red Hat build of Keycloak supports the functionality of rotating client secrets through Client Policies.
The client secrets rotation policy provides greater security in order to alleviate problems such as secret leakage. Once enabled, Red Hat build of Keycloak supports up to two concurrently active secrets for each client. The policy manages rotations according to the following settings:
- Secret expiration: [seconds] - When the secret is rotated, this is the expiration of time of the new secret. The amount, in seconds, added to the secret creation date. Calculated at policy execution time.
- Rotated secret expiration: [seconds] - When the secret is rotated, this value is the remaining expiration time for the old secret. This value should be always smaller than Secret expiration. When the value is 0, the old secret will be immediately removed during client rotation. The amount, in seconds, added to the secret rotation date. Calculated at policy execution time.
- Remaining expiration time for rotation during update: [seconds] - Time period when an update to a dynamic client should perform client secret rotation. Calculated at policy execution time.
When a client secret rotation occurs, a new main secret is generated and the old client main secret becomes the secondary secret with a new expiration date.
13.1.5.1. Rules for client secret rotation
Rotations do not occur automatically or through a background process. In order to perform the rotation, an update action is required on the client, either through the Red Hat build of Keycloak Admin Console through the function of Regenerate Secret, in the client’s credentials tab or Admin REST API. When invoking a client update action, secret rotation occurs according to the rules:
- When the value of Secret expiration is less than the current date.
- During dynamic client registration client-update request, the client secret will be automatically rotated if the value of Remaining expiration time for rotation during update match the period between the current date and the Secret expiration.
Additionally it is possible through Admin REST API to force a client secret rotation at any time.
During the creation of new clients, if the client secret rotation policy is active, the behavior will be applied automatically.
To apply the secret rotation behavior to an existing client, update that client after you define the policy so that the behavior is applied.
13.1.6. Creating an OIDC Client Secret Rotation Policy
The following is an example of defining a secret rotation policy:
Procedure
- Click Realm Settings in the menu.
- Click Client Policies tab.
On the Profiles page, click Create client profile.
Create a profile
- Enter any name for Name.
- Enter a description that helps you identify the purpose of the profile for Description.
Click Save.
This action creates the profile and enables you to configure executors.
Click Add executor to configure an executor for this profile.
Create a profile executor
- Select secret-rotation for Executor Type.
- Enter the maximum duration time of each secret, in seconds, for Secret Expiration.
Enter the maximum duration time of each rotated secret, in seconds, for Rotated Secret Expiration.
WarningRemember that the Rotated Secret Expiration value must always be less than Secret Expiration.
- Enter the amount of time, in seconds, after which any update action will update the client for Remain Expiration Time.
Click Add.
In the example above:
- Each secret is valid for one week.
- The rotated secret expires after two days.
- The window for updating dynamic clients starts one day before the secret expires.
- Return to the Client Policies tab.
- Click Policies.
Click Create client policy.
Create the Client Secret Rotation Policy
- Enter any name for Name.
- Enter a description that helps you identify the purpose of the policy for Description.
Click Save.
This action creates the policy and enables you to associate policies with profiles. It also allows you to configure the conditions for policy execution.
Under Conditions, click Add condition.
Create the Client Secret Rotation Policy Condition
To apply the behavior to all confidential clients select client-access-type in the Condition Type field
NoteTo apply to a specific group of clients, another approach would be to select the client-roles type in the Condition Type field. In this way, you could create specific roles and assign a custom rotation configuration to each role.
- Add confidential to the field Client Access Type.
- Click Add.
Back in the policy setting, under Client Profiles, click Add client profile and then select Weekly Client Secret Rotation Profile from the list and then click Add.
Client Secret Rotation Policy
To apply the secret rotation behavior to an existing client, follow the following steps:
Using the Admin Console
- Click Clients in the menu.
- Click a client.
- Click the Credentials tab.
- Click Re-generate of the client secret.
Using client REST services it can be executed in two ways:
- Through an update operation on a client
- Through the regenerate client secret endpoint
13.1.7. Using a service account
Each OIDC client has a built-in service account. Use this service account to obtain an access token.
Procedure
- Click Clients in the menu.
- Select your client.
- Click the Settings tab.
- Toggle Client authentication to On.
- Select Service accounts roles.
- Click Save.
- Configure your client credentials.
- Click the Scope tab.
- Verify that you have roles or toggle Full Scope Allowed to ON.
- Click the Service Account Roles tab
- Configure the roles available to this service account for your client.
Roles from access tokens are the intersection of:
- Role scope mappings of a client combined with the role scope mappings inherited from linked client scopes.
- Service account roles.
The REST URL to invoke is /realms/{realm-name}/protocol/openid-connect/token
. This URL must be invoked as a POST request and requires that you post the client credentials with the request.
By default, client credentials are represented by the clientId and clientSecret of the client in the Authorization: Basic header but you can also authenticate the client with a signed JWT assertion or any other custom mechanism for client authentication.
You also need to set the grant_type parameter to "client_credentials" as per the OAuth2 specification.
For example, the POST invocation to retrieve a service account can look like this:
POST /realms/demo/protocol/openid-connect/token
Authorization: Basic cHJvZHVjdC1zYS1jbGllbnQ6cGFzc3dvcmQ=
Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials
The response would be similar to this Access Token Response from the OAuth 2.0 specification.
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache
{
"access_token":"2YotnFZFEjr1zCsicMWpAA",
"token_type":"bearer",
"expires_in":60
}
Only the access token is returned by default. No refresh token is returned and no user session is created on the Red Hat build of Keycloak side upon successful authentication by default. Due to the lack of a refresh token, re-authentication is required when the access token expires. However, this situation does not mean any additional overhead for the Red Hat build of Keycloak server because sessions are not created by default.
In this situation, logout is unnecessary. However, issued access tokens can be revoked by sending requests to the OAuth2 Revocation Endpoint as described in the OpenID Connect Endpoints section.
13.1.8. Audience support
Typically, the environment where Red Hat build of Keycloak is deployed consists of a set of confidential or public client applications that use Red Hat build of Keycloak for authentication.
Services (Resource Servers in the OAuth 2 specification) are also available that serve requests from client applications and provide resources to these applications. These services require an Access token (Bearer token) to be sent to them to authenticate a request. This token is obtained by the frontend application upon login to Red Hat build of Keycloak.
In the environment where trust among services is low, you may encounter this scenario:
- A frontend client application requires authentication against Red Hat build of Keycloak.
- Red Hat build of Keycloak authenticates a user.
- Red Hat build of Keycloak issues a token to the application.
- The application uses the token to invoke an untrusted service.
- The untrusted service returns the response to the application. However, it keeps the applications token.
- The untrusted service then invokes a trusted service using the applications token. This results in broken security as the untrusted service misuses the token to access other services on behalf of the client application.
This scenario is unlikely in environments with a high level of trust between services but not in environments where trust is low. In some environments, this workflow may be correct as the untrusted service may have to retrieve data from a trusted service to return data to the original client application.
An unlimited audience is useful when a high level of trust exists between services. Otherwise, the audience should be limited. You can limit the audience and, at the same time, allow untrusted services to retrieve data from trusted services. In this case, ensure that the untrusted service and the trusted service are added as audiences to the token.
To prevent any misuse of the access token, limit the audience on the token and configure your services to verify the audience on the token. The flow will change as follows:
- A frontend application authenticates against Red Hat build of Keycloak.
- Red Hat build of Keycloak authenticates a user.
Red Hat build of Keycloak issues a token to the application. The application knows that it will need to invoke an untrusted service so it places scope=<untrusted service> in the authentication request sent to Red Hat build of Keycloak (see Client Scopes section for more details about the scope parameter).
The token issued to the application contains a reference to the untrusted service in its audience ("audience": [ "<untrusted service>" ]) which declares that the client uses this access token to invoke the untrusted service.
- The untrusted service invokes a trusted service with the token. Invocation is not successful because the trusted service checks the audience on the token and find that its audience is only for the untrusted service. This behavior is expected and security is not broken.
If the client wants to invoke the trusted service later, it must obtain another token by reissuing the SSO login with scope=<trusted service>. The returned token will then contain the trusted service as an audience:
"audience": [ "<trusted service>" ]
Use this value to invoke the <trusted service>.
13.1.8.1. Setup
When setting up audience checking:
- Ensure that services are configured to check audience on the access token sent to them. This may be done in a way specific to your client OIDC adapter, which you are using to secure your OIDC client application.
- Ensure that access tokens issued by Red Hat build of Keycloak contain all necessary audiences. Audiences can be added using the client roles as described in the next section or hardcoded. See Hardcoded audience.
13.1.8.2. Automatically add audience
An Audience Resolve protocol mapper is defined in the default client scope roles. The mapper checks for clients that have at least one client role available for the current token. The client ID of each client is then added as an audience, which is useful if your service clients rely on client roles. Service client could be usually a client without any flows enabled, which may not have any tokens issued directly to itself. It represents an OAuth 2 Resource Server.
For example, for a service client and a confidential client, you can use the access token issued for the confidential client to invoke the service client REST service. The service client will be automatically added as an audience to the access token issued for the confidential client if the following are true:
- The service client has any client roles defined on itself.
- Target user has at least one of those client roles assigned.
- Confidential client has the role scope mappings for the assigned role.
If you want to ensure that the audience is not added automatically, do not configure role scope mappings directly on the confidential client. Instead, you can create a dedicated client scope that contains the role scope mappings for the client roles of your dedicated client scope.
Assuming that the client scope is added as an optional client scope to the confidential client, the client roles and the audience will be added to the token if explicitly requested by the scope=<trusted service> parameter.
The frontend client itself is not automatically added to the access token audience, therefore allowing easy differentiation between the access token and the ID token, since the access token will not contain the client for which the token is issued as an audience.
If you need the client itself as an audience, see the hardcoded audience option. However, using the same client as both frontend and REST service is not recommended.
13.1.8.3. Hardcoded audience
When your service relies on realm roles or does not rely on the roles in the token at all, it can be useful to use a hardcoded audience. A hardcoded audience is a protocol mapper, that will add the client ID of the specified service client as an audience to the token. You can use any custom value, for example a URL, if you want to use a different audience than the client ID.
You can add the protocol mapper directly to the frontend client. If the protocol mapper is added directly, the audience will always be added as well.
For more control over the protocol mapper, you can create the protocol mapper on the dedicated client scope, which will be called for example good-service.
Audience protocol mapper
- From the Client details tab of the good-service client, you can generate the adapter configuration and confirm that verify-token-audience is set to true. This action forces the adapter to verify the audience if you use this configuration.
You need to ensure that the confidential client is able to request good-service as an audience in its tokens.
On the confidential client:
- Click the Client Scopes tab.
Assign good-service as an optional (or default) client scope.
See Client Scopes Linking section for more details.
- You can optionally Evaluate Client Scopes and generate an example access token. good-service will be added to the audience of the generated access token if good-service is included in the scope parameter, when you assigned it as an optional client scope.
In your confidential client application, ensure that the scope parameter is used. The value good-service must be included when you want to issue the token for accessing good-service.
See:
- Keycloak JavaScript adapter in the securing apps section if your application uses the javascript adapter.
Both the Audience and Audience Resolve protocol mappers add the audiences to the access token only, by default. The ID Token typically contains only a single audience, the client ID for which the token was issued, a requirement of the OpenID Connect specification. However, the access token does not necessarily have the client ID, which was the token issued for, unless the audience mappers added it.
13.2. Creating a SAML client
Red Hat build of Keycloak supports SAML 2.0 for registered applications. POST and Redirect bindings are supported. You can choose to require client signature validation. You can have the server sign and/or encrypt responses as well.
Procedure
- Click Clients in the menu.
- Click Create client to go to the Create client page.
Set Client type to SAML.
Create client
- Enter the Client ID of the client. This is often a URL and is the expected issuer value in SAML requests sent by the application.
- Click Save. This action creates the client and brings you to the Settings tab.
The following sections describe each setting on this tab.
13.2.1. Settings tab
The Settings tab includes many options to configure this client.
Client settings
13.2.1.1. General settings
- Client ID
- The alphanumeric ID string that is used in OIDC requests and in the Red Hat build of Keycloak database to identify the client. This value must match the issuer value sent with AuthNRequests. Red Hat build of Keycloak pulls the issuer from the Authn SAML request and match it to a client by this value.
- Name
- The name for the client in a Red Hat build of Keycloak UI screen. To localize the name, set up a replacement string value. For example, a string value such as ${myapp}. See the Server Developer Guide for more information.
- Description
- The description of the client. This setting can also be localized.
- Always Display in Console
- Always list this client in the Account Console even if this user does not have an active session.
13.2.1.2. Access Settings
- Root URL
- When Red Hat build of Keycloak uses a configured relative URL, this value is prepended to the URL.
- Home URL
- If Red Hat build of Keycloak needs to link to a client, this URL is used.
- Valid Redirect URIs
- Enter a URL pattern and click the + sign to add. Click the - sign to remove. Click Save to save these changes. Wildcards values are allowed only at the end of a URL. For example, http://host.com/*$$. This field is used when the exact SAML endpoints are not registered and Red Hat build of Keycloak pulls the Assertion Consumer URL from a request.
- IDP-Initiated SSO URL name
- URL fragment name to reference client when you want to do IDP Initiated SSO. Leaving this empty will disable IDP Initiated SSO. The URL you will reference from your browser will be: server-root/realms/{realm}/protocol/saml/clients/{client-url-name}
- IDP Initiated SSO Relay State
- Relay state you want to send with SAML request when you want to do IDP Initiated SSO.
- Master SAML Processing URL
This URL is used for all SAML requests and the response is directed to the SP. It is used as the Assertion Consumer Service URL and the Single Logout Service URL.
If login requests contain the Assertion Consumer Service URL then those login requests will take precedence. This URL must be validated by a registered Valid Redirect URI pattern.
13.2.1.3. SAML capabilities
- Name ID Format
- The Name ID Format for the subject. This format is used if no name ID policy is specified in a request, or if the Force Name ID Format attribute is set to ON.
- Force Name ID Format
- If a request has a name ID policy, ignore it and use the value configured in the Admin Console under Name ID Format.
- Force POST Binding
- By default, Red Hat build of Keycloak responds using the initial SAML binding of the original request. By enabling Force POST Binding, Red Hat build of Keycloak responds using the SAML POST binding even if the original request used the redirect binding.
- Force artifact binding
- If enabled, response messages are returned to the client through the SAML ARTIFACT binding system.
- Include AuthnStatement
- SAML login responses may specify the authentication method used, such as password, as well as timestamps of the login and the session expiration. Include AuthnStatement is enabled by default, so that the AuthnStatement element will be included in login responses. Setting this to OFF prevents clients from determining the maximum session length, which can create client sessions that do not expire.
- Include OneTimeUse Condition
- If enable, a OneTimeUse Condition is included in login responses.
- Optimize REDIRECT signing key lookup
When set to ON, the SAML protocol messages include the Red Hat build of Keycloak native extension. This extension contains a hint with the signing key ID. The SP uses the extension for signature validation instead of attempting to validate the signature using keys.
This option applies to REDIRECT bindings where the signature is transferred in query parameters and this information is not found in the signature information. This is contrary to POST binding messages where key ID is always included in document signature.
This option is used when Red Hat build of Keycloak server and adapter provide the IDP and SP. This option is only relevant when Sign Documents is set to ON.
13.2.1.4. Signature and Encryption
- Sign Documents
- When set to ON, Red Hat build of Keycloak signs the document using the realms private key.
- Sign Assertions
- The assertion is signed and embedded in the SAML XML Auth response.
- Signature Algorithm
-
The algorithm used in signing SAML documents. Note that
SHA1
based algorithms are deprecated and may be removed in a future release. We recommend the use of some more secure algorithm instead of*_SHA1
. Also, with*_SHA1
algorithms, verifying signatures do not work if the SAML client runs on Java 17 or higher. - SAML Signature Key Name
Signed SAML documents sent using POST binding contain the identification of the signing key in the KeyName element. This action can be controlled by the SAML Signature Key Name option. This option controls the contents of the Keyname.
- KEY_ID The KeyName contains the key ID. This option is the default option.
- CERT_SUBJECT The KeyName contains the subject from the certificate corresponding to the realm key. This option is expected by Microsoft Active Directory Federation Services.
- NONE The KeyName hint is completely omitted from the SAML message.
- Canonicalization Method
- The canonicalization method for XML signatures.
13.2.1.5. Login settings
- Login theme
- A theme to use for login, OTP, grant registration, and forgotten password pages.
- Consent required
If enabled, users have to consent to client access.
For client-side clients that perform browser logins. As it is not possible to ensure that secrets can be kept safe with client-side clients, it is important to restrict access by configuring correct redirect URIs.
- Display client on screen
This switch applies if Consent Required is Off.
Off
The consent screen will contain only the consents corresponding to configured client scopes.
On
There will be also one item on the consent screen about this client itself.
- Client consent screen text
- Applies if Consent required and Display client on screen are enabled. Contains the text that will be on the consent screen about permissions for this client.
13.2.1.6. Logout settings
- Front channel logout
- If Front Channel Logout is enabled, the application requires a browser redirect to perform a logout. For example, the application may require a cookie to be reset which could only be done via a redirect. If Front Channel Logout is disabled, Red Hat build of Keycloak invokes a background SAML request to log out of the application.
13.2.2. Keys tab
- Encrypt Assertions
- Encrypts the assertions in SAML documents with the realms private key. The AES algorithm uses a key size of 128 bits.
- Client Signature Required
-
If Client Signature Required is enabled, documents coming from a client are expected to be signed. Red Hat build of Keycloak will validate this signature using the client public key or cert set up in the
Keys
tab. - Allow ECP Flow
- If true, this application is allowed to use SAML ECP profile for authentication.
13.2.3. Advanced tab
This tab has many fields for specific situations. Some fields are covered in other topics. For details on other fields, click the question mark icon.
13.2.3.1. Fine Grain SAML Endpoint Configuration
- Logo URL
- URL that references a logo for the Client application.
- Policy URL
- URL that the Relying Party Client provides to the End-User to read about how the profile data will be used.
- Terms of Service URL
- URL that the Relying Party Client provides to the End-User to read about the Relying Party’s terms of service.
- Assertion Consumer Service POST Binding URL
- POST Binding URL for the Assertion Consumer Service.
- Assertion Consumer Service Redirect Binding URL
- Redirect Binding URL for the Assertion Consumer Service.
- Logout Service POST Binding URL
- POST Binding URL for the Logout Service.
- Logout Service Redirect Binding URL
- Redirect Binding URL for the Logout Service.
- Logout Service Artifact Binding URL
-
Artifact Binding URL for the Logout Service. When set together with the
Force Artifact Binding
option, Artifact binding is forced for both login and logout flows. Artifact binding is not used for logout unless this property is set. - Logout Service SOAP Binding URL
- Redirect Binding URL for the Logout Service. Only applicable if back channel logout is used.
- Artifact Binding URL
- URL to send the HTTP artifact messages to.
- Artifact Resolution Service
-
URL of the client SOAP endpoint where to send the
ArtifactResolve
messages to.
13.2.4. IDP Initiated login
IDP Initiated Login is a feature that allows you to set up an endpoint on the Red Hat build of Keycloak server that will log you into a specific application/client. In the Settings tab for your client, you need to specify the IDP Initiated SSO URL Name. This is a simple string with no whitespace in it. After this you can reference your client at the following URL: root/realms/{realm}/protocol/saml/clients/{url-name}
The IDP initiated login implementation prefers POST over REDIRECT binding (check saml bindings for more information). Therefore the final binding and SP URL are selected in the following way:
- If the specific Assertion Consumer Service POST Binding URL is defined (inside Fine Grain SAML Endpoint Configuration section of the client settings) POST binding is used through that URL.
- If the general Master SAML Processing URL is specified then POST binding is used again throughout this general URL.
- As the last resort, if the Assertion Consumer Service Redirect Binding URL is configured (inside Fine Grain SAML Endpoint Configuration) REDIRECT binding is used with this URL.
If your client requires a special relay state, you can also configure this on the Settings tab in the IDP Initiated SSO Relay State field. Alternatively, browsers can specify the relay state in a RelayState query parameter, i.e. root/realms/{realm}/protocol/saml/clients/{url-name}?RelayState=thestate
.
When using identity brokering, it is possible to set up an IDP Initiated Login for a client from an external IDP. The actual client is set up for IDP Initiated Login at broker IDP as described above. The external IDP has to set up the client for application IDP Initiated Login that will point to a special URL pointing to the broker and representing IDP Initiated Login endpoint for a selected client at the brokering IDP. This means that in client settings at the external IDP:
- IDP Initiated SSO URL Name is set to a name that will be published as IDP Initiated Login initial point,
Assertion Consumer Service POST Binding URL in the Fine Grain SAML Endpoint Configuration section has to be set to the following URL:
broker-root/realms/{broker-realm}/broker/{idp-name}/endpoint/clients/{client-id}
, where:- broker-root is base broker URL
- broker-realm is name of the realm at broker where external IDP is declared
- idp-name is name of the external IDP at broker
- client-id is the value of IDP Initiated SSO URL Name attribute of the SAML client defined at broker. It is this client, which will be made available for IDP Initiated Login from the external IDP.
Please note that you can import basic client settings from the brokering IDP into client settings of the external IDP - just use SP Descriptor available from the settings of the identity provider in the brokering IDP, and add clients/client-id
to the endpoint URL.
13.2.5. Using an entity descriptor to create a client
Instead of registering a SAML 2.0 client manually, you can import the client using a standard SAML Entity Descriptor XML file.
The Client page includes an Import client option.
Add client
Procedure
- Click Browse.
- Load the file that contains the XML entity descriptor information.
- Review the information to ensure everything is set up correctly.
Some SAML client adapters, such as mod-auth-mellon, need the XML Entity Descriptor for the IDP. You can find this descriptor by going to this URL:
root/realms/{realm}/protocol/saml/descriptor
where realm is the realm of your client.
13.3. Client links
To link from one client to another, Red Hat build of Keycloak provides a redirect endpoint: /realms/realm_name/clients/{client-id}/redirect
.
If a client accesses this endpoint using a HTTP GET
request, Red Hat build of Keycloak returns the configured base URL for the provided Client and Realm in the form of an HTTP 307
(Temporary Redirect) in the response’s Location
header. As a result of this, a client needs only to know the Realm name and the Client ID to link to them. This indirection avoids hard-coding client base URLs.
As an example, given the realm master
and the client-id account
:
http://host:port/realms/master/clients/account/redirect
This URL temporarily redirects to: http://host:port/realms/master/account
13.4. OIDC token and SAML assertion mappings
Applications receiving ID tokens, access tokens, or SAML assertions may require different roles and user metadata.
You can use Red Hat build of Keycloak to:
- Hardcode roles, claims and custom attributes.
- Pull user metadata into a token or assertion.
- Rename roles.
You perform these actions in the Mappers tab in the Admin Console.
Mappers tab
New clients do not have built-in mappers, but they can inherit some mappers from client scopes. See the client scopes section for more details.
Protocol mappers map items (such as an email address, for example) to a specific claim in the identity and access token. The function of a mapper should be self-explanatory from its name. You add pre-configured mappers by clicking Add Builtin.
Each mapper has a set of common settings. Additional settings are available, depending on the mapper type. Click Edit next to a mapper to access the configuration screen to adjust these settings.
Mapper config
Details on each option can be viewed by hovering over its tooltip.
You can use most OIDC mappers to control where the claim gets placed. You opt to include or exclude the claim from the id and access tokens by adjusting the Add to ID token and Add to access token switches.
You can add mapper types as follows:
Procedure
- Go to the Mappers tab.
Click Configure a new mapper.
Add mapper
- Select a Mapper Type from the list box.
13.4.1. Priority order
Mapper implementations have priority order. Priority order is not the configuration property of the mapper. It is the property of the concrete implementation of the mapper.
Mappers are sorted by the order in the list of mappers. The changes in the token or assertion are applied in that order with the lowest applying first. Therefore, the implementations that are dependent on other implementations are processed in the necessary order.
For example, to compute the roles which will be included with a token:
- Resolve audiences based on those roles.
- Process a JavaScript script that uses the roles and audiences already available in the token.
13.4.2. OIDC user session note mappers
User session details are defined using mappers and are automatically included when you use or enable a feature on a client. Click Add builtin to include session details.
Impersonated user sessions provide the following details:
- IMPERSONATOR_ID: The ID of an impersonating user.
- IMPERSONATOR_USERNAME: The username of an impersonating user.
Service account sessions provide the following details:
- clientId: The client ID of the service account.
- client_id: The client ID of the service account.
- clientAddress: The remote host IP of the service account’s authenticated device.
- clientHost: The remote host name of the service account’s authenticated device.
13.4.3. Script mapper
Use the Script Mapper to map claims to tokens by running user-defined JavaScript code. For more details about deploying scripts to the server, see JavaScript Providers.
When scripts deploy, you should be able to select the deployed scripts from the list of available mappers.
13.4.4. Pairwise subject identifier mapper
Subject claim sub is mapped by default by Subject (sub) protocol mapper in the default client scope basic.
To use a pairwise subject identifier by using a protocol mapper such as Pairwise subject identifier, you can remove the Subject (sub) protocol mapper from the basic client scope. However it is not strictly needed as the Subject (sub) protocol mapper is executed before the Pairwise subject identifier mapper and hence the pairwise value will override the value added by the Subject mapper. This is due to the priority of the Subject mapper. So the only advantage of removing the built-in Subject (sub) mapper might be to save a little bit of performance by avoiding the use of the protocol mapper, which may not have any effect.
13.4.5. Using lightweight access token
The access token in Red Hat build of Keycloak contains sensitive information, including Personal Identifiable Information (PII). Therefore, if the resource server does not want to disclose this type of information to third party entities such as clients, Red Hat build of Keycloak supports lightweight access tokens that remove PII from access tokens. Further, when the resource server acquires the PII removed from the access token, it can acquire the PII by sending the access token to Red Hat build of Keycloak’s token introspection endpoint.
- Information that cannot be removed from a lightweight access token
-
Protocol mappers can controls which information is put onto an access token and the lightweight access token use the protocol mappers. Therefore, the following information cannot be removed from the lightweight access.
exp
,iat
,jti
,iss
,typ
,azp
,sid
,scope
,cnf
- Using a lightweight access token in Red Hat build of Keycloak
-
By applying
use-lightweight-access-token
executor of client policies to a client, the client can receive a lightweight access token instead of an access token. The lightweight access token contains a claim controlled by a protocol mapper where its settingAdd to lightweight access token
(default OFF) is turned ON. Also, by turning ON its settingAdd to token introspection
of the protocol mapper, the client can obtain the claim by sending the access token to Red Hat build of Keycloak’s token introspection endpoint. - Introspection endpoint
-
In some cases, it might be useful to trigger the token introspection endpoint with the HTTP header
Accept: application/jwt
instead ofAccept: application/json
, which can be useful especially for lightweight access tokens. See the details of Token Introspection endpoint in the securing apps section.
13.5. Generating client adapter config
Red Hat build of Keycloak can generate configuration files that you can use to install a client adapter in your application’s deployment environment. A number of adapter types are supported for OIDC and SAML.
Click on the Action menu and select the Download adapter config option
- Select the Format Option you want configuration generated for.
All Red Hat build of Keycloak client adapters for OIDC and SAML are supported. The mod-auth-mellon Apache HTTPD adapter for SAML is supported as well as standard SAML entity descriptor files.
13.6. Client scopes
Use Red Hat build of Keycloak to define a shared client configuration in an entity called a client scope. A client scope configures protocol mappers and role scope mappings for multiple clients.
Client scopes also support the OAuth 2 scope parameter. Client applications use this parameter to request claims or roles in the access token, depending on the requirement of the application.
To create a client scope, follow these steps:
Click Client Scopes in the menu.
Client scopes list
- Click Create.
- Name your client scope.
- Click Save.
A client scope has similar tabs to regular clients. You can define protocol mappers and role scope mappings. These mappings can be inherited by other clients and are configured to inherit from this client scope.
13.6.1. Protocol
When you create a client scope, choose the Protocol. Clients linked in the same scope must have the same protocol.
Each realm has a set of pre-defined built-in client scopes in the menu.
- SAML protocol: The role_list. This scope contains one protocol mapper for the roles list in the SAML assertion.
OpenID Connect protocol: Several client scopes are available:
roles
This scope is not defined in the OpenID Connect specification and is not added automatically to the scope claim in the access token. This scope has mappers, which are used to add the roles of the user to the access token and add audiences for clients that have at least one client role. These mappers are described in more detail in the Audience section.
web-origins
This scope is also not defined in the OpenID Connect specification and not added to the scope claiming the access token. This scope is used to add allowed web origins to the access token allowed-origins claim.
microprofile-jwt
This scope handles claims defined in the MicroProfile/JWT Auth Specification. This scope defines a user property mapper for the upn claim and a realm role mapper for the groups claim. These mappers can be changed so different properties can be used to create the MicroProfile/JWT specific claims.
offline_access
This scope is used in cases when clients need to obtain offline tokens. More details on offline tokens is available in the Offline Access section and in the OpenID Connect specification.
- profile
- address
- phone
The client scopes profile, email, address and phone are defined in the OpenID Connect specification. These scopes do not have any role scope mappings defined but they do have protocol mappers defined. These mappers correspond to the claims defined in the OpenID Connect specification.
For example, when you open the phone client scope and open the Mappers tab, you will see the protocol mappers which correspond to the claims defined in the specification for the scope phone.
Client scope mappers
When the phone client scope is linked to a client, the client automatically inherits all the protocol mappers defined in the phone client scope. Access tokens issued for this client contain the phone number information about the user, assuming that the user has a defined phone number.
Built-in client scopes contain the protocol mappers as defined in the specification. You are free to edit client scopes and create, update, or remove any protocol mappers or role scope mappings.
13.6.3. Link client scope with the client
Linking between a client scope and a client is configured in the Client Scopes tab of the client. Two ways of linking between client scope and client are available.
- Default Client Scopes
- This setting is applicable to the OpenID Connect and SAML clients. Default client scopes are applied when issuing OpenID Connect tokens or SAML assertions for a client. The client will inherit Protocol Mappers and Role Scope Mappings that are defined on the client scope. For the OpenID Connect Protocol, the Mappers and Role Scope Mappings are always applied, regardless of the value used for the scope parameter in the OpenID Connect authorization request.
- Optional Client Scopes
- This setting is applicable only for OpenID Connect clients. Optional client scopes are applied when issuing tokens for this client but only when requested by the scope parameter in the OpenID Connect authorization request.
13.6.3.1. Example
For this example, assume the client has profile and email linked as default client scopes, and phone and address linked as optional client scopes. The client uses the value of the scope parameter when sending a request to the OpenID Connect authorization endpoint.
scope=openid phone
The scope parameter contains the string, with the scope values divided by spaces. The value openid is the meta-value used for all OpenID Connect requests. The token will contain mappers and role scope mappings from the default client scopes profile and email as well as phone, an optional client scope requested by the scope parameter.
13.6.4. Evaluating Client Scopes
The Mappers tab contains the protocol mappers and the Scope tab contains the role scope mappings declared for this client. They do not contain the mappers and scope mappings inherited from client scopes. It is possible to see the effective protocol mappers (that is the protocol mappers defined on the client itself as well as inherited from the linked client scopes) and the effective role scope mappings used when generating a token for a client.
Procedure
- Click the Client Scopes tab for the client.
- Open the sub-tab Evaluate.
- Select the optional client scopes that you want to apply.
This will also show you the value of the scope parameter. This parameter needs to be sent from the application to the Red Hat build of Keycloak OpenID Connect authorization endpoint.
Evaluating client scopes
To send a custom value for a scope parameter from your application, see the Keycloak JavaScript adapter in the securing apps section, for javascript adapters.
All examples are generated for the particular user and issued for the particular client, with the specified value of the scope parameter. The examples include all of the claims and role mappings used.
13.6.5. Client scopes permissions
When issuing tokens to a user, the client scope applies only if the user is permitted to use it.
When a client scope does not have any role scope mappings defined, each user is permitted to use this client scope. However, when a client scope has role scope mappings defined, the user must be a member of at least one of the roles. There must be an intersection between the user roles and the roles of the client scope. Composite roles are factored into evaluating this intersection.
If a user is not permitted to use the client scope, no protocol mappers or role scope mappings will be used when generating tokens. The client scope will not appear in the scope value in the token.
13.6.6. Realm default client scopes
Use Realm Default Client Scopes to define sets of client scopes that are automatically linked to newly created clients.
Procedure
- Click the Client Scopes tab for the client.
- Click Default Client Scopes.
From here, select the client scopes that you want to add as Default Client Scopes to newly created clients and Optional Client Scopes.
Default client scopes
When a client is created, you can unlink the default client scopes, if needed. This is similar to removing Default Roles.
13.6.7. Scopes explained
- Client scope
- Client scopes are entities in Red Hat build of Keycloak that are configured at the realm level and can be linked to clients. Client scopes are referenced by their name when a request is sent to the Red Hat build of Keycloak authorization endpoint with a corresponding value of the scope parameter. See the client scopes linking section for more details.
- Role scope mapping
- This is available under the Scope tab of a client or client scope. Use Role scope mapping to limit the roles that can be used in the access tokens. See the Role Scope Mappings section for more details.
13.7. Client Policies
To make it easy to secure client applications, it is beneficial to realize the following points in a unified way.
- Setting policies on what configuration a client can have
- Validation of client configurations
- Conformance to a required security standards and profiles such as Financial-grade API (FAPI) and OAuth 2.1
To realize these points in a unified way, Client Policies concept is introduced.
13.7.1. Use-cases
Client Policies realize the following points mentioned as follows.
- Setting policies on what configuration a client can have
- Configuration settings on the client can be enforced by client policies during client creation/update, but also during OpenID Connect requests to Red Hat build of Keycloak server, which are related to particular client. Red Hat build of Keycloak supports similar thing also through the Client Registration Policies described in the Client registration service in the Securing applications and Services guide. However, Client Registration Policies can only cover OIDC Dynamic Client Registration. Client Policies cover not only what Client Registration Policies can do, but other client registration and configuration ways. The current plans are for Client Registration to be replaced by Client Policies.
- Validation of client configurations
- Red Hat build of Keycloak supports validation whether the client follows settings like Proof Key for Code Exchange, Request Object Signing Algorithm, Holder-of-Key Token, and so on some endpoints like Authorization Endpoint, Token Endpoint, and so on. These can be specified by each setting item (on Admin Console, switch, pull-down menu and so on). To make the client application secure, the administrator needs to set many settings in the appropriate way, which makes it difficult for the administrator to secure the client application. Client Policies can do these validation of client configurations mentioned just above and they can also be used to autoconfigure some client configuration switches to meet the advanced security requirements. In the future, individual client configuration settings may be replaced by Client Policies directly performing required validations.
- Conformance to a required security standards and profiles such as FAPI and OAuth 2.1
- The Global client profiles are client profiles pre-configured in Red Hat build of Keycloak by default. They are pre-configured to be compliant with standard security profiles like FAPI and OAuth 2.1 in the securing apps section, which makes it easy for the administrator to secure their client application to be compliant with the particular security profile. At this moment, Red Hat build of Keycloak has global profiles for the support of FAPI and OAuth 2.1 specifications. The administrator will just need to configure the client policies to specify which clients should be compliant with the FAPI and OAuth 2.1. The administrator can configure client profiles and client policies, so that Red Hat build of Keycloak clients can be easily made compliant with various other security profiles like SPA, Native App, Open Banking and so on.
13.7.2. Protocol
The client policy concept is independent of any specific protocol. Red Hat build of Keycloak currently supports especially client profiles for the OpenID Connect (OIDC) protocol, but there is also a client profile available for the SAML protocol.
13.7.3. Architecture
Client Policies consists of the four building blocks: Condition, Executor, Profile and Policy.
13.7.3.1. Condition
A condition determines to which client a policy is adopted and when it is adopted. Some conditions are checked at the time of client create/update when some other conditions are checked during client requests (OIDC Authorization request, Token endpoint request and so on). The condition checks whether one specified criteria is satisfied. For example, some condition checks whether the access type of the client is confidential.
The condition can not be used solely by itself. It can be used in a policy that is described afterwards.
A condition can be configurable the same as other configurable providers. What can be configured depends on each condition’s nature.
The following conditions are provided:
- The way of creating/updating a client
- Dynamic Client Registration (Anonymous or Authenticated with Initial access token or Registration access token)
- Admin REST API (Admin Console and so on)
So for example when creating a client, a condition can be configured to evaluate to true when this client is created by OIDC Dynamic Client Registration without initial access token (Anonymous Dynamic Client Registration). So this condition can be used for example to ensure that all clients registered through OIDC Dynamic Client Registration are FAPI or OAuth 2.1 compliant.
- Author of a client (Checked by presence to the particular role or group)
- On OpenID Connect dynamic client registration, an author of a client is the end user who was authenticated to get an access token for generating a new client, not Service Account of the existing client that actually accesses the registration endpoint with the access token. On registration by Admin REST API, an author of a client is the end user like the administrator of the Red Hat build of Keycloak.
- Client Access Type (confidential, public, bearer-only)
- For example when a client sends an authorization request, a policy is adopted if this client is confidential. Confidential client has enabled client authentication when public client has disabled client authentication. Bearer-only is a deprecated client type.
- Client Scope
-
Evaluates to true if the client has a particular client scope (either as default or as an optional scope used in current request). This can be used for example to ensure that OIDC authorization requests with scope
fapi-example-scope
need to be FAPI compliant. - Client Role
- Applies for clients with the client role of the specified name. Typically you can create a client role of specified name to requested clients and use it as a "marker role" to make sure that specified client policy will be applied for requested clients.
A use-case often exists for requiring the application of a particular client policy for the specified clients such as my-client-1
and my-client-2
. The best way to achieve this result is to use a Client Role condition in your policy and then a create client role of specified name to requested clients. This client role can be used as a "marker role" used solely for marking that particular client policy for particular clients.
- Client Domain Name, Host or IP Address
- Applied for specific domain names of client. Or for the cases when the administrator registers/updates client from particular Host or IP Address.
- Client Attribute
- Applies to clients with the client attribute of the specified name and value. If you specify multiple client attributes, they will be evaluated using AND conditions. If you want to evaluate using OR conditions, set this condition multiple times.
- Any Client
- This condition always evaluates to true. It can be used for example to ensure that all clients in the particular realm are FAPI compliant.
13.7.3.2. Executor
An executor specifies what action is executed on a client to which a policy is adopted. The executor executes one or several specified actions. For example, some executor checks whether the value of the parameter redirect_uri
in the authorization request matches exactly with one of the pre-registered redirect URIs on Authorization Endpoint and rejects this request if not.
The executor can not be used solely by itself. It can be used in a profile that is described afterwards.
An executor can be configurable the same as other configurable providers. What can be configured depends on the nature of each executor.
An executor acts on various events. An executor implementation can ignore certain types of events (For example, executor for checking OIDC request
object acts just on the OIDC authorization request). Events are:
- Creating a client (including creation through dynamic client registration)
- Updating a client
- Sending an authorization request
- Sending a token request
- Sending a token refresh request
- Sending a token revocation request
- Sending a token introspection request
- Sending a userinfo request
- Sending a logout request with a refresh token (note that logout with refresh token is proprietary Red Hat build of Keycloak functionality unsupported by any specification. It is rather recommended to rely on the official OIDC logout).
On each event, an executor can work in multiple phases. For example, on creating/updating a client, the executor can modify the client configuration by autoconfigure specific client settings. After that, the executor validates this configuration in validation phase.
One of several purposes for this executor is to realize the security requirements of client conformance profiles like FAPI and OAuth 2.1. To do so, the following executors are needed:
- Enforce secure Client Authentication method is used for the client
- Enforce Holder-of-key tokens are used
- Enforce Proof Key for Code Exchange (PKCE) is used
- Enforce secure signature algorithm for Signed JWT client authentication (private-key-jwt) is used
- Enforce HTTPS redirect URI and make sure that configured redirect URI does not contain wildcards
-
Enforce OIDC
request
object satisfying high security level - Enforce Response Type of OIDC Hybrid Flow including ID Token used as detached signature as described in the FAPI 1 specification, which means that ID Token returned from Authorization response won’t contain user profile data
-
Enforce more secure
state
andnonce
parameters treatment for preventing CSRF - Enforce more secure signature algorithm when client registration
-
Enforce
binding_message
parameter is used for CIBA requests - Enforce Client Secret Rotation
- Enforce Client Registration Access Token
- Enforce checking if a client is the one to which an intent was issued in a use case where an intent is issued before starting an authorization code flow to get an access token like UK OpenBanking
- Enforce prohibiting implicit and hybrid flow
- Enforce checking if a PAR request includes necessary parameters included by an authorization request
-
Enforce DPoP-binding tokens is used (available when
dpop
feature is enabled) - Enforce using lightweight access token
- Enforce that refresh token rotation is skipped and there is no refresh token returned from the refresh token response
- Enforce a valid redirect URI that the OAuth 2.1 specification requires
- Enforce SAML Redirect binding cannot be used or SAML requests and assertions are signed
13.7.3.3. Profile
A profile consists of several executors, which can realize a security profile like FAPI and OAuth 2.1. Profile can be configured by the Admin REST API (Admin Console) together with its executors. Three global profiles exist and they are configured in Red Hat build of Keycloak by default with pre-configured executors compliant with the FAPI 1 Baseline, FAPI 1 Advanced, FAPI CIBA, FAPI 2 and OAuth 2.1 specifications. More details exist in the FAPI and OAuth 2.1 in the securing apps section.
13.7.3.4. Policy
A policy consists of several conditions and profiles. The policy can be adopted to clients satisfying all conditions of this policy. The policy refers several profiles and all executors of these profiles execute their task against the client that this policy is adopted to.
13.7.4. Configuration
Policies, profiles, conditions, executors can be configured by Admin REST API, which means also the Admin Console. To do so, there is a tab Realm
The Global Client Profiles are automatically available in each realm. However there are no client policies configured by default. This means that the administrator is always required to create any client policy if they want for example the clients of his realm to be FAPI compliant. Global profiles cannot be updated, but the administrator can easily use them as a template and create their own profile if they want to do some slight changes in the global profile configurations. There is JSON Editor available in the Admin Console, which simplifies the creation of new profile based on some global profile.
13.7.5. Backward Compatibility
Client Policies can replace Client Registration Policies described in the Client registration service from Securing applications and Services guide. However, Client Registration Policies also still co-exist. This means that for example during a Dynamic Client Registration request to create/update a client, both client policies and client registration policies are applied.
The current plans are for the Client Registration Policies feature to be removed and the existing client registration policies will be migrated into new client policies automatically.
13.7.6. Client Secret Rotation Example
See an example configuration for client secret rotation.
