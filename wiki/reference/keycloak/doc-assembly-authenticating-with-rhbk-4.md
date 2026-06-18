---
title: "Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK) - Red Hat Developer Hub 1.8 Authentication in Red Hat Developer Hub"
type: reference
domain: keycloak
slug: doc-assembly-authenticating-with-rhbk-4
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.8/html/authentication_in_red_hat_developer_hub/assembly-authenticating-with-rhbk
guide: authentication_in_red_hat_developer_hub
documentKind: "Documentation"
---

# Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK) - Red Hat Developer Hub 1.8 Authentication in Red Hat Developer Hub

Chapter 3. Authenticating with Red Hat Build of Keycloak (RHBK)
3.1. Enabling user authentication with Red Hat Build of Keycloak (RHBK), with optional steps
Authenticate users with Red Hat Build of Keycloak (RHBK), by provisioning the users and groups from RHBK to the Developer Hub software catalog, and configuring the OpenID Connect (OIDC) authentication provider in Red Hat Developer Hub.
Prerequisites
- You added a custom Developer Hub application configuration, and have enough permissions to change it.
You have enough permissions in RHSSO to create and manage a realm and a client.
TipAlternatively, ask your RHBK administrator to prepare in RHBK the required realm and client.
Procedure
Register your Developer Hub app in RHBK:
Use an existing realm, or create a realm, with a distinctive Name such as <my_realm>. Save the value for the next step:
- RHBK realm base URL, such as: <your_rhbk_URL>/realms/<your_realm>.
To register your Developer Hub in RHBK, in the created realm, secure the first application, with:
- Client ID: A distinctive client ID, such as <RHDH>.
-
Valid redirect URIs: Set to the OIDC handler URL:
https://<my_developer_hub_domain>/api/auth/oidc/handler/frame
. - Go to the Credentials tab and copy the Client secret.
Save the values for the next step:
- Client ID
- Client Secret
- To prepare for the verification steps, in the same realm, get the credential information for an existing user or create a user. Save the user credential information for the verification steps.
Add your RHSSO credentials to Developer Hub, by adding the following key/value pairs to your Developer Hub secrets. You can use these secrets in the Developer Hub configuration files by using their environment variable name.
KEYCLOAK_CLIENT_ID
- Enter the saved Client ID.
KEYCLOAK_CLIENT_SECRET
- Enter the saved Client Secret.
KEYCLOAK_BASE_URL
- Enter the saved RHBK realm base URL.
KEYCLOAK_REALM
- Enter the realm name to provision users.
KEYCLOAK_LOGIN_REALM
- Enter the realm name to authenticate users.
Enable the Keycloak catalog provider plugin in your
dynamic-plugins.yaml
file.The plugin is named after RHBK upstream project.
This plugin imports RHBK users and groups to the Developer Hub software catalog.
plugins: - package: './dynamic-plugins/dist/backstage-community-plugin-catalog-backend-module-keycloak-dynamic' disabled: false
Enable provisioning RHBK users and groups to the Developer Hub software catalog, by adding the
catalog.providers.keycloakOrg
section to yourapp-config.yaml
file:catalog: providers: keycloakOrg: default: baseUrl: ${KEYCLOAK_BASE_URL} clientId: ${KEYCLOAK_CLIENT_ID} clientSecret: ${KEYCLOAK_CLIENT_SECRET} realm: ${KEYCLOAK_REALM} loginRealm: ${KEYCLOAK_LOGIN_REALM}
baseUrl
- Enter your RHBK server URL, defined earlier.
clientId
- Enter your Developer Hub application client ID in RHBK, defined earlier.
clientSecret
- Enter your Developer Hub application client secret in RHBK, defined earlier.
realm
- Enter the realm name to provision users.
loginRealm
- Enter the realm name to authenticate users.
Optional: Add optional fields to the
keycloackOrg
catalog provider section in yourapp-config.yaml
file:catalog: providers: keycloakOrg: default: baseUrl: ${KEYCLOAK_BASE_URL} clientId: ${KEYCLOAK_CLIENT_ID} clientSecret: ${KEYCLOAK_CLIENT_SECRET} realm: ${KEYCLOAK_REALM} loginRealm: ${KEYCLOAK_LOGIN_REALM} userQuerySize: 100 groupQuerySize: 100 schedule: frequency: { hours: 1 } timeout: { minutes: 50 } initialDelay: { seconds: 15}
userQuerySize
-
Enter the user count to query simultaneously. Default value:
100
. groupQuerySize
-
Enter the group count to query simultaneously. Default value:
100
. schedule
frequency
- Enter the schedule frequency. Supports cron, ISO duration, and "human duration" as used in code.
timeout
- Enter the timeout for the user provisioning job. Supports ISO duration and "human duration" as used in code.
initialDelay
- Enter the initial delay to wait for before starting the user provisioning job. Supports ISO duration and "human duration" as used in code.
Enable the RHBK authentication provider, by adding the OIDC provider section in your
app-config.yaml
file:auth: environment: production providers: oidc: production: metadataUrl: ${KEYCLOAK_BASE_URL} clientId: ${KEYCLOAK_CLIENT_ID} clientSecret: ${KEYCLOAK_CLIENT_SECRET} prompt: auto signInPage: oidc
environment: production
-
Mark the environment as
production
to hide the Guest login in the Developer Hub home page. metadataUrl
,clientId
,clientSecret
- Configure the OIDC provider with your secrets.
prompt
Enter
auto
to allow the identity provider to automatically determine whether to prompt for credentials or bypass the login redirect if an active RHSSO session exists.The identity provider defaults to
none
, which assumes that you are already logged in. Sign-in requests without an active session are rejected.signInPage
-
Enter
oidc
to enable the OIDC provider as default sign-in provider.
Optional: Add optional fields to the OIDC authentication provider section in your
app-config.yaml
file:auth: providers: oidc: production: metadataUrl: ${KEYCLOAK_BASE_URL} clientId: ${KEYCLOAK_CLIENT_ID} clientSecret: ${KEYCLOAK_CLIENT_SECRET} callbackUrl: ${KEYCLOAK_CALLBACK_URL} tokenEndpointAuthMethod: ${KEYCLOAK_TOKEN_ENDPOINT_METHOD} tokenSignedResponseAlg: ${KEYCLOAK_SIGNED_RESPONSE_ALG} additionalScopes: ${KEYCLOAK_SCOPE} signIn: resolvers: - resolver: oidcSubClaimMatchingKeycloakUserId - resolver: preferredUsernameMatchingUserEntityName - resolver: emailMatchingUserEntityProfileEmail - resolver: emailLocalPartMatchingUserEntityName dangerouslyAllowSignInWithoutUserInCatalog: true sessionDuration: { hours: 24 } backstageTokenExpiration: { minutes: _<user_defined_value>_ } signInPage: oidc
callbackUrl
- RHBK callback URL.
tokenEndpointAuthMethod
- Enter your token endpoint authentication method.
tokenSignedResponseAlg
- Token signed response algorithm.
additionalScopes
- Enter additional RHBK scopes to request for during the authentication flow.
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
WarningIn production mode, configure only one resolver to make sure users are securely matched.
dangerouslyAllowSignInWithoutUserInCatalog: true
Configure the sign-in resolver to bypass the user provisioning requirement in the Developer Hub software catalog.
WarningIn production mode, do not enable the
dangerouslyAllowSignInWithoutUserInCatalog
option.
sessionDuration
-
Lifespan of the user session. Enter a duration in
ms
library format (such as '24h', '2 days'), ISO duration, or "human duration" as used in code. backstageTokenExpiration
Enter a value to modify the Developer Hub token expiration from its default value of one hour. It refers to the validity of short-term cryptographic tokens, not to the session duration. The expiration value must be set between 10 minutes and 24 hours.
WarningIf multiple valid refresh tokens are issued due to frequent refresh token requests, older tokens will remain valid until they expire. Enhance security and prevent potential misuse of older tokens by enabling a refresh token rotation strategy in your RHBK realm.
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
3.2. Enabling user provisioning with LDAP
When Red Hat Build of Keycloak (RHBK) depends on Lightweight Directory Access Protocol (LDAP) to resolve user and group identities, you can opt to provision users and groups from LDAP directly to the Red Hat Developer Hub software catalog, rather than using the RHBK provisioning mechanism.
Prerequisites
- You have configured authentication with Red Hat Build of Keycloak (RHBK).
You have collected the required LDAP credentials:
- LDAP URL
-
Your LDAP server URL, such as
ldaps://ds.example.net
. - Bind dn
-
Your bind distinguished name, such as
cn=admin,OU=Users,DC=rhdh,DC=test
- LDAP secret
- Your LDAP secret.
- Recommended: LDAP certificates and keys
To use a secure LDAP connexion (
ldaps://
): you stored your LDAP certificates and keys respectively in theldap_certs.pem
andldap_keys.pem
files.WarningIn production mode, use a secure LDAP connexion.
Procedure
Enter your LDAP credentials to Developer Hub, by adding the
LDAP_SECRET
environment variable to your Developer Hub secrets.$ oc patch secret my-rhdh-secrets --patch '{"stringData": { "LDAP_SECRET": "<ldap_secret>" }}'
- <ldap_secret>
- Enter your LDAP secret.
Recommended: To use a secure LDAP connection (
ldaps://
), add your LDAP certificates and keys files to a {a-platform-generic} secret.$ oc create secret generic my-rhdh-ldap-secrets \ --from-file=./ldap_certs.pem \ --from-file=./ldap_keys.pem
Enable the LDAP catalog provider plugin in your
dynamic-plugins.yaml
file.plugins: - package: './dynamic-plugins/dist/backstage-plugin-catalog-backend-module-ldap-dynamic' disabled: false
Enable provisioning GitHub users and groups to the Developer Hub software catalog, by adding the LDAP catalog provider section to your
app-config.yaml
file:- Optional: Remove other catalog providers, by removing the other catalog providers section.
Enter the mandatory fields:
catalog: providers: ldapOrg: default: target: ldaps://ds.example.net bind: dn: cn=admin,ou=Users,dc=rhdh secret: ${LDAP_SECRET} users: - dn: OU=Users,OU=RHDH Local,DC=rhdh,DC=test options: filter: (uid=*) groups: - dn: OU=Groups,OU=RHDH Local,DC=rhdh,DC=test schedule: frequency: PT1H timeout: PT15M
target
-
Enter your LDAP server URL, such as
ldaps://ds.example.net
. bind
Enter your service account information:
dn
-
Enter your service account distinguished name (DN), such as
cn=admin,OU=Users,DC=rhdh,DC=test
secret
-
Enter the name of the variable containing your LDAP secret:
${LDAP_SECRET}
.
users
Enter information about how to find your users:
dn
- Enter the DN containing the user information.
options
filter
-
Enter your filter, such as
(uid=*)
to provision to the RHDH software catalog only users with an existinguid
.
groups
Enter information about how to find your groups:
dn
- Enter the DN containing the group information.
schedule
Enter your schedule information:
frequency
- Enter your schedule frequency, in the cron, ISO duration, or "human duration" format.
timeout
- Enter your schedule timeout, in the ISO duration or "human duration" format.
initialDelay
- Enter your schedule initial delay, in the ISO duration or "human duration" format.
Optional: To change how Developer Hub maps LDAP user fields to the software catalog, enter optional
maps
andset
fields.catalog: providers: ldapOrg: default: target: ldaps://ds.example.net bind: dn: cn=admin,ou=Users,dc=rhdh secret: ${LDAP_SECRET} users: - dn: OU=Users,OU=RHDH Local,DC=rhdh,DC=test options: filter: (uid=*) map: rdn: uid name: uid description: {} displayName: cn email: mail picture: {} memberOf: memberOf set: metadata.customField: 'hello' groups: - dn: OU=Groups,OU=RHDH Local,DC=rhdh,DC=test schedule: frequency: PT1H timeout: PT15M
rdn
-
To change the default value:
uid
, enter the relative distinguished name of each entry. name
-
To change the default value:
uid
, enter the LDAP field to map to the RHDHmetadata.name
field. description
-
To set a value, enter the LDAP field to map to the RHDH
metadata.description
field. displayName
-
To change the default value:
cn
, enter the LDAP field to map to the RHDHmetadata.displayName
field. email
-
To change the default value:
mail
, enter the LDAP field to map to the RHDHspec.profile.email
field. picture
-
To set a value, enter the LDAP field to map to the RHDH
spec.profile.picture
field. memberOf
-
To change the default value:
memberOf
, enter the LDAP field to map to the RHDHspec.memberOf
field. set
-
To set a value, enter the hard coded JSON to apply to the entities after ingestion, such as
metadata.customField: 'hello'
.
Optional: To change how Developer Hub maps LDAP group fields to the software catalog, enter optional
groups.maps
fields.catalog: providers: ldapOrg: default: target: ldaps://ds.example.net bind: dn: cn=admin,ou=Users,dc=rhdh secret: ${LDAP_SECRET} users: - dn: OU=Users,OU=RHDH Local,DC=rhdh,DC=test options: filter: (uid=*) groups: - dn: OU=Groups,OU=RHDH Local,DC=rhdh,DC=test map: rdn: uid name: uid description: {} displayName: cn email: mail picture: {} memberOf: memberOf members: member type: groupType set: metadata.customField: 'hello' schedule: frequency: PT1H timeout: PT15M
rdn
-
To change the default value:
cn
, enter the relative distinguished name of each entry. name
-
To change the default value:
cn
, enter the LDAP field to map to the RHDHmetadata.name
field. description
-
To set a value, enter the LDAP field to map to the RHDH
metadata.description
field. displayName
-
To change the default value:
cn
, enter the LDAP field to map to the RHDHmetadata.displayName
field. email
-
To change the default value:
mail
, enter the LDAP field to map to the RHDHspec.profile.email
field. picture
-
To set a value, enter the LDAP field to map to the RHDH
spec.profile.picture
field. memberOf
-
To change the default value:
memberOf
, enter the LDAP field to map to the RHDHspec.memberOf
field. members
-
To change the default value:
member
, enter the LDAP field to map to the RHDHspec.children
field. type
-
To change the default value:
groupType
, enter the LDAP field to map to the RHDHspec.type
field. set
-
To set a value, enter the hard coded JSON to apply to the entities after ingestion, such as
metadata.customField: 'hello'
.
Recommended: To use a secure LDAP connection (
ldaps://
), enter optionaltls
fields.Optional
tls
fieldscatalog: providers: ldapOrg: default: target: ldaps://ds.example.net bind: dn: cn=admin,ou=Users,dc=rhdh secret: ${LDAP_SECRET} users: ldapOrg: default: tls: rejectUnauthorized: true keys: '/path/to/keys.pem' certs: '/path/to/certs.pem'
rejectUnauthorized
Set to
false
to allow self-signed certificatesWarningThis option is not recommended for production.
keys
- Enter a file containing private keys in PEM format
certs
- Enter a file containing cert chains in PEM format
Optional: Enter configuration for vendor-specific attributes to set custom attribute names for distinguished names (DN) and universally unique identifiers (UUID) in LDAP directories. Default values are defined per supported vendor and automatically detected.
catalog: providers: ldapOrg: default: vendor: dnAttributeName: customDN uuidAttributeName: customUUID
dnAttributeName
- Enter the attribute name that holds the distinguished name (DN) for an entry.
uuidAttributeName
- Enter the attribute name that holds a universal unique identifier (UUID) for an entry.
Optional: Enter low level users and groups configuration in the
options
subsection.catalog: providers: ldapOrg: default: target: ldaps://ds.example.net bind: dn: cn=admin,ou=Users,dc=rhdh secret: ${LDAP_SECRET} users: options: scope: sub filter: (uid=*) attributes: - cn - uid - description paged: pageSize: 500 groups: options: scope: sub filter: (cn=*) attributes: - cn - uid - description paged: pageSize: 500 pagePause: true
scope
To change the default value:
one
, enter how deep the search should go within the directory tree:-
base
to search only the base DN. -
one
to search one level below the base DN. -
sub
to search all descendant entries.
-
filter
To change the default value:
(objectclass=*)
, enter your LDAP filter. With the default mapping:-
For users, enter
(uid=*)
to make sure only users with valid uid field is synced, since users without uid will cause error and ingestion fails. For groups, enter
(cn=*)
TipWhen you change the mapping, also update the filter.
-
For users, enter
attributes
-
To change the default value: all attributes
['*', '+']
, enter the array of attribute names to import from LDAP. paged
Enter a value to enable paged results.
pageSize
-
Enter a value to set the results page size, such as
500
. pagePause
-
Enter
true
to tell the client to wait for the asynchronous results of the next page, when the page limit has been reached.
Recommended: To use a secure LDAP connection (
ldaps://
), mount your LDAP certificates and keys files in your Developer Hub deployment, by editing your Backstage custom resource.kind: Backstage spec: application: extraFiles: mountPath: /opt/ldap-secrets secrets: - name: my-rhdh-database-database-secrets key: ldap-certs.pem, ldap-keys.pem
Verification
To verify user and group provisioning, check the console logs.
Successful synchronization example:
2025-10-15T20:45:49.072Z catalog info Read 4 LDAP users and 6 LDAP groups in 0.3 seconds. Committing... class="LdapOrgEntityProvider" taskId="LdapOrgEntityProvider:default:refresh" taskInstanceId="9bb48fd5-2f55-4096-9fd0-61cee6679952" trace_id="6a318e2eadba84e20df773948668aa4c" span_id="cbec568cb6e64985" trace_flags="01" 2025-10-15T20:45:49.075Z catalog info Committed 4 LDAP users and 6 LDAP groups in 0.0 seconds. class="LdapOrgEntityProvider" taskId="LdapOrgEntityProvider:default:refresh" taskInstanceId="9bb48fd5-2f55-4096-9fd0-61cee6679952" trace_id="6a318e2eadba84e20df773948668aa4c" span_id="cbec568cb6e64985" trace_flags="01"
3.3. Creating a custom transformer to provision users from Red Hat Build of Keycloak (RHBK) to the software catalog
Customize how Red Hat Developer Hub provisions users and groups to Red Hat Developer Hub software catalog entities, by creating a backend module that uses the keycloakTransformerExtensionPoint
to offer custom user and group transformers for the Keycloak backend.
Prerequisites
Procedure
-
Create a new backend module with the
yarn new
command. Add your custom user and group transformers to the
keycloakTransformerExtensionPoint
.The following is an example
plugins/<module_name>/src/module.ts
file defining the backend module:import { GroupTransformer, keycloakTransformerExtensionPoint, UserTransformer, } from '@backstage-community/plugin-catalog-backend-module-keycloak'; const customGroupTransformer: GroupTransformer = async ( entity, // entity output from default parser realm, // Keycloak realm name groups, // Keycloak group representation ) => { /* apply transformations */ return entity; }; const customUserTransformer: UserTransformer = async ( entity, // entity output from default parser user, // Keycloak user representation realm, // Keycloak realm name groups, // Keycloak group representation ) => { /* apply transformations */ return entity; }; export const keycloakBackendModuleTransformer = createBackendModule({ pluginId: 'catalog', moduleId: 'keycloak-transformer', register(reg) { reg.registerInit({ deps: { keycloak: keycloakTransformerExtensionPoint, }, async init({ keycloak }) { keycloak.setUserTransformer(customUserTransformer); keycloak.setGroupTransformer(customGroupTransformer); /* highlight-add-end */ }, }); }, });
ImportantSet the module’s
pluginId
tocatalog
to match thepluginId
of thekeycloak-backend
; otherwise, the module fails to initialize.Install this new backend module into your Developer Hub backend.
$ backend.add(import(backstage-plugin-catalog-backend-module-keycloak-transformer))
Verification
Developer Hub imports the users and groups each time when started. Check the console logs to verify the synchronization result.
Successful synchronization example:
{"class":"KeycloakOrgEntityProvider","level":"info","message":"Read 3 Keycloak users and 2 Keycloak groups in 1.5 seconds. Committing...","plugin":"catalog","service":"backstage","taskId":"KeycloakOrgEntityProvider:default:refresh","taskInstanceId":"bf0467ff-8ac4-4702-911c-380270e44dea","timestamp":"2024-09-25 13:58:04"} {"class":"KeycloakOrgEntityProvider","level":"info","message":"Committed 3 Keycloak users and 2 Keycloak groups in 0.0 seconds.","plugin":"catalog","service":"backstage","taskId":"KeycloakOrgEntityProvider:default:refresh","taskInstanceId":"bf0467ff-8ac4-4702-911c-380270e44dea","timestamp":"2024-09-25 13:58:04"}
- After the first import is complete, go to the Catalog page and select User to view the list of users.
- When you select a user, you see the information imported from RHBK.
- You can select a group, view the list, and access or review the information imported from RHBK.
- You can log in with an RHBK account.
