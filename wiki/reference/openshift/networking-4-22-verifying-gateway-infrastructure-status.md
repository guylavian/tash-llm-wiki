---
title: "Verify Gateway infrastructure status"
type: reference
domain: openshift
slug: networking-4-22-verifying-gateway-infrastructure-status
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/verifying-gateway-infrastructure-status
version: 4.22
family: networking
documentKind: "Documentation"
---

# Verify Gateway infrastructure status

[id="verifying-gateway-infrastructure-status"]
= Verify Gateway infrastructure status

[role="_abstract"]
To ensure your gateway infrastructure is properly configured and functioning, review the `status` conditions of your `GatewayClass` and `Gateway` custom resources (CRs). Checking these conditions confirms that the controller has successfully programmed your underlying data plane without routing conflicts.

To verify that your gateway infrastructure is functioning correctly, complete the following tasks:

* Understand `GatewayClass` status conditions to verify that the controller has claimed the class and that your installed API version is compatible.
* Review `Gateway` CR and listener `status` conditions to pinpoint data plane failures, configuration errors, or negative polarity conflicts.
* Query gateway infrastructure status using the CLI to quickly validate your deployment and retrieve assigned IP addresses.

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/verifying-gateway-infrastructure-status.adoc
//
[id="gatewayclass-status-conditions_{context}"]
= GatewayClass status conditions reference

[role="_abstract"]
To verify that your `GatewayClass` custom resource (CR) is valid and ready to provision gateways, review its `status` conditions. A healthy `GatewayClass` CR reports a status of `True` for core conditions like `Accepted` and `SupportedVersion`.

.`GatewayClass` CR status conditions
[cols="1,1,3",options="header"]
|===
|Condition |Status |Description and common reasons

|`Accepted`
|`True`
|The `GatewayClass` CR is valid and the controller has claimed it.

|`Accepted`
|`False`
|The configuration has errors or was rejected. Common reasons include `InvalidParameters` (referenced parameters are invalid or not found), `Pending` (the controller has not processed the resource yet), or `Unknown` (an unsupported `controllerName` was provided).

|`Accepted`
|`Unknown`
|The `GatewayClass` CR is waiting for the controller to process it.

|`SupportedVersion`
|`True`
|The installed Gateway API version is compatible with the controller.

|`SupportedVersion`
|`False`
|There is a version mismatch. A common reason is `UnsupportedVersion`, which indicates that the custom resource definition (CRD) version does not match the controller requirements.

|`ControllerInstalled`
|`True`
|The Cluster Ingress Operator successfully installed the Gateway API controller.

|`ControllerInstalled`
|`False`
|The installation failed.

|`ControllerInstalled`
|`Unknown`
|The controller has not started the installation yet.

|`CRDsReady`
|`True`
|The Istio CRDs are installed and actively managed by either the Cluster Ingress Operator or OLM.

|`CRDsReady`
|`False`
|The CRDs were installed by a third party or have mixed ownership, preventing the controller from managing them.

|`CRDsReady`
|`Unknown`
|The CRDs are not installed yet.
|===

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/verifying-gateway-infrastructure-status.adoc
//
[id="gateway-listener-status-conditions_{context}"]
= Gateway and listener status conditions reference

[role="_abstract"]
To verify that your gateway is configured in the data plane and ready to route traffic, review its gateway-level and listener-level `status` conditions. A healthy `Gateway` custom resource (CR) reports a status of `True` for its `Accepted` and `Programmed` conditions.

[IMPORTANT]
====
The `Conflicted` listener condition uses negative polarity. This means that a status of `False` indicates a healthy state, while a status of `True` indicates an error.
====

.Gateway-level status conditions
[cols="1,1,3",options="header"]
|===
|Condition |Status |Description and common reasons

|`Accepted`
|`True`
|The gateway configuration is valid and working properly.

|`Accepted`
|`False`
|The configuration has errors. Common reasons include `ListenersNotValid` (one or more listeners have issues) or `InvalidParameters` (the configuration is invalid).

|`Accepted`
|`Unknown`
|The controller has not evaluated the gateway yet.

|`Programmed`
|`True`
|The infrastructure is provisioned and the gateway is configured in the data plane, such as a load balancer or proxy.

|`Programmed`
|`False`
|Programming failed or the data plane is not ready. Common reasons include `NoResources` (insufficient resources or pods unavailable), `Invalid` (cannot apply to the data plane), or `Pending`.

|`Programmed`
|`Unknown`
|Programming is currently in progress.

|`LoadBalancerReady`
|`True`
|The cloud load balancer service for the gateway is successfully provisioned.

|`LoadBalancerReady`
|`False`
|The load balancer service failed to provision or is pending. Common reasons include `ServiceNotFound`, `LoadBalancerPending`, or `SyncLoadBalancerFailed`.

|`DNSReady`
|`True`
|DNS records for all listeners are functioning correctly.

|`DNSReady`
|`False`
|One or more listeners have DNS provisioning issues.
|===

.Listener-level status conditions
[cols="1,1,3",options="header"]
|===
|Condition |Status |Description and common reasons

|`Accepted`
|`True`
|The listener configuration is valid and working properly.

|`Accepted`
|`False`
|The listener configuration has errors.

|`Programmed`
|`True`
|The listener is successfully configured in the data plane.

|`Programmed`
|`False`
|The listener configuration failed in the data plane.

|`ResolvedRefs`
|`True`
|All references, such as TLS certificates, are found and valid.

|`ResolvedRefs`
|`False`
|At least one reference is invalid. Common reasons include `InvalidCertificateRef` (a TLS certificate was not found or is invalid) or `RefNotPermitted` (a cross-namespace reference is not allowed).

|`Conflicted` (Negative polarity)
|`False`
|Healthy state. There are no conflicts.

|`Conflicted` (Negative polarity)
|`True`
|The listener conflicts with another listener. Common reasons include `ProtocolConflict` (multiple listeners on the same port with incompatible protocols) or `HostnameConflict` (overlapping hostnames).

|`DNSReady`
|`True`
|The DNS record for this listener's hostname is successfully provisioned in all reported zones.

|`DNSReady`
|`False`
|The DNS record failed to provision. Common reasons include `FailedZones`, `NoDNSZones`, or `RecordNotFound`.

|`DNSReady`
|`Unknown`
a|The DNS status cannot be determined or is unmanaged.

[NOTE]
====
Listeners without a configured hostname will not have DNS conditions added to their `status`.
====
|===

.Example `Gateway` CR status output showing a DNS failure on one listener
[source,yaml]
----
# ...
status:
  # Gateway-level conditions (LoadBalancer and aggregate DNS status)
  conditions:
  - type: LoadBalancerReady
    status: "True"
    reason: LoadBalancerProvisioned
    message: "The LoadBalancer service is provisioned"
    observedGeneration: 1
    lastTransitionTime: "2025-01-12T10:00:00Z"
  - type: DNSReady
    status: "False"
    reason: SomeListenersNotReady
    message: "One or more listeners have DNS provisioning issues"
    observedGeneration: 1
    lastTransitionTime: "2025-01-12T10:00:00Z"

  # Listener-level conditions (DNS status per listener)
  listeners:
  - name: <stage_http>
    conditions:
    - type: DNSReady
      status: "True"
      reason: NoFailedZones
      message: "The record is provisioned in all reported zones."
      observedGeneration: 1
      lastTransitionTime: "2025-01-12T10:00:00Z"
  - name: <prod_https>
    conditions:
    - type: DNSReady
      status: "False"
      reason: FailedZones
      message: "The record failed to provision in some zones: [<prod.example.com>]"
      observedGeneration: 1
      lastTransitionTime: "2025-01-12T10:00:00Z"
----

[NOTE]
====
For {gcp-first} installations, you can use a custom DNS solution. You must manually create a DNS record for any gateways in Gateway API. For more information, see "Installing a cluster on {gcp-short} with customizations".
====

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/verifying-gateway-infrastructure-status.adoc
//
[id="querying-gateway-status-cli_{context}"]
= Query Gateway infrastructure status using the CLI

[role="_abstract"]
To quickly check the health of your gateway infrastructure, query specific `status` fields using the OpenShift Container Platform CLI. You can validate your deployment, check route attachments, and retrieve IP addresses without parsing lengthy YAML manifests.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {oc-first}.
* Your gateway is deployed in the `openshift-ingress` namespace.
* Your gateway is managed by the gateway controller (`openshift.io/gateway-controller/v1`).

.Procedure

* Run the relevant command for the status information you need to retrieve:
+
--
** To list all `GatewayClass` custom resources (CRs) in your cluster, run the following command:
+
[source,terminal]
----
$ oc get gatewayclass
----

** To check if a specific `GatewayClass` CR has been accepted by the controller, run the following command:
+
[source,terminal]
----
$ oc get gatewayclass <gatewayclass_name> -o jsonpath='{.status.conditions[?(@.type=="Accepted")].status}'
----
*** `<gatewayclass_name>`: Specify the name of your gateway class.

** To list all `Gateway` custom resources (CRs) across all namespaces, run the following command:
+
[source,terminal]
----
$ oc get gateway -A
----

** To check if a specific `Gateway` CR is successfully programmed in the data plane, run the following command:
+
[source,terminal]
----
$ oc get gateway <gateway_name> -n openshift-ingress -o jsonpath='{.status.conditions[?(@.type=="Programmed")].status}'
----
*** `<gateway_name>`: Specify the name of your gateway.

** To retrieve the IP address assigned to a specific `Gateway` CR, run the following command:
+
[source,terminal]
----
$ oc get gateway <gateway_name> -n openshift-ingress -o jsonpath='{.status.addresses[0].value}'
----
*** `<gateway_name>`: Specify the name of your gateway.

** To check the total number of routes attached to a specific `Gateway` CR, run the following command:
+
[source,terminal]
----
$ oc get gateway <gateway_name> -n openshift-ingress -o jsonpath='{.status.listeners[*].attachedRoutes}'
----
*** `<gateway_name>`: Specify the name of your gateway.

** To watch a specific `Gateway` CR for real-time status changes, run the following command:
+
[source,terminal]
----
$ oc get gateway <gateway_name> -n openshift-ingress -w
----
*** `<gateway_name>`: Specify the name of your gateway.
--
