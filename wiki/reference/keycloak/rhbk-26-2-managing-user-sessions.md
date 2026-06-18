---
title: "Chapter 6. Managing user sessions - Red Hat build of Keycloak 26.2 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-managing-user-sessions
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_administration_guide/managing-user-sessions
guide: server_administration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 6. Managing user sessions - Red Hat build of Keycloak 26.2 Server Administration Guide

Chapter 6. Managing user sessions
When users log into realms, Red Hat build of Keycloak maintains a user session for each user and remembers each client visited by the user within the session. Realm administrators can perform multiple actions on each user session:
- View login statistics for the realm.
- View active users and where they logged in.
- Log a user out of their session.
- Revoke tokens.
- Set up token timeouts.
- Set up session timeouts.
6.1. Administering sessions
To see a top-level view of the active clients and sessions in Red Hat build of Keycloak, click Sessions from the menu.
Sessions
6.1.1. Signing out all active sessions
You can sign out all users in the realm. From the Action list, select Sign out all active sessions. All SSO cookies become invalid. Red Hat build of Keycloak notifies clients by using the Red Hat build of Keycloak OIDC client adapter of the logout event. Clients requesting authentication within active browser sessions must log in again. Client types such as SAML do not receive a back-channel logout request.
Clicking Sign out all active sessions does not revoke outstanding access tokens. Outstanding tokens must expire naturally. For clients using the Red Hat build of Keycloak OIDC client adapter, you can push a revocation policy to revoke the token, but this does not work for other adapters.
6.1.2. Viewing client sessions
Procedure
- Click Clients in the menu.
- Click a client to see that client’s sessions.
Click the Sessions tab.
Client sessions
6.1.3. Viewing user sessions
Procedure
- Click Users in the menu.
- Click a user to see that user’s sessions.
Click the Sessions tab.
User sessions
6.2. Revoking active sessions
If your system is compromised, you can revoke all active sessions and access tokens.
Procedure
- Click Sessions in the menu.
From the Actions list, select Revocation.
Revocation
Specify a time and date where sessions or tokens issued before that time and date are invalid using this console.
- Click Set to now to set the policy to the current time and date.
- Click Push to push this revocation policy to any registered OIDC client with the Red Hat build of Keycloak OIDC client adapter.
6.3. Session and token timeouts
Red Hat build of Keycloak includes control of the session, cookie, and token timeouts through the Sessions and Tokens tabs in the Realm settings menu.
Sessions tab
| Configuration | Description |
|---|---|
| SSO Session Idle | This setting is for OIDC clients only. If a user is inactive for longer than this timeout, the user session is invalidated. This timeout value resets when clients request authentication or send a refresh token request. Red Hat build of Keycloak adds a window of time to the idle timeout before the session invalidation takes effect. See the note later in this section. |
| SSO Session Max | The maximum time before a user session expires. |
| SSO Session Idle Remember Me | This setting is similar to the standard SSO Session Idle configuration but specific to logins with Remember Me enabled. Users can specify longer session idle timeouts when they click Remember Me when logging in. This setting is an optional configuration and, if its value is not greater than zero, it uses the same idle timeout as the SSO Session Idle configuration. |
| SSO Session Max Remember Me | This setting is similar to the standard SSO Session Max but specific to Remember Me logins. Users can specify longer sessions when they click Remember Me when logging in. This setting is an optional configuration and, if its value is not greater than zero, it uses the same session lifespan as the SSO Session Max configuration. |
| Client Session Idle | Idle timeout for the client session. If the user is inactive for longer than this timeout, the client session is invalidated and the refresh token requests bump the idle timeout. This setting never affects the general SSO user session, which is unique. Note the SSO user session is the parent of zero or more client sessions, one client session is created for every different client app the user logs in. This value should specify a shorter idle timeout than the SSO Session Idle. Users can override it for individual clients in the Advanced Settings client tab. This setting is an optional configuration and, when set to zero, uses the same idle timeout in the SSO Session Idle configuration. |
| Client Session Max | The maximum time for a client session and before a refresh token expires and invalidates. As in the previous option, this setting never affects the SSO user session and should specify a shorter value than the SSO Session Max. Users can override it for individual clients in the Advanced Settings client tab. This setting is an optional configuration and, when set to zero, uses the same max timeout in the SSO Session Max configuration.
|
| Offline Session Idle | This setting is for offline access. The amount of time the session remains idle before Red Hat build of Keycloak revokes its offline token. Red Hat build of Keycloak adds a window of time to the idle timeout before the session invalidation takes effect. See the note later in this section.
|
| Offline Session Max Limited | This setting is for offline access. If this flag is Enabled, Offline Session Max can control the maximum time the offline token remains active, regardless of user activity. If the flag is Disabled, offline sessions never expire by lifespan, only by idle. Once this option is activated, the Offline Session Max and Client Offline Session Max (global option at realm level) can be configured.
|
| Offline Session Max | This setting is for offline access, and it is the maximum time before Red Hat build of Keycloak revokes the corresponding offline token. This option controls the maximum amount of time the offline token remains active, regardless of user activity.
|
| Client Offline Session Max | This setting is for offline access, and it is the maximum time before Red Hat build of Keycloak revokes the corresponding offline token for the client. This option controls the maximum amount of time the offline token remains active, regardless of user activity. Users can override it for individual clients in the Advanced Settings client tab. |
| Login timeout | The total time a logging in must take. If authentication takes longer than this time, the user must start the authentication process again. |
| Login action timeout | The Maximum time users can spend on any one page during the authentication process. |
Tokens tab
| Configuration | Description |
|---|---|
| Default Signature Algorithm | The default algorithm used to assign tokens for the realm.
|
| Revoke Refresh Token | When Enabled, Red Hat build of Keycloak revokes refresh tokens and issues another token that the client must use. This action applies to OIDC clients performing the refresh token flow. |
| Access Token Lifespan | When Red Hat build of Keycloak creates an OIDC access token, this value controls the lifetime of the token. |
| Access Token Lifespan For Implicit Flow | With the Implicit Flow, Red Hat build of Keycloak does not provide a refresh token. A separate timeout exists for access tokens created by the Implicit Flow. |
| Client login timeout | The maximum time before clients must finish the Authorization Code Flow in OIDC. |
| User-Initiated Action Lifespan | The maximum time before a user’s action permission expires. Keep this value short because users generally react to self-created actions quickly. |
| Default Admin-Initiated Action Lifespan | The maximum time before an action permission sent to a user by an administrator expires. Keep this value long to allow administrators to send e-mails to offline users. An administrator can override the default timeout before issuing the token. |
| Email Verification | Specifies independent timeout for email verification. |
| IdP account email verification | Specifies independent timeout for IdP account email verification. |
| Forgot password | Specifies independent timeout for forgot password. |
| Execute actions | Specifies independent timeout for execute actions. |
The following logic is only applied if persistent user sessions are not active:
For idle timeouts, a two-minute window of time exists that the session is active. For example, when you have the timeout set to 30 minutes, it will be 32 minutes before the session expires.
This action is necessary for some scenarios in cluster and cross-data center environments where the token refreshes on one cluster node a short time before the expiration and the other cluster nodes incorrectly consider the session as expired because they have not yet received the message about a successful refresh from the refreshing node.
6.4. Offline access
During offline access logins, the client application requests an offline token instead of a refresh token. The client application saves this offline token and can use it for future logins if the user logs out. This action is useful if your application needs to perform offline actions on behalf of the user even when the user is not online. For example, a regular data backup.
The client application is responsible for persisting the offline token in storage and then using it to retrieve new access tokens from the Red Hat build of Keycloak server.
The difference between a refresh token and an offline token is that an offline token never expires and is not subject to the SSO Session Idle
timeout and SSO Session Max
lifespan. The offline token is valid after a user logout. You must use the offline token for a refresh token action at least once per thirty days or for the value of the Offline Session Idle.
If you enable Offline Session Max Limited, offline tokens expire after 60 days even if you use the offline token for a refresh token action. You can change this value, Offline Session Max, in the Admin Console.
When using offline access, client idle and max timeouts can be overridden at the client level. The options Client Offline Session Idle and Client Offline Session Max, in the client Advanced Settings tab, allow you to have a shorter offline timeouts for a specific application. Note that client session values also control the refresh token expiration but they never affect the global offline user SSO session. The option Client Offline Session Max is only evaluated in the client if Offline Session Max Limited is Enabled at the realm level.
If you enable the Revoke Refresh Token option, you can use each offline token once only. After refresh, you must store the new offline token from the refresh response instead of the previous one.
Users can view and revoke offline tokens that Red Hat build of Keycloak grants them in the User Account Console. Administrators can revoke offline tokens for individual users in the Admin Console in the Consents
tab. Administrators can view all offline tokens issued in the Offline Access
tab of each client. Administrators can revoke offline tokens by setting a revocation policy.
To issue an offline token, users must have the role mapping for the realm-level offline_access
role. Clients must also have that role in their scope. Clients must add an offline_access
client scope as an Optional client scope
to the role, which is done by default.
Clients can request an offline token by adding the parameter scope=offline_access
when sending their authorization request to Red Hat build of Keycloak. The Red Hat build of Keycloak OIDC client adapter automatically adds this parameter when you use it to access your application’s secured URL (such as, http://localhost:8080/customer-portal/secured?scope=offline_access). The Direct Access Grant and Service Accounts support offline tokens if you include scope=offline_access
in the authentication request body.
Red Hat build of Keycloak will limit its internal cache for offline user and offline client sessions to 10000 entries by default, which will reduce the overall memory usage for offline sessions. Items which are evicted from memory will be loaded on-demand from the database when needed. To set different sizes for the caches, edit Red Hat build of Keycloak’s cache config file to set a <memory max-count="..."/>
for those caches.
If you disabled feature persistent-user-sessions
, it is possible to reduce memory requirements using a configuration option that shortens lifespan for imported offline sessions. Such sessions will be evicted from the Infinispan caches after the specified lifespan, but still available in the database. This will lower memory consumption, especially for deployments with a large number of offline sessions.
To specify the lifespan override for offline user sessions, start Red Hat build of Keycloak server with the following parameter:
--spi-user-sessions-infinispan-offline-session-cache-entry-lifespan-override=<lifespan-in-seconds>
Similarly for offline client sessions:
--spi-user-sessions-infinispan-offline-client-session-cache-entry-lifespan-override=<lifespan-in-seconds>
6.5. Transient sessions
You can conduct transient sessions in Red Hat build of Keycloak. When using transient sessions, Red Hat build of Keycloak does not create a user session after successful authentication. Red Hat build of Keycloak creates a temporary, transient session for the scope of the current request that successfully authenticates the user. Red Hat build of Keycloak can run protocol mappers using transient sessions after authentication.
The sid
and session_state
of the tokens are usually empty when the token is issued with transient sessions. So during transient sessions, the client application cannot refresh tokens or validate a specific session. Sometimes these actions are unnecessary, so you can avoid the additional resource use of persisting user sessions. This session saves performance, memory, and network communication (in cluster and cross-data center environments) resources.
At this moment, transient sessions are automatically used just during service account authentication with disabled token refresh. Note that token refresh is automatically disabled during service account authentication unless explicitly enabled by client switch Use refresh tokens for client credentials grant
.
