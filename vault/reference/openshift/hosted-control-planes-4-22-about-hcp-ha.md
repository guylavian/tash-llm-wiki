---
title: "About high availability for {hcp}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-about-hcp-ha
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/about-hcp-ha
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# About high availability for {hcp}

[id="about-hcp-ha"]
= About high availability for {hcp}

[role="_abstract"]
You can maintain high availability (HA) for {hcp} by recovering etcd members for a hosted cluster, backing up and restoring etcd for a hosted cluster, and completing a disaster recovery process for a hosted cluster.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp_high_availability/about-hcp-ha.adoc

[id="hcp-mgmt-component-loss-impact_{context}"]
= Impact of the failed management cluster component

[role="_abstract"]
If the management cluster component fails, your workload remains unaffected. In the OpenShift Container Platform management cluster, the control plane is decoupled from the data plane to provide resiliency.

The following table covers the impact of a failed management cluster component on the control plane and the data plane. However, the table does not cover all scenarios for the management cluster component failures.

.Impact of the failed component on {hcp}
[cols="1,1,1",options="header"]
|===
|Name of the failed component |Hosted control plane API status |Hosted cluster data plane status

|Worker node
|Available
|Available

|Availability zone
|Available
|Available

|Management cluster control plane
|Available
|Available

|Management cluster control plane and worker nodes
|Not available
|Available
|===
