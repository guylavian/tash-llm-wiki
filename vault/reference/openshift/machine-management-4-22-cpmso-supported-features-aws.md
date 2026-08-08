---
title: "Configuring {aws-full} features for control plane machines"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-supported-features-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-supported-features-aws
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Configuring {aws-full} features for control plane machines

[id="cpmso-supported-features-aws"]
= Configuring {aws-full} features for control plane machines

[role="_abstract"]
You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".

//Restricting the API server to private for an {aws-full} cluster
// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-supported-features-aws.adoc

[id="private-clusters-setting-api-private-aws_{context}"]
= Restricting the API server to private for an {aws-full} cluster

[role="_abstract"]
If the security posture of your organization does not allow clusters to use an open API endpoint, you can restrict the API server to use only internal load balancers.
To implement this API server restriction, use the {aws-first} console and {oc-first} to delete the external load balancer components.

[IMPORTANT]
====
The {oc-first} steps that remove the external load balancers require the Machine API.
For clusters that cannot use the Machine API, you must manually remove the external load balancers.

Clusters with the infrastructure platform type `none` cannot use the Machine API.
To view the platform type for your cluster, run the following command:

[source,terminal]
----
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
----
====

.Prerequisites

* You have installed an OpenShift Container Platform cluster on {aws-short}.
* You have access to the {aws-short} console as a user with administrator privileges.
* You have access to the {oc-first} as a user with administrator privileges.

.Procedure

. Log in to the {aws-short} console as a user with administrator privileges.

. Delete the external load balancer.
+
[NOTE]
====
The API DNS entry in the private zone already points to the internal load balancer, which uses an identical configuration, so you do not need to modify the internal load balancer.
====

. Delete the `api.<cluster_name>.<domain_name>` DNS entry in the public zone.
+
where `<cluster_name>` is the name of the cluster and `<domain_name>` is the base domain for the cluster.

. To remove the external load balancers, log in to the {oc-first} as a user with administrator privileges.

** If your cluster uses a control plane machine set, remove the external load balancers by editing the `ControlPlaneMachineSet` custom resource (CR).
+
--
. Edit the `ControlPlaneMachineSet` CR by running the following command:
+
[source,terminal]
----
$ oc edit controlplanemachineset.machine.openshift.io cluster \
  -n openshift-machine-api
----

. Remove the external load balancers by deleting the corresponding lines in the control plane machine set custom resource (CR).
+
In the `spec.template.spec.providerSpec.value.loadBalancers` section of the CR, the `name` value for the external load balancer ends in `-ext`.
Delete the line with the external load balancer `name` value and the line with the external load balancer `type` value that accompanies it.
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            loadBalancers:
            - name: <cluster_id>-ext
              type: network
            - name: <cluster_id>-int
              type: network
# ...
----

. Save your changes and exit the object specification.
+
When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".
--

** If your cluster does not use a control plane machine set, you must delete the external load balancers from each control plane machine.

... List the cluster machines by running the following command:
+
[source,terminal]
----
$ oc get machine -n openshift-machine-api
----
+
.Example output
[source,text]
----
NAME                                        STATE     TYPE        REGION      ZONE         AGE
<cluster_id>-master-0                       running   m4.xlarge   us-east-1   us-east-1a   17m
<cluster_id>-master-1                       running   m4.xlarge   us-east-1   us-east-1b   17m
<cluster_id>-master-2                       running   m4.xlarge   us-east-1   us-east-1a   17m
<cluster_id>-worker-us-east-1a-<zone_tag>   running   m4.xlarge   us-east-1   us-east-1a   15m
<cluster_id>-worker-us-east-1a-<zone_tag>   running   m4.xlarge   us-east-1   us-east-1a   15m
<cluster_id>-worker-us-east-1b-<zone_tag>   running   m4.xlarge   us-east-1   us-east-1b   15m
----
+
The control plane machines contain the `master` string in their names.

... Remove the external load balancer from each control plane machine:

.... Edit a control plane machine object to by running the following command:
+
[source,terminal]
----
$ oc edit machines -n openshift-machine-api <control_plane_machine_name>
----
+
where `<control_plane_machine_name>` is the name of the control plane machine object to modify.

.... Remove the lines that describe the external load balancer.
+
In the `spec.providerSpec.value.loadBalancers` section of the CR, the `name` value for the external load balancer ends in `-ext`.
Delete the line with the external load balancer `name` value and the the line with the external load balancer `type` value that accompanies it.
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  name: <control_plane_machine_name>
  namespace: openshift-machine-api
spec:
  providerSpec:
    value:
      loadBalancers:
      - name: <cluster_id>-ext
        type: network
      - name: <cluster_id>-int
        type: network
# ...
----

.... Save your changes and exit the object specification.

.... Repeat this process for each control plane machine.

[role="_additional-resources"]
.Additional resources
* Configuring the Ingress Controller endpoint publishing scope to Internal

//Selecting a larger Amazon Web Services instance type for control plane machines
// Module included in the following assemblies:
//
// * scalability_and_performance/recommended-performance-scale-practices/recommended-control-plane-practices.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="cpms-changing-aws-instance-type_{context}"]
= Changing the Amazon Web Services instance type by using a control plane machine set

[role="_abstract"]
You can change the {aws-first} instance type that your control plane machines use by updating the specification in the control plane machine set custom resource (CR).

** For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

** For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

.Prerequisites

* Your {aws-short} cluster uses a control plane machine set.

.Procedure

. Edit your control plane machine set CR by running the following command:
+
[source,terminal]
----
$ oc --namespace openshift-machine-api edit controlplanemachineset.machine.openshift.io cluster
----

. Edit the following line under the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  value:
    ...
    instanceType: <compatible_aws_instance_type>
----
** `<compatible_aws_instance_type>`: Specifies a larger {aws-short} instance type with the same base as the previous selection. For example, you can change `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`.

. Save your changes.

//Assigning machines to placement groups by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating-machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-aws-existing-placement-group_{context}"]
= Assigning machines to placement groups for Elastic Fabric Adapter instances by using machine sets

[role="_abstract"]
You can configure a machine set to deploy machines on Elastic Fabric Adapter (EFA) instances within an existing {aws-first} placement group. Using EFA instances to run control plane machines can improve network performance.

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html[EFA] instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. This example uses both to demonstrate a configuration that can improve network performance for machines within the specified placement group.

.Prerequisites

* You created a placement group in the {aws-short} console.
+
[NOTE]
====
Ensure that the rules and limitations for the type of placement group that you create are compatible with your intended use case.
The control plane machine set spreads the control plane machines across multiple failure domains when possible. To use placement groups for the control plane, you must use a placement group type that can span multiple Availability Zones.
====

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following lines under the `providerSpec` field:

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    spec:
      providerSpec:
        value:
          instanceType: <supported_instance_type>
          networkInterfaceType: EFA
          placement:
            availabilityZone: <zone>
            region: <region>
          placementGroupName: <placement_group>
          placementGroupPartition: <placement_group_partition_number>
# ...
----

where:

--
`spec.template.spec.providerSpec.value.instanceType`:: Specifies an instance type that supports EFAs.
`spec.template.spec.providerSpec.value.networkInterfaceType`:: Specifies the `EFA` network interface type.
`spec.template.spec.providerSpec.value.placement.availabilityZone`:: Specifies the zone, for example, `us-east-1a`.
`spec.template.spec.providerSpec.value.placement.region`:: Specifies the region, for example, `us-east-1`.
`spec.template.spec.providerSpec.value.placementGroupName`:: Specifies the name of the existing {aws-short} placement group to deploy machines in.
`spec.template.spec.providerSpec.value.placementGroupPartition`:: Optional: Specifies the partition number of the existing AWS placement group to deploy machines in.
--

.Verification

* In the {aws-short} console, find a machine that the machine set created and verify the following in the machine properties:

** The placement group field has the value that you specified for the `placementGroupName` parameter in the machine set.

** The partition number field has the value that you specified for the `placementGroupPartition` parameter in the machine set.

** The interface type field indicates that it uses an EFA.

//Machine sets that enable the Amazon EC2 Instance Metadata Service
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-imds-options_{context}"]
= Machine set options for the Amazon EC2 Instance Metadata Service

[role="_abstract"]
You can use machine sets to create machines that use a specific version of the Amazon EC2 Instance Metadata Service (IMDS). Configuring Amazon EC2 IMDS behavior for control plane machines improves security.

Machine sets can create machines that allow the use of both IMDSv1 and IMDSv2 or machines that require the use of IMDSv2.

[NOTE]
====
To use IMDSv2 on {aws-first} clusters that were created with OpenShift Container Platform version 4.6 or earlier, you must update your boot image. For more information, see "Boot image management".
====

To deploy new compute machines with your preferred IMDS configuration, create a compute machine set YAML file with the appropriate values. You can also edit an existing machine set to create new machines with your preferred IMDS configuration when the machine set is scaled up.

[IMPORTANT]
====
Before configuring a machine set to create machines that require IMDSv2, ensure that any workloads that interact with the {aws-short} metadata service support IMDSv2.
====

[role="_additional-resources"]
.Additional resources
* Boot image management

//Creating machines that use the Amazon EC2 Instance Metadata Service
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-creating-imds-options_{context}"]
= Configuring IMDS by using machine sets

[role="_abstract"]
You can specify whether to require the use of IMDSv2 by adding or editing the value of `metadataServiceOptions.authentication` in the machine set YAML file for your machines.

.Prerequisites
* To use IMDSv2, your {aws-first} cluster must have been created with OpenShift Container Platform version 4.7 or later.

.Procedure
* Add or edit the following lines under the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  value:
    metadataServiceOptions:
      authentication: Required
----

where:

`providerSpec.value.metadataServiceOptions.authentication`:: Specifies whether to require IMDSv2. Set this parameter to `Required` to require IMDSv2. Set this parameter to `Optional` to allow the use of both IMDSv1 and IMDSv2. If you do not specify a value, both IMDSv1 and IMDSv2 are allowed.

//Configuring storage throughput for gp3 drives
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-creating-gp3-throughput_{context}"]
= Configuring storage throughput for gp3 drives

[role="_abstract"]
You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an {aws-short} cluster.
You can configure the storage throughput by editing your compute or control plane machine set.

.Prerequisites

* You use gp3 storage volume(s).

.Procedure
* Add or edit the following lines under the `providerSpec` field in your compute or control plane machine set:
+
[source,yaml]
----
providerSpec:
  value:
    blockDevices:
      - ebs:
          throughputMib: <throughput_value>
----
where:

`<throughput_value>`::
Specifies a value in MiB per second between 125 and 2,000.
You can only edit this value on gp3 volumes.
The default value is `125`.

//Machine sets that deploy machines as Dedicated Instances
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-dedicated-instance_{context}"]
= Machine sets that deploy machines as Dedicated Instances

[role="_abstract"]
You can create a machine set running on {aws-first} that deploys machines as Dedicated Instances. Dedicated Instances run in a virtual private cloud (VPC) on hardware that is dedicated to a single customer.

These Amazon EC2 instances are physically isolated at the host hardware level. The isolation of Dedicated Instances occurs even if the instances belong to different {aws-short} accounts that are linked to a single payer account. However, other instances that are not dedicated can share hardware with Dedicated Instances if they belong to the same {aws-short} account.

Instances with either public or dedicated tenancy are supported by the Machine API. Instances with public tenancy run on shared hardware. Public tenancy is the default tenancy. Instances with dedicated tenancy run on single-tenant hardware.

//Creating Dedicated Instances by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-creating-dedicated-instance_{context}"]
= Creating Dedicated Instances by using machine sets

[role="_abstract"]
You can run a machine that is backed by a Dedicated Instance by using Machine API integration. Set the `tenancy` field in your machine set YAML file to launch a Dedicated Instance on {aws-first}.

.Procedure

* Specify a dedicated tenancy under the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  placement:
    tenancy: dedicated
----

//Configuring Capacity Reservation by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-supported-features-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-supported-features-aws.adoc

[id="machineset-capacity-reservation_{context}"]

OpenShift Container Platform version  and later supports

[role="_abstract"]
You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define.

These parameters specify the
region, and number of instances that you want to reserve.
If your
can accommodate the capacity request, the deployment succeeds.

For more information, including limitations and suggested use cases for this

[NOTE]
====
You cannot change an existing Capacity Reservation configuration for a machine set.
To use a different Capacity Reservation group, you must replace the machine set and the machines that the previous machine set deployed.
====

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You installed the {oc-first}.
* You created a Capacity Reservation group.
For more information, see Create a Capacity Reservation in the {azure-full} documentation.
* You purchased an On-Demand Capacity Reservation or Capacity Block for ML.
For more information, see On-Demand Capacity Reservations and Capacity Blocks for ML in the {aws-short} documentation.

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following section under the `providerSpec` field:
+
.Sample configuration
[source,yaml]
----
tag::compute[]
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
end::compute[]
tag::controlplane[]
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
end::controlplane[]
# ...
spec:
  template:
tag::compute[]
    spec:
      providerSpec:
        value:
          capacityReservationGroupID: <capacity_reservation_group>
          capacityReservationId: <capacity_reservation>
          marketType: <market_type>
end::compute[]
tag::controlplane[]
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            capacityReservationGroupID: <capacity_reservation_group>
            capacityReservationId: <capacity_reservation>
            marketType: <market_type>
end::controlplane[]
# ...
----
+
where:
+
tag::compute[]
`<capacity_reservation_group>`::
`<capacity_reservation>`::
end::compute[]
tag::controlplane[]
`<capacity_reservation_group>`::
`<capacity_reservation>`::
end::controlplane[]
Specifies the ID of the
that you want the machine set to deploy machines on.

`<market_type>`::
Specifies the market type to use.
The following values are valid:
+
--
`CapacityBlock`:: Use this market type with Capacity Blocks for ML.
`OnDemand`:: Use this market type with On-Demand Capacity Reservations.
tag::compute[]
`Spot`:: Use this market type with Spot Instances.
This option is not compatible with Capacity Reservations.
end::compute[]
--

.Verification

* To verify machine deployment, list the machines that the machine set created by running the following command:
+
[source,terminal]
----
tag::compute[]
$ oc get machines.machine.openshift.io \
  -n openshift-machine-api \
  -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
end::compute[]
tag::controlplane[]
$ oc get machine \
  -n openshift-machine-api \
  -l machine.openshift.io/cluster-api-machine-role=master
end::controlplane[]
----
tag::compute[]
+
where `<machine_set_name>` is the name of the compute machine set.
end::compute[]
+
In the output, verify that the characteristics of the listed machines match the parameters of your

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources
* Updating the control plane configuration
* Control plane configuration options for {aws-full}
