---
title: "Monitoring overview"
type: reference
domain: openshift
slug: virt-4-22-virt-monitoring-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-monitoring-overview
version: 4.22
family: virt
documentKind: "Documentation"
---

# Monitoring overview

[id="virt-monitoring-overview"]
= Monitoring overview

[role="_abstract"]
Monitor the health of your cluster and virtual machines (VMs) to have a unified operational view of your environment. This ensures high availability and optimal resource performance.

You can monitor the health of your cluster and VMs with the following tools:

Monitoring {VirtProductName} VM health status::
View the overall health of your {VirtProductName} environment in the web console by navigating to the *Home* -> *Overview* page in the OpenShift Container Platform web console. The *Status* card displays the overall health of {VirtProductName} based on the alerts and conditions.

OpenShift Container Platform cluster checkup framework::
Run automated tests with the OpenShift Container Platform cluster checkup framework to ensure that your cluster, including cluster storage, is optimally configured for {VirtProductName}.

Prometheus queries for virtual resources::
Query vCPU, network, storage, and guest memory swapping usage and live migration progress.

VM custom metrics::
Configure the `node-exporter` service to expose internal VM metrics and processes.

VM health checks::
Configure readiness, liveness, and guest agent ping probes and a watchdog for VMs.

Runbooks::

Diagnose and resolve issues that trigger {VirtProductName} alerts in the OpenShift Container Platform web console.

//:FeatureName: The guest agent ping probe
//include::snippets/technology-preview.adoc[]
