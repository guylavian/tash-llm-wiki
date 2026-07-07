---
title: "Creating infrastructure nodes"
type: reference
domain: openshift
slug: nodes-4-22-nodes-nodes-creating-infrastructure-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-nodes-creating-infrastructure-nodes
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Creating infrastructure nodes

[id="nodes-nodes-creating-infrastructure-nodes"]
= Creating infrastructure nodes

[role="_abstract"]
You can use infrastructure machine sets to create machines that host only infrastructure components, such as the default router, the integrated container image registry, and the components for cluster metrics and monitoring. These infrastructure machines are not counted toward the total number of subscriptions that are required to run the environment.

[NOTE]
====
After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or add toleration on `misscheduled` DNS pods.
====

// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * nodes-nodes-creating-infrastructure-nodes.adoc

[id="infrastructure-components_{context}"]
= OpenShift Container Platform infrastructure components

[role="_abstract"]
To reduce subscription costs, you can review the following information to understand which components you can move to an infrastructure node. Components that you move to an infrastructure node do not need to be accounted for during sizing.

Each self-managed Red{nbsp}Hat OpenShift subscription includes entitlements for OpenShift Container Platform and other OpenShift-related components. These entitlements are included for running OpenShift Container Platform control plane and infrastructure workloads and do not need to be accounted for during sizing.

To qualify as an infrastructure node and use the included entitlement, only components that are supporting the cluster, and not part of an end-user application, can run on those instances. Examples include the following components:

* Kubernetes and OpenShift Container Platform control plane services
* The default router
* The integrated container image registry
* The HAProxy-based Ingress Controller
* The cluster metrics collection, or monitoring service, including components for monitoring user-defined projects
* Cluster aggregated logging
* {quay}
* {rh-storage-first}
* Red Hat Advanced Cluster Management for Kubernetes
* Red Hat Advanced Cluster Security for Kubernetes
* Red Hat OpenShift GitOps
* Red Hat OpenShift Pipelines
* {SMProductName}

// Updated the list to match the list under "Red Hat OpenShift control plane and infrastructure nodes" in https://www.redhat.com/en/resources/openshift-subscription-sizing-guide

Any node that runs any other container, pod, or component is a worker node that your subscription must cover.

For information about infrastructure nodes and which components can run on infrastructure nodes, see the "Red Hat OpenShift control plane and infrastructure nodes" section in the OpenShift sizing and subscription guide for enterprise Kubernetes document.

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * machine_management/creating-infrastructure-machinesets.adoc
// * nodes/nodes/nodes-nodes-creating-infrastructure-nodes.adoc

[id="creating-an-infra-node_{context}"]
= Creating an infrastructure node

[role="_abstract"]
To reduce subscription costs, you can use labels to configure compute nodes as infrastructure nodes, where you can move infrastructure resources.

After you create the infrastructure nodes, you can move appropriate workloads to those nodes by using taints and tolerations.

You can optionally create a default cluster-wide node selector. The default node selector is applied to pods created in all namespaces and creates an intersection with any existing node selectors on a pod, which additionally constrains the pod's selector.

[IMPORTANT]
====
* See "Creating infrastructure machine sets" for installer-provisioned infrastructure environments or for any cluster where the control plane nodes are managed by the Machine API.

* If the default node selector key conflicts with the key of a pod's label, then the default node selector is not applied.
+
However, do not set a default node selector that might cause a pod to become unschedulable. For example, setting the default node selector to a specific node role, such as `node-role.kubernetes.io/infra=""`, when a pod's label is set to a different node role, such as `node-role.kubernetes.io/master=""`, can cause the pod to become unschedulable. For this reason, use caution when setting the default node selector to specific node roles.
+
You can alternatively use a project node selector to avoid cluster-wide node selector key conflicts.
====

.Procedure

. Add a label to the compute nodes that you want to act as infrastructure nodes by running the following command:
+
[source,terminal]
----
$ oc label node <node-name> node-role.kubernetes.io/infra=""
----

. Check to see if applicable nodes now have the `infra` role by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Optional: Create a default cluster-wide node selector.

.. Edit the `Scheduler` object by running the following command:
+
[source,terminal]
----
$ oc edit scheduler cluster
----

.. Add the `defaultNodeSelector` field with the appropriate node selector by running the following command:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
spec:
  defaultNodeSelector: node-role.kubernetes.io/infra=""
# ...
----
+
This example node selector deploys pods on infrastructure nodes by default.

.. Save the file to apply the changes.

+
You can now move infrastructure resources to the new infrastructure nodes and remove any workloads that you do not want, or that do not belong, on the new infrastructure node. See the list of workloads supported for use on infrastructure nodes in "OpenShift Container Platform infrastructure components".

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Moving resources to infrastructure machine sets
* Creating infrastructure machine sets
* Creating a compute machine set
* Creating an infrastructure node
* Creating a machine config pool for infrastructure machines
