---
title: "Disabling the control plane machine set"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-disabling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-disabling
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Disabling the control plane machine set

[id="cpmso-disabling"]
= Disabling the control plane machine set

[role="_abstract"]
Disable the control plane machine set if you need to manually manage control plane machines or troubleshoot Operator behavior.

The `.spec.state` field in an activated `ControlPlaneMachineSet` custom resource (CR) cannot be changed from `Active` to `Inactive`. To disable the control plane machine set, you must delete the CR so that it is removed from the cluster.

When you delete the CR, the Control Plane Machine Set Operator performs cleanup operations and disables the control plane machine set. The Operator then removes the CR from the cluster and creates an inactive control plane machine set with default settings.

//Deleting the control plane machine set
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-disabling.adoc

[id="cpmso-deleting_{context}"]
= Deleting the control plane machine set

[role="_abstract"]
To stop managing control plane machines with the control plane machine set on your cluster, you must delete the `ControlPlaneMachineSet` custom resource (CR).

.Procedure

* Delete the control plane machine set CR by running the following command:
+
[source,terminal]
----
$ oc delete controlplanemachineset.machine.openshift.io cluster \
  -n openshift-machine-api
----

.Verification

* Check the control plane machine set custom resource state. A result of `Inactive` indicates that the removal and replacement process is successful. A `ControlPlaneMachineSet` CR exists but is not activated.

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

//Re-enabling the control plane machine set
// Module included in the following assemblies:
//
// * machine_management/control_plane_machine_management/cpmso-disabling.adoc

[id="cpmso-reenabling_{context}"]
= Re-enabling the control plane machine set

[role="_abstract"]
Restore automated control plane management after previously disabling the control plane machine set.

To re-enable the control plane machine set, you must ensure that the configuration in the CR is correct for your cluster and activate it.

For more information, see "Activating the control plane machine set custom resource".

[role="_additional-resources"]
.Additional resources
* Activating the control plane machine set custom resource
