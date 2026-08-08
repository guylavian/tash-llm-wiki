---
title: "Storing and recording data for user workload monitoring"
type: reference
domain: openshift
slug: observability-4-22-storing-and-recording-data-uwm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/storing-and-recording-data-uwm
version: 4.22
family: observability
documentKind: "Documentation"
---

# Storing and recording data for user workload monitoring

[id="storing-and-recording-data-uwm"]
= Storing and recording data for user workload monitoring

Store and record your metrics and alerting data, configure logs to specify which activities are recorded, control how long Prometheus retains stored data, and set the maximum amount of disk space for the data. These actions help you protect your data and use them for troubleshooting.

// Configuring persistent storage
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="configuring-persistent-storage_{context}"]
= Configuring persistent storage

Run cluster monitoring with persistent storage to gain the following benefits:

* Protect your metrics and alerting data from data loss by storing them in a persistent volume (PV). As a result, they can survive pods being restarted or recreated.
* Avoid getting duplicate notifications and losing silences for alerts when the Alertmanager pods are restarted.

// tag::CPM[]
[IMPORTANT]
====
In multi-node clusters, you must configure persistent storage for Prometheus and Alertmanager to ensure high availability.
====
// end::CPM[]
// tag::UWM[]
[IMPORTANT]
====
In multi-node clusters, you must configure persistent storage for Prometheus, Alertmanager, and Thanos Ruler to ensure high availability.
====
// end::UWM[]

[NOTE]
====
For production environments, it is highly recommended to configure persistent storage.
====

[id="persistent-storage-prerequisites_{context}"]
== Persistent storage prerequisites

* Use the block type of storage.

* Dedicate sufficient persistent storage to ensure that the disk does not become full.

* Use `Filesystem` as the storage type value for the `volumeMode` parameter when you configure the persistent volume.
+
[IMPORTANT]
====
* Do not use a raw block volume, which is described with `volumeMode: Block` in the `PersistentVolume` resource. Prometheus cannot use raw block volumes.

* Prometheus does not support file systems that are not POSIX compliant.
For example, some NFS file system implementations are not POSIX compliant.
If you want to use an NFS file system for storage, verify with the vendor that their NFS implementation is fully POSIX compliant.
====

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="configuring-a-persistent-volume-claim_{context}"]
= Configuring a persistent volume claim

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

To use a persistent volume (PV) for monitoring components, you must configure a persistent volume claim (PVC).

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role, or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add your PVC configuration for the component under `data/config.yaml`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    <component>: # <1>
      volumeClaimTemplate:
        spec:
          storageClassName: <storage_class> # <2>
          resources:
            requests:
              storage: <amount_of_storage> # <3>
----
<1> Specify the monitoring component for which you want to configure the PVC.
<2> Specify an existing storage class. If a storage class is not specified, the default storage class is used.
<3> Specify the amount of required storage.
+
The following example configures a PVC that claims persistent storage for
// tag::CPM[]
Prometheus:
// end::CPM[]
// tag::UWM[]
Thanos Ruler:
// end::UWM[]
+
.Example PVC configuration
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      volumeClaimTemplate:
        spec:
          storageClassName: my-storage-class
          resources:
            requests:
# tag::CPM[]
              storage: 40Gi
# end::CPM[]
# tag::UWM[]
              storage: 10Gi
# end::UWM[]
----
// tag::UWM[]
+
[NOTE]
====
Storage requirements for the `thanosRuler` component depend on the number of rules that are evaluated and how many samples each rule generates.
====
// end::UWM[]

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed and the new storage configuration is applied.
+
[WARNING]
====
When you update the config map with a PVC configuration, the affected `StatefulSet` object is recreated, resulting in a temporary service outage.
====

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* Understanding persistent storage
* PersistentVolumeClaims (Kubernetes documentation)

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="resizing-a-persistent-volume_{context}"]
= Resizing a persistent volume

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

// tag::CPM[]
You can resize a persistent volume (PV) for monitoring components, such as Prometheus or Alertmanager.
// end::CPM[]
// tag::UWM[]
You can resize a persistent volume (PV) for the instances of Prometheus, Thanos Ruler, and Alertmanager.
// end::UWM[]
You need to manually expand a persistent volume claim (PVC), and then update the config map in which the component is configured.

[IMPORTANT]
====
You can only expand the size of the PVC. Shrinking the storage size is not possible.
====

.Prerequisites
// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
* You have configured at least one PVC for core OpenShift Container Platform monitoring components.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role, or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have configured at least one PVC for components that monitor user-defined projects.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Manually expand a PVC with the updated storage request. For more information, see "Expanding persistent volume claims (PVCs) with a file system" in _Expanding persistent volumes_.

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add a new storage size for the PVC configuration for the component under `data/config.yaml`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    <component>: # <1>
      volumeClaimTemplate:
        spec:
          resources:
            requests:
              storage: <amount_of_storage> # <2>
----
<1> The component for which you want to change the storage size.
<2> Specify the new size for the storage volume. It must be greater than the previous value.
+
The following example sets the new PVC request to
// tag::CPM[]
100 gigabytes for the Prometheus instance:
// end::CPM[]
// tag::UWM[]
20 gigabytes for Thanos Ruler:
// end::UWM[]
+
.Example storage configuration for `{component}`
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      volumeClaimTemplate:
        spec:
          resources:
            requests:
# tag::CPM[]
              storage: 100Gi
# end::CPM[]
# tag::UWM[]
              storage: 20Gi
# end::UWM[]
----
// tag::UWM[]
+
[NOTE]
====
Storage requirements for the `thanosRuler` component depend on the number of rules that are evaluated and how many samples each rule generates.
====
// end::UWM[]

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.
+
[WARNING]
====
When you update the config map with a new storage size, the affected `StatefulSet` object is recreated, resulting in a temporary service outage.
====

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* Prometheus database storage requirements
* Expanding persistent volume claims (PVCs) with a file system

// Modifying the retention time and size

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="modifying-retention-time-and-size-for-prometheus-metrics-data_{context}"]
= Modifying retention time and size for Prometheus metrics data

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

By default, Prometheus retains metrics data for
// tag::CPM[]
15 days for core platform monitoring.
// end::CPM[]
// tag::UWM[]
24 hours for monitoring for user-defined projects.
// end::UWM[]
You can modify the retention time for the Prometheus instance to change when the data is deleted. You can also set the maximum amount of disk space the retained metrics data uses.

[NOTE]
====
Data compaction occurs every two hours. Therefore, a persistent volume (PV) might fill up before compaction, potentially exceeding the `retentionSize` limit. In such cases, the `KubePersistentVolumeFillingUp` alert fires until the space on a PV is lower than the `retentionSize` limit.
====

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role, or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add the retention time and size configuration under `data/config.yaml`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      retention: <time_specification> # <1>
      retentionSize: <size_specification> # <2>
----
<1> The retention time: a number directly followed by `ms` (milliseconds), `s` (seconds), `m` (minutes), `h` (hours), `d` (days), `w` (weeks), or `y` (years). You can also combine time values for specific times, such as `1h30m15s`.
<2> The retention size: a number directly followed by `B` (bytes), `KB` (kilobytes), `MB` (megabytes), `GB` (gigabytes), `TB` (terabytes), `PB` (petabytes), and `EB` (exabytes).
+
The following example sets the retention time to 24 hours and the retention size to 10 gigabytes for the Prometheus instance:
+
.Example of setting retention time for Prometheus
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      retention: 24h
      retentionSize: 10GB
----

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

// Unset the source code block attributes just to be safe.

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="modifying-the-retention-time-for-thanos-ruler-metrics-data_{context}"]
= Modifying the retention time for Thanos Ruler metrics data

By default, for user-defined projects, Thanos Ruler automatically retains metrics data for 24 hours. You can modify the retention time to change how long this data is retained by specifying a time value in the `user-workload-monitoring-config` config map in the `openshift-user-workload-monitoring` namespace.

[NOTE]
====
If you configure retention for user-workload Prometheus, Thanos Ruler automatically inherits the same retention time, unless explicitly configured otherwise.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
* You have installed the {oc-first}.

.Procedure

. Edit the `user-workload-monitoring-config` `ConfigMap` object in the `openshift-user-workload-monitoring` project:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring edit configmap user-workload-monitoring-config
----

. Add the retention time configuration under `data/config.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-workload-monitoring-config
  namespace: openshift-user-workload-monitoring
data:
  config.yaml: |
    thanosRuler:
      retention: <time_specification> <1>
----
+
<1> Specify the retention time in the following format: a number directly followed by `ms` (milliseconds), `s` (seconds), `m` (minutes), `h` (hours), `d` (days), `w` (weeks), or `y` (years).
You can also combine time values for specific times, such as `1h30m15s`.
The default is `24h`.
+
The following example sets the retention time to 10 days for Thanos Ruler data:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-workload-monitoring-config
  namespace: openshift-user-workload-monitoring
data:
  config.yaml: |
    thanosRuler:
      retention: 10d
----

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

[role="_additional-resources"]
.Additional resources

* Retention time and size for Prometheus metrics
* Understanding persistent storage
* Enabling monitoring for user-defined projects
* Prometheus database storage requirements
* Recommended configurable storage technology
* Optimizing storage

// Setting log levels for monitoring components
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="setting-log-levels-for-monitoring-components_{context}"]
= Setting log levels for monitoring components

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

// tag::CPM[]
You can configure the log level for Alertmanager, Prometheus Operator, Prometheus, and {component-name} and log verbosity for Metrics Server.
// end::CPM[]
// tag::UWM[]
You can configure the log level for Alertmanager, Prometheus Operator, Prometheus, and {component-name}.
// end::UWM[]
You can use these settings for troubleshooting and to gain better insight into how the components are functioning.

The following log levels can be applied to the relevant component in the `{configmap-name}` `ConfigMap` object:

* `debug`. Log debug, informational, warning, and error messages.
* `info` (default). Log informational, warning, and error messages.
* `warn`. Log warning and error messages only.
* `error`. Log error messages only.

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.

* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add log configuration for a component under `data/config.yaml`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    <component>: # <1>
      logLevel: <log_level> # <2>
# tag::CPM[]
    metricsServer:
      verbosity: <value> # <3>
# end::CPM[]
    # ...
----
<1> Specify the monitoring stack component for which you are setting a log level.
Available component values are `{prometheus}`, `{alertmanager}`, `prometheusOperator`, and `{thanos}`.
<2> Specify the log level for the component.
The available values are `error`, `warn`, `info`, and `debug`.
The default value is `info`.
// tag::CPM[]
<3> Specify the verbosity for Metrics Server.
Valid values are positive integers.
Increasing the number increases the amount of logged events, values over `10` are usually unnecessary.
The default value is `0`.
// end::CPM[]

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

. Verify that the log configuration is applied by reviewing the deployment or pod configuration in the related project.

** The following example checks the log level for the `prometheus-operator` deployment:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} get deploy prometheus-operator -o yaml | grep "log-level"
----
+
.Example output
[source,terminal]
----
        - --log-level=debug
----

// tag::CPM[]
** The following example checks the log verbosity for the `metrics-server` deployment:
+
[source,terminal]
----
$ oc -n openshift-monitoring get deploy metrics-server -o yaml | grep -- '--v='
----
+
.Example output
[source,terminal]
----
        - --v=3
----
// end::CPM[]

. Verify that the pods for the component are running:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} get pods
----
+
[NOTE]
====
If an unrecognized `logLevel` value is included in the `ConfigMap` object, the pods for the component might not restart successfully.
====

// Unset the source code block attributes just to be safe.

// Enabling the query log file for Prometheus
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="setting-query-log-file-for-prometheus_{context}"]
= Enabling the query log file for Prometheus

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

You can configure Prometheus to write all queries that have been run by the engine to a log file.

[IMPORTANT]
====
Because log rotation is not supported, only enable this feature temporarily when you need to troubleshoot an issue. After you finish troubleshooting, disable query logging by reverting the changes you made to the `ConfigMap` object to enable the feature.
====

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.

* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add the `queryLogFile` parameter for Prometheus under `data/config.yaml`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      queryLogFile: <path> # <1>
----
<1> Add the full path to the file in which queries will be logged.

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

. Verify that the pods for the component are running. The following sample command lists the status of pods:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} get pods
----
+
// tag::CPM[]
.Example output
[source,terminal]
----
...
prometheus-operator-567c9bc75c-96wkj   2/2     Running   0          62m
prometheus-k8s-0                       6/6     Running   1          57m
prometheus-k8s-1                       6/6     Running   1          57m
thanos-querier-56c76d7df4-2xkpc        6/6     Running   0          57m
thanos-querier-56c76d7df4-j5p29        6/6     Running   0          57m
...
----
// end::CPM[]
// tag::UWM[]
.Example output
[source,terminal]
----
...
prometheus-operator-776fcbbd56-2nbfm   2/2     Running   0          132m
prometheus-user-workload-0             5/5     Running   1          132m
prometheus-user-workload-1             5/5     Running   1          132m
thanos-ruler-user-workload-0           3/3     Running   0          132m
thanos-ruler-user-workload-1           3/3     Running   0          132m
...
----
// end::UWM[]

. Read the query log:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} exec {pod} -- cat <path>
----
+
[IMPORTANT]
====
Revert the setting in the config map after you have examined the logged query information.
====

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* Enabling monitoring for user-defined projects
