---
title: "About the {mce}"
type: reference
domain: openshift
slug: architecture-4-22-mce-overview-ocp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/mce-overview-ocp
version: 4.22
family: architecture
documentKind: "Documentation"
---

# About the {mce}

[id="mce-overview-ocp"]
= About the {mce}

One of the challenges of scaling Kubernetes environments is managing the lifecycle of a growing fleet. To meet that challenge, you can use the {mce-short}. The operator delivers full lifecycle capabilities for managed OpenShift Container Platform clusters and partial lifecycle management for other Kubernetes distributions. It is available in two ways:

* As a standalone operator that you install as part of your OpenShift Container Platform or {oke} subscription
* As part of Red Hat Advanced Cluster Management for Kubernetes

[id="mce-on-ocp"]
== Cluster management with multicluster engine on OpenShift Container Platform

When you enable multicluster engine on OpenShift Container Platform, you gain the following capabilities:

* {hcp-capital}, which is a feature that is based on the HyperShift project. With a centralized hosted control plane, you can operate OpenShift Container Platform clusters in a hyperscale manner.
* Hive, which provisions self-managed OpenShift Container Platform clusters to the hub and completes the initial configurations for those clusters.
* klusterlet agent, which registers managed clusters to the hub.
* Infrastructure Operator, which manages the deployment of the Assisted Service to orchestrate on-premise bare metal and vSphere installations of OpenShift Container Platform, such as {sno} on bare metal. The Infrastructure Operator includes {ztp-first}, which fully automates cluster creation on bare metal and vSphere provisioning with GitOps workflows to manage deployments and configuration changes.
* Open cluster management, which provides resources to manage Kubernetes clusters.

The multicluster engine is included with your OpenShift Container Platform support subscription and is delivered separately from the core payload. To start to use multicluster engine, you deploy the OpenShift Container Platform cluster and then install the operator. For more information, see Installing and upgrading multicluster engine operator.

[id="mce-on-rhacm"]
== Cluster management with Red Hat Advanced Cluster Management

If you need cluster management capabilities beyond what OpenShift Container Platform with multicluster engine can provide, consider Red Hat Advanced Cluster Management. The multicluster engine is an integral part of Red Hat Advanced Cluster Management and is enabled by default.

[id="mce-additional-resources-ocp"]
== Additional resources

For the complete documentation for multicluster engine, see Cluster lifecycle with multicluster engine documentation, which is part of the product documentation for Red Hat Advanced Cluster Management.
