---
title: "Migrating to a cluster with multi-architecture compute machines"
type: reference
domain: openshift
slug: updating-4-22-migrating-to-multi-payload
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/updating/migrating-to-multi-payload
version: 4.22
family: updating
documentKind: "Documentation"
---

# Migrating to a cluster with multi-architecture compute machines

[id="migrating-clusters-to-multi-payload"]
= Migrating to a cluster with multi-architecture compute machines

[role="_abstract"]
You can migrate your current cluster with single-architecture compute machines to a cluster with multi-architecture compute machines by updating to a multi-architecture, manifest-listed payload. This allows you to add mixed architecture compute nodes to your cluster.

For information about configuring your multi-architecture compute machines, see "Configuring multi-architecture compute machines on an OpenShift Container Platform cluster".

Before migrating your single-architecture cluster to a cluster with multi-architecture compute machines, it is recommended to install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` custom resource. For more information, see Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator.

[IMPORTANT]
====
Migration from a multi-architecture payload to a single-architecture payload is not supported. Once a cluster has transitioned to using a multi-architecture payload, it can no longer accept a single-architecture update payload.
====

// Migrating to a cluster with multi-architecture compute machines using the CLI
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/migrating-to-multi-payload.adoc

[id="migrating-to-multi-arch-cli_{context}"]
= Migrating to a cluster with multi-architecture compute machines using the CLI

[role="_abstract"]
You can use the {oc-first} to migrate to a cluster with multi-architecture compute machines.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* Your OpenShift Container Platform version is 4.13.0 or later.
+
For more information on how to update your cluster version, see "Updating a cluster using the web console" or "Updating a cluster using the CLI".
* You have installed the {oc-first} that matches the version for your current cluster.
* Your `oc` client is updated to version 4.13.0 or later.
* Your OpenShift Container Platform cluster is installed on AWS, Azure, {gcp-short}, bare metal, or IBM P/Z platforms.
+
For more information on selecting a supported platform for your cluster installation, see "Selecting a cluster installation type".

.Procedure
. Verify that the `RetrievedUpdates` condition is `True` in the Cluster Version Operator (CVO) by running the following command:
+
[source,terminal]
----
$ oc get clusterversion/version -o=jsonpath="{.status.conditions[?(.type=='RetrievedUpdates')].status}"
----
+
If the `RetrievedUpates` condition is `False`, you can find supplemental information regarding the failure by using the following command:
+
[source,terminal]
----
$ oc adm upgrade
----
+
For more information about cluster version condition types, see "Understanding cluster version condition types".

. If the condition `RetrievedUpdates` is `False`, change the channel to `stable-<4.y>` or `fast-<4.y>` by running the following command:
+
[source,terminal]
----
$ oc adm upgrade channel <channel>
----
+
After setting the channel, verify if `RetrievedUpdates` is `True`.
+
For more information about channels, see "Understanding update channels and releases".

. Migrate to the multi-architecture payload by running the following command:
+
[source,terminal]
----
$ oc adm upgrade --to-multi-arch
----

.Verification

* Monitor the migration by running the following command:
+
[source,terminal]
----
$ oc adm upgrade
----
+
.Example output
[source,terminal]
----
working towards ${VERSION}: 106 of 841 done (12% complete), waiting on machine-config
----
+
[IMPORTANT]
====
Machine launches may fail as the cluster settles into the new state. To notice and recover when machines fail to launch, it is recommended that you deploy machine health checks. For more information about machine health checks and how to deploy them, see "About machine health checks".
====
+
. Optional: Retrieve more detailed information about the status of your update and monitor the migration by running the following command:
+
[source,terminal]
----
$ oc adm upgrade status
----
+
For more information about how to use the `oc adm upgrade status` command, see "Gathering cluster update status using oc adm upgrade status (Technology Preview)".

The migrations must be complete and all the cluster operators must be stable before you can add compute machine sets with different architectures to your cluster.

[role="_additional-resources"]
.Additional resources
* Configuring multi-architecture compute machines on an OpenShift Container Platform cluster
* Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator
* Updating a cluster using the web console
* Updating a cluster using the CLI
* Understanding cluster version condition types
* Understanding update channels and releases
* Selecting a cluster installation type
* About machine health checks

//  Migrating the x86 control plane to the arm64 architecture on AWS
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/migrating-to-multi-payload.adoc

[id="migrating-from-x86-to-arm64-cp_{context}"]
= Migrating the x86 control plane to arm64 architecture on {aws-full}

[role="_abstract"]
You can migrate the control plane in your cluster from `x86` to `arm64` architecture on {aws-first}.

.Prerequisites

* You have installed the {oc-first}.
* You logged in to `oc` as a user with `cluster-admin` privileges.

.Procedure

. Check the architecture of the control plane nodes by running the following command:
+
[source,terminal]
----
$ oc get nodes -o wide
----
+
.Example output
[source,terminal]
----
NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
worker-001.example.com        Ready    worker                 100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
worker-002.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
worker-003.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
master-002.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
master-003.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
----
+
The `KERNEL-VERSION` field in the output indicates the architecture of the nodes.

. Check that your cluster uses the multi payload by running the following command:
+
[source,terminal]
----
$ oc adm release info -o jsonpath="{ .metadata.metadata}"
----
+
If you see the following output, the cluster is multi-architecture compatible.
+
[source,terminal]
----
{
 "release.openshift.io/architecture": "multi",
 "url": "https://access.redhat.com/errata/<errata_version>"
}
----
+
If the cluster is not using the multi payload, migrate the cluster to a multi-architecture cluster. For more information, see "Migrating to a cluster with multi-architecture compute machines using the CLI".

. Update your image stream from single-architecture to multi-architecture by running the following command:
+
--
--

. Get the `arm64` compatible Amazon Machine Image (AMI) for configuring the control plane machine set by running the following command:
+
[source,terminal]
----
$ oc get configmap/coreos-bootimages -n openshift-machine-config-operator -o jsonpath='{.data.stream}' | jq -r '.architectures.aarch64.images.aws.regions."<aws_region>".image'
----
+
Replace `<aws_region>` with the {aws-short} region where the current cluster is installed. You can get the {aws-short} region for the installed cluster by running the following command:
+
[source,terminal]
----
$ oc get infrastructure cluster -o jsonpath='{.status.platformStatus.aws.region}'
----
+
.Example output
[source,terminal]
----
ami-xxxxxxx
----

. Update the control plane machine set to support the `arm64` architecture by running the following command:
+
[source,terminal]
----
$ oc edit controlplanemachineset.machine.openshift.io cluster -n openshift-machine-api
----

.. Update the `instanceType` field to a type that supports the `arm64` architecture, and set the `ami.id` field to an AMI that is compatible with the `arm64` architecture. For information about supported instance types, see "Tested instance types for {aws-short} on 64-bit ARM infrastructures".
+
For more information about configuring the control plane machine set for {aws-short}, see "Control plane configuration options for {aws-full}".

.Verification

* Verify that the control plane nodes are now running on the `arm64` architecture by running the following command:
+
[source,terminal]
----
$ oc get nodes -o wide
----
+
.Example output
[source,terminal]
----
NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
worker-001.example.com        Ready    worker                 100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
worker-002.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
worker-003.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
master-002.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
master-003.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
----

[role="_additional-resources"]
.Additional resources

* Control plane configuration options for {aws-full}

* Tested instance types for AWS on 64-bit ARM infrastructures

* Migrating to a cluster with multi-architecture compute machines using the CLI

// Migrating CP or infra between x86 and arm on GCP
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/migrating-to-multi-payload.adoc

[id="multiarch-migrating-cp-infra-gcp_{context}"]
= Migrating control plane or infra machine sets between architectures on {gcp-full}

[role="_abstract"]
You can migrate the control plane or infra machine sets in your {gcp-short} cluster between `x86` and `arm64` architectures.

.Prerequisites

* You have installed the {oc-first}.
* You logged in to `oc` as a user with `cluster-admin` privileges.

.Procedure

. Check the architecture of the control plane or infra nodes by running the following command:
+
[source,terminal]
----
$ oc get nodes -o wide
----
+
.Example output
[source,terminal]
----
NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
worker-001.example.com        Ready    infra                  100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
----
+
The `KERNEL-VERSION` field in the output indicates the architecture of the nodes.

. Check that your cluster uses the multi payload by running the following command:
+
[source,terminal]
----
$ oc adm release info -o jsonpath="{ .metadata.metadata}"
----
+
If you see the following output, the cluster is multi-architecture compatible.
+
[source,terminal]
----
{
 "release.openshift.io/architecture": "multi",
 "url": "https://access.redhat.com/errata/<errata_version>"
}
----
+
If the cluster is not using the multi payload, migrate the cluster to a multi-architecture cluster. For more information, see "Migrating to a cluster with multi-architecture compute machines".

. If you use any custom image streams, update them from single-architecture to multi-architecture by running the following command for each image stream:
+
--
--

. Select an instance type that matches the target architecture from General-purpose machine family for Compute engine (Google documentation). Check the Available regions and zones table (Google documentation) to verify that the instance type is supported in your zone.

. Select a supported disk type for the instance type that you selected from the "Supported disk types" section of General-purpose machine family for Compute engine (Google documentation).

. Determine the {gcp-short} image that the machine set uses after migration by running the following command:
+
[source,terminal]
----
$ oc get configmap/coreos-bootimages \
  -n openshift-machine-config-operator \
  -o jsonpath='{.data.stream}' | jq \
  -r '.architectures.aarch64.images.gcp'
----
+
.Example output
[source,terminal]
----
"gcp": {
    "release": "415.92.202309142014-0",
    "project": "rhcos-cloud",
    "name": "rhcos-415-92-202309142014-0-gcp-aarch64"
  }
----
Use the `project` and `name` parameters from the output to form the `image` parameter in the following format: `projects/<project>/global/images/<name>`.

. To migrate the control plane to another architecture, run the following command:
+
[source,terminal]
----
$ oc edit controlplanemachineset.machine.openshift.io cluster -n openshift-machine-api
----
+
.. Replace the `disks.type` parameter with the disk type that you selected.
.. Replace the `disks.image` parameter with the `image` parameter that you formed previously.
.. Replace the `machineType` parameter with the instance type that you selected.

. To migrate an infra machine set to another architecture, run the following command using the ID of an infra machine set:
+
[source,terminal]
----
$ oc edit machineset <infra-machine-set_id> -n openshift-machine-api
----
+
.. Replace the `disks.type` parameter with the disk type that you selected.
.. Replace the `disks.image` parameter with the `image` parameter that you formed previously.
.. Replace the `machineType` parameter with the instance type that you selected.

[role="_additional-resources"]
.Additional resources

* Tested instance types for {gcp-short} on 64-bit ARM infrastructures

* Migrating to a cluster with multi-architecture compute machines using the CLI
