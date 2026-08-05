---
title: "Control incoming traffic with gateway listeners"
type: reference
domain: openshift
slug: networking-4-22-controlling-incoming-traffic-gateway-listeners-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/controlling-incoming-traffic-gateway-listeners
version: 4.22
family: networking
documentKind: "Documentation"
---

# Control incoming traffic with gateway listeners

[id="controlling-incoming-traffic-gateway-listeners"]
= Control incoming traffic with gateway listeners

[role="_abstract"]
To control network traffic flow, you can configure Gateway API listeners to define the designated port, protocol, and hostname for your gateway. By configuring listeners, you can specify secure TLS connections, dictate how traffic is terminated, and restrict which application routes are permitted to attach to the gateway.

To successfully manage your incoming traffic with gateway listeners, complete the following tasks:

* Configure listener routing and security settings to define the ports, protocols, hostnames, and TLS certificates for your incoming traffic.
* Understand listener routing conflicts by applying conflict management rules to ensure overlapping hostnames or ports are routed correctly.
* Troubleshoot listener connections by monitoring listener status conditions to identify and resolve configuration errors.

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/controlling-incoming-traffic-gateway-listeners.adoc
//
[id="configuring-listener-routing-security_{context}"]
= Configure listener routing and security settings

[role="_abstract"]
To ensure that your applications receive only authenticated and authorized traffic, you must specify the allowed protocols and ports for your gateway. If you are routing secure traffic, you must also configure TLS settings. You can define these parameters by configuring the `spec.listeners` field in your `Gateway` custom resource (CR).

.Procedure

. Create or edit a `Gateway` YAML file to include your desired listener configuration.
+
--
The following example demonstrates a `Gateway` CR with two listeners, one for HTTP and one for HTTPS. For detailed descriptions of the listener fields, see .

[source,yaml]
----
kind: Gateway
apiVersion: gateway.networking.k8s.io/v1
metadata:
  name: <example_gateway>
  namespace: openshift-ingress
spec:
  gatewayClassName: openshift-default
  listeners:
  - protocol: HTTP
    port: 80
    name: http
    allowedRoutes:
      namespaces:
        from: Selector
        selector:
          matchLabels:
            env: "dev"
  - protocol: HTTPS
    port: 443
    name: https
    hostname: "*.<example_domain.tld>"
    tls:
      mode: Terminate
      certificateRefs:
        - name: <listener_cert>
          kind: Secret
    allowedRoutes:
      namespaces:
        from: All
----
--

. Apply the `Gateway` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <gateway_cr>.yaml
----

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/controlling-incoming-traffic-gateway-listeners.adoc
//
[id="gateway-listener-configuration-reference_{context}"]
= Gateway listener configuration reference

[role="_abstract"]
When configuring the `spec.listeners` field in your `Gateway` custom resource (CR), you can define network protocols, ports, hostnames, TLS termination, and route attachment policies.

You can customize your gateway listener configuration using the following fields:

`spec.listeners`::
Defines the list of listeners for the gateway. You can customize this field with settings for port, protocol, TLS, hostnames, and allowed routes.

`listeners.protocol` and `listeners.port`::
Defines the network port and protocol. For example, `protocol: HTTP` accepts HTTP traffic on port `80`, and `protocol: HTTPS` accepts HTTPS traffic on port `443`.

`listeners.hostname`::
Defines the hostnames that the listener matches for incoming requests. For example, it can match only requests for hostnames ending in `<example_domain.tld>` (such as `www.<example_domain.tld>`). If no hostname is specified, the gateway routes any traffic that can attach to it.

`listeners.tls`::
Specifies the TLS settings for secure communication, including the mode (currently, only `Terminate` is supported on OpenShift Container Platform) and the Kubernetes secret containing the certificate keypair. For example, TLS is terminated at the gateway using a certificate stored in a Kubernetes `Secret` called `<listener_cert>`. You must ensure that the specified Kubernetes secret exists before you create the `Gateway` CR.

`listeners.allowedRoutes`::
Controls which `Route` resources can attach to this listener. For example, an HTTP listener might only allow `HTTPRoute` resources from namespaces that have the `env: "dev"` label (using `Selector`), while an HTTPS listener might allow `HTTPRoute` resources from any namespace to attach (using `All`). Setting `allowedRoutes.namespaces.from: Same` is not supported; routes from the same namespace as the gateway are always allowed.

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/controlling-incoming-traffic-gateway-listeners.adoc
//
[id="resolving-listener-routing-conflicts_{context}"]
= Understand listener routing conflicts

[role="_abstract"]
When you configure a `Gateway` custom resource (CR) with multiple listeners, you must establish clear rules for overlapping hostnames and ports to ensure your traffic does not get misrouted. To avoid ambiguity, the Gateway API uses specific conflict management rules.

If your listener configurations violate these rules, the affected listener receives a `Conflicted` status condition and cannot route traffic correctly.

To resolve or prevent routing conflicts, ensure that your listeners adhere to the following rules:

* Distinct ports: A gateway can have distinct listeners that use the exact same hostname, provided their network ports are distinct.
* Distinct hostnames: A gateway can have distinct listeners that use the exact same protocol and port, provided their hostnames are different.
* Specificity precedence: If one listener uses a wildcard domain (for example, `+++*+++.<example_domain.tld>`) and another listener uses a more specific endpoint for that exact same domain (for example, `<www.example_domain.tld>`), the more specific entry takes precedence.
+
This specificity rule also applies to multiple wildcard domains. For example, `+++*+++.<example_domain.tld>` takes precedence over `+++*+++.<tld>`. This ensures that traffic intended for a specific subdomain is accurately routed to its dedicated listener, even if a broader wildcard listener exists.
+
[NOTE]
====
In the Gateway API, wildcards match one or more complete DNS labels. For example, `+++*+++.<example.com>` matches `<www.example.com>` and `<sub.domain.example.com>`, but does not match the root domain `<example.com>`.
====

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/controlling-incoming-traffic-gateway-listeners.adoc
//
[id="troubleshooting-listener-conditions_{context}"]
= Troubleshoot listener connections using status conditions

[role="_abstract"]
When a listener is not routing traffic as expected, you can review its `status` conditions to quickly diagnose and fix the configuration error. The listener `status` condition gives insight into its current state and any underlying issues preventing it from accepting traffic.

.Procedure

. Check the `status` conditions of your `Gateway` custom resource (CR) by running the following command:
+
[source,terminal]
----
$ oc describe gateway <gateway_cr> -n <namespace>
----
* `<gateway_cr>`: Specify the name of your gateway.
* `<namespace>`: Specify the namespace where the gateway resides.
+
For details on how to interpret the output and resolve common errors, see .

// Module included in the following assemblies:
//
// * networking/ingress_load_balancing/configuring_ingress_cluster_traffic/controlling-incoming-traffic-gateway-listeners.adoc
//
[id="gateway-listener-troubleshooting-reference_{context}"]
= Gateway listener troubleshooting reference

[role="_abstract"]
When you troubleshoot your gateway listeners, you can review the status conditions in the `Gateway` custom resource (CR) output to identify configuration errors or conflicts.

The following table describes common listener conditions and how to resolve them:

.Gateway listener status conditions
[cols="1,3",options="header"]
|===
|Condition |Description

|`Ready`
|Indicates that the listener is configured correctly and is actively listening for traffic.

|`Conflicted`
|Signifies an ambiguity or conflict in the listener's configuration with another listener on the same gateway. If a listener is conflicted, review your listener configurations against the conflict management rules to identify and resolve the ambiguity.

|`Programmed`
|Denotes that the underlying infrastructure, such as a load balancer or proxy, has successfully been programmed with the listener's configuration.

|`Accepted`
|Indicates that the gateway has accepted the listener's configuration. This is usually an early step in the listener's lifecycle.

|`Invalid`
|Means the listener's configuration itself contains errors or is malformed, preventing it from being processed. An invalid status indicates errors in your YAML configuration. Check your configuration for typos, incorrect syntax, or missing required fields.
|===

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Gateway API documentation: Protocol-specific distinctiveness rules
* Gateway API documentation: Hostnames
