---
title: "Migration from OpenShift Container Platform 3 to 4 overview"
type: reference
domain: openshift
slug: migrating-from-ocp-3-to-4-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/migrating_from_ocp_3_to_4/index
version: 4.22
family: migrating_from_ocp_3_to_4
documentKind: "Documentation"
---

# Migration from OpenShift Container Platform 3 to 4 overview

[id="migration-from-version-3-to-4-overview"]
= Migration from OpenShift Container Platform 3 to 4 overview

OpenShift Container Platform 4 clusters are different from OpenShift Container Platform 3 clusters. OpenShift Container Platform 4 clusters contain new technologies and functionality that result in a cluster that is self-managing, flexible, and automated. To learn more about migrating from OpenShift Container Platform 3 to 4 see About migrating from OpenShift Container Platform 3 to 4.

[id="mtc-3-to-4-overview-differences-mtc"]
== Differences between OpenShift Container Platform 3 and 4
Before migrating from OpenShift Container Platform 3 to 4, you can check differences between OpenShift Container Platform 3 and 4. Review the following information:

* Architecture
* Installation and update
* Storage, network, security, and monitoring considerations

[id="mtc-3-to-4-overview-planning-network-considerations-mtc"]
== Planning network considerations
Before migrating from OpenShift Container Platform 3 to 4, review the differences between OpenShift Container Platform 3 and 4 for information about the following areas:

* DNS considerations
** Isolating the DNS domain of the target cluster from the clients.
** Setting up the target cluster to accept the source DNS domain.
