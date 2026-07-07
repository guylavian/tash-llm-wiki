---
title: "Options for embedding applications in a RHEL for Edge image"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-embedded-apps-on-rhel-edge
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-embedded-apps-on-rhel-edge
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Options for embedding applications in a RHEL for Edge image

[id="microshift-embedded-apps-on-rhel-edge"]
= Options for embedding applications in a RHEL for Edge image

[role="_abstract"]
You can embed microservices-based workloads and applications in a {op-system-ostree-first} image to run in a {microshift-short} node. Embedded applications can be installed directly on edge devices to run in disconnected or offline environments.

[id="microshift-add-app-RPMs-to-rpm-ostree-image_{context}"]
== Adding application RPMs to an rpm-ostree image
If you have an application that includes APIs, container images, and configuration files for deployment such as manifests, you can build application RPMs. You can then add the RPMs to your {op-system-ostree} system image.

The following is an outline of the procedures to embed applications or workloads in a fully self-contained operating system image:

* Build your own RPM that includes your application manifest.
* Add the RPM to the blueprint you used to install OpenShift Container Platform.
* Add the workload container images to the same blueprint.
* Create a bootable ISO.

For a step-by-step tutorial about preparing and embedding applications in a {op-system-ostree} image, use the following tutorial:

* Embedding applications tutorial

[id="microshift-add-app-manifests-to-image_{context}"]
== Adding application manifests to an image for offline use
If you have a simple application that includes a few files for deployment such as manifests, you can add those manifests directly to a {op-system-ostree} system image.

See the "Create a custom file blueprint customization" section of the following {op-system-ostree} documentation for an example:

* Create a custom file blueprint customization

[id="microshift-embed-apps-for-offline-use_{context}"]
== Embedding applications for offline use
If you have an application that includes more than a few files, you can embed the application for offline use. See the following procedure:

* Embedding applications for offline use

//additional resources for assembly
[id="additional-resources_microshift-embed-apps-on-rhel-edge_{context}"]
[role="_additional-resources"]
== Additional resources
* Embedding OpenShift Container Platform in an RPM-OSTree image

* Composing, installing, and managing {op-system-ostree} images

* Preparing for image building

* Meet Red Hat Device Edge

* Composing a RHEL for Edge image using image builder command-line

* Image Builder system requirements
