---
title: "About CI/CD"
type: reference
domain: openshift
slug: cicd-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/index
version: 4.22
family: cicd
documentKind: "Documentation"
---

# About CI/CD

[id="ci-cd-overview"]
= About CI/CD

OpenShift Container Platform is an enterprise-ready Kubernetes platform for developers, which enables organizations to automate the application delivery process through DevOps practices, such as continuous integration (CI) and continuous delivery (CD). To meet your organizational needs, the OpenShift Container Platform provides the following CI/CD solutions:

* OpenShift Builds
* {pipelines-shortname}
* OpenShift GitOps
* Jenkins

[id="openshift-builds"]
== OpenShift Builds
OpenShift Builds provides you the following options to configure and run a build:

* Builds using Shipwright is an extensible build framework based on the Shipwright project. You can use it to build container images on a cluster. You can build container images from source code and Dockerfile by using image build tools, such as Source-to-Image (S2I) and Buildah.
+
For more information, see builds for Red Hat OpenShift.

* Builds using `BuildConfig` objects is a declarative build process to create cloud-native apps. You can define the build process in a YAML file that you use to create a `BuildConfig` object. This definition includes attributes such as build triggers, input parameters, and source code. When deployed, the `BuildConfig` object builds a runnable image and pushes the image to a container image registry. With the `BuildConfig` object, you can create a Docker, Source-to-image (S2I), or custom build.
+
For more information, see Understanding image builds.

[id="openshift-pipelines"]
== {pipelines-shortname}
{pipelines-shortname} provides a Kubernetes-native CI/CD framework to design and run each step of the CI/CD pipeline in its own container. It can scale independently to meet the on-demand pipelines with predictable outcomes.

For more information, see Red Hat OpenShift Pipelines.

[id="openshift-gitops"]
== OpenShift GitOps
OpenShift GitOps is an Operator that uses Argo CD as the declarative GitOps engine. It enables GitOps workflows across multicluster OpenShift and Kubernetes infrastructure. Using OpenShift GitOps, administrators can consistently configure and deploy Kubernetes-based infrastructure and applications across clusters and development lifecycles.

For more information, see Red Hat OpenShift GitOps.

[id="jenkins-ci-cd"]
== Jenkins
Jenkins automates the process of building, testing, and deploying applications and projects. OpenShift Developer Tools provides a Jenkins image that integrates directly with OpenShift Container Platform. Jenkins can be deployed on OpenShift by using the Samples Operator templates or certified Helm chart.

For more information, see Configuring Jenkins images.
