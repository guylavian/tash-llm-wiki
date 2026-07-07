---
title: "Sizing requirements for GitOps Operator"
type: reference
domain: openshift
slug: cicd-4-22-about-sizing-requirements-gitops
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/about-sizing-requirements-gitops
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Sizing requirements for GitOps Operator

[id="about-sizing-requirements-gitops"]
= Sizing requirements for GitOps Operator

[role="_abstract"]
The sizing requirements page displays the sizing requirements for installing {gitops-title} on OpenShift Container Platform. It also provides the sizing details for the default ArgoCD instance that is instantiated by the GitOps Operator.

// Module is included in the following assemblies:
//
// * openshift-docs/cicd/gitops/about-sizing-requirements-gitops.adoc

[id="sizing-requirements-for-gitops_{context}"]
= Sizing requirements for GitOps

[role="_abstract"]
{gitops-title} is a declarative way to implement continuous deployment for cloud-native applications. Through GitOps, you can define and configure the CPU and memory requirements of your application.

Every time you install the {gitops-title} Operator, the resources on the namespace are installed within the defined limits. If the default installation does not set any limits or requests, the Operator fails within the namespace with quotas. Without enough resources, the cluster cannot schedule ArgoCD related pods. The following table details the resource requests and limits for the default workloads:

[cols="2,2,2,2,2",options="header"]
|===
|Workload |CPU requests |CPU limits |Memory requests |Memory limits
|argocd-application-controller |1 |2 |1024M |2048M
|applicationset-controller |1 |2 |512M |1024M
|argocd-server |0.125 |0.5 |128M |256M
|argocd-repo-server |0.5 |1 |256M |1024M
|argocd-redis |0.25 |0.5 |128M |256M
|argocd-dex |0.25 |0.5 |128M |256M
|HAProxy |0.25 |0.5 |128M |256M
|===

Optionally, you can also use the ArgoCD custom resource with the `oc` command to see the specifics and modify them:

[source,terminal]
----
oc edit argocd <name of argo cd> -n namespace
----
