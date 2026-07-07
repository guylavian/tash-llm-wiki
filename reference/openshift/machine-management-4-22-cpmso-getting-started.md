---
title: "Getting started with control plane machine sets"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-getting-started
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-getting-started
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Getting started with control plane machine sets

[id="cpmso-getting-started"]
= Getting started with control plane machine sets

[role="_abstract"]
Set up the control plane machine set to enable automated management, recovery, and configuration updates for control plane machines in your cluster.

The process for getting started with control plane machine sets depends on the state of the `ControlPlaneMachineSet` custom resource (CR) in your cluster.

Clusters with an active generated CR:: Clusters that have a generated CR with an active state use the control plane machine set by default. No administrator action is required.

Clusters with an inactive generated CR:: For clusters that include an inactive generated CR, you must review the CR configuration and activate the CR.

Clusters without a generated CR:: For clusters that do not include a generated CR, you must create and activate a CR with the appropriate configuration for your cluster.

If you are uncertain about the state of the `ControlPlaneMachineSet` CR in your cluster, you can verify the CR status.

[id="cpmso-platform-matrix_{context}"]
== Supported cloud providers

In OpenShift Container Platform , the control plane machine set is supported for Amazon Web Services (AWS), {gcp-first}, Microsoft Azure, Nutanix, and VMware vSphere clusters.

The status of the control plane machine set after installation depends on your cloud provider and the version of OpenShift Container Platform that you installed on your cluster.

.Control plane machine set implementation for OpenShift Container Platform 
[cols="<.^5,^.^4,^.^4,^.^4"]
|====
|Cloud provider |Active by default |Generated CR |Manual CR required

|{aws-first}
|X ^[1]^
|X
|

|{gcp-first}
|X ^[2]^
|X
|

|{azure-first}
|X ^[2]^
|X
|

|Nutanix
|X ^[3]^
|X
|

|{rh-openstack-first}
|X ^[3]^
|X
|

|{vmw-full}
|X ^[4]^
|X
|
|====
[.small]
--
1. {aws-short} clusters that are upgraded from version 4.11 or earlier require CR activation.
2. {gcp-short} and {azure-short} clusters that are upgraded from version 4.12 or earlier require CR activation.
3. Nutanix and {rh-openstack} clusters that are upgraded from version 4.13 or earlier require CR activation.
4. {vmw-short} clusters that are upgraded from version 4.15 or earlier require CR activation.
--

//Checking the control plane machine set custom resource state
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-getting-started.adoc
// * machine_management/control_plane_machine_management/cpmso-troubleshooting.adoc
// * machine_management/control_plane_machine_management/cpmso-disabling.adoc

[id="cpmso-checking-status_{context}"]
= Checking the control plane machine set custom resource state

[role="_abstract"]
Check the state of the control plane machine set custom resource to determine if it is active, inactive, or missing before making configuration changes.

.Procedure

* Determine the state of the CR by running the following command:
+
[source,terminal]
----
$ oc get controlplanemachineset.machine.openshift.io cluster \
  --namespace openshift-machine-api
----

** A result of `Active` indicates that the `ControlPlaneMachineSet` CR exists and is activated. No administrator action is required.

** A result of `Inactive` indicates that a `ControlPlaneMachineSet` CR exists but is not activated.

** A result of `NotFound` indicates that there is no existing `ControlPlaneMachineSet` CR.

.Next steps

To use the control plane machine set, you must ensure that a `ControlPlaneMachineSet` CR with the correct settings for your cluster exists.

* If your cluster has an existing CR, you must verify that the configuration in the CR is correct for your cluster.

* If your cluster does not have an existing CR, you must create one with the correct configuration for your cluster.

//Activating the control plane machine set custom resource
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-getting-started.adoc

[id="cpmso-activating_{context}"]
= Activating the control plane machine set custom resource

[role="_abstract"]
To use the control plane machine set, you must ensure that a `ControlPlaneMachineSet` custom resource (CR) with the correct settings for your cluster exists. On a cluster with a generated CR, you must verify that the configuration in the CR is correct for your cluster and activate it.

[NOTE]
====
For more information about the parameters in the CR, see "Control plane machine set configuration".
====

.Procedure

. View the configuration of the CR by running the following command:
+
[source,terminal]
----
$ oc --namespace openshift-machine-api edit controlplanemachineset.machine.openshift.io cluster
----

. Change the values of any fields that are incorrect for your cluster configuration.

. When the configuration is correct, activate the CR by setting the `.spec.state` field to `Active` and saving your changes.
+
[IMPORTANT]
====
To activate the CR, you must change the `.spec.state` field to `Active` in the same `oc edit` session that you use to update the CR configuration. If the CR is saved with the state left as `Inactive`, the control plane machine set generator resets the CR to its original settings.
====

[role="_additional-resources"]
.Additional resources
* Control plane machine set configuration

//Creating a control plane machine set custom resource
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-getting-started.adoc

[id="cpmso-creating-cr_{context}"]
= Creating a control plane machine set custom resource

[role="_abstract"]
To use the control plane machine set, you must ensure that a `ControlPlaneMachineSet` custom resource (CR) with the correct settings for your cluster exists. On a cluster without a generated CR, you must create the CR manually and activate it.

[NOTE]
====
For more information about the structure and parameters of the CR, see "Control plane machine set configuration".
====

.Procedure

. Create a YAML file using the following template:
+
--
[source,yaml]
----
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
  replicas: 3
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <cluster_id>
      machine.openshift.io/cluster-api-machine-role: master
      machine.openshift.io/cluster-api-machine-type: master
  state: Active
  strategy:
    type: RollingUpdate
  template:
    machineType: machines_v1beta1_machine_openshift_io
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        platform: <platform>
        <platform_failure_domains>
      metadata:
        labels:
          machine.openshift.io/cluster-api-cluster: <cluster_id>
          machine.openshift.io/cluster-api-machine-role: master
          machine.openshift.io/cluster-api-machine-type: master
      spec:
        providerSpec:
          value:
            <platform_provider_spec>
----

where:

`<cluster_id>`:: Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You must specify this value when you create a `ControlPlaneMachineSet` CR. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----

`state: Active`:: Specifies the state of the Operator. When the state is `Inactive`, the Operator is not operational. You can activate the Operator by setting the value to `Active`.
+
[IMPORTANT]
====
Before you activate the CR, you must ensure that its configuration is correct for your cluster requirements.
====

`type: RollingUpdate`:: Specifies the update strategy for the cluster. Valid values are `OnDelete` and `RollingUpdate`. The default value is `RollingUpdate`. For more information about update strategies, see "Updating the control plane configuration".

`platform: <platform>`:: Specifies the cloud provider platform name. Valid values are `AWS`, `Azure`, `GCP`, `Nutanix`, `VSphere`, and `OpenStack`.

`<platform_failure_domains>`:: Specifies the failure domains configuration for the cluster. The format and values of this section are provider-specific. For more information, see the sample failure domain configuration for your cloud provider.

`<platform_provider_spec>`:: Specifies the provider spec configuration for the cluster. The format and values of this section are provider-specific. For more information, see the sample provider specification for your cloud provider.
--

. Refer to the sample YAML for a control plane machine set CR and populate your file with values that are appropriate for your cluster configuration.

. Refer to the sample failure domain configuration and sample provider specification for your cloud provider and update those sections of your file with the appropriate values.

. When the configuration is correct, activate the CR by setting the `.spec.state` field to `Active` and saving your changes.

. Create the CR from your YAML file by running the following command:
+
[source,terminal]
----
$ oc create -f <control_plane_machine_set>.yaml
----
+
where `<control_plane_machine_set>` specifies the name of the YAML file that contains the CR configuration.

[role="_additional-resources"]
.Additional resources
* Updating the control plane configuration

* Control plane machine set configuration

* Provider-specific configuration options
