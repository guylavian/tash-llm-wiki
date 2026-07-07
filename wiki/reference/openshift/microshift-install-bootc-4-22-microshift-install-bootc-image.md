---
title: "Installing and publishing a bootc image to a registry"
type: reference
domain: openshift
slug: microshift-install-bootc-4-22-microshift-install-bootc-image
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_bootc/microshift-install-bootc-image
version: 4.22
family: microshift_install_bootc
documentKind: "Documentation"
---

# Installing and publishing a bootc image to a registry

[id="microshift-install-bootc-image"]
= Installing and publishing a bootc image to a registry

{microshift-short} is built and published as image mode containers. When installing a {op-system-base-full} bootable container image with {microshift-short}, use either a prebuilt bootable container image or build your own custom bootable container image.

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-about-rhel-image-mode

[id="microshift-install-rhel-image-mode-conc_{context}"]
= The image mode for {op-system-base} with {microshift-short} workflow

Before you use {op-system-image}, ensure that the following resources are available:

* A {op-system-base} {op-system-version} host with an active Red{nbsp}Hat subscription for building {microshift-short} bootc images.
* A remote registry for storing and accessing `rhel-bootc` images.
* An AArch64 or x86_64 system architecture.

The workflow for using {op-system-image} with {microshift-short} includes the following steps:

. Find and use a prebuilt {microshift-short} container image to install {op-system-base}.
. If the prebuilt {microshift-short} container image requires customization, build a custom {microshift-short} container image.
. Run the container image.

[IMPORTANT]
====
The `rpm-ostree` file system used by {op-system-ostree} is not supported in {op-system-image}. Do not use the `rpm-ostree` file system to modify deployments that use {op-system-image}.
====

[id="microshift-get-build-bootc-image_{context}"]
== Get or build your bootc image

Either get an existing bootc image or create one, then you can publish that image to a remote registry for use.

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-install-rhel-bootc-image.adoc

[id="microshift-install-bootc-get-published-image_{context}"]
= Getting the published bootc image for {microshift-short}

You can use the {microshift-short} container images to install {op-system-image}.

.Prerequisites

* You have an x86_64 or AArch64 platform.

* You have access to the `registry.redhat.io` registry.

.Procedure

. Navigate to the Red{nbsp}Hat Ecosystem Catalog.

. Search for the {microshift-short} container image by using the `microshift-bootc` keyword.

. Open the container image page of the {microshift-short} container image.

. Select the `Get this image` tab to view instructions for downloading the image.

. Get access to the latest image on x86_64 and AArch64 platforms by logging into the registry using the following command:
+
[source,terminal]
----
$ sudo podman login registry.redhat.io
----

. Download the bootc image by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ podman pull registry.redhat.io/openshift4/microshift-bootc-rhel{op-system-version-major}:v
----

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-install-bootc-image.adoc

[id="microshift-install-bootc-build-image_{context}"]
= Building the bootc image

Build your {op-system-base-full} that contains {microshift-short} as a bootable container image by using a Containerfile.

.Prerequisites

* A {op-system-base} {op-system-version} host with an active Red{nbsp}Hat subscription for building {microshift-short} bootc images and running containers.
* You logged into the {op-system-base} {op-system-version} host by using the user credentials that have `sudo` permissions.
* The `rhocp` and `fast-datapath` repositories are accessible in the host subscription. The repositories do not necessarily need to be enabled on the host.
* You have a remote registry such as {quay} for storing and accessing bootc images.
* You used the `dnf install -y container-tools` command to install the `container-tools` meta-package on the host. The meta-package contains all container tools, such as Podman, Buildah, and Skopeo for additional support and troubleshooting. These tools are required for obtaining assistance from Red{nbsp}Hat Support when you are building and installing the image.

.Procedure

. Create a Containerfile that includes the following instructions:
+
.Example Containerfile for {op-system-base} image mode
[source,text,subs="attributes+"]
----
FROM registry.redhat.io/rhel{op-system-version-major}/rhel-bootc:{op-system-version}

ARG USHIFT_VER=
RUN dnf config-manager \
        --set-enabled rhocp-${USHIFT_VER}-for-rhel-{op-system-version-major}-$(uname -m)-rpms \
        --set-enabled fast-datapath-for-rhel-{op-system-version-major}-$(uname -m)-rpms
RUN dnf install -y firewalld microshift && \
    systemctl enable microshift && \
    dnf clean all

# Create a default 'redhat' user with the specified password.
# Add it to the 'wheel' group to allow for running sudo commands.
ARG USER_PASSWD
RUN if [ -z "${USER_PASSWD}" ] ; then \
        echo USER_PASSWD is a mandatory build argument && exit 1 ; \
    fi
RUN useradd -m -d /var/home/redhat -G wheel redhat && \
    echo "redhat:${USER_PASSWD}" | chpasswd

# Mandatory firewall configuration
RUN firewall-offline-cmd --zone=public --add-port=22/tcp && \
    firewall-offline-cmd --zone=trusted --add-source=10.42.0.0/16 && \
    firewall-offline-cmd --zone=trusted --add-source=169.254.169.1

# Create a systemd unit to recursively make the root filesystem subtree
# shared as required by OVN images
RUN cat > /etc/systemd/system/microshift-make-rshared.service <<'EOF'
[Unit]
Description=Make root filesystem shared
Before=microshift.service
ConditionVirtualization=container
[Service]
Type=oneshot
ExecStart=/usr/bin/mount --make-rshared /
[Install]
WantedBy=multi-user.target
EOF
RUN systemctl enable microshift-make-rshared.service
----
[IMPORTANT]
====
Podman uses the host subscription information and repositories inside the container when building the container image. If the `rhocp` and `fast-datapath` repositories are not available on the host, the build fails.
====

. Set the `PULL_SECRET` environment variable:
+
[source,terminal]
----
$ PULL_SECRET=~/.pull-secret.json
----

. Configure the `USER_PASSWD` environment variable:
+
[source,terminal,subs="+quotes"]
----
$ USER_PASSWD=_<redhat_user_password>_ <1>
----
<1> Replace _<redhat_user_password>_ with your password.

. Configure the `IMAGE_NAME` environment variable:
+
[source,terminal,subs="attributes+"]
----
$ IMAGE_NAME=microshift--bootc
----

. Create a local bootc image by running the following image build command:
+
[source,terminal,subs="+quotes"]
----
$ sudo podman build --authfile "${PULL_SECRET}" -t "${IMAGE_NAME}" \
    --build-arg USER_PASSWD="${USER_PASSWD}" \
    -f Containerfile
----
+
[IMPORTANT]
====
How secrets are used during the image build:

* The podman `--authfile` argument is required to pull the base `rhel-bootc:{op-system-version}` image from the `registry.redhat.io` registry.
* The build `USER_PASSWD` argument is used to set a password for the `redhat` user.
====

.Verification

. Verify that the local {microshift-short} bootc image was created by running the following command:
+
[source,terminal]
----
$ sudo podman images "${IMAGE_NAME}"
----
+
.Example output
[source,text,subs="attributes+"]
----
REPOSITORY                       TAG         IMAGE ID      CREATED        SIZE
localhost/microshift--bootc  latest      193425283c00  2 minutes ago  2.31 GB
----

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-install-rhel-bootc-image.adoc

[id="microshift-bootc-publish-image_{context}"]
= Publishing the bootc image to the remote registry

Publish your bootc image to the remote registry so that the image can be used for running the container on another host, or for when you want to install a new operating system with the bootc image layer.

.Prerequisites

* You are logged in to the {op-system-base} {op-system-version} host where the image was built using the user credentials that have `sudo` permissions.
* You have a remote registry such as {quay} for storing and accessing bootc images.
* You created the Containerfile and built the image.

.Procedure

. Set the `REGISTRY_URL` variable for the image by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ REGISTRY_URL=_<quay.io>_ # <1>
----
<1> Replace _<quay.io>_ with the URL for your image registry.

. Log in to your remote registry by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo podman login "${REGISTRY_URL}"
----

. Set the `IMAGE_NAME` variable for the image by running the following command:
+
[source,terminal,subs="attributes+,quotes"]
----
$ IMAGE_NAME=_<microshift--bootc>_ # <1>
----
<1> Replace _<microshift--bootc>_ with the name of the image you want to publish.

. Set the `REGISTRY_IMG` variable for the image by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ REGISTRY_IMG=_<myorg/mypath>_/"${IMAGE_NAME}" # <1>
----
<1> Replace _<myorg/mypath>_ with your remote registry organization name and path.

. Publish the image by running the following command:
+
[source,terminal]
----
$ sudo podman push localhost/"${IMAGE_NAME}" "${REGISTRY_URL}/${REGISTRY_IMG}"
----

.Verification

. Run the container using the image you pushed to your registry as described in the "Running the {microshift-short} bootc container" section.
