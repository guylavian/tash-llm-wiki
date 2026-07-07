---
title: "Using the vSphere Problem Detector Operator"
type: reference
domain: openshift
slug: installing-4-22-using-vsphere-problem-detector-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/using-vsphere-problem-detector-operator
version: 4.22
family: installing
documentKind: "Documentation"
---

# Using the vSphere Problem Detector Operator

[id="using-vsphere-problem-detector-operator"]
= Using the vSphere Problem Detector Operator

You can use the {operator-name} to check a cluster that you deployed on {vmw-full} for common installation and misconfiguration issues that relate to storage.

// About the operator
// Module included in the following assemblies:
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

[id="vsphere-problem-detector-about_{context}"]
= About the {operator-name}

The {operator-name} checks a cluster that you deployed on {vmw-full} for common installation and configuration issues that relate to storage.

After the Cluster Storage Operator starts and determines that a cluster runs on {vmw-full}, the Cluster Storage Operator launches the {operator-name}. When the {operator-name} starts, the Operator immediately runs the checks. The {operator-name} communicates with the {vmw-short} vCenter Server to find the virtual machines in the cluster, the default datastore, and other information about the {vmw-short} vCenter Server configuration. The Operator uses the credentials from the Cloud Credential Operator to connect to {vmw-short}.

The Operator runs the checks according to the following schedule:

* The checks run every hour.

* If any check fails, the Operator runs the checks again in intervals of 1 minute, 2 minutes, 4, 8, and so on. The Operator doubles the interval up to a maximum interval of 8 hours.

* When all checks pass, the schedule returns to an hour interval.

After a failure, the Operator increases its check frequency to quickly report success when the failure condition gets resolved. You can run the Operator manually for immediate troubleshooting information.

// Run the checks
// Module included in the following assemblies:
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

[id="vsphere-problem-detector-running_{context}"]
= Running the {operator-name} checks

You can override the schedule for running the {operator-name} checks and run the checks immediately.

The {operator-name} automatically runs the checks every hour. After the Operator starts, the Operator runs the checks immediately. After the Cluster Storage Operator starts and determines that a cluster runs on {vmw-full}, the Cluster Storage Operator starts the {operator-name}. To run the checks immediately, you can scale the {operator-name} to `0` and back to `1` so that the Cluster Storage Operator restarts the {operator-name}.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

* Scale the Operator to `0`:
+
[source,terminal]
----
$ oc scale deployment/vsphere-problem-detector-operator --replicas=0 \
    -n openshift-cluster-storage-operator
----

.Verification

* Verify that the pods have restarted by running the following command:
+
[source,terminal]
----
$ oc -n openshift-cluster-storage-operator get pod -l name=vsphere-problem-detector-operator -w
----
+
.Example output
[source,terminal]
----
NAME                                                 READY   STATUS    RESTARTS   AGE
vsphere-problem-detector-operator-77486bd645-9ntpb   1/1     Running   0          11s
----
+
The `AGE` field must indicate that the pod restarted.

.Next steps

* Viewing the events from the {operator-name}
* Viewing the logs from the {operator-name}

// View the events
// Module included in the following assemblies
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

[id="vsphere-problem-detector-viewing-events_{context}"]
= Viewing the events from the {operator-name}

After the {operator-name} runs and performs the configuration checks, the Operator creates events that you can view from the command-line interface (CLI) or from the OpenShift Container Platform web console.

.Prerequisites

* The {operator-name} ran checks on your cluster.

.Procedure

* To view the events by using the CLI, run the following command:
+
[source,terminal]
----
$ oc get event -n openshift-cluster-storage-operator \
    --sort-by={.metadata.creationTimestamp}
----
+
.Example output
[source,terminal]
----
16m     Normal    Started             pod/vsphere-problem-detector-operator-xxxxx         Started container vsphere-problem-detector
16m     Normal    Created             pod/vsphere-problem-detector-operator-xxxxx         Created container vsphere-problem-detector
16m     Normal    LeaderElection      configmap/vsphere-problem-detector-lock    vsphere-problem-detector-operator-xxxxx became leader
----

* To view the events by using the OpenShift Container Platform web console, navigate to *Home* -> *Events* and select `openshift-cluster-storage-operator` from the *Project* menu.

// View the logs
// Module included in the following assemblies:
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

[id="vsphere-problem-detector-viewing-logs_{context}"]
= Viewing the logs from the {operator-name}

After the {operator-name} runs and performs the configuration checks, the Operator creates log records that you can view from the command-line interface (CLI) or from the OpenShift Container Platform web console. Log lines that indicate `passed` means that you do not need to perform any actions.

The ideal output for a log line indicates `passed` or `0 problems`. If a log line indicates `failure` or 1 or more problems, see the information in the "Configuration checks run by the {operator-name}" document.

.Prerequisites

* The {operator-name} ran checks on your cluster.

.Procedure

* To view the logs by using the CLI, run the following command. A log line that shows `passed` in the output means that you must analyze the log output and resolve the issue.
+
[source,terminal]
----
$ oc logs deployment/vsphere-problem-detector-operator \
    -n openshift-cluster-storage-operator
----
+
.Example output
[source,terminal]
----
I0108 08:32:28.445696       1 operator.go:209] ClusterInfo passed
I0108 08:32:28.451029       1 datastore.go:57] CheckStorageClasses checked 1 storage classes, 0 problems found
I0108 08:32:28.451047       1 operator.go:209] CheckStorageClasses passed
I0108 08:32:28.452160       1 operator.go:209] CheckDefaultDatastore passed
I0108 08:32:28.480648       1 operator.go:271] CheckNodeDiskUUID:<host_name> passed
I0108 08:32:28.480685       1 operator.go:271] CheckNodeProviderID:<host_name> passed
----

* To view the Operator logs with the OpenShift Container Platform web console, perform the following steps:
+
.. Navigate to *Workloads* -> *Pods*.
+
.. Select `openshift-cluster-storage-operator` from the *Projects* menu.
+
.. Click the link for the `vsphere-problem-detector-operator` pod.
+
.. Click the *Logs* tab on the *Pod details* page to view the logs.

// Reference: Problem detector checks
// Module included in the following assemblies:
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

[id="vsphere-problem-detector-config-checks_{context}"]
= Configuration checks run by the {operator-name}

The following tables identify the configuration checks that the {operator-name} runs. Some checks verify the configuration of the cluster. Other checks verify the configuration of each node in the cluster.

.Cluster configuration checks
[options="header",cols="20,80a"]
|===
|Name
|Description

|`CheckDefaultDatastore`
|Verifies that the default datastore name in the {vmw-full} configuration is short enough for use with dynamic provisioning.

If this check fails, you can expect the following:

* `systemd` logs errors to the journal such as `Failed to set up mount unit: Invalid argument`.

* `systemd` does not unmount volumes if the virtual machine shuts down or reboots without draining all the pods from the node.

If this check fails, reconfigure {vmw-short} with a shorter name for the default datastore.

|`CheckFolderPermissions`
|Verifies the permission to list volumes in the default datastore. You must enable the permission to create volumes. The Operator verifies the permission by listing the `/` and `/kubevols` directories. When the Operator performs the check, the root directory must exist. The `/kubevols` directory might not exist at the time of the check. The creation of the `/kubevols` directory occurs when the datastore supports dynamic provisioning.

If this check fails, review the required permissions for the vCenter account that you specified during the OpenShift Container Platform installation.

|`CheckStorageClasses`
|Verifies the following:

* The fully qualified path to each persistent volume that the storage class provisions does not go lower than 255 characters.

* The storage class can use only one storage policy and the policy must be defined.

|`CheckTaskPermissions`
|Verifies the permission to list recent tasks and datastores.

|`ClusterInfo`
|Collects the cluster version and UUID from {vmw-short} vCenter.
|===

.Node configuration checks
[options="header",cols="20,80a"]
|===
|Name
|Description

|`CheckNodeDiskUUID`
|Verifies that all the {vmw-short} virtual machines include the `disk.enableUUID=TRUE` configuration.

If this check fails, see the How to check `disk.EnableUUID` parameter from VM in vSphere Red Hat Knowledgebase solution.

|`CheckNodeProviderID`
|Verifies that all nodes have the `ProviderID` configuration from {vmw-short} vCenter. This check fails when the output from the following command does not include a provider ID for each node.

[source,terminal]
----
$ oc get nodes -o custom-columns=NAME:.metadata.name,PROVIDER_ID:.spec.providerID,UUID:.status.nodeInfo.systemUUID
----

If this check fails, reference the {vmw-short} product documentation on how to set the provider ID for each node in the cluster.

|`CollectNodeESXiVersion`
|Reports the version of the ESXi hosts that run nodes.

|`CollectNodeHWVersion`
|Reports the virtual machine hardware version for a node.
|===

// Concept: Storage class config check
// Module included in the following assemblies:
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

[id="vsphere-problem-detector-storage-class-config-check_{context}"]
= About the storage class configuration check

The datastore name and cluster ID relate to the names for persistent volumes that use {vmw-full} storage. After the creation of a persistent volume, `systemd` creates a mount unit for the persistent volume.

The `systemd` process has a 255 character limit for the length of the fully qualified path to the virtual machine disk (VMDK) file. This path follows the naming conventions for `systemd` and {vmw-short}. The naming conventions use the following example pattern:

[source,text]
----
/var/lib/kubelet/plugins/kubernetes.io/vsphere-volume/mounts/[<datastore>] 00000000-0000-0000-0000-000000000000/<cluster_id>-dynamic-pvc-00000000-0000-0000-0000-000000000000.vmdk
----

* The naming conventions require 205 characters of the 255 character limit.

* The depolyment determines the datastore name and the cluster ID.

* The datastore name and cluster ID substitute into the example pattern. The fully qualified path gets processed with the `systemd-escape` command to escape special characters. For example, after the escape operation, a hyphen character uses four characters, such as `\x2d`.

* After the `systemd-escape` CLI processes the VMDK file path, the length of the path must not be lower than 255 characters. This criteria ensures that the `systemd` process can access the fully qualified VMDK file path.

// Metrics
// Module included in the following assemblies:
//
// * installing/installing_vsphere/using-vsphere-problem-detector-operator.adoc

[id="vsphere-problem-detector-operator-metrics_{context}"]
= Metrics for the {operator-name}

The {operator-name} exposes the following metrics for use by the OpenShift Container Platform monitoring stack.

.Metrics exposed by the {operator-name}
[cols="2a,8a",options="header"]
|===
|Name |Description

|`vsphere_cluster_check_total`
|Cumulative number of cluster-level checks that the {operator-name} performed. This count includes both successes and failures.

|`vsphere_cluster_check_errors`
|Number of failed cluster-level checks that the {operator-name} performed. For example, a value of `1` indicates that one cluster-level check failed.

|`vsphere_esxi_version_total`
|Counts the number of ESXi hosts with a specific version. Note that if a host runs more than one node, the {operator-name} counts the host only once.

|`vsphere_node_check_total`
|Cumulative number of node-level checks that the {operator-name} performed. This count includes both successes and failures.

|`vsphere_node_check_errors`
|Counts the number of failed node-level checks that the {operator-name} performed. For example, a value of `1` indicates that one node-level check failed.

|`vsphere_node_hw_version_total`
|Number of {vmw-short} nodes with a specific hardware version.

|`vsphere_vcenter_info`
|Information about the {vmw-short} vCenter Server.
|===

[role="_additional-resources"]
== Additional resources

* About OpenShift Container Platform monitoring

// Clear temporary attributes
