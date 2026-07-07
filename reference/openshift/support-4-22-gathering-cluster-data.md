---
title: "Gathering data about your cluster"
type: reference
domain: openshift
slug: support-4-22-gathering-cluster-data
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/gathering-cluster-data
version: 4.22
family: support
documentKind: "Documentation"
---

# Gathering data about your cluster

[id="gathering-cluster-data"]
= Gathering data about your cluster

[role="_abstract"]
When opening a support case, it is helpful to provide debugging information about your cluster to Red Hat Support. You can use tools such as `must-gather`, `sosreport`, and cluster node journal logs to collect diagnostic data.

When opening a support case, it is helpful to provide debugging
information about your cluster to Red Hat Support.

It is recommended to provide:

* Data gathered using the `oc adm must-gather` command
* The  unique cluster ID

You can use the following tools to get debugging information about your OpenShift Container Platform cluster.

// About the must-gather tool
// Module included in the following assemblies:
//
// * sandboxed_containers/troubleshooting-sandboxed-containers.adoc
// * virt/support/virt-collecting-virt-data.adoc
// * support/gathering-cluster-data.adoc
// * service_mesh/v2x/ossm-support.adoc
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * serverless/serverless-support.adoc

[id="about-must-gather_{context}"]
= About the must-gather tool

[role="_abstract"]
The `oc adm must-gather` CLI command collects the information from your cluster that is most likely needed for debugging issues, including:

* Resource definitions
* Service logs

By default, the `oc adm must-gather` command uses the default plugin image and writes into `./must-gather.local`.

Alternatively, you can collect specific information by running the command with the appropriate arguments as described in the following sections:

* To collect data related to one or more specific features, use the `--image` argument with an image, as listed in a following section.
+
For example:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion}
----

* To collect the audit logs, use the `-- /usr/bin/gather_audit_logs` argument, as described in a following section.
+

For example:
+
[source,terminal]
----
$ oc adm must-gather -- /usr/bin/gather_audit_logs
----
+
[NOTE]
====
- Audit logs are not collected as part of the default set of information to reduce the size of the files.
- On a Windows operating system, install the `cwRsync` client and add to the `PATH`  variable for use with the `oc rsync` command.
====

When you run `oc adm must-gather`, a new pod with a random name is created in a new project on the cluster. The data is collected on that pod and saved in a new directory that starts with `must-gather.local` in the current working directory.

For example:

[source,terminal]
----
NAMESPACE                      NAME                 READY   STATUS      RESTARTS      AGE
...
openshift-must-gather-5drcj    must-gather-bklx4    2/2     Running     0             72s
openshift-must-gather-5drcj    must-gather-s8sdh    2/2     Running     0             72s
...
----
// todo: table or ref module listing available images?
Optionally, you can run the `oc adm must-gather` command in a specific namespace by using the `--run-namespace` option.

For example:

[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --run-namespace <namespace> \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion}
----

// Gathering data about your cluster for Red Hat Support
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support_gathering_data_{context}"]
= Gathering data about your cluster for Red Hat Support

[role="_abstract"]
You can gather debugging information about your cluster by using the `oc adm must-gather` CLI command.

If you are gathering information to debug a self-managed hosted cluster, see "Gathering information to troubleshoot {hcp}".

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
+
[NOTE]
====
In OpenShift Container Platform deployments, customers who are not using the Customer Cloud Subscription (CCS) model cannot use the `oc adm must-gather` command as it requires `cluster-admin` privileges.
====
+
* The OpenShift Container Platform CLI (`oc`) is installed.
* The OpenShift CLI (`oc`) is installed.

.Procedure

. Navigate to the directory where you want to store the `must-gather` data.
+

[NOTE]
====
If your cluster is in a disconnected environment, you must take additional steps. If your mirror registry has a trusted CA, you must first add the trusted CA to the cluster. For all clusters in disconnected environments, you must import the default `must-gather` image as an image stream.

[source,terminal]
----
$ oc import-image is/must-gather -n openshift
----
====

. Run the `oc adm must-gather` command:
+
[source,terminal]

----
$ oc adm must-gather
----
+
[IMPORTANT]
====
If you are in a disconnected environment, use the `--image` flag as part of must-gather and point to the payload image.
====
+
[NOTE]
====
Because this command picks a random control plane node by default, the pod might be scheduled to a control plane node that is in the `NotReady` and `SchedulingDisabled` state.
====

.. If this command fails, for example, if you cannot schedule a pod on your cluster, then use the `oc adm inspect` command to gather information for particular resources.
+
[NOTE]
====
Contact Red Hat Support for the recommended resources to gather.
====

. Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see How to find the cluster-id or name on OpenShift cluster. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
----
+
where:

`<must_gather_local_dir>`:: Replace with the actual directory name.

. Attach the compressed file to your support case on the the *Customer Support* page of the Red Hat Customer Portal.

. Attach the compressed file to the bugreport

// Reducing the size of must-gather output
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-must-gather-targeted-collection_{context}"]
= Reducing the size of must-gather output

[role="_abstract"]
The `oc adm must-gather` command collects comprehensive cluster information. However, a full data collection can result in a large file that is difficult to upload and analyze and could result in timeouts.

To manage the output size and target your data collection for more effective troubleshooting, you can pass specific flags to the underlying `gather` script or scope the collection to particular resources.

// Gathering data for specific resources
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-must-gather-targeted-collection-gathering-data_{context}"]
= Gathering data for specific resources

[role="_abstract"]
Instead of collecting data for the entire cluster, you can direct the `must-gather` tool to inspect a specific resource. This method is highly effective for isolating issues within a single project, Operator, or application.

The `must-gather` tool uses `oc adm inspect` internally. You can specify what to inspect by passing the `inspect` command and its arguments after the `--` separator.

.Procedure

* To gather data for a specific namespace, such as `my-project`, run the following command:
+
[source,terminal]
----
$ oc adm must-gather --dest-dir=my-project-must-gather -- oc adm inspect ns/my-project
----

* This command collects all standard resources within the `my-project` namespace, including logs from pods in that namespace, but excludes cluster-scoped resources.

* To gather data related to a specific Cluster Operator, such as `openshift-apiserver`, run the following command:
+
[source,terminal]
----
$ oc adm must-gather --dest-dir=apiserver-must-gather -- oc adm inspect clusteroperator/openshift-apiserver
----

* To exclude rotated logs, such as `+*.gz+` or `+*.1+` files, from data collection, set the `REDUCE_LOGS` environment variable by running the following command:
+
[source,terminal]
----
$ oc adm must-gather -- REDUCE_LOGS=skip_rotated_logs /usr/bin/gather
----

* To exclude logs entirely and significantly reduce the size of the `must-gather` archive, add a double dash (`--`) after `oc adm must-gather` command and add the `--no-logs` argument:
+
[source,terminal]
----
$ oc adm must-gather -- /usr/bin/gather --no-logs
----

// Commented this additional resources section out because the hosted control plane section was removed from the openshift-enterprise topic map.
//ifndef::openshift-rosa,openshift-rosa-hcp,openshift-dedicated[]
//[role="_additional-resources"]
//== Additional resources
//* Gathering information to troubleshoot {hcp}
//endif::openshift-rosa,openshift-rosa-hcp,openshift-dedicated[]

// Table of must-gather flags
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="must-gather-flags_{context}"]
= Must-gather flags

[role="_abstract"]
The flags listed in the following table are available to use with the `oc adm must-gather` command.

.OpenShift Container Platform flags for `oc adm must-gather`
[cols="1,1,3",options="header"]
|====
|Flag |Example command |Description

|`--all-images`
|`oc adm must-gather --all-images=false`
|Collect `must-gather` data using the default image for all Operators on the cluster that are annotated with `operators.openshift.io/must-gather-image`.

|`--dest-dir`
|`oc adm must-gather --dest-dir='<directory_name>'`
|Set a specific directory on the local machine where the gathered data is written.

|`--host-network`
|`oc adm must-gather --host-network=false`
|Run `must-gather` pods as `hostNetwork: true`. Relevant if a specific command and image needs to capture host-level data.

|`--image`
|`oc adm must-gather --image=[<plugin_image>]`
|Specify a `must-gather` plugin image to run. If not specified, OpenShift Container Platform's default `must-gather` image is used.

|`--image-stream`
|`oc adm must-gather --image-stream=[<image_stream>]`
|Specify an`<image_stream>` using a namespace or name:tag value containing a `must-gather` plugin image to run.

|`--node-name`
|`oc adm must-gather --node-name='<node>'`
|Set a specific node to use. If not specified, by default a random master is used.

|`--node-selector`
|`oc adm must-gather --node-selector='<node_selector_name>'`
|Set a specific node selector to use. Only relevant when specifying a command and image which needs to capture data on a set of cluster nodes simultaneously.

|`--run-namespace`
|`oc adm must-gather --run-namespace='<namespace>'`
|An existing privileged namespace where `must-gather` pods should run. If not specified, a temporary namespace is generated.

|`--since`
|`oc adm must-gather --since=<time>`
|Only return logs newer than the specified duration. Defaults to all logs. Plugins are encouraged but not required to support this. Only one `since-time` or `since` may be used.

|`--since-time`
|`oc adm must-gather --since-time='<date_and_time>'`
|Only return logs after a specific date and time, expressed in (RFC3339) format. Defaults to all logs. Plugins are encouraged but not required to support this. Only one `since-time` or `since` may be used.

|`--source-dir`
|`oc adm must-gather --source-dir='/<directory_name>/'`
|Set the specific directory on the pod where you copy the gathered data from.

|`--timeout`
|`oc adm must-gather --timeout='<time>'`
|The length of time to gather data before timing out, expressed as seconds, minutes, or hours, for example, 3s, 5m, or 2h. Time specified must be higher than zero. Defaults to 10 minutes if not specified.

|`--volume-percentage`
|`oc adm must-gather --volume-percentage=<percent>`
|Specify maximum percentage of pod's allocated volume that can be used for `must-gather`. If this limit is exceeded, `must-gather` stops gathering, but still copies gathered data. Defaults to 30% if not specified.
|====

// Gathering data about specific features
// Module included in the following assemblies:
//
// * virt/support/virt-collecting-virt-data.adoc
// * support/gathering-cluster-data.adoc

//This file contains UI elements and/or package names that need to be updated.

[id="gathering-data-specific-features_{context}"]
= Gathering data about specific features

[role="_abstract"]
You can gather debugging information about specific features by using the `oc adm must-gather` CLI command with the `--image` or `--image-stream` argument. The `must-gather` tool supports multiple images, so you can gather data about more than one feature by running a single command.

.Supported must-gather images
[cols="2,2",options="header",subs="attributes+"]
|===
|Image |Purpose

|`registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion}`
|Data collection for {VirtProductName}.

|`registry.redhat.io/openshift-serverless-1/svls-must-gather-rhel8`
|Data collection for OpenShift Serverless.

|`registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:<installed_version_service_mesh>`
|Data collection for Red Hat OpenShift Service Mesh.

|`registry.redhat.io/multicluster-engine/must-gather-rhel8`
|Data collection for {hcp}.

|`registry.redhat.io/odf4/odf-must-gather-rhel9:v<installed_version_ODF>`
|Data collection for {rh-storage-first}.

|`registry.redhat.io/openshift-logging/cluster-logging-rhel9-operator:v<installed_version_logging>`
|Data collection for {logging}.

|`quay.io/netobserv/must-gather`
|Data collection for the Network Observability Operator.

|`registry.redhat.io/openshift4/ose-local-storage-mustgather-rhel9:v<installed_version_LSO>`
|Data collection for Local Storage Operator.

|`registry.redhat.io/openshift-sandboxed-containers/osc-must-gather-rhel8:v<installed_version_sandboxed_containers>`
|Data collection for {osc}.

|`registry.redhat.io/workload-availability/node-healthcheck-must-gather-rhel8:v<installed_version_NHC>`
|Data collection for the Red{nbsp}Hat Workload Availability Operators, including the Self Node Remediation (SNR) Operator, the Fence Agents Remediation (FAR) Operator, the Machine Deletion Remediation (MDR) Operator, the Node Health Check (NHC) Operator, and the Node Maintenance Operator (NMO).

Use this image if your NHC Operator version is *earlier than 0.9.0*.

For more information, see the "Gathering data" section for the specific Operator in https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/latest/html/remediation_fencing_and_maintenance/index[Remediation, fencing, and maintenance] (Workload Availability for Red Hat OpenShift documentation).

|`registry.redhat.io/workload-availability/node-healthcheck-must-gather-rhel9:v<installed_version_NHC>`
|Data collection for the Red{nbsp}Hat Workload Availability Operators, including the Self Node Remediation (SNR) Operator, the Fence Agents Remediation (FAR) Operator, the Machine Deletion Remediation (MDR) Operator, the Node Health Check (NHC) Operator, and the Node Maintenance Operator (NMO).

Use this image if your NHC Operator version is *0.9.0. or later*.

For more information, see the "Gathering data" section for the specific Operator in https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/latest/html/remediation_fencing_and_maintenance/index[Remediation, fencing, and maintenance] (Workload Availability for Red Hat OpenShift documentation).

|`registry.redhat.io/numaresources/numaresources-must-gather-rhel9:v<installed-version-nro>`
|Data collection for the NUMA Resources Operator (NRO).

|`registry.redhat.io/openshift4/ptp-must-gather-rhel8:v<installed-version-ptp>`
|Data collection for the PTP Operator.

|`registry.redhat.io/openshift-gitops-1/must-gather-rhel8:v<installed_version_GitOps>`
|Data collection for {gitops-title}.

|`registry.redhat.io/openshift4/ose-secrets-store-csi-mustgather-rhel9:v<installed_version_secret_store>`
|Data collection for the {secrets-store-operator}.

|`registry.redhat.io/lvms4/lvms-must-gather-rhel9:v<installed_version_LVMS>`
|Data collection for the LVM Operator.

|`registry.redhat.io/compliance/openshift-compliance-must-gather-rhel8:<digest-version>`
|Data collection for the Compliance Operator.

|===

[NOTE]
====
To determine the latest version for an OpenShift Container Platform component's image, see the OpenShift Operator Life Cycles web page on the Red Hat Customer Portal.
====

.Available must-gather images
[cols="2,2",options="header"]
|===
|Image |Purpose

|`quay.io/kubevirt/must-gather`
|Data collection for KubeVirt.

|`quay.io/openshift-knative/must-gather`
|Data collection for Knative.

|`docker.io/maistra/istio-must-gather`
|Data collection for service mesh.

|`quay.io/konveyor/must-gather`
|Data collection for migration-related information.

|`quay.io/ocs-dev/ocs-must-gather`
|Data collection for {rh-storage}.

|`quay.io/openshift/origin-cluster-logging-operator`
|Data collection for OpenShift Logging.

|`quay.io/openshift/origin-local-storage-mustgather`
|Data collection for Local Storage Operator.

|`quay.io/openshift/origin-secrets-store-csi-mustgather`
|Data collection for the {secrets-store-operator}.

|===

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* The OpenShift Container Platform CLI (`oc`) is installed.
* The OpenShift CLI (`oc`) is installed.

.Procedure

. Navigate to the directory where you want to store the `must-gather` data.

. Run the `oc adm must-gather` command with one or more `--image` or `--image-stream` arguments.
+
[NOTE]
====
* To collect the default `must-gather` data in addition to specific feature data, add the `--image-stream=openshift/must-gather` argument.
* For information on gathering data about the Custom Metrics Autoscaler, see the Additional resources section that follows.
====
+
For example, the following command gathers both the default cluster data and information specific to {VirtProductName}:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
  --image-stream=openshift/must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion}
----
+
You can use the `must-gather` tool with additional arguments to gather data that is specifically related to OpenShift Logging and the
Red Hat OpenShift
Cluster
Logging Operator in your cluster. For OpenShift Logging, run the following command:
+
[source,terminal]
----
$ oc adm must-gather --image=$(oc -n openshift-logging get deployment.apps/cluster-logging-operator \
  -o jsonpath='{.spec.template.spec.containers[?(@.name == "cluster-logging-operator")].image}')
----
+
.Example `must-gather` output for OpenShift Logging
[source,terminal]
----
├── cluster-logging
│  ├── clo
│  │  ├── cluster-logging-operator-74dd5994f-6ttgt
│  │  ├── clusterlogforwarder_cr
│  │  ├── cr
│  │  ├── csv
│  │  ├── deployment
│  │  └── logforwarding_cr
│  ├── collector
│  │  ├── fluentd-2tr64
│  ├── curator
│  │  └── curator-1596028500-zkz4s
│  ├── eo
│  │  ├── csv
│  │  ├── deployment
│  │  └── elasticsearch-operator-7dc7d97b9d-jb4r4
│  ├── es
│  │  ├── cluster-elasticsearch
│  │  │  ├── aliases
│  │  │  ├── health
│  │  │  ├── indices
│  │  │  ├── latest_documents.json
│  │  │  ├── nodes
│  │  │  ├── nodes_stats.json
│  │  │  └── thread_pool
│  │  ├── cr
│  │  ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
│  │  └── logs
│  │     ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
│  ├── install
│  │  ├── co_logs
│  │  ├── install_plan
│  │  ├── olmo_logs
│  │  └── subscription
│  └── kibana
│     ├── cr
│     ├── kibana-9d69668d4-2rkvz
├── cluster-scoped-resources
│  └── core
│     ├── nodes
│     │  ├── ip-10-0-146-180.eu-west-1.compute.internal.yaml
│     └── persistentvolumes
│        ├── pvc-0a8d65d9-54aa-4c44-9ecc-33d9381e41c1.yaml
├── event-filter.html
├── gather-debug.log
└── namespaces
   ├── openshift-logging
   │  ├── apps
   │  │  ├── daemonsets.yaml
   │  │  ├── deployments.yaml
   │  │  ├── replicasets.yaml
   │  │  └── statefulsets.yaml
   │  ├── batch
   │  │  ├── cronjobs.yaml
   │  │  └── jobs.yaml
   │  ├── core
   │  │  ├── configmaps.yaml
   │  │  ├── endpoints.yaml
   │  │  ├── events
   │  │  │  ├── elasticsearch-im-app-1596020400-gm6nl.1626341a296c16a1.yaml
   │  │  │  ├── elasticsearch-im-audit-1596020400-9l9n4.1626341a2af81bbd.yaml
   │  │  │  ├── elasticsearch-im-infra-1596020400-v98tk.1626341a2d821069.yaml
   │  │  │  ├── elasticsearch-im-app-1596020400-cc5vc.1626341a3019b238.yaml
   │  │  │  ├── elasticsearch-im-audit-1596020400-s8d5s.1626341a31f7b315.yaml
   │  │  │  ├── elasticsearch-im-infra-1596020400-7mgv8.1626341a35ea59ed.yaml
   │  │  │  ├── curator-1596021300-wn2ks.162634ebf0055a94.yaml
   │  │  │  ├── curator.162638330681bee2.yaml
   │  │  │  ├── elasticsearch-delete-app-1596020400-gm6nl.1626341a296c16a1.yaml
   │  │  │  ├── elasticsearch-delete-audit-1596020400-9l9n4.1626341a2af81bbd.yaml
   │  │  │  ├── elasticsearch-delete-infra-1596020400-v98tk.1626341a2d821069.yaml
   │  │  │  ├── elasticsearch-rollover-app-1596020400-cc5vc.1626341a3019b238.yaml
   │  │  │  ├── elasticsearch-rollover-audit-1596020400-s8d5s.1626341a31f7b315.yaml
   │  │  │  ├── elasticsearch-rollover-infra-1596020400-7mgv8.1626341a35ea59ed.yaml
   │  │  ├── events.yaml
   │  │  ├── persistentvolumeclaims.yaml
   │  │  ├── pods.yaml
   │  │  ├── replicationcontrollers.yaml
   │  │  ├── secrets.yaml
   │  │  └── services.yaml
   │  ├── openshift-logging.yaml
   │  ├── pods
   │  │  ├── cluster-logging-operator-74dd5994f-6ttgt
   │  │  │  ├── cluster-logging-operator
   │  │  │  │  └── cluster-logging-operator
   │  │  │  │     └── logs
   │  │  │  │        ├── current.log
   │  │  │  │        ├── previous.insecure.log
   │  │  │  │        └── previous.log
   │  │  │  └── cluster-logging-operator-74dd5994f-6ttgt.yaml
   │  │  ├── cluster-logging-operator-registry-6df49d7d4-mxxff
   │  │  │  ├── cluster-logging-operator-registry
   │  │  │  │  └── cluster-logging-operator-registry
   │  │  │  │     └── logs
   │  │  │  │        ├── current.log
   │  │  │  │        ├── previous.insecure.log
   │  │  │  │        └── previous.log
   │  │  │  ├── cluster-logging-operator-registry-6df49d7d4-mxxff.yaml
   │  │  │  └── mutate-csv-and-generate-sqlite-db
   │  │  │     └── mutate-csv-and-generate-sqlite-db
   │  │  │        └── logs
   │  │  │           ├── current.log
   │  │  │           ├── previous.insecure.log
   │  │  │           └── previous.log
   │  │  ├── curator-1596028500-zkz4s
   │  │  ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
   │  │  ├── elasticsearch-im-app-1596030300-bpgcx
   │  │  │  ├── elasticsearch-im-app-1596030300-bpgcx.yaml
   │  │  ├── elasticsearch-delete-app-1596030300-bpgcx
   │  │  │  ├── elasticsearch-delete-app-1596030300-bpgcx.yaml
   │  │  │  └── indexmanagement
   │  │  │     └── indexmanagement
   │  │  │        └── logs
   │  │  │           ├── current.log
   │  │  │           ├── previous.insecure.log
   │  │  │           └── previous.log
   │  │  ├── fluentd-2tr64
   │  │  │  ├── fluentd
   │  │  │  │  └── fluentd
   │  │  │  │     └── logs
   │  │  │  │        ├── current.log
   │  │  │  │        ├── previous.insecure.log
   │  │  │  │        └── previous.log
   │  │  │  ├── fluentd-2tr64.yaml
   │  │  │  └── fluentd-init
   │  │  │     └── fluentd-init
   │  │  │        └── logs
   │  │  │           ├── current.log
   │  │  │           ├── previous.insecure.log
   │  │  │           └── previous.log
   │  │  ├── kibana-9d69668d4-2rkvz
   │  │  │  ├── kibana
   │  │  │  │  └── kibana
   │  │  │  │     └── logs
   │  │  │  │        ├── current.log
   │  │  │  │        ├── previous.insecure.log
   │  │  │  │        └── previous.log
   │  │  │  ├── kibana-9d69668d4-2rkvz.yaml
   │  │  │  └── kibana-proxy
   │  │  │     └── kibana-proxy
   │  │  │        └── logs
   │  │  │           ├── current.log
   │  │  │           ├── previous.insecure.log
   │  │  │           └── previous.log
   │  └── route.openshift.io
   │     └── routes.yaml
   └── openshift-operators-redhat
      ├── ...
----

. Run the `oc adm must-gather` command with one or more `--image` or `--image-stream` arguments. For example, the following command gathers both the default cluster data and information specific to KubeVirt:
+
[source,terminal]
----
$ oc adm must-gather \
 --image-stream=openshift/must-gather \
 --image=quay.io/kubevirt/must-gather
----

. Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see How to find the cluster-id or name on OpenShift cluster. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
----
+
where:

`<must_gather_local_dir>`:: Replace with the actual directory name.

. Attach the compressed file to your support case on the the *Customer Support* page of the Red Hat Customer Portal.

[role="_additional-resources"]
.Additional resources

* Gathering debugging data for the Custom Metrics Autoscaler
* Red Hat OpenShift Container Platform Life Cycle Policy

* OpenShift Container Platform update life cycle

* OpenShift Container Platform update life cycle

* OpenShift Container Platform update life cycle

// Gathering network logs
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="gathering-data-network-logs_{context}"]
= Gathering network logs

[role="_abstract"]
You can gather network logs on all nodes in a cluster.

.Procedure

. Run the `oc adm must-gather` command with `-- gather_network_logs`:
+
[source,terminal]
----
$ oc adm must-gather -- gather_network_logs
----
+
[NOTE]
====
By default, the `must-gather` tool collects the OVN `nbdb` and `sbdb` databases from all of the nodes in the cluster. Adding the `-- gather_network_logs` option to include additional logs that contain OVN-Kubernetes transactions for OVN `nbdb` database.
====
.  Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see How to find the cluster-id or name on OpenShift cluster. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
----
+
Replace the `<must_gather_local_dir>` placeholder with the actual directory name.

. Attach the compressed file to your support case on the the *Customer Support* page of the Red Hat Customer Portal.

//Changing the must-gather storage limit
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="must-gather-storage-limit_{context}"]
= Changing the must-gather storage limit

[role="_abstract"]
When using the `oc adm must-gather` command to collect data the default maximum storage for the information is 30% of the storage capacity of the container. After the 30% limit is reached the container is killed and the gathering process stops. Information already gathered is downloaded to your local storage. To run the must-gather command again, you need either a container with more storage capacity or to adjust the maximum volume percentage.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* The OpenShift CLI (`oc`) is installed.

.Procedure

* Run the `oc adm must-gather` command with the `volume-percentage` flag. The new value cannot exceed 100.
+
[source,terminal]
----
$ oc adm must-gather --volume-percentage <storage_percentage>
----
+
If the container reaches the storage limit, an error message similar to the following example is generated:
+
[source,terminal]
----
Disk usage exceeds the volume percentage of 30% for mounted directory. Exiting...
----

// support log gather overview
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-log-gather-overview_{context}"]
= About {support-log-gather}

[role="_abstract"]
{support-log-gather} Operator builds on the functionality of the traditional `must-gather` tool to automate the collection of debugging data. It streamlines troubleshooting by packaging the collected information into a single `.tar` file and automatically uploading it to the specified Red{nbsp}Hat Support case.

The key features of {support-log-gather} include the following:

* **No administrator privileges required**: Enables you to collect and upload logs without needing elevated permissions, making it easier for non-administrators to gather data securely.

* **Simplified log collection**: Collects debugging data from the cluster, such as resource definitions and service logs.

* **Configurable data upload**: Provides configuration options to either automatically upload the `.tar` file to a support case, or store it locally for manual upload.

// Support log gather installation
// Module included in the following assemblies:
//
// * support/support-log-gather-operator-install.adoc

[id="support-log-gather-install-console_{context}"]
= Installing {support-log-gather} by using the web console

[role="_abstract"]
You can use the web console to install the {support-log-gather}.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Software Catalog*.

. In the filter box, enter *{support-log-gather}*.

. Select *{support-log-gather}*.

. From *Version* list, select the {support-log-gather} version, and click *Install*.

. On the *Install Operator* page, configure the installation settings:

.. Choose the *Installed Namespace* for the Operator.
+
The default Operator namespace is `must-gather-operator`. The `must-gather-operator` namespace is created automatically if it does not exist.

.. Select an *Update approval* strategy:

*** Select **Automatic** to have the Operator Lifecycle Manager (OLM) update the Operator automatically when a newer version is available.

*** Select **Manual** if Operator updates must be approved by a user with appropriate credentials.

.. Click *Install*.

.Verification

. Verify that the Operator is installed successfully:

.. Navigate to *Ecosystem* -> *Software Catalog*.

.. Verify that *{support-log-gather}* is listed with a *Status* of *Succeeded* in the `must-gather-operator` namespace.

. Verify that {support-log-gather} pods are running:

.. Navigate to *Workloads* -> *Pods*

.. Verify that the status of the {support-log-gather} pods is *Running*.
+
You can use the {support-log-gather} only after the pods are up and running.

// Module included in the following assemblies:
//
// * support/support-log-gather-operator-install.adoc

[id="support-log-gather-install-cli_{context}"]
= Installing {support-log-gather} by using the CLI

[role="_abstract"]
To enable automated log collection for support cases, you can install {support-log-gather} from the command-line interface (CLI).

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Create a new project named `must-gather-operator` by running the following command:
+
[source,terminal]
----
$ oc new-project must-gather-operator
----

. Create an `OperatorGroup` object:

.. Create a YAML file, for example, `operatorGroup.yaml`, that defines the `OperatorGroup` object:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: must-gather-operator
  namespace: must-gather-operator
spec: {}
----

.. Create the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc create -f operatorGroup.yaml
----

. Create a `Subscription` object:

.. Create a YAML file, for example, `subscription.yaml`, that defines the `Subscription` object:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: support-log-gather-operator
  namespace: must-gather-operator
spec:
  channel: tech-preview
  name: support-log-gather-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Automatic
----

.. Create the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc create -f subscription.yaml
----

.Verification

. Verify the status of the pods in the Operator namespace by running the following command.
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                                              READY   STATUS      RESTARTS   AGE
must-gather-operator-657fc74d64-2gg2w                             1/1     Running     0          13m
----
+
The status of all the pods must be `Running`.

. Verify that the subscription is created by running the following command:
+
[source,terminal]
----
$ oc get subscription -n must-gather-operator
----
+
.Example output
[source,terminal]
----
NAME                          PACKAGE                       SOURCE            CHANNEL
support-log-gather-operator   support-log-gather-operator   redhat-operators  tech-preview
----

. Verify that the Operator is installed by running the following command:
+
[source,terminal]
----
$ oc get csv -n must-gather-operator
----
+
.Example output
[source,terminal]
----
NAME                                  DISPLAY                VERSION   REPLACES   PHASE
support-log-gather-operator.v4.22.0   support log gather     4.22.0               Succeeded
----

//Support log gather configuration
// Module included in the following assemblies:
//
// * support/support-log-gather-operator-install.adoc

[id="support-log-gather-config-cli_{context}"]
= Configuring a {support-log-gather} instance

[role="_abstract"]
You must create a `MustGather` custom resource (CR) from the command-line interface (CLI) to automate the collection of diagnostic data from your cluster. This process also automatically uploads the data to a Red{nbsp}Hat Support case.

.Prerequisites

* You have installed the {oc-first} tool.

* You have installed {support-log-gather} in your cluster.

* You have a Red{nbsp}Hat Support case ID.

* You have created a Kubernetes secret containing your Red Hat Customer Portal credentials. The secret must contain a username field and a password field.

* If you are using a custom image, you have configured an `ImageStream` resource in the Operator namespace that references an approved custom image URL.

* You have created a service account. If you are using a custom image, you have created a service account with permissions to access the `ImageStream` resource.

.Procedure

. Create a YAML file for the `MustGather` CR, such as `support-log-gather.yaml`, that contains the following configuration:
+
.Example `support-log-gather.yaml`
[source, yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: MustGather
metadata:
  name: example-mg
  namespace: must-gather-operator
spec:
  serviceAccountName: my-service-account
  gatherSpec:
    command:
    - "/usr/bin/custom-gather"
    args:
    - "--verbose"
    - "--subsystem=network"
  imageStreamRef:
    name: "network-debug-tools"
    tag: "v1.2"
  proxyConfig:
    httpProxy: "http://proxy.example.com:8080"
    httpsProxy: "https://proxy.example.com:8443"
    noProxy: ".example.com,localhost"
  mustGatherTimeout: "1h30m9s"
  uploadTarget:
    type: SFTP
    sftp:
      caseID: "04230315"
      caseManagementAccountSecretRef:
        name: mustgather-creds
      host: "sftp.access.redhat.com"
  retainResourcesOnCompletion: true
  storage:
    type: PersistentVolume
    persistentVolume:
      claim:
        name: mustgather-pvc
      subPath: must-gather-bundles/case-04230315
----
+
For more information on the configuration parameters, see "Configuration parameters for MustGather custom resource".

. Create the `MustGather` object by running the following command:
+
[source, terminal]
----
$ oc create -f support-log-gather.yaml
----

.Verification

. Verify that the `MustGather` CR was created by running the following command:
+
[source, terminal]
----
$ oc get mustgather
----
+
.Example output
[source, terminal]
----
NAME          AGE
example-mg    7s
----

. Verify the status of the pods in the Operator namespace by running the following command.
+
[source, terminal]
----
$ oc get pods
----
+
.Example output
[source, terminal]
----
NAME                                                              READY   STATUS      RESTARTS   AGE
must-gather-operator-657fc74d64-2gg2w                             1/1     Running     0          13m
example-mg-gk8m8                                                  2/2     Running     0          13s
----
+
A new pod with a name based on the `MustGather` CR must be created. The status of all the pods must be `Running`.

. To monitor the progress of the file upload, view the logs of the upload container in the job pod by running the following command:
+
[source, terminal]
----
oc logs -f pod/example-mg-gk8m8 -c upload
----
+
When successful, the process must create an archive and upload it to the Red{nbsp}Hat Secure File Transfer Protocol (SFTP) server for the specified case.

// Module included in the following assemblies:
//
// * troubleshooting/gathering-diagnostic-data.adoc

[id="must-gather-operator-size-reduction-examples_{context}"]
= Configurations for reducing the must-gather log size

[role="_abstract"]
Large `must-gather` logs can take a significant amount of time to upload to support cases and also consume considerable cluster storage. You can optimize the size of the collected diagnostic data by applying specific configurations to your `MustGather` custom resource (CR).

The following examples demonstrate different methods for reducing the must-gather log size:

*Skipping rotated logs*
You can exclude older, rotated log files, such as `+*.gz+` or `+*.1+` files, from the collection by setting the shell variable `REDUCE_LOGS=skip_rotated_logs` before running the `gather` script.

.Example `MustGather` CR configured to skip rotated logs
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: MustGather
metadata:
  name: full-mustgather
spec:
  serviceAccountName: must-gather-operator
  gatherSpec:
    command:
      - /bin/sh
      - -c
      - |
        REDUCE_LOGS=skip_rotated_logs gather
  uploadTarget:
    type: SFTP
    sftp:
      caseID: '02527285'
      caseManagementAccountSecretRef:
        name: sftp-access-rh-creds
      internalUser: true
----

`REDUCE_LOGS=skip_rotated_logs gather`:: Sets the `REDUCE_LOGS` shell variable and executes the `gather` script. As a result, the script excludes the collection of rotated log files.

[role="_additional-resources"]
.Additional resources

* Understanding and creating service accounts

// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-log-gather-config-params_{context}"]
= Configuration parameters for MustGather custom resource

[role="_abstract"]
You can manage your `MustGather` custom resource (CR) by creating a YAML file that specifies the parameters for data collection and the upload process.
The following table provides an overview of the parameters that you can configure in the `MustGather` CR.

[cols="1,3,1", options="header"]
|===
|Parameter name |Description |Type

|`spec.gatherSpec.args`
|Optional: Specifies a list of command-line arguments. The Operator passes this value to the `args` field of the container. If you do not specify `spec.gatherSpec.command`, the specified arguments are appended to the default command of the Operator.
|List of strings

|`spec.gatherSpec.audit`
|Optional: Specifies whether to collect audit logs. The valid values are `true` and `false`. You must not set this field if you are using a custom image, or   `spec.gatherSpec.command` with the default image.
|`boolean`

|`spec.gatherSpec.command`
|Optional: Overrides the default command of the container. The Operator passes this value to the `command` field of the container.
|List of strings

|`spec.gatherSpec.since`
|Optional: Specifies a time duration to restrict log collection to entries newer than the specified duration. By default, the controller collects all available logs. You can specify either `spec.gatherSpec.since` or `spec.gatherSpec.sinceTime`, but not both.
|The value must be a number with a time unit. The valid units are `s` (seconds), `m` (minutes), or `h` (hours).

|`spec.gatherSpec.sinceTime`
|Optional: Specifies a timestamp to restrict log collection to entries newer than the specified timestamp. By default, the controller collects all available logs. You can specify either `spec.gatherSpec.since` or `spec.gatherSpec.sinceTime`, but not both.
|The value must be in RFC3339 format.

|`spec.imageStreamRef`
a|Optional: Overrides the default image by defining a specific custom image.

[NOTE]
====
Each `MustGather` CR supports only one custom image. To use multiple custom images, you must create a separate `MustGather` CR for each image.
====
|`object`

|`spec.imageStreamRef.name`
|Specifies the name of the `ImageStream` resource in the Operator namespace.
|`string`

|`spec.imageStreamRef.tag`
|Specifies the name of the tag within the `ImageStream` resource.
|`string`

|`spec.mustGatherTimeout`
|Optional: Specifies the time limit for the `must-gather` command to complete.
|The value must be a number with a time unit. The valid units are `s` (seconds), `m` (minutes), or `h` (hours). By default, no time limit is set.

|`spec.retainResourcesOnCompletion`
|Optional: Specifies whether to retain the `must-gather` job and its related resources after the completion of data collection. The valid values are `true` and `false`. The default value is `false`.
|`boolean`

|`spec.serviceAccountName`
a|Optional: Specifies the name of the service account. The default value is `default`.

[NOTE]
====
Because the `default` service account has minimal permissions, you can specify the service account that you created.
====
|`string`

|`spec.storage`
|Optional: Defines the storage configuration for the `must-gather` bundle.
|`Object`

|`spec.storage.persistentVolume`
|Defines the details of the persistent volume.
|`Object`

|`spec.storage.persistentVolume.claim`
|Defines the details of the persistent volume claim (PVC).
|`Object`

|`spec.storage.persistentVolume.claim.name`
|Specifies the name of the PVC to be used for storage.
|`string`

|`spec.storage.persistentVolume.subPath`
|Optional: Specifies the path within the PVC to store the bundle.
|`string`

|`spec.storage.type`
|Defines the type of storage. The only supported value is `PersistentVolume`.
|`string`

|`spec.uploadTarget`
|Optional: Defines the upload location for the `must-gather` bundle.
|`Object`

|`spec.uploadTarget.sftp.caseID`
|Specifies the Red{nbsp}Hat Support case ID for which the diagnostic data is collected.
|`string`

|`spec.uploadTarget.sftp.caseManagementAccountSecretRef`
|Defines the credentials required for authenticating and uploading the files to the Red{nbsp}Hat Customer Portal support case. The value must contain a `username` and `password` field.
|`Object`

|`spec.uploadTarget.sftp.caseManagementAccountSecretRef.name`
|Specifies the name of the Kubernetes secret that contains the credentials.
|`string`

|`spec.uploadTarget.sftp.host`
|Optional: Specifies the destination server for the bundle upload. By default, the bundle is uploaded to `sftp.access.redhat.com`.
|

|`spec.uploadTarget.sftp.internalUser`
|Optional: Specifies whether the user provided in the `caseManagementAccountSecretRef` is a Red{nbsp}Hat internal user. The valid values are `true` and `false`. The default value is `false`.
|`boolean`

|`spec.uploadTarget.type`
|Specifies the type of upload location for the `must-gather` bundle. The only supported value is `SFTP`.
|`string`

|===

[NOTE]
====
If you do not specify `spec.uploadTarget` or `spec.storage`, the pod saves the data to an ephemeral volume and the data is permanently deleted when the pod terminates.
====

//Support log gather uninstallation
// Module included in the following assemblies:
//
// * support/support-log-gather-uninstall.adoc

[id="support-log-gather-uninstall-console_{context}"]
= Uninstalling {support-log-gather}

[role="_abstract"]
You can uninstall the {support-log-gather} by using the web console.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

* You have access to the OpenShift Container Platform web console.

* The {support-log-gather} is installed.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Uninstall the {support-log-gather} Operator.

.. Navigate to *Ecosystem* -> *Installed Operators*.

.. Click the Options menu {kebab} next to the *{support-log-gather}* entry and click *Uninstall Operator*.

.. In the confirmation dialog, click *Uninstall*.

// Module included in the following assemblies:
//
// * support/support-log-gather-uninstall.adoc

[id="support-log-gather-remove-resources-console_{context}"]
= Removing {support-log-gather} resources

[role="_abstract"]
Once you have uninstalled the {support-log-gather}, you can remove the associated resources from your cluster.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Delete the component deployments in the must-gather-operator namespace.:

.. Click the *Project* drop-down menu to view the list of all available projects, and select the *must-gather-operator* project.

.. Navigate to *Workloads* -> *Deployments*.

.. Select the deployment that you want to delete.

.. Click the *Actions* drop-down menu, and select *Delete Deployment*.

..  In the confirmation dialog box, click *Delete* to delete the deployment.

.. Alternatively, delete deployments of the components present in the `must-gather-operator` namespace by using the command-line interface (CLI).
+
[source,terminal]
----
$ oc delete deployment -n must-gather-operator -l operators.coreos.com/support-log-gather-operator.must-gather-operator
----

. Optional: Remove the custom resource definitions (CRDs) that were installed by the {support-log-gather}:

.. Navigate to *Administration* -> *CustomResourceDefinitions*.

.. Enter `MustGather` in the *Name* field to filter the CRDs.

.. Click the Options menu {kebab} next to each of the following CRDs, and select *Delete Custom Resource Definition*:

*** `MustGather`

. Optional: Remove the `must-gather-operator` namespace.

.. Navigate to *Administration* -> *Namespaces*.

.. Click the Options menu {kebab} next to the *must-gather-operator* and select *Delete Namespace*.

.. In the confirmation dialog box, enter `must-gather-operator` and click *Delete*.

// Obtain your cluster identifier
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-get-cluster-id_{context}"]
= Obtaining your cluster ID

[role="_abstract"]
When providing information to Red Hat Support, it is helpful to provide the unique identifier for your cluster. You can have your cluster ID autofilled by using the OpenShift Container Platform web console. You can also manually obtain your cluster ID by using the web console or the OpenShift CLI (`oc`).

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have access to the web console or the OpenShift CLI (`oc`) installed.

.Procedure
* To manually obtain your cluster ID using {cluster-manager-url}:
.. Navigate to *Cluster List*.
.. Click on the name of the cluster you need to open a support case for.
.. Find the value in the *Cluster ID* field of the *Details* section of the *Overview* tab.
* To open a support case and have your cluster ID autofilled using the web console:
.. From the toolbar, navigate to *(?) Help* and select *Share Feedback* from the list.
.. Click *Open a support case* from the *Tell us about your experience* window.

* To open a bug and have your cluster ID autofilled using the web console:
.. From the toolbar, navigate to *(?) Help* -> *Report Bug*.
.. The *Cluster ID* value is autofilled after you click `Submit Bug`.

* To manually obtain your cluster ID using the web console:
.. Navigate to *Home* -> *Overview*.
.. The value is available in the *Cluster ID* field of the *Details* section.

* To obtain your cluster ID using the OpenShift CLI (`oc`), run the following command:
+
[source,terminal]
----
$ oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}'
----

// About `sosreport`
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="about-sosreport_{context}"]
= About sosreport

[role="_abstract"]
`sosreport` is a tool that collects configuration details, system information, and diagnostic data from {op-system-base-full} and {op-system-first} systems. `sosreport` provides a standardized way to collect diagnostic information relating to a node, which can then be provided to Red Hat Support for issue diagnosis.

In some support interactions, Red Hat Support may ask you to collect a `sosreport` archive for a specific OpenShift Container Platform node. For example, it might sometimes be necessary to review system logs or other node-specific data that is not included within the output of `oc adm must-gather`.

// Generating a `sosreport` archive for an OpenShift Container Platform cluster node
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-generating-a-sosreport-archive_{context}"]
= Generating a sosreport archive for an OpenShift Container Platform cluster node

[role="_abstract"]
The recommended way to generate a `sosreport` for an OpenShift Container Platform  cluster node is through a debug pod.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have SSH access to your hosts.
* You have installed the OpenShift CLI (`oc`).
* You have a Red Hat standard or premium Subscription.
* You have a Red Hat Customer Portal account.
* You have an existing Red Hat Support case ID.

.Procedure

. Obtain a list of cluster nodes:
+
[source,terminal]
----
$ oc get nodes
----

. Enter into a debug session on the target node. This step instantiates a debug pod called `<node_name>-debug`:
+
[source,terminal]
----
$ oc debug node/my-cluster-node
----
+
To enter into a debug session on the target node that is tainted with the `NoExecute` effect, add a toleration to a dummy namespace, and start the debug pod in the dummy namespace:
+
[source,terminal]
----
$ oc new-project dummy
----
+
[source,terminal]
----
$ oc patch namespace dummy --type=merge -p '{"metadata": {"annotations": { "scheduler.alpha.kubernetes.io/defaultTolerations": "[{\"operator\": \"Exists\"}]"}}}'
----
+
[source,terminal]
----
$ oc debug node/my-cluster-node
----
+
. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
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

. Start a `toolbox` container, which includes the required binaries and plugins to run `sosreport`:
+
[source,terminal]
----
# toolbox
----
+
[NOTE]
====
If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start...`. Remove the running toolbox container with `podman rm toolbox-` and spawn a new toolbox container, to avoid issues with `sosreport` plugins.
====
+
. Collect a `sosreport` archive.
.. Run the `sos report` command to collect necessary troubleshooting data on `crio` and `podman`:
+
[source,terminal]
----
# sos report -k crio.all=on -k crio.logs=on  -k podman.all=on -k podman.logs=on
----
+
where::
* `-k` enables you to define `sosreport` plugin parameters outside of the defaults.
+
.. Optional: To include information on OVN-Kubernetes networking configurations from a node in your report, run the following command:
+
[source,terminal]
----
# sos report --all-logs
----

.. Press *Enter* when prompted, to continue.
+
.. Provide the Red Hat Support case ID. `sosreport` adds the ID to the archive's file name.
+
.. The `sosreport` output provides the archive's location and checksum. The following sample output references support case ID `01234567`:
+
[source,terminal]
----
Your sosreport has been generated and saved in:
  /host/var/tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz

The checksum is: 382ffc167510fd71b4f12a4f40b97a4e
----
+
where::
* The `sosreport` archive's file path is outside of the `chroot` environment because the toolbox container mounts the host's root directory at `/host`.

. Provide the `sosreport` archive to Red Hat Support for analysis, using one of the following methods.
+
* Upload the file to an existing Red Hat support case.
.. Concatenate the `sosreport` archive by running the `oc debug node/<node_name>` command and redirect the output to a file. This command assumes you have exited the previous `oc debug` session:
+
[source,terminal]
----
$ oc debug node/my-cluster-node -- bash -c 'cat /host/var/tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz' > /tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz
----
+
where::
* The debug container mounts the host's root directory at `/host`. Reference the absolute path from the debug container's root directory, including `/host`, when specifying target files for concatenation.
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Transferring a `sosreport` archive from a cluster node by using `scp` is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to copy a `sosreport` archive from a node by running `scp core@<node>.<cluster_name>.<base_domain>:<file_path> <local_path>`.
====
+
.. Navigate to an existing support case within the *Customer Support* page of the Red Hat Customer Portal.
+
.. Select *Attach files* and follow the prompts to upload the file.

// Querying bootstrap node journal logs
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="querying-bootstrap-node-journal-logs_{context}"]
= Querying bootstrap node journal logs

[role="_abstract"]
If you experience bootstrap-related issues, you can gather `bootkube.service` `journald` unit logs and container logs from the bootstrap node.

.Prerequisites

* You have SSH access to your bootstrap node.
* You have the fully qualified domain name of the bootstrap node.

.Procedure

. Query `bootkube.service` `journald` unit logs from a bootstrap node during OpenShift Container Platform installation. Replace `<bootstrap_fqdn>` with the bootstrap node's fully qualified domain name:
+
[source,terminal]
----
$ ssh core@<bootstrap_fqdn> journalctl -b -f -u bootkube.service
----
+
[NOTE]
====
The `bootkube.service` log on the bootstrap node outputs etcd `connection refused` errors, indicating that the bootstrap server is unable to connect to etcd on control plane nodes. After etcd has started on each control plane node and the nodes have joined the cluster, the errors should stop.
====
+
. Collect logs from the bootstrap node containers using `podman` on the bootstrap node. Replace `<bootstrap_fqdn>` with the bootstrap node's fully qualified domain name:
+
[source,terminal]
----
$ ssh core@<bootstrap_fqdn> 'for pod in $(sudo podman ps -a -q); do sudo podman logs $pod; done'
----

// Querying cluster node journal logs
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc
// * support/troubleshooting/verifying-node-health.adoc

[id="querying-cluster-node-journal-logs_{context}"]
= Querying cluster node journal logs

[role="_abstract"]
You can gather `journald` unit logs and other logs within `/var/log` on individual cluster nodes.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
+
[NOTE]
====
In OpenShift Container Platform deployments, customers who are not using the Customer Cloud Subscription (CCS) model cannot use the `oc adm node-logs` command as it requires `cluster-admin` privileges.
====
+
* You have installed the OpenShift CLI (`oc`).
* Your API service is still functional.
* You have SSH access to your hosts.

.Procedure

. Query `kubelet` `journald` unit logs from OpenShift Container Platform cluster nodes. The following example queries control plane nodes only:
* Query `kubelet` `journald` unit logs from OpenShift Container Platform cluster nodes. The following example queries worker nodes only:
+
[source,terminal]
----
$ oc adm node-logs --role=master -u kubelet  <1>
----
[source,terminal]
----
$ oc adm node-logs --role=worker -u kubelet
----
`kubelet`:: Replace as appropriate to query other unit logs.

. Collect logs from specific subdirectories under `/var/log/` on cluster nodes.
+
.. Retrieve a list of logs contained within a `/var/log/` subdirectory. The following example lists files in `/var/log/openshift-apiserver/` on all control plane nodes:
+
[source,terminal]
----
$ oc adm node-logs --role=master --path=openshift-apiserver
----
+
.. Inspect a specific log within a `/var/log/` subdirectory. The following example outputs `/var/log/openshift-apiserver/audit.log` contents from all control plane nodes:
+
[source,terminal]
----
$ oc adm node-logs --role=master --path=openshift-apiserver/audit.log
----
+
.. If the API is not functional, review the logs on each node using SSH instead. The following example tails `/var/log/openshift-apiserver/audit.log`:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo tail -f /var/log/openshift-apiserver/audit.log
----
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. Before attempting to collect diagnostic data over SSH, review whether the data collected by running `oc adm must gather` and other `oc` commands is sufficient instead. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>`.
====

// Network trace methods
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-network-trace-methods_{context}"]
= Network trace methods

[role="_abstract"]
Collecting network traces, in the form of packet capture records, can assist Red Hat Support with troubleshooting network issues.

OpenShift Container Platform supports two ways of performing a network trace.
Review the following table and choose the method that meets your needs.

.Supported methods of collecting a network trace
[cols="1,4a",options="header"]
|===

|Method
|Benefits and capabilities

|Collecting a host network trace
|You perform a packet capture for a duration that you specify on one or more nodes at the same time.
The packet capture files are transferred from nodes to the client machine when the specified duration is met.

You can troubleshoot why a specific action triggers network communication issues. Run the packet capture, perform the action that triggers the issue, and use the logs to diagnose the issue.

|Collecting a network trace from an OpenShift Container Platform node or container
|You perform a packet capture on one node or one container.
You run the `tcpdump` command interactively, so you can control the duration of the packet capture.

You can start the packet capture manually, trigger the network communication issue, and then stop the packet capture manually.

This method uses the `cat` command and shell redirection to copy the packet capture data from the node or container to the client machine.

|===

// Collecting a host network trace
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-collecting-host-network-trace_{context}"]
= Collecting a host network trace

[role="_abstract"]
Sometimes, troubleshooting a network-related issue is simplified by tracing network communication and capturing packets on multiple nodes at the same time.

You can use a combination of the `oc adm must-gather` command and the `registry.redhat.io/openshift4/network-tools-rhel8` container image to gather packet captures from nodes.
Analyzing packet captures can help you troubleshoot network communication issues.

You can use a combination of the `oc adm must-gather` command and the `quay.io/openshift/origin-network-tools:latest` container image to gather packet captures from nodes.
Analyzing packet captures can help you troubleshoot network communication issues.

The `oc adm must-gather` command is used to run the `tcpdump` command in pods on specific nodes.
The `tcpdump` command records the packet captures in the pods.
When the `tcpdump` command exits, the `oc adm must-gather` command transfers the files with the packet captures from the pods to your client machine.

[TIP]
====
The sample command in the following procedure demonstrates performing a packet capture with the `tcpdump` command.
However, you can run any command in the container image that is specified in the `--image` argument to gather troubleshooting information from multiple nodes at the same time.
====

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
+
[NOTE]
====
In OpenShift Container Platform deployments, customers who are not using the Customer Cloud Subscription (CCS) model cannot use the `oc adm must-gather` command as it requires `cluster-admin` privileges.
====
+
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Run a packet capture from the host network on some nodes by running the following command:
+
[source,terminal]
----
$ oc adm must-gather \
    --dest-dir /tmp/captures \
    --source-dir '/tmp/tcpdump/' \
    --image registry.redhat.io/openshift4/network-tools-rhel8:latest \
    --node-selector 'node-role.kubernetes.io/worker' \
    --host-network=true \
    --timeout 30s \
    -- \
    tcpdump -i any \
    -w /tmp/tcpdump/%Y-%m-%dT%H:%M:%S.pcap -W 1 -G 300
----
+
where:

`--dest-dir /tmp/captures`:: The `--dest-dir` argument specifies that `oc adm must-gather` stores the packet captures in directories that are relative to `/tmp/captures` on the client machine. You can specify any writable directory.
`--source-dir '/tmp/tcpdump/'`:: When `tcpdump` is run in the debug pod that `oc adm must-gather` starts, the `--source-dir` argument specifies that the packet captures are temporarily stored in the `/tmp/tcpdump` directory on the pod.
`--image registry.redhat.io/openshift4/network-tools-rhel8:latest`:: The `--image` argument specifies a container image that includes the `tcpdump` command.
`--node-selector 'node-role.kubernetes.io/worker'`:: The `--node-selector` argument and example value specifies to perform the packet captures on the worker nodes. As an alternative, you can specify the `--node-name` argument instead to run the packet capture on a single node. If you omit both the `--node-selector` and the `--node-name` argument, the packet captures are performed on all nodes.
`--host-network=true`:: The `--host-network=true` argument is required so that the packet captures are performed on the network interfaces of the node.
`--timeout 30s`:: The `--timeout` argument and value specify to run the debug pod for 30 seconds. If you do not specify the `--timeout` argument and a duration, the debug pod runs for 10 minutes.
`-i any`:: The `-i any` argument for the `tcpdump` command specifies to capture packets on all network interfaces. As an alternative, you can specify a network interface name.

. Run a packet capture from the host network on some nodes by running the following command:
+
[source,terminal]
----
$ oc adm must-gather \
    --dest-dir /tmp/captures \
    --source-dir '/tmp/tcpdump/' \
    --image quay.io/openshift/origin-network-tools:latest \
    --node-selector 'node-role.kubernetes.io/worker' \
    --host-network=true \
    --timeout 30s \
    -- \
    tcpdump -i any \
    -w /tmp/tcpdump/%Y-%m-%dT%H:%M:%S.pcap -W 1 -G 300
----
+
where:

`--dest-dir /tmp/captures`:: The `--dest-dir` argument specifies that `oc adm must-gather` stores the packet captures in directories that are relative to `/tmp/captures` on the client machine. You can specify any writable directory.
`--source-dir '/tmp/tcpdump/'`:: When `tcpdump` is run in the debug pod that `oc adm must-gather` starts, the `--source-dir` argument specifies that the packet captures are temporarily stored in the `/tmp/tcpdump` directory on the pod.
`--image quay.io/openshift/origin-network-tools:latest`:: The `--image` argument specifies a container image that includes the `tcpdump` command.
`--node-selector 'node-role.kubernetes.io/worker'`:: The `--node-selector` argument and example value specifies to perform the packet captures on the worker nodes. As an alternative, you can specify the `--node-name` argument instead to run the packet capture on a single node. If you omit both the `--node-selector` and the `--node-name` argument, the packet captures are performed on all nodes.
`--host-network=true`:: The `--host-network=true` argument is required so that the packet captures are performed on the network interfaces of the node.
`--timeout 30s`:: The `--timeout` argument and value specify to run the debug pod for 30 seconds. If you do not specify the `--timeout` argument and a duration, the debug pod runs for 10 minutes.
`-i any`:: The `-i any` argument for the `tcpdump` command specifies to capture packets on all network interfaces. As an alternative, you can specify a network interface name.

. Perform the action, such as accessing a web application, that triggers the network communication issue while the network trace captures packets.

. Review the packet capture files that `oc adm must-gather` transferred from the pods to your client machine:
+
[source,text]
----
tmp/captures
├── event-filter.html
├── ip-10-0-192-217-ec2-internal
│   └── registry-redhat-io-openshift4-network-tools-rhel8-sha256-bca...
│       └── 2022-01-13T19:31:31.pcap
├── ip-10-0-201-178-ec2-internal
│   └── registry-redhat-io-openshift4-network-tools-rhel8-sha256-bca...
│       └── 2022-01-13T19:31:30.pcap
├── ip-...
└── timestamp
----
+
where:

`ip-10-0-192-217-ec2-internal`, `ip-10-0-201-178-ec2-internal`:: The packet captures are stored in directories that identify the hostname, container, and file name.
If you did not specify the `--node-selector` argument, then the directory level for the hostname is not present.

. Review the packet capture files that `oc adm must-gather` transferred from the pods to your client machine:
+
[source,text]
----
tmp/captures
├── event-filter.html
├── ip-10-0-192-217-ec2-internal
│   └── quay.io/openshift/origin-network-tools:latest...
│       └── 2022-01-13T19:31:31.pcap
├── ip-10-0-201-178-ec2-internal
│   └── quay.io/openshift/origin-network-tools:latest...
│       └── 2022-01-13T19:31:30.pcap
├── ip-...
└── timestamp
----
+
where:

`ip-10-0-192-217-ec2-internal`, `ip-10-0-201-178-ec2-internal`:: The packet captures are stored in directories that identify the hostname, container, and file name.
If you did not specify the `--node-selector` argument, then the directory level for the hostname is not present.

// Collecting a network trace from an OpenShift Container Platform node or container
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-collecting-network-trace_{context}"]
= Collecting a network trace from an OpenShift Container Platform node or container

[role="_abstract"]
When investigating potential network-related OpenShift Container Platform issues, Red Hat Support might request a network packet trace from a specific OpenShift Container Platform cluster node or from a specific container. The recommended method to capture a network trace in OpenShift Container Platform is through a debug pod.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
+
[NOTE]
====
In OpenShift Container Platform deployments, customers who are not using the Customer Cloud Subscription (CCS) model cannot use the `oc debug` command as it requires `cluster-admin` privileges.
====
+
* You have installed the OpenShift CLI (`oc`).
* You have an existing Red Hat Support case ID.
* You have a Red Hat standard or premium Subscription.
* You have a Red Hat Customer Portal account.
* You have SSH access to your hosts.

.Procedure

. Obtain a list of cluster nodes:
+
[source,terminal]
----
$ oc get nodes
----

. Enter into a debug session on the target node. This step instantiates a debug pod called `<node_name>-debug`:
+
[source,terminal]
----
$ oc debug node/my-cluster-node
----

. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
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

. From within the `chroot` environment console, obtain the node's interface names:
+
[source,terminal]
----
# ip ad
----

. Start a `toolbox` container, which includes the required binaries and plugins to run `sosreport`:
+
[source,terminal]
----
# toolbox
----
+
[NOTE]
====
If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start...`. To avoid `tcpdump` issues, remove the running toolbox container with `podman rm toolbox-` and spawn a new toolbox container.
====

. Initiate a `tcpdump` session on the cluster node and redirect output to a capture file. This example uses `ens5` as the interface name:
+
[source,terminal]
----
$ tcpdump -nn -s 0 -i ens5 -w /host/var/tmp/my-cluster-node_$(date +%d_%m_%Y-%H_%M_%S-%Z).pcap
----
+
where:

`/host/var/tmp/my-cluster-node_$(date +%d_%m_%Y-%H_%M_%S-%Z).pcap`:: The `tcpdump` capture file's path is outside of the `chroot` environment because the toolbox container mounts the host's root directory at `/host`.

. If a `tcpdump` capture is required for a specific container on the node, follow these steps.
.. Determine the target container ID. The `chroot host` command precedes the `crictl` command in this step because the toolbox container mounts the host's root directory at `/host`:
+
[source,terminal]
----
# chroot /host crictl ps
----
+
.. Determine the container's process ID. In this example, the container ID is `a7fe32346b120`:
+
[source,terminal]
----
# chroot /host crictl inspect --output yaml a7fe32346b120 | grep 'pid' | awk '{print $2}'
----
+
.. Initiate a `tcpdump` session on the container and redirect output to a capture file. This example uses `49628` as the container's process ID and `ens5` as the interface name. The `nsenter` command enters the namespace of a target process and runs a command in its namespace. because the target process in this example is a container's process ID, the `tcpdump` command is run in the container's namespace from the host:
+
[source,terminal]
----
# nsenter -n -t 49628 -- tcpdump -nn -i ens5 -w /host/var/tmp/my-cluster-node-my-container_$(date +%d_%m_%Y-%H_%M_%S-%Z).pcap
----
+
where:

`/host/var/tmp/my-cluster-node-my-container_$(date +%d_%m_%Y-%H_%M_%S-%Z).pcap`:: The `tcpdump` capture file's path is outside of the `chroot` environment because the toolbox container mounts the host's root directory at `/host`.

. Provide the `tcpdump` capture file to Red Hat Support for analysis, using one of the following methods.
+
* Upload the file to an existing Red Hat support case.

.. Concatenate the `sosreport` archive by running the `oc debug node/<node_name>` command and redirect the output to a file. This command assumes you have exited the previous `oc debug` session:
+
[source,terminal]
----
$ oc debug node/my-cluster-node -- bash -c 'cat /host/var/tmp/my-tcpdump-capture-file.pcap' > /tmp/my-tcpdump-capture-file.pcap
----
+
where:

`/host/var/tmp/my-tcpdump-capture-file.pcap`:: The debug container mounts the host's root directory at `/host`. Reference the absolute path from the debug container's root directory, including `/host`, when specifying target files for concatenation.
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Transferring a `tcpdump` capture file from a cluster node by using `scp` is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to copy a `tcpdump` capture file from a node by running `scp core@<node>.<cluster_name>.<base_domain>:<file_path> <local_path>`.
====

.. Navigate to an existing support case within the *Customer Support* page of the Red Hat Customer Portal.

.. Select *Attach files* and follow the prompts to upload the file.

// TODO - Add details relating to https://github.com/openshift/must-gather/pull/156 within the procedure.

// Collecting a host network trace

// Providing diagnostic data to Red Hat Support
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-providing-diagnostic-data-to-red-hat_{context}"]
= Providing diagnostic data to Red Hat Support

[role="_abstract"]
When investigating OpenShift Container Platform issues, Red Hat Support might ask you to upload diagnostic data to a support case. Files can be uploaded to a support case through the Red Hat Customer Portal.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
+
[NOTE]
====
In OpenShift Container Platform deployments, customers who are not using the Customer Cloud Subscription (CCS) model cannot use the `oc debug` command as it requires `cluster-admin` privileges.
====
+
* You have installed the OpenShift CLI (`oc`).
* You have SSH access to your hosts.
* You have a Red Hat standard or premium Subscription.
* You have a Red Hat Customer Portal account.
* You have an existing Red Hat Support case ID.

.Procedure

* Upload diagnostic data to an existing Red Hat support case through the Red Hat Customer Portal.
.. Concatenate a diagnostic file contained on an OpenShift Container Platform node by using the `oc debug node/<node_name>` command and redirect the output to a file. The following example copies `/host/var/tmp/my-diagnostic-data.tar.gz` from a debug container to `/var/tmp/my-diagnostic-data.tar.gz`:
+
[source,terminal]
----
$ oc debug node/my-cluster-node -- bash -c 'cat /host/var/tmp/my-diagnostic-data.tar.gz' > /var/tmp/my-diagnostic-data.tar.gz
----
+
where:

`/host/var/tmp/my-diagnostic-data.tar.gz`:: The debug container mounts the host's root directory at `/host`. Reference the absolute path from the debug container's root directory, including `/host`, when specifying target files for concatenation.
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Transferring files from a cluster node by using `scp` is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to copy diagnostic files from a node by running `scp core@<node>.<cluster_name>.<base_domain>:<file_path> <local_path>`.
====

.. Navigate to an existing support case within the *Customer Support* page of the Red Hat Customer Portal.

.. Select *Attach files* and follow the prompts to upload the file.

// About `toolbox`
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="about-toolbox_{context}"]
= About `toolbox`

[role="_abstract"]
`toolbox` is a tool that starts a container on a {op-system-first} system. The tool is primarily used to start a container that includes the required binaries and plugins that are needed to run commands such as `sosreport`.

The primary purpose for a `toolbox` container is to gather diagnostic information and to provide it to Red Hat Support. However, if additional diagnostic tools are required, you can add RPM packages or run an image that is an alternative to the standard support tools image.

`toolbox` is a tool that starts a container on a {op-system-first} system. The tool is primarily used to start a container that includes the required binaries and plugins that are needed to run your favorite debugging or admin tools.

// Installing packages to a toolbox container

// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="installing-packages-to-a-toolbox-container_{context}"]
= Installing packages to a `toolbox` container

[role="_abstract"]
By default, running the `toolbox` command starts a container with the `registry.redhat.io/rhel9/support-tools:latest` image. This image contains the most frequently used support tools. If you need to collect node-specific data that requires a support tool that is not part of the image, you can install additional packages.

By default, running the `toolbox` command starts a container with the `quay.io/fedora/fedora` image. This image contains the most frequently used support tools. If you need to collect node-specific data that requires a support tool that is not part of the image, you can install additional packages.

.Prerequisites

* You have accessed a node with the `oc debug node/<node_name>` command.
* You can access your system as a user with root privileges.

.Procedure

. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----

. Start the toolbox container:
+
[source,terminal]
----
# toolbox
----

. Install the additional package, such as `wget`:
+
[source,terminal]
----
# dnf install -y <package_name>
----

// Starting an alternative image with toolbox

// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="starting-an-alternative-image-with-toolbox_{context}"]
= Starting an alternative image with `toolbox`

[role="_abstract"]
By default, running the `toolbox` command starts a container with the `registry.redhat.io/rhel9/support-tools:latest` image.

[NOTE]
====
You can start an alternative image by creating a `.toolboxrc` file and specifying the image to run. However, running an older version of the `support-tools` image, such as `registry.redhat.io/rhel8/support-tools:latest`,  is not supported on OpenShift Container Platform .
====

By default, running the `toolbox` command starts a container with the `quay.io/fedora/fedora` image. You can start an alternative image by creating a `.toolboxrc` file and specifying the image to run.

.Prerequisites

* You have accessed a node with the `oc debug node/<node_name>` command.
* You can access your system as a user with root privileges.

.Procedure

. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----

. Optional: If you need to use an alternative image instead of the default image, create a `.toolboxrc` file in the home directory for the root user ID, and specify the image metadata:
+
[source,text]
----
REGISTRY=quay.io
IMAGE=fedora/fedora:latest
TOOLBOX_NAME=toolbox-fedora-latest
----
+
where:

`REGISTRY=quay.io`:: Optional: Specify an alternative container registry.
`IMAGE=fedora/fedora:latest`:: Specify an alternative image to start.
`TOOLBOX_NAME=toolbox-fedora-latest`:: Optional: Specify an alternative name for the toolbox container.

. Start a toolbox container by entering the following command:
+
[source,terminal]
----
# toolbox
----
+
[NOTE]
====
If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start...`. To avoid issues with `sosreport` plugins, remove the running toolbox container with `podman rm toolbox-` and then spawn a new toolbox container.
====
