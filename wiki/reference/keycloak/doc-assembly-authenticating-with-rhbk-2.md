---
title: "Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK) - Red Hat Developer Hub 1.6 Authentication in Red Hat Developer Hub"
type: reference
domain: keycloak
slug: doc-assembly-authenticating-with-rhbk-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.6/html/authentication_in_red_hat_developer_hub/assembly-authenticating-with-rhbk
guide: authentication_in_red_hat_developer_hub
documentKind: "Documentation"
---

# Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK) - Red Hat Developer Hub 1.6 Authentication in Red Hat Developer Hub

Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK)
To authenticate users with Red Hat Build of Keycloak (RHBK):
3.1. Enabling authentication with Red Hat Build of Keycloak (RHBK)
To authenticate users with Red Hat Build of Keycloak (RHBK), enable the OpenID Connect (OIDC) authentication provider in Red Hat Developer Hub.
Prerequisites
- You added a custom Developer Hub application configuration, and have sufficient permissions to modify it.
- You have sufficient permissions in RHSSO to create and manage a realm.
Procedure
To allow Developer Hub to authenticate with RHBK, complete the steps in RHBK, to create a realm and a user and secure the first application:
Use an existing realm, or create a realm, with a distinctive Name such as <my_realm>. Save the value for the next step:
- RHBK realm base URL, such as: <your_rhbk_URL>/realms/<your_realm>.
To register your Developer Hub in RHBK, in the created realm, secure the first application, with:
- Client ID: A distinctive client ID, such as <RHDH>.
-
Valid redirect URIs: Set to the OIDC handler URL:
https://<RHDH_URL>/api/auth/oidc/handler/frame
. - Navigate to the Credentials tab and copy the Client secret.
Save the values for the next step:
- Client ID
- Client Secret
- To prepare for the verification steps, in the same realm, get the credential information for an existing user or create a user. Save the user credential information for the verification steps.
To add your RHSSO credentials to your Developer Hub, add the following key/value pairs to your Developer Hub secrets:
AUTH_OIDC_CLIENT_ID
- Enter the saved Client ID.
AUTH_OIDC_CLIENT_SECRET
- Enter the saved Client Secret.
AUTH_OIDC_METADATA_URL
- Enter the saved RHBK realm base URL.
To set up the RHBK authentication provider in your Developer Hub custom configuration, edit your custom Developer Hub ConfigMap such as
app-config-rhdh
, and add the following lines to theapp-config.yaml
content:Configure mandatory fields:
app-config.yaml
fragment with mandatory fields to enable authentication with RHBKauth: environment: production providers: oidc: production: metadataUrl: ${AUTH_OIDC_METADATA_URL} clientId: ${AUTH_OIDC_CLIENT_ID} clientSecret: ${AUTH_OIDC_CLIENT_SECRET} prompt: auto signInPage: oidc
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
- To allow the identity provider to automatically determine whether to prompt for credentials or bypass the login redirect if an active RHSSO session exists.
If prompt: auto
is not set, the identity provider defaults to prompt: none
, which assumes that you are already logged in and rejects sign-in requests without an active session.
callbackUrl
RHBK callback URL.
app-config.yaml
fragment with optionalcallbackURL
fieldauth: providers: oidc: production: callbackUrl: ${AUTH_OIDC_CALLBACK_URL}
tokenEndpointAuthMethod
Token endpoint authentication method.
app-config.yaml
fragment with optionaltokenEndpointAuthMethod
fieldauth: providers: oidc: production: tokenEndpointAuthMethod: ${AUTH_OIDC_TOKEN_ENDPOINT_METHOD}
tokenSignedResponseAlg
Token signed response algorithm.
app-config.yaml
fragment with optionaltokenSignedResponseAlg
fieldauth: providers: oidc: production: tokenSignedResponseAlg: ${AUTH_OIDC_SIGNED_RESPONSE_ALG}
scope
RHBK scope.
app-config.yaml
fragment with optionalscope
fieldauth: providers: oidc: production: scope: ${AUTH_OIDC_SCOPE}
signIn
resolvers
After successful authentication, the user signing in must be resolved to an existing user in the Developer Hub catalog. To best match users securely for your use case, consider configuring a specific resolver. Enter the resolver list to override the default resolver:
oidcSubClaimMatchingKeycloakUserId
.The authentication provider tries each sign-in resolver in order until it succeeds, and fails if none succeed.
WarningIn production mode, only configure one resolver to ensure users are securely matched.
resolver
:::: Enter the sign-in resolver name. Available values: *oidcSubClaimMatchingKeycloakUserId
*emailLocalPartMatchingUserEntityName
*emailMatchingUserEntityProfileEmail
*preferredUsernameMatchingUserEntityName
+ .
app-config.yaml
fragment with optionalresolvers
listauth: providers: oidc: production: signIn: resolvers: - resolver: oidcSubClaimMatchingKeycloakUserId - resolver: preferredUsernameMatchingUserEntityName - resolver: emailMatchingUserEntityProfileEmail - resolver: emailLocalPartMatchingUserEntityName
dangerouslyAllowSignInWithoutUserInCatalog: true
Configure the sign-in resolver to bypass the user provisioning requirement in the Developer Hub software catalog.
WarningUse this option to explore Developer Hub features, but do not use it in production.
app-config-rhdh.yaml
fragment with optional field to allow signing in users absent from the software catalogauth: environment: production providers: oidc: production: metadataUrl: ${AUTH_OIDC_METADATA_URL} clientId: ${AUTH_OIDC_CLIENT_ID} clientSecret: ${AUTH_OIDC_CLIENT_SECRET} signIn: resolvers: - resolver: oidcSubClaimMatchingKeycloakUserID dangerouslyAllowSignInWithoutUserInCatalog: true signInPage: oidc
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
- Go to the Developer Hub login page.
- Your Developer Hub sign-in page displays Sign in using OIDC and the Guest user sign-in is disabled.
- Log in with OIDC by using the saved Username and Password values.
3.2. Provisioning users from Red Hat Build of Keycloak (RHBK) to the software catalog
Prerequisites
Procedure
To enable RHBK member discovery, edit your custom Developer Hub ConfigMap, such as
app-config-rhdh
, and add the following lines to theapp-config.yaml
content:app-config.yaml
fragment with mandatorykeycloakOrg
fieldscatalog: providers: keycloakOrg: default: baseUrl: ${AUTH_OIDC_METADATA_URL} clientId: ${AUTH_OIDC_CLIENT_ID} clientSecret: ${AUTH_OIDC_CLIENT_SECRET}
baseUrl
- Your RHBK server URL, defined when enabling authentication with RHBK.
clientId
- Your Developer Hub application client ID in RHBK, defined when enabling authentication with RHBK.
clientSecret
- Your Developer Hub application client secret in RHBK, defined when enabling authentication with RHBK.
Optional: Consider adding the following optional fields:
realm
Realm to synchronize. Default value:
master
.app-config.yaml
fragment with optionalrealm
fieldcatalog: providers: keycloakOrg: default: realm: master
loginRealm
Realm used to authenticate. Default value:
master
.app-config.yaml
fragment with optionalloginRealm
fieldcatalog: providers: keycloakOrg: default: loginRealm: master
userQuerySize
User number to query simultaneously. Default value:
100
.app-config.yaml
fragment with optionaluserQuerySize
fieldcatalog: providers: keycloakOrg: default: userQuerySize: 100
groupQuerySize
Group number to query simultaneously. Default value:
100
.app-config.yaml
fragment with optionalgroupQuerySize
fieldcatalog: providers: keycloakOrg: default: groupQuerySize: 100
schedule.frequency
To specify custom schedule frequency. Supports cron, ISO duration, and "human duration" as used in code.
app-config.yaml
fragment with optionalschedule.frequency
fieldcatalog: providers: keycloakOrg: default: schedule: frequency: { hours: 1 }
schedule.timeout
To specify custom timeout. Supports ISO duration and "human duration" as used in code.
app-config.yaml
fragment with optionalschedule.timeout
fieldcatalog: providers: keycloakOrg: default: schedule: timeout: { minutes: 50 }
schedule.initialDelay
To specify custom initial delay. Supports ISO duration and "human duration" as used in code.
app-config.yaml
fragment with optionalschedule.initialDelay
fieldcatalog: providers: keycloakOrg: default: schedule: initialDelay: { seconds: 15}
Verification
Check the console logs to verify that the synchronization is completed.
Successful synchronization example:
{"class":"KeycloakOrgEntityProvider","level":"info","message":"Read 3 Keycloak users and 2 Keycloak groups in 1.5 seconds. Committing...","plugin":"catalog","service":"backstage","taskId":"KeycloakOrgEntityProvider:default:refresh","taskInstanceId":"bf0467ff-8ac4-4702-911c-380270e44dea","timestamp":"2024-09-25 13:58:04"} {"class":"KeycloakOrgEntityProvider","level":"info","message":"Committed 3 Keycloak users and 2 Keycloak groups in 0.0 seconds.","plugin":"catalog","service":"backstage","taskId":"KeycloakOrgEntityProvider:default:refresh","taskInstanceId":"bf0467ff-8ac4-4702-911c-380270e44dea","timestamp":"2024-09-25 13:58:04"}
- Log in with an RHBK account.
3.3. Creating a custom transformer to provision users from Red Hat Build of Keycloak (RHBK) to the software catalog
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
