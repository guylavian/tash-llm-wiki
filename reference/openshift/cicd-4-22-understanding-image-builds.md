---
title: "Understanding image builds"
type: reference
domain: openshift
slug: cicd-4-22-understanding-image-builds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/understanding-image-builds
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Understanding image builds

[id="understanding-image-builds"]
= Understanding image builds

// Module included in the following assemblies:
//
//*builds/understanding-image-builds

[id="builds-about_{context}"]
= Builds

A build is the process of transforming input parameters into a resulting object. Most often, the process is used to transform input parameters or source code into a runnable image. A `BuildConfig` object is the definition of the entire build process.

OpenShift Container Platform uses Kubernetes by creating containers from build images and pushing them to a container image registry.

Build objects share common characteristics including inputs for a build, the requirement to complete a build process, logging the build process, publishing resources from successful builds, and publishing the final status of the build. Builds take advantage of resource restrictions, specifying limitations on resources such as CPU usage, memory usage, and build or pod execution time.

The OpenShift Container Platform build system provides extensible support for build strategies that are based on selectable types specified in the build API. There are three primary build strategies available:

* Docker build
* Source-to-image (S2I) build
* Custom build

By default, docker builds and S2I builds are supported.

The resulting object of a build depends on the builder used to create it. For docker and S2I builds, the resulting objects are runnable images. For custom builds, the resulting objects are whatever the builder image author has specified.

Additionally, the pipeline build strategy can be used to implement sophisticated
workflows:

* Continuous integration
* Continuous deployment

// Module included in the following assemblies:
//
//*builds/build-strategies.adoc
//*builds/understanding-image-builds

[id="builds-strategy-docker-build_{context}"]
= Docker build

OpenShift Container Platform uses Buildah to build a container image from a Dockerfile. For more information on building container images with Dockerfiles, see the Dockerfile reference documentation.

[TIP]
====
If you set Docker build arguments by using the `buildArgs` array, see Understand how ARG and FROM interact in the Dockerfile reference documentation.
====

// Module included in the following assemblies:
//
//* builds/build-strategies.adoc
//* builds/understanding-image-builds.adoc

[id="builds-strategy-s2i-build_{context}"]
= Source-to-image build

Source-to-image (S2I) is a tool for building reproducible container images. It produces ready-to-run images by injecting application source into a container image and assembling a new image. The new image incorporates the base image, the builder, and built source and is ready to use with the `buildah run` command. S2I supports incremental builds, which re-use previously downloaded dependencies, previously built artifacts, and so on.

The advantages of S2I include the following:

[horizontal]
Image flexibility:: S2I scripts can be written to inject application code into almost any existing Docker-formatted container image, taking advantage of the existing ecosystem. Note that, currently, S2I relies on `tar` to inject application source, so the image needs to be able to process tarred content.

Speed:: With S2I, the assemble process can perform a large number of complex operations without creating a new layer at each step, resulting in a fast process. In addition, S2I scripts can be written to re-use artifacts stored in a previous version of the application image, rather than having to download or build them each time the build is run.

Patchability:: S2I allows you to rebuild the application consistently if an underlying image needs a patch due to a security issue.

Operational efficiency:: By restricting build operations instead of allowing arbitrary actions, as a Dockerfile would allow, the PaaS operator can avoid accidental or intentional abuses of the build system.

Operational security:: Building an arbitrary Dockerfile exposes the host system to root privilege escalation. This can be exploited by a malicious user because the entire Docker build process is run as a user with Docker privileges. S2I restricts the operations performed as a root user and can run the scripts as a non-root user.

User efficiency:: S2I prevents developers from performing arbitrary `yum install` type operations, which could slow down development iteration, during their application build.

Ecosystem:: S2I encourages a shared ecosystem of images where you can leverage best practices for your applications.

Reproducibility:: Produced images can include all inputs including specific versions of build tools and dependencies. This ensures that the image can be reproduced precisely.

// Custom builds require cluster-admin
// Module included in the following assemblies:
//
// * builds/build-strategies.adoc

[id="builds-strategy-custom-build_{context}"]
= Custom build

The custom build strategy allows developers to define a specific builder image responsible for the entire build process. Using your own builder image allows you to customize your build process.

A custom builder image is a plain container image embedded with build process logic, for example for building RPMs or base images.

Custom builds run with a high level of privilege and are not available to users by default. Only users who can be trusted with cluster administration permissions should be granted access to run custom builds.

// Module included in the following assemblies:
//
//*builds/build-strategies.adoc
//*builds/understanding-image-builds

[id="builds-strategy-pipeline-build_{context}"]
= Pipeline build

[IMPORTANT]
====
The Pipeline build strategy is deprecated in OpenShift Container Platform 4. Equivalent and improved functionality is present in the OpenShift Container Platform Pipelines based on Tekton.

Jenkins images on OpenShift Container Platform are fully supported and users should follow Jenkins user documentation for defining their `jenkinsfile` in a job or store it in a Source Control Management system.
====

The Pipeline build strategy allows developers to define a Jenkins pipeline for use by the Jenkins pipeline plugin. The build can be started, monitored, and managed by OpenShift Container Platform in the same way as any other build type.

Pipeline workflows are defined in a `jenkinsfile`, either embedded directly in the build configuration, or supplied in a Git repository and referenced by the build configuration.

//The first time a project defines a build configuration using a Pipeline
//strategy, OpenShift Container Platform instantiates a Jenkins server to execute the
//pipeline. Subsequent Pipeline build configurations in the project share this
//Jenkins server.

//[role="_additional-resources"]
//.Additional resources

//* Pipeline build configurations require a Jenkins server to manage the
//pipeline execution.
