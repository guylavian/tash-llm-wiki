---
title: "Understanding Helm"
type: reference
domain: openshift
slug: applications-4-22-understanding-helm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/understanding-helm
version: 4.22
family: applications
documentKind: "Documentation"
---

# Understanding Helm

[id="understanding-helm"]
= Understanding Helm

[role="_abstract"]
Helm is a software package manager that simplifies deployment of applications and services to OpenShift Container Platform clusters.

Helm uses a packaging format called _charts_.
A Helm chart is a collection of files that describes the OpenShift Container Platform resources.

Creating a chart in a cluster creates a running instance of the chart known as a _release_.

Each time a chart is created, or a release is upgraded or rolled back, an incremental revision is created.

== Key features

Helm provides the ability to:

* Search through a large collection of charts stored in the chart repository.
* Modify existing charts.
* Create your own charts with OpenShift Container Platform or Kubernetes resources.
* Package and share your applications as charts.

// No tech preview in ROSA/OSD, added ifndef in case this note gets un-commented.
//[NOTE]
//====
// In OpenShift Container Platform 4.10 and 4.11, Helm is disabled for the Multicluster Console (Technology Preview).
//====

== Red Hat Certification of Helm charts for OpenShift

You can choose to verify and certify your Helm charts by Red Hat for all the components you will be deploying on the Red Hat OpenShift Container Platform. Charts go through an automated Red Hat OpenShift certification workflow that guarantees security compliance as well as best integration and experience with the platform. Certification assures the integrity of the chart and ensures that the Helm chart works seamlessly on Red Hat OpenShift clusters.

[role="_additional-resources"]
== Additional resources
* For more information on how to certify your Helm charts as a Red Hat partner, see Red Hat Certification of Helm charts for OpenShift.
* For more information on OpenShift and Container certification guides for Red Hat partners, see Partner Guide for OpenShift and Container Certification.
* For a list of the charts, see the Red Hat `Helm index` file.
// * You can view the available charts at the Red Hat Marketplace. For more information, see Using the Red Hat Marketplace.
