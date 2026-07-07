---
title: "Troubleshooting Operator issues"
type: reference
domain: openshift
slug: support-4-22-troubleshooting-operator-issues
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/troubleshooting-operator-issues
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting Operator issues

[id="troubleshooting-operator-issues"]
= Troubleshooting Operator issues

// This assembly is duplicated in operators/admin/olm-troubleshooting-operator-issues.adoc.

[role="_abstract"]
A cluster administrator can do the following to resolve Operator issues: verify Operator subscription status, check Operator pod health, and gather Operator logs.

Operators are a method of packaging, deploying, and managing an OpenShift Container Platform application. They act like an extension of the software vendor's engineering team, watching over an OpenShift Container Platform environment and using its current state to make decisions in real time. Operators are designed to handle upgrades seamlessly, react to failures automatically, and not take shortcuts, such as skipping a software backup process to save time.

OpenShift Container Platform  includes a default set of Operators that are required for proper functioning of the cluster. These default Operators are managed by the Cluster Version Operator (CVO).

As a cluster administrator, you can install application Operators from the software catalog using the OpenShift Container Platform web console or the CLI. You can then subscribe the Operator to one or more namespaces to make it available for developers on your cluster. Application Operators are managed by Operator Lifecycle Manager (OLM).

If you experience Operator issues, verify Operator subscription status. Check Operator pod health across the cluster and gather Operator logs for diagnosis.

// Operator subscription condition types
// Module included in the following assemblies:
//
// * operators/admin/olm-status.adoc
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="olm-status-conditions_{context}"]
= Operator subscription condition types

[role="_abstract"]
Subscriptions can report the following condition types:

.Subscription condition types
[cols="1,2",options="header"]
|===
|Condition |Description

|`CatalogSourcesUnhealthy`
|Some or all of the catalog sources to be used in resolution are unhealthy.

|`InstallPlanMissing`
|An install plan for a subscription is missing.

|`InstallPlanPending`
|An install plan for a subscription is pending installation.

|`InstallPlanFailed`
|An install plan for a subscription has failed.

|`ResolutionFailed`
|The dependency resolution for a subscription has failed.

|===

[NOTE]
====
Default OpenShift Container Platform cluster Operators are managed by the Cluster Version Operator (CVO) and they do not have a `Subscription` object. Application Operators are managed by Operator Lifecycle Manager (OLM) and they have a `Subscription` object.
====

// TODO: Add this xref when the Operators book is added to ROSA HCP.
[role="_additional-resources"]
== Additional resources

* Catalog health requirements

// Viewing Operator subscription status by using the CLI
// Module included in the following assemblies:
//
// * operators/admin/olm-status.adoc
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="olm-status-viewing-cli_{context}"]
= Viewing Operator subscription status by using the CLI

[role="_abstract"]
You can view Operator subscription status by using the CLI.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List Operator subscriptions:
+
[source,terminal]
----
$ oc get subs -n <operator_namespace>
----

. Use the `oc describe` command to inspect a `Subscription` resource:
+
[source,terminal]
----
$ oc describe sub <subscription_name> -n <operator_namespace>
----

. In the command output, find the `Conditions` section for the status of Operator subscription condition types. In the following example, the `CatalogSourcesUnhealthy` condition type has a status of `false` because all available catalog sources are healthy:
+
.Example output
[source,terminal]
----
Name:         cluster-logging
Namespace:    openshift-logging
Labels:       operators.coreos.com/cluster-logging.openshift-logging=
Annotations:  <none>
API Version:  operators.coreos.com/v1alpha1
Kind:         Subscription
# ...
Conditions:
   Last Transition Time:  2019-07-29T13:42:57Z
   Message:               all available catalogsources are healthy
   Reason:                AllCatalogSourcesHealthy
   Status:                False
   Type:                  CatalogSourcesUnhealthy
# ...
----
+
[NOTE]
====
Default OpenShift Container Platform cluster Operators are managed by the Cluster Version Operator (CVO) and they do not have a `Subscription` object. Application Operators are managed by Operator Lifecycle Manager (OLM) and they have a `Subscription` object.
====

// Viewing Operator catalog source status by using the CLI
// Module included in the following assemblies:
//
// * operators/admin/olm-status.adoc
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="olm-cs-status-cli_{context}"]
= Viewing Operator catalog source status by using the CLI

[role="_abstract"]
You can view the status of an Operator catalog source by using the CLI.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List the catalog sources in a namespace. For example, you can check the `{global_ns}` namespace, which is used for cluster-wide catalog sources:
+
[source,terminal,subs="attributes+"]
----
$ oc get catalogsources -n {global_ns}
----
+
.Example output
[source,terminal]
----
NAME                  DISPLAY               TYPE   PUBLISHER   AGE
certified-operators   Certified Operators   grpc   Red Hat     55m
community-operators   Community Operators   grpc   Red Hat     55m
example-catalog       Example Catalog       grpc   Example Org 2m25s
redhat-operators      Red Hat Operators     grpc   Red Hat     55m
----

. Use the `oc describe` command to get more details and status about a catalog source:
+
[source,terminal,subs="attributes+"]
----
$ oc describe catalogsource example-catalog -n {global_ns}
----
+
.Example output
[source,terminal,subs="attributes+"]
----
Name:         example-catalog
Namespace:    {global_ns}
Labels:       <none>
Annotations:  operatorframework.io/managed-by: marketplace-operator
              target.workload.openshift.io/management: {"effect": "PreferredDuringScheduling"}
API Version:  operators.coreos.com/v1alpha1
Kind:         CatalogSource
# ...
Status:
  Connection State:
    Address:              example-catalog.{global_ns}.svc:50051
    Last Connect:         2021-09-09T17:07:35Z
    Last Observed State:  TRANSIENT_FAILURE
  Registry Service:
    Created At:         2021-09-09T17:05:45Z
    Port:               50051
    Protocol:           grpc
    Service Name:       example-catalog
    Service Namespace:  {global_ns}
# ...
----
+
In the preceding example output, the last observed state is `TRANSIENT_FAILURE`. This state indicates that there is a problem establishing a connection for the catalog source.

. List the pods in the namespace where your catalog source was created:
+
[source,terminal,subs="attributes+"]
----
$ oc get pods -n {global_ns}
----
+
.Example output
[source,terminal]
----
NAME                                    READY   STATUS             RESTARTS   AGE
certified-operators-cv9nn               1/1     Running            0          36m
community-operators-6v8lp               1/1     Running            0          36m
marketplace-operator-86bfc75f9b-jkgbc   1/1     Running            0          42m
example-catalog-bwt8z                   0/1     ImagePullBackOff   0          3m55s
redhat-operators-smxx8                  1/1     Running            0          36m
----
+
When a catalog source is created in a namespace, a pod for the catalog source is created in that namespace. In the preceding example output, the status for the `example-catalog-bwt8z` pod is `ImagePullBackOff`. This status indicates that there is an issue pulling the catalog source's index image.

. Use the `oc describe` command to inspect a pod for more detailed information:
+
[source,terminal,subs="attributes+"]
----
$ oc describe pod example-catalog-bwt8z -n {global_ns}
----
+
.Example output
[source,terminal,subs="attributes+"]
----
Name:         example-catalog-bwt8z
Namespace:    {global_ns}
Priority:     0
Node:         ci-ln-jyryyg2-f76d1-ggdbq-worker-b-vsxjd/10.0.128.2
...
Events:
  Type     Reason          Age                From               Message
  ----     ------          ----               ----               -------
  Normal   Scheduled       48s                default-scheduler  Successfully assigned {global_ns}/example-catalog-bwt8z to ci-ln-jyryyf2-f76d1-fgdbq-worker-b-vsxjd
  Normal   AddedInterface  47s                multus             Add eth0 [10.131.0.40/23] from openshift-sdn
  Normal   BackOff         20s (x2 over 46s)  kubelet            Back-off pulling image "quay.io/example-org/example-catalog:v1"
  Warning  Failed          20s (x2 over 46s)  kubelet            Error: ImagePullBackOff
  Normal   Pulling         8s (x3 over 47s)   kubelet            Pulling image "quay.io/example-org/example-catalog:v1"
  Warning  Failed          8s (x3 over 47s)   kubelet            Failed to pull image "quay.io/example-org/example-catalog:v1": rpc error: code = Unknown desc = reading manifest v1 in quay.io/example-org/example-catalog: unauthorized: access to the requested resource is not authorized
  Warning  Failed          8s (x3 over 47s)   kubelet            Error: ErrImagePull
----
+
In the preceding example output, the error messages indicate that the catalog source's index image is failing to pull successfully because of an authorization issue. For example, the index image might be stored in a registry that requires login credentials.

[role="_additional-resources"]
== Additional resources

// TODO: Add this xref when the Operators book is added to ROSA HCP.
* Operator Lifecycle Manager concepts and resources -> Catalog source
* States of Connectivity (gRPC documentation)
* Accessing images for Operators from private registries

// Querying Operator Pod status
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="querying-operator-pod-status_{context}"]
= Querying Operator pod status

[role="_abstract"]
You can list Operator pods within a cluster and their status. You can also collect a detailed Operator pod summary.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* Your API service is still functional.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List Operators running in the cluster. The output includes Operator version, availability, and up-time information:
+
[source,terminal]
----
$ oc get clusteroperators
----

. List Operator pods running in the Operator's namespace, plus pod status, restarts, and age:
+
[source,terminal]
----
$ oc get pod -n <operator_namespace>
----

. Output a detailed Operator pod summary:
+
[source,terminal]
----
$ oc describe pod <operator_pod_name> -n <operator_namespace>
----

. If an Operator issue is node-specific, query Operator container status on that node.
.. Start a debug pod for the node:
+
[source,terminal]
----
$ oc debug node/my-node
----
+
.. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.
====
+
.. List details about the node's containers, including state and associated pod IDs:
+
[source,terminal]
----
# crictl ps
----
+
.. List information about a specific Operator container on the node. The following example lists information about the `network-operator` container:
+
[source,terminal]
----
# crictl ps --name network-operator
----
+
.. Exit from the debug shell.

// Gathering Operator logs
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="gathering-operator-logs_{context}"]
= Gathering Operator logs

[role="_abstract"]
If you experience Operator issues, you can gather detailed diagnostic information from Operator pod logs.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* Your API service is still functional.
* You have installed the OpenShift CLI (`oc`).
* You have the fully qualified domain names of the control plane or control plane machines.

.Procedure

. List the Operator pods that are running in the Operator's namespace, plus the pod status, restarts, and age:
+
[source,terminal]
----
$ oc get pods -n <operator_namespace>
----

. Review logs for an Operator pod:
+
[source,terminal]
----
$ oc logs pod/<pod_name> -n <operator_namespace>
----
+
If an Operator pod has multiple containers, the preceding command will produce an error that includes the name of each container. Query logs from an individual container:
+
[source,terminal]
----
$ oc logs pod/<operator_pod_name> -c <container_name> -n <operator_namespace>
----
. If the API is not functional, review Operator pod and container logs on each control plane node by using SSH instead. Replace `<master-node>.<cluster_name>.<base_domain>` with appropriate values.
.. List pods on each control plane node:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl pods
----
+
.. For any Operator pods not showing a `Ready` status, inspect the pod's status in detail. Replace `<operator_pod_id>` with the Operator pod's ID listed in the output of the preceding command:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl inspectp <operator_pod_id>
----
+
.. List containers related to an Operator pod:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl ps --pod=<operator_pod_id>
----
+
.. For any Operator container not showing a `Ready` status, inspect the container's status in detail. Replace `<container_id>` with a container ID listed in the output of the preceding command:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl inspect <container_id>
----
+
.. Review the logs for any Operator containers not showing a `Ready` status. Replace `<container_id>` with a container ID listed in the output of the preceding command:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl logs -f <container_id>
----
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. Before attempting to collect diagnostic data over SSH, review whether the data collected by running `oc adm must gather` and other `oc` commands is sufficient instead. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>`.
====

// cannot patch resource "machineconfigpools"
// Disabling Machine Config Operator from autorebooting
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="troubleshooting-disabling-autoreboot-mco_{context}"]
= Disabling the Machine Config Operator from automatically rebooting

[role="_abstract"]
When configuration changes are made by the Machine Config Operator (MCO), {op-system-first} must reboot for the changes to take effect. Whether the configuration change is automatic or manual, an {op-system} node reboots automatically unless it is paused.

[NOTE]
====
====

To avoid unwanted disruptions, you can modify the machine config pool (MCP) to prevent automatic rebooting after the Operator makes changes to the machine config.

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="troubleshooting-disabling-autoreboot-mco-console_{context}"]
= Disabling the Machine Config Operator from automatically rebooting by using the console

[role="_abstract"]
To avoid unwanted disruptions from changes made by the Machine Config Operator (MCO), you can use the OpenShift Container Platform web console to modify the machine config pool (MCP) to prevent the MCO from making any changes to nodes in that pool. This prevents any reboots that would normally be part of the MCO update process.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

. Click *Compute* -> *MachineConfigPools*.

. On the *MachineConfigPools* page, click either *master* or *worker*, depending upon which nodes you want to pause rebooting for.

. On the *master* or *worker* page, click *YAML*.

. In the YAML, update the `spec.paused` field to `true`.
+
.Sample MachineConfigPool object
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
# ...
spec:
# ...
  paused: true
# ...
----
+
Update the `spec.paused` field to `true` to pause rebooting.

. To verify that the MCP is paused, return to the *MachineConfigPools* page.
+
On the *MachineConfigPools* page, the *Paused* column reports *True* for the MCP you modified.
+
If the MCP has pending changes while paused, the *Updated* column is *False* and *Updating* is *False*. When *Updated* is *True* and *Updating* is *False*, there are no pending changes.
+
[IMPORTANT]
====
If there are pending changes (where both the *Updated* and *Updating* columns are *False*), it is recommended to schedule a maintenance window for a reboot as early as possible. Use the following steps for unpausing the autoreboot process to apply the changes that were queued since the last reboot.
====

* Unpause the autoreboot process:

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

. Click *Compute* -> *MachineConfigPools*.

. On the *MachineConfigPools* page, click either *master* or *worker*, depending upon which nodes you want to pause rebooting for.

. On the *master* or *worker* page, click *YAML*.

. In the YAML, update the `spec.paused` field to `false`.
+
.Sample MachineConfigPool object
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
# ...
spec:
# ...
  paused: false
# ...
----
+
Update the `spec.paused` field to `false` to allow rebooting.
+
[NOTE]
====
By unpausing an MCP, the MCO applies all paused changes reboots {op-system-first} as needed.
====

. To verify that the MCP is paused, return to the *MachineConfigPools* page.
+
On the *MachineConfigPools* page, the *Paused* column reports *False* for the MCP you modified.
+
If the MCP is applying any pending changes, the *Updated* column is *False* and the *Updating* column is *True*. When *Updated* is *True* and *Updating* is *False*, there are no further changes being made.

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="troubleshooting-disabling-autoreboot-mco-cli_{context}"]
= Disabling the Machine Config Operator from automatically rebooting by using the CLI

[role="_abstract"]
To avoid unwanted disruptions from changes made by the Machine Config Operator (MCO), you can modify the machine config pool (MCP) using the OpenShift CLI (oc) to prevent the MCO from making any changes to nodes in that pool. This prevents any reboots that would normally be part of the MCO update process.

[NOTE]
====
See second `NOTE` in Disabling the Machine Config Operator from automatically rebooting.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

* To pause or unpause automatic MCO update rebooting:
. Update the `MachineConfigPool` custom resource to set the `spec.paused` field to `true`.
+
.Control plane (master) nodes
[source,terminal]
----
$ oc patch --type=merge --patch='{"spec":{"paused":true}}' machineconfigpool/master
----
+
.Worker nodes
[source,terminal]
----
$ oc patch --type=merge --patch='{"spec":{"paused":true}}' machineconfigpool/worker
----

. Verify that the MCP is paused:
+
.Control plane (master) nodes
[source,terminal]
----
$ oc get machineconfigpool/master --template='{{.spec.paused}}'
----
+
.Worker nodes
[source,terminal]
----
$ oc get machineconfigpool/worker --template='{{.spec.paused}}'
----
+
.Example output
[source,terminal]
----
true
----
+
The `spec.paused` field is `true` and the MCP is paused.

. Determine if the MCP has pending changes:
+
[source,terminal]
----
# oc get machineconfigpool
----
+
.Example output
----
NAME     CONFIG                                             UPDATED   UPDATING
master   rendered-master-33cf0a1254318755d7b48002c597bf91   True      False
worker   rendered-worker-e405a5bdb0db1295acea08bcca33fa60   False     False
----
+
If the *UPDATED* column is *False* and *UPDATING* is *False*, there are pending changes. When *UPDATED* is *True* and *UPDATING* is *False*, there are no pending changes. In the previous example, the worker node has pending changes. The control plane node does not have any pending changes.
+
[IMPORTANT]
====
If there are pending changes (where both the *Updated* and *Updating* columns are *False*), it is recommended to schedule a maintenance window for a reboot as early as possible. Use the following steps for unpausing the autoreboot process to apply the changes that were queued since the last reboot.
====

* Unpause the autoreboot process:

. Update the `MachineConfigPool` custom resource to set the `spec.paused` field to `false`.
+
.Control plane (master) nodes
[source,terminal]
----
$ oc patch --type=merge --patch='{"spec":{"paused":false}}' machineconfigpool/master
----
+
.Worker nodes
[source,terminal]
----
$ oc patch --type=merge --patch='{"spec":{"paused":false}}' machineconfigpool/worker
----
+
[NOTE]
====
By unpausing an MCP, the MCO applies all paused changes and reboots {op-system-first} as needed.
====
+
. Verify that the MCP is unpaused:
+
.Control plane (master) nodes
[source,terminal]
----
$ oc get machineconfigpool/master --template='{{.spec.paused}}'
----
+
.Worker nodes
[source,terminal]
----
$ oc get machineconfigpool/worker --template='{{.spec.paused}}'
----
+
.Example output
[source,terminal]
----
false
----
+
The `spec.paused` field is `false` and the MCP is unpaused.

. Determine if the MCP has pending changes:
+
[source,terminal]
----
$ oc get machineconfigpool
----
+
.Example output
----
NAME     CONFIG                                   UPDATED  UPDATING
master   rendered-master-546383f80705bd5aeaba93   True     False
worker   rendered-worker-b4c51bb33ccaae6fc4a6a5   False    True
----
+
If the MCP is applying any pending changes, the *UPDATED* column is *False* and the *UPDATING* column is *True*. When *UPDATED* is *True* and *UPDATING* is *False*, there are no further changes being made. In the previous example, the MCO is updating the worker node.

// Refreshing failing subscriptions
// cannot delete resource "clusterserviceversions", "jobs" in API group "operators.coreos.com" in the namespace "openshift-apiserver"
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc
// * serverless/install/removing-openshift-serverless.adoc

[id="olm-refresh-subs_{context}"]
= Refreshing failing subscriptions

[role="_abstract"]
In Operator Lifecycle Manager (OLM), if you subscribe to an Operator that references images that are not accessible on your network, you can find jobs in the `openshift-marketplace` namespace that are failing with the following errors:

.Example output
[source,terminal]
----
ImagePullBackOff for
Back-off pulling image "example.com/openshift4/ose-elasticsearch-operator-bundle@sha256:6d2587129c846ec28d384540322b40b05833e7e00b25cca584e004af9a1d292e"
----

.Example output
[source,terminal]
----
rpc error: code = Unknown desc = error pinging docker registry example.com: Get "https://example.com/v2/": dial tcp: lookup example.com on 10.0.0.1:53: no such host
----

As a result, the subscription is stuck in this failing state and the Operator is unable to install or upgrade.

You can refresh a failing subscription by deleting the subscription, cluster service version (CSV), and other related objects. After recreating the subscription, OLM then reinstalls the correct version of the Operator.

.Prerequisites

* You have a failing subscription that is unable to pull an inaccessible bundle image.
* You have confirmed that the correct bundle image is accessible.

.Procedure

. Get the names of the `Subscription` and `ClusterServiceVersion` objects from the namespace where the Operator is installed:
+
[source,terminal]
----
$ oc get sub,csv -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME                                                       PACKAGE                  SOURCE             CHANNEL
subscription.operators.coreos.com/elasticsearch-operator   elasticsearch-operator   redhat-operators   5.0

NAME                                                                         DISPLAY                            VERSION    REPLACES   PHASE
clusterserviceversion.operators.coreos.com/elasticsearch-operator.5.0.0-65   OpenShift Elasticsearch Operator   5.0.0-65              Succeeded
----

. Delete the subscription:
+
[source,terminal]
----
$ oc delete subscription <subscription_name> -n <namespace>
----

. Delete the cluster service version:
+
[source,terminal]
----
$ oc delete csv <csv_name> -n <namespace>
----

. Get the names of any failing jobs and related config maps in the `openshift-marketplace` namespace:
+
[source,terminal]
----
$ oc get job,configmap -n openshift-marketplace
----
+
.Example output
[source,terminal]
----
NAME                                                                        COMPLETIONS   DURATION   AGE
job.batch/1de9443b6324e629ddf31fed0a853a121275806170e34c926d69e53a7fcbccb   1/1           26s        9m30s

NAME                                                                        DATA   AGE
configmap/1de9443b6324e629ddf31fed0a853a121275806170e34c926d69e53a7fcbccb   3      9m30s
----

. Delete the job:
+
[source,terminal]
----
$ oc delete job <job_name> -n openshift-marketplace
----
+
This ensures pods that try to pull the inaccessible image are not recreated.

. Delete the config map:
+
[source,terminal]
----
$ oc delete configmap <configmap_name> -n openshift-marketplace
----

. Reinstall the Operator using the software catalog in the web console.

.Verification

* Check that the Operator has been reinstalled successfully:
+
[source,terminal]
----
$ oc get sub,csv,installplan -n <namespace>
----

// Reinstalling Operators after failed uninstallation
// cannot delete resource "customresourcedefinitions"
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc

[id="olm-reinstall_{context}"]
= Reinstalling Operators after failed uninstallation

[role="_abstract"]
You must successfully and completely uninstall an Operator prior to attempting to reinstall the same Operator. Failure to fully uninstall the Operator properly can leave resources, such as a project or namespace, stuck in a "Terminating" state and cause "error resolving resource" messages. For example:

**Example `Project` resource description**

----
...
    message: 'Failed to delete all resource types, 1 remaining: Internal error occurred:
      error resolving resource'
...
----

These types of issues can prevent an Operator from being reinstalled successfully.

[WARNING]
====
Forced deletion of a namespace is not likely to resolve "Terminating" state issues and can lead to unstable or unpredictable cluster behavior, so it is better to try to find related resources that might be preventing the namespace from being deleted. For more information, see the Red Hat Knowledgebase Solution #4165791, paying careful attention to the cautions and warnings.
====

The following procedure shows how to troubleshoot when an Operator cannot be reinstalled because an existing custom resource definition (CRD) from a previous installation of the Operator is preventing a related namespace from deleting successfully.

.Procedure

. Check if there are any namespaces related to the Operator that are stuck in "Terminating" state:
+
[source,terminal]
----
$ oc get namespaces
----
+
.Example output
----
operator-ns-1                                       Terminating
----

. Check if there are any CRDs related to the Operator that are still present after the failed uninstallation:
+
[source,terminal]
----
$ oc get crds
----
+
[NOTE]
====
CRDs are global cluster definitions; the actual custom resource (CR) instances related to the CRDs could be in other namespaces or be global cluster instances.
====

. If there are any CRDs that you know were provided or managed by the Operator and that should have been deleted after uninstallation, delete the CRD:
+
[source,terminal]
----
$ oc delete crd <crd_name>
----

. Check if there are any remaining CR instances related to the Operator that are still present after uninstallation, and if so, delete the CRs:

.. The type of CRs to search for can be difficult to determine after uninstallation and can require knowing what CRDs the Operator manages. For example, if you are troubleshooting an uninstallation of the etcd Operator, which provides the `EtcdCluster` CRD, you can search for remaining `EtcdCluster` CRs in a namespace:
+
[source,terminal]
----
$ oc get EtcdCluster -n <namespace_name>
----
+
Alternatively, you can search across all namespaces:
+
[source,terminal]
----
$ oc get EtcdCluster --all-namespaces
----

.. If there are any remaining CRs that should be removed, delete the instances:
+
[source,terminal]
----
$ oc delete <cr_name> <cr_instance_name> -n <namespace_name>
----

. Check that the namespace deletion has successfully resolved:
+
[source,terminal]
----
$ oc get namespace <namespace_name>
----
+
[IMPORTANT]
====
If the namespace or other Operator resources are still not uninstalled cleanly, contact Red Hat Support.
====

. Reinstall the Operator using the software catalog in the web console.

.Verification

* Check that the Operator has been reinstalled successfully:
+
[source,terminal]
----
$ oc get sub,csv,installplan -n <namespace>
----

[role="_additional-resources"]
== Additional resources

* Deleting Operators from a cluster
* Adding Operators to a cluster
