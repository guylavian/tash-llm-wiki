---
title: "Monitoring MetalLB configuration status"
type: reference
domain: openshift
slug: networking-4-22-monitoring-metallb-status
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/monitoring-metallb-status
version: 4.22
family: networking
documentKind: "Documentation"
---

# Monitoring MetalLB configuration status

[id=monitoring-metallb-status"]
= Monitoring MetalLB configuration status

[role="_abstract"]
As an OpenShift Container Platform system administrator, you can monitor the operational status of your MetalLB deployment by examining its custom resources (CRs). These status fields provide information about IP address allocations, BGP peer announcements, and session states, which are important for effective monitoring and troubleshooting.

// Address pool custom resource
// Module included in the following assemblies:
//
// * networking/metallb/monitoring-metallb-status.adoc

[id="nw-metallb-status-reporting_{context}"]
= Understanding MetalLB status custom resources

[role="_abstract"]
MetalLB provides a scalable framework for monitoring the health of network traffic and IP addresses. Use status fields in MetalLB custom resources to track session status and troubleshoot configuration.

MetalLB exposes status information for several key components, providing a comprehensive view of its configuration and operation.

.MetalLB status resources
[cols="1,2,2", options="header"]
|===
| Resource | Description | Troubleshooting command

| *`IPAddressPool` (status field)*
| Shows the cluster-wide allocation and availability of IP addresses within a defined pool, including the number of assigned and available addresses for both IPv4 and IPv6.
| `oc get ipaddresspool _<IPAddressPool-name>_ -n metallb-system -o yaml`

| *`ServiceBGPStatus`*
| Shows which service IP addresses the system announces to specific BGP peers across the network infrastructure.
| `oc get servicebgpstatus -n metallb-system`

| *`BGPSessionStatus`*
| Shows the real-time operational state of the border gateway protocol (BGP) and bidirectional forwarding detection (BFD) sessions between a specific cluster node and a BGP peer, indicating if the channel is `Established` or `Up` based on routing stack feedback.
| `oc get bgpsessionstatus -o wide`

| *`ConfigurationState`*
| Shows whether the MetalLB controller and speakers have successfully validated and applied the current configuration. MetalLB creates one resource for the controller and one for each speaker node. Reports errors when custom resources are incompatible.
| `oc get configurationstates -n metallb-system`

|===

The MetalLB controller, typically deployed as `metallb-system/controller`, is responsible for managing IP address assignments and updating the `IPAddressPool` status. When a service requests a `LoadBalancer` IP, the controller allocates an IP from an appropriate `IPAddressPool` and updates the status fields to reflect the current number of assigned and available IP addresses.

// Add an address pool
[id="nw-metallb-configure-address-pool_{context}"]
= Viewing the `IPAddressPool` status

[role="_abstract"]
Check IP address allocation from your MetalLB pools by viewing the `IPAddressPool` status. This status shows the number of addresses assigned to services and the number remaining available for assignment.

As a cluster administrator, you can add address pools to your cluster to control the IP addresses that MetalLB can assign to load-balancer services. This example shows how to create an `IPAddressPool` custom resource (CR) and view its status. The configuration sets the advertisement mode to Layer 2 (L2).

.Prerequisites

* You have an OpenShift Container Platform cluster with the MetalLB Operator installed.
* You have deployed a MetalLB instance.

.Procedure

. Create an IP address pool.

.. Create a file, named for example `ipaddresspool.yaml`, with content such as the following:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: doc-example-l2
  namespace: metallb-system
spec:
  addresses:
  - 192.168.122.200-192.168.122.220
  autoAssign: true
  avoidBuggyIPs: false
----

.. Apply the configuration for the IP address pool:
+
[source,terminal]
----
$ oc apply -f ipaddresspool.yaml
----

. View the status of the IP address pool by running the following command:
+
[source,terminal]
----
$ oc get ipaddresspool doc-example-l2 -n metallb-system -o yaml
----
+
The output is similar to the following:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"metallb.io/v1beta1","kind":"IPAddressPool","metadata":{"annotations":{},"name":"doc-example-l2","namespace":"metallb-system"},"spec":{"addresses":["192.168.122.200-192.168.122.220"],"autoAssign":true,"avoidBuggyIPs":false}}
  creationTimestamp: "2025-07-17T10:13:37Z"
  generation: 1
  name: doc-example-l2
  namespace: metallb-system
  resourceVersion: "29080"
  uid: 8df1c303-03ac-4d31-8970-6dacdb173dc2
spec:
  addresses:
  - 192.168.122.200-192.168.122.220
  autoAssign: true
  avoidBuggyIPs: false
status:
  assignedIPv4: 0
  assignedIPv6: 0
  availableIPv4: 21
  availableIPv6: 0
----
+
* `assignedIPv4` represents the total number of IPv4 addresses that MetalLB has successfully assigned from this pool to `LoadBalancer` services.
* `assignedIPv6` represents the total number of IPv6 addresses that MetalLB has successfully assigned from this pool to `LoadBalancer` services.
* `availableIPv4` indicates the total number of IPv4 addresses remaining and available for assignment within this pool. MetalLB calculates this value by subtracting `assignedIPv4` from the total theoretical IPv4 addresses in the `spec.addresses` ranges, potentially accounting for `avoidBuggyIPs` if enabled.
* `availableIPv6` indicates the total number of IPv6 addresses remaining and available for assignment within this pool. The system calculates this value similarly to `availableIPv4`, using the total theoretical IPv6 addresses in the `spec.addresses` ranges.

. Create an `L2Advertisement` CR for Layer 2 mode with the following sample YAML:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: l2advertisement
  namespace: metallb-system
spec:
  ipAddressPools:
  - doc-example-l2
----

.. Apply the configuration for the L2 advertisement by running the following command:
+
[source,terminal]
----
$ oc apply -f l2advertisement.yaml
----

. Deploy an application and expose it with a `LoadBalancer` service.

.. Create a file, like `nginx.yaml`, with the following content to deploy an Nginx application:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: quay.io/openshifttest/hello-openshift:multiarch
        ports:
        - containerPort: 8080
----

.. Apply the configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f nginx.yaml
----

.. Expose the deployment as a `LoadBalancer` service by creating a file, such as `nginx-service.yaml`, with content like the following:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  namespace: default
  annotations:
    metallb.universe.tf/address-pool: doc-example-l2
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: LoadBalancer
----
+
[IMPORTANT]
====
The service must be in the same namespace as your application deployment. The `metallb.universe.tf/address-pool` annotation tells MetalLB which `IPAddressPool` to use for IP allocation.
====

.. Apply the service configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f nginx-service.yaml
----

. View the updated `IPAddressPool` status to see the assigned and available IP addresses by running the following command:
+
[source,terminal]
----
$ oc get ipaddresspool doc-example-l2 -n metallb-system -o yaml
----
+
The output is similar to the following:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"metallb.io/v1beta1","kind":"IPAddressPool","metadata":{"annotations":{},"name":"doc-example-l2","namespace":"metallb-system"},"spec":{"addresses":["192.168.122.200-192.168.122.220"],"autoAssign":true,"avoidBuggyIPs":false}}
  creationTimestamp: "2025-07-17T10:13:37Z"
  generation: 1
  name: doc-example-l2
  namespace: metallb-system
  resourceVersion: "30250"
  uid: 8df1c303-03ac-4d31-8970-6dacdb173dc2
spec:
  addresses:
  - 192.168.122.200-192.168.122.220
  autoAssign: true
  avoidBuggyIPs: false
status:
  assignedIPv4: 1
  assignedIPv6: 0
  availableIPv4: 20
  availableIPv6: 0
----
+
The `assignedIPv4` value of `1` indicates that one IPv4 address from this pool has been successfully assigned by MetalLB to your `nginx-service` `LoadBalancer`.

// View ServiceBGPStatus
[id="nw-viewing-service-bgp-status_{context}"]
= Viewing the ServiceBGPStatus custom resource

[role="_abstract"]
You can verify border gateway protocol (BGP) advertisement status for your services by viewing the `ServiceBGPStatus` custom resource, which shows which BGP peers receive advertisements from each node. This is essential for debugging connectivity in telco environments.

The `ServiceBGPStatus` CR reports the BGP peering status for a service, detailing which neighbors are receiving updates from a specific node.

[NOTE]
====
`ServiceBGPStatus` resources are created in the `metallb-system` namespace, not in the namespace where your `LoadBalancer` service is deployed. Always query these resources with `-n metallb-system`.
====

.Prerequisites

* You have an OpenShift Container Platform cluster with the MetalLB Operator installed.
* You have deployed a MetalLB instance.

This example shows how to configure MetalLB for BGP mode, deploy a service, and view the `ServiceBGPStatus` to verify BGP advertisements.

.Procedure

. Create an `IPAddressPool` CR for BGP, like the following example, and save it as `ipaddresspool.yaml`:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: bgp-pool
  namespace: metallb-system
spec:
  addresses:
  - 192.168.122.210-192.168.122.220
  autoAssign: true
----

. Run the following command to create the `IPAddressPool` configuration:
+
[source,terminal]
----
$ oc apply -f ipaddresspool.yaml
----

. To configure a BGP peer, create a file named `bgppeer.yaml` with the following content:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: bgp-peer
  namespace: metallb-system
spec:
  myASN: 64501
  peerASN: 64500
  peerAddress: 192.168.1.1
----
+
* Set the `spec:peerAddress` field to the IP address of your BGP router.

. Apply the BGPPeer configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f bgppeer.yaml
----

. To create a BGP advertisement to advertise the pool, create a file named `bgpadvertisement.yaml` with the following content:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: bgp-advertisement
  namespace: metallb-system
spec:
  ipAddressPools:
  - bgp-pool
----

. Apply the BGPAdvertisement configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f bgpadvertisement.yaml
----

. Deploy an application and expose it with a `LoadBalancer` service. For this example, create a simple test application named for example `test-app` by creating a file named `deployment.yaml` with the following content:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-app
  namespace: default
spec:
  replicas: 2
  selector:
    matchLabels:
      app: test-app
  template:
    metadata:
      labels:
        app: test-app
    spec:
      containers:
      - name: test-app
        image: quay.io/openshifttest/hello-openshift:multiarch
        ports:
        - containerPort: 8080
----

. Apply the deployment:
+
[source,terminal]
----
$ oc apply -f deployment.yaml
----

. Create a `LoadBalancer` service for the application:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: test-service
  namespace: default
spec:
  selector:
    app: test-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: LoadBalancer
----
+
[IMPORTANT]
====
The system creates `ServiceBGPStatus` resources automatically only when the service has at least one ready endpoint (running pod). Ensure your application pods are running before checking for `ServiceBGPStatus` resources.
====

. Apply the service configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f service.yaml
----

. Verify the service received an external IP by running the following command:
+
[source,terminal]
----
$ oc get svc test-service -n default
----
+
The output is similar to the following:
+
[source,terminal]
----
NAME           TYPE           CLUSTER-IP       EXTERNAL-IP       PORT(S)        AGE
test-service   LoadBalancer   172.30.116.108   192.168.122.210   80:32431/TCP   2m
----

. View the `ServiceBGPStatus` resources by running the following command:
+
[source,terminal]
----
$ oc get servicebgpstatus -n metallb-system
----
+
The output is similar to the following:
+
[source,terminal]
----
NAME                  NODE       SERVICE NAME   SERVICE NAMESPACE
bgp-xxxxx             worker0    test-service   default
----
+
[NOTE]
====
`ServiceBGPStatus` resources are created with generated names. Use labels to find the status for your service:

[source,terminal]
----
$ oc get servicebgpstatus -n metallb-system -l metallb.io/service-name=test-service
----
====

. View the details of the `ServiceBGPStatus` CR for your service:
+
[source,terminal]
----
$ oc get servicebgpstatus bgp-xxxxx -n metallb-system -o yaml
----
+
The output is similar to the following:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: ServiceBGPStatus
metadata:
  name: bgp-xxxxx
  namespace: metallb-system
  labels:
    metallb.io/node: worker0
    metallb.io/service-name: test-service
    metallb.io/service-namespace: default
status:
  node: worker0
  peers:
  - bgp-peer
  serviceName: test-service
  serviceNamespace: default
----
+
* `metadata.labels.metallb.io/node` indicates the node that is advertising the service via BGP.
* `metadata.labels.metallb.io/service-name` identifies the service being advertised.
* `metadata.labels.metallb.io/service-namespace` identifies the namespace of the service being advertised.
* `status.node` confirms the name of the node advertising the service.
* `status.peers` lists the names of the BGPPeer resources to which the service is being advertised. This is useful for confirming that the advertisement is reaching the intended peers.
* `status.serviceName` indicates the name of the service being advertised.
* `status.serviceNamespace` indicates the namespace of the service being advertised.

// Verify BGP session establishment
[id="nw-metallb-verifying-bgp-session_{context}"]
= Verifying BGP session state

[role="_abstract"]
Once you configure MetalLB for border gateway protocol (BGP) mode, you can verify that the system has established BGP sessions and is advertising routes. You can examine the `BGPSessionState` custom resource (CR) and the `FRRNodeState` CR to troubleshoot BGP connectivity and confirm proper route advertisement.

[NOTE]
====
The `BGPSessionState` CR is updated at a regular poll interval of 2 minutes. It can take up to 2 minutes for the CR to reflect the actual BGP state.
====

.Prerequisites

* You have an OpenShift Container Platform cluster with the MetalLB Operator installed.
* You have configured MetalLB for BGP mode with:
** An `IPAddressPool`
** A `BGPPeer` configuration
** A `BGPAdvertisement`
* You have deployed at least one `LoadBalancer` service.

.Procedure

. Check BGP session status by running the following command:
+
[source,terminal]
----
$ oc get bgpsessionstates.frrk8s.metallb.io -A -o wide
----
+
This example output shows the BGP session status between each node and its configured BGP peers. Look for the `BGP` column to confirm that the session is `Established`.
+
[source,terminal]
----
NAMESPACE           NAME               NODE       PEER         VRF   BGP           BFD
openshift-frr-k8s   worker-2gjfq       worker     10.89.0.64         Active        N/A
openshift-frr-k8s   worker-9gtnb       worker     10.89.0.63         Established   N/A
openshift-frr-k8s   worker2-rknga      worker2    10.89.0.66         Established   Up
openshift-frr-k8s   worker2-t7bfc      worker2    172.30.0.2         Established   Down
----

. Check `FRRNodeState` to see the BGP configuration on each node by running the following command:
+
[source,terminal]
----
$ oc get frrnodestate -n metallb-system
----
+
The example output lists the `FRRNodeState` resources for each node where the MetalLB speaker is running.
+
[source,terminal]
----
NAME                 AGE
worker0.example.com  5m
----

. View the detailed BGP configuration and running state by running the following command for a specific node:
+
[source,terminal]
----
$ oc get frrnodestate worker0.example.com -n metallb-system -o yaml
----
+
The `status.runningConfig` field shows the FRR BGP configuration including configured BGP neighbors, route advertisements, and prefix lists.

. Verify that the system is advertising routes by checking the `FRRNodeState` resource for the relevant node with this command:
+
[source,terminal]
----
$ oc get frrnodestate _<node-name>_ -n metallb-system -o jsonpath='{.status.runningConfig}' | grep "network"
----
+
The output displays the network prefixes that BGP advertises. For example:
+
[source,terminal]
----
 address-family ipv4 unicast
  network 192.168.122.210/32
----
+
This confirms that BGP is advertising the service IP.

// Check configuration status
// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/metallb/monitoring-metallb-status.adoc

[id="nw-metallb-checking-configuration-status_{context}"]
= Checking MetalLB configuration status

[role="_abstract"]
You can verify that the MetalLB controller and speakers have successfully applied the current configuration by viewing the `ConfigurationState` custom resource (CR). MetalLB creates a `ConfigurationState` resource for the controller and one for each speaker node. These resources report whether the configuration is valid and surface error details when validation fails, such as incompatible custom resources.

.Prerequisites

* You have an OpenShift Container Platform cluster with the MetalLB Operator installed.
* You have deployed a MetalLB instance.
* You have configured MetalLB resources such as `IPAddressPool`, `BGPPeer`, `BFDProfile`, `Community`, or `FRRConfiguration`.

.Procedure

. List the `ConfigurationState` resources by running the following command:
+
[source,terminal]
----
$ oc get configurationstates -n metallb-system
----
+
.Example output
[source,terminal]
----
NAME                         RESULT   ERRORSUMMARY   AGE
controller                   Valid                   75m
speaker-mysno-sno.demo.lab   Valid                   28m
----
+
The `controller` resource shows the status for the MetalLB controller. Each `speaker-<node-name>` resource shows the status for the speaker on that node.

. Verify that the controller has a valid configuration by inspecting the `ConfigurationState` details. Run the following command:
+
[source,terminal]
----
$ oc get configurationstates controller -n metallb-system -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: ConfigurationState
metadata:
  creationTimestamp: "2026-04-21T09:46:47Z"
  generation: 1
  labels:
    metallb.io/component-type: controller
  name: controller
  namespace: metallb-system
  resourceVersion: "28268"
  uid: 23f5c492-4d5c-4893-84ea-77904c006404
status:
  conditions:
  - lastTransitionTime: "2026-04-21T09:54:00Z"
    message: ""
    reason: Reconciled
    status: "True"
    type: poolReconcilerValid
  result: Valid
----
+
Confirm that the output has the following values:
+
* `result: Valid` indicates that all configured resources are compatible and active. If this value is `Invalid`, check the `errorSummary` field for aggregated error messages that identify which part of the configuration has failed.
* `message: Describes any configuration problem that occurs.  Here, `""` confirms that no errors were reported.
* `reason: Reconciled` with `status: "True"` confirms that the reconciler has successfully processed the configuration. If the `reason` is `ReconciliationFailed` and `status` is `"False"`, the `message` field contains details about the failure.
+
[NOTE]
====
The controller does not validate peer-level settings. Errors such as a missing `BFDProfile`, undefined `Community`, or missing authentication secret are reported only by the speakers. A `Valid` controller with one or more `Invalid` speakers is expected in these cases. Always check both controller and speaker `ConfigurationState` resources.
====
+
If the configuration is invalid, the output is similar to the following example:
+
[source,yaml]
----
apiVersion: metallb.io/v1beta1
kind: ConfigurationState
metadata:
  creationTimestamp: "2026-04-21T09:51:17Z"
  generation: 1
  labels:
    metallb.io/component-type: speaker
    metallb.io/node-name: mysno-sno.demo.lab
  name: speaker-mysno-sno.demo.lab
  namespace: metallb-system
  resourceVersion: "31161"
  uid: 339781bf-ec9a-4ba9-aaba-0a9ac8ebce78
status:
  conditions:
  - lastTransitionTime: "2026-04-21T10:09:34Z"
    message: 'configuration error: peer peer1 referencing non existing bfd profile
      my-bfd-profile'
    reason: ConfigurationError
    status: "False"
    type: configReconcilerValid
  errorSummary: 'configuration error: peer peer1 referencing non existing bfd profile
    my-bfd-profile'
  result: Invalid
----
+
Confirm that the output has the following values to identify the problem:
+
* `result: Invalid` indicates that one or more configured resources are incompatible. The `errorSummary` field provides an aggregated description of the problem.
* `reason: ConfigurationError` with `status: "False"` indicates that the reconciler failed to process the configuration. The `message` field describes the specific error.
* In this example, the `BGPPeer` resource `peer1` references a `BFDProfile` named `my-bfd-profile` that does not exist. To resolve this error, either create the missing `BFDProfile` resource or update the `BGPPeer` to reference an existing `BFDProfile`.
+
[NOTE]
====
The `ConfigurationState` resource does not report errors that arise when the configuration applied by the speaker to the `frr-k8s` daemon conflicts with other external configurations within that daemon.
====

. After correcting the configuration, verify that the status shows a valid configuration by running the following command:
+
[source,terminal]
----
$ oc get configurationstates -n metallb-system -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.result}{"\n"}{end}'
----
+
A return value of `Valid` for all entries confirms that the MetalLB controller and speakers are operating with a valid configuration.

[role="_additional-resources"]
== Additional resources

* About MetalLB and the MetalLB Operator
