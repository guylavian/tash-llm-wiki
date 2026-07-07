---
title: "Collecting data for Red{nbsp}Hat Support"
type: reference
domain: openshift
slug: virt-4-22-virt-collecting-virt-data
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-collecting-virt-data
version: 4.22
family: virt
documentKind: "Documentation"
---

# Collecting data for Red{nbsp}Hat Support

[id="virt-collecting-virt-data"]
= Collecting data for Red{nbsp}Hat Support

[role="_abstract"]
When you submit a support case to Red{nbsp}Hat Support, it is helpful to provide debugging information for OpenShift Container Platform and {VirtProductName} by using the following tools:

// must-gather not supported for ROSA/OSD, per Dustin Row
must-gather tool::
The `must-gather` tool collects diagnostic information, including resource definitions and service logs.

Prometheus::
Prometheus is a time-series database and a rule evaluation engine for metrics. Prometheus sends alerts to Alertmanager for processing.

Alertmanager::
The Alertmanager service handles alerts received from Prometheus. The Alertmanager is also responsible for sending the alerts to external notification systems.
//link needs to be added for HCP when available

// Module included in the following assemblies:
//
// * virt/support/virt-collecting-virt-data.adoc

[id="virt-collecting-data-about-your-environment_{context}"]
= Collecting data about your environment

[role="_abstract"]
Collecting data about your environment minimizes the time required to analyze and determine the root cause.

.Prerequisites
//link needs to be added for HCP when available
* You have set the retention time for Prometheus metrics data to a minimum of seven days.
* You have configured the Alertmanager to capture relevant alerts and to send alert notifications to a dedicated mailbox so that they can be viewed and persisted outside the cluster.

* You have set the retention time for Prometheus metrics data to a minimum of seven days.
* You have configured the Alertmanager to capture relevant alerts and to send alert notifications to a dedicated mailbox so that they can be viewed and persisted outside the cluster.
* You have recorded the exact number of affected nodes and virtual machines.

.Procedure

// must-gather not supported for ROSA/OSD, per Dustin Row
. Collect must-gather data for the cluster.
. Collect must-gather data for {rh-storage-first}, if necessary.
. Collect must-gather data for {VirtProductName}.
. Collect Prometheus metrics for the cluster.
//link needs to be added for HCP when available

// Module included in the following assemblies:
//
// * virt/support/virt-collecting-virt-data.adoc

[id="virt-collecting-data-about-vms_{context}"]
= Collecting data about virtual machines

[role="_abstract"]
Collecting data about malfunctioning virtual machines (VMs) minimizes the time required to analyze and determine the root cause.

.Prerequisites

* For Linux VMs, you have installed the latest QEMU guest agent.
* For Windows VMs, you have:
** Recorded the Windows patch update details.
** Installed the latest VirtIO drivers.
** Installed the latest QEMU guest agent.
** If Remote Desktop Protocol (RDP) is enabled, you have connected by using the desktop viewer to determine whether there is a problem with the connection software.

.Procedure

// must-gather not supported for ROSA/OSD, per Dustin Row
. Collect must-gather data for the VMs using the `/usr/bin/gather` script.
. Collect screenshots of VMs that have crashed before you restart them.
. Collect memory dumps from VMs before remediation attempts.
. Record factors that the malfunctioning VMs have in common. For example, the VMs have the same host or network.

// must-gather not supported for ROSA/OSD, per Dustin Row
// Module included in the following assemblies:
//
// * virt/support/virt-collecting-virt-data.adoc

//This file contains UI elements and/or package names that need to be updated.

[id="virt-using-virt-must-gather_{context}"]
= Using the must-gather tool for {VirtProductName}

[role="_abstract"]
You can collect data about {VirtProductName} resources by running the `must-gather` command with the {VirtProductName} image.

The default data collection includes information about the following resources:

* {VirtProductName} Operator namespaces, including child objects
* {VirtProductName} custom resource definitions
* Namespaces that contain virtual machines
* Basic virtual machine definitions

You can add optional environment details and scripts to the `must-gather` command to collect additional information. Use these environment variables and scripts to collect data about specific VMs, images, or instance types.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* Run the `must-gather` command to collect data about {VirtProductName}:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion} \
  -- /usr/bin/gather
----
+
[NOTE]
====
You can also collect `must-gather` logs for all Operators and products on your cluster by running following command:

[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --all-images
----
====

.. Run the following command to modify the number of processes running in parallel when collecting `must-gather` data:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion} \
  -- PROS=<number> /usr/bin/gather
----
+
`PROS` defines the number of parallel processes running to collect data. The default number of processes is 5. Increasing the number of processes may result in faster data collection, but uses more resources. Increasing the maximum number of parallel processes is not recommended.

.. Run the following command to collect detailed information for a specific VM in a specific namespace:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion} \
  -- NS=<namespace name> VM=<VM name> /usr/bin/gather --vms_details
----
+
`NS` is the environment variable for `namespace`. It is mandatory when using the `VM` environment variable.

.. Run the following command to collect image, image-stream, and image-stream-tags information from the cluster:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
 --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion} \
 /usr/bin/gather --images
----

.. Run the following command to collect information about instance types from the cluster:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
 --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion} \
 /usr/bin/gather --instancetypes
----

// Module included in the following assemblies:
//
// * virt/support/virt-collecting-virt-data.adoc

[id="virt-must-gather-options_{context}"]
= must-gather tool options

[role="_abstract"]
To troubleshoot complex issues and collect specific data beyond the default logs, add optional parameters to the `must-gather` command when gathering information from your cluster.

You can specify a combination of scripts and environment variables for the following options:

* Collecting detailed virtual machine (VM) information from a namespace
* Collecting detailed information about specified VMs
* Collecting image, image-stream, and image-stream-tags information
* Limiting the maximum number of parallel processes used by the `must-gather` tool

[id="must-gather-environment-variables_{context}"]
== Environment variables

You can specify environment variables for a compatible script.

`NS=<namespace_name>`::: Collect virtual machine information, including `virt-launcher` pod details, from the namespace that you specify. The `VirtualMachine` and `VirtualMachineInstance` CR data is collected for all namespaces.

`VM=<vm_name>`::: Collect details about a particular virtual machine. To use this option, you must also specify a namespace by using the `NS` environment variable.

`PROS=<number_of_processes>`::: Modify the maximum number of parallel processes that the `must-gather` tool uses. The default value is `5`.
+
[IMPORTANT]
====
Using too many parallel processes can cause performance issues. Increasing the maximum number of parallel processes is not recommended.
====

[id="must-gather-scripts_{context}"]
== Scripts

Each script is compatible only with certain environment variable combinations.

`/usr/bin/gather`::: Use the default `must-gather` script, which collects cluster data from all namespaces and includes only basic VM information. This script is compatible only with the `PROS` variable.

`/usr/bin/gather --vms_details`::: Collect VM log files, VM definitions, control-plane logs, and namespaces that belong to {VirtProductName} resources. Specifying namespaces includes their child objects. If you use this parameter without specifying a namespace or VM, the `must-gather` tool collects this data for all VMs in the cluster. This script is compatible with all environment variables, but you must specify a namespace if you use the `VM` variable.

`/usr/bin/gather --images`::: Collect image, image-stream, and image-stream-tags custom resource information. This script is compatible only with the `PROS` variable.

`/usr/bin/gather --instancetypes`::: Collect instance types information. This information is not currently collected by default; you can, however, optionally collect it.

[id="usage-and-examples_{context}"]
== Usage and examples

You can run a script by itself or with one or more compatible environment variables.

.must-gather syntax with optional parameters
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion} \
  -- <environment_variable_1> <environment_variable_2> <script_name>
----

.Compatible parameters
[options="header"]
|===
|Script |Compatible environment variable
|`/usr/bin/gather`
|* `PROS=<number_of_processes>`
|`/usr/bin/gather --vms_details`
|* For a namespace: `NS=<namespace_name>`

* For a VM: `VM=<vm_name> NS=<namespace_name>`

* `PROS=<number_of_processes>`

|`/usr/bin/gather --images`
|* `PROS=<number_of_processes>`
|===

// Module included in the following assemblies:
//
// virt/support/virt-collecting-virt-data.adoc

[id="virt-generating-a-vm-memory-dump_{context}"]
= Generating a VM memory dump

[role="_abstract"]
When a virtual machine (VM) terminates unexpectedly, you can use the `virtctl memory-dump` to generate a memory dump command to output a VM memory dump and save it on a persistent volume claim (PVC). Afterwards, you can analyze the memory dump to diagnose and troubleshoot issues on the VM.

// You can specify an existing PVC or use the `--create-claim` flag to create a new PVC.

.Procedure

. Optional: You have an existing PVC on which you want to save the memory dump.
** The PVC volume mode must be `FileSystem`.
** The PVC must be large enough to contain the memory dump.
+
The formula for calculating the PVC size is `(VMMemorySize + 100Mi) * (1 + FileSystemOverhead)`, where `100Mi` is the memory dump overhead, and `FileSystemOverhead` is defined in the `HCO` object.

. Create a memory dump of the required VM:

** If you have an existing PVC selected on which you want to save the memory dump:
+
[source,terminal]
----
$ virtctl memory-dump get <vm_name> --claim-name=<pvc_name>
----

** If you want to create a new PVC for the memory dump:
+
[source,terminal]
----
$ virtctl memory-dump get <vm_name> --claim-name=<new_pvc_name> --create-claim
----

. Download the memory dump:
+
[source,terminal]
----
$ virtctl memory-dump download <vm_name> --output=<output_file>
----

. Attach the memory dump to a Red Hat Support case.
+
Alternatively, you can inspect the memory dump, for example by using the volatility3 tool.

. Optional: Remove the memory dump:
+
[source,terminal]
----
$ virtctl memory-dump remove <vm_name>
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* VM support overview
* How to provide log files to Red Hat Support (Red Hat Knowledgebase)
* About OpenShift Container Platform monitoring
* About OpenShift Container Platform monitoring
* Installing the QEMU guest agent on a Linux VM
* Installing VirtIO drivers from a SATA CD drive on an existing Windows VM
* Connect to the desktop viewer by using the web console
* Collect memory dumps from VMs
* Submitting a support case
* Modifying retention time and size for Prometheus metrics data
* Configuring the Alertmanager to capture relevant alerts and to send alert notifications to a dedicated mailbox
* Modifying retention time and size for Prometheus metrics data
* Configuring alerts and notifications
* Downloading log files and diagnostic information
* Querying metrics for all projects with the monitoring dashboard
* Installing the latest VirtIO drivers
* Volatility3 tool
* Customer Support
* Create issue
