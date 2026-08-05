---
title: "Ingress Node Firewall Operator in {product-title}"
type: reference
domain: openshift
slug: networking-4-22-ingress-node-firewall-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/ingress-node-firewall-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# Ingress Node Firewall Operator in {product-title}

[id="ingress-node-firewall-operator"]
= Ingress Node Firewall Operator in OpenShift Container Platform

[role="_abstract"]
The Ingress Node Firewall Operator provides a stateless, eBPF-based firewall for managing node-level ingress traffic in OpenShift Container Platform.

// Module included in the following assemblies:
//
// * networking/ingress-node-firewall-operator.adoc

[id="nw-infw-operator-cr_{context}"]
= Ingress Node Firewall Operator

[role="_abstract"]
The Ingress Node Firewall Operator provides ingress firewall rules at a node level that you can specify and manage in the firewall configurations.

To deploy the daemon set created by the Operator, you create an `IngressNodeFirewallConfig` custom resource (CR). The Operator applies the `IngressNodeFirewallConfig` CR to create ingress node firewall daemon set `daemon`, which run on all nodes that match the `nodeSelector`.

You configure `rules` of the `IngressNodeFirewall` CR and apply them to clusters using the `nodeSelector` and setting values to "true".

[IMPORTANT]
====
The Ingress Node Firewall Operator supports only stateless firewall rules.

Network interface controllers (NICs) that do not support native XDP drivers will run at a lower performance.

For OpenShift Container Platform 4.14 or later, you must run Ingress Node Firewall Operator on {op-system-base} 9.0 or later.

You must run Ingress Node Firewall Operator on OpenShift Container Platform 4.14 or later or later.
====

// Module included in the following assemblies:
//
// * networking/ingress-node-firewall-operator.adoc

[id="installing-infw-operator_{context}"]
= Installing the Ingress Node Firewall Operator

[role="_abstract"]
As a cluster administrator, you can install the Ingress Node Firewall Operator to enable node-level ingress firewalling by using the OpenShift Container Platform CLI.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have an account with administrator privileges.

.Procedure

. To create the `openshift-ingress-node-firewall` namespace, enter the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: v1
kind: Namespace
metadata:
  labels:
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/enforce-version: v1.24
  name: openshift-ingress-node-firewall
EOF
----

. To create an `OperatorGroup` CR, enter the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: ingress-node-firewall-operators
  namespace: openshift-ingress-node-firewall
EOF
----

. Subscribe to the Ingress Node Firewall Operator.
** To create a `Subscription` CR for the Ingress Node Firewall Operator, enter the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: ingress-node-firewall-sub
  namespace: openshift-ingress-node-firewall
spec:
  name: ingress-node-firewall
  channel: stable
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
----

. To verify that the Operator is installed, enter the following command:
+
[source,terminal]
----
$ oc get ip -n openshift-ingress-node-firewall
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME            CSV                                         APPROVAL    APPROVED
install-5cvnz   ingress-node-firewall..0-202211122336   Automatic   true
----

. To verify the version of the Operator, enter the following command:

+
[source,terminal]
----
$ oc get csv -n openshift-ingress-node-firewall
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                        DISPLAY                          VERSION               REPLACES                                    PHASE
ingress-node-firewall..0-202211122336   Ingress Node Firewall Operator   .0-202211122336   ingress-node-firewall..0-202211102047   Succeeded
----

// Module included in the following assemblies:
//
// * networking/ingress-node-firewall-operator.adoc

[id="install-operator-web-console_{context}"]
= Installing the Ingress Node Firewall Operator using the web console

[role="_abstract"]
As a cluster administrator, you can install the Ingress Node Firewall Operator to enable node-level ingress firewalling by using the web console.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have an account with administrator privileges.

.Procedure

. Install the Ingress Node Firewall Operator:

.. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

.. Select *Ingress Node Firewall Operator* from the list of available Operators, and then click *Install*.

.. On the *Install Operator* page, under *Installed Namespace*, select *Operator recommended Namespace*.

.. Click *Install*.

. Verify that the Ingress Node Firewall Operator is installed successfully:

.. Navigate to the *Ecosystem* -> *Installed Operators* page.

.. Ensure that *Ingress Node Firewall Operator* is listed in the *openshift-ingress-node-firewall* project with a *Status* of *InstallSucceeded*.
+
[NOTE]
====
During installation an Operator might display a *Failed* status.
If the installation later succeeds with an *InstallSucceeded* message, you can ignore the *Failed* message.
====

+
If the Operator does not have a *Status* of *InstallSucceeded*, troubleshoot using the following steps:

+
* Inspect the *Operator Subscriptions* and *Install Plans* tabs for any failures or errors under *Status*.
* Navigate to the *Workloads* -> *Pods* page and check the logs for pods in the `openshift-ingress-node-firewall` project.
* Check the namespace of the YAML file. If the annotation is missing, you can add the annotation `workload.openshift.io/allowed=management` to the Operator namespace with the following command:
+
[source,terminal]
----
$ oc annotate ns/openshift-ingress-node-firewall workload.openshift.io/allowed=management
----
+
[NOTE]
====
For {sno} clusters, the `openshift-ingress-node-firewall` namespace requires the `workload.openshift.io/allowed=management` annotation.
====

// Module included in the following assemblies:
//
// * networking/ingress-node-firewall-operator.adoc

[id="nw-infw-operator-deploying_{context}"]
= Deploying Ingress Node Firewall Operator

[role="_abstract"]
To deploy the Ingress Node Firewall Operator, create a `IngressNodeFirewallConfig` custom resource that will deploy the Operator's daemon set. You can deploy one or multiple `IngressNodeFirewall` CRDs to nodes by applying firewall rules.

.Prerequisite
* The Ingress Node Firewall Operator is installed.

.Procedure

. Create the `IngressNodeFirewallConfig` inside the `openshift-ingress-node-firewall` namespace named `ingressnodefirewallconfig`.

. Run the following command to deploy Ingress Node Firewall Operator rules:
+
[source,terminal]
----
$ oc apply -f rule.yaml
----

// Module included in the following assemblies:
//
// * networking/ingress-node-firewall-operator.adoc

[id="nw-infw-operator-config-object_{context}"]
= Ingress Node Firewall configuration object

[role="_abstract"]
Review configuration fields so you can define how the Operator deploys the firewall.

The fields for the Ingress Node Firewall configuration object are described in the following table:

.Ingress Node Firewall Configuration object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|The name of the CR object. The name of the firewall rules object must be `ingressnodefirewallconfig`.

|`metadata.namespace`
|`string`
|Namespace for the Ingress Firewall Operator CR object. The `IngressNodeFirewallConfig` CR must be created inside the `openshift-ingress-node-firewall` namespace.

|`spec.nodeSelector`
|`string`
|
A node selection constraint used to target nodes through specified node labels. For example:

[source,yaml]
----
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewallConfig
metadata:
  name: ingressnodefirewallconfig
  namespace: openshift-ingress-node-firewall
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
----

[NOTE]
====
One label used in `nodeSelector` must match a label on the nodes in order for the daemon set to start. For example, if the node labels `node-role.kubernetes.io/worker` and `node-type.kubernetes.io/vm` are applied to a node, then at least one label must be set using `nodeSelector` for the daemon set to start.
====

|`spec.ebpfProgramManagerMode`
|`boolean`
|
Specifies if the Node Ingress Firewall Operator uses the eBPF Manager Operator or not to manage eBPF programs. This capability is a Technology Preview feature.

For more information about the support scope of Red Hat Technology Preview features, see Technology Preview Features Support Scope.

|====

[NOTE]
====
The Operator consumes the CR and creates an ingress node firewall daemon set on all the nodes that match the `nodeSelector`.

To start, the Operator consumes an `IngressNodeFirewallConfig` in order to generate the daemonset on all nodes. After this is created, additional firewall rule objects can be created.
====

[id="nw-ingress-node-firewall-example-cr-2_{context}"]
== Ingress Node Firewall Operator example configuration

A complete Ingress Node Firewall Configuration is specified in the following example:

.Example of how to create an Ingress Node Firewall Configuration object
[source,yaml]
----
$ cat << EOF | oc create -f -
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewallConfig
metadata:
  name: ingressnodefirewallconfig
  namespace: openshift-ingress-node-firewall
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
EOF
----

[NOTE]
====
The Operator consumes the CR object and creates an ingress node firewall daemon set on all the nodes that match the `nodeSelector`.
====

// Module included in the following assemblies:
//
// * networking/ingress-node-firewall-operator.adoc

[id="nw-ingress-node-firewall-operator-rules-object_{context}"]
= Ingress Node Firewall rules object

[role="_abstract"]
You can review rule fields and examples to define which ingress traffic is allowed or denied by using the Ingress Node Firewall rules object.

The fields for the Ingress Node Firewall rules object are described in the following table:

.Ingress Node Firewall rules object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|The name of the CR object.

|`interfaces`
|`array`
|The fields for this object specify the interfaces to apply the firewall rules to. For example, `- en0` and
`- en1`.

|`nodeSelector`
|`array`
|You can use `nodeSelector` to select the nodes to apply the firewall rules to. Set the value of your named `nodeselector` labels to `true` to apply the rule.

|`ingress`
|`object`
|`ingress` allows you to configure the rules that allow outside access to the services on your cluster.
|====

[id="nw-infw-ingress-rules-object_{context}"]
== Ingress object configuration

The values for the `ingress` object are defined in the following table:

.`ingress` object
[cols=".^3,.^2,.^5a",options="header"]
|====
|Field|Type|Description

|`sourceCIDRs`
|`array`
|Allows you to set the CIDR block. You can configure multiple CIDRs from different address families.

[NOTE]
====
Different CIDRs allow you to use the same order rule. In the case that there are multiple `IngressNodeFirewall` objects for the same nodes and interfaces with overlapping CIDRs, the `order` field will specify which rule is applied first. Rules are applied in ascending order.
====

|`rules`
|`array`
|Ingress firewall `rules.order` objects are ordered starting at `1` for each `source.CIDR` with up to 100 rules per CIDR. Lower order rules are executed first.

`rules.protocolConfig.protocol` supports the following protocols: TCP, UDP, SCTP, ICMP and ICMPv6. ICMP and ICMPv6 rules can match against ICMP and ICMPv6 types or codes. TCP, UDP, and SCTP rules can match against a single destination port or a range of ports using `<start : end-1>` format.

Set `rules.action` to `allow` to apply the rule or `deny` to disallow the rule.

[NOTE]
====
Ingress firewall rules are verified using a verification webhook that blocks any invalid configuration. The verification webhook prevents you from blocking any critical cluster services such as the API server.
====
|====

[id="nw-ingress-node-firewall-example-cr_{context}"]
== Ingress Node Firewall rules object example

A complete Ingress Node Firewall configuration is specified in the following example:

.Example Ingress Node Firewall configuration
[source,yaml]
----
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewall
metadata:
  name: ingressnodefirewall
spec:
  interfaces:
  - eth0
  nodeSelector:
    matchLabels:
      <label_name>: <label_value>
  ingress:
  - sourceCIDRs:
       - 172.16.0.0/12
    rules:
    - order: 10
      protocolConfig:
        protocol: ICMP
        icmp:
          icmpType: 8 #ICMP Echo request
      action: Deny
    - order: 20
      protocolConfig:
        protocol: TCP
        tcp:
          ports: "8000-9000"
      action: Deny
  - sourceCIDRs:
       - fc00:f853:ccd:e793::0/64
    rules:
    - order: 10
      protocolConfig:
        protocol: ICMPv6
        icmpv6:
          icmpType: 128 #ICMPV6 Echo request
      action: Deny
----
+
A `<label_name>` and a `<label_value>` must exist on the node and must match the `nodeselector` label and value applied to the nodes you want the `ingressfirewallconfig` CR to run on. The `<label_value>` can be `true` or `false`. By using `nodeSelector` labels, you can target separate groups of nodes to apply different rules to using the `ingressfirewallconfig` CR.

[id="nw-ingress-node-firewall-zero-trust-example-cr_{context}"]
== Zero trust Ingress Node Firewall rules object example

Zero trust Ingress Node Firewall rules can provide additional security to multi-interface clusters. For example, you can use zero trust Ingress Node Firewall rules to drop all traffic on a specific interface except for SSH.

A complete configuration of a zero trust Ingress Node Firewall rule for a network-interface cluster is specified in the following example:

[IMPORTANT]
====
Users need to add all ports their application will use to their allowlist in the following case to ensure proper functionality.
====

.Example zero trust Ingress Node Firewall rules
[source,yaml]
----
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewall
metadata:
 name: ingressnodefirewall-zero-trust
spec:
 interfaces:
 - eth1
 nodeSelector:
   matchLabels:
     <ingress_firewall_label_name>: <label_value>
 ingress:
 - sourceCIDRs:
      - 0.0.0.0/0
   rules:
   - order: 10
     protocolConfig:
       protocol: TCP
       tcp:
         ports: 22
     action: Allow
   - order: 20
     action: Deny
----

// Module included in the following assemblies:
//
// * networking/network_security/ingress-node-firewall-operator.adoc

[id="ingress-node-firewall-operator_{context}"]
= Ingress Node Firewall Operator integration

[role="_abstract"]
Learn when to use eBPF Manager to load and manage Ingress Node Firewall programs.

The Ingress Node Firewall uses eBPF programs to implement some of its key firewall functionality. By default these eBPF programs are loaded into the kernel using a mechanism specific to the Ingress Node Firewall. You can configure the Ingress Node Firewall Operator to use the eBPF Manager Operator for loading and managing these programs instead.

When this integration is enabled, the following limitations apply:

- The Ingress Node Firewall Operator uses TCX if XDP is not available and TCX is incompatible with bpfman.
- The Ingress Node Firewall Operator daemon set pods remain in the `ContainerCreating` state until the firewall rules are applied.
- The Ingress Node Firewall Operator daemon set pods run as privileged.

// Module included in the following assemblies:
//
// * networking/network_security/ebpf_manager/ebpf-manager-operator-about.adoc

[id="bpfman-infw-configure_{context}"]
= Configuring Ingress Node Firewall Operator to use the eBPF Manager Operator

[role="_abstract"]
Configure the Ingress Node Firewall to use eBPF Manager for program lifecycle control.

The Ingress Node Firewall uses eBPF programs to implement some of its key firewall functionality. By default these eBPF programs are loaded into the kernel using a mechanism specific to the Ingress Node Firewall.

As a cluster administrator, you can configure the Ingress Node Firewall Operator to use the eBPF Manager Operator for loading and managing these programs instead, adding additional security and observability functionality.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have an account with administrator privileges.
* You installed the Ingress Node Firewall Operator.
* You have installed the eBPF Manager Operator.

.Procedure

. Apply the following labels to the `ingress-node-firewall-system` namespace:
+
[source,terminal]
----
$ oc label namespace openshift-ingress-node-firewall \
    pod-security.kubernetes.io/enforce=privileged \
    pod-security.kubernetes.io/warn=privileged --overwrite
----

. Edit the `IngressNodeFirewallConfig` object named `ingressnodefirewallconfig` and set the `ebpfProgramManagerMode` field:
+
.Ingress Node Firewall Operator configuration object
[source,yaml]
----
apiVersion: ingressnodefirewall.openshift.io/v1alpha1
kind: IngressNodeFirewallConfig
metadata:
  name: ingressnodefirewallconfig
  namespace: openshift-ingress-node-firewall
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  ebpfProgramManagerMode: <ebpf_mode>
----
+
--
where:

`<ebpf_mode>`: Specifies whether or not the Ingress Node Firewall Operator uses the eBPF Manager Operator to manage eBPF programs. Must be either `true` or `false`. If unset, eBPF Manager is not used.
--

// Module included in the following assemblies:
//
// * networking/ingress-node-firewall-operator.adoc

[id="nw-infw-operator-viewing_{context}"]
= Viewing Ingress Node Firewall Operator rules

[role="_abstract"]
Inspect existing rules and configs to confirm the firewall is applied as intended.

.Procedure

. Run the following command to view all current rules :
+
[source,terminal]
----
$ oc get ingressnodefirewall
----

. Choose one of the returned `<resource>` names and run the following command to view the rules or configs:
+
[source,terminal]
----
$ oc get <resource> <name> -o yaml
----

// Module included in the following assemblies:
//
// * networking/ingress-node-firewall-operator.adoc

[id="nw-infw-operator-troubleshooting_{context}"]
= Troubleshooting the Ingress Node Firewall Operator

[role="_abstract"]
You can verify the status and view the logs to diagnose ingress firewall deployment or rule issues.

.Procedure

* Run the following command to list installed Ingress Node Firewall custom resource definitions (CRD):
+
[source,terminal]
----
$ oc get crds | grep ingressnodefirewall
----
+
.Example output
[source,terminal]
----
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
ingressnodefirewallconfigs.ingressnodefirewall.openshift.io       2022-08-25T10:03:01Z
ingressnodefirewallnodestates.ingressnodefirewall.openshift.io    2022-08-25T10:03:00Z
ingressnodefirewalls.ingressnodefirewall.openshift.io             2022-08-25T10:03:00Z
----

* Run the following command to view the state of the Ingress Node Firewall Operator:
+
[source,terminal]
----
$ oc get pods -n openshift-ingress-node-firewall
----
+
.Example output
[source,terminal]
----
NAME                                       READY  STATUS         RESTARTS  AGE
ingress-node-firewall-controller-manager   2/2    Running        0         5d21h
ingress-node-firewall-daemon-pqx56         3/3    Running        0         5d21h
----
+
The following fields provide information about the status of the Operator:
`READY`, `STATUS`, `AGE`, and `RESTARTS`. The `STATUS` field is `Running` when the Ingress Node Firewall Operator is deploying a daemon set to the assigned nodes.

* Run the following command to collect all ingress firewall node pods' logs:
+
[source,terminal]
----
$ oc adm must-gather – gather_ingress_node_firewall
----
+
The logs are available in the sos node's report containing eBPF `bpftool` outputs at `/sos_commands/ebpf`. These reports include lookup tables used or updated as the ingress firewall XDP handles packet processing, updates statistics, and emits events.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* About the eBPF Manager Operator
