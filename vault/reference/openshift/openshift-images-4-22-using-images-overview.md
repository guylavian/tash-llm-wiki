---
title: "Using images overview"
type: reference
domain: openshift
slug: openshift-images-4-22-using-images-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/openshift_images/using-images-overview
version: 4.22
family: openshift_images
documentKind: "Documentation"
---

# Using images overview

[id="using-images-overview"]
= Using images overview

[role="_abstract"]
To build and deploy containerized applications in OpenShift Container Platform, you can use Source-to-Image (S2I), database, and other container images. These images provide the base components you need to run applications on your cluster.

Red{nbsp}Hat official container images are provided in the Red{nbsp}Hat Registry at registry.redhat.io. OpenShift Container Platform's supported S2I, database, and Jenkins images are provided in the `openshift4` repository in the {quay} Registry. For example, `quay.io/openshift-release-dev/ocp-v4.0-<address>` is the name of an OpenShift Container Platform image.

The xPaaS middleware images are provided in their product repositories on the Red Hat Registry but suffixed with a `-openshift`. For example, `registry.redhat.io/jboss-eap-6/eap64-openshift` is the name of the Red Hat JBoss Enterprise Application Platform (JBoss EAP) image.

All Red{nbsp}Hat supported images are described in the Red Hat Ecosystem Catalog. For every version of each image, you can find details on its contents and usage.

[IMPORTANT]
====
The newer versions of container images are not compatible with earlier versions of OpenShift Container Platform. Verify and use the correct version of container images, based on your version of OpenShift Container Platform.
====

[role="_additional-resources"]
[id="additional-resources_using-images-overview"]
== Additional resources

* Red Hat container registry
* Container images section of the Red Hat Ecosystem Catalog
