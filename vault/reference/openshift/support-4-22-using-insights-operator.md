---
title: "Using the Insights Operator"
type: reference
domain: openshift
slug: support-4-22-using-insights-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/using-insights-operator
version: 4.22
family: support
documentKind: "Documentation"
---

# Using the Insights Operator

[id="using-insights-operator"]
= Using the Insights Operator

[role="_abstract"]
The {insights-operator} periodically gathers configuration and component failure status and, by default, reports that data every two hours to Red{nbsp}Hat. This information enables Red{nbsp}Hat to assess configuration and deeper failure data than is reported through Telemetry. Users of OpenShift Container Platform can display the report in the {insights-advisor-url} service on {hybrid-console}.

[role="_additional-resources"]
.Additional resources

* Remote health reporting
* Using {red-hat-lightspeed} to identify issues with your cluster

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="insights-operator-configuring_{context}"]
= Configuring {insights-operator}

[role="_abstract"]
{insights-operator} configuration is a combination of the default Operator configuration and the configuration that is stored in either the *insights-config* `ConfigMap` object in the `openshift-insights` namespace, OR in the support secret in the `openshift-config` namespace.

When a `ConfigMap` object or support secret exists, the contained attribute values override the default Operator configuration values. If both a `ConfigMap` object _and_ a support secret exist, the Operator reads the `ConfigMap` object.

The `ConfigMap` object does not exist by default, so an OpenShift Container Platform cluster administrator must create it.

//[NOTE]
//====
//{red-hat-lightspeed} encourages cluster administrators to use the config-map configuration method. Support secrets will continue to be supported in the near future but will eventually be deprecated.
//====

[id="insights-operator-configuring-configmap_{context}"]
== ConfigMap object configuration structure

This example of an *insights-config* `ConfigMap` object (`config.yaml` configuration) shows configuration options by using standard YAML formatting.

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: insights-config
  namespace: openshift-insights
data:
  config.yaml: |
    dataReporting:
      uploadEndpoint: https://console.redhat.com/api/ingress/v1/upload
      storagePath: /var/lib/insights-operator
      downloadEndpoint: https://console.redhat.com/api/insights-results-aggregator/v2/cluster/%s/reports
      conditionalGathererEndpoint: https://console.redhat.com/api/gathering/gathering_rules
    sca:
        disabled: false
        endpoint: https://api.openshift.com/api/accounts_mgmt/v1/entitlement_certificates
        interval: 8h0m0s
    alerting:
        disabled: false
    proxy:
        httpProxy: http://example.com
        httpsProxy: https://example.com
        noProxy: test.org
----

**Configurable attributes and default values**

The following table describes the available configuration attributes:

[NOTE]
====
The *insights-config* `ConfigMap` object follows standard YAML formatting, wherein child values are below the parent attribute and indented two spaces. For the *Obfuscation* attribute, enter values as bulleted children of the parent attribute.
====

.{insights-operator} configurable attributes
[cols=".^2l,.^3a,.^1a,.^1a",options="header"]
|====
|Attribute name|Description|Value type|Default value

|alerting:
    disabled: false
|Disables {insights-operator} alerts to the cluster Prometheus instance.
|Boolean
|`false`

|clusterTransfer:
    endpoint: <url>
|The endpoint for checking and downloading cluster transfer data.
|URL
|https://api.openshift.com/api/accounts_mgmt/v1/cluster_transfers/

|clusterTransfer:
    interval: 1h0m0s
|Sets the frequency for checking available cluster transfers.
|Time interval
|`24h`

|dataReporting:
    interval: 30m0s
|Sets the data gathering and upload frequency.
|Time interval
|`2h`

|dataReporting:
    uploadEndpoint: <url>
|Sets the upload endpoint.
|URL
|https://console.redhat.com/api/ingress/v1/upload

|dataReporting:
    storagePath: <path>
|Configures the path where archived data gets stored.
|File path
|/var/lib/insights-operator

|dataReporting:
    downloadEndpoint: <url>
|Specifies the endpoint for downloading the latest {red-hat-lightspeed} analysis.
|URL
|https://console.redhat.com/api/ingress/v1/download

|dataReporting:
    conditionalGathererEndpoint: <url>
|Sets the endpoint for providing conditional gathering rule definitions.
|URL
|https://console.redhat.com/api/gathering/gathering_rules

|dataReporting:
    obfuscation:
    - networking
|Enables the global obfuscation of IP addresses and the cluster domain name.
|String
|Not applicable

|dataReporting:
    obfuscation:
    - workload_names
|Enables the obfuscation of Data Validation Operator data. The cluster resource ID is only visible in the archive file and not the resource name.
|String
|Not applicable

|proxy:
    httpProxy: http://example.com
    httpsProxy: http://example.com
    noProxy: test.org
|Set custom proxy for {insights-operator}.
|URL
|No default

|sca:
    interval: 8h0m0s
|Specifies the frequency of the simple content access (SCA) entitlements download.
|Time interval
|`2h`

|sca:
    endpoint: <url>
|Specifies the endpoint for downloading the simple content access (SCA) entitlements.
|URL
|https://api.openshift.com/api/accounts_mgmt/v1/entitlement_certificates

|sca:
    disabled: false
|Disables the simple content access entitlements download.
|Boolean
|`false`
|====
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="insights-operator-insights-config_{context}"]
= Creating the insights-config ConfigMap object

[role="_abstract"]
This procedure describes how to create the *insights-config* `ConfigMap` object for the {insights-operator} to set custom configurations.

[IMPORTANT]
====
Red{nbsp}Hat recommends you consult Red{nbsp}Hat Support before making changes to the default {insights-operator} configuration.
====

.Prerequisites

* Remote health reporting is enabled, which is the default.
* You are logged in to the OpenShift Container Platform web console as a user with `cluster-admin` role.

.Procedure

. Go to *Workloads* -> *ConfigMaps* and select *Project: openshift-insights*.
. Click *Create ConfigMap*.
. Select *Configure via: YAML view* and enter your configuration preferences, for example
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: insights-config
  namespace: openshift-insights
data:
  config.yaml: |
    dataReporting:
      obfuscation:
        - networking
        - workload_names
    sca:
      disabled: false
      interval: 2h
    alerting:
       disabled: false
binaryData: {}
immutable: false
----

. Optional: Select *Form view* and enter the necessary information that way.
. In the *ConfigMap Name* field, enter *insights-config*.
. In the *Key* field, enter *config.yaml*.
. For the *Value* field, either browse for a file to drag and drop into the field or enter your configuration parameters manually.
. Click *Create* and you can see the `ConfigMap` object and configuration information.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="understanding-insights-operator-alerts_{context}"]
= Understanding {insights-operator} alerts

[role="_abstract"]
The {insights-operator} declares alerts through the Prometheus monitoring system to the Alertmanager. You can view these alerts in the Alerting UI in the OpenShift Container Platform web console by using one of the following methods:

* In the *Administrator* perspective, click *Observe* -> *Alerting*.
* In the *Developer* perspective, click *Observe* -> <project_name> -> *Alerts* tab.

Currently, {insights-operator} sends the following alerts when the conditions are met:

.{insights-operator} alerts
[options="header"]
|====
|Alert|Description
|`InsightsDisabled`|{insights-operator} is disabled.
|`SimpleContentAccessNotAvailable`|Simple content access is not enabled in Red Hat Subscription Management.
|`InsightsRecommendationActive`|{red-hat-lightspeed} has an active recommendation for the cluster.
|====

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="disabling-insights-operator-alerts_{context}"]
= Disabling {insights-operator} alerts

[role="_abstract"]
To prevent the {insights-operator} from sending alerts to the cluster Prometheus instance, you create or edit the *insights-config* `ConfigMap` object.

[NOTE]
====
Previously, a cluster administrator would create or edit the {insights-operator} configuration using a *support secret* in the `openshift-config` namespace. {red-hat-lightspeed} now supports the creation of a `ConfigMap` object to configure the Operator. The Operator gives preference to the config map configuration over the support secret if both exist.
====

If the *insights-config* `ConfigMap` object does not exist, you must create it when you first add custom configurations. Note that configurations within the `ConfigMap` object take precedence over the default settings defined in the `config/pod.yaml` file.

.Prerequisites

* Remote health reporting is enabled, which is the default.
* You are logged in to the OpenShift Container Platform web console as `cluster-admin`.
* You are logged in to the OpenShift Container Platform web console as a user with the `dedicated-admin` role.
* The *insights-config* `ConfigMap` object exists in the `openshift-insights` namespace.

.Procedure

. Go to *Workloads* -> *ConfigMaps* and select *Project: openshift-insights*.
. Click on the *insights-config* `ConfigMap` object to open it.
. Click *Actions* and select *Edit ConfigMap*.
. Click the *YAML view* radio button.
. In the file, set the `alerting` attribute to `disabled: true`.
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
# ...
data:
  config.yaml: |
    alerting:
      disabled: true
# ...
----

. Click *Save*. The *insights-config* config-map details page opens.
. Verify that the value of the `config.yaml` `alerting` attribute is set to `disabled: true`.
+
After you save the changes, {insights-operator} no longer sends alerts to the cluster Prometheus instance.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="enabling-insights-operator-alerts_{context}"]
= Enabling {insights-operator} alerts

[role="_abstract"]
When alerts are disabled, the {insights-operator} no longer sends alerts to the cluster Prometheus instance. You can reenable them.

[NOTE]
====
Previously, a cluster administrator would create or edit the {insights-operator} configuration using a *support secret* in the `openshift-config` namespace. {red-hat-lightspeed} now supports the creation of a `ConfigMap` object to configure the {insights-operator}. The {insights-operator} gives preference to the config map configuration over the support secret if both exist.
====

.Prerequisites

* Remote health reporting is enabled, which is the default.
* You are logged in to the OpenShift Container Platform web console as `cluster-admin`.
* You are logged in to the OpenShift Container Platform web console as a user with the `dedicated-admin` role.
* The *insights-config* `ConfigMap` object exists in the `openshift-insights` namespace.

.Procedure

. Go to *Workloads* -> *ConfigMaps* and select *Project: openshift-insights*.
. Click on the *insights-config* `ConfigMap` object to open it.
. Click *Actions* and select *Edit ConfigMap*.
. Click the *YAML view* radio button.
. In the file, set the `alerting` attribute to `disabled: false`.
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
# ...
data:
  config.yaml: |
    alerting:
      disabled: false
# ...
----

. Click *Save*. The *insights-config* config-map details page opens.
. Verify that the value of the `config.yaml` `alerting` attribute is set to `disabled: false`.
+
After you save the changes, {insights-operator} again sends alerts to the cluster Prometheus instance.

// cannot create resource "pods/exec" in API group "" in the namespace "openshift-insights"

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="insights-operator-downloading-archive_{context}"]
= Downloading your {insights-operator} archive

[role="_abstract"]
{insights-operator} stores gathered data in an archive located in the `openshift-insights` namespace of your cluster. You can download and review the data that is gathered by the {insights-operator}.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

. Find the name of the running pod for the {insights-operator}:
+
[source,terminal]
----
$ oc get pods --namespace=openshift-insights -o custom-columns=:metadata.name --no-headers  --field-selector=status.phase=Running
----

. Copy the recent data archives collected by the {insights-operator}:
+
[source,terminal]
----
$ oc cp openshift-insights/<insights_operator_pod_name>:/var/lib/insights-operator ./insights-data
----
+
Replace `<insights_operator_pod_name>` with the pod name output from the preceding command.
+
The recent {insights-operator} archives are now available in the `insights-data` directory.

// cannot download archive using previous module

// InsightsDataGather is a Tech Preview feature. When the feature goes GA, verify if it can be added to ROSA/OSD.

// tech preview feature
[id="running-insights-operator-gather_using-insights-operator"]
== Running an {insights-operator} gather operation on-demand

Instead of waiting for the next periodic data gather operation, you can run a custom on-demand {insights-operator} data gather operation by using the OpenShift Container Platform web console or command-line interface (CLI).

A periodic data gather operation uses the `InsightsDataGather` custom resource definition (CRD) for configuration instructions, whereas an on-demand equivalent requires a `DataGather` CRD to be configured.

An on-demand `DataGather` operation is:

* Useful for one-off data collections that require different CRD configurations to the periodic data gathering (`InsightsDataGather`) specification.
* Independent from the periodic data gathering. When you create an on-demand `DataGather` CRD, the configuration is independent from the `InsightsDataGather` CRD specification of your periodic data gathering job.

**Custom specification options**

You can optionally customize the following items for the on-demand data gather operation:

* *Enable and define data obfuscation:* By defining the `DataGather` `dataPolicy` specification, you can enable additional obfuscation of the {red-hat-lightspeed} archive data, for example, the IP address or workload names.

* *Enable persistant storage:* By default, the {insights-operator} uses ephemeral storage, which means that a new pod will be created for each gather operation and the history of gather operations and data collected is not retained. You can switch to persistent storage to retain the data and history for up to the last 10 gather operations by defining the `DataGather` `storage` specification in the CRD.

* *Exclude specific data gather operations:*  You can choose to disable specific gather operations from running by defining the `DataGather` `gatherers` specification. For example, you can choose to disable the cluster authentication operation or the workload data operation.

[IMPORTANT]
====
Excluding gather operations from the default list might reduce or limit the  recommendations offered by the {red-hat-lightspeed} advisor service for your cluster.
====

If you do not configure any custom specification options in the `DataGather` CRD, the default {insights-operator} data collection job will run. This means that all gather operations will run, the collected data will be unobfuscated and the archive file will not be retained.

When you run a gather operation on-demand, any configuration that was previously applied to disable {insights-operator} gather operations for your cluster will be overridden.

[NOTE]
====
If you enable Technology Preview in your cluster, the {insights-operator} runs gather operations in individual pods. This is part of the Technology Preview feature set for the {insights-operator} and supports the new data gathering features.
====
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="insights-operator-gather-duration_{context}"]
= Viewing {insights-operator} gather durations

[role="_abstract"]
You can view the time it takes for the {insights-operator} to gather the information contained in the archive. This helps you to understand {insights-operator} resource usage and issues with {red-hat-lightspeed} Advisor.

.Prerequisites

* A recent copy of your {insights-operator} archive.

.Procedure

. From your archive, open `/insights-operator/gathers.json`.
+
The file contains a list of {insights-operator} gather operations:
+
[source,json]
----
    {
      "name": "clusterconfig/authentication",
      "duration_in_ms": 730,
      "records_count": 1,
      "errors": null,
      "panic": null
    }
----
+
The `duration_in_ms` field is the amount of time in milliseconds for each gather operation.

. Inspect each gather operation for abnormalities.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="running-insights-operator-gather-web-console_{context}"]
= Gathering data on demand with the {insights-operator} from the web console

[role="_abstract"]
You can run a custom {insights-operator} gather operation on-demand from the OpenShift Container Platform web console. An on-demand `DataGather` operation is useful for one-off data collections that require different configurations to the periodic data gathering (`InsightsDataGather`) specification.

Use the following procedure to create a `DataGather` custom resource definition (CRD), and then run the data gather operation on demand from the web console.

.Prerequisites

* You are logged in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

.Procedure

. On the console, select *Administration* > *CustomResourceDefinitions*.
. On the *CustomResourceDefinitions* page, in the *Search by name* field, find the *DataGather* resource definition, and then click it.
. On the *CustomResourceDefinition details* page, click the *Instances* tab.
. Click *Create DataGather*.
. To create a new `DataGather` operation where all gather operations will run, complete the following YAML specification, and then save your changes.
+
[source,yaml]
----

apiVersion: insights.openshift.io/v1alpha2
kind: DataGather
metadata:
  name: <your_data_gather>
spec:
# Gatherers configuration
  gatherers:
    mode: All # Options: All, Custom
# ...
----
+
[IMPORTANT]
====
* The name you specify for your gather operation, `<your_data_gather>`, must be unique and must not include a prefix of `periodic-gathering-` because this string is reserved for other administrative operations and might impact the intended gather operation.
* If the `spec` of `DataGather` CRD is undefined, the default {insights-operator} data collection job will run. This means that all gather operations will run, the collected data will be unobfuscated and the archive file will not be retained.
====
+
. Optional: To customize the data gather operation, you can configure any of the following options in your `DataGather` YAML file:
* To disable specific gatherers, change the value of `mode` to *Custom*, and then specify the individual gatherer that you intend to disable. For example, to disable the workload gatherer, add the following example:
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha2
kind: DataGather
metadata:
  name: <your_data_gather>
spec:
    # Gatherers configuration
  gatherers:
    mode: Custom  # Options: All, Custom
    custom:
      configs:
        # Essential cluster configuration gatherers
        - name: clusterconfig/authentication
          state: Enabled
        - name: clusterconfig/clusteroperators
          state: Enabled
        - name: workloads
          state: Disabled
----
* To enable persistent storage to retain the data archive file and history for up to the last 10 data gathering jobs, define the `storage` specification. Set *type* to `PersistentVolume`, and define the `mountPath` and `name` of the volume, as outlined in the following example:
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha2
kind: DataGather
metadata:
  name: <your_data_gather>
spec:
  storage:
    type: PersistentVolume
    mountPath: /data
    persistentVolume:
      claim:
        name: on-demand-gather-pvc
----
+
[IMPORTANT]
====
Ensure that the volume name specified matches the existing `PersistentVolumeClaim` value in the `openshift-insights` namespace. For more information, see Persistent volume claims.
====
* To enable data obfuscation, define the `dataPolicy` key and required values. For example, to obfuscate IP addresses and workload names, add the following configuration:
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha2
kind: DataGather
metadata:
  name: <your_data_gather>
spec:
  dataPolicy:
    - ObfuscateNetworking
    - WorkloadNames
----

.Verification

. On the console, select to *Workloads* > *Pods*.
. On the Pods page, go to the *Project* pull-down menu, and then select *Show default projects*.
. Select the `openshift-insights` project from the *Project* pull-down menu.
. Check that your new gather operation is prefixed with your chosen name under the list of pods in the `openshift-insights` project. Upon completion, the {insights-operator} automatically uploads the data to Red Hat for processing.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="running-insights-operator-gather-openshift-cli_{context}"]
= Gathering data on demand with the {insights-operator} from the OpenShift CLI

[role="_abstract"]
You can run a custom {insights-operator} gather operation on-demand from the  OpenShift Container Platform command-line interface (CLI).
An on-demand `DataGather` operation is useful for one-off data collections that require different configurations to the periodic data gathering (`InsightsDataGather`) specification.

Use the following procedure to create a `DataGather` custom resource definition (CRD), and then run the data gather operation on demand from the CLI.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.

.Procedure

. Create a YAML file with the following `DataGather` specification:
+
[source,yaml]
----

apiVersion: insights.openshift.io/v1alpha2
kind: DataGather
metadata:
  name: <your_data_gather>
spec:
# Gatherers configuration
  gatherers:
    mode: All # Options: All, Custom
# ...
----
+
[IMPORTANT]
====
* The name you specify for your gather operation, `<your_data_gather>`, must be unique and must not include a prefix of `periodic-gathering-` because this string is reserved for other administrative operations and might impact the intended gather operation.
* If the `spec` of `DataGather` CRD is undefined, the default {insights-operator} data collection job will run. This means that all gather operations will run, the collected data will be unobfuscated and the archive file will not be retained.
====
+
. Optional: To customize the data gather operation, you can configure any of the following options in your `DataGather` YAML file:
* To disable specific gatherers, change the value of `mode` to *Custom*, and then specify the individual gatherer that you intend to disable. For example, to disable the workload gatherer, add the following example:
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha2
kind: DataGather
metadata:
  name: <your_data_gather>
spec:
    # Gatherers configuration
  gatherers:
    mode: Custom  # Options: All, Custom
    custom:
      configs:
        # Essential cluster configuration gatherers
        - name: clusterconfig/authentication
          state: Enabled
        - name: clusterconfig/clusteroperators
          state: Enabled
        - name: workloads
          state: Disabled
----
* To enable persistent storage to retain the data archive file and history for up to the last 10 data gathering jobs, define the `storage` specification. Set *type* to `PersistentVolume`, and define the `mountPath` and `name` of the volume, as outlined in the following example:
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha2
kind: DataGather
metadata:
  name: <your_data_gather>
spec:
  storage:
    type: PersistentVolume
    mountPath: /data
    persistentVolume:
      claim:
        name: on-demand-gather-pvc
----
+
[IMPORTANT]
====
Ensure that the volume name specified matches the existing `PersistentVolumeClaim` value in the `openshift-insights` namespace. For more information, see Persistent volume claims.
====
+
* To enable data obfuscation, define the `dataPolicy` key and required values. For example, to obfuscate IP addresses and workload names, add the following configuration:
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha2
kind: DataGather
metadata:
  name: <your_data_gather>
spec:
  dataPolicy:
    - ObfuscateNetworking
    - WorkloadNames
----
+
. On the OpenShift Container Platform CLI, enter the following command to run the gather operation:
+
[source,terminal]
----
$ oc apply -f <your_data_gather_definition>.yaml
----

.Verification

* Check that your new gather operation is prefixed with your chosen name under the list of pods in the `openshift-insights` project. Upon completion, the {insights-operator} automatically uploads the data to Red Hat for processing.

[role="_additional-resources"]
.Additional resources
* {insights-operator} Gathered Data GitHub repository

// cannot list resource "secrets" in API group "" in the namespace "openshift-config"
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="disabling-insights-operator-gather_{context}"]
= Disabling the {insights-operator} periodic gather operations

[role="_abstract"]
You can optionally disable the periodic `InsightsDataGather` operations that the {insights-operator} runs every 2 hours by default. Disabling the periodic data gather operations increases privacy for your organization as {insights-operator} will no longer gather and send {red-hat-lightspeed} cluster reports to Red{nbsp}Hat.

Disabling gather operations will also disable {red-hat-lightspeed} analysis and recommendations for your cluster without affecting other core functions that require communication with Red{nbsp}Hat such as cluster transfers.

You can view a list of attempted gather operations for your cluster from the `/insights-operator/gathers.json` file in your {insights-operator} archive. Be aware that some gather operations occur only when certain conditions are met and might not show in your most recent archive.

[NOTE]
====
If you enable Technology Preview in your cluster, the {insights-operator} runs gather operations in individual pods. This is part of the Technology Preview feature set for the {insights-operator} and supports the new data gathering features.
====

.Prerequisites

* You are logged in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.
* You are logged in to the OpenShift Container Platform web console as a user with the `dedicated-admin` role.

.Procedure

. Navigate to *Administration* > *CustomResourceDefinitions*.
. On the *CustomResourceDefinitions* page, use the *Search by name* field to find the *InsightsDataGather* custom resource definition (CRD), and click to open.
. On the *CustomResourceDefinition details* page, click the *Instances* tab.
. Click *cluster*, and then click the *YAML* tab.
. Edit the `InsightsDataGather` CRD, and complete one of the following steps:
** To disable all the gather operations and data collection, define the `gatherers` specification and set the `mode` to *None* as outlined in the following example extract:
+
[source,yaml]
----

apiVersion: insights.openshift.io/v1alpha2
kind: InsightsDataGather
metadata:
  name: cluster
spec:
# Gatherers configuration
  gatherers:
    mode: None # Options: All, None, Custom
----
** To disable individual gather operations, under `gatherers`, set the `mode` to *Custom* and then specify the individual gatherer that you intend to disable. For example, to disable the workload gatherer, define the following specification:
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha2
kind: InsightsDataGather
metadata:
  name: cluster
spec:
    # Gatherers configuration
  gatherers:
    mode: Custom  # Options: All, None, Custom
    custom:
      configs:
        # Essential cluster configuration gatherers
        - name: clusterconfig/authentication
          state: Enabled
        - name: clusterconfig/clusteroperators
          state: Enabled
        - name: workloads
          state: Disabled
----
. Click *Save*.

.Results

After you save the changes, the {insights-operator} gather configurations are updated and the operations that you disabled in the configuration will no longer occur.

[NOTE]
====
Disabling gather operations restricts the ability of the {red-hat-lightspeed} advisor service to offer effective recommendations for your cluster.
====

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="enabling-insights-operator-gather_{context}"]
= Re-enabling the {insights-operator} periodic gather operations

[role="_abstract"]
If you disabled the default `InsightsDataGather` data gather operations, you can enable them again so that the {insights-operator} resumes the periodic data collection, and sends the resulting {red-hat-lightspeed} cluster reports to Red{nbsp}Hat.

.Prerequisites

* You are logged in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.
* You are logged in to the OpenShift Container Platform web console as a user with the `dedicated-admin` role.

.Procedure

. Navigate to *Administration* > *CustomResourceDefinitions*.
. On the *CustomResourceDefinitions* page, use the *Search by name* field to find the *InsightsDataGather* custom resource definition (CRD), and click to open.
. On the *CustomResourceDefinition details* page, click the *Instances* tab.
. Click *cluster*, and then click the *YAML* tab.
. Edit the `InsightsDataGather` CRD, and complete one of the following steps:

** To enable all disabled gather operations, under the `gatherers` specification, set the `mode` back to *All* as outlined in the following example extract:
+
[source,yaml]
----

apiVersion: insights.openshift.io/v1alpha2
kind: InsightsDataGather
metadata:
  name: cluster
spec:
# Gatherers configuration
  gatherers:
    mode: All # Options: All, None, Custom
----

** To enable individual gather operations that were previously disabled, find the name of the gatherer operation under the `gatherers:custom:configs` key section and change the `state` to *Enabled*. Alternatively, under the `config` specification, remove the `name` and `state` configuration lines for the operation you want to enable.
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha2
kind: InsightsDataGather
metadata:
  name: cluster
spec:
    # Gatherers configuration
  gatherers:
    mode: Custom  # Options: All, None, Custom
    custom:
      configs:
        # Essential cluster configuration gatherers
        - name: clusterconfig/authentication
          state: Enabled
        - name: clusterconfig/clusteroperators
          state: Enabled
        - name: workloads
          state: Enabled
----
+
. Click *Save*.
+
After you save the changes, the {insights-operator} gather configurations are updated and the affected gather operations start.
+
[NOTE]
====
Disabling gather operations restricts the ability of the {red-hat-lightspeed} advisor service to offer effective recommendations for your cluster.
====

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc

[id="obfuscating-deployment-validation-operator-data_{context}"]
= Obfuscating Deployment Validation Operator data

[role="_abstract"]
By default, when you install the Deployment Validation Operator (DVO), the name and unique identifier (UID) of a resource are included in the data that is captured and processed by the {insights-operator} for OpenShift Container Platform.
If you are a cluster administrator, you can configure the {insights-operator} to obfuscate data from the Deployment Validation Operator (DVO).
For example, you can obfuscate workload names in the archive file that is then sent to Red{nbsp}Hat.

To obfuscate the name of resources, you must manually set the `obfuscation` attribute in the `insights-config` `ConfigMap` object to include the `workload_names` value, as outlined in the following procedure.

.Prerequisites

* Remote health reporting is enabled, which is the default.
* You are logged in to the OpenShift Container Platform web console with the "cluster-admin" role.
* The *insights-config* `ConfigMap` object exists in the `openshift-insights` namespace.
* The cluster is self managed and the Deployment Validation Operator is installed.

.Procedure

. Go to *Workloads* -> *ConfigMaps* and select *Project: openshift-insights*.
. Click the `insights-config` `ConfigMap` object to open it.
. Click *Actions* and select *Edit ConfigMap*.
. Click the *YAML view* radio button.
. In the file, set the `obfuscation` attribute with the `workload_names` value.
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
# ...
data:
  config.yaml: |
    dataReporting:
      obfuscation:
        - workload_names
# ...
----

. Click *Save*. The *insights-config* config-map details page opens.
. Verify that the value of the `config.yaml` `obfuscation` attribute is set to `- workload_names`.
