---
title: "Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK) - Red Hat Developer Hub 1.7 Authentication in Red Hat Developer Hub"
type: reference
domain: keycloak
slug: doc-assembly-authenticating-with-rhbk
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.7/html/authentication_in_red_hat_developer_hub/assembly-authenticating-with-rhbk
guide: authentication_in_red_hat_developer_hub
documentKind: "Documentation"
abstract: "3.1. Enabling user authentication with Red Hat Build of Keycloak (RHBK) To authenticate users with Red Hat Build of Keycloak (RHBK), enable and configure the OpenID Connect (OIDC) authentication provider in Red Hat Developer Hub and provision the users and groups from RHBK to the Developer Hub software catalog. Prerequisites You added a custom Developer Hub application configuration, and have suff…"
---

# Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK) - Red Hat Developer Hub 1.7 Authentication in Red Hat Developer Hub

Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK)
3.1. Enabling user authentication with Red Hat Build of Keycloak (RHBK)
To authenticate users with Red Hat Build of Keycloak (RHBK), enable and configure the OpenID Connect (OIDC) authentication provider in Red Hat Developer Hub and provision the users and groups from RHBK to the Developer Hub software catalog.
Prerequisites
- You added a custom Developer Hub application configuration, and have sufficient permissions to modify it.
- You have sufficient permissions in RHSSO to create and manage a realm and a client. Alternatively, your RHBK administrator can prepare in RHBK the required realm and client for you.
Procedure
To allow Developer Hub to authenticate with RHBK, complete the steps in RHBK, to create a realm and a user and secure the first application:
Use an existing realm, or create a realm, with a distinctive Name such as <my_realm>. Save the value for the next step:
- RHBK realm base URL, such as: <your_rhbk_URL>/realms/<your_realm>.
To register your Developer Hub in RHBK, in the created realm, secure the first application, with:
- Client ID: A distinctive client ID, such as <RHDH>.
-
Valid redirect URIs: Set to the OIDC handler URL:
https://<my_developer_hub_domain>/api/auth/oidc/handler/frame
. - Navigate to the Credentials tab and copy the Client secret.
Save the values for the next step:
- Client ID
- Client Secret
- To prepare for the verification steps, in the same realm, get the credential information for an existing user or create a user. Save the user credential information for the verification steps.
To add your RHSSO credentials to Developer Hub, add the following key/value pairs to your Developer Hub secrets. You can use these secrets in the Developer Hub configuration files by using their respective environment variable name.
AUTHENTICATION_OIDC_CLIENT_ID
- Enter the saved Client ID.
AUTHENTICATION_OIDC_CLIENT_SECRET
- Enter the saved Client Secret.
AUTHENTICATION_OIDC_METADATA_URL
- Enter the saved RHBK realm base URL.
Enable the Keycloak organization plugin (
backstage-community-plugin-catalog-backend-module-keycloak-dynamic
). The plugin is named after RHBK upstream project. This plugin ingests RHBK users and groups to the Developer Hub software catalog.dynamic-plugins.yaml
file fragmentplugins: - package: './dynamic-plugins/dist/backstage-community-plugin-catalog-backend-module-keycloak-dynamic' disabled: false
To provision RHBK users and groups to the Developer Hub software catalog, add the
catalog.providers.keycloakOrg
section to your custom Developer Hubapp-config.yaml
configuration file:Add mandatory fields:
app-config.yaml
fragment with mandatorykeycloakOrg
fieldscatalog: providers: keycloakOrg: default: baseUrl: ${AUTHENTICATION_OIDC_METADATA_URL} clientId: ${AUTHENTICATION_OIDC_CLIENT_ID} clientSecret: ${AUTHENTICATION_OIDC_CLIENT_SECRET} realm: master loginRealm: master
baseUrl
- Enter your RHBK server URL, defined when enabling authentication with RHBK.
clientId
- Enter your Developer Hub application client ID in RHBK, defined when enabling authentication with RHBK.
clientSecret
- Enter your Developer Hub application client secret in RHBK, defined when enabling authentication with RHBK.
realm
-
Enter the realm name to provision users, such as
master
. loginRealm
-
Enter the realm name to authenticate users, such as
master
.
Optional: Consider adding optional fields:
userQuerySize
Enter the user count to query simultaneously. Default value:
100
.app-config.yaml
fragment with optionaluserQuerySize
fieldcatalog: providers: keycloakOrg: default: userQuerySize: 100
groupQuerySize
Enter the group count to query simultaneously. Default value:
100
.app-config.yaml
fragment with optionalgroupQuerySize
fieldcatalog: providers: keycloakOrg: default: groupQuerySize: 100
schedule.frequency
Enter the schedule frequency. Supports cron, ISO duration, and "human duration" as used in code.
app-config.yaml
fragment with optionalschedule.frequency
fieldcatalog: providers: keycloakOrg: default: schedule: frequency: { hours: 1 }
schedule.timeout
Enter the timeout for the user provisioning job. Supports ISO duration and "human duration" as used in code.
app-config.yaml
fragment with optionalschedule.timeout
fieldcatalog: providers: keycloakOrg: default: schedule: timeout: { minutes: 50 }
schedule.initialDelay
Enter the initial delay to wait for before starting the user provisioning job. Supports ISO duration and "human duration" as used in code.
app-config.yaml
fragment with optionalschedule.initialDelay
fieldcatalog: providers: keycloakOrg: default: schedule: initialDelay: { seconds: 15}
To set up the RHBK authentication provider in your Developer Hub custom configuration, edit your custom Developer Hub ConfigMap such as
app-config-rhdh
, and add the following lines to theapp-config.yaml
content:Add mandatory fields:
app-config.yaml
fragment with mandatory fields to enable authentication with RHBKauth: environment: production providers: oidc: production: metadataUrl: ${AUTHENTICATION_OIDC_METADATA_URL} clientId: ${AUTHENTICATION_OIDC_CLIENT_ID} clientSecret: ${AUTHENTICATION_OIDC_CLIENT_SECRET} prompt: auto signInPage: oidc
environment: production
-
Mark the environment as
production
to hide the Guest login in the Developer Hub home page. metadataUrl
,clientId
,clientSecret
- To configure the OIDC provider with your secrets.
sigInPage: oidc
- To enable the OIDC provider as default sign-in provider.
prompt: auto
To allow the identity provider to automatically determine whether to prompt for credentials or bypass the login redirect if an active RHSSO session exists.
NoteIf
prompt: auto
is not set, the identity provider defaults toprompt: none
, which assumes that you are already logged in and rejects sign-in requests without an active session.
Optional: Consider adding optional fields:
callbackUrl
RHBK callback URL.
app-config.yaml
fragment with optionalcallbackURL
fieldauth: providers: oidc: production: callbackUrl: ${AUTHENTICATION_OIDC_CALLBACK_URL}
tokenEndpointAuthMethod
Token endpoint authentication method.
app-config.yaml
fragment with optionaltokenEndpointAuthMethod
fieldauth: providers: oidc: production: tokenEndpointAuthMethod: ${AUTHENTICATION_OIDC_TOKEN_ENDPOINT_METHOD}
tokenSignedResponseAlg
Token signed response algorithm.
app-config.yaml
fragment with optionaltokenSignedResponseAlg
fieldauth: providers: oidc: production: tokenSignedResponseAlg: ${AUTHENTICATION_OIDC_SIGNED_RESPONSE_ALG}
additionalScopes
Enter additional RHBK scopes to request for during the authentication flow.
app-config.yaml
fragment with optionaladditionalScopes
fieldauth: providers: oidc: production: additionalScopes: ${AUTHENTICATION_OIDC_SCOPE}
signIn
resolvers
After successful authentication, the user signing in must be resolved to an existing user in the Developer Hub catalog. To best match users securely for your use case, consider configuring a specific resolver.
Enter the resolver list to override the default resolver:
oidcSubClaimMatchingKeycloakUserId
.Available values:
oidcSubClaimMatchingKeycloakUserId
-
Matches the user with the immutable
sub
parameter from OIDC to the RHBK user ID. Consider using this resolver for enhanced security. emailLocalPartMatchingUserEntityName
- Matches the email local part with the user entity name.
emailMatchingUserEntityProfileEmail
- Matches the email with the user entity profile email.
preferredUsernameMatchingUserEntityName
Matches the preferred username with the user entity name.
The authentication provider tries each sign-in resolver in order until it succeeds, and fails if none succeed.
WarningIn production mode, only configure one resolver to ensure users are securely matched.
app-config.yaml
fragment with optionalresolvers
listauth: providers: oidc: production: signIn: resolvers: - resolver: oidcSubClaimMatchingKeycloakUserId - resolver: preferredUsernameMatchingUserEntityName - resolver: emailMatchingUserEntityProfileEmail - resolver: emailLocalPartMatchingUserEntityName
dangerouslyAllowSignInWithoutUserInCatalog: true
Configure the sign-in resolver to bypass the user provisioning requirement in the Developer Hub software catalog.
WarningUse this option to explore Developer Hub features, but do not use it in production.
app-config-rhdh.yaml
fragment with optional field to allow signing in users absent from the software catalogauth: environment: production providers: oidc: production: metadataUrl: ${AUTHENTICATION_OIDC_METADATA_URL} clientId: ${AUTHENTICATION_OIDC_CLIENT_ID} clientSecret: ${AUTHENTICATION_OIDC_CLIENT_SECRET} signIn: resolvers: - resolver: oidcSubClaimMatchingKeycloakUserID dangerouslyAllowSignInWithoutUserInCatalog: true signInPage: oidc
sessionDuration
Lifespan of the user session. Enter a duration in
ms
library format (such as '24h', '2 days'), ISO duration, or "human duration" as used in code.app-config-rhdh.yaml
fragment with optionalsessionDuration
fieldauth: providers: github: production: sessionDuration: { hours: 24 }
auth
backstageTokenExpiration
- To modify the Developer Hub token expiration from its default value of one hour, note that this refers to the validity of short-term cryptographic tokens, not the session duration. The expiration value must be set between 10 minutes and 24 hours.
app-config.yaml
fragment with optionalauth.backstageTokenExpiration
fieldauth: backstageTokenExpiration: { minutes: <user_defined_value> }
Security considerationIf multiple valid refresh tokens are issued due to frequent refresh token requests, older tokens will remain valid until they expire. To enhance security and prevent potential misuse of older tokens, enable a refresh token rotation strategy in your RHBK realm.
- From the Configure section of the navigation menu, click Realm Settings.
- From the Realm Settings page, click the Tokens tab.
- From the Refresh tokens section of the Tokens tab, toggle the Revoke Refresh Token to the Enabled position.
Verification
To verify user and group provisioning, check the console logs.
Successful synchronization example:
2025-06-27T16:02:34.647Z catalog info Read 5 Keycloak users and 3 Keycloak groups in 0.4 seconds. Committing... class="KeycloakOrgEntityProvider" taskId="KeycloakOrgEntityProvider:default:refresh" taskInstanceId="db55c34b-46b3-402b-b12f-2fbc48498e82" trace_id="606f80a9ce00d1c86800718c4522f7c6" span_id="7ebc2a254a546e90" trace_flags="01" 2025-06-27T16:02:34.650Z catalog info Committed 5 Keycloak users and 3 Keycloak groups in 0.0 seconds. class="KeycloakOrgEntityProvider" taskId="KeycloakOrgEntityProvider:default:refresh" taskInstanceId="db55c34b-46b3-402b-b12f-2fbc48498e82" trace_id="606f80a9ce00d1c86800718c4522f7c6" span_id="7ebc2a254a546e90" trace_flags="01"
To verify RHBK user authentication:
- Go to the Developer Hub login page.
- Your Developer Hub sign-in page displays Sign in using OIDC and the Guest user sign-in is disabled.
- Log in with OIDC by using the saved Username and Password values.
3.2. Creating a custom transformer to provision users from Red Hat Build of Keycloak (RHBK) to the software catalog
To customize how RHBK users and groups are mapped to Red Hat Developer Hub entities, you can create a backend module that uses the keycloakTransformerExtensionPoint
to provide custom user and group transformers for the Keycloak backend.
Prerequisites
Procedure
-
Create a new backend module with the
yarn new
command. Add your custom user and group transformers to the
keycloakTransformerExtensionPoint
.The following is an example of how the backend module can be defined:
plugins/<module-name>/src/module.ts
import { GroupTransformer, keycloakTransformerExtensionPoint, UserTransformer, } from '@backstage-community/plugin-catalog-backend-module-keycloak'; const customGroupTransformer: GroupTransformer = async ( entity, // entity output from default parser realm, // Keycloak realm name groups, // Keycloak group representation ) => { /* apply transformations */ return entity; }; const customUserTransformer: UserTransformer = async ( entity, // entity output from default parser user, // Keycloak user representation realm, // Keycloak realm name groups, // Keycloak group representation ) => { /* apply transformations */ return entity; }; export const keycloakBackendModuleTransformer = createBackendModule({ pluginId: 'catalog', moduleId: 'keycloak-transformer', register(reg) { reg.registerInit({ deps: { keycloak: keycloakTransformerExtensionPoint, }, async init({ keycloak }) { keycloak.setUserTransformer(customUserTransformer); keycloak.setGroupTransformer(customGroupTransformer); /* highlight-add-end */ }, }); }, });
ImportantThe module’s
pluginId
must be set tocatalog
to match thepluginId
of thekeycloak-backend
; otherwise, the module fails to initialize.Install this new backend module into your Developer Hub backend.
backend.add(import(backstage-plugin-catalog-backend-module-keycloak-transformer))
Verification
Developer Hub imports the users and groups each time when started. Check the console logs to verify that the synchronization is completed.
Successful synchronization example:
{"class":"KeycloakOrgEntityProvider","level":"info","message":"Read 3 Keycloak users and 2 Keycloak groups in 1.5 seconds. Committing...","plugin":"catalog","service":"backstage","taskId":"KeycloakOrgEntityProvider:default:refresh","taskInstanceId":"bf0467ff-8ac4-4702-911c-380270e44dea","timestamp":"2024-09-25 13:58:04"} {"class":"KeycloakOrgEntityProvider","level":"info","message":"Committed 3 Keycloak users and 2 Keycloak groups in 0.0 seconds.","plugin":"catalog","service":"backstage","taskId":"KeycloakOrgEntityProvider:default:refresh","taskInstanceId":"bf0467ff-8ac4-4702-911c-380270e44dea","timestamp":"2024-09-25 13:58:04"}
- After the first import is complete, navigate to the Catalog page and select User to view the list of users.
- When you select a user, you see the information imported from RHBK.
- You can select a group, view the list, and access or review the information imported from RHBK.
- You can log in with an RHBK account.
