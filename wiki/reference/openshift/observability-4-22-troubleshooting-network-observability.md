---
title: "Troubleshooting network observability"
type: reference
domain: openshift
slug: observability-4-22-troubleshooting-network-observability
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/troubleshooting-network-observability
version: 4.22
family: observability
documentKind: "Documentation"
---

# Troubleshooting network observability

[id="installing-troubleshooting"]
= Troubleshooting network observability

[role="_abstract"]
Perform diagnostic actions to troubleshoot common issues related to the Network Observability Operator and its components.

// Module included in the following assemblies:
//
// * networking/network_observability/troubleshooting-network-observability.adoc

[id="network-observability-must-gather_{context}"]
= Using the must-gather tool

[role="_abstract"]
Use the must-gather tool to collect diagnostic information about Network Observability Operator resources, including pod logs and configuration details, to assist in troubleshooting cluster issues.

.Procedure
. Navigate to the directory where you want to store the must-gather data.
. Run the following command to collect cluster-wide must-gather resources:
+
[source,terminal]
----
$ oc adm must-gather
 --image-stream=openshift/must-gather \
 --image=quay.io/netobserv/must-gather
----

// Module included in the following assemblies:
//
// * networking/network_observability/troubleshooting-network-observability.adoc

[id="configure-network-traffic-console_{context}"]
= Configuring network traffic menu entry in the OpenShift Container Platform console

[role="_abstract"]
Restore a missing network traffic menu entry in the *Observe* menu of the OpenShift Container Platform console by manually registering the console plugin in the `FlowCollector` resource and the console operator configuration.

.Prerequisites

* You have installed OpenShift Container Platform version 4.10 or newer.

.Procedure

. Check if the `spec.consolePlugin.register` field is set to `true` by running the following command:
+
[source,terminal]
----
$ oc -n netobserv get flowcollector cluster -o yaml
----
+
.Example output
----
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollector
metadata:
  name: cluster
spec:
  consolePlugin:
    register: false
----

. Optional: Add the `netobserv-plugin` plugin by manually editing the Console Operator config:
+
[source,terminal]
----
$ oc edit console.operator.openshift.io cluster
----
+
.Example output
----
...
spec:
  plugins:
  - netobserv-plugin
...
----

. Optional: Set the `spec.consolePlugin.register` field to `true` by running the following command:
+
[source,terminal]
----
$ oc -n netobserv edit flowcollector cluster -o yaml
----
+
.Example output
----
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollector
metadata:
  name: cluster
spec:
  consolePlugin:
    register: true
----

. Ensure the status of console pods is `running` by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-console -l app=console
----

. Restart the console pods by running the following command:
+
[source,terminal]
----
$ oc delete pods -n openshift-console -l app=console
----

. Clear your browser cache and history.

. Check the status of network observability plugin pods by running the following command:
+
[source,terminal]
----
$ oc get pods -n netobserv -l app=netobserv-plugin
----
+
.Example output
----
NAME                                READY   STATUS    RESTARTS   AGE
netobserv-plugin-68c7bbb9bb-b69q6   1/1     Running   0          21s
----

. Check the logs of the network observability plugin pods by running the following command:
+
[source,terminal]
----
$ oc logs -n netobserv -l app=netobserv-plugin
----
+
.Example output
[source,terminal]
----
time="2022-12-13T12:06:49Z" level=info msg="Starting netobserv-console-plugin [build version: , build date: 2022-10-21 15:15] at log level info" module=main
time="2022-12-13T12:06:49Z" level=info msg="listening on https://:9001" module=server
----

// Module included in the following assemblies:
//
// * networking/network_observability/troubleshooting-network-observability.adoc

[id="configure-network-traffic-flowlogs-pipeline-kafka_{context}"]
= Flowlogs-Pipeline does not consume network flows after installing Kafka

[role="_abstract"]
Resolve issues where the flow-pipeline fails to consume network flows from Kafka by manually restarting the flow-pipeline pods to restore the connection between the flow collector and your Kafka deployment.

If you deployed the flow collector first with `deploymentModel: KAFKA` and then deployed Kafka, the flow collector might not connect correctly to Kafka. Manually restart the flow-pipeline pods where Flowlogs-pipeline does not consume network flows from Kafka.

.Procedure

. Delete the flow-pipeline pods to restart them by running the following command:
+
[source,terminal]
----
$ oc delete pods -n netobserv -l app=flowlogs-pipeline-transformer
----

// Module included in the following assemblies:
//
// * networking/network_observability/troubleshooting-network-observability.adoc

[id="configure-network-traffic-interfaces_{context}"]
= Failing to see network flows from both br-int and br-ex interfaces

[role="_abstract"]
Resolve issues with missing network flows by removing interface restrictions on virtual bridge devices like `br-int` and `br-ex`, ensuring the eBPF agent can attach to the appropriate Layer 3 interfaces.

`br-ex` and `br-int` are virtual bridge devices operated at OSI layer 2. The eBPF agent works at the IP and TCP levels, layers 3 and 4 respectively. You can expect that the eBPF agent captures the network traffic passing through `br-ex` and `br-int`, when the network traffic is processed by other interfaces such as physical host or virtual pod interfaces. If you restrict the eBPF agent network interfaces to attach only to `br-ex` and `br-int`, you do not see any network flow.

Manually remove the part in the `interfaces` or `excludeInterfaces` that restricts the network interfaces to `br-int` and `br-ex`.

.Procedure

. Remove the `interfaces: [ 'br-int', 'br-ex' ]` field. This allows the agent to fetch information from all the interfaces. Alternatively, you can specify the Layer-3 interface for example, `eth0`. Run the following command:
+
[source,terminal]
----
$ oc edit -n netobserv flowcollector.yaml -o yaml
----
+
.Example output
----
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollector
metadata:
  name: cluster
spec:
  agent:
    type: EBPF
    ebpf:
      interfaces: [ 'br-int', 'br-ex' ] <1>
----
<1> Specifies the network interfaces.

// Module included in the following assemblies:
//
// * networking/network_observability/troubleshooting-network-observability.adoc

[id="controller-manager-pod-runs-out-of-memory_{context}"]
= Network observability controller manager pod runs out of memory

[role="_abstract"]
Resolve memory issues with the Network Observability Operator by increasing the memory limits in the `Subscription` object to prevent the controller manager pod from running out of memory.

You can increase memory limits for the Network Observability Operator by editing the `spec.config.resources.limits.memory` specification in the `Subscription` object.

.Procedure

. In the web console, navigate to *Ecosystem* -> *Installed Operators*
. Click *Network Observability* and then select *Subscription*.
. From the *Actions* menu, click *Edit Subscription*.
.. Alternatively, you can use the CLI to open the YAML configuration for the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc edit subscription netobserv-operator -n openshift-netobserv-operator
----
. Edit the `Subscription` object to add the `config.resources.limits.memory` specification and set the value to account for your memory requirements. See the Additional resources for more information about resource considerations:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: netobserv-operator
  namespace: openshift-netobserv-operator
spec:
  channel: stable
  config:
    resources:
      limits:
        memory: 800Mi     <1>
      requests:
        cpu: 100m
        memory: 100Mi
  installPlanApproval: Automatic
  name: netobserv-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  startingCSV: <network_observability_operator_latest_version> <2>
----
<1> For example, you can increase the memory limit to `800Mi`.
<2> This value should not be edited, but note that it changes depending on the most current release of the Operator.

// Module included in the following assemblies:
//
// * networking/network_observability/troubleshooting-network-observability.adoc

[id="troubleshooting-query-loki-manually_{context}"]
= Running custom queries to Loki

[role="_abstract"]
Troubleshoot network flow data by running custom Loki queries to retrieve available labels or filter logs by specific criteria, such as source namespaces, using the command-line interface.

There are two examples of ways to do this, which you can adapt according to your needs by replacing the <api_token> with your own.

[NOTE]
====
These examples use the `netobserv` namespace for the Network Observability Operator and Loki deployments. Additionally, the examples assume that the LokiStack is named `loki`. You can optionally use a different namespace and naming by adapting the examples, specifically the `-n netobserv` or the `loki-gateway` URL.
====

.Prerequisites
* Installed {loki-op} for use with Network Observability Operator.

.Procedure

. To get all available labels, run the following command:
+
[source,terminal]
----
$ oc exec deployment/netobserv-plugin -n netobserv -- curl -G -s -H 'X-Scope-OrgID:network' -H 'Authorization: Bearer <api_token>' -k https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network/loki/api/v1/labels | jq
----

. To get all flows from the source namespace, `my-namespace`, run the following command:
+
[source,terminal]
----
$ oc exec deployment/netobserv-plugin -n netobserv -- curl -G -s -H 'X-Scope-OrgID:network' -H 'Authorization: Bearer <api_token>' -k https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network/loki/api/v1/query --data-urlencode 'query={SrcK8S_Namespace="my-namespace"}' | jq
----

[role="_additional-resources"]
.Additional resources
* Resource considerations

// Module included in the following assemblies:

// * networking/network_observability/troubleshooting-network-observability.adoc

[id="network-observability-troubleshooting-loki-resource-exhausted_{context}"]
= Troubleshooting Loki ResourceExhausted error

[role="_abstract"]
Resolve Loki `ResourceExhausted` errors by adjusting the `batchSize` in the `FlowCollector` resource or the maximum message size settings in your Loki configuration to ensure flow data stays within memory limits.

Loki may return a `ResourceExhausted` error when network flow data sent by network observability exceeds the configured maximum message size. If you are using the Red{nbsp}Hat {loki-op}, this maximum message size is configured to 100 MiB.

.Procedure
. Navigate to *Ecosystem* -> *Installed Operators*, viewing *All projects* from the *Project* drop-down menu.
. In the *Provided APIs* list, select the Network Observability Operator.
. Click the *Flow Collector* then the *YAML view* tab.
.. If you are using the {loki-op}, check that the `spec.loki.batchSize` value does not exceed 98 MiB.
.. If you are using a Loki installation method that is different from the Red{nbsp}Hat {loki-op}, such as Grafana Loki, verify that the `grpc_server_max_recv_msg_size` Grafana Loki server setting is higher than the `FlowCollector` resource `spec.loki.batchSize` value. If it is not, you must either increase the `grpc_server_max_recv_msg_size` value, or decrease the `spec.loki.batchSize` value so that it is lower than the limit.
. Click *Save* if you edited the *FlowCollector*.

// Module included in the following assemblies:

// * networking/network_observability/troubleshooting-network-observability.adoc

[id="network-observability-troubleshooting-loki-empty-ring_{context}"]
= Loki empty ring error

[role="_abstract"]
Investigate and resolve Loki "empty ring" errors by checking pod health, clearing old persistent volume claims, or restarting pods to restore connectivity and ensure network flows are properly stored and displayed.

The Loki "empty ring" error results in flows not being stored in Loki and not showing up in the web console. This error might happen in various situations. A single workaround to address them all does not exist. There are some actions you can take to investigate the logs in your Loki pods, and verify that the `LokiStack` is healthy and ready.

Some of the situations where this error is observed are as follows:

* After a `LokiStack` is uninstalled and reinstalled in the same namespace, old PVCs are not removed, which can cause this error.
** *Action*: You can try removing the `LokiStack` again, removing the PVC, then reinstalling the `LokiStack`.
* After a certificate rotation, this error can prevent communication with the `flowlogs-pipeline` and `console-plugin` pods.
** *Action*: You can restart the pods to restore the connectivity.

// Module included in the following assemblies:

// * networking/network_observability/troubleshooting-network-observability.adoc

[id="network-observability-troubleshooting-loki-tenant-rate-limit_{context}"]
= LokiStack rate limit errors

[role="_abstract"]
Resolve Loki rate limit errors and prevent data loss by updating the `LokiStack` resource to increase the ingestion rate and burst limits for your network observability data streams.

A rate-limit placed on the Loki tenant can result in potential temporary loss of data and a 429 error: `Per stream rate limit exceeded (limit:xMB/sec) while attempting to ingest for stream`. You might consider having an alert set to notify you of this error. For more information, see "Creating Loki rate limit alerts for the NetObserv dashboard" in the Additional resources of this section.

You can update the LokiStack CRD with the `perStreamRateLimit` and `perStreamRateLimitBurst` specifications, as shown in the following procedure.

.Procedure
. Navigate to *Ecosystem* -> *Installed Operators*, viewing *All projects* from the *Project* dropdown.
. Look for *{loki-op}*, and select the *LokiStack* tab.
. Create or edit an existing *LokiStack* instance using the *YAML view* to add the `perStreamRateLimit` and `perStreamRateLimitBurst` specifications:
+
[source, yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: loki
  namespace: netobserv
spec:
  limits:
    global:
      ingestion:
        perStreamRateLimit: 6        <1>
        perStreamRateLimitBurst: 30  <2>
  tenants:
    mode: openshift-network
  managementState: Managed
----
<1> The default value for `perStreamRateLimit` is `3`.
<2> The default value for `perStreamRateLimitBurst` is `15`.

. Click *Save*.

.Verification
Once you update the `perStreamRateLimit` and `perStreamRateLimitBurst` specifications, the pods in your cluster restart and the 429 rate-limit error no longer occurs.

[id="network-observability-troubleshooting-large-query-timeout_{context}"]
= Running a large query results in Loki errors

[role="_abstract"]
Understand how you can mitigate Loki timeout and request errors when running large queries by using indexed filters, leveraging Prometheus for long time ranges, creating custom metrics, or adjusting Loki and FlowCollector performance settings.

When running large queries for a long time, Loki errors can occur, such as a `timeout` or `too many outstanding requests`. There is no complete corrective for this issue, but there are several ways to mitigate it:

Adapt your query to add an indexed filter::
+
With Loki queries, you can query on both indexed and non-indexed fields or labels. Queries that contain filters on labels perform better. For example, if you query for a particular Pod, which is not an indexed field, you can add its Namespace to the query. The list of indexed fields can be found in the "Network flows format reference", in the `Loki label` column.

Consider querying Prometheus rather than Loki::
+
Prometheus is a better fit than Loki to query on large time ranges. However, whether or not you can use Prometheus instead of Loki depends on the use case. For example, queries on Prometheus are much faster than on Loki, and large time ranges do not impact performance. But Prometheus metrics do not contain as much information as flow logs in Loki. The Network Observability OpenShift web console automatically favors Prometheus over Loki if the query is compatible; otherwise, it defaults to Loki. If your query does not run against Prometheus, you can change some filters or aggregations to make the switch. In the OpenShift web console, you can force the use of Prometheus. An error message is displayed when incompatible queries fail, which can help you figure out which labels to change to make the query compatible. For example, changing a filter or an aggregation from *Resource* or *Pods* to *Owner*.

Consider using the FlowMetrics API to create your own metric::
If the data that you need isn't available as a Prometheus metric, you can use the FlowMetrics API to create your own metric. For more information, see "FlowMetrics API Reference" and "Configuring custom metrics by using FlowMetric API".

Configure Loki to improve the query performance::
+
If the problem persists, you can consider configuring Loki to improve the query performance. Some options depend on the installation mode you used for Loki, such as using the Operator and `LokiStack`, or `Monolithic` mode, or `Microservices` mode.
+
* In `LokiStack` or `Microservices` modes, try increasing the number of querier replicas.
* Increase the query timeout. You must also increase the Network Observability read timeout to Loki in the `FlowCollector` `spec.loki.readTimeout`.

[role="_additional-resources"]
.Additional resources
* Network flows format reference
* FlowMetric API reference
* Configuring custom metrics by using FlowMetric API
