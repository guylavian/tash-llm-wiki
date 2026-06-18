---
title: "Chapter 16. Mitigating security threats - Red Hat build of Keycloak 26.0 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-mitigating-security-threats
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_administration_guide/mitigating_security_threats
guide: server_administration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 16. Mitigating security threats - Red Hat build of Keycloak 26.0 Server Administration Guide

Chapter 16. Mitigating security threats
Security vulnerabilities exist in any authentication server. See the Internet Engineering Task Force’s (IETF) OAuth 2.0 Threat Model and the OAuth 2.0 Security Best Current Practice for more information.
16.1. Host
Red Hat build of Keycloak uses the public hostname in several ways, such as within token issuer fields and URLs in password reset emails.
By default, the hostname derives from request headers. No validation exists to ensure a hostname is valid. If you are not using a load balancer, or proxy, with Red Hat build of Keycloak to prevent invalid host headers, configure the acceptable hostnames.
The hostname’s Service Provider Interface (SPI) provides a way to configure the hostname for requests. You can use this built-in provider to set a fixed URL for frontend requests while allowing backend requests based on the request URI. If the built-in provider does not have the required capability, you can develop a customized provider.
16.2. Admin endpoints and Admin Console
Red Hat build of Keycloak exposes the administrative REST API and the web console on the same port as non-administrative usage. Do not expose administrative endpoints externally if external access is not necessary.
16.3. Brute force attacks
A brute force attack attempts to guess a user’s password by trying to log in multiple times. Red Hat build of Keycloak has brute force detection capabilities and can temporarily disable a user account if the number of login failures exceeds a specified threshold.
Red Hat build of Keycloak disables brute force detection by default. Enable this feature to protect against brute force attacks.
Procedure
To enable this protection:
- Click Realm Settings in the menu
- Click the Security Defenses tab.
Click the Brute Force Detection tab.
Brute force detection
Red Hat build of Keycloak can deploy permanent lockout and temporary lockout actions when it detects an attack. Permanent lockout disables a user account until an administrator re-enables it. Temporary lockout disables a user account for a specific period of time. The time period that the account is disabled increases as the attack continues and subsequent failures reach multiples of Max Login Failures
.
When a user is temporarily locked and attempts to log in, Red Hat build of Keycloak displays the default Invalid username or password
error message. This message is the same error message as the message displayed for an invalid username or invalid password to ensure the attacker is unaware the account is disabled.
Common Parameters
| Name | Description | Default |
|---|---|---|
| Max Login Failures | The maximum number of login failures. | 30 failures. |
| Quick Login Check Milliseconds | The minimum time between login attempts. | 1000 milliseconds. |
| Minimum Quick Login Wait | The minimum time the user is disabled when login attempts are quicker than Quick Login Check Milliseconds. | 1 minute. |
Temporary Lockout Parameters
| Name | Description | Default |
|---|---|---|
| Wait Increment | The time added to the time a user is temporarily disabled when the user’s login attempts exceed Max Login Failures. | 1 minute. |
| Max Wait | The maximum time a user is temporarily disabled. | 15 minutes. |
| Failure Reset Time |
The time when the failure count resets. The timer runs from the last failed login. Make sure this number is always greater than | 12 hours. |
Temporary Lockout Algorithm
On successful login
-
Reset
count
-
Reset
On failed login
If the time between this failure and the last failure is greater than Failure Reset Time
-
Reset
count
-
Reset
-
Increment
count
-
Calculate
wait
according the brute force strategy defined (see below Strategies to set Wait Time). If
wait
equals is less than 0 and the time between this failure and the last failure is less than Quick Login Check Milliseconds, setwait
to Minimum Quick Login Wait.-
Temporarily disable the user for the smallest of
wait
and Max Wait seconds - Increment the temporary lockout counter
-
Temporarily disable the user for the smallest of
count
does not increment when a temporarily disabled account commits a login failure.
Strategies to set Wait Time
Red Hat build of Keycloak provides two strategies to calculate wait time: By multiples or Linear. By multiples is the first strategy introduced by Red Hat build of Keycloak, so that is the default one.
By multiples strategy, wait time is incremented when the number (or count) of failures are multiples of Max Login Failure
. For instance, if you set Max Login Failures
to 5
and a Wait Increment
to 30
seconds, the effective time that an account is disabled after several failed authentication attempts will be:
|
|
|
|
|
| 1 | 30 | 5 | 0 |
| 2 | 30 | 5 | 0 |
| 3 | 30 | 5 | 0 |
| 4 | 30 | 5 | 0 |
| 5 | 30 | 5 | 30 |
| 6 | 30 | 5 | 30 |
| 7 | 30 | 5 | 30 |
| 8 | 30 | 5 | 30 |
| 9 | 30 | 5 | 30 |
| 10 | 30 | 5 | 60 |
At the fifth failed attempt of the Effective Wait Time
, the account is disabled for 30
seconds. After reaching the next multiple of Max Login Failures
, in this case 10
, the time increases from 30
to 60
seconds.
The By multiple strategy uses the following formula to calculate wait time: Wait Increment * (count
/ Max Login Failures). The division is an integer division rounded down to a whole number.
For linear strategy, wait time is incremented when the number (or count) of failures equals or is greater than Max Login Failure
. For instance, if you have set Max Login Failures
to 5
and a Wait Increment
to`30` seconds, the effective time that an account is disabled after several failed authentication attempts will be:
|
|
|
|
|
| 1 | 30 | 5 | 0 |
| 2 | 30 | 5 | 0 |
| 3 | 30 | 5 | 0 |
| 4 | 30 | 5 | 0 |
| 5 | 30 | 5 | 30 |
| 6 | 30 | 5 | 60 |
| 7 | 30 | 5 | 90 |
| 8 | 30 | 5 | 120 |
| 9 | 30 | 5 | 150 |
| 10 | 30 | 5 | 180 |
At the fifth failed attempt for the Effective Wait Time
, the account is disabled for 30
seconds. Each new failed attempt increases wait time.
The linear strategy uses the following formula to calculate wait time: Wait Increment * (1 + count
- Max Login Failures).
Permanent Lockout Parameters
| Name | Description | Default |
|---|---|---|
| Max temporary Lockouts | The maximum number of temporary lockouts permitted before permanent lockout occurs. | 0 |
Permanent Lockout Flow
- Follow temporary lockout flow
If temporary lockout counter exceeds Max temporary lockouts
- Permanently disable user
When Red Hat build of Keycloak disables a user, the user cannot log in until an administrator enables the user. Enabling an account resets the count
.
The downside of Red Hat build of Keycloak brute force detection is that the server becomes vulnerable to denial of service attacks. When implementing a denial of service attack, an attacker can attempt to log in by guessing passwords for any accounts it knows and eventually causing Red Hat build of Keycloak to disable the accounts.
Consider using intrusion prevention software (IPS). Red Hat build of Keycloak logs every login failure and client IP address failure. You can point the IPS to the Red Hat build of Keycloak server’s log file, and the IPS can modify firewalls to block connections from these IP addresses.
16.3.1. Password policies
Ensure you have a complex password policy to force users to choose complex passwords. See the Password Policies chapter for more information. Prevent password guessing by setting up the Red Hat build of Keycloak server to use one-time-passwords.
16.4. Read-only user attributes
Typical users who are stored in Red Hat build of Keycloak have various attributes related to their user profiles. Such attributes include email, firstName or lastName. However users may also have attributes, which are not typical profile data, but rather metadata. The metadata attributes usually should be read-only for the users and the typical users never should have a way to update those attributes from the Red Hat build of Keycloak user interface or Account REST API. Some of the attributes should be even read-only for the administrators when creating or updating user with the Admin REST API.
The metadata attributes are usually attributes from those groups:
-
Various links or metadata related to the user storage providers. For example in case of the LDAP integration, the
LDAP_ID
attribute contains the ID of the user in the LDAP server. -
Metadata provisioned by User Storage. For example
createdTimestamp
provisioned from the LDAP should be always read-only by user or administrator. -
Metadata related to various authenticators. For example
KERBEROS_PRINCIPAL
attribute can contain the kerberos principal name of the particular user. Similarly attributeusercertificate
can contain metadata related to binding the user with the data from the X.509 certificate, which is used typically when X.509 certificate authentication is enabled. -
Metadata related to the identificator of users by the applications/clients. For example
saml.persistent.name.id.for.my_app
can contain SAML NameID, which will be used by the client applicationmy_app
as the identifier of the user. - Metadata related to the authorization policies, which are used for the attribute based access control (ABAC). Values of those attributes may be used for the authorization decisions. Hence it is important that those attributes cannot be updated by the users.
From the long term perspective, Red Hat build of Keycloak will have a proper User Profile SPI, which will allow fine-grained configuration of every user attribute. Currently this capability is not fully available yet. So Red Hat build of Keycloak has the internal list of user attributes, which are read-only for the users and read-only for the administrators configured at the server level.
This is the list of the read-only attributes, which are used internally by the Red Hat build of Keycloak default providers and functionalities and hence are always read-only:
-
For users:
KERBEROS_PRINCIPAL
,LDAP_ID
,LDAP_ENTRY_DN
,CREATED_TIMESTAMP
,createTimestamp
,modifyTimestamp
,userCertificate
,saml.persistent.name.id.for.*
,ENABLED
,EMAIL_VERIFIED
-
For administrators:
KERBEROS_PRINCIPAL
,LDAP_ID
,LDAP_ENTRY_DN
,CREATED_TIMESTAMP
,createTimestamp
,modifyTimestamp
System administrators have a way to add additional attributes to this list. The configuration is currently available at the server level.
You can add this configuration by using the spi-user-profile-declarative-user-profile-read-only-attributes
and spi-user-profile-declarative-user-profile-admin-read-only-attributes
options. For example:
kc.[sh|bat] start --spi-user-profile-declarative-user-profile-read-only-attributes=foo,bar*
For this example, users and administrators would not be able to update attribute foo
. Users would not be able to edit any attributes starting with the bar
. So for example bar
or barrier
. Configuration is case-insensitive, so attributes like FOO
or BarRier
will be denied as well for this example. The wildcard character *
is supported only at the end of the attribute name, so the administrator can effectively deny all the attributes starting with the specified character. The *
in the middle of the attribute is considered as a normal character.
16.5. Validate user attributes
With the functionality in Section 5.2, “Managing user attributes”, administrators can restrict the data users enter for attributes, for example, in user registration or the account console.
Administrators should not allow unmanaged attributes for users to prevent attackers adding an unlimited number of attributes. Attributes should have a validation that restricts the amount of data entered by attackers.
When using regular expressions to validate user attributes, avoid regular expressions that use an excessive amount of memory or CPU. See OWASP’s Regular expression Denial of Service for details.
16.6. Clickjacking
Clickjacking is a technique of tricking users into clicking on a user interface element different from what users perceive. A malicious site loads the target site in a transparent iFrame, overlaid on top of a set of dummy buttons placed directly under important buttons on the target site. When a user clicks a visible button, they are clicking a button on the hidden page. An attacker can steal a user’s authentication credentials and access their resources by using this method.
By default, every response by Red Hat build of Keycloak sets some specific HTTP headers that can prevent this from happening. Specifically, it sets X-Frame-Options and Content-Security-Policy. You should take a look at the definition of both of these headers as there is a lot of fine-grain browser access you can control.
Procedure
In the Admin Console, you can specify the values of the X-Frame-Options and Content-Security-Policy headers.
- Click the Realm Settings menu item.
Click the Security Defenses tab.
Security Defenses
By default, Red Hat build of Keycloak only sets up a same-origin policy for iframes.
16.7. SSL/HTTPS requirement
OAuth 2.0/OpenID Connect uses access tokens for security. Attackers can scan your network for access tokens and use them to perform malicious operations for which the token has permission. This attack is known as a man-in-the-middle attack. Use SSL/HTTPS for communication between the Red Hat build of Keycloak auth server and the clients Red Hat build of Keycloak secures to prevent man-in-the-middle attacks.
Red Hat build of Keycloak has three modes for SSL/HTTPS. SSL is complex to set up, so Red Hat build of Keycloak allows non-HTTPS communication over private IP addresses such as localhost, 192.168.x.x, and other private IP addresses. In production, ensure you enable SSL and SSL is compulsory for all operations.
On the adapter/client-side, you can disable the SSL trust manager. The trust manager ensures the client’s identity that Red Hat build of Keycloak communicates with is valid and ensures the DNS domain name against the server’s certificate. In production, ensure that each of your client adapters uses a truststore to prevent DNS man-in-the-middle attacks.
16.8. CSRF attacks
A Cross-site request forgery (CSRF) attack uses HTTP requests from users that websites have already authenticated. Any site using cookie-based authentication is vulnerable to CSRF attacks. You can mitigate these attacks by matching a state cookie against a posted form or query parameter.
The OAuth 2.0 login specification requires that a state cookie matches against a transmitted state parameter. Red Hat build of Keycloak fully implements this part of the specification, so all logins are protected.
The Red Hat build of Keycloak Admin Console is a JavaScript/HTML5 application that makes REST calls to the backend Red Hat build of Keycloak admin REST API. These calls all require bearer token authentication and consist of JavaScript Ajax calls, so CSRF is impossible. You can configure the admin REST API to validate the CORS origins.
The Account Console in Red Hat build of Keycloak can be vulnerable to CSRF. To prevent CSRF attacks, Red Hat build of Keycloak sets a state cookie and embeds the value of this cookie in hidden form fields or query parameters within action links. Red Hat build of Keycloak checks the query/form parameter against the state cookie to verify that the same user made the call.
16.9. Unspecific redirect URIs
Make your registered redirect URIs as specific as feasible. Registering vague redirect URIs for Authorization Code Flows can allow malicious clients to impersonate another client with broader access. Impersonation can happen if two clients live under the same domain, for example.
You can use secure redirect uris enforcer executor for your realm. The result makes sure that client administrators are able to register only clients with specific redirect-uris matching various requirements such as requiring that a URL cannot have wildcards in the context path or can be limited to specified permitted domains. See Client Policies for details about how to configure client policies with a specific executor.
16.10. FAPI compliance
To make sure that Red Hat build of Keycloak server will validate your client to be more secure and FAPI compliant, you can configure client policies for the FAPI support. FAPI details are described in the securing apps section. Among other things, this ensures some security best practices described above like SSL required for clients, secure redirect URI used and more of similar best practices.
16.11. OAuth 2.1 compliance
To make sure that Red Hat build of Keycloak server will validate your client to be more secure and OAuth 2.1 compliant, you can configure client policies for the OAuth 2.1 support. OAuth 2.1 details are described in the securing apps section.
16.12. Compromised access and refresh tokens
Red Hat build of Keycloak includes several actions to prevent malicious actors from stealing access tokens and refresh tokens. The crucial action is to enforce SSL/HTTPS communication between Red Hat build of Keycloak and its clients and applications. Red Hat build of Keycloak does not enable SSL by default.
Another action to mitigate damage from leaked access tokens is to shorten the token’s lifespans. You can specify token lifespans within the timeouts page. Short lifespans for access tokens force clients and applications to refresh their access tokens after a short time. If an admin detects a leak, the admin can log out all user sessions to invalidate these refresh tokens or set up a revocation policy.
Ensure refresh tokens always stay private to the client and are never transmitted.
You can mitigate damage from leaked access tokens and refresh tokens by issuing these tokens as holder-of-key tokens. See OAuth 2.0 Mutual TLS Client Certificate Bound Access Token for more information.
If an access token or refresh token is compromised, access the Admin Console and push a not-before revocation policy to all applications. Pushing a not-before policy ensures that any tokens issued before that time become invalid. Pushing a new not-before policy ensures that applications must download new public keys from Red Hat build of Keycloak and mitigate damage from a compromised realm signing key. See the keys chapter for more information.
You can disable specific applications, clients, or users if they are compromised.
16.13. Compromised authorization code
For the OIDC Auth Code Flow, Red Hat build of Keycloak generates a cryptographically strong random value for its authorization codes. An authorization code is used only once to obtain an access token.
On the timeouts page in the Admin Console, you can specify the length of time an authorization code is valid. Ensure that the length of time is less than 10 seconds, which is long enough for a client to request a token from the code.
You can also defend against leaked authorization codes by applying Proof Key for Code Exchange (PKCE) to clients.
16.14. Open redirectors
An open redirector is an endpoint using a parameter to automatically redirect a user agent to the location specified by the parameter value without validation. An attacker can use the end-user authorization endpoint and the redirect URI parameter to use the authorization server as an open redirector, using a user’s trust in an authorization server to launch a phishing attack.
Red Hat build of Keycloak requires that all registered applications and clients register at least one redirection URI pattern. When a client requests that Red Hat build of Keycloak performs a redirect, Red Hat build of Keycloak checks the redirect URI against the list of valid registered URI patterns. Clients and applications must register as specific a URI pattern as possible to mitigate open redirector attacks.
If an application requires a non http(s) custom scheme, it should be an explicit part of the validation pattern (for example custom:/app/*
). For security reasons a general pattern like *
does not cover non http(s) schemes.
By using Client Policies, an administrator can make sure that clients cannot register open redirect URLs such as *
.
16.15. Password database compromised
Red Hat build of Keycloak does not store passwords in raw text but as hashed text, using the PBKDF2-HMAC-SHA512
message digest algorithm. Red Hat build of Keycloak performs 210,000
hashing iterations, the number of iterations recommended by the security community. This number of hashing iterations can adversely affect performance as PBKDF2 hashing uses a significant amount of CPU resources.
16.16. Limiting scope
By default, new client applications have unlimited role scope mappings
. Every access token for that client contains all permissions that the user has. If an attacker compromises the client and obtains the client’s access tokens, each system that the user can access is compromised.
Limit the roles of an access token by using the Scope menu for each client. Alternatively, you can set role scope mappings at the Client Scope level and assign Client Scopes to your client by using the Client Scope menu.
16.17. Limit token audience
In environments with low levels of trust among services, limit the audiences on the token. See the OAuth2 Threat Model and the Audience Support section for more information.
16.18. Limit Authentication Sessions
Authentication sessions track the state of the authentication. The text below is applicable regardless of the source flow.
This section describes deployments that use the Data Grid provider for authentication sessions.
Authentication session is internally stored as RootAuthenticationSessionEntity
. Each RootAuthenticationSessionEntity
can have multiple authentication sub-sessions stored within the RootAuthenticationSessionEntity
as a collection of AuthenticationSessionEntity
objects. Red Hat build of Keycloak stores authentication sessions in a dedicated Data Grid cache. The number of AuthenticationSessionEntity
per RootAuthenticationSessionEntity
contributes to the size of each cache entry. Total memory footprint of authentication session cache is determined by the number of stored RootAuthenticationSessionEntity
and by the number of AuthenticationSessionEntity
within each RootAuthenticationSessionEntity
.
The number of maintained RootAuthenticationSessionEntity
objects corresponds to the number of unfinished login flows from the browser. To keep the number of RootAuthenticationSessionEntity
under control, using an advanced firewall control to limit ingress network traffic is recommended.
Higher memory usage may occur for deployments where there are many active RootAuthenticationSessionEntity
with a lot of AuthenticationSessionEntity
. If the load balancer does not support or is not configured for session stickiness, the load over network in a cluster can increase significantly. The reason for this load is that each request that lands on a node that does not own the appropriate authentication session needs to retrieve and update the authentication session record in the owner node which involves a separate network transmission for both the retrieval and the storage.
The maximum number of AuthenticationSessionEntity
per RootAuthenticationSessionEntity
can be configured in authenticationSessions
SPI by setting property authSessionsLimit
. The default value is set to 300 AuthenticationSessionEntity
per a RootAuthenticationSessionEntity
. When this limit is reached, the oldest authentication sub-session will be removed after a new authentication session request.
The following example shows how to limit the number of active AuthenticationSessionEntity
per a RootAuthenticationSessionEntity
to 100.
bin/kc.[sh|bat] start --spi-authentication-sessions-infinispan-auth-sessions-limit=100
16.19. SQL injection attacks
Currently, Red Hat build of Keycloak has no known SQL injection vulnerabilities.
