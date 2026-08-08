---
title: "Challenges of the network far edge"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-deploying-far-edge-clusters-at-scale
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-clusters-at-scale
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Challenges of the network far edge

[id="ztp-deploying-far-edge-clusters-at-scale"]
= Challenges of the network far edge

Edge computing presents complex challenges when managing many sites in geographically displaced locations. Use {ztp-first} to provision and manage sites at the far edge of the network.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-clusters-at-scale.adoc

[id="ztp-challenges-of-far-edge-deployments_{context}"]
= Overcoming the challenges of the network far edge

[role="_abstract"]
Today, service providers want to deploy their infrastructure at the edge of the network. This presents significant challenges:

* How do you handle deployments of many edge sites in parallel?
* What happens when you need to deploy sites in disconnected environments?
* How do you manage the lifecycle of large fleets of clusters?

{ztp-first} and _GitOps_ meets these challenges by allowing you to provision remote edge sites at scale with declarative site definitions and configurations for bare-metal equipment. Template or overlay configurations install OpenShift Container Platform features that are required for CNF workloads. The full lifecycle of installation and upgrades is handled through the {ztp} pipeline.

{ztp} uses GitOps for infrastructure deployments. With GitOps, you use declarative YAML files and other defined patterns stored in Git repositories. {rh-rhacm-first} uses your Git repositories to drive the deployment of your infrastructure.

GitOps provides traceability, role-based access control (RBAC), and a single source of truth for the desired state of each site. Scalability issues are addressed by Git methodologies and event driven operations through webhooks.

You start the {ztp} workflow by creating declarative site definition and configuration custom resources (CRs) that the {ztp} pipeline delivers to the edge nodes.

The following diagram shows how {ztp} works within the far edge framework.

image::217_OpenShift_Zero_Touch_Provisioning_updates_1022_1.png[{ztp} at the network far edge]

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-clusters-at-scale.adoc

[id="about-ztp_{context}"]
= Using {ztp} to provision clusters at the network far edge

[role="_abstract"]
{rh-rhacm-first} manages clusters in a hub-and-spoke architecture, where a single hub cluster manages many spoke clusters. Hub clusters running {rh-rhacm} provision and deploy the managed clusters by using {ztp-first} and the assisted service that is deployed when you install {rh-rhacm}.

The assisted service handles provisioning of OpenShift Container Platform on single node clusters, three-node clusters, or standard clusters running on bare metal.

A high-level overview of using {ztp} to provision and maintain bare-metal hosts with OpenShift Container Platform is as follows:

* A hub cluster running {rh-rhacm} manages an {product-registry} that mirrors the OpenShift Container Platform release images. {rh-rhacm} uses the {product-registry} to provision the managed clusters.

* You manage the bare-metal hosts in a YAML format inventory file, versioned in a Git repository.

* You make the hosts ready for provisioning as managed clusters, and use {rh-rhacm} and the assisted service to install the bare-metal hosts on site.

Installing and deploying the clusters is a two-stage process, involving an initial installation phase, and a subsequent configuration and deployment phase. The following diagram illustrates this workflow:

image::474_OpenShift_OpenShift_RAN_RDS_arch_updates_1023.png[Using GitOps and {ztp} to install and deploy managed clusters]

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-clusters-at-scale.adoc

[id="ztp-creating-ztp-crs-for-multiple-managed-clusters_{context}"]
= Installing managed clusters with ClusterInstance resources and {rh-rhacm}

[role="_abstract"]
{ztp-first} uses `ClusterInstance` custom resources (CRs) in a Git repository to manage the processes that install OpenShift Container Platform clusters. The `ClusterInstance` CR contains cluster-specific parameters required for installation. It has options for applying select configuration CRs during installation including user defined extra manifests.

The {ztp} plugin processes `ClusterInstance` CRs to generate a collection of CRs on the hub cluster. This triggers the assisted service in {rh-rhacm-first} to install OpenShift Container Platform on the bare-metal host. You can find installation status and error messages in these CRs on the hub cluster.
You can provision single clusters manually or in batches with {ztp}:

Provisioning a single cluster:: Create a single `ClusterInstance` CR and related configuration CRs for the cluster, and apply them in the hub cluster to begin cluster provisioning. This is a good way to test your CRs before deploying on a larger scale.

Provisioning many clusters:: Install managed clusters in batches of up to 500 by defining `ClusterInstance` and related CRs in a Git repository. ArgoCD uses the `ClusterInstance` CRs to deploy the clusters. The {rh-rhacm} policy generator creates the manifests and applies them to the hub cluster. This starts the cluster provisioning process.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-clusters-at-scale.adoc

[id="ztp-configuring-cluster-policies_{context}"]
= Configuring managed clusters with policies and {policy-gen-cr} resources

[role="_abstract"]
{ztp-first} uses {rh-rhacm-first} to configure clusters by using a policy-based governance approach to applying the configuration.

The policy generator is a plugin for the GitOps Operator that enables the creation of {rh-rhacm} policies from a concise template. The tool can combine multiple CRs into a single policy, and you can generate multiple policies that apply to various subsets of clusters in your fleet.

[NOTE]
====
For scalability and to reduce the complexity of managing configurations across the fleet of clusters, use configuration CRs with as much commonality as possible.

* Where possible, apply configuration CRs using a fleet-wide common policy.

* The next preference is to create logical groupings of clusters to manage as much of the remaining configurations as possible under a group policy.

* When a configuration is unique to an individual site, use {rh-rhacm} templating on the hub cluster to inject the site-specific data into a common or group policy. Alternatively, apply an individual site policy for the site.
====

The following diagram shows how the policy generator interacts with GitOps and {rh-rhacm} in the configuration phase of cluster deployment.

image::217_OpenShift_Zero_Touch_Provisioning_updates_1022_3.png[Policy generator]

For large fleets of clusters, it is typical for there to be a high-level of consistency in the configuration of those clusters.

The following recommended structuring of policies combines configuration CRs to meet several goals:

* Describe common configurations once and apply to the fleet.

* Minimize the number of maintained and managed policies.

* Support flexibility in common configurations for cluster variants.

.Recommended {policy-gen-cr} policy categories
[cols="1,5", width="100%", options="header"]
|====
|Policy category
|Description

|Common
|A policy that exists in the common category is applied to all clusters in the fleet. Use common `{policy-gen-cr}` CRs to apply common installation settings across all cluster types.

|Groups
|A policy that exists in the groups category is applied to a group of clusters in the fleet. Use group `{policy-gen-cr}` CRs to manage specific aspects of single-node, three-node, and standard cluster installations. Cluster groups can also follow geographic region, hardware variant, etc.

|Sites
|A policy that exists in the sites category is applied to a specific cluster site. Any cluster
can have its own specific policies maintained.
|====

[role="_additional-resources"]
.Additional resources

* Configuring managed cluster policies by using PolicyGenerator resources

* Comparing {rh-rhacm} PolicyGenerator and PolicyGenTemplate resource patching

* Preparing the {ztp} Git repository
