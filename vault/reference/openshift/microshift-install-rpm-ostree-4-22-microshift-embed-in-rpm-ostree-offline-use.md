---
title: "Embedding in a {op-system-ostree} image for offline use"
type: reference
domain: openshift
slug: microshift-install-rpm-ostree-4-22-microshift-embed-in-rpm-ostree-offline-use
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree-offline-use
version: 4.22
family: microshift_install_rpm_ostree
documentKind: "Documentation"
---

# Embedding in a {op-system-ostree} image for offline use

[id="microshift-embed-in-rpm-ostree-for-offline-use"]
= Embedding in a {op-system-ostree} image for offline use

[role="_abstract"]
You can embed {microshift-short} in a container by using {op-system-base-full} for fully offline deployments.

// Module included in the following assemblies:
//
// microshift_running_applications/embed-microshift-offline-deploy.adoc
// microshift_install_rpm_ostree/microshift-embed-rpm-ostree-offline-use.adoc

[id="microshift-about-offline-deployment-rhel-edge_{context}"]
= About offline deployments with {op-system-ostree}

[role="_abstract"]
Embedding {microshift-short} containers in an `rpm-ostree` commit means that you can run a node in disconnected or offline environments.

You can embed OpenShift Container Platform containers in a {op-system-ostree-first} image so that container engines do not need to pull images over a network from a container registry. Workloads can start immediately without network connectivity.

// Module included in the following assemblies:
//
// microshift_running_applications/embed-microshift-offline-deploy.adoc
// microshift_install_rpm_ostree/microshift-embed-rpm-ostree-offline-use.adoc

[id="microshift-embed-microshift-image-offline-deployment_{context}"]
= Embedding {microshift-short} containers for offline deployments

[role="_abstract"]
You can use image builder to create {op-system-ostree} images with embedded {microshift-short} container images. To embed container images, you must add the image references to your image builder blueprint file.

.Prerequisites

* You have root-user access to your build host.
* Your build host meets the image builder system requirements.
* You installed and set up image builder and the `composer-cli` tool.
* You created a {op-system-ostree} image blueprint.
* You installed jq.

.Procedure

. Get the exact list of container image references used by the {microshift-short} version you are deploying. You can either install the `microshift-release-info` RPM package by following step 2 or download and unpack the RPM by following step 3.

. To install the `microshift-release-info` RPM package:

.. Install the `microshift-release-info` RPM package by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo dnf install -y microshift-release-info-_<release_version>_
----
+
Replace `_<release_version>_` with the numerical value of the release you are deploying, using the entire version number, such as `4.22.0`.

.. List the contents of the `/usr/share/microshift/release` directory to verify the presence of the release information files by running the following command:
+
[source,terminal]
----
$ sudo ls /usr/share/microshift/release
----
+
.Example output
[source,terminal]
----
release-x86_64.json
release-aarch64.json
----
+
If you installed the `microshift-release-info` RPM, proceed to step 4.

. If you did not complete step 2, download and unpack the `microshift-release-info` RPM without installing it:

.. Download the RPM package by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo dnf download microshift-release-info-_<release_version>_
----
+
Replace `_<release_version>_` with the numerical value of the release you are deploying, using the entire version number, such as `4.22.0`.
+
.Example RPM output
[source,terminal,subs="+quotes"]
----
microshift-release-info-4.22.0.-202605191402.p0.g4f61957.assembly.rc.4.el9.noarch.rpm
----

.. Unpack the RPM package without installing it by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ rpm2cpio _<my_microshift_release_info>_ | cpio -idmv
./usr/share/microshift/release/release-aarch64.json
./usr/share/microshift/release/release-x86_64.json
----
+
Replace `_<my_microshift_release_info>_` with the name of the RPM package from the previous step.

. Define the location of your JSON file, which contains the container reference information, by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ RELEASE_FILE=_</path/to/your/release-$(uname -m).json>_
----
+
Replace `_</path/to/your/release-$(uname -m).json>_` with the full path to your JSON file. Be sure to use the file needed for your architecture.

. Define the location of your TOML file, which contains instructions for building the image, by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ BLUEPRINT_FILE=_</path/to/your/blueprint.toml>_
----
+
Replace `_</path/to/your/blueprint.toml>_` with the full path to your TOML file.

. Generate and then embed the container image references in your blueprint TOML file by running the following command:
+
[source,terminal]
----
$  jq -r '.images | .[] | ("[[containers]]\nsource = \"" + . + "\"\n")' "${RELEASE_FILE}" >> "${BLUEPRINT_FILE}"
----
+
.Example resulting TOML fragment showing container references
[source,terminal]
----
[[containers]]
source = "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:82cfef91557f9a70cff5a90accba45841a37524e9b93f98a97b20f6b2b69e5db"

[[containers]]
source = "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:82cfef91557f9a70cff5a90accba45841a37524e9b93f98a97b20f6b2b69e5db"
----

. You can manually embed any container image by adding it to an image builder blueprint file using the following example:
+
.Example section for manually embedding container image to a blueprint
[source,text,subs="+quotes"]
----
[[containers]]
source = "_<my_image_pullspec_with_tag_or_digest>_"
----
+
Replace `_<my_image_pullspec_with_tag_or_digest>_` with the exact reference to a container image used by the {microshift-short} version you are deploying.

// Module included in the following assemblies:
//
// microshift_running_applications/embed-microshift-offline-deploy.adoc

[id="microshift-embed-registry-auth-image-building_{context}"]
= Adding registry authentication to prepare for image building

[role="_abstract"]
After you have updated the blueprint, you must add authentication for the container registries to build the image with embedded {microshift-short} containers. To do this, update one of the systemd service files that are part of the image builder configuration.

.Prerequisites

* You have root-user access to your build host.
* Your build host meets the image builder system requirements.
* You have installed and set up image builder and the `composer-cli` tool.

.Procedure

. Create an `/etc/osbuild-worker/osbuild-worker.toml` directory and configuration file if they do not exist.

. Add a pull secret for authenticating to the registry by setting the `auth_file_path` in the `[containers]` section of the `/etc/osbuild-worker/osbuild-worker.toml` configuration file:
+
[source,terminal]
----
[containers]
auth_file_path = "/etc/osbuild-worker/pull-secret.json"
----

. Restart the host to apply configuration changes.

// Module included in the following assemblies:
//
// microshift_running_applications/embed-microshift-offline-deploy.adoc

[id="microshift-embed-microshift-build-image-offline-deployment_{context}"]
= Build and use the rpm-ostree image for offline deployments

[role="_abstract"]
You can use image builder to create `rpm-ostree` system images with embedded {microshift-short} container images.

To embed container images, you must add the image references to your image builder blueprint. You can create the commit and ISO as needed for your use case.

Add the prerequisites listed here to the ones that are included in the procedures that follow.

[id="microshift-embed-microshift-build-image-offline-deployment-prereqs_{context}"]
== Additional prerequisites for offline deployments

* You have created and updated a {op-system-ostree} image blueprint for offline use. The following procedures use the example of a blueprint created with container images. You must use the updated blueprint you created in the "Embedding MicroShift containers for offline deployments" procedure.
* You have updated the `/etc/osbuild-worker/osbuild-worker.toml` configuration file for offline use.

[IMPORTANT]
====
Replace `minimal-microshift.toml` in the following procedures with the name of the TOML you updated for offline use, <my_blueprint_name>.
====

// Module included in the following assemblies:
//
// * microshift_install_rpm_ostree/microshift-embed-into-rpm-ostree.adoc
// * microshift_install_rpm/microshift-update-rpms-ostree.adoc

[id="adding-microshift-service-to-blueprint_{context}"]
= Adding the {microshift-short} service to a blueprint

[role="_abstract"]
Adding the {microshift-short} RPM package to an image builder blueprint enables the build of a {op-system-ostree} image with {microshift-short} embedded.

.Procedure

. Use the blueprint installed in the `/usr/share/microshift/blueprint` directory that is specific to your platform architecture. See the following example snippet for an explanation of the blueprint sections:
+
.Generated image builder blueprint example snippet
[source,text,subs="attributes+"]
----
name = "microshift_blueprint"
description = "MicroShift {ocp-version}.1 on x86_64 platform"
version = "0.0.1"
modules = []
groups = []

[[packages]]
name = "microshift"
version = "{ocp-version}.1"
...
...

[customizations.services]
enabled = ["microshift"]

[customizations.firewall]
ports = ["ssh"]
...
...

[[containers]]
source = "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:f41e79c17e8b41f1b0a5a32c3e2dd7cd15b8274554d3f1ba12b2598a347475f4"

[[containers]]
source = "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:dbc65f1fba7d92b36cf7514cd130fe83a9bd211005ddb23a8dc479e0eea645fd"
...
…
EOF
----
* `\[[packages]] name = "microshift"`: references for all non-optional {microshift-short} RPM packages using the same version compatible with the `microshift-release-info` RPM.
* `[customizations.services] enabled = ["microshift"]`: references for automatically enabling {microshift-short} on system startup and applying default networking settings.
* `\[[containers]] source = "quay.io/openshift-release-dev/...`: references for all non-optional {microshift-short} container images necessary for an offline deployment. The SHA depends on the release you are using.

. Add the blueprint to the image builder by running the following command:
+
[source,terminal]
----
$ sudo composer-cli blueprints push microshift_blueprint.toml
----

.Verification

. Verify the image builder configuration listing only {microshift-short} packages by running the following command:
+
[source,terminal]
----
$ sudo composer-cli blueprints depsolve microshift_blueprint | grep microshift
----
+
.Example output
[source,terminal,subs="+attributes"]
----
blueprint: microshift_blueprint v0.0.1
    microshift-release-info-{ocp-version}.1-202511250827.p0.g4105d3b.assembly.{ocp-version}.1.el9.noarch
    microshift-{ocp-version}.1-202511250827.p0.g4105d3b.assembly.{ocp-version}.1.el9.x86_64
----

. Optional: Verify the image builder configuration that lists all of the components to be installed by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo composer-cli blueprints depsolve microshift_blueprint
----

// Module included in the following assemblies:
//
// * microshift/microshift-embed-into-rpm-ostree.adoc
// * microshift/microshift-update-rpms-ostree.adoc

[id="microshift-creating-ostree-iso_{context}"]
= Creating the {op-system-ostree} image with image builder

[role="_abstract"]
The {op-system-ostree} Installer image pulls the commit from the running container and creates an installable boot ISO with a Kickstart file configured to use the embedded `rpm-ostree` commit.

.Prerequisites

* Your build host meets the image builder system requirements.
* You installed and set up image builder and the `composer-cli` tool.
* You root-user access to your build host.
* You installed the `podman` tool.

.Procedure

. Start an `ostree` container image build by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ BUILDID=$(sudo composer-cli compose start-ostree --ref "rhel/{op-system-version-major}/$(uname -m)/edge" __<microshift_blueprint>__ edge-container | awk '/^Compose/ {print $2}')
----
Replace `_<microshift_blueprint>_` with the name of your blueprint.
+
This command also returns the identification (ID) of the build for monitoring.

. You can check the status of the build periodically by running the following command:
+
[source,terminal]
----
$ sudo composer-cli compose status
----
+
.Example output of a running build
[source,terminal]
----
ID                                     Status     Time                     Blueprint                 Version   Type               Size
cc3377ec-4643-4483-b0e7-6b0ad0ae6332   RUNNING    Wed Jun 7 12:26:23 2023  microshift_blueprint      0.0.1     edge-container
----
+
.Example output of a completed build
[source,terminal]
----
ID                                     Status     Time                      Blueprint              Version   Type               Size
cc3377ec-4643-4483-b0e7-6b0ad0ae6332   FINISHED   Wed Jun 7 12:32:37 2023   microshift_blueprint   0.0.1     edge-container
----
+
[NOTE]
====
You can use the `watch` command to monitor your build if you are familiar with how to start and stop it.
====

. Download the container image using the ID and get the image ready for use by running the following command:
+
[source,terminal]
----
$ sudo composer-cli compose image ${BUILDID}
----

. Change the ownership of the downloaded container image to the current user by running the following command:
+
[source,terminal]
----
$ sudo chown $(whoami). ${BUILDID}-container.tar
----

. Add read permissions for the current user to the image by running the following command:
+
[source,terminal]
----
$ sudo chmod a+r ${BUILDID}-container.tar
----

. Bootstrap a server on port 8085 for the `ostree` container image to be consumed by the ISO build by completing the following steps:

.. Get the `IMAGEID` variable result by running the following command:
+
[source,terminal]
----
$ IMAGEID=$(cat < "./${BUILDID}-container.tar" | sudo podman load | grep -o -P '(?<=sha256[@:])[a-z0-9]*')
----

.. Use the `IMAGEID` variable result to run the Podman command step by running the following command:
+
[source,terminal]
----
$ sudo podman run -d --name=minimal-microshift-server -p 8085:8080 ${IMAGEID}
----
+
This command also returns the ID of the container saved in the `IMAGEID` variable for monitoring.

. Generate the installation program blueprint file by running the following command:
+
[source,text]
----
cat > microshift-installer.toml <<EOF
name = "microshift-installer"

description = ""
version = "0.0.0"
modules = []
groups = []
packages = []
EOF
----

[id="additional-resources_microshift-embed-microshift-offline-deployments"]
[role="_additional-resources"]
== Additional resources

* Pushing a container artifact directly to a container registry
* Container registry credentials
* Configuring network settings for fully disconnected hosts
* Using Operator Lifecycle Manager with {microshift-short}
* Creating custom catalogs using the oc-mirror plugin
