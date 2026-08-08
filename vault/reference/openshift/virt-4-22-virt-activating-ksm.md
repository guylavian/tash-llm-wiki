---
title: "Activating kernel samepage merging (KSM)"
type: reference
domain: openshift
slug: virt-4-22-virt-activating-ksm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-activating-ksm
version: 4.22
family: virt
documentKind: "Documentation"
---

# Activating kernel samepage merging (KSM)

[id="virt-activating-ksm"]
= Activating kernel samepage merging (KSM)

[role="_abstract"]
{VirtProductName} can activate kernel samepage merging (KSM) when nodes are overloaded. KSM deduplicates identical data found in the memory pages of virtual machines (VMs). If you have very similar VMs, KSM can make it possible to schedule more VMs on a single node.

[IMPORTANT]
====
You must only use KSM with trusted workloads.
====

[role="_prerequisites"]
[id="prerequisites_{context}"]
== Prerequisites
* Ensure that an administrator has configured KSM support on any nodes where you want {VirtProductName} to activate KSM.

// Module included in the following assembly:
//
// * virt/virtual_machines/advanced_vm_management/virt-activating-ksm.adoc
//

[id="virt-about-ksm_{context}"]
= About using {VirtProductName} to activate KSM

[role="_abstract"]
You can configure {VirtProductName} to activate kernel samepage merging (KSM) when nodes experience memory overload.

[id="virt-ksm-configuration-methods"]
== Configuration methods

You can enable or disable the KSM activation feature for all nodes by using the OpenShift Container Platform web console or by editing the `HyperConverged` custom resource (CR). The `HyperConverged` CR supports more granular configuration.

[id="virt-ksm-cr-configuration"]
CR configuration::
+
You can configure the KSM activation feature by editing the `spec.configuration.ksmConfiguration` stanza of the `HyperConverged` CR.
+
--
* You enable the feature and configure settings by editing the `ksmConfiguration` stanza.

* You disable the feature by deleting the `ksmConfiguration` stanza.

* You can allow {VirtProductName} to enable KSM on only a subset of nodes by adding node selection syntax to the `ksmConfiguration.nodeLabelSelector` field.
--
+
[NOTE]
====
Even if the KSM activation feature is disabled in {VirtProductName}, an administrator can still enable KSM on nodes that support it.
====

[id="virt-ksm-node-labels"]
== KSM node labels

{VirtProductName} identifies nodes that are configured to support KSM and applies the following node labels:

`kubevirt.io/ksm-handler-managed: "false"`:: This label is set to `"true"` when {VirtProductName} activates KSM on a node that is experiencing memory overload. This label is not set to `"true"` if an administrator activates KSM.

`kubevirt.io/ksm-enabled: "false"`:: This label is set to `"true"` when KSM is activated on a node, even if {VirtProductName} did not activate KSM.

These labels are not applied to nodes that do not support KSM.

// Module included in the following assembly:
//
// * virt/virtual_machines/advanced_vm_management/virt-activating-ksm.adoc
//

[id="virt-configure-ksm-web_{context}"]
= Configuring KSM activation by using the web console

[role="_abstract"]
You can allow {VirtProductName} to activate kernel samepage merging (KSM) on all nodes in your cluster by using the OpenShift Container Platform web console.

.Procedure

. From the side menu, click *Virtualization* -> *Settings*.

. Select the *Cluster* tab.

. Expand *Resource management*.

. Enable or disable the feature for all nodes using the *Kernel Samepage Merging (KSM)* toggle button.

// Module included in the following assembly:
//
// * virt/virtual_machines/advanced_vm_management/virt-activating-ksm.adoc
//

[id="virt-configure-ksm-cli_{context}"]
= Configuring KSM activation by using the CLI

[role="_abstract"]
You can enable or disable {VirtProductName}'s kernel samepage merging (KSM) activation feature by editing the `HyperConverged` custom resource (CR). Use this method if you want {VirtProductName} to activate KSM on only a subset of nodes.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `ksmConfiguration` stanza:
* To enable the KSM activation feature for all nodes, set the `nodeLabelSelector` value to `{}`. For example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  configuration:
    ksmConfiguration:
      nodeLabelSelector: {}
# ...
----

* To enable the KSM activation feature on a subset of nodes, edit the `nodeLabelSelector` field. Add syntax that matches the nodes where you want {VirtProductName} to enable KSM. For example, the following configuration allows {VirtProductName} to enable KSM on nodes where both `<first_example_key>` and `<second_example_key>` are set to `"true"`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  configuration:
    ksmConfiguration:
      nodeLabelSelector:
        matchLabels:
          <first_example_key>: "true"
          <second_example_key>: "true"
# ...
----

* To disable the KSM activation feature, delete the `ksmConfiguration` stanza. For example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  configuration:
# ...
----

. Save the file.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Specifying nodes for virtual machines
* Placing pods on specific nodes using node selectors
* Managing kernel samepage merging
