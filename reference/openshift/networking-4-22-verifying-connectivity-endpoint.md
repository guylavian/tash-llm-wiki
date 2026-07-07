---
title: "Verifying connectivity to an endpoint"
type: reference
domain: openshift
slug: networking-4-22-verifying-connectivity-endpoint
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/verifying-connectivity-endpoint
version: 4.22
family: networking
documentKind: "Documentation"
---

# Verifying connectivity to an endpoint

[id="verifying-connectivity-endpoint"]
= Verifying connectivity to an endpoint

The Cluster Network Operator (CNO) runs a controller, the connectivity check controller, that performs a connection health check between resources within your cluster.
By reviewing the results of the health checks, you can diagnose connection problems or eliminate network connectivity as the cause of an issue that you are investigating.

// Module included in the following assemblies:
//
// * networking/verifying-connectivity-endpoint.adoc

[id="nw-pod-network-connectivity-checks_{context}"]
= Connection health checks that are performed

To verify that cluster resources are reachable, a TCP connection is made to each of the following cluster API services:

* Kubernetes API server service
* Kubernetes API server endpoints
* OpenShift API server service
* OpenShift API server endpoints
* Load balancers

To verify that services and service endpoints are reachable on every node in the cluster, a TCP connection is made to each of the following targets:

* Health check target service
* Health check target endpoints

// Module included in the following assemblies:
//
// * networking/verifying-connectivity-endpoint.adoc

[id="nw-pod-network-connectivity-implementation_{context}"]
= Implementation of connection health checks

The connectivity check controller orchestrates connection verification checks in your cluster. The results for the connection tests are stored in `PodNetworkConnectivity` objects in the `openshift-network-diagnostics` namespace. Connection tests are performed every minute in parallel.

The Cluster Network Operator (CNO) deploys several resources to the cluster to send and receive connectivity health checks:

Health check source:: This program deploys in a single pod replica set managed by a `Deployment` object. The program consumes `PodNetworkConnectivity` objects and connects to the `spec.targetEndpoint` specified in each object.

Health check target:: A pod deployed as part of a daemon set on every node in the cluster. The pod listens for inbound health checks. The presence of this pod on every node allows for the testing of connectivity to each node.

You can configure the nodes which network connectivity sources and targets run on with a node selector. Additionally, you can specify permissible _tolerations_ for source and target pods. The configuration is defined in the singleton `cluster` custom resource of the `Network` API in the `config.openshift.io/v1` API group.

Pod scheduling occurs after you have updated the configuration. Therefore, you must apply node labels that you intend to use in your selectors before updating the configuration. Labels applied after updating your network connectivity check pod placement are ignored.

Refer to the default configuration in the following YAML:

.Default configuration for connectivity source and target pods
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  # ...
    networkDiagnostics: <1>
      mode: "All" <2>
      sourcePlacement: <3>
        nodeSelector:
          checkNodes: groupA
        tolerations:
        - key: myTaint
          effect: NoSchedule
          operator: Exists
      targetPlacement: <4>
        nodeSelector:
          checkNodes: groupB
        tolerations:
        - key: myOtherTaint
          effect: NoExecute
          operator: Exists
----
<1> Specifies the network diagnostics configuration. If a value is not specified or an empty object is specified, and `spec.disableNetworkDiagnostics=true` is set in the `network.operator.openshift.io` custom resource named `cluster`, network diagnostics are disabled. If set, this value overrides `spec.disableNetworkDiagnostics=true`.
<2> Specifies the diagnostics mode. The value can be the empty string, `All`, or `Disabled`. The empty string is equivalent to specifying `All`.
<3> Optional: Specifies a selector for connectivity check source pods. You can use the `nodeSelector` and `tolerations` fields to further specify the `sourceNode` pods. These are optional for both source and target pods. You can omit them, use both, or use only one of them.
<4> Optional: Specifies a selector for connectivity check target pods.
You can use the `nodeSelector` and `tolerations` fields to further specify the `targetNode` pods. These are optional for both source and target pods. You can omit them, use both, or use only one of them.

// Module included in the following assemblies:
//
// * networking/verifying-connectivity-endpoint.adoc

[id="nw-pod-network-connectivity-configuration_{context}"]
= Configuring pod connectivity check placement

As a cluster administrator, you can configure which nodes the connectivity check pods run by modifying the `network.config.openshift.io` object named `cluster`.

.Prerequisites

* Install the {oc-first}.

.Procedure

. Edit the connectivity check configuration by entering the following command:
+
[source,terminal]
----
$ oc edit network.config.openshift.io cluster
----

. In the text editor, update the `networkDiagnostics` stanza to specify the node selectors that you want for the source and target pods.

. Save your changes and exit the text editor.

.Verification

* Verify that the source and target pods are running on the intended nodes by entering the following command:

[source,terminal]
----
$ oc get pods -n openshift-network-diagnostics -o wide
----

.Example output
[source,text]
----
NAME                                    READY   STATUS    RESTARTS   AGE     IP           NODE                                        NOMINATED NODE   READINESS GATES
network-check-source-84c69dbd6b-p8f7n   1/1     Running   0          9h      10.131.0.8   ip-10-0-40-197.us-east-2.compute.internal   <none>           <none>
network-check-target-46pct              1/1     Running   0          9h      10.131.0.6   ip-10-0-40-197.us-east-2.compute.internal   <none>           <none>
network-check-target-8kwgf              1/1     Running   0          9h      10.128.2.4   ip-10-0-95-74.us-east-2.compute.internal    <none>           <none>
network-check-target-jc6n7              1/1     Running   0          9h      10.129.2.4   ip-10-0-21-151.us-east-2.compute.internal   <none>           <none>
network-check-target-lvwnn              1/1     Running   0          9h      10.128.0.7   ip-10-0-17-129.us-east-2.compute.internal   <none>           <none>
network-check-target-nslvj              1/1     Running   0          9h      10.130.0.7   ip-10-0-89-148.us-east-2.compute.internal   <none>           <none>
network-check-target-z2sfx              1/1     Running   0          9h      10.129.0.4   ip-10-0-60-253.us-east-2.compute.internal   <none>           <none>
----

// Module included in the following assemblies:
//
// * networking/verifying-connectivity-endpoint.adoc

[id="nw-pod-network-connectivity-check-object_{context}"]
= PodNetworkConnectivityCheck object fields

The `PodNetworkConnectivityCheck` object fields are described in the following tables.

.PodNetworkConnectivityCheck object fields
[cols="2,1,3a",options="header"]
|===

|Field|Type|Description

|`metadata.name`
|`string`
|The name of the object in the following format: `<source>-to-<target>`. The destination described by `<target>` includes one of following strings:

* `load-balancer-api-external`
* `load-balancer-api-internal`
* `kubernetes-apiserver-endpoint`
* `kubernetes-apiserver-service-cluster`
* `network-check-target`
* `openshift-apiserver-endpoint`
* `openshift-apiserver-service-cluster`

|`metadata.namespace`
|`string`
|The namespace that the object is associated with. This value is always `openshift-network-diagnostics`.

|`spec.sourcePod`
|`string`
|The name of the pod where the connection check originates, such as `network-check-source-596b4c6566-rgh92`.

|`spec.targetEndpoint`
|`string`
|The target of the connection check, such as `api.devcluster.example.com:6443`.

|`spec.tlsClientCert`
|`object`
|Configuration for the TLS certificate to use.

|`spec.tlsClientCert.name`
|`string`
|The name of the TLS certificate used, if any. The default value is an empty string.

|`status`
|`object`
|An object representing the condition of the connection test and logs of recent connection successes and failures.

|`status.conditions`
|`array`
|The latest status of the connection check and any previous statuses.

|`status.failures`
|`array`
|Connection test logs from unsuccessful attempts.

|`status.outages`
|`array`
|Connect test logs covering the time periods of any outages.

|`status.successes`
|`array`
|Connection test logs from successful attempts.

|===

The following table describes the fields for objects in the `status.conditions` array:

.status.conditions
[cols="2,1,3",options="header"]
|===
|Field |Type |Description

|`lastTransitionTime`
|`string`
|The time that the condition of the connection transitioned from one status to another.

|`message`
|`string`
|The details about last transition in a human readable format.

|`reason`
|`string`
|The last status of the transition in a machine readable format.

|`status`
|`string`
|The status of the condition.

|`type`
|`string`
|The type of the condition.

|===

The following table describes the fields for objects in the `status.conditions` array:

.status.outages
[cols="2,1,3",options="header"]
|===
|Field |Type |Description

|`end`
|`string`
|The timestamp from when the connection failure is resolved.

|`endLogs`
|`array`
|Connection log entries, including the log entry related to the successful end of the outage.

|`message`
|`string`
|A summary of outage details in a human readable format.

|`start`
|`string`
|The timestamp from when the connection failure is first detected.

|`startLogs`
|`array`
|Connection log entries, including the original failure.

|===

== Connection log fields

The fields for a connection log entry are described in the following table. The object is used in the following fields:

* `status.failures[]`
* `status.successes[]`
* `status.outages[].startLogs[]`
* `status.outages[].endLogs[]`

.Connection log object
[cols="2,1,3",options="header"]
|===
|Field |Type |Description

|`latency`
|`string`
|Records the duration of the action.

|`message`
|`string`
|Provides the status in a human readable format.

|`reason`
|`string`
|Provides the reason for status in a machine readable format. The value is one of `TCPConnect`, `TCPConnectError`, `DNSResolve`, `DNSError`.

|`success`
|`boolean`
|Indicates if the log entry is a success or failure.

|`time`
|`string`
|The start time of connection check.
|===

// Module included in the following assemblies:
//
// * networking/verifying-connectivity-endpoint.adoc

[id="nw-pod-network-connectivity-verify_{context}"]
= Verifying network connectivity for an endpoint

As a cluster administrator, you can verify the connectivity of an endpoint, such as an API server, load balancer, service, or pod, and verify that network diagnostics is enabled.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Confirm that network diagnostics are enable by entering the following command:
+
[source,terminal]
----
$ oc get network.config.openshift.io cluster -o yaml
----
+
.Example output
[source,text]
----
  # ...
  status:
  # ...
    conditions:
    - lastTransitionTime: "2024-05-27T08:28:39Z"
      message: ""
      reason: AsExpected
      status: "True"
      type: NetworkDiagnosticsAvailable
----

. List the current `PodNetworkConnectivityCheck` objects by entering the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitycheck -n openshift-network-diagnostics
----
+
.Example output
[source,terminal]
----
NAME                                                                                                                                AGE
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0   75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-1   73m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-2   75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-kubernetes-apiserver-service-cluster                               75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-kubernetes-default-service-cluster                                 75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-load-balancer-api-external                                         75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-load-balancer-api-internal                                         75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-network-check-target-ci-ln-x5sv9rb-f76d1-4rzrp-master-0            75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-network-check-target-ci-ln-x5sv9rb-f76d1-4rzrp-master-1            75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-network-check-target-ci-ln-x5sv9rb-f76d1-4rzrp-master-2            75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-network-check-target-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh      74m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-network-check-target-ci-ln-x5sv9rb-f76d1-4rzrp-worker-c-n8mbf      74m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-network-check-target-ci-ln-x5sv9rb-f76d1-4rzrp-worker-d-4hnrz      74m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-network-check-target-service-cluster                               75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-openshift-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0    75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-openshift-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-1    75m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-openshift-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-2    74m
network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-openshift-apiserver-service-cluster                                75m
----

. View the connection test logs:
.. From the output of the previous command, identify the endpoint that you want to review the connectivity logs for.
.. View the object by entering the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitycheck <name> \
  -n openshift-network-diagnostics -o yaml
----
+
where `<name>` specifies the name of the `PodNetworkConnectivityCheck` object.
+
.Example output
[source,terminal]
----
apiVersion: controlplane.operator.openshift.io/v1alpha1
kind: PodNetworkConnectivityCheck
metadata:
  name: network-check-source-ci-ln-x5sv9rb-f76d1-4rzrp-worker-b-6xdmh-to-kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0
  namespace: openshift-network-diagnostics
  ...
spec:
  sourcePod: network-check-source-7c88f6d9f-hmg2f
  targetEndpoint: 10.0.0.4:6443
  tlsClientCert:
    name: ""
status:
  conditions:
  - lastTransitionTime: "2021-01-13T20:11:34Z"
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnectSuccess
    status: "True"
    type: Reachable
  failures:
  - latency: 2.241775ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: failed
      to establish a TCP connection to 10.0.0.4:6443: dial tcp 10.0.0.4:6443: connect:
      connection refused'
    reason: TCPConnectError
    success: false
    time: "2021-01-13T20:10:34Z"
  - latency: 2.582129ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: failed
      to establish a TCP connection to 10.0.0.4:6443: dial tcp 10.0.0.4:6443: connect:
      connection refused'
    reason: TCPConnectError
    success: false
    time: "2021-01-13T20:09:34Z"
  - latency: 3.483578ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: failed
      to establish a TCP connection to 10.0.0.4:6443: dial tcp 10.0.0.4:6443: connect:
      connection refused'
    reason: TCPConnectError
    success: false
    time: "2021-01-13T20:08:34Z"
  outages:
  - end: "2021-01-13T20:11:34Z"
    endLogs:
    - latency: 2.032018ms
      message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0:
        tcp connection to 10.0.0.4:6443 succeeded'
      reason: TCPConnect
      success: true
      time: "2021-01-13T20:11:34Z"
    - latency: 2.241775ms
      message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0:
        failed to establish a TCP connection to 10.0.0.4:6443: dial tcp 10.0.0.4:6443:
        connect: connection refused'
      reason: TCPConnectError
      success: false
      time: "2021-01-13T20:10:34Z"
    - latency: 2.582129ms
      message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0:
        failed to establish a TCP connection to 10.0.0.4:6443: dial tcp 10.0.0.4:6443:
        connect: connection refused'
      reason: TCPConnectError
      success: false
      time: "2021-01-13T20:09:34Z"
    - latency: 3.483578ms
      message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0:
        failed to establish a TCP connection to 10.0.0.4:6443: dial tcp 10.0.0.4:6443:
        connect: connection refused'
      reason: TCPConnectError
      success: false
      time: "2021-01-13T20:08:34Z"
    message: Connectivity restored after 2m59.999789186s
    start: "2021-01-13T20:08:34Z"
    startLogs:
    - latency: 3.483578ms
      message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0:
        failed to establish a TCP connection to 10.0.0.4:6443: dial tcp 10.0.0.4:6443:
        connect: connection refused'
      reason: TCPConnectError
      success: false
      time: "2021-01-13T20:08:34Z"
  successes:
  - latency: 2.845865ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:14:34Z"
  - latency: 2.926345ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:13:34Z"
  - latency: 2.895796ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:12:34Z"
  - latency: 2.696844ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:11:34Z"
  - latency: 1.502064ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:10:34Z"
  - latency: 1.388857ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:09:34Z"
  - latency: 1.906383ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:08:34Z"
  - latency: 2.089073ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:07:34Z"
  - latency: 2.156994ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:06:34Z"
  - latency: 1.777043ms
    message: 'kubernetes-apiserver-endpoint-ci-ln-x5sv9rb-f76d1-4rzrp-master-0: tcp
      connection to 10.0.0.4:6443 succeeded'
    reason: TCPConnect
    success: true
    time: "2021-01-13T21:05:34Z"
----
