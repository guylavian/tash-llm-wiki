---
title: "Chapter 4. Installing and configuring Keycloak - Red Hat Developer Hub 1.5 Configuring dynamic plugins"
type: reference
domain: keycloak
slug: doc-rhdh-keycloak-title-plugins-rhdh-configure-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.5/html/configuring_dynamic_plugins/rhdh-keycloak_title-plugins-rhdh-configure
guide: configuring_dynamic_plugins
documentKind: "Documentation"
abstract: "The Keycloak backend plugin, which integrates Keycloak into Developer Hub, has the following capabilities: Synchronization of Keycloak users in a realm. Synchronization of Keycloak groups and their users in a realm. Note The supported Red Hat Build of Keycloak (RHBK) version is 24.0. 4.1. Installation The Keycloak plugin is pre-loaded in Developer Hub with basic configuration properties. To enable…"
---

# Chapter 4. Installing and configuring Keycloak - Red Hat Developer Hub 1.5 Configuring dynamic plugins

Chapter 4. Installing and configuring Keycloak
The Keycloak backend plugin, which integrates Keycloak into Developer Hub, has the following capabilities:
- Synchronization of Keycloak users in a realm.
- Synchronization of Keycloak groups and their users in a realm.
The supported Red Hat Build of Keycloak (RHBK) version is 24.0
.
4.1. Installation
The Keycloak plugin is pre-loaded in Developer Hub with basic configuration properties. To enable it, set the disabled
property to false
as follows:
global:
dynamic:
includes:
- dynamic-plugins.default.yaml
plugins:
- package: ./dynamic-plugins/dist/backstage-community-plugin-catalog-backend-module-keycloak-dynamic
disabled: false
4.2. Basic configuration
To enable the Keycloak plugin, you must set the following environment variables:
-
KEYCLOAK_BASE_URL
-
KEYCLOAK_LOGIN_REALM
-
KEYCLOAK_REALM
-
KEYCLOAK_CLIENT_ID
-
KEYCLOAK_CLIENT_SECRET
4.3. Advanced configuration
Schedule configuration
You can configure a schedule in the app-config.yaml
file, as follows:
catalog:
providers:
keycloakOrg:
default:
# ...
# highlight-add-start
schedule: # optional; same options as in TaskScheduleDefinition
# supports cron, ISO duration, "human duration" as used in code
frequency: { minutes: 1 }
# supports ISO duration, "human duration" as used in code
timeout: { minutes: 1 }
initialDelay: { seconds: 15 }
# highlight-add-end
If you have made any changes to the schedule in the app-config.yaml
file, then restart to apply the changes.
Keycloak query parameters
You can override the default Keycloak query parameters in the app-config.yaml
file, as follows:
catalog:
providers:
keycloakOrg:
default:
# ...
# highlight-add-start
userQuerySize: 500 # Optional
groupQuerySize: 250 # Optional
# highlight-add-end
Communication between Developer Hub and Keycloak is enabled by using the Keycloak API. Username and password, or client credentials are supported authentication methods.
The following table describes the parameters that you can configure to enable the plugin under catalog.providers.keycloakOrg.<ENVIRONMENT_NAME>
object in the app-config.yaml
file:
| Name | Description | Default Value | Required |
|---|---|---|---|
|
|
Location of the Keycloak server, such as | "" | Yes |
|
| Realm to synchronize |
| No |
|
| Realm used to authenticate |
| No |
|
| Username to authenticate | "" | Yes if using password based authentication |
|
| Password to authenticate | "" | Yes if using password based authentication |
|
| Client ID to authenticate | "" | Yes if using client credentials based authentication |
|
| Client Secret to authenticate | "" | Yes if using client credentials based authentication |
|
| Number of users to query at a time |
| No |
|
| Number of groups to query at a time |
| No |
When using client credentials, the access type must be set to confidential
and service accounts must be enabled. You must also add the following roles from the realm-management
client role:
-
query-groups
-
query-users
-
view-users
4.4. Limitations
If you have self-signed or corporate certificate issues, you can set the following environment variable before starting Developer Hub:
NODE_TLS_REJECT_UNAUTHORIZED=0
The solution of setting the environment variable is not recommended.
