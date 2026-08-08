---
title: "Configuring performance and scalability for user workload monitoring"
type: reference
domain: openshift
slug: observability-4-22-configuring-performance-and-scalability-uwm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/configuring-performance-and-scalability-uwm
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring performance and scalability for user workload monitoring

[id="configuring-performance-and-scalability-uwm"]
= Configuring performance and scalability for user workload monitoring

You can configure the monitoring stack to optimize the performance and scale of your clusters. The following documentation provides information about how to distribute the monitoring components and control the impact of the monitoring stack on CPU and memory resources.

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
// The nodes topics may apply to OSD/ROSA when that content is ported from OCP.
* Enabling monitoring for user-defined projects
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

* Enabling monitoring for user-defined projects
* Controlling pod placement using node taints
* Taints and tolerations (Kubernetes documentation)

[id="managing-cpu-and-memory-resources-for-monitoring-components_{context}"]
== Managing CPU and memory resources for monitoring components

You can ensure that the containers that run monitoring components have enough CPU and memory resources by specifying values for resource limits and requests for those components.

You can configure these limits and requests for monitoring components that monitor user-defined projects in the `openshift-user-workload-monitoring` namespace.

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
* About specifying limits and requests for monitoring components
* Requests and limits (Kubernetes documentation)

[id="controlling-the-impact-of-unbound-attributes-in-user-defined-projects_{context}"]
== Controlling the impact of unbound metrics attributes in user-defined projects

Cluster administrators
A `dedicated-admin`
can use the following measures to control the impact of unbound metrics attributes in user-defined projects:

* Limit the number of samples that can be accepted per target scrape in user-defined projects
* Limit the number of scraped labels, the length of label names, and the length of label values
* Configure the intervals between consecutive scrapes and between Prometheus rule evaluations
* Create alerts that fire when a scrape sample threshold is reached or when the target cannot be scraped

[NOTE]
====
Limiting scrape samples can help prevent the issues caused by adding many unbound attributes to labels. Developers can also prevent the underlying cause by limiting the number of unbound attributes that they define for metrics. Using attributes that are bound to a limited set of possible values reduces the number of potential key-value pair combinations.
====

[role="_additional-resources"]
.Additional resources

* Controlling the impact of unbound metrics attributes in user-defined projects
* Enabling monitoring for user-defined projects
* Determining why Prometheus is consuming a lot of disk space

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="setting-scrape-and-evaluation-intervals-limits-for-user-defined-projects_{context}"]
= Setting scrape intervals, evaluation intervals, and enforced limits for user-defined projects

You can set the following scrape and label limits for user-defined projects:

* Limit the number of samples that can be accepted per target scrape
* Limit the number of scraped labels
* Limit the length of label names and label values

You can also set an interval between consecutive scrapes and between Prometheus rule evaluations.

[WARNING]
====
If you set sample or label limits, no further sample data is ingested for that target scrape after the limit is reached.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role, or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
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

. Add the enforced limit and time interval configurations to `data/config.yaml`:
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
    prometheus:
      enforcedSampleLimit: 50000 # <1>
      enforcedLabelLimit: 500 # <2>
      enforcedLabelNameLengthLimit: 50 # <3>
      enforcedLabelValueLengthLimit: 600 # <4>
      scrapeInterval: 1m30s # <5>
      evaluationInterval: 1m15s # <6>
----
<1> A value is required if this parameter is specified. This `enforcedSampleLimit` example limits the number of samples that can be accepted per target scrape in user-defined projects to 50,000.
<2> Specifies the maximum number of labels per scrape.
The default value is `0`, which specifies no limit.
<3> Specifies the maximum character length for a label name.
The default value is `0`, which specifies no limit.
<4> Specifies the maximum character length for a label value.
The default value is `0`, which specifies no limit.
<5> Specifies the interval between consecutive scrapes. The interval must be set between 5 seconds and 5 minutes.
The default value is `30s`.
<6> Specifies the interval between Prometheus rule evaluations. The interval must be set between 5 seconds and 5 minutes.
The default value for Prometheus is `30s`.
+
[NOTE]
====
You can also configure the `evaluationInterval` property for Thanos Ruler through the `data/config.yaml/thanosRuler` field. The default value for Thanos Ruler is `15s`.
====

. Save the file to apply the changes. The limits are applied automatically.

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="creating-scrape-sample-alerts_{context}"]
= Creating scrape sample alerts

You can create alerts that notify you when:

* The target cannot be scraped or is not available for the specified `for` duration
* A scrape sample threshold is reached or is exceeded for the specified `for` duration

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role, or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have limited the number of samples that can be accepted per target scrape in user-defined projects, by using `enforcedSampleLimit`.
* You have installed the {oc-first}.

.Procedure

. Create a YAML file with alerts that inform you when the targets are down and when the enforced sample limit is approaching. The file in this example is called `monitoring-stack-alerts.yaml`:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    prometheus: k8s
    role: alert-rules
  name: monitoring-stack-alerts #<1>
  namespace: ns1 #<2>
spec:
  groups:
  - name: general.rules
    rules:
    - alert: TargetDown #<3>
      annotations:
        message: '{{ printf "%.4g" $value }}% of the {{ $labels.job }}/{{ $labels.service
          }} targets in {{ $labels.namespace }} namespace are down.' #<4>
      expr: 100 * (count(up == 0) BY (job, namespace, service) / count(up) BY (job,
        namespace, service)) > 10
      for: 10m #<5>
      labels:
        severity: warning #<6>
    - alert: ApproachingEnforcedSamplesLimit #<7>
      annotations:
        message: '{{ $labels.container }} container of the {{ $labels.pod }} pod in the {{ $labels.namespace }} namespace consumes {{ $value | humanizePercentage }} of the samples limit budget.' #<8>
      expr: (scrape_samples_post_metric_relabeling / (scrape_sample_limit > 0)) > 0.9 #<9>
      for: 10m #<10>
      labels:
        severity: warning #<11>
----
<1> Defines the name of the alerting rule.
<2> Specifies the user-defined project where the alerting rule is deployed.
<3> The `TargetDown` alert fires if the target cannot be scraped and is not available for the `for` duration.
<4> The message that is displayed when the `TargetDown` alert fires.
<5> The conditions for the `TargetDown` alert must be true for this duration before the alert is fired.
<6> Defines the severity for the `TargetDown` alert.
<7> The `ApproachingEnforcedSamplesLimit` alert fires when the defined scrape sample threshold is exceeded and lasts for the specified `for` duration.
<8> The message that is displayed when the `ApproachingEnforcedSamplesLimit` alert fires.
<9> The threshold for the `ApproachingEnforcedSamplesLimit` alert. In this example, the alert fires when the number of ingested samples exceeds 90% of the configured limit.
<10> The conditions for the `ApproachingEnforcedSamplesLimit` alert must be true for this duration before the alert is fired.
<11> Defines the severity for the `ApproachingEnforcedSamplesLimit` alert.

. Apply the configuration to the user-defined project:
+
[source,terminal]
----
$ oc apply -f monitoring-stack-alerts.yaml
----

. Additionally, you can check if a target has hit the configured limit:

.. In the OpenShift Container Platform web console, go to *Observe* -> *Targets* and select an endpoint with a `Down` status that you want to check.
+
The *Scrape failed: sample limit exceeded* message is displayed if the endpoint failed because of an exceeded sample limit.

//Configuring pod topology spread constraints for monitoring of user-defined projects
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
