---
title: "Source-to-image"
type: reference
domain: openshift
slug: openshift-images-4-22-using-s21-images
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/openshift_images/using-s21-images
version: 4.22
family: openshift_images
documentKind: "Documentation"
---

# Source-to-image

[id="using-s21-images"]
= Source-to-image

[role="_abstract"]
To create containerized applications in OpenShift Container Platform without manually configuring runtime environments, you can use Source-to-Image (S2I) images. S2I images are runtime base images for languages such as Node.js, Python, and Java that you can insert your code into. You can use Red{nbsp}Hat Software Collections images as a foundation for applications that rely on specific runtime environments, and access S2I images through the Cluster Samples Operator.

// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc

[id="accessing-s2i-builder-images-in-developer-console_{context}"]
= Accessing S2I builder images in the OpenShift Container Platform Developer Console

[role="_abstract"]
You can access S2I builder images through the Developer Console in the web console.
You need these images to build containerized applications from your source code.

.Procedure

. Log in to the OpenShift Container Platform web console using your login credentials. The default view for the OpenShift Container Platform web console is the *Administrator* perspective.

. Use the perspective switcher to switch to the *Developer* perspective.

. In the *+Add* view, use the *Project* drop-down list to select an existing project or create a new project.

. Click *All services* in the *Developer Catalog* tile.

. Click *Builder Images* under *Type* to see the available S2I images.

// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc

[id="images-s2i-build-process-overview_{context}"]
= Source-to-image build process overview

[role="_abstract"]
Source-to-image (S2I) is a build process in OpenShift Container Platform that injects your source code into a container image. S2I automates the creation of ready-to-run container images from your application source code without manual configuration.

S2I performs the following steps:

. Runs the `FROM <builder image>` command
. Copies the source code to a defined location in the builder image
. Runs the assemble script in the builder image
. Sets the run script in the builder image as the default command

Buildah then creates the container image.

[role="_additional-resources"]
[id="additional-resources_using-s21-images"]
== Additional resources

* Red{nbsp}Hat Software Collections container images
* Introduction to source-to-image for OpenShift with Red Hat build of OpenJDK
* Configuring the Cluster Samples Operator
* Using build strategies
* Troubleshooting the Source-to-Image process
* Creating images from source code with source-to-image
* About testing source-to-image images
