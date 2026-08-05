---
title: "Disabling the Cluster API"
type: reference
domain: openshift
slug: machine-management-4-22-cluster-api-disabling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cluster-api-disabling
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Disabling the Cluster API

[id="cluster-api-disabling"]
= Disabling the Cluster API

To stop using the Cluster API to automate the management of infrastructure resources on your OpenShift Container Platform cluster, convert any Cluster API resources on your cluster to equivalent Machine API resources.

//Migrating Cluster API resources to Machine API resources
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster-api-disabling.adoc

[id="capi-to-mapi-migration-overview_{context}"]
= Migrating Cluster API resources to Machine API resources

On clusters that support migrating between Machine API and Cluster API resources, the two-way synchronization controller supports converting a Cluster API resource to a Machine API resource.

[NOTE]
====
The two-way synchronization controller only operates on clusters with the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set enabled.
====

You can migrate resources that you originally migrated from the Machine API to the Cluster API, or resources that you created as Cluster API resources initially.
Migrating an original Machine API resource to a Cluster API resource and then migrating it back provides an opportunity to verify that the migration process works as expected.

[NOTE]
====
You can only migrate some resources on supported infrastructure types.
====

.Supported resource conversions
[cols="6",options="header"]
|===
|Infrastructure
|Compute machine
|Compute machine set
|Machine health check
|Control plane machine set
|Cluster autoscaler

|{aws-short}
|Technology Preview
|Technology Preview
|Not Available
|Not Available
|Not Available

|All other infrastructure types
|Not Available
|Not Available
|Not Available
|Not Available
|Not Available
|===

//Migrating a Cluster API resource to use the Machine API
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster-api-disabling.adoc
// * machine_management/cluster_api_machine_management/cluster-api-getting-started.adoc

[id="migrating-between-capi-mapi_{context}"]
= Migrating a {from-api-name} resource to use the {to-api-name}

You can migrate individual {from-api-name} objects to equivalent {to-api-name} objects.

.Prerequisites

* You have deployed an OpenShift Container Platform cluster on a supported infrastructure type.

* You have enabled the use of the Cluster API.

* You have enabled the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set.

* You have access to the cluster using an account with `cluster-admin` permissions.

* You have installed the {oc-first}.

.Procedure

. Identify the {from-api-name} resource that you want to migrate to a {to-api-name} resource by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get <resource_kind> -n {from-namespace}
----
+
--
where `<resource_kind>` is one of the following values:

`machine.{from-api-group}`:: The fully qualified name of the resource kind for a compute or control plane machine.

`machineset.{from-api-group}`:: The fully qualified name of the resource kind for a compute machine set.
--

. Edit the resource specification by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit <resource_kind>/<resource_name> -n openshift-machine-api
----
+
--
where:

`<resource_kind>`:: Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.
`<resource_name>`:: Specifies the name of the Machine API resource that you want to migrate to a Cluster API resource.
`<resource_name>`:: Specifies the name of the Machine API resource that corresponds to the Cluster API resource that you want to migrate to the Machine API.
--

. In the resource specification, update the value of the `spec.authoritativeAPI` field:
+
[source,yaml,subs="attributes+"]
----
apiVersion: machine.openshift.io/v1beta1
kind: <resource_kind>
metadata:
  name: <resource_name>
  [...]
spec:
  authoritativeAPI: {to-api-value}
  [...]
status:
  authoritativeAPI: {from-api-value}
  [...]
----
+
--
where:

`kind`::
Specifies the resource kind of the resource that you want to migrate.
For example, the resource kind for a compute machine set is `MachineSet` and the resource kind for a compute machine is `Machine`.
`metadata.name`::
Specifies the name of the resource that you want to migrate.
`spec.authoritativeAPI`::
Specifies the authoritative API that you want this resource to use.
For example, to start migrating a {from-api-name} resource to the {to-api-name}, specify `{to-api-value}`.
`status.authoritativeAPI`::
Specifies the value for the current authoritative API.
This value indicates which API currently manages this resource.
Do not change the value in this part of the specification.
--
+
[IMPORTANT]
====
Do not change other values when you update the value of the `spec.authoritativeAPI` field.
Because other controllers might process updates to other values before the synchronization controller processes the `spec.authoritativeAPI` field update, changing other values can cause unexpected behavior.

For more information, see "Unexpected behavior when changing resource configurations".
====

.Verification

* Check the status of the conversion by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc -n openshift-machine-api get <resource_kind>/<resource_name> -o json | jq .status.authoritativeAPI
----
+
--
where:

`<resource_kind>`:: Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.
`<resource_name>`:: Specifies the name of the Machine API resource that you want to migrate to a Cluster API resource.
`<resource_name>`:: Specifies the name of the Machine API resource that corresponds to the Cluster API resource that you want to migrate to the Machine API.
--
+
--
* While the conversion progresses, this command returns a value of `Migrating`.
If this value persists for a long time, check the logs for the `cluster-capi-operator` deployment in the `openshift-cluster-api` namespace for more information and to identify potential issues.
* When the conversion is complete, this command returns a value of `{to-api-value}`.
--
+
[IMPORTANT]
====
Do not delete any nonauthoritative resource that does not use the current authoritative API unless you want to delete the corresponding resource that does use the current authoritative API.

When you delete a nonauthoritative resource that does not use the current authoritative API, the synchronization controller deletes the corresponding resource that does use the current authoritative API.
For more information, see "Unexpected resource deletion behavior" in the _Troubleshooting resource migration_ content.
====

[role="_additional-resources"]
.Additional resources
* Unexpected behavior when changing resource configurations

//Authoritative API types of compute machines
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster-api-disabling.adoc
// * machine_management/cluster_api_machine_management/cluster-api-getting-started.adoc
// * machine_management/cluster_api_machine_management/cluster-api-troubleshooting.adoc

[id="machine-set-authoritative-api-machines_{context}"]
= Authoritative API types of compute machines

The authoritative API of a compute machine depends on the values of the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` fields in the Machine API compute machine set that creates it.

.Interaction of `authoritativeAPI` fields when creating compute machines
[cols="h,1,1,1,1"]
|===
|`.spec.authoritativeAPI` value
|`ClusterAPI`
|`ClusterAPI`
|`MachineAPI`
|`MachineAPI`

|`.spec.template.spec.authoritativeAPI` value
|`ClusterAPI`
|`MachineAPI`
|`MachineAPI`
|`ClusterAPI`

|`authoritativeAPI` value for new compute machines
|`ClusterAPI`
|`ClusterAPI`
|`MachineAPI`
|`ClusterAPI`
|===

[NOTE]
====
When the `.spec.authoritativeAPI` value is `ClusterAPI`, the Machine API machine set is not authoritative and the `.spec.template.spec.authoritativeAPI` value is not used.
As a result, the only combination that creates a compute machine with the Machine API as authoritative is where the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` values are `MachineAPI`.
====

[role="_additional-resources"]
.Additional resources
* Troubleshooting resource migration
* Migrating Machine API resources to Cluster API resources
