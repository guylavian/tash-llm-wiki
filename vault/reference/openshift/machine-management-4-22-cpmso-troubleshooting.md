---
title: "Troubleshooting the control plane machine set"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-troubleshooting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-troubleshooting
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Troubleshooting the control plane machine set

[id="cpmso-troubleshooting"]
= Troubleshooting the control plane machine set

[role="_abstract"]
Use the following information to understand and recover from issues you might encounter.

//Checking the control plane machine set custom resource status
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

[role="_additional-resources"]
.Additional resources
* Activating the control plane machine set custom resource
* Creating a control plane machine set custom resource

//Adding a missing Azure internal load balancer
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-troubleshooting.adoc

[id="cpmso-ts-ilb-missing_{context}"]
= Adding a missing Azure internal load balancer

[role="_abstract"]
Add the required `internalLoadBalancer` parameter to Azure control plane resources to ensure proper load balancing configuration.

For more information about where this parameter is located in the Azure provider specification, see the sample Azure provider specification. The placement in the control plane `Machine` CR is similar.

.Procedure

. List the control plane machines in your cluster by running the following command:
+
[source,terminal]
----
$ oc get machines \
  -l machine.openshift.io/cluster-api-machine-role==master \
  -n openshift-machine-api
----

. For each control plane machine, edit the CR by running the following command:
+
[source,terminal]
----
$ oc edit machine <control_plane_machine_name>
----

. Add the `internalLoadBalancer` parameter with the correct details for your cluster and save your changes.

. Edit your control plane machine set CR by running the following command:
+
[source,terminal]
----
$ oc edit controlplanemachineset.machine.openshift.io cluster \
  -n openshift-machine-api
----

. Add the `internalLoadBalancer` parameter with the correct details for your cluster and save your changes.

.Next steps

* For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

* For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

[role="_additional-resources"]
.Additional resources
* Sample {azure-full} provider specification

//Recovering a degraded etcd Operator after a machine health check operation
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-troubleshooting.adoc

[id="cpmso-ts-etcd-degraded_{context}"]
= Recovering a degraded etcd Operator

[role="_abstract"]
Recover a degraded etcd Operator by removing failed members to restore cluster state after machine health check operations.

For example, while performing remediation, the machine health check might delete a control plane machine that is hosting etcd. If the etcd member is not reachable at that time, the etcd Operator becomes degraded.

When the etcd Operator is degraded, manual intervention is required to force the Operator to remove the failed member and restore the cluster state.

.Procedure

. List the control plane machines in your cluster by running the following command:
+
[source,terminal]
----
$ oc get machines \
  -l machine.openshift.io/cluster-api-machine-role==master \
  -n openshift-machine-api \
  -o wide
----
+
Any of the following conditions might indicate a failed control plane machine:
+
--
** The `STATE` value is `stopped`.
** The `PHASE` value is `Failed`.
** The `PHASE` value is `Deleting` for more than ten minutes.
--
+
[IMPORTANT]
====
Before continuing, ensure that your cluster has two healthy control plane machines. Performing the actions in this procedure on more than one control plane machine risks losing etcd quorum and can cause data loss.

If you have lost the majority of your control plane hosts, leading to etcd quorum loss, then you must follow the disaster recovery procedure "Restoring to a previous cluster state" instead of this procedure.
====

. Edit the machine CR for the failed control plane machine by running the following command:
+
[source,terminal]
----
$ oc edit machine <control_plane_machine_name>
----

. Remove the contents of the `lifecycleHooks` parameter from the failed control plane machine and save your changes.
+
The etcd Operator removes the failed machine from the cluster and can then safely add new etcd members.

[role="_additional-resources"]
.Additional resources
* Restoring to a previous cluster state

//Upgrading clusters that run on Red Hat OpenStack Platform
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-troubleshooting.adoc

[id="cpmso-ts-openstack-upgrade_{context}"]
= Upgrading clusters that run on {rh-openstack}

[role="_abstract"]
Review post-upgrade requirements for clusters running on {rh-openstack-first} to ensure control plane machine sets function correctly.

For clusters that run on {rh-openstack} that were created with OpenShift Container Platform 4.13 or earlier, you might have to perform post-upgrade tasks before you can use control plane machine sets.

// Post-upgrade config for ShiftStack with machine AZs explicitly defined and rootVolumes w/out AZs
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-troubleshooting.adoc

[id="cpmso-openstack-ts-root-volume-azs_{context}"]
= Configuring {rh-openstack} clusters that have machines with root volume availability zones after an upgrade

[role="_abstract"]
For some clusters that run on {rh-openstack-first} that you upgrade, you must manually update machine resources before you can use control plane machine sets if the following configurations are true:

* The upgraded cluster was created with OpenShift Container Platform 4.13 or earlier.

* The cluster infrastructure is installer-provisioned.

* Machines were distributed across multiple availability zones.

* Machines were configured to use root volumes for which block storage availability zones were not defined.

To understand why this procedure is necessary, see Solution #7024383.

.Procedure

. For all control plane machines, edit the provider spec for all control plane machines that match the environment. For example, to edit the machine `master-0`, enter the following command:
+
[source,terminal]
----
$ oc edit machine/<cluster_id>-master-0 -n openshift-machine-api
----
+
where:
+
`<cluster_id>`:: Specifies the ID of the upgraded cluster.

. In the provider spec, set the value of the property `rootVolume.availabilityZone` to the volume of the availability zone you want to use.
+
.An example {rh-openstack} provider spec
[source,yaml]
----
providerSpec:
  value:
    apiVersion: machine.openshift.io/v1alpha1
    availabilityZone: az0
      cloudName: openstack
    cloudsSecret:
      name: openstack-cloud-credentials
      namespace: openshift-machine-api
    flavor: m1.xlarge
    image: rhcos-4.14
    kind: OpenstackProviderSpec
    metadata:
      creationTimestamp: null
    networks:
    - filter: {}
      subnets:
      - filter:
          name: refarch-lv7q9-nodes
          tags: openshiftClusterID=refarch-lv7q9
    rootVolume:
        availabilityZone: nova
        diskSize: 30
        sourceUUID: rhcos-4.12
        volumeType: fast-0
    securityGroups:
    - filter: {}
      name: refarch-lv7q9-master
    serverGroupName: refarch-lv7q9-master
    serverMetadata:
      Name: refarch-lv7q9-master
      openshiftClusterID: refarch-lv7q9
    tags:
    - openshiftClusterID=refarch-lv7q9
    trunk: true
    userDataSecret:
      name: master-user-data
----
+
where:
+
`availabilityZone: nova`:: Specifies the zone name for the root volume.
+
[NOTE]
====
If you edited or recreated machine resources after your initial cluster deployment, you might have to adapt these steps for your configuration.

In your {rh-openstack} cluster, find the availability zone of the root volumes for your machines and use that as the value.
====

. Run the following command to retrieve information about the control plane machine set resource:
+
[source,terminal]
----
$ oc describe controlplanemachineset.machine.openshift.io/cluster --namespace openshift-machine-api
----

. Run the following command to edit the resource:
+
[source,terminal]
----
$ oc edit controlplanemachineset.machine.openshift.io/cluster --namespace openshift-machine-api
----

. For that resource, set the value of the `spec.state` property to `Active` to activate control plane machine sets for your cluster.
+
The control plane is now ready to be managed by the Cluster Control Plane Machine Set Operator.

// Post-upgrade config for ShiftStack with control plane AZs explicitly defined
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-troubleshooting.adoc

[id="cpmso-openstack-with-az-config_{context}"]
= Configuring {rh-openstack} clusters that have control plane machines with availability zones after an upgrade

[role="_abstract"]
For some clusters that run on {rh-openstack-first} that you upgrade, you must manually update machine resources before you can use control plane machine sets if the following configurations are true:

* The upgraded cluster was created with OpenShift Container Platform 4.13 or earlier.

* The cluster infrastructure is installer-provisioned.

* Control plane machines were distributed across multiple compute availability zones.

To understand why this procedure is necessary, see Solution #7013893.

.Procedure

. For the `master-1` and `master-2` control plane machines, open the provider specs for editing. For example, to edit the first machine, enter the following command:
+
[source,terminal]
----
$ oc edit machine/<cluster_id>-master-1 -n openshift-machine-api
----
+
where:
+
`<cluster_id>`:: Specifies the ID of the upgraded cluster.

. For the `master-1` and `master-2` control plane machines, edit the value of the `serverGroupName` property in their provider specs to match that of the machine `master-0`.
+
.An example {rh-openstack} provider spec
[source,yaml,subs="attributes+"]
----
providerSpec:
  value:
    apiVersion: machine.openshift.io/v1alpha1
    availabilityZone: az0
      cloudName: openstack
    cloudsSecret:
      name: openstack-cloud-credentials
      namespace: openshift-machine-api
    flavor: m1.xlarge
    image: rhcos-
    kind: OpenstackProviderSpec
    metadata:
      creationTimestamp: null
    networks:
    - filter: {}
      subnets:
      - filter:
          name: refarch-lv7q9-nodes
          tags: openshiftClusterID=refarch-lv7q9
    securityGroups:
    - filter: {}
      name: refarch-lv7q9-master
    serverGroupName: refarch-lv7q9-master-az0
    serverMetadata:
      Name: refarch-lv7q9-master
      openshiftClusterID: refarch-lv7q9
    tags:
    - openshiftClusterID=refarch-lv7q9
    trunk: true
    userDataSecret:
      name: master-user-data
----
+
where:
+
`serverGroupName`:: Specifies the server group name. This value must match for machines `master-0`, `master-1`, and `master-2`.
+
[NOTE]
====
If you edited or recreated machine resources after your initial cluster deployment, you might have to adapt these steps for your configuration.

In your {rh-openstack} cluster, find the server group that your control plane instances are in and use that as the value.
====

. Run the following command to retrieve information about the control plane machine set resource:
+
[source,terminal]
----
$ oc describe controlplanemachineset.machine.openshift.io/cluster --namespace openshift-machine-api
----

. Run the following command to edit the resource:
+
[source,terminal]
----
$ oc edit controlplanemachineset.machine.openshift.io/cluster --namespace openshift-machine-api
----

. For that resource, set the value of the `spec.state` property to `Active` to activate control plane machine sets for your cluster.
+
The control plane is now ready to be managed by the Cluster Control Plane Machine Set Operator.

//Improving reliability for multiple subnet configurations on Nutanix
// Module included in the following assemblies:
//
// * installing/installing_nutanix/nutanix-failure-domains.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-nutanix.adoc
// * machine_management/control_plane_machine_management/cpmso-troubleshooting.adoc
// * machine_management/creating_machinesets/creating-machineset-nutanix.adoc

[id="cpmso-ts-nutanix-multiple-subnet_{context}"]
= Improving reliability for multiple subnet configurations on Nutanix

[role="_abstract"]
To improve reliability and avoid common networking problems with multiple subnet configurations on Nutanix, adhere to the configuration practices that minimize networking conflicts.

The following networking configuration and management practices can help your multiple subnet configuration perform more reliably:

* To avoid overlapping IP address assignments, use predefined static IP addresses in the `cloud-init` metadata.

* Tag all VMs, disks, and networks with a unique cluster ID.

* Avoid IP address conflicts by using dedicated subnets for each OpenShift Container Platform cluster:
+
Nutanix uses Nutanix Acropolis Hypervisor (AHV) and Nutanix Prism networking to assign IP addresses to virtual machines (VMs).
If a single subnet provides IP addresses for more than one OpenShift Container Platform cluster, AHV or Prism might assign the same IP address to a VM or pod in more than one cluster.
+
To avoid this issue, use dedicated subnets for each OpenShift Container Platform cluster, even when you have more than one cluster on a single Prism Central instance.
You can use the Prism UI or automation tools, such as Terraform or Ansible, to create separate IP address pools for each OpenShift Container Platform cluster.

* Ensure that each OpenShift Container Platform cluster uses distinct DNS zones and virtual IP address ranges.

* Avoid DHCP conflicts by maintaining DHCP allocations:
+
If you use Nutanix to manage DHCP allocation, objects in your cluster might have duplicate leases.
Duplicate leases can cause DHCP conflicts when you apply changes to the control plane machine set custom resource (CR) specification.
+
To avoid this issue, regularly remove stale DHCP leases.

* Use automation tools, such as Terraform or Ansible, to isolate the infrastructure for each OpenShift Container Platform cluster.
