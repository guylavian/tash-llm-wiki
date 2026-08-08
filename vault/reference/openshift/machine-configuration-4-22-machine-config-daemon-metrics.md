---
title: "Machine Config Daemon metrics overview"
type: reference
domain: openshift
slug: machine-configuration-4-22-machine-config-daemon-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/machine-config-daemon-metrics
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Machine Config Daemon metrics overview

[id="machine-config-daemon-metrics"]
= Machine Config Daemon metrics overview

The Machine Config Daemon is a part of the Machine Config Operator. It runs on every node in the cluster. The Machine Config Daemon manages configuration changes and updates on each of the nodes.

// Module included in the following assemblies:
//
// * machine-config/machine-config-daemon-metrics.adoc

[id="machine-config-daemon-metrics-understanding_{context}"]
= Understanding Machine Config Daemon metrics

Beginning with OpenShift Container Platform 4.3, the Machine Config Daemon provides a set of metrics. These metrics can be accessed using the Prometheus Cluster Monitoring stack.

The following table describes this set of metrics. Some entries contain commands for getting specific logs. However, the most comprehensive set of logs is available using the `oc adm must-gather` command.

[NOTE]
====
Metrics marked with `+*+` in the *Name* and *Description* columns represent serious errors that might cause performance problems. Such problems might prevent updates and upgrades from proceeding.
====

[cols="1,1,2,2", options="header"]
.MCO metrics
|===
|Name
|Format
|Description
|Notes

|`mcd_host_os_and_version`
|`[]string{"os", "version"}`
|Shows the OS that MCD is running on, such as RHCOS or RHEL. In case of RHCOS, the version is provided.
|

|`mcd_host_os_and_version`
|`[]string{"os", "version"}`
|Shows the OS that MCD is running on, such as Fedora.
|

|`mcd_drain_err*`
|
|Logs errors received during failed drain. *
|While drains might need multiple tries to succeed, terminal failed drains prevent updates from proceeding. The `drain_time` metric, which shows how much time the drain took, might help with troubleshooting.

For further investigation, see the logs by running:

`$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon`

|`mcd_pivot_err*`
|`[]string{"err", "node", "pivot_target"}`
|Logs errors encountered during pivot. *
|Pivot errors might prevent OS upgrades from proceeding.

For further investigation, run this command to see the logs from the `machine-config-daemon` container:

`$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon`

|`mcd_state`
|`[]string{"state", "reason"}`
|State of Machine Config Daemon for the indicated node. Possible states are "Done", "Working", and "Degraded". In case of "Degraded", the reason is included.
|For further investigation, see the logs by running:

`$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon`

|`mcd_kubelet_state*`
|
|Logs kubelet health failures.  *
|This is expected to be empty, with failure count of 0. If failure count exceeds 2, the error indicating threshold is exceeded. This indicates a possible issue with the health of the kubelet.

For further investigation, run this command to access the node and see all its logs:

`$ oc debug node/<node> -- chroot /host journalctl -u kubelet`

|`mcd_reboot_err*`
|`[]string{"message", "err", "node"}`
|Logs the failed reboots and the corresponding errors. *
|This is expected to be empty, which indicates a successful reboot.

For further investigation, see the logs by running:

`$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon`

|`mcd_update_state`
|`[]string{"config", "err"}`
|Logs success or failure of configuration updates and the corresponding errors.
|The expected value is `rendered-master/rendered-worker-XXXX`. If the update fails, an error is present.

For further investigation, see the logs by running:

`$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon`
|===

[role="_additional-resources"]
.Additional resources
* About OpenShift Container Platform monitoring
* Gathering data about your cluster
