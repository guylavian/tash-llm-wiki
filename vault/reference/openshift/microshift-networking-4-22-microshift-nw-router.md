---
title: "Understanding and configuring the router"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-nw-router
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-nw-router
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Understanding and configuring the router

[id="microshift-understanding-and-configuring-router"]
= Understanding and configuring the router

[role="_abstract"]
To control how external traffic reaches your applications and limit ingress exposure in {microshift-short}, you can configure router listen addresses, ports, IP bindings, and route admission policy.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-nw-router.adoc

[id="microshift-about-router-config_{context}"]
= About configuring the router

[role="_abstract"]
To make ingress optional, you can configure {microshift-short} ingress router settings to manage which ports, if any, are exposed to network traffic. Specified routing is an example of ingress load balancing.

* The default ingress router is always on, running on all IP addresses on the `http: 80` and `https: 443` ports.
* Default router settings allow access to any namespace.

Some applications running on top of {microshift-short} might not require the default router and instead create their own. You can configure the router to control both ingress and namespace access.

[TIP]
====
You can check for the presence of the default router in your {microshift-short} installation before you begin configurations by using the `oc get deployment -n openshift-ingress` command, which returns the following output:

[source,terminal]
----
NAME             READY   UP-TO-DATE   AVAILABLE   AGE
router-default   1/1     1            1           2d23h
----
====

// Module included in the following assemblies:
//
// * microshift_networking/microshift-nw-router.adoc

[id="microshift-router-csettings_{context}"]
= Router settings and valid values

[role="_abstract"]
Valid values and defaults for ingress router fields in the `config.yaml` file on {microshift-short} cover `listenAddress`, `ports`, `routeAdmissionPolicy`, and `status`.

.Example `config.yaml` router settings
[source,yaml]
----
# ...
ingress:
  listenAddress:
    - ""
  ports:
    http: 80
    https: 443
  routeAdmissionPolicy:
    namespaceOwnership: InterNamespaceAllowed
  status: Managed
# ...
----
where:

`ingress.listenAddress`:: Specifies the single IP address or host name or a list of IP addresses or host names. The default value is the entire network of the host.

`ingress.ports`:: Specifies a single, unique port in the `1` to `65535` range. The values of the `ports.http` and `ports.https` fields cannot be the same.

`ingress.routeAdmissionPolicy.namespaceOwnership`:: Specifies whether routes can claim different paths of the same host name across namespaces. The default value is `InterNamespaceAllowed`.

`ingress.status`:: Specifies whether the ingress ports remain open. The default value is `Managed`.

[IMPORTANT]
====
The firewalld service is bypassed by the default {microshift-short} router and by configurations that enable the router. Ingress and egress must be controlled by setting network policies when the router is active.
====

// Module included in the following assemblies:
//
// * microshift_networking/microshift-nw-router.adoc

[id="microshift-disabling-the-router_{context}"]
= Disabling the router

[role="_abstract"]
To disable the router in {microshift-short} when inbound services are not required, including in industrial IoT environments where pods connect only to southbound operational systems and northbound cloud-data systems, set `ingress.status` to `Removed` in the `config.yaml` file and restart the service.

.Prerequisites

* You installed {microshift-short}.
* You created a {microshift-short} `config.yaml` file.
* The {oc-first} is installed.

[TIP]
====
If you complete all the configurations that you need to make in the {microshift-short} `config.yaml` file at the same time, you can minimize system restarts.
====

.Procedure

. Update the value of `ingress.status` field to `Removed` in the {microshift-short} `config.yaml` file as shown in the following example:
+
.Example `config.yaml` ingress stanza
[source,yaml]
----
# ...
ingress:
  ports:
    http: 80
    https: 443
  routeAdmissionPolicy:
    namespaceOwnership: InterNamespaceAllowed
  status: Removed
# ...
----
+
where:
+
--
`ingress.status`:: Specifies whether the ingress ports remain open. When the value is set to `Removed`, the ports listed in `ingress.ports` are automatically closed. Any other settings in the `ingress` stanza are ignored, for example, any values in the `routeAdmissionPolicy.namespaceOwnership` field.
--

. Restart the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----
+
[NOTE]
====
The {microshift-short} service outputs current configurations during restarts.
====

.Verification
* After the system restarts, verify that the router has been removed and that ingress is stopped by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress get svc
----
+
.Expected output
[source,text]
----
No resources found in openshift-ingress namespace.
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-nw-router.adoc

[id="microshift-configuring-router-ingress_{context}"]
= Configuring router ingress

[role="_abstract"]
Configure the `listenAddress` setting if your {microshift-short} applications need to listen only for data traffic. You can also configure specific ports and IP addresses for network connections. Use the combination required to customize the endpoint configuration for your use case.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-nw-router.adoc

[id="microshift-config-router-ports_{context}"]
= Configuring router ports

[role="_abstract"]
To bind the ingress router to specific HTTP and HTTPS port numbers in {microshift-short}, you can edit the `ingress.ports.http` and `ingress.ports.https` settings in `config.yaml` file.

.Prerequisites

* You installed {microshift-short}.
* You created a {microshift-short} `config.yaml` file.
* The {oc-first} is installed.

[TIP]
====
If you complete all the configurations that you need to make in the {microshift-short} `config.yaml` file at the same time, you can minimize system restarts.
====

.Procedure

. Update the {microshift-short} `config.yaml` port values in the `ingress.ports.http` and `ingress.ports.https` fields to the ports you want to use:
+
.Example `config.yaml` router settings
[source,yaml]
----
# ...
ingress:
  ports:
    http: 80
    https: 443
  routeAdmissionPolicy:
    namespaceOwnership: InterNamespaceAllowed
  status: Managed
# ...
----
+
where:
+
--
`ingress.ports`:: Specifies the HTTP and HTTPS port numbers to bind the ingress router to. This field is customizable. Valid values for both port entries are a single, unique port in the 1-65535 range. The values of the `ports.http` and `ports.https` fields cannot be the same.
`status`:: Specifies the status of the ingress ports. The default value is `Managed`. `Managed` is required for the ingress ports to remain open.
--

. Restart the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-nw-router.adoc

[id="microshift-config-ip-addresses_{context}"]
= Configuring router IP addresses

[role="_abstract"]
To limit ingress to selected host IP addresses or network interfaces in {microshift-short}, you can set the `ingress.listenAddress` list in your `config.yaml` file.

You can restrict the network traffic to the router by configuring specific IP addresses. For example:

* Use cases where the router is reachable only on internal networks, but not on northbound public networks
* Use cases where the router is reachable only by northbound public networks, but not on internal networks
* Use cases where the router is reachable by both internal networks and northbound public networks, but on separate IP addresses

.Prerequisites

* You installed {microshift-short}.
* You created a {microshift-short} `config.yaml` file.
* The {oc-first} is installed.

[TIP]
====
If you complete all the configurations that you need to make in the {microshift-short} `config.yaml` file at the same time, you can minimize system restarts.
====

.Procedure

. Update the list in the `ingress.listenAddress` field in the {microshift-short} `config.yaml` according to your requirements and as shown in the following examples:
+
.Default router IP address list
[source,yaml]
----
# ...
ingress:
  listenAddress:
    - "<host_network>"
# ...
----
+
where:
+
--
`ingress.listenAddress`:: Specifies the IP addresses or network interfaces to limit ingress to. The default value is the entire network of the host. To continue to use the default list, remove the `listen.Address` field from the {microshift-short} `config.yaml` file. To customize this parameter, use a list. The list can contain either a single IP address or NIC name or multiple IP addresses and NIC names.
--
+
[IMPORTANT]
====
You must either remove the `listenAddress` parameter or add values to it in the form of a list when using the `config.yaml` file. Do not leave the field empty or {microshift-short} crashes on restart.
====
+
.Example router setting with a single host IP address
[source,yaml]
----
# ...
ingress:
  listenAddress:
    - 10.2.1.100
# ...
----
+
.Example router setting with a combination of IP addresses and NIC names
[source,yaml]
----
# ...
ingress:
  listenAddress:
    - 10.2.1.100
    - 10.2.2.10
    - ens3
# ...
----

. Restart the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

.Verification

* To verify that your settings are applied, make sure that the `ingress.listenAddress` IP addresses are reachable, then you can `curl` the route with the destination to one of these load balancer IP address.

[id="additional-resources_microshift-understanding-and-configuring-router_{context}"]
[role="_additional-resources"]
== Additional resources

* About the default {microshift-short} configuration file
* About network policies

// Module included in the following assemblies:
//
// * microshift_networking/microshift-nw-router.adoc

[id="microshift-configuring-route-admission_{context}"]
= Configuring the route admission policy

[role="_abstract"]
By default, {microshift-short} allows routes in multiple namespaces to use the same hostname. To prevent routes from claiming the same hostname in different namespaces, you can configure the route admission policy.

.Prerequisites

* You installed {microshift-short}.
* You created a {microshift-short} `config.yaml` file.
* You installed the {oc-first}.
+
[TIP]
====
If you complete all the configurations that you need to make in the {microshift-short} `config.yaml` file at the same time, you can minimize system restarts.
====

.Procedure

. To prevent routes in different namespaces from claiming the same hostname, update the `namespaceOwnership` field value to `Strict` in the {microshift-short} `config.yaml` file. See the following example:
+
.Example `config.yaml` route admission policy
[source,yaml]
----
# ...
ingress:
  routeAdmissionPolicy:
    namespaceOwnership: Strict
# ...
----
+
where:
+
--
`ingress.routeAdmissionPolicy.namespaceOwnership`:: Specifies the route admission policy. Prevents routes in different namespaces from claiming the same host. Valid values are `Strict` and `InterNamespaceAllowed`. If you delete the value in a customized `config.yaml`, the `InterNamespaceAllowed` value is set automatically.
--

. To apply the configuration, restart the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----
