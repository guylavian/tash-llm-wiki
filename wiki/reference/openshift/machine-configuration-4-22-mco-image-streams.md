---
title: "Setting the {op-system} version in a cluster"
type: reference
domain: openshift
slug: machine-configuration-4-22-mco-image-streams
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/mco-image-streams
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Setting the {op-system} version in a cluster

[id="mco-image-streams"]
= Setting the {op-system} version in a cluster

[role="_abstract"]
You can create an OpenShift Container Platform cluster that uses {op-system-first} 10.x or update an existing cluster to {op-system} 10.x, which is available as a Technology Preview feature in OpenShift Container Platform 4.21.2 and greater. By running {op-system-first} 10.x as a Technology Preview feature, you can test how the operating system works with your cluster and your hardware, anticipate changes, and report bugs to Red{nbsp}Hat.

By default, {op-system} 9.x is installed on OpenShift Container Platform clusters starting with 4.13.

At any time, you can revert the cluster back to {op-system} 9.x, if needed.

{op-system} is a purpose-designed operating system for use with containers that is deployed by default on all OpenShift Container Platform nodes. Each version of {op-system} is based on a specific version of {op-system-base-full}. For OpenShift Container Platform 4.13 and greater, the {op-system} version is based on RHEL 9.x.

Running a cluster with {op-system} 10.x is for *testing purposes only* on test clusters, and should not be used on production clusters. For example, by testing your cluster with {op-system} 10.x, you can ensure that any existing hardware operates as expected with the new operating system.

You can use one of the following methods to run the nodes in a cluster on {op-system} 10.x:

* Upgrading an existing 4.21.2 or later cluster to {op-system} 10.x. For more information, see "Updating the nodes in an existing cluster from {op-system} 9 to {op-system} 10".
* Deploying {op-system} 10.x on a new OpenShift Container Platform cluster. For more information, see "Installation configuration parameters".

// Module included in the following assemblies:
//
// * machine configuration/mco-image-streams.adoc

[id="mco-image-streams-updating_{context}"]
= Updating the nodes in an existing cluster from {op-system} 9 to {op-system} 10

[role="_abstract"]
For an existing OpenShift Container Platform 4.21.2 or later cluster, you can move the nodes in your machine config pool to {op-system-first} 10.x. By running {op-system-first} 10.x as a Technology Preview feature, you can test how the operating system works with your cluster and your hardware, anticipate changes, and report bugs to Red Hat.

Use the following procedure for an OpenShift Container Platform 4.22.x cluster. For an OpenShift Container Platform 4.21.x cluster that is 4.21.2 or later, see the How to deploy a RHCOS 10 OpenShift Container Platform cluster knowledgebase article.

[IMPORTANT]
====
Running a cluster with a mixture of RHCOS 9.x and 10.x nodes is not supported. You must move all of your nodes to RHCOS 10.x.
====

.Prerequisites

* You have updated the boot image in your cluster to at least {op-system} 9.x. Note that the boot image on each node remains at {op-system} 9.x after installing or upgrading to {op-system} 10.x. After you configure {op-system} 10.x in your cluster, new nodes boot using {op-system} 9.x initially and automatically upgrade to {op-system} 10.x. For more information, see "Manually updating the boot image".

* You have enabled the `TechPreviewNoUpgrade` feature set in your cluster's `FeatureGate` custom resource (CR).
For more information, see "Enabling features using feature gates".

.Procedure

. Confirm that your cluster has the {op-system} 10.x stream available by running the following command:
+
[source,terminal]
----
$ oc get osImageStreams/cluster -o yaml | grep rhel-10
----
+
.Example output
[source,terminal]
----
  - name: rhel-10
----
+
It can take several minutes for the `osImageStream` object to become available after you enable the `TechPreviewNoUpgrade` feature set.

. Update the nodes by using one of the following procedures:

* Update all of the nodes in your cluster to RHCOS 10:
+
.. Edit the `OSImageStream` custom resource by running the following command:
+
[source,terminal]
----
$ oc edit osimagestream cluster
----
+
.. Add or edit the `defaultStream` parameter to specify `rhel-10`:
+
[source,terminal]
----
apiVersion: machineconfiguration.openshift.io/v1alpha1
kind: OSImageStream
metadata:
  annotations:
    machineconfiguration.openshift.io/release-image-version: c4a08067821f304642e731fdcca0c8c6a6b19484
  creationTimestamp: "2026-04-13T17:27:41Z"
  generation: 1
  name: cluster
  resourceVersion: "36503"
  uid: f2ef4c15-4c1b-4117-850e-ae6adf408c4f
spec:
  defaultStream: rhel-10
status:
  availableStreams:
  - name: rhel-10
    osExtensionsImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:34baf90f333d89690a2f99b3ab746f8a43fee99b1218a8a058f75231f7c7ab53
    osImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:b208f0f861d009008b43a103e64d087f6da59e480bb0292d401895e041095da7
  - name: rhel-9
    osExtensionsImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:4aa864da633b1ce0a3612992a75849ff2b7d289699fa9b9b400522371a77d3ea
    osImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:cb34964bd5d957a1226e9fb082a591b650eca339ebd4aad15343d02fc21130dd
  defaultStream: rhel-9
----
+
The `spec.defaultStream: rhel-10` parameter directs the Machine Config Operator (MCO) to update the nodes to the image referenced in `status.availableStreams.osImage` value under `name: rhel-10`.

* Update all machine config pools to RHCOS 10:
+
--
.. Update the worker machine config pool to RHCOS 10 by using the following command:
+
[source,terminal]
----
$ oc patch mcp worker --type merge -p '{"spec":{"osImageStream":{"name":"rhel-10"}}}'
----

.. Update the control plane machine config pool to RHCOS 10 by using the following command:
+
[source,terminal]
----
$ oc patch mcp master --type merge -p '{"spec":{"osImageStream":{"name":"rhel-10"}}}'
----

.. Update all custom machine config pools to RHCOS 10 by using the following command with the name of the machine config pool to update:
+
[source,terminal]
----
$ oc patch mcp <mcp_name> --type merge -p '{"spec":{"osImageStream":{"name":"rhel-10"}}}'
----
+
Replace `<mcp_name>` with the names of the custom machine config pools to update.
--
+
[IMPORTANT]
====
Running a cluster with a mixture of RHCOS 9.x and 10.x nodes is not supported. You must move all of your nodes to RHCOS 10.x.
====
+
Wait for the pools to finish rolling out the update.

.Verification

. After the nodes have returned to the READY state, examine the `/etc/redhat-release` file to see the current {op-system} version on the nodes:

.. Log in to a node by using the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----
+
Replace `<node_name>` with the name of the node.

.. Set `/host` as the root directory within the debug shell by using the following command:
+
[source,terminal]
----
$ chroot /host
----

.. Look at the contents of the `/etc/redhat-release` file by using the following command:
+
[source,terminal]
----
$ cat /etc/redhat-release
----
+
The output should appear similar to  the following example:
+
.Example output
[source,terminal]
----
Red Hat Enterprise Linux release 10.2 (Coughlan)
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Enabling features using feature gates

* Manually updating the boot image

When the installation documentation is updated, update:
* /installing/install_config/installation-config-parameters-generic.adoc#installation-config-parameters-generic[Installation configuration parameters]
