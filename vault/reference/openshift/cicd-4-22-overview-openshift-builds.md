---
title: "Overview of Builds"
type: reference
domain: openshift
slug: cicd-4-22-overview-openshift-builds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/overview-openshift-builds
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Overview of Builds

[id="overview-openshift-builds"]
= Overview of Builds

Builds is an extensible build framework based on the Shipwright project, which you can use to build container images on your OpenShift Container Platform cluster. You can build container images from source code and Dockerfiles by using image build tools, such as Source-to-Image (S2I) and Buildah. You can create and apply build resources, view logs of build runs, and manage builds in your OpenShift Container Platform namespaces.

Builds includes the following capabilities:

* Standard Kubernetes-native API for building container images from source code and Dockerfiles
* Support for Source-to-Image (S2I) and Buildah build strategies
* Extensibility with your own custom build strategies
* Execution of builds from source code in a local directory
* Shipwright CLI for creating and viewing logs, and managing builds on the cluster
* Integrated user experience with the *Developer* perspective of the OpenShift Container Platform web console

[NOTE]
====
Because Builds releases on a different cadence from OpenShift Container Platform, the Builds documentation is now available as a separate documentation set at Builds for Red Hat OpenShift.
====
