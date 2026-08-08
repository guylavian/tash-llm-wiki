---
title: "Chapter 4. Enabling and configuring the Keycloak plugin - Red Hat Developer Hub 1.7 Configuring dynamic plugins"
type: reference
domain: keycloak
slug: doc-assembly-enabling-configuring-the-keycloak-plugin-assembly-installing-configuring-jfrog-3
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.7/html/configuring_dynamic_plugins/assembly-enabling-configuring-the-keycloak-plugin_assembly-installing-configuring-jfrog
guide: configuring_dynamic_plugins
documentKind: "Documentation"
abstract: "The Keycloak backend plugin, which integrates Keycloak into Developer Hub, has the following capabilities: Synchronization of Keycloak users in a realm. Synchronization of Keycloak groups and their users in a realm. Note The supported Red Hat Build of Keycloak (RHBK) version is 26.0. 4.1. Enabling the Keycloak plugin Prerequisites To enable the Keycloak plugin, you must set the following environme…"
---

# Chapter 4. Enabling and configuring the Keycloak plugin - Red Hat Developer Hub 1.7 Configuring dynamic plugins

Chapter 4. Enabling and configuring the Keycloak plugin
The Keycloak backend plugin, which integrates Keycloak into Developer Hub, has the following capabilities:
- Synchronization of Keycloak users in a realm.
- Synchronization of Keycloak groups and their users in a realm.
The supported Red Hat Build of Keycloak (RHBK) version is 26.0
.
4.1. Enabling the Keycloak plugin
Prerequisites
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
-
Procedure
The Keycloak plugin is pre-loaded in Developer Hub with basic configuration properties. To enable it, set the
disabled
property tofalse
as follows:global: dynamic: includes: - dynamic-plugins.default.yaml plugins: - package: ./dynamic-plugins/dist/backstage-community-plugin-catalog-backend-module-keycloak-dynamic disabled: false
4.2. Configuring the Keycloak plugin
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
4.3. Metrics
The Keycloak backend plugin supports OpenTelemetry metrics that you can use to monitor fetch operations and diagnose potential issues.
4.3.1. Available Counters
| Metric Name | Description |
|---|---|
|
| Counts fetch task failures where no data was returned due to an error. |
|
| Counts partial data batch failures. Even if some batches fail, the plugin continues fetching others. |
4.3.2. Labels
All counters include the taskInstanceId
label, which uniquely identifies each scheduled fetch task. You can use this label to trace failures back to individual task executions.
Users can enter queries in the Prometheus UI or Grafana to explore and manipulate metric data.
In the following examples, a Prometheus Query Language (PromQL) expression returns the number of backend failures.
Example to get the number of backend failures associated with a taskInstanceId
backend_keycloak_fetch_data_batch_failure_count_total{taskInstanceId="df040f82-2e80-44bd-83b0-06a984ca05ba"} 1
Example to get the number of backend failures during the last hour
sum(backend_keycloak_fetch_data_batch_failure_count_total) - sum(backend_keycloak_fetch_data_batch_failure_count_total offset 1h)
PromQL supports arithmetic operations, comparison operators, logical/set operations, aggregation, and various functions. Users can combine these features to analyze time-series data effectively.
Additionally, the results can be visualized using Grafana.
4.3.3. Exporting Metrics
You can export metrics using any OpenTelemetry-compatible backend, such as Prometheus.
See the Backstage OpenTelemetry setup guide for integration instructions.
4.4. Limitations
If you have self-signed or corporate certificate issues, you can set the following environment variable before starting Developer Hub:
NODE_TLS_REJECT_UNAUTHORIZED=0
The solution of setting the environment variable is not recommended.
