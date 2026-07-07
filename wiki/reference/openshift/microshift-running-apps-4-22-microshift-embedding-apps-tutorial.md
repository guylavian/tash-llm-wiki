---
title: "Embedding {microshift-short} applications tutorial"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-embedding-apps-tutorial
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-embedding-apps-tutorial
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Embedding {microshift-short} applications tutorial

[id="microshift-embedding-apps-tutorial"]
= Embedding {microshift-short} applications tutorial

[role="_abstract"]
The following tutorial gives a detailed example of how to embed applications in a {op-system-ostree} image for use in a {microshift-short} node in various environments.

// Module included in the following assemblies:
//
// microshift_running_applications/embedding-apps-tutorial.adoc

[id="microshift-embed-app-rpms-tutorial_{context}"]
= Embed application RPMs tutorial

[role="_abstract"]
The following tutorial reviews the {microshift-short} installation steps and adds a description of the workflow for embedding applications. If you are already familiar with `rpm-ostree` systems such as {op-system-ostree-first} and {microshift-short}, you can go straight to the procedures.

[id="microshift-installation-workflow-review_{context}"]
== Installation workflow review
Embedding applications requires a similar workflow to embedding {microshift-short} into a {op-system-ostree} image.

* The following image shows how system artifacts such as RPMs, containers, and files are added to a blueprint and used by the image composer to create an ostree commit.
* The ostree commit then can follow either the ISO path or the repository path to edge devices.
* The ISO path can be used for disconnected environments, while the repository path is often used in places were the network is usually connected.

.Embedding {microshift-short} workflow
image:468_RHbM_install_workflow_1023_1.png[title="Embedding MicroShift in a RHEL for Edge image workflow."]

Reviewing these steps can help you understand the steps needed to embed an application:

. To embed {microshift-short} on {op-system-ostree}, you added the {microshift-short} repositories to image builder.

. You created a blueprint that declared all the RPMs, container images, files and customizations you needed, including the addition of {microshift-short}.

. You added the blueprint to image builder and ran a build with the image builder CLI tool (`composer-cli`). This step created `rpm-ostree` commits, which were used to create the container image. This image contained {op-system-ostree}.

. You added the installer blueprint to image builder to create an `rpm-ostree` image (ISO) to boot from. This build contained both {op-system-ostree} and {microshift-short}.

. You downloaded the ISO with {microshift-short} embedded, prepared it for use, provisioned it, then installed it onto your edge devices.

[id="microshift-embed-app-rpms-workflow_{context}"]
== Embed application RPMs workflow

After you have set up a build host that meets the image builder requirements, you can add your application in the form of a directory of manifests to the image. After those steps, the simplest way to embed your application or workload into a new ISO is to create your own RPMs that include the manifests. Your application RPMs contain all of the configuration files describing your deployment.

The following "Embedding applications workflow" image shows how Kubernetes application manifests and RPM spec files are combined in a single application RPM build. This build becomes the RPM artifact included in the workflow for embedding {microshift-short} in an ostree commit.

.Embedding applications workflow
image:468_RHbM_install_workflow_1023_2.png[title="Embedding applications workflow."]

The following procedures use the `rpmbuild` tool to create a specification file and local repository. The specification file defines how the package is built, moving your application manifests to the correct location inside the RPM package for {microshift-short} to pick them up. That RPM package is then embedded in the ISO.

// Module included in the following assemblies:
//
// microshift_running_applications/embedding-apps-tutorial.adoc

[id="microshift-preparing-to-make-app-rpms_{context}"]
= Preparing to make application RPMs

[role="_abstract"]
To build your own RPMs, choose a tool of your choice, such as the `rpmbuild` tool, and initialize the RPM build tree in your home directory. If your RPMs are accessible to image builder, you can use the method you prefer to build the application RPMs.

The following is an example procedure.

.Prerequisites

* You have set up a {op-system-ostree-first} {op-system-version} build host that meets the image builder system requirements.
* You have root access to the host.

.Procedure

. Install the `rpmbuild` tool and create the yum repository for it by running the following command:
+
[source,terminal]
----
$ sudo dnf install rpmdevtools rpmlint yum-utils createrepo
----

. Create the file tree you need to build RPM packages by running the following command:
+
[source,terminal]
----
$ rpmdev-setuptree
----

.Verification

* List the directories to confirm creation by running the following command:
+
[source,terminal]
----
$ ls ~/rpmbuild/
----
+
.Example output
[source,terminal]
----
BUILD RPMS SOURCES SPECS SRPMS
----

// Module included in the following assemblies:
//
// microshift_running_applications/embedding-apps-tutorial.adoc

[id="microshift-building-apps-rpms_{context}"]
= Building the RPM package for the application manifests

[role="_abstract"]
To build your own RPMs, you must create a spec file that adds the application manifests to the RPM package. If the application RPMs and other elements needed for image building are accessible to image builder, you can use the method that you prefer.

The following is an example procedure.

.Prerequisites
* You have set up a {op-system-ostree-first} {op-system-version} build host that meets the image builder system requirements.
* You have root access to the host.
* The file tree required to build RPM packages was created.

.Procedure

. In the `~/rpmbuild/SPECS` directory, create a file such as `_<application_workload_manifests.spec>_` using the following template:
+
.Example spec file
[source,terminal,subs="+quotes"]
----
Name: _<application_workload_manifests>_
Version: 0.0.1
Release: 1%{?dist}
Summary: Adds workload manifests to microshift
BuildArch: noarch
License: GPL
Source0: %{name}-%{version}.tar.gz
#Requires: microshift
%description
Adds workload manifests to microshift
%prep
%autosetup
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib/microshift/manifests
cp -pr ~/manifests $RPM_BUILD_ROOT/%{_prefix}/lib/microshift/
%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_prefix}/lib/microshift/manifests/**
%changelog
* _<DDD MM DD YYYY username@domain - V major.minor.patch>_
- _<your_change_log_comment>_
----
+
The `%install` section creates the target directory inside the RPM package, `/usr/lib/microshift/manifests/`
and copies the manifests from the source home directory, `~/manifests`.
+
[IMPORTANT]
====
All of the required YAML files must be in the source home directory `~/manifests`, including a `kustomize.yaml` file if you are using kustomize.
====

. Build your RPM package in the `~/rpmbuild/RPMS` directory by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ rpmbuild -bb ~/rpmbuild/SPECS/_<application_workload_manifests.spec>_
----

// Module included in the following assemblies:
//
// microshift_running_applications/embedding-apps-tutorial.adoc

[id="microshift-adding-app-rpms-to-blueprint_{context}"]
= Adding application RPMs to a blueprint

[role="_abstract"]
To add application RPMs to a blueprint on {microshift-short}, you must create a local repository that image builder can use to create the ISO. With this procedure, the required container images for your workload can be pulled over the network.

.Prerequisites

* You have root access to the host.
* Workload or application RPMs exist in the `~/rpmbuild/RPMS` directory.

.Procedure

. Create a local RPM repository by running the following command:
+
[source,terminal]
----
$ createrepo ~/rpmbuild/RPMS/
----

. Give image builder access to the RPM repository by running the following command:
+
[source,terminal]
----
$ sudo chmod a+rx ~
----
+

You must ensure that image builder has all of the necessary permissions to access all of the files needed for image building, or the build cannot proceed.

. Create the blueprint file, `repo-local-rpmbuild.toml` using the following template:
+
[source,toml,subs="+quotes"]
----
id = "local-rpm-build"
name = "RPMs build locally"
type = "yum-baseurl"
url = "file://_<path>_/rpmbuild/RPMS"
check_gpg = false
check_ssl = false
system = false
----
+

Replace `_<path>_` with the path to create a location that you choose. This path is used in later commands in this procedure to set up the repository and copy the RPMs.

. Add the repository as a source for image builder by running the following command:
+
[source,terminal]
----
$ sudo composer-cli sources add repo-local-rpmbuild.toml
----

. Add the RPM to your blueprint, by adding the following lines:
+
[source,toml,subs="+quotes"]
----
…
[[packages]]
name = "_<application_workload_manifests>_"
version = "*"
…
----
+
Replace `_<application_workload_manifests>_` with the name of your workload.

. Push the updated blueprint to image builder by running the following command:
+
[source,terminal]
----
$ sudo composer-cli blueprints push repo-local-rpmbuild.toml
----

. At this point, you can either run image builder to create the ISO, or embed the container images for offline use.

.. To create the ISO, start image builder by running the following command:
+
[source,terminal]
----
$ sudo composer-cli compose start-ostree repo-local-rpmbuild edge-commit
----
+
In this scenario, the container images are pulled over the network by the edge device during startup.

//additional resources for adding app rpms to blueprint
[role="_additional-resources"]
.Additional resources
* Composing a {op-system-ostree} image using the image builder CLI

* Network-based deployments workflow

//additional resources for assembly
[id="additional-resources_microshift-embedding-apps-tutorial_{context}"]
[role="_additional-resources"]
== Additional resources
* Embedding applications for offline use

* Embedding OpenShift Container Platform in an RPM-OSTree image

* Composing, installing, and managing {op-system-ostree} images

* Preparing for image building

* Meet Red Hat Device Edge with OpenShift Container Platform

* How to create a Linux RPM package

* Composing a {op-system-ostree} image using image builder command-line

* Image builder system requirements
