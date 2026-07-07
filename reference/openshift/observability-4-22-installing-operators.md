---
title: "Installing the Network Observability Operator"
type: reference
domain: openshift
slug: observability-4-22-installing-operators
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/installing-operators
version: 4.22
family: observability
documentKind: "Documentation"
---

# Installing the Network Observability Operator

[id="installing-network-observability-operators"]
= Installing the Network Observability Operator

[role="_abstract"]
Installing the Loki Operator is recommended before using the Network Observability Operator. You can use network observability without Loki, but special considerations apply if you only need metrics or external exporters.

- Commenting out for now.
- This may need to be reworked as part of NetObserv moving to the stand alone format. Network Observability Operator without Loki may be a separate user journey to setup.

Installing Loki is a recommended prerequisite for using the Network Observability Operator. You can choose to use Network observability without Loki, but there are some considerations for doing this, described in the previously linked section.

The {loki-op} integrates a gateway that implements multi-tenancy and authentication with Loki for data flow storage. The `LokiStack` resource manages Loki, which is a scalable, highly-available, multi-tenant log aggregation system, and a web proxy with OpenShift Container Platform authentication. The `LokiStack` proxy uses OpenShift Container Platform authentication to enforce multi-tenancy and facilitate the saving and indexing of data in Loki log stores.

// module included in the following assemblies:
// networking/network_observability/installing-operators.adoc

[id="network-observability-without-loki_{context}"]
= Network observability without Loki

[role="_abstract"]
Compare the features available with network observability with and without installing the {loki-op}.

If you only want to export flows to a Kafka consumer or IPFIX collector, or you only need dashboard metrics, then you do not need to install Loki or provide storage for Loki. The following table compares available features with and without Loki.

.Comparison of feature availability with and without Loki
[options="header"]
|===
|                                     | *With Loki* | *Without Loki*
| *Exporters*                         | X | X
| *Multi-tenancy*                     | X | X
| *Complete filtering and aggregations capabilities* ^[1]^| X |
| *Partial filtering and aggregations capabilities* ^[2]^ | X | X
| *Flow-based metrics and dashboards* | X | X
| *Traffic flows view overview* ^[3]^  | X | X
| *Traffic flows view table*       | X |
| *Topology view*                | X | X
| *OpenShift Container Platform console Network Traffic tab integration* | X | X
|===
[.small]
--
1. Such as per pod.
2. Such as per workload or namespace.
3. Statistics on packet drops are only available with Loki.
--

[role="_additional-resources"]
.Additional resources
* Export enriched network flow data

// Module included in the following assemblies:

// * networking/network_observability/installing-operators.adoc

[id="network-observability-loki-installation_{context}"]
= Installing the {loki-op}

[role="_abstract"]
Install the supported {loki-op} version from the software catalog to enable the secure `LokiStack` instance, which provides automatic in-cluster authentication and authorization for network observability.

The {loki-op} versions 6.0+ are the supported {loki-op} versions for network observability; these versions provide the ability to create a `LokiStack` instance using the `openshift-network` tenant configuration mode and provide fully-automatic, in-cluster authentication and authorization support for network observability.

.Prerequisites

* You have administrator permissions.
* You have access to the OpenShift Container Platform web console.
* You have access to a supported object store. For example: AWS S3, Google Cloud Storage, Azure, Swift, Minio, or OpenShift Data Foundation.

.Procedure
. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.
. Choose  *{loki-op}* from the list of available Operators, and click *Install*.
. Under *Installation Mode*, select *All namespaces on the cluster*.

.Verification
. Verify that you installed the {loki-op}. Visit the *Ecosystem* -> *Installed Operators* page and look for *{loki-op}*.
. Verify that *{loki-op}* is listed with *Status* as *Succeeded* in all the projects.

[IMPORTANT]
====
To uninstall Loki, refer to the uninstallation process that corresponds with the method you used to install Loki. You might have remaining `ClusterRoles` and `ClusterRoleBindings`, data stored in object store, and persistent volume that must be removed.
====

// Module included in the following assemblies:

// * networking/network_observability/installing-operators.adoc

[id="network-observability-loki-secret_{context}"]
= Creating a secret for Loki storage

[role="_abstract"]
Create a secret with cloud storage credentials, such as for {aws-first}, to allow the Loki Operator to access the necessary object store for log persistence.

The {loki-op} supports a few log storage options, such as AWS S3, {gcp-full} Storage, Azure, Swift, Minio, {rh-storage}. The following example shows how to create a secret for AWS S3 storage. The secret created in this example, `loki-s3`, is referenced in "Creating a LokiStack custom resource". You can create this secret in the web console or CLI.

.Procedure

. Using the web console, navigate to the *Project* -> *All Projects* dropdown and select *Create Project*.
. Name the project `netobserv` and click *Create*.
. Navigate to the Import icon, *+*, in the top right corner. Paste your YAML file into the editor.
+
The following shows an example secret YAML file for S3 storage:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: loki-s3
  namespace: netobserv-loki
stringData:
  access_key_id: QUtJQUlPU0ZPRE5ON0VYQU1QTEUK
  access_key_secret: d0phbHJYVXRuRkVNSS9LN01ERU5HL2JQeFJmaUNZRVhBTVBMRUtFWQo=
  bucketnames: s3-bucket-name
  endpoint: https://s3.eu-central-1.amazonaws.com
  region: eu-central-1
----
+
where:

`metadata.namespace`:: Specifies the namespace for the Loki S3 secret. While this example uses `netobserv-loki`, you can use a different namespace for different components.
`stringData.access_key_id`:: Specifies the access key ID for the S3 bucket.
`stringData.access_key_secret`:: Specifies the secret access key for the S3 bucket.
`stringData.bucketnames`:: Specifies the name of the S3 bucket.
`stringData.endpoint`:: Specifies the endpoint URL for the S3 service.
`stringData.region`:: Specifies the AWS region where the bucket is located.

.Verification
* After you create the secret, you view the secret listed under *Workloads* -> *Secrets* in the web console.

[role="_additional-resources"]
.Additional resources
* Creating a LokiStack custom resource
* Flow Collector API Reference
* Flow Collector sample resource
//* xref :../../observability/logging/log_storage/installing-log-storage.adoc#logging-loki-storage_installing-log-storage[Loki object storage]

// Module included in the following assemblies:

// * networking/network_observability/installing-operators.adoc

[id="network-observability-lokistack-create_{context}"]
= Creating a LokiStack custom resource

[role="_abstract"]
Deploy the `LokiStack` custom resource using the web console or {oc-first}, ensuring you configure the correct namespace, deployment size, and secret name for Loki object storage.

You can deploy a `LokiStack` custom resource (CR) to create a namespace or new project.

.Procedure

. Navigate to *Ecosystem* -> *Installed Operators*, viewing *All projects* from the *Project* dropdown.
. Look for *{loki-op}*. In the details, under *Provided APIs*, select *LokiStack*.
. Click *Create LokiStack*.
. Ensure the following fields are specified in either *Form View* or *YAML view*:
+
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: loki
  namespace: netobserv-loki
spec:
  size: 1x.small
  storage:
    schemas:
    - version: v13
      effectiveDate: '2022-06-01'
    secret:
      name: loki-s3
      type: s3
  storageClassName: gp3
  tenants:
    mode: openshift-network
----
+
where:

`metadata.namespace`:: Specifies the namespace for the `LokiStack` resource. While this example uses `netobserv-loki`, you can use a different namespace for different components.
`spec.size`:: Specifies the deployment size. In {loki-op} 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.
+
[IMPORTANT]
====
It is not possible to change the number `1x` for the deployment size.
====
`spec.storageClassName`:: Specifies a storage class name that is available on the cluster for `ReadWriteOnce` access mode. For best performance, specify a storage class that allocates block storage. Use the `oc get storageclasses` command to see available storage classes on your cluster.
+
[IMPORTANT]
====
You must not reuse the same `LokiStack` custom resource that is used for {logging}.
====

. Click *Create*.

// Module included in the following assemblies:

//  * cluster-logging-loki.adoc
//  * network_observability/installing-operators.adoc

[id="logging-creating-new-group-cluster-admin-user-role_{context}"]
= Creating a new group for the cluster-admin user role

Use the following procedure to create a new group for users with `cluster-admin` permissions.

.Procedure

. Enter the following command to create a new group:
+
[source,terminal]
----
$ oc adm groups new cluster-admin
----
. Enter the following command to add the desired user to the `cluster-admin` group:
+
[source,terminal]
----
$ oc adm groups add-users cluster-admin <username>
----
. Enter the following command to add `cluster-admin` user role to the group:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-group cluster-admin cluster-admin
----

// Module included in the following assemblies:
//
// * observability/network_observability/installing-operators.adoc
// * logging/cluster-logging-loki.adoc

[id="logging-loki-log-access_{context}"]
= Fine grained access for Loki logs

In {logging} 5.8 and later, the {clo} does not grant all users access to logs by default. As an administrator, you must configure your users' access unless the Operator was upgraded and prior configurations are in place. Depending on your configuration and need, you can configure fine grain access to logs using the following:

* Cluster wide policies
* Namespace scoped policies
* Creation of custom admin groups

As an administrator, you need to create the role bindings and cluster role bindings appropriate for your deployment. The {clo} provides the following cluster roles:

* `cluster-logging-application-view` grants permission to read application logs.
* `cluster-logging-infrastructure-view` grants permission to read infrastructure logs.
* `cluster-logging-audit-view` grants permission to read audit logs.

If you have upgraded from a prior version, an additional cluster role `logging-application-logs-reader` and associated cluster role binding `logging-all-authenticated-application-logs-reader` provide backward compatibility, allowing any authenticated user read access in their namespaces.

[NOTE]
====
Users with access by namespace must provide a namespace when querying application logs.
====

== Cluster wide access
Cluster role binding resources reference cluster roles, and set permissions cluster wide.

.Example ClusterRoleBinding
[source,yaml]
----
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: logging-all-application-logs-reader
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-logging-application-view # <1>
subjects: # <2>
- kind: Group
  name: system:authenticated
  apiGroup: rbac.authorization.k8s.io
----
<1> Additional `ClusterRoles` are `cluster-logging-infrastructure-view`, and `cluster-logging-audit-view`.
<2> Specifies the users or groups this object applies to.

== Namespaced access

`RoleBinding` resources can be used with `ClusterRole` objects to define the namespace a user or group has access to logs for.

.Example RoleBinding
[source,yaml]
----
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: allow-read-logs
  namespace: log-test-0 # <1>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-logging-application-view
subjects:
- kind: User
  apiGroup: rbac.authorization.k8s.io
  name: testuser-0
----
<1> Specifies the namespace this `RoleBinding` applies to.

// tag::CustomAdmin[]
== Custom admin group access

// tag::LokiMode[]
If you have a large deployment with several users who require broader permissions, you can create a custom group using the `adminGroup` field. Users who are members of any group specified in the `adminGroups` field of the `LokiStack` CR are considered administrators.
// end::LokiMode[]

// tag::NetObservMode[]
If you need to see cluster-wide logs without necessarily being an administrator, or if you already have any group defined that you want to use here, you can specify a custom group using the `adminGroup` field. Users who are members of any group specified in the `adminGroups` field of the `LokiStack` custom resource (CR) have the same read access to logs as administrators.
// end::NetObservMode[]

// tag::LokiMode[]
Administrator users have access to all application logs in all namespaces, if they also get assigned the `cluster-logging-application-view` role.
// end::LokiMode[]

// tag::NetObservMode[]
Administrator users have access to all network logs across the cluster.
// end::NetObservMode[]

.Example LokiStack CR
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
# tag::LokiMode[]
  name: logging-loki
  namespace: openshift-logging
# end::LokiMode[]
# tag::NetObservMode[]
  name: loki
  namespace: netobserv
# end::NetObservMode[]
spec:
  tenants:
# tag::LokiMode[]
    mode: openshift-logging # <1>
# end::LokiMode[]
# tag::NetObservMode[]
    mode: openshift-network # <1>
# end::NetObservMode[]
    openshift:
      adminGroups: # <2>
      - cluster-admin
      - custom-admin-group # <3>
----
<1> Custom admin groups are only available in this mode.
<2> Entering an empty list `[]` value for this field disables admin groups.
<3> Overrides the default groups (`system:cluster-admins`, `cluster-admin`, `dedicated-admin`)
// end::CustomAdmin[]

// Module is included in the following assemblies:
// * observability/logging/log_storage/installing-log-storage.adoc
// * network_observability/installing-operators.adoc

[id="loki-deployment-sizing_{context}"]
= Loki deployment sizing

Sizing for Loki follows the format of `1x.<size>` where the value `1x` is number of instances and `<size>` specifies performance capabilities.

[IMPORTANT]
====
It is not possible to change the number `1x` for the deployment size.
====

.Loki sizing
[cols="1h,4*",options="header"]
|===
|
|1x.demo
|1x.extra-small
|1x.small
|1x.medium

|Data transfer
|Demo use only
|100GB/day
|500GB/day
|2TB/day

|Queries per second (QPS)
|Demo use only
|1-25 QPS at 200ms
|25-50 QPS at 200ms
|25-75 QPS at 200ms

|Replication factor
|None
|2
|2
|2

|Total CPU requests
|None
|14 vCPUs
|34 vCPUs
|54 vCPUs

|Total CPU requests if using the ruler
|None
|16 vCPUs
|42 vCPUs
|70 vCPUs

|Total memory requests
|None
|31Gi
|67Gi
|139Gi

|Total memory requests if using the ruler
|None
|35Gi
|83Gi
|171Gi

|Total disk requests
|40Gi
|430Gi
|430Gi
|590Gi

|Total disk requests if using the ruler
|80Gi
|750Gi
|750Gi
|910Gi
|===

// Module included in the following assemblies:

// * networking/network_observability/installing-operators.adoc
[id="network-observability-lokistack-configuring-ingestion_{context}"]
= LokiStack ingestion limits and health alerts

[role="_abstract"]
The `LokiStack` instance includes default ingestion and query limits that can be overridden by administrators to manage performance and prevent system alerts or errors.

[NOTE]
====
You might want to update the ingestion and query limits if you get Loki errors showing up in the Console plugin, or in `flowlogs-pipeline` logs.
====

Here is an example of configured limits:

[source,yaml]
----
spec:
  limits:
    global:
      ingestion:
        ingestionBurstSize: 40
        ingestionRate: 20
        maxGlobalStreamsPerTenant: 25000
      queries:
        maxChunksPerQuery: 2000000
        maxEntriesLimitPerQuery: 10000
        maxQuerySeries: 3000
----

For more information about these settings, see "LokiStack API reference".

[role="_additional-resources"]
.Additional resources
* LokiStack API reference

// Module included in the following assemblies:

// * networking/network_observability/installing-operators.adoc

[id="network-observability-operator-installation_{context}"]
= Installing the Network Observability Operator

[role="_abstract"]
Install the Network Observability Operator and use the setup wizard to create the `FlowCollector` custom resource definition (CRD) to complete the initial configuration.

You can set specifications in the web console when you create the `FlowCollector`.

[IMPORTANT]
====
The actual memory consumption of the Operator depends on your cluster size and the number of resources deployed. Memory consumption might need to be adjusted accordingly. For more information refer to "Network Observability controller manager pod runs out of memory" in the "Important Flow Collector configuration considerations" section.
====

.Prerequisites

* If you choose to use Loki, install the {loki-op} version 5.7+.
* You must have `cluster-admin` privileges.
* One of the following supported architectures is required: `amd64`, `ppc64le`, `arm64`, or `s390x`.
* Any CPU supported by Red Hat Enterprise Linux (RHEL) 9.
* Must be configured with OVN-Kubernetes as the main network plugin, and optionally using secondary interfaces with Multus and SR-IOV.

[NOTE]
====
Additionally, this installation example uses the `netobserv` namespace, which is used across all components. You can optionally use a different namespace.
====

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.
. Choose  *Network Observability Operator* from the list of available Operators in the software catalog, and click *Install*.
. Select the checkbox `Enable Operator recommended cluster monitoring on this Namespace`.
. Navigate to *Operators* -> *Installed Operators*. Under Provided APIs for Network Observability, select the *Flow Collector* link.
. Follow the *Network Observability FlowCollector setup* wizard.
. Click *Create*.

.Verification

To confirm this was successful, when you navigate to *Observe* you should see *Network Traffic* listed in the options.

In the absence of *Application Traffic* within the OpenShift Container Platform cluster, default filters might show that there are "No results", which results in no visual flow. Beside the filter selections, select *Clear all filters* to see the flow.

// Module included in the following assemblies:
//
// * network_observability/installing-operators.adoc

[id="network-observability-important-flowcollector-configuration-considerations_{context}"]
= Important FlowCollector configuration considerations

[role="_abstract"]
Review essential `FlowCollector` configuration options before initial deployment to avoid pod disruptions caused by later reconfiguration. Key settings include Kafka integration, enriched flow data exports, SR-IOV traffic monitoring, and advanced tracking for DNS and packet drops.

Once you create the `FlowCollector` instance, you can reconfigure it, but the pods are terminated and recreated again, which can be disruptive.

Therefore, you can consider configuring the following options when creating the `FlowCollector` for the first time.

//03/20/2026: Comment for JTBD work. This will likely need to be addressed and redone for JTBD. This file was created only to meet the ConceptLink rule by the deadline.

[role="_additional-resources"]
.Additional resources
* Configuring the Flow Collector resource with Kafka
* Export enriched network flow data to Kafka or IPFIX
* Configuring monitoring for SR-IOV interface traffic
* Working with conversation tracking
* Working with DNS tracking
* Working with packet drops
* Flow Collector API Reference
* Flow Collector sample resource
* Resource considerations
* Troubleshooting network observability controller manager pod runs out of memory
* Network observability architecture

// Module included in the following assemblies:

// * networking/network_observability/installing-operators.adoc

[id="network-observability-updating-migrating_{context}"]
= Migrating removed stored versions of the FlowCollector CRD

[role="_abstract"]
Manually remove the deprecated `v1alpha1` version from the `FlowCollector` custom resource definition (CRD) `storedVersion` list to prevent upgrade errors and successfully migrate to Network Observability Operator 1.6.

There are two options to remove stored versions:

. Use the Storage Version Migrator Operator.
. Uninstall and reinstall the Network Observability Operator, ensuring that the installation is in a clean state.

.Prerequisites
* You have an older version of the Operator installed, and you want to prepare your cluster to install the latest version of the Operator. Or you have attempted to install the Network Observability Operator 1.6 and run into the error: `Failed risk of data loss updating "flowcollectors.flows.netobserv.io": new CRD removes version v1alpha1 that is listed as a stored version on the existing CRD`.

.Procedure
. Verify that the old `FlowCollector` CRD version is still referenced in the `storedVersion`:
+
[source,terminal]
----
$ oc get crd flowcollectors.flows.netobserv.io -ojsonpath='{.status.storedVersions}'
----
. If `v1alpha1` appears in the list of results, proceed with *Step a* to use the Kubernetes Storage Version Migrator or *Step b* to uninstall and reinstall the CRD and the Operator.
.. *Option 1: Kubernetes Storage Version Migrator*: Create a YAML to define the `StorageVersionMigration` object, for example `migrate-flowcollector-v1alpha1.yaml`:
+
[source,yaml]
----
apiVersion: migration.k8s.io/v1alpha1
kind: StorageVersionMigration
metadata:
  name: migrate-flowcollector-v1alpha1
spec:
  resource:
    group: flows.netobserv.io
    resource: flowcollectors
    version: v1alpha1
----
... Save the file.
... Apply the `StorageVersionMigration` by running the following command:
+
[source,terminal]
----
$ oc apply -f migrate-flowcollector-v1alpha1.yaml
----
... Update the `FlowCollector` CRD to manually remove `v1alpha1` from the `storedVersion`:
+
[source,terminal]
----
$ oc edit crd flowcollectors.flows.netobserv.io
----
.. *Option 2: Reinstall*: Save the Network Observability Operator 1.5 version of the `FlowCollector` CR to a file, for example `flowcollector-1.5.yaml`.
+
[source,terminal]
----
$ oc get flowcollector cluster -o yaml > flowcollector-1.5.yaml
----
... Follow the steps in "Uninstalling the Network Observability Operator", which uninstalls the Operator and removes the existing `FlowCollector` CRD.
... Install the Network Observability Operator latest version, 1.6.0.
... Create the `FlowCollector` using backup that was saved in Step b.

.Verification
* Run the following command:
+
[source,terminal]
----
$ oc get crd flowcollectors.flows.netobserv.io -ojsonpath='{.status.storedVersions}'
----
The list of results should no longer show `v1alpha1` and only show the latest version, `v1beta1`.

// Module included in the following assemblies:
//
// network_observability/installing-operators.adoc

[id="network-observability-multi-tenancy_{context}"]
= Enabling multi-tenancy in network observability

[role="_abstract"]
Enable multi-tenancy in network observability by configuring cluster roles and namespace roles to grant project administrators and developers granular, restricted access to flows and metrics in Loki and Prometheus.

Access is enabled for project administrators. Project administrators who have limited access to some namespaces can access flows for only those namespaces.

For Developers, multi-tenancy is available for both Loki and Prometheus but requires different access rights.

.Prerequisite
* If you are using Loki, you have installed at least Loki Operator version 5.7.
* You must be logged in as a project administrator.

.Procedure

*  For per-tenant access, you must have the `netobserv-loki-reader` cluster role and the `netobserv-metrics-reader` namespace role to use the developer perspective. Run the following commands for this level of access:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user netobserv-loki-reader <user_group_or_name>
----
+
[source,terminal]
----
$ oc adm policy add-role-to-user netobserv-metrics-reader <user_group_or_name> -n <namespace>
----

* For cluster-wide access, non-cluster-administrators must have the `netobserv-loki-reader`, `cluster-monitoring-view`, and `netobserv-metrics-reader` cluster roles. In this scenario, you can use either the admin perspective or the developer perspective. Run the following commands for this level of access:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user netobserv-loki-reader <user_group_or_name>
----
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user cluster-monitoring-view <user_group_or_name>
----
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user netobserv-metrics-reader <user_group_or_name>
----

[role="_additional-resources"]
.Additional resources
* Kubernetes Storage Version Migrator Operator

[role="_additional-resources"]
.Additional resources
* Red Hat AMQ Streams
* Configuring the FlowCollector resource with Kafka

// Module included in the following assemblies:
//
// * networking/network_observability/installing-operators.adoc

[id="network-observability-operator-uninstall_{context}"]
= Uninstalling the Network Observability Operator

[role="_abstract"]
Uninstall the Network Observability Operator using the OpenShift Container Platform web console Operator Hub, working in the *Ecosystem* -> *Installed Operators* area.

.Procedure

. Remove the `FlowCollector` custom resource.
.. Click *Flow Collector*, which is next to the *Network Observability Operator* in the *Provided APIs* column.
.. Click the Options menu {kebab} for the *cluster* and select *Delete FlowCollector*.
. Uninstall the Network Observability Operator.
.. Navigate back to the *Ecosystem* -> *Installed Operators* area.
.. Click the Options menu {kebab} next to the  *Network Observability Operator* and select *Uninstall Operator*.
.. *Home* -> *Projects* and select `openshift-netobserv-operator`
.. Navigate to *Actions* and select *Delete Project*
. Remove the `FlowCollector` custom resource definition (CRD).
.. Navigate to *Administration* -> *CustomResourceDefinitions*.
.. Look for *FlowCollector* and click the Options menu {kebab}.
.. Select *Delete CustomResourceDefinition*.
+
[IMPORTANT]
====
The {loki-op} and Kafka remain if they were installed and must be removed separately. Additionally, you might have remaining data stored in an object store, and a persistent volume that must be removed.
====
