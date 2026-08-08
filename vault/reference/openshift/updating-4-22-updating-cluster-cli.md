---
title: "Updating a cluster using the CLI"
type: reference
domain: openshift
slug: updating-4-22-updating-cluster-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/updating/updating-cluster-cli
version: 4.22
family: updating
documentKind: "Documentation"
---

# Updating a cluster using the CLI

[id="updating-cluster-cli"]
= Updating a cluster using the CLI

[role="_abstract"]
You can perform minor version and patch updates on an OpenShift Container Platform cluster by using the {oc-first}.

All OpenShift advisories link directly to this assembly. If you are doing work that changes the URL, DON'T!
But if you really need to, please contact the release notes team so they can change the advisory templates. These templates are not part of the openshift-docs repo.

// About updating single node OpenShift Container Platform
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating-cluster-web-console.adoc
// * updating/updating_a_cluster/updating-cluster-cli.adoc

[id="update-single-node-openshift_{context}"]
= About updating single node OpenShift Container Platform

[role="_abstract"]
You can update a single-node OpenShift Container Platform cluster by using either the console or CLI.

However, note the following limitations:

* The prerequisite to pause the `MachineHealthCheck` resources is not required because there is no other node to perform the health check.

* Restoring a single-node OpenShift Container Platform cluster using an etcd backup is not officially supported. However, it is good practice to perform the etcd backup in case your update fails. If your control plane is healthy, you might be able to restore your cluster to a previous state by using the backup.

* Updating a single-node OpenShift Container Platform cluster requires downtime and can include an automatic reboot. The amount of downtime depends on the update payload, as described in the following scenarios:

** If the update payload contains an operating system update, which requires a reboot, the downtime is significant and impacts cluster management and user workloads.

** If the update contains machine configuration changes that do not require a reboot, the downtime is less, and the impact on the cluster management and user workloads is lessened. In this case, the node draining step is skipped with single-node OpenShift Container Platform because there is no other node in the cluster to reschedule the workloads to.

** If the update payload does not contain an operating system update or machine configuration changes, a short API outage occurs and resolves quickly.

[IMPORTANT]
====
There are conditions, such as bugs in an updated package, that can cause the single node to not restart after a reboot. In this case, the update does not rollback automatically.
====

[role="_additional-resources"]
.Additional resources

* About the Machine Config Operator

[id="updating-cli-prereqs_{context}"]
= Prerequisites for a cluster update

[role="_abstract"]
You must satisfy the following prerequisites before updating a cluster using the CLI.

* Have access to the cluster as a user with `admin` privileges.
See "Using RBAC to define and apply permissions" for more information.
* Have a recent etcd backup in case your update fails and you must restore your cluster to a previous state.
* Have a recent Container Storage Interface (CSI) volume snapshot in case you need to restore persistent volumes due to a pod failure.
* Your {op-system-base}7 workers are replaced with {op-system-base}8 or {op-system} workers. Red{nbsp}Hat does not support in-place {op-system-base}7 to {op-system-base}8 updates for {op-system-base} workers; those hosts must be replaced with a clean operating system install.
* You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default software catalogs switch from the current minor version to the next during a cluster update. See "Updating installed Operators" for more information on how to check compatibility and, if necessary, update the installed Operators.
* Ensure that all machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing a canary rollout update strategy.
* If your cluster uses manually maintained credentials, update the cloud provider resources for the new release. For more information, including how to determine if this is a requirement for your cluster, see "Preparing to update a cluster with manually maintained credentials".
* Ensure that you address all `Upgradeable=False` conditions so the cluster allows an update to the next minor version. An alert displays at the top of the *Cluster Settings* page when you have one or more cluster Operators that cannot be updated. You can still update to the next available patch update for the minor release you are currently on.
// * Review the list of APIs that were removed in Kubernetes 1.28, migrate any affected components to use the new API version, and provide the administrator acknowledgment. For more information, see Preparing to update to OpenShift Container Platform 4.16.
* If you run an Operator or you have configured any application with the pod disruption budget, you might experience an interruption during the update process. If `minAvailable` is set to 1 in `PodDisruptionBudget`, the nodes are drained to apply pending machine configs which might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the `PodDisruptionBudget` field can prevent the node drain.

[IMPORTANT]
====
* When an update is failing to complete, the Cluster Version Operator (CVO) reports the status of any blocking components while attempting to reconcile the update. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red{nbsp}Hat support.
* Using the `unsupportedConfigOverrides` section to modify the configuration of an Operator is unsupported and might block cluster updates. You must remove this setting before you can update your cluster.
====

[role="_additional-resources"]
.Additional resources
* Support policy for unmanaged Operators
* Using RBAC to define and apply permissions
* Backing up etcd
* Backing up persistent volumes with CSI snapshots
* Updating installed Operators
* Preparing to update a cluster with manually maintained credentials

// Pausing a MachineHealthCheck resource
// Module included in the following assemblies:

// * updating/updating_a_cluster/updating-cluster-cli.adoc
// * updating/updating_a_cluster/updating-cluster-web-console.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update.adoc

[id="machine-health-checks-pausing_{context}"]
= Pausing a MachineHealthCheck resource

[role="_abstract"]
During the update process, nodes in the cluster might become temporarily unavailable. For worker nodes, the `MachineHealthCheck` resources might identify such nodes as unhealthy and reboot them. To avoid rebooting worker nodes, you must pause all the `MachineHealthCheck` resources before updating the cluster.

[NOTE]
====
Some `MachineHealthCheck` resources might not need to be paused. If your `MachineHealthCheck` resource relies on unrecoverable conditions, pausing that MHC is unnecessary.
====

.Prerequisites

* You installed the {oc-first}.

.Procedure

. List all of the available `MachineHealthCheck` resources that you want to pause by running the following command:
+
[source,terminal]
----
$ oc get machinehealthcheck -n openshift-machine-api
----

. For each `MachineHealthCheck` resource, pause the machine health check by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api annotate mhc <mhc_name> cluster.x-k8s.io/paused=""
----
+
The annotated `MachineHealthCheck` resource resembles the following YAML file:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineHealthCheck
metadata:
  name: example
  namespace: openshift-machine-api
  annotations:
    cluster.x-k8s.io/paused: ""
spec:
  selector:
    matchLabels:
      role: worker
  unhealthyConditions:
  - type:    "Ready"
    status:  "Unknown"
    timeout: "300s"
  - type:    "Ready"
    status:  "False"
    timeout: "300s"
  maxUnhealthy: "40%"
status:
  currentHealthy: 5
  expectedMachines: 5
----
+
[IMPORTANT]
====
Resume the machine health checks after updating the cluster. To resume the check, remove the pause annotation from the `MachineHealthCheck` resource by running the following command:

[source,terminal]
----
$ oc -n openshift-machine-api annotate mhc <mhc-name> cluster.x-k8s.io/paused-
----
====

// Updating a cluster by using the CLI
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating-cluster-cli.adoc
// * updating/updating_a_cluster/updating-cluster-rhel-compute.adoc

[id="update-upgrading-cli_{context}"]
= Updating a cluster by using the CLI

[role="_abstract"]
You can use the {oc-first} to review and request cluster updates.

You can find information about available OpenShift Container Platform advisories and updates
in the errata section
of the Customer Portal.

.Prerequisites

* You installed the {oc-first} that matches the version for your updated version.
* You are logged in to the cluster as user with `cluster-admin` privileges.
* You have paused all `MachineHealthCheck` resources.
// Example output Failing=true taken from https://github.com/openshift/oc/blob/main/pkg/cli/admin/upgrade/recommend/examples/4.16.27-degraded-monitoring.output

.Procedure

. View the available updates and note the version number of the update that you want to apply by running the following command:
+
[source,terminal]
----
$ oc adm upgrade recommend
----
+
.Example output
[source,terminal]
----
The following conditions found no cause for concern in updating this cluster to later releases: recommended/CriticalAlerts (AsExpected), recommended/NodeAlerts (AsExpected), recommended/PodDisruptionBudgetAlerts (AsExpected), recommended/PodImagePullAlerts (AsExpected), recommended/UpdatePrecheckAlerts (AsExpected)

Upstream update service is unset, so the cluster will use an appropriate default.
Channel: stable-4.21 (available channels: candidate-4.20, candidate-4.21, candidate-4.22, eus-4.20, fast-4.20, fast-4.21, stable-4.20, stable-4.21)

Updates to 4.21:
  VERSION     ISSUES
  4.21.14     no known issues relevant to this cluster
  4.21.13     no known issues relevant to this cluster
And 2 older 4.21 updates you can see with '--show-outdated-releases' or '--version VERSION'.

Updates to 4.20:
  VERSION     ISSUES
  4.20.20     no known issues relevant to this cluster
----
.Example output
[source,terminal]
----
...

Upstream update service: https://amd64.origin.releases.ci.openshift.org/graph
Channel: stable-scos-4

Updates to 4.21:
  VERSION               ISSUES
  4.21.0-okd-scos.ec.14 no known issues relevant to this cluster

Updates to 4.20:
  VERSION            ISSUES
  4.20.0-okd-scos.17 no known issues relevant to this cluster
----
+
[NOTE]
====
* You can use the `--version` flag to determine whether a specific version is recommended for your update. If there are no recommended updates, updates that have known issues might still be available.
* For details and information on how to perform a _Control Plane Only_ update, see "Performing a Control Plane Only update".
====

. Based on your organization requirements, set the appropriate update channel by running the following command. For example, you can set your channel to `stable-4.13` or `fast-4.13`. For more information about channels, see "Understanding update channels and releases".
// In OKD, no need to set the channel.
//this example will need to be updated per eus release to reflect options available
+
[source,terminal]
----
$ oc adm upgrade channel <channel>
----
+
.Example command
[source,terminal,subs="attributes+"]
----
$ oc adm upgrade channel stable-
----
+
[IMPORTANT]
====
For production clusters, you must subscribe to a `stable-\*`, `eus-*`, or `fast-*` channel.
====
+
[NOTE]
====
When you are ready to move to the next minor version, choose the channel that corresponds to that minor version.
The sooner you declare the update channel, the more effectively the cluster can recommend update paths to your target version.
The cluster might take some time to evaluate all the possible updates that are available and offer the best update recommendations to choose from.
Update recommendations can change over time, as they are based on what update options are available at the time.

If you cannot see an update path to your target minor version, keep updating your cluster to the latest patch release for your current version until the next minor version is available in the path.
====

. Apply an update:
** To update to the latest version, run the following command:
+
[source,terminal]
----
$ oc adm upgrade --to-latest=true
----

** To update to a specific version, run the following command:
+
[source,terminal]
----
$ oc adm upgrade --to=<version>
----
+
Replace `<version>` with the update version that you obtained from the output of the `oc adm upgrade recommend` command.
+
[IMPORTANT]
====
When using the `oc adm upgrade --help` command, there is a listed option for the `--force` flag. This is _heavily discouraged_, because using the `--force` option bypasses cluster-side guards, including release verification and precondition checks. Using the `--force` flag does not guarantee a successful update. Bypassing guards puts the cluster at risk.
====

. If the cluster administrator evaluates the potential known risks and decides it is acceptable for the current cluster, then the administrator can waive the safety guards and proceed with the update by running the following command:
+
[source,terminal]
----
$ oc adm upgrade --allow-not-recommended --to <version>
----

. Optional: Review the status of the Cluster Version Operator by running the following command:
+
[source,terminal]
----
$ oc adm upgrade status
----
+
[NOTE]
====
To monitor the update in real time, run `oc adm upgrade status` in a `watch` utility.
====

+
[source,terminal]
.Example output
----
info: An upgrade is in progress. Working towards 4.14.0-0.okd-2024-01-06-084517: 117 of 864 done (13% complete), waiting on etcd, kube-apiserver

Upstream: https://amd64.origin.releases.ci.openshift.org/graph
Channel: stable-4
No updates available. You may still upgrade to a specific release image with --to-image or wait for new updates to be available.
----

. After the update completes, confirm that the cluster version has
updated to the new version by running the following command:
+
[source,terminal]
----
$ oc adm upgrade
----
+
.Example output
[source,terminal]
----
Cluster version is <version>

Upstream is unset, so the cluster will use an appropriate default.
Channel: stable-<version> (available channels: candidate-<version>, eus-<version>, fast-<version>, stable-<version>)

No updates available. You may force an update to a specific release image, but doing so might not be supported and might result in downtime or data loss.
----
+
[source,terminal]
.Example output
----
Cluster version is 4.14.0-0.okd-2024-01-06-084517

Upstream: https://amd64.origin.releases.ci.openshift.org/graph
Channel: stable-4
No updates available. You may still upgrade to a specific release image with --to-image or wait for new updates to be available.
----
+
. If you are updating your cluster to the next minor version, such as version X.y to X.(y+1), confirm that your nodes are updated before deploying workloads that rely on a new feature. Run the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                           STATUS   ROLES    AGE   VERSION
ip-10-0-168-251.ec2.internal   Ready    master   82m   v1.35.4
ip-10-0-170-223.ec2.internal   Ready    master   82m   v1.35.4
ip-10-0-179-95.ec2.internal    Ready    worker   70m   v1.35.4
ip-10-0-182-134.ec2.internal   Ready    worker   70m   v1.35.4
ip-10-0-211-16.ec2.internal    Ready    master   82m   v1.35.4
ip-10-0-250-100.ec2.internal   Ready    worker   69m   v1.35.4
----

[role="_additional-resources"]
.Additional resources

* Performing a Control Plane Only update
* Understanding update channels and releases

// Cluster update status using oc adm upgrade status
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating-cluster-cli.adoc

[id="update-upgrading-oc-adm-upgrade-status_{context}"]
= Cluster update status using oc adm upgrade status

[role="_abstract"]
When updating your cluster, the `oc adm upgrade` command returns limited information about the status of your update. The cluster administrator can use the `oc adm upgrade status` command to return specific information regarding a cluster update, including the status of the control plane and worker node updates. Worker is also known as compute.

The `oc adm upgrade status` command is read-only and does not alter any state in your cluster.

The `oc adm upgrade status` command can be used for clusters on versions 4.12 or later.

The `oc adm upgrade status` command will output three sections, control plane update, worker nodes update, and health insights.

Control Plane Update:: Displays details about the updating cluster control plane, contains a high-level assessment, completion status, duration estimate, or cluster Operator health. The section also shows a table with control plane node update information.
+
The control plane update section can also show an additional table that lists cluster Operators being updated if the `--details=operators` or `--details-all` flags are used. Please note that due the asynchronous distributed nature of OpenShift Container Platform, an operator may appear in this section more than once during the update, or not at all. The section is only shown when a cluster Operator is observed to be updating. It is normal during an update to observe no updating cluster Operator at certain periods; not every performed action can be assigned to an observable updating cluster Operator.

Worker Notes Update:: Displays the worker node update information. The worker nodes section starts with a table that displays a summary of information about each worker pool configured in the cluster. Each non-empty worker pool output will show a dedicated table listing update information about nodes that belong to that pool. If a cluster does not have any worker nodes, the output will not contain the worker node section. You can make the node tables show all lines by using the `--details=nodes` or `--details=all` flags.

Health Insights:: Displays insights about states and events present in the cluster that may be relevant for the ongoing update. You can use the `--details=health` flag to expand the items in this section into a more verbose form with more content such as documentation links, longer form descriptions, or cluster resources involved in the insight.

[NOTE]
====
The `oc adm upgrade status` command is currently not supported on {hcp} clusters.
====

The following is an example of the output you will see for an update progressing successfully:

[source,terminal]
----
= Control Plane =
Assessment:      Progressing
Target Version:  4.17.1 (from 4.17.0)
Updating:        machine-config
Completion:      97% (32 operators updated, 1 updating, 0 waiting)
Duration:        54m (Est. Time Remaining: <10m)
Operator Status: 32 Healthy, 1 Unavailable

Control Plane Nodes
NAME                                        ASSESSMENT    PHASE      VERSION   EST    MESSAGE
ip-10-0-53-40.us-east-2.compute.internal    Progressing   Draining   4.17.0    +10m
ip-10-0-30-217.us-east-2.compute.internal   Outdated      Pending    4.17.0    ?
ip-10-0-92-180.us-east-2.compute.internal   Outdated      Pending    4.17.0    ?

= Worker Upgrade =

WORKER POOL   ASSESSMENT    COMPLETION   STATUS
worker        Progressing   0% (0/2)     1 Available, 1 Progressing, 1 Draining
infra         Progressing   50% (1/2)    1 Available, 1 Progressing, 1 Draining

Worker Pool Nodes: Worker
NAME                                       ASSESSMENT    PHASE      VERSION   EST    MESSAGE
ip-10-0-4-159.us-east-2.compute.internal   Progressing   Draining   4.17.0    +10m
ip-10-0-99-40.us-east-2.compute.internal   Outdated      Pending    4.17.0    ?

Worker Pool Nodes: infra
NAME                                             ASSESSMENT    PHASE      VERSION   EST    MESSAGE
ip-10-0-4-159-infra.us-east-2.compute.internal   Progressing   Draining   4.17.0    +10m
ip-10-0-20-162.us-east-2.compute.internal        Completed     Updated    4.17.1    -

= Update Health =

SINCE   LEVEL   IMPACT   MESSAGE
54m4s   Info    None     Update is proceeding well
----

// Changing the update server by using the CLI
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating-cluster-cli.adoc
// * updating/updating_a_cluster/updating-cluster-rhel-compute.adoc

[id="update-changing-update-server-cli_{context}"]
= Changing the update server by using the CLI

[role="_abstract"]
You can change the update server your cluster uses to retrieve information about update paths.

Changing the update server is optional. If you have an OpenShift Update Service (OSUS) installed and configured locally, you must set the URL for the server as the `upstream` to use the local server during updates. The default value for `upstream` is `\https://api.openshift.com/api/upgrades_info/v1/graph`.

.Procedure

* Change the `upstream` parameter value in the cluster version by running the following command:
+
[source,terminal]
----
$ oc patch clusterversion/version --patch '{"spec":{"upstream":"<update_server_url>"}}' --type=merge
----
Replace `<update_server_url>` with the URL for the update server.
+
.Example output
+
[source,terminal]
----
clusterversion.config.openshift.io/version patched
----
