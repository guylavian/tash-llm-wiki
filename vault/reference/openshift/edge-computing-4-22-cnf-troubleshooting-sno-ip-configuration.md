---
title: "Troubleshoot {sno} network reconfiguration"
type: reference
domain: openshift
slug: edge-computing-4-22-cnf-troubleshooting-sno-ip-configuration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-troubleshooting-sno-ip-configuration
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Troubleshoot {sno} network reconfiguration

[id="cnf-troubleshooting-sno-ip-configuration"]
= Troubleshoot {sno} network reconfiguration

Use the following information to diagnose and resolve network reconfiguration issues on {sno} clusters.

// Module included in the following assemblies:
//
// * edge_computing/sno_ip_configuration/cnf-troubleshooting-sno-ip-configuration.adoc

[id="cnf-gathering-sno-ip-configuration-diagnostics_{context}"]
= Gather diagnostic information for network reconfiguration issues

[role="_abstract"]
You can gather diagnostic information to help troubleshoot network reconfiguration issues on {sno} clusters.

.Procedure

. Inspect the `IPConfig` custom resource (CR) status by running the following command:
+
[source,terminal]
----
$ oc get ipc ipconfig -o yaml
----
+
Review the `status.conditions` field for the current state, reason, and message. Check `status.validNextStages` for possible stage transitions, and `status.history` for timestamps of stage progression.

. View the {lcao} controller logs by running the following command:
+
[source,terminal]
----
$ oc logs -n openshift-lifecycle-agent deployment/lifecycle-agent-controller-manager -c manager
----

. Create a debug session on the target node by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
# chroot /host
----
+
* Replace `<node_name>` with the name of your {sno} node.

. View the relevant service logs depending on which phase you are troubleshooting by running one of the following commands:
+
--
* View the logs for pre-pivot issues by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u lca-ipconfig-pre-pivot -b --no-pager
----

* View the logs for post-pivot issues by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u ip-configuration.service -b --no-pager
----

* View the logs for `init-monitor` watchdog issues by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u lca-init-monitor.service -b --no-pager
----

* View the logs for rollback issues by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u lca-ipconfig-rollback -b --no-pager
----
--

// Module included in the following assemblies:
//
// * edge_computing/sno_ip_configuration/cnf-troubleshooting-sno-ip-configuration.adoc

[id="cnf-troubleshooting-sno-ip-configuration_{context}"]
= Network reconfiguration troubleshooting reference

[role="_abstract"]
Use the following reference information to help diagnose and resolve network reconfiguration issues on {sno} clusters.

.On-node artifacts for troubleshooting
[cols="2,3",options="header"]
|===
|File |Description

|`/var/lib/lca/workspace/ip-config-pre-pivot.json`
|Pre-pivot configuration data

|`/var/lib/lca/workspace/ip-config-post-pivot.json`
|Post-pivot configuration data

|`/var/lib/lca/workspace/nmstate.yaml`
|Generated `nmstate` configuration for network changes

|`/var/lib/lca/workspace/recert_config.json`
|Configuration for certificate regeneration

|`/var/lib/lca/workspace/ip-config-autorollback-config.json`
|Auto-rollback configuration

|`/var/lib/lca/workspace/recert-pull-secret.json`
|Pull secret for the recert image, if a custom pull secret was specified

|`/var/lib/lca/ipc.json`
|Persistence file that stores `IPConfig` state for rollback and status continuity across restarts
|===

.Common failure patterns
[cols="1,2,2",options="header"]
|===
|Issue |Cause |Solution

|Stage transition rejected
|You attempted to transition to a stage not in `status.validNextStages`.
|Check `status.validNextStages` and only transition to an allowed stage.

|Specification fields cannot be changed
|You attempted to modify `spec` fields while the CR is not in the `Idle` stage.
|Wait for the current operation to complete and the CR to return to `Idle`.

|Health checks never pass
|Cluster health blockers are preventing progress.
|Investigate cluster health issues.

|Post-pivot phase failed
|An error occurred during network configuration or certificate regeneration.
|Review the post-pivot service logs. If auto-rollback is enabled, the node automatically reverts. Otherwise, manually trigger rollback by setting `spec.stage: Rollback`.

|Pods not receiving new IP family
|Pre-existing pods might not automatically receive an IP address from the new family because of CNI behavior.
|Delete and re-create the affected pods to obtain addresses from the new IP family.

|Configuration stuck in disconnected environment
|The {lcao} or recert container might be attempting to pull images not available in the disconnected registry.
|Ensure all required images are mirrored to your disconnected registry before starting. Verify the `lca.openshift.io/recert-pull-secret` annotation references a valid pull secret.
|===

[role="_additional-resources"]
.Additional resources

* Gathering data about your cluster
