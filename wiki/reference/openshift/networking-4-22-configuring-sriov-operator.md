---
title: "Configuring the SR-IOV Network Operator"
type: reference
domain: openshift
slug: networking-4-22-configuring-sriov-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-sriov-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring the SR-IOV Network Operator

[id="configuring-sriov-operator"]
= Configuring the SR-IOV Network Operator

[role="_abstract"]
To manage SR-IOV network devices and network attachments in your cluster, use the Single Root I/O Virtualization (SR-IOV) Network Operator.

// Configuring the SR-IOV Network Operator
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="nw-sriov-configuring-operator_{context}"]
= Configuring the SR-IOV Network Operator

[role="_abstract"]
To manage SR-IOV network devices and network attachments in your cluster, configure the Single Root I/O Virtualization (SR-IOV) Network Operator.

.Procedure

. Create a `SriovOperatorConfig` custom resource (CR). The following example creates a file named `sriovOperatorConfig.yaml`:
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  disableDrain: false
  enableInjector: true
  enableOperatorWebhook: true
  logLevel: 2
  featureGates:
    metricsExporter: false
# ...
----
+
where:

`metadata.name`:: Specifies the name of the SR-IOV Network Operator instance. The only valid name for the `SriovOperatorConfig` resource is `default` and the name must be in the namespace where the Operator is deployed.

`spec.enableInjector`:: Specifies if any `network-resources-injector` pod can run in the namespace. If not specified in the CR or explicitly set to `true`, defaults to `false` or `<none>`, preventing any `network-resources-injector` pod from running in the namespace. The recommended setting is `true`.

`spec.enableOperatorWebhook`:: Specifies if any `operator-webhook` pods can run in the namespace. The `enableOperatorWebhook` field, if not specified in the CR or explicitly set to true, defaults to `false` or `<none>`, preventing any `operator-webhook` pod from running in the namespace. The recommended setting is `true`.

. Apply the resource to your cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f sriovOperatorConfig.yaml
----

// SR-IOV Network Operator config custom resource
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="nw-sriov-operator-cr_{context}"]
= SR-IOV Network Operator config custom resource

[role="_abstract"]
To customize the SR-IOV Network Operator, configure the `sriovoperatorconfig` custom resource.

The following table describes the `sriovoperatorconfig` CR fields:

.SR-IOV Network Operator config custom resource
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|Specifies the name of the SR-IOV Network Operator instance. The default value is `default`. Do not set a different value.

|`metadata.namespace`
|`string`
|Specifies the namespace of the SR-IOV Network Operator instance. The default value is `openshift-sriov-network-operator`. Do not set a different value.

|`spec.configDaemonNodeSelector`
|`string`
|Specifies the node selection to control scheduling the SR-IOV Network Config Daemon on selected nodes. By default, this field is not set and the Operator deploys the SR-IOV Network Config daemon set on compute nodes.

|`spec.disableDrain`
|`boolean`
|Specifies whether to disable the node draining process or enable the node draining process when you apply a new policy to configure the NIC on a node. Setting this field to `true` facilitates software development and installing OpenShift Container Platform on a single node. By default, this field is not set. For single-node clusters, set this field to `true` after installing the Operator. This field must remain set to `true`.

|`spec.enableInjector`
|`boolean`
|Specifies whether to enable or disable the Network Resources Injector daemon set.

|`spec.enableOperatorWebhook`
|`boolean`
|Specifies whether to enable or disable the Operator Admission Controller webhook daemon set.

|`spec.logLevel`
|`integer`
|Specifies the log verbosity level of the Operator. By default, this field is set to `0`, which shows only basic logs. Set to `2` to show all the available logs.

|`spec.featureGates`
|`map[string]bool`
|Specifies whether to enable or disable the optional features. For example, `metricsExporter`.

|`spec.featureGates.metricsExporter`
|`boolean`
|Specifies whether to enable or disable the SR-IOV Network Operator metrics. By default, this field is set to `false`.

|`spec.featureGates.mellanoxFirmwareReset`
|`boolean`
|Specifies whether to reset the firmware on virtual function (VF) changes in the SR-IOV Network Operator. Some chipsets, such as the Intel C740 Series, do not completely power off the PCI-E devices, which is required to configure VFs on NVIDIA/Mellanox NICs. By default, this field is set to `false`.

|====

// About the Network Resources Injector
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="about-network-resource-injector_{context}"]
= About the Network Resources Injector

[role="_abstract"]
You can use the Network Resources Injector, a Kubernetes Dynamic Admission Controller application, to mutate resource requests and limits in a pod specification and mutate a pod specification with a Downward API volume.

The Network Resources Injector provides the following capabilities:

* Mutation of resource requests and limits in a pod specification to add an SR-IOV resource name according to an SR-IOV network attachment definition annotation.
* Mutation of a pod specification with a Downward API volume to expose pod annotations, labels, and huge pages requests and limits. Containers that run in the pod can access the exposed information as files under the `/etc/podnetinfo` path.

The SR-IOV Network Operator enables the Network Resources Injector when the `enableInjector` is set to `true` in the `SriovOperatorConfig` CR. The `network-resources-injector` pod runs as a daemon set on all control plane nodes. The following is an example of Network Resources Injector pods running in a cluster with three control plane nodes:

[source,terminal]
----
$ oc get pods -n openshift-sriov-network-operator
----

.Example output
[source,terminal]
----
NAME                                      READY   STATUS    RESTARTS   AGE
network-resources-injector-5cz5p          1/1     Running   0          10m
network-resources-injector-dwqpx          1/1     Running   0          10m
network-resources-injector-lktz5          1/1     Running   0          10m
----

By default, the `failurePolicy` field in the Network Resources Injector webhook is set to `Ignore`. This default setting prevents pod creation from being blocked if the webhook is unavailable.

If you set the `failurePolicy` field to `Fail`, and the Network Resources Injector webhook is unavailable, the webhook attempts to mutate all pod creation and update requests. This behavior can block pod creation and disrupt normal cluster operations. To prevent such issues, you can enable the `featureGates.resourceInjectorMatchCondition` feature in the `SriovOperatorConfig` object to limit the scope of the Network Resources Injector webhook. If this feature is enabled, the webhook applies only to pods with the secondary network annotation `k8s.v1.cni.cncf.io/networks`.

If you set the `failurePolicy` field to `Fail` after enabling the `resourceInjectorMatchCondition` feature, the webhook applies only to pods with the secondary network annotation `k8s.v1.cni.cncf.io/networks`. If the webhook is unavailable, the cluster still deploys pods without this annotation; this prevents unnecessary disruptions to cluster operations.

The `featureGates.resourceInjectorMatchCondition` feature is disabled by default. To enable this feature, set the `featureGates.resourceInjectorMatchCondition` field to `true` in the `SriovOperatorConfig` object.

.Example `SriovOperatorConfig` object configuration
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: sriov-network-operator
spec:
# ...
  featureGates:
    resourceInjectorMatchCondition: true
# ...
----

// Disabling or enabling the Network Resources Injector
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="disable-enable-network-resource-injector_{context}"]
= Disabling or enabling the Network Resources Injector

[role="_abstract"]
To control the automatic configuration of your cluster workloads, enable or disable the Network Resources Injector.

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.
* You must have installed the SR-IOV Network Operator.

.Procedure

* Set the `enableInjector` field. Replace `<value>` with `false` to disable the feature or `true` to enable the feature.
+
[source,terminal]
----
$ oc patch sriovoperatorconfig default \
  --type=merge -n openshift-sriov-network-operator \
  --patch '{ "spec": { "enableInjector": <value> } }'
----
+
[TIP]
====
You can alternatively apply the following YAML to update the Operator:

[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  enableInjector: <value>
# ...
----
====

// About the SR-IOV Network Operator admission controller webhook
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="about-sr-iov-operator-admission-control-webhook_{context}"]
= About the SR-IOV Network Operator admission controller webhook

[role="_abstract"]
You can use the SR-IOV Network Operator Admission Controller webhook to mutate or validate the `SriovNetworkNodePolicy` CR.

* Validation of the `SriovNetworkNodePolicy` CR when it is created or updated.
* Mutation of the `SriovNetworkNodePolicy` CR by setting the default value for the `priority` and `deviceType` fields when the CR is created or updated.

The SR-IOV Network Operator Admission Controller webhook is enabled by the Operator when the `enableOperatorWebhook` is set to `true` in the `SriovOperatorConfig` CR. The `operator-webhook` pod runs as a daemon set on all control plane nodes.

[NOTE]
====
Use caution when disabling the SR-IOV Network Operator Admission Controller webhook. You can disable the webhook under specific circumstances, such as troubleshooting, or if you want to use unsupported devices. For information about configuring unsupported devices, see "Configuring the SR-IOV Network Operator to use an unsupported NIC".
====

The following is an example of the Operator Admission Controller webhook pods running in a cluster with three control plane nodes:

[source,terminal]
----
$ oc get pods -n openshift-sriov-network-operator
----

.Example output
[source,terminal]
----
NAME                                      READY   STATUS    RESTARTS   AGE
operator-webhook-9jkw6                    1/1     Running   0          16m
operator-webhook-kbr5p                    1/1     Running   0          16m
operator-webhook-rpfrl                    1/1     Running   0          16m
----

[role="_additional-resources"]
.Additional resources

* Configuring the SR-IOV Network Operator to use an unsupported NIC

// Disabling or enabling the SR-IOV Network Operator admission controller webhook
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="disable-enable-sr-iov-operator-admission-control-webhook_{context}"]
= Disabling or enabling the SR-IOV Network Operator admission controller webhook

[role="_abstract"]
To manage validation of your network configurations, enable or disable the SR-IOV Network Operator admission controller webhook.

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.
* You must have installed the SR-IOV Network Operator.

.Procedure

* Set the `enableOperatorWebhook` field. Replace `<value>` with `false` to disable the feature or `true` to enable it:
+
[source,terminal]
----
$ oc patch sriovoperatorconfig default --type=merge \
  -n openshift-sriov-network-operator \
  --patch '{ "spec": { "enableOperatorWebhook": <value> } }'
----
+
[TIP]
====
You can alternatively apply the following YAML to update the Operator:

[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  enableOperatorWebhook: <value>
# ...
----
====

//Configuring a custom NodeSelector for the SR-IOV Network Config daemon
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="configuring-custom-nodeselector_{context}"]
= Configuring a custom NodeSelector for the SR-IOV Network Config daemon

[role="_abstract"]
The SR-IOV Network Config daemon discovers and configures the SR-IOV network devices on cluster nodes. By default, the daemon is deployed to all the compute nodes in the cluster. You can use node labels to specify on which nodes the SR-IOV Network Config daemon runs.

[IMPORTANT]
=====
When you update the `configDaemonNodeSelector` field, the SR-IOV Network Config daemon is recreated on each selected node.
While the daemon is recreated, cluster users are unable to apply any new SR-IOV Network node policy or create new SR-IOV pods.
=====

.Procedure

* To update the node selector for the Operator, enter the following command:
+
[source,terminal]
----
$ oc patch sriovoperatorconfig default --type=json \
  -n openshift-sriov-network-operator \
  --patch '[{
      "op": "replace",
      "path": "/spec/configDaemonNodeSelector",
      "value": {<node_label>}
    }]'
----
+
Replace `<node_label>` with a label to apply as in the following example:
`"node-role.kubernetes.io/worker": ""`.
+
[TIP]
====
You can alternatively apply the following YAML to update the Operator:

[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  configDaemonNodeSelector:
    <node_label>
# ...
----
====

// Configuring the SR-IOV Network Operator for single node installations
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="configure-sr-iov-operator-single-node_{context}"]
= Configuring the SR-IOV Network Operator for single node installations

[role="_abstract"]
By default, the SR-IOV Network Operator drains workloads from a node before every policy change. The Operator performs this action to ensure that no workloads are using the virtual functions before the reconfiguration. As a result, you must configure the Operator to not drain workloads from the single node.

For installations on a single node, other nodes do not receive the workloads.

[IMPORTANT]
====
After performing the following procedure to disable draining workloads, you must remove any workload that uses an SR-IOV network interface before you change any SR-IOV network node policy.
====

.Prerequisites

* Install the {oc-first}.
* Log in as a user with `cluster-admin` privileges.
* You must have installed the SR-IOV Network Operator.

.Procedure

- To set the `disableDrain` field to `true` and the `configDaemonNodeSelector` field to `node-role.kubernetes.io/master: ""`, enter the following command:
+
[source,terminal]
----
$ oc patch sriovoperatorconfig default --type=merge -n openshift-sriov-network-operator --patch '{ "spec": { "disableDrain": true, "configDaemonNodeSelector": { "node-role.kubernetes.io/master": "" } } }'
----
+
[TIP]
====
You can alternatively apply the following YAML to update the Operator:

[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  disableDrain: true
  configDaemonNodeSelector:
   node-role.kubernetes.io/master: ""
# ...
----
====

// Deploying the SR-IOV Operator for HCP
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc
// * hosted-control-planes/hcp-machine-config.adoc

[id="sriov-operator-hosted-control-planes_{context}"]
= Deploying the SR-IOV Operator for {hcp}

[role="_abstract"]
After you configure and deploy your hosting service cluster, you can create a subscription to the SR-IOV Operator on a hosted cluster. The SR-IOV pod runs on worker machines rather than the control plane.

.Prerequisites

You must configure and deploy the hosted cluster on AWS.

.Procedure

. Create a namespace and an Operator group:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-sriov-network-operator
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: sriov-network-operators
  namespace: openshift-sriov-network-operator
spec:
  targetNamespaces:
  - openshift-sriov-network-operator
----

. Create a subscription to the SR-IOV Operator:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: sriov-network-operator-subsription
  namespace: openshift-sriov-network-operator
spec:
  channel: stable
  name: sriov-network-operator
  config:
    nodeSelector:
      node-role.kubernetes.io/worker: ""
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

.Verification

. To verify that the SR-IOV Operator is ready, run the following command and view the resulting output:
+
[source,terminal]
----
$ oc get csv -n openshift-sriov-network-operator
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                         DISPLAY                   VERSION               REPLACES                                     PHASE
sriov-network-operator..0-202211021237   SR-IOV Network Operator   .0-202211021237   sriov-network-operator..0-202210290517   Succeeded
----

. To verify that the SR-IOV pods are deployed, run the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-sriov-network-operator
----

// About the SR-IOV network metrics exporter
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="sriov-network-metrics-exporter_{context}"]
= About the SR-IOV network metrics exporter

[role="_abstract"]
The Single Root I/O Virtualization (SR-IOV) network metrics exporter reads the metrics for SR-IOV virtual functions (VFs) and exposes these VF metrics in Prometheus format. When the SR-IOV network metrics exporter is enabled, you can query the SR-IOV VF metrics by using the OpenShift Container Platform web console to monitor the networking activity of the SR-IOV pods.

When you query the SR-IOV VF metrics by using the web console, the SR-IOV network metrics exporter fetches and returns the VF network statistics along with the name and namespace of the pod that the VF is attached to.

The following table describes the SR-IOV VF metrics that the metrics exporter reads and exposes in Prometheus format:

.SR-IOV VF metrics
[%autowidth,options="header"]
|====
|Metric| Description |Example PromQL query to examine the VF metric

|`sriov_vf_rx_bytes` |Received bytes per virtual function. |`sriov_vf_rx_bytes * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice`
|`sriov_vf_tx_bytes` |Transmitted bytes per virtual function. |`sriov_vf_tx_bytes * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice`
|`sriov_vf_rx_packets` |Received packets per virtual function. |`sriov_vf_rx_packets * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice`
|`sriov_vf_tx_packets` |Transmitted packets per virtual function. |`sriov_vf_tx_packets * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice`
|`sriov_vf_rx_dropped` |Dropped packets upon receipt per virtual function. |`sriov_vf_rx_dropped * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice`
|`sriov_vf_tx_dropped` |Dropped packets during transmission per virtual function. |`sriov_vf_tx_dropped * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice`
|`sriov_vf_rx_multicast` |Received multicast packets per virtual function. |`sriov_vf_rx_multicast * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice`
|`sriov_vf_rx_broadcast` |Received broadcast packets per virtual function. |`sriov_vf_rx_broadcast * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice`
|`sriov_kubepoddevice` |Virtual functions linked to active pods. |-

|====

You can also combine these queries by using the `kube-state-metrics` tool to get more information about the SR-IOV pods. For example, you can use the following query to get the VF network statistics along with the application name from the standard Kubernetes pod label:

[source,terminal]
----
(sriov_vf_tx_packets * on (pciAddr,node)  group_left(pod,namespace)  sriov_kubepoddevice) * on (pod,namespace) group_left (label_app_kubernetes_io_name) kube_pod_labels
----

// Enabling the SR-IOV network metrics exporter
// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-sriov-operator.adoc

[id="sriov-operator-metrics_{context}"]
= Enabling the SR-IOV network metrics exporter

[role="_abstract"]
To enable the SR-IOV network metrics exporter, set the `spec.featureGates.metricsExporter` field to `true`. Because the exporter is disabled by default, you must explicitly enable the SR-IOV network metrics exporter.

[IMPORTANT]
====
When the metrics exporter is enabled, the SR-IOV Network Operator deploys the metrics exporter only on nodes with SR-IOV capabilities.
====

.Prerequisites

* You have installed the {oc-first}.
* You have logged in as a user with `cluster-admin` privileges.
* You have installed the SR-IOV Network Operator.

.Procedure

. Enable cluster monitoring by running the following command:
+
[source,terminal]
----
$ oc label ns/openshift-sriov-network-operator openshift.io/cluster-monitoring=true
----
+
To enable cluster monitoring, you must add the `openshift.io/cluster-monitoring=true` label in the namespace where you have installed the SR-IOV Network Operator.

. Set the `spec.featureGates.metricsExporter` field to `true` by running the following command:
+
[source,terminal]
----
$ oc patch -n openshift-sriov-network-operator sriovoperatorconfig/default \
    --type='merge' -p='{"spec": {"featureGates": {"metricsExporter": true}}}'
----

.Verification

. Check that the SR-IOV network metrics exporter is enabled by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-sriov-network-operator
----
+
.Example output
[source,terminal]
----
NAME                                     READY   STATUS    RESTARTS   AGE
operator-webhook-hzfg4                   1/1     Running   0          5d22h
sriov-network-config-daemon-tr54m        1/1     Running   0          5d22h
sriov-network-metrics-exporter-z5d7t     1/1     Running   0          10s
sriov-network-operator-cc6fd88bc-9bsmt   1/1     Running   0          5d22h
----
+
Ensure that `sriov-network-metrics-exporter` pod is in the `READY` state.

. Optional: Examine the SR-IOV virtual function (VF) metrics by using the OpenShift Container Platform web console. For more information, see "Querying metrics".

[role="_additional-resources"]
.Additional resources

* Querying metrics for all projects with the monitoring dashboard

* Querying metrics for user-defined projects as a developer

* Configuring an SR-IOV network device

* Uninstalling the SR-IOV Network Operator
