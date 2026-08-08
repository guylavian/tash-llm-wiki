---
title: "Installing the eBPF Manager Operator"
type: reference
domain: openshift
slug: networking-4-22-ebpf-manager-operator-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/ebpf-manager-operator-install
version: 4.22
family: networking
documentKind: "Documentation"
---

# Installing the eBPF Manager Operator

[id="bpfman-operator-install"]
= Installing the eBPF Manager Operator

[role="_abstract"]
To manage eBPF programs across your cluster nodes, you can install the eBPF Manager Operator by using the OpenShift Container Platform CLI or the web console. This Operator provides a standardized way to deploy, monitor, and secure eBPF-based networking and observability tools.

// Module included in the following assemblies:
//
// * networking/network_security/ebpf_manager/ebpf-manager-operator-install.adoc

[id="nw-bpfman-operator-installing-cli_{context}"]
= Installing the eBPF Manager Operator using the CLI

[role="_abstract"]
To manage eBPF programs across your cluster nodes, you can install the eBPF Manager Operator by using the OpenShift Container Platform CLI. This process involves creating a dedicated namespace and subscribing to the Operator to enable node-level networking and observability tools.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have an account with administrator privileges.

.Procedure

. To create the `bpfman` namespace, enter the following command:
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
  name: bpfman
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
  name: bpfman-operators
  namespace: bpfman
EOF
----

. Subscribe to the eBPF Manager Operator.

.. To create a `Subscription` CR for the eBPF Manager Operator, enter the following command:
+
[source,terminal]
----
$ cat << EOF| oc create -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: bpfman-operator
  namespace: bpfman
spec:
  name: bpfman-operator
  channel: alpha
  source: community-operators
  sourceNamespace: openshift-marketplace
EOF
----

. To verify that the Operator is installed, enter the following command:
+
[source,terminal]
----
$ oc get ip -n bpfman
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME            CSV                                 APPROVAL    APPROVED
install-ppjxl   security-profiles-operator.v0.8.5   Automatic   true
----

. To verify the version of the Operator, enter the following command:

+
[source,terminal]
----
$ oc get csv -n bpfman
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                DISPLAY                      VERSION   REPLACES                            PHASE
bpfman-operator.v0.5.0              eBPF Manager Operator              0.5.0     bpfman-operator.v0.4.2              Succeeded
----

// Module included in the following assemblies:
//
// * networking/network_security/ebpf_manager/ebpf-manager-operator-install.adoc

Operator Hub capitalizes all Operator names; officially, it is eBPF Manager though.

[id="nw-bpfman-operator-installing-console_{context}"]
= Installing the eBPF Manager Operator using the web console

[role="_abstract"]
To manage eBPF programs across your cluster nodes, you can install the eBPF Manager Operator by using the OpenShift Container Platform web console. You can use the eBPF Manager Operator to enable node-level networking and observability tools through the OperatorHub interface.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have an account with administrator privileges.

.Procedure

. Install the eBPF Manager Operator:

.. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

.. Select *eBPF Manager Operator* from the list of available Operators, and if prompted to *Show community Operator*, click *Continue*.

.. Click *Install*.

.. On the *Install Operator* page, under *Installed Namespace*, select *Operator recommended Namespace*.

.. Click *Install*.

. Verify that the eBPF Manager Operator is installed successfully:

.. Navigate to the *Ecosystem* -> *Installed Operators* page.

.. Ensure that *eBPF Manager Operator* is listed in the *openshift-ingress-node-firewall* project with a *Status* of *InstallSucceeded*.
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
* Navigate to the *Workloads* -> *Pods* page and check the logs for pods in the `bpfman` project.

[role="_additional-resources"]
.Additional resources

* Deploying a containerized eBPF program
* Configuring Ingress Node Firewall Operator to use the eBPF Manager Operator
