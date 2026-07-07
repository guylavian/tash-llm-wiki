---
title: "Managing images overview"
type: reference
domain: openshift
slug: openshift-images-4-22-managing-images-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/openshift_images/managing-images-overview
version: 4.22
family: openshift_images
documentKind: "Documentation"
---

# Managing images overview

[id="managing-images-overview"]
= Managing images overview

[role="_abstract"]
Image streams in OpenShift Container Platform provide a layer of abstraction over container images, enabling automation for your CI/CD pipelines. You can configure builds and deployments to watch image streams and automatically trigger new builds or deployments when images are updated.

The main advantage of using image streams is the automation they enable for your continuous integration and continuous delivery (CI/CD) pipelines. For example:

* Image streams allow OpenShift Container Platform resources such as Builds and Deployments to "watch" them.
* When a new image is added to the stream, or when an existing tag is modified to point to a new image, the watching resources receive notifications.
* When notifications are received, the watching resources can automatically react by performing a new build or a new deployment.
