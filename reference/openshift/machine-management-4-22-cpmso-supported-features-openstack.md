---
title: "Configuring {rh-openstack-first} features for control plane machines"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-supported-features-openstack
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-supported-features-openstack
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Configuring {rh-openstack-first} features for control plane machines

[id="cpmso-supported-features-openstack"]
= Configuring {rh-openstack-first} features for control plane machines

[role="_abstract"]
You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".

//Changing the OpenStack Nova flavor by using a control plane machine set
// Module included in the following assemblies:
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-openstack.adoc

[id="cpms-changing-openstack-flavor-type_{context}"]
= Changing the {rh-openstack} compute flavor by using a control plane machine set

You can change the {rh-openstack-first} compute service (Nova) flavor that your control plane machines use by updating the specification in the control plane machine set custom resource.

In {rh-openstack}, flavors define the compute, memory, and storage capacity of computing instances. By increasing or decreasing the flavor size, you can scale your control plane vertically.

.Prerequisites

* Your {rh-openstack} cluster uses a control plane machine set.

.Procedure

. Edit the following line under the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  value:
# ...
    flavor: m1.xlarge <1>
----
<1> Specify a {rh-openstack} flavor type that has the same base as the existing selection. For example, you can change `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`. You can choose larger or smaller flavors depending on your vertical scaling needs.

. Save your changes.

After you save your changes, machines are replaced with ones that use the flavor you chose.

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources
* Updating the control plane configuration
* Control plane configuration options for {rh-openstack-full}
