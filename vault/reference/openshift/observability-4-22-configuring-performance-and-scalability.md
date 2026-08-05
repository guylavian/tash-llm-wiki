---
title: "Configuring performance and scalability for core platform monitoring"
type: reference
domain: openshift
slug: observability-4-22-configuring-performance-and-scalability
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/configuring-performance-and-scalability
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring performance and scalability for core platform monitoring

[id="configuring-performance-and-scalability"]
= Configuring performance and scalability for core platform monitoring

You can configure the monitoring stack to optimize the performance and scale of your clusters. The following documentation provides information about how to distribute the monitoring components and control the impact of the monitoring stack on CPU and memory resources.

[role="_additional-resources"]
.Additional resources

* About performance and scalability

[id="controlling-placement-and-distribution-of-monitoing-components_{context}"]
== Controlling the placement and distribution of monitoring components

You can move the monitoring stack components to specific nodes:

* Use the `nodeSelector` constraint with labeled nodes to move any of the monitoring stack components to specific nodes.
* Assign tolerations to enable moving components to tainted nodes.

By doing so, you control the placement and distribution of the monitoring components across a cluster.

By controlling placement and distribution of monitoring components, you can optimize system resource use, improve performance, and separate workloads based on specific requirements or policies.

[role="_additional-resources"]
.Additional resources

* Using node selectors to move monitoring components

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="moving-monitoring-components-to-different-nodes_{context}"]
= Moving monitoring components to different nodes

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples.
// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

// tag::CPM[]
To specify the nodes in your cluster on which monitoring stack components will run, configure the `nodeSelector` constraint for the components in the `cluster-monitoring-config` config map to match labels assigned to the nodes.

[NOTE]
====
You cannot add a node selector constraint directly to an existing scheduled pod.
====
// end::CPM[]

// tag::UWM[]
You can move any of the components that monitor workloads for user-defined projects to specific worker nodes.

[WARNING]
====
It is not permitted to move components to control plane or infrastructure nodes.
====
// end::UWM[]

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
* You have installed the {oc-first}.
// end::CPM[]

// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
* You have installed the {oc-first}.
// end::UWM[]

.Procedure

. If you have not done so yet, add a label to the nodes on which you want to run the monitoring components:
+
[source,terminal]
----
$ oc label nodes <node_name> <node_label> <1>
----
<1> Replace `<node_name>` with the name of the node where you want to add the label.
Replace `<node_label>` with the name of the wanted label.

. Edit the `{configmap-name}` `ConfigMap` object in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Specify the node labels for the `nodeSelector` constraint for the component under `data/config.yaml`:
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
    # ...
    <component>: #<1>
      nodeSelector:
        <node_label_1> #<2>
        <node_label_2> #<3>
    # ...
----
<1> Substitute `<component>` with the appropriate monitoring stack component name.
<2> Substitute `<node_label_1>` with the label you added to the node.
<3> Optional: Specify additional labels.
If you specify additional labels, the pods for the component are only scheduled on the nodes that contain all of the specified labels.
+
[NOTE]
====
If monitoring components remain in a `Pending` state after configuring the `nodeSelector` constraint, check the pod events for errors relating to taints and tolerations.
====

. Save the file to apply the changes. The components specified in the new configuration are automatically moved to the new nodes, and the pods affected by the new configuration are redeployed.

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* Preparing to configure core platform monitoring stack
* Understanding how to update labels on nodes
* Placing pods on specific nodes using node selectors
* `nodeSelector` (Kubernetes documentation)

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="assigning-tolerations-to-monitoring-components_{context}"]
= Assigning tolerations to monitoring components

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples.
// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

// tag::CPM[]
You can assign tolerations to any of the monitoring stack components to enable moving them to tainted nodes.
// end::CPM[]

// tag::UWM[]
You can assign tolerations to the components that monitor user-defined projects, to enable moving them to tainted worker nodes. Scheduling is not permitted on control plane or infrastructure nodes.
// end::UWM[]

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]

// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role, or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists in the `openshift-user-workload-monitoring` namespace. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Specify `tolerations` for the component:
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
    <component>:
      tolerations:
        <toleration_specification>
----
+
Substitute `<component>` and `<toleration_specification>` accordingly.
+
For example, `oc adm taint nodes node1 key1=value1:NoSchedule` adds a taint to `node1` with the key `key1` and the value `value1`. This prevents monitoring components from deploying pods on `node1` unless a toleration is configured for that taint. The following example configures the `{component}` component to tolerate the example taint:
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
      tolerations:
      - key: "key1"
        operator: "Equal"
        value: "value1"
        effect: "NoSchedule"
----

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* Preparing to configure core platform monitoring stack
* Controlling pod placement using node taints
* Taints and tolerations (Kubernetes documentation)

// Setting the body size limit for metrics scraping
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="setting-the-body-size-limit-for-metrics-scraping_{context}"]
= Setting the body size limit for metrics scraping

By default, no limit exists for the uncompressed body size for data returned from scraped metrics targets.
You can set a body size limit to help avoid situations in which Prometheus consumes excessive amounts of memory when scraped targets return a response that contains a large amount of data.
In addition, by setting a body size limit, you can reduce the impact that a malicious target might have on Prometheus and on the cluster as a whole.

After you set a value for `enforcedBodySizeLimit`, the alert `PrometheusScrapeBodySizeLimitHit` fires when at least one Prometheus scrape target replies with a response body larger than the configured value.

[NOTE]
====
If metrics data scraped from a target has an uncompressed body size exceeding the configured size limit, the scrape fails.
Prometheus then considers this target to be down and sets its `up` metric value to `0`, which can trigger the `TargetDown` alert.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have installed the {oc-first}.

.Procedure

. Edit the `cluster-monitoring-config` `ConfigMap` object in the `openshift-monitoring` namespace:
+
[source,terminal]
----
$ oc -n openshift-monitoring edit configmap cluster-monitoring-config
----

. Add a value for `enforcedBodySizeLimit` to `data/config.yaml/prometheusK8s` to limit the body size that can be accepted per target scrape:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |-
    prometheusK8s:
      enforcedBodySizeLimit: 40MB <1>
----
<1> Specify the maximum body size for scraped metrics targets.
This `enforcedBodySizeLimit` example limits the uncompressed size per target scrape to 40 megabytes.
Valid numeric values use the Prometheus data size format: B (bytes), KB (kilobytes), MB (megabytes), GB (gigabytes), TB (terabytes), PB (petabytes), and EB (exabytes).
The default value is `0`, which specifies no limit.
You can also set the value to `automatic` to calculate the limit automatically based on cluster capacity.

. Save the file to apply the changes. The new configuration is applied automatically.

[role="_additional-resources"]
.Additional resources

* `scrape_config` (Prometheus documentation)

[id="managing-cpu-and-memory-resources-for-monitoring-components_{context}"]
== Managing CPU and memory resources for monitoring components

You can ensure that the containers that run monitoring components have enough CPU and memory resources by specifying values for resource limits and requests for those components.

You can configure these limits and requests for core platform monitoring components in the `openshift-monitoring` namespace.

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="specifying-limits-and-resource-requests-for-monitoring-components_{context}"]
= Specifying limits and requests

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples.
// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

To configure CPU and memory resources, specify values for resource limits and requests in the `{configmap-name}` `ConfigMap` object in the `{namespace-name}` namespace.

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `ConfigMap` object named `cluster-monitoring-config`.
// end::CPM[]

// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role, or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add values to define resource limits and requests for each component you want to configure.
+
[IMPORTANT]
====
Ensure that the value set for a limit is always higher than the value set for a request.
Otherwise, an error will occur, and the container will not run.
====
+
.Example of setting resource limits and requests
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
    {alertmanager}:
      resources:
        limits:
          cpu: 500m
          memory: 1Gi
        requests:
          cpu: 200m
          memory: 500Mi
    {prometheus}:
      resources:
        limits:
          cpu: 500m
          memory: 3Gi
        requests:
          cpu: 200m
          memory: 500Mi
    {thanos}:
      resources:
        limits:
          cpu: 500m
          memory: 1Gi
        requests:
          cpu: 200m
          memory: 500Mi
# tag::CPM[]
    prometheusOperator:
      resources:
        limits:
          cpu: 500m
          memory: 1Gi
        requests:
          cpu: 200m
          memory: 500Mi
    metricsServer:
      resources:
        requests:
          cpu: 10m
          memory: 50Mi
        limits:
          cpu: 50m
          memory: 500Mi
    kubeStateMetrics:
      resources:
        limits:
          cpu: 500m
          memory: 1Gi
        requests:
          cpu: 200m
          memory: 500Mi
    telemeterClient:
      resources:
        limits:
          cpu: 500m
          memory: 1Gi
        requests:
          cpu: 200m
          memory: 500Mi
    openshiftStateMetrics:
      resources:
        limits:
          cpu: 500m
          memory: 1Gi
        requests:
          cpu: 200m
          memory: 500Mi
    nodeExporter:
      resources:
        limits:
          cpu: 50m
          memory: 150Mi
        requests:
          cpu: 20m
          memory: 50Mi
    monitoringPlugin:
      resources:
        limits:
          cpu: 500m
          memory: 1Gi
        requests:
          cpu: 200m
          memory: 500Mi
    prometheusOperatorAdmissionWebhook:
      resources:
        limits:
          cpu: 50m
          memory: 100Mi
        requests:
          cpu: 20m
          memory: 50Mi
# end::CPM[]
----

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* About specifying limits and requests
* Requests and limits (Kubernetes documentation)

// Choosing a metrics collection profile
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="choosing-a-metrics-collection-profile_{context}"]
= Choosing a metrics collection profile

To choose a metrics collection profile for core OpenShift Container Platform monitoring components, edit the `cluster-monitoring-config` `ConfigMap` object.

.Prerequisites

* You have installed the {oc-first}.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
* You have access to the cluster as a user with the `cluster-admin` cluster role.

.Procedure

. Edit the `cluster-monitoring-config` `ConfigMap` object in the `openshift-monitoring` project:
+
[source,terminal]
----
$ oc -n openshift-monitoring edit configmap cluster-monitoring-config
----

. Add the metrics collection profile setting under `data/config.yaml/prometheusK8s`:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |
    prometheusK8s:
      collectionProfile: <metrics_collection_profile_name> <1>
----
+
<1> The name of the metrics collection profile.
The available values are `full` or `minimal`.
If you do not specify a value or if the `collectionProfile` key name does not exist in the config map, the default setting of `full` is used.
+
The following example sets the metrics collection profile to `minimal` for the core platform instance of Prometheus:
+
[source,yaml,subs=quotes]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |
    prometheusK8s:
      collectionProfile: *minimal*
----

. Save the file to apply the changes. The new configuration is applied automatically.

[role="_additional-resources"]
.Additional resources

* About metrics collection profiles
* Viewing a list of available metrics
* Enabling features using feature gates

//Configuring pod topology spread constraints for core platform monitoring
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="configuring-pod-topology-spread-constraints_{context}"]
= Configuring pod topology spread constraints

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

You can configure pod topology spread constraints for
// tag::CPM[]
all the pods deployed by the {cmo-full}
// end::CPM[]
// tag::UWM[]
all the pods for user-defined monitoring
// end::UWM[]
to control how pod replicas are scheduled to nodes across zones.
This ensures that the pods are highly available and run more efficiently, because workloads are spread across nodes in different data centers or hierarchical infrastructure zones.

You can configure pod topology spread constraints for monitoring pods by using the `{configmap-name}` config map.

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

. Add the following settings under the `data/config.yaml` field to configure pod topology spread constraints:
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
      topologySpreadConstraints:
      - maxSkew: <n> # <2>
        topologyKey: <key> # <3>
        whenUnsatisfiable: <value> # <4>
        labelSelector: # <5>
          <match_option>
----
<1> Specify a name of the component for which you want to set up pod topology spread constraints.
<2> Specify a numeric value for `maxSkew`, which defines the degree to which pods are allowed to be unevenly distributed.
<3> Specify a key of node labels for `topologyKey`.
Nodes that have a label with this key and identical values are considered to be in the same topology.
The scheduler tries to put a balanced number of pods into each domain.
<4> Specify a value for `whenUnsatisfiable`.
Available options are `DoNotSchedule` and `ScheduleAnyway`.
Specify `DoNotSchedule` if you want the `maxSkew` value to define the maximum difference allowed between the number of matching pods in the target topology and the global minimum.
Specify `ScheduleAnyway` if you want the scheduler to still schedule the pod but to give higher priority to nodes that might reduce the skew.
<5> Specify `labelSelector` to find matching pods.
Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.
+
.Example configuration for {component-name}
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
      topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: monitoring
# tag::CPM[]
        whenUnsatisfiable: DoNotSchedule
# end::CPM[]
# tag::UWM[]
        whenUnsatisfiable: ScheduleAnyway
# end::UWM[]
        labelSelector:
          matchLabels:
            app.kubernetes.io/name: {label}
----

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* About pod topology spread constraints for monitoring
* Controlling pod placement by using pod topology spread constraints
* Pod topology spread constraints (Kubernetes documentation)
