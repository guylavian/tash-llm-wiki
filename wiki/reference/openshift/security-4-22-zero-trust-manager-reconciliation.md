---
title: "Enabling create-only mode for the Zero Trust Workload Identity Manager"
type: reference
domain: openshift
slug: security-4-22-zero-trust-manager-reconciliation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/zero-trust-manager-reconciliation
version: 4.22
family: security
documentKind: "Documentation"
---

# Enabling create-only mode for the Zero Trust Workload Identity Manager

[id="zero-trust-manager-reconciliation_{context}"]
= Enabling create-only mode for the Zero Trust Workload Identity Manager

[role="_abstract"]
To pause Operator reconciliation, enable `create-only` mode by setting an environment variable in the subscription object. By setting this value, you can perform manual configurations or debug the operator without the controller overwriting your changes.

The following scenarios are examples of when the `create-only` mode might be of use:

**Manual Customization Required**: You need to customize operator-managed resources (ConfigMaps, Deployments, DaemonSets, etc.) with specific configurations that differ from the operator's defaults

**Day 2 Operations**: After initial deployment, you want to prevent the operator from overwriting their manual changes during subsequent reconciliation cycles

**Configuration Drift Prevention**: You want to maintain control over certain resource configurations while still benefiting from the operator's lifecycle management

// Pause reconciliation
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zero-trust-manager-reconciliation.adoc

[id="zero-trust-manager-pause-reconciliation_{context}"]
= Pausing Operator reconciliation

[role="_abstract"]
Pause reconciliation of the operands by enabling `create-only` mode. This setting prevents the Operator from automatically reverting your manual changes to the desired state. You can enable this mode by updating the Operator's subscription object.

[IMPORTANT]
====
When `create-only` mode is disabled, the Operator overwrites the resources if any conflicts exist.
====

.Prerequisites

* You have installed {zero-trust-full} on your machine.

* You have installed the SPIRE Servers, Agents, SPIFFE Container Storage Interface (CSI), and an OpenID Connect (OIDC) Discovery Provider and are in running status.

.Procedure

* To pause reconciling the operands resources managed by the Operator, add the environment variable `CREATE_ONLY_MODE`: `true` in the subscription object by running the following command:
+
[source,terminal]
----
$ oc -n $OPERATOR_NAMESPACE patch subscription openshift-zero-trust-workload-identity-manager --type='merge' -p '{"spec":{"config":{"env":[{"name":"CREATE_ONLY_MODE","value":"true"}]}}}'
----

.Verification
* Check the status of the `SpireServer` resource to confirm that the `create-only` mode is active. The `status` must be `true` and the `reason` must be `CreateOnlyModeEnabled`.
+
[source,terminal]
----
$ oc get SpireServer cluster -o yaml
----
+
The following is an example that confirms that the 'create-only' mode is active.
[source,yaml]
----
status:
  conditions:
  - lastTransitionTime: "2025-12-23T11:36:58Z"
    message: All components are ready
    reason: Ready
    status: "True"
    type: Ready
  - lastTransitionTime: "2025-12-23T11:36:58Z"
    message: All operand CRs are ready
    reason: Ready
    status: "True"
    type: OperandsAvailable
  - lastTransitionTime: "2025-12-23T11:36:58Z"
    message: create-only mode enabled
    reason: CreateOnlyModeEnabled
    status: "True"
    type: CreateOnlyMode
----

[IMPORTANT]
====
The Operator updates the upgradeable condition to `false` in the `operatorCondition` resource. You might not be able to upgrade the Operator when in `create-only` mode.
====

// Removing {zero-trust-full} resources
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zero-trust-manager-reconciliation.adoc

[id="zero-trust-manager-restart-reconciliation_{context}"]

= Resuming Operator reconciliation

[role="_abstract"]
To resume Operator reconciliation after manual configuration or debugging, disable the `create-only` mode. This allows the controller to resume managing resources and applying the desired state. You can disable this mode by setting the environment variable in the subscription object.

.Prerequisites

* You have enabled `create-only` mode on the {zero-trust-full}.

* You have completed your manual configuration or debugging tasks.

.Procedure

* To restart reconciling the Operator-managed resources, add the environment variable `CREATE_ONLY_MODE`: `false` in the subscription object by running the following command:
+
[source,terminal]
----
$ oc -n $OPERATOR_NAMESPACE patch subscription openshift-zero-trust-workload-identity-manager --type='merge' -p '{"spec":{"config":{"env":[{"name":"CREATE_ONLY_MODE","value":"false"}]}}}'
----

.Verification

* Check the status of the `SpireServer` resource to confirm that `create-only` mode is disabled by running the following command:
+
[source,terminal]
----
$ oc get SpireServer cluster -o yaml
----
+
.Example output
[source,yaml]
----
status:
 conditions:
 - lastTransitionTime: "2025-12-23T11:40:00Z"
   message: create-only mode disabled
   reason: CreateOnlyModeDisabled
   status: "False"
   type: CreateOnlyMode
----
