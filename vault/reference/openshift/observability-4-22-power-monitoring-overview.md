---
title: "{PM-shortname-c} overview"
type: reference
domain: openshift
slug: observability-4-22-power-monitoring-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/power-monitoring-overview
version: 4.22
family: observability
documentKind: "Documentation"
---

# {PM-shortname-c} overview

[id="power-monitoring-overview"]
= {PM-shortname-c} overview

// Module included in the following assemblies:
//
// * power_monitoring/power-monitoring-overview.adoc

[id="power-monitoring-about-power-monitoring_{context}"]
= About {PM-shortname}

You can use {PM-title} to monitor the power usage and identify power-consuming containers running in an OpenShift Container Platform cluster. {PM-shortname-c} collects and exports energy-related system statistics from various components, such as CPU and DRAM. It provides estimates and granular power consumption data for Kubernetes pods and namespaces, and reads the power consumption of nodes.

[WARNING]
====
{PM-shortname-c} Technology Preview works only in bare-metal deployments. Most public cloud vendors do not expose Kernel Power Management Subsystems to virtual machines.
====

// Module included in the following assemblies:
//
// * power_monitoring/power-monitoring-overview.adoc

[id="power-monitoring-kepler-architecture_{context}"]
= {PM-shortname-c} architecture

{PM-shortname-c} is made up of the following major components:

The {PM-operator}:: For administrators, the {PM-operator} streamlines the monitoring of power usage for workloads by simplifying the deployment and management of {PM-kepler} in an OpenShift Container Platform cluster. The setup and configuration for the {PM-operator} are simplified by adding a `PowerMonitor` custom resource definition (CRD). The Operator also manages operations, such as upgrading, removing, configuring, and redeploying {PM-kepler}.

{PM-kepler}:: {PM-kepler} is a key component of {PM-shortname}. It is responsible for monitoring the power usage of containers running in OpenShift Container Platform. It generates metrics related to the power usage of both nodes and containers.

// Module included in the following assemblies:
//
// * power_monitoring/power-monitoring-overview.adoc

[id="power-monitoring-hardware-support_{context}"]
= {PM-kepler} hardware support

{PM-kepler} is the key component of {PM-shortname} that collects real-time CPU power consumption data from a node through the RAPL Subsystem. By understanding the total power consumption of the node and calculating the percent of CPU time each process is using, it is able to estimate the power consumption at a per process and container level.

Kernel Power Management Subsystem::
* `rapl-sysfs`: This requires access to the `/sys/class/powercap/intel-rapl` directory.

// Module included in the following assemblies:
//
// * power_monitoring/power-monitoring-overview.adoc

[id="power-monitoring-fips-support_{context}"]
= About FIPS compliance for {PM-operator}

Starting with version 0.4, {PM-operator} for Red{nbsp}Hat OpenShift is FIPS compliant. When deployed on an OpenShift Container Platform cluster in FIPS mode, it uses {op-system-base-full} cryptographic libraries validated by National Institute of Standards and Technology (NIST).

For details on the NIST validation program, see Cryptographic module validation program. For the latest NIST status of {op-system-base} cryptographic libraries, see Compliance activities and government standards.

To enable FIPS mode, you must install {PM-operator} for Red{nbsp}Hat OpenShift on an OpenShift Container Platform cluster. For more information, see "Do you need extra security for your cluster?".

[role="_additional-resources"]
[id="additional-resources_power-monitoring-overview"]
== Additional resources
* {PM-shortname-c} dashboards overview

* Do you need extra security for your cluster?
