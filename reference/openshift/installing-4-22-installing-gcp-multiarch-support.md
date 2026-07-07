---
title: "Installing a cluster with the support for configuring multi-architecture compute machines"
type: reference
domain: openshift
slug: installing-4-22-installing-gcp-multiarch-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-gcp-multiarch-support
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster with the support for configuring multi-architecture compute machines

[id="installing-gcp-multiarch-support"]
= Installing a cluster with the support for configuring multi-architecture compute machines

An OpenShift Container Platform cluster with multi-architecture compute machines supports compute machines with different architectures.

[NOTE]
====
When you have nodes with multiple architectures in your cluster, the architecture of your image must be consistent with the architecture of the node. You must ensure that the pod is assigned to the node with the appropriate architecture and that it matches the image architecture. For more information on assigning pods to nodes, Scheduling workloads on clusters with multi-architecture compute machines.
====

You can install a {gcp-first} cluster with the support for configuring multi-architecture compute machines. After installing the {gcp-short} cluster, you can add multi-architecture compute machines to the cluster in the following ways:

* Adding 64-bit x86 compute machines to a cluster that uses 64-bit ARM control plane machines and already includes 64-bit ARM compute machines. In this case, 64-bit x86 is considered the secondary architecture.
* Adding 64-bit ARM compute machines to a cluster that uses 64-bit x86 control plane machines and already includes 64-bit x86 compute machines. In this case, 64-bit ARM is considered the secondary architecture.

[id="installing-a-cluster-with-multiarch-support_{context}"]
= Installing a cluster with multi-architecture support

You can install a cluster with the support for configuring multi-architecture compute machines.

.Prerequisites

* You installed the {oc-first}.
* You have the OpenShift Container Platform installation program.
* You downloaded the pull secret for your cluster.

.Procedure

. Check that the `openshift-install` binary is using the `multi` payload by running the following command:
+
[source,terminal]
----
$ ./openshift-install version
----
+
.Example output
[source,terminal]
----
./openshift-install 4.22.0
built from commit abc123etc
release image quay.io/openshift-release-dev/ocp-release@sha256:abc123wxyzetc
release architecture multi
default architecture amd64
----
+
The output must contain `release architecture multi` to indicate that the `openshift-install` binary is using the `multi` payload.

. Update the `install-config.yaml` file to configure the architecture for the nodes.
+
.Sample `install-config.yaml` file with multi-architecture configuration
+
[source,yaml]
----
apiVersion: v1
baseDomain: example.openshift.com
compute:
- architecture: amd64 <1>
  hyperthreading: Enabled
  name: worker
  platform: {}
  replicas: 3
controlPlane:
  architecture: arm64 <2>
  name: master
  platform: {}
  replicas: 3
# ...
----
<1> Specify the architecture of the worker node. You can set this field to either `arm64` or `amd64`.
<2> Specify the control plane node architecture. You can set this field to either `arm64` or `amd64`.

.Next steps

* Deploying the cluster

[role="_additional-resources"]
.Additional resources

* Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator
