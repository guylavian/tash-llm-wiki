---
title: "Assign network addresses to gateways"
type: reference
domain: openshift
slug: networking-4-22-assigning-network-addresses-gateways
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/assigning-network-addresses-gateways
version: 4.22
family: networking
documentKind: "Documentation"
---

# Assign network addresses to gateways

[id="assigning-network-addresses-gateways"]
= Assigning network addresses to gateways

[role="_abstract"]
You can configure network addresses for your gateway to provide a predictable entry point for external traffic. This ensures that clients can reliably resolve and route requests to your load balancers.

The Gateway API uses addresses to define the specific network locations that are assigned to your `Gateway` resource. In OpenShift Container Platform, you rely on the Gateway controller to automatically provision and bind the necessary network addresses, such as an external load balancer IP, to your gateway. The controller then populates the `status.addresses` field of the `Gateway` resource with the assigned addresses once they are available.

To successfully assign network addresses to your gateway, complete the following tasks:

* Understand gateway address assignment and types to plan your DNS and load balancer configuration.
* Configure automatic address assignment for a gateway to successfully deploy it without violating manual address constraints.

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/assigning-network-addresses-gateways.adoc
//
[id="understand-gateway-address-assignment_{context}"]
= Understand gateway address assignment and types

[role="_abstract"]
OpenShift Container Platform automatically handles address assignment by provisioning a `LoadBalancer` service when you create a `Gateway` resource. The network address assigned to your gateway corresponds to the IP address or hostname of this underlying load balancer.

[IMPORTANT]
====
Do not define the `spec.addresses` field. Manually requesting specific network addresses is not currently supported in OpenShift Container Platform. If you attempt to request a specific address manually, the gateway enters an error state.

The `status.addresses` field is populated automatically by the gateway controller. This field lists the actual, active network address assigned to your gateway by the load balancing infrastructure.
====

== Address types

When the controller dynamically assigns an address to your gateway and populates the `status.addresses` field, it uses one of the following primary types to reflect the underlying load balancer:

`Hostname`::
Represents a DNS-based ingress point. This concept is typically used for cloud load balancers where a DNS name exposes the load balancer.

`IPAddress`::
A textual representation of a numeric IP address (IPv4 or IPv6) assigned by the load balancing infrastructure.

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/assigning-network-addresses-gateways.adoc
//
[id="configuring-automatic-address-assignment-gateway_{context}"]
= Configure automatic address assignment for a gateway

[role="_abstract"]
When you create a gateway resource, you must configure it for automatic address provisioning to successfully deploy the gateway without violating OpenShift Container Platform manual address constraints. By intentionally omitting the addresses field, you allow the controller to seamlessly provision and bind the necessary external network addresses to your gateway.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {oc-first}.
* You have an existing `GatewayClass` resource, such as `openshift-default`.

.Procedure

. Create a YAML file, such as `hello-gateway.yaml`, that defines your `Gateway` object without the addresses field:
+
[source,yaml]
----
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: sample-gateway
  namespace: openshift-ingress
spec:
  gatewayClassName: openshift-default
  listeners:
  - name: http
    hostname: "*.gwapi.<cluster_domain>"
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: All
----
+
* `metadata.name`: The name of your `Gateway` object. The name must consist of a maximum of 63 lowercase alphanumeric characters or hyphens (`-`). The name must also start and end with an alphanumeric character.
* Replace `<cluster_domain>` with your actual cluster ingress domain (for example, `example.com`).
* The `spec.addresses` field is omitted from this configuration to ensure automatic assignment.
* The `gatewayClassName` dictates which controller provisions the address and populates the `status.addresses` field.

. Apply the `Gateway` configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f hello-gateway.yaml
----

. Verify that the controller automatically assigned an address to your gateway by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress get gateway sample-gateway
----
+
.Example output
[source,terminal]
----
NAME             CLASS               ADDRESS             PROGRAMMED   AGE
sample-gateway   openshift-default   <gateway_address>   True         6m16s
----
+
The `ADDRESS` column in the output displays the dynamically provisioned network address for your gateway.
