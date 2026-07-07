---
title: "Selecting a larger AWS instance type for control plane machines"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-increasing-aws-flavor-size
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/increasing-aws-flavor-size
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Selecting a larger AWS instance type for control plane machines

[id="increasing-aws-flavor-size"]
= Selecting a larger AWS instance type for control plane machines

[role="_abstract"]
If the control plane machines in an {aws-first} cluster require more resources, you can select a larger {aws-short} instance type for the control plane machines to use.

[NOTE]
====
The procedure for clusters that use a control plane machine set is different from the procedure for clusters that do not use a control plane machine set.

If you are uncertain about the state of the `ControlPlaneMachineSet` CR in your cluster, you can verify the CR status.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Verify the CR status

//Changing the Amazon Web Services instance type by using a control plane machine set
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

[role="_additional-resources"]
.Additional resources
* Managing control plane machines with control plane machine sets

//Changing the Amazon Web Services instance type by using the AWS console
// Module included in the following assemblies:
//
// * scalability_and_performance/recommended-performance-scale-practices/recommended-control-plane-practices.adoc

[id="aws-console-changing-aws-instance-type_{context}"]
= Changing the Amazon Web Services instance type by using the AWS console

[role="_abstract"]
You can change the {aws-first} instance type that your control plane machines use by updating the instance type in the AWS console.

.Prerequisites

* You have access to the {aws-short} console with the permissions required to modify the EC2 Instance for your cluster.
* You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

.Procedure

. Open the {aws-short} console and fetch the instances for the control plane machines.

. Choose one control plane machine instance.
+
.. For the selected control plane machine, back up the etcd data by creating an etcd snapshot. For more information, see "Backing up etcd".
+
.. In the {aws-short} console, stop the control plane machine instance.
+
.. Select the stopped instance, and click *Actions* -> *Instance Settings* -> *Change instance type*.
+
.. Change the instance to a larger type, ensuring that the type is the same base as the previous selection, and apply changes. For example, you can change `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`.
+
.. Start the instance.
+
.. If your OpenShift Container Platform cluster has a corresponding `Machine` object for the instance, update the instance type of the object to match the instance type set in the {aws-short} console.

. Repeat this process for each control plane machine.

[role="_additional-resources"]
.Additional resources
* Backing up etcd
* AWS documentation about changing the instance type
