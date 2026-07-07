---
title: "Managing a cluster with multi-architecture compute machines"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-multi-architecture-compute-managing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/multi-architecture-compute-managing
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Managing a cluster with multi-architecture compute machines

[id="multi-architecture-compute-managing"]
= Managing a cluster with multi-architecture compute machines

Managing a cluster that has nodes with multiple architectures requires you to consider node architecture as you monitor the cluster and manage your workloads. This requires you to take additional considerations into account when you
configure cluster resource requirements and behavior, or
schedule workloads in a multi-architecture cluster.

[id="multi-architecture-scheduling_{context}"]
= Scheduling workloads on clusters with multi-architecture compute machines

When you deploy workloads on a cluster with compute nodes that use different architectures, you must align pod architecture with the architecture of the underlying node. Your workload may also require additional configuration to particular resources depending on the underlying node architecture.

You can use the Multiarch Tuning Operator to enable architecture-aware scheduling of workloads on clusters with multi-architecture compute machines. The Multiarch Tuning Operator implements additional scheduler predicates in the pods specifications based on the architectures that the pods can support at creation time.

For information about the Multiarch Tuning Operator, see Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator.

// Module included in the following assembly
//
//post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-compute-managing.adoc

[id="multi-architecture-scheduling-examples_{context}"]
= Sample multi-architecture node workload deployments

Scheduling a workload to an appropriate node based on architecture works in the same way as scheduling based on any other node characteristic.
Consider the following options when determining how to schedule your workloads.

.Additional resources
* Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator
* Controlling pod placement using node taints
* Controlling pod placement on nodes using node affinity
* Controlling pod placement using the scheduler
* Modifying a compute machine set

//Module included in the following assemblies
//
//post_installation_configuration/multi-architecture-configuration.adoc

[id="multi-architecture-enabling-64k-pages_{context}"]

= Enabling 64k pages on the {op-system-first} kernel

You can enable the 64k memory page in the {op-system-first} kernel on the 64-bit ARM compute machines in your cluster. The 64k page size kernel specification can be used for large GPU or high memory workloads. This is done using the Machine Config Operator (MCO) which uses a machine config pool to update the kernel. To enable 64k page sizes, you must dedicate a machine config pool for ARM64 to enable on the kernel.

[IMPORTANT]
====
Using 64k pages is exclusive to 64-bit ARM architecture compute nodes or clusters installed on 64-bit ARM machines. If you configure the 64k pages kernel on a machine config pool using 64-bit x86 machines, the machine config pool and MCO will degrade.
====

.Prerequisites
* You installed the OpenShift CLI (`oc`).
* You created a cluster with compute nodes of different architecture on one of the supported platforms.

.Procedure

. Label the nodes where you want to run the 64k page size kernel:
[source,terminal]
+
----
$ oc label node <node_name> <label>
----
+
.Example command
[source,terminal]
----
$ oc label node worker-arm64-01 node-role.kubernetes.io/worker-64k-pages=
----

. Create a machine config pool that contains the worker role that uses the ARM64 architecture and the `worker-64k-pages` role:
[source,yaml]
+
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker-64k-pages
spec:
  machineConfigSelector:
    matchExpressions:
      - key: machineconfiguration.openshift.io/role
        operator: In
        values:
        - worker
        - worker-64k-pages
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/worker-64k-pages: ""
      kubernetes.io/arch: arm64
----

. Create a machine config on your compute node to enable `64k-pages` with the `64k-pages` parameter.
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----
+
.Example MachineConfig
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: "worker-64k-pages" <1>
  name: 99-worker-64kpages
spec:
  kernelType: 64k-pages <2>
----
<1> Specify the value of the `machineconfiguration.openshift.io/role` label in the custom machine config pool. The example MachineConfig uses the `worker-64k-pages` label to enable 64k pages in the `worker-64k-pages` pool.
<2> Specify your desired kernel type. Valid values are `64k-pages` and `default`
+
[NOTE]
====
The `64k-pages` type is supported on only 64-bit ARM architecture based compute nodes. The `realtime` type is supported on only 64-bit x86 architecture based compute nodes.
====

.Verification

* To view your new `worker-64k-pages` machine config pool, run the following command:
+
[source,terminal]
----
$ oc get mcp
----
+
.Example output
[source,terminal]
----
NAME     CONFIG                                                                UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-9d55ac9a91127c36314e1efe7d77fbf8                      True      False      False      3              3                   3                     0                      361d
worker   rendered-worker-e7b61751c4a5b7ff995d64b967c421ff                      True      False      False      7              7                   7                     0                      361d
worker-64k-pages  rendered-worker-64k-pages-e7b61751c4a5b7ff995d64b967c421ff   True      False      False      2              2                   2                     0                      35m
----

//Module included in the following assemblies
//
//post_installation_configuration/multi-architecture-configuration.adoc

[id="multi-architecture-import-imagestreams_{context}"]

= Importing manifest lists in image streams on your multi-architecture compute machines

On an OpenShift Container Platform  cluster with multi-architecture compute machines, the image streams in the cluster do not import manifest lists automatically. You must manually change the default `importMode` option to the `PreserveOriginal` option in order to import the manifest list.

.Prerequisites

* You installed the OpenShift Container Platform CLI (`oc`).

.Procedure

* The following example command shows how to patch the `ImageStream` cli-artifacts so that the `cli-artifacts:latest` image stream tag is imported as a manifest list.
+
[source,terminal]
----
$ oc patch is/cli-artifacts -n openshift -p '{"spec":{"tags":[{"name":"latest","importPolicy":{"importMode":"PreserveOriginal"}}]}}'
----

.Verification

* You can check that the manifest lists imported properly by inspecting the image stream tag. The following command will list the individual architecture manifests for a particular tag.
+
[source,terminal]
----
$ oc get istag cli-artifacts:latest -n openshift -oyaml
----

+
If the `dockerImageManifests` object is present, then the manifest list import was successful.

+
.Example output of the `dockerImageManifests` object
[source, yaml]
----
dockerImageManifests:
  - architecture: amd64
    digest: sha256:16d4c96c52923a9968fbfa69425ec703aff711f1db822e4e9788bf5d2bee5d77
    manifestSize: 1252
    mediaType: application/vnd.docker.distribution.manifest.v2+json
    os: linux
  - architecture: arm64
    digest: sha256:6ec8ad0d897bcdf727531f7d0b716931728999492709d19d8b09f0d90d57f626
    manifestSize: 1252
    mediaType: application/vnd.docker.distribution.manifest.v2+json
    os: linux
  - architecture: ppc64le
    digest: sha256:65949e3a80349cdc42acd8c5b34cde6ebc3241eae8daaeea458498fedb359a6a
    manifestSize: 1252
    mediaType: application/vnd.docker.distribution.manifest.v2+json
    os: linux
  - architecture: s390x
    digest: sha256:75f4fa21224b5d5d511bea8f92dfa8e1c00231e5c81ab95e83c3013d245d1719
    manifestSize: 1252
    mediaType: application/vnd.docker.distribution.manifest.v2+json
    os: linux
----
