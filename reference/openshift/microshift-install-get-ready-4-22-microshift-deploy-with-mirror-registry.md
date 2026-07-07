---
title: "Mirroring container images for disconnected installations"
type: reference
domain: openshift
slug: microshift-install-get-ready-4-22-microshift-deploy-with-mirror-registry
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_get_ready/microshift-deploy-with-mirror-registry
version: 4.22
family: microshift_install_get_ready
documentKind: "Documentation"
---

# Mirroring container images for disconnected installations

[id="microshift-deploy-with-mirror-registry"]
= Mirroring container images for disconnected installations

[role=_abstract]
You can use a custom container registry when you deploy {microshift-short} in a disconnected network. Running your node in a restricted network without direct internet connectivity is possible by installing the node from a mirrored set of container images in a private registry.

// Module included in the following assemblies:
//
// * microshift/microshift_install_get_ready/microshift-deploy-with-mirror-registry.adoc

[id="microshift-mirror-container-images_{context}"]
= Mirror container images into an existing registry

[role="_abstract"]
Using a custom air-gapped container registry, or mirror, is necessary with certain user environments and workload requirements. Mirroring allows for the transfer of container images and updates to air-gapped environments where they can be installed on a {microshift-short} instance.

To create an air-gapped mirror registry for {microshift-short} containers, you must complete the following steps:

* Get the container image list to be mirrored.
* Configure the mirroring prerequisites, including secure signatures management.
* Download images on a host with internet access.
* Copy the downloaded image directory to an air-gapped site.
* Upload images to a mirror registry in an air-gapped site.
* Configure your {microshift-short} hosts to use the mirror registry.

// Module included in the following assemblies:
//
// * microshift/microshift_install_get_ready/microshift-deploy-with-mirror-registry.adoc

[id="microshift-get-mirror-reg-container-image-list_{context}"]
= Getting the mirror registry container image list

[role="_abstract"]
To use a mirror registry, you must know which container image references are used by a specific version of {microshift-short}. These references are provided in the `release-<arch>.json` files that are part of the `microshift-release-info` RPM package.

[NOTE]
====
To mirror the Operator Lifecycle Manager (OLM) in disconnected environments, add the references provided in the `release-olm-$ARCH.json` that is included in the `microshift-olm` RPM and follow the same procedure. Use the `oc-mirror` CLI plugin for mirroring Operator catalogs and Operators.
====

.Prerequisites

* You have installed jq.

.Procedure

. Access the list of container image references by using one of the following methods:

** If the package is installed on the {microshift-short} host, get the location of the files by running the following command:
+
[source,terminal]
----
$ rpm -ql microshift-release-info
----
+
.Example output
[source,text]
----
/usr/share/microshift/release/release-x86_64.json
----

** If the package is not installed on a {microshift-short} host, download and unpack the RPM package without installing it by running the following command:
+
[source,terminal]
----
$ rpm2cpio microshift-release-info*.noarch.rpm | cpio -idmv
----
+
.Example output
[source,text]
----
/usr/share/microshift/release/release-x86_64.json
----

. Extract the list of container images into the `microshift-container-refs.txt` file by running the following commands:
+
[source,terminal]
----
$ RELEASE_FILE=/usr/share/microshift/release/release-$(uname -m).json
----
+
[source,terminal]
----
$ jq -r '.images | .[]' ${RELEASE_FILE} > microshift-container-refs.txt
----
+
[NOTE]
====
After the `microshift-container-refs.txt` file is created with the {microshift-short} container image list, you can append the file with other user-specific image references before running the mirroring procedure.
====

// Module included in the following assemblies:
//
// * microshift/microshift_install_get_ready/microshift-deploy-with-mirror-registry.adoc

[id="microshift-configuring-mirroring-prereqs_{context}"]
= Configuring mirroring prerequisites

[role="_abstract"]
You must create a container image registry credentials file that allows the mirroring of images from your internet-connected mirror host to your air-gapped mirror. Follow the instructions in the "Configuring credentials that allow images to be mirrored" link provided in the "Additional resources" section. These instructions guide you to create a `~/.pull-secret-mirror.json` file on the mirror registry host that includes the user credentials for accessing the mirror.

[id="microshift-example-mirror-pull-secret-entry_{context}"]
== Example mirror registry pull secret entry

In this example, the following section is added to the pull secret file for the `microshift_quay:8443` mirror registry by using `microshift:microshift` as username and password.

.Example mirror registry section for pull secret file
[source,terminal]
----
"<microshift_quay:8443>": {
    "auth": "<microshift_auth>",
    "email": "<microshift_quay@example.com>"
},
----

* Replace the `<registry_host>:<port>` value `microshift_quay:8443` with the hostname and port of your mirror registry server.
* Replace the `_<microshift_auth>_` value with the user password.
* Replace the `_</microshift_quay@example.com>_` value with the user email.

// Module included in the following assemblies:
//
// * microshift/microshift_install_get_ready/microshift-deploy-with-mirror-registry.adoc

[id="microshift-downloading-container-images_{context}"]
= Downloading container images

[role="_abstract"]
After you have located the container list and completed the mirroring prerequisites, download the container images to a host with internet access.

.Prerequisites

* You logged into a host with access to the internet.
* The `.pull-secret-mirror.json` file and `microshift-containers` directory contents are available locally.

.Procedure

. Install the `skopeo` tool used for copying the container images by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y skopeo
----

. Set the environment variable that points to the pull secret file:
+
[source,terminal]
----
$ PULL_SECRET_FILE=~/.pull-secret-mirror.json
----

. Set the environment variable that points to the list of container images:
+
[source,terminal]
----
$ IMAGE_LIST_FILE=~/microshift-container-refs.txt
----

. Set the environment variable that points to the destination directory for storing the downloaded data:
+
[source,terminal]
----
$ IMAGE_LOCAL_DIR=~/microshift-containers
----

. Run the following script to download the container images to the `${IMAGE_LOCAL_DIR}` directory:
+
[source,terminal]
----
while read -r src_img ; do
   # Remove the source registry prefix
   dst_img=$(echo "${src_img}" | cut -d '/' -f 2-)

   # Run the image download command
   echo "Downloading '${src_img}' to '${IMAGE_LOCAL_DIR}'"
   mkdir -p "${IMAGE_LOCAL_DIR}/${dst_img}"
   skopeo copy --all --quiet \
      --preserve-digests \
      --authfile "${PULL_SECRET_FILE}" \
      docker://"${src_img}" dir://"${IMAGE_LOCAL_DIR}/${dst_img}"

done < "${IMAGE_LIST_FILE}"
----

// Module included in the following assemblies:
//
// * microshift/microshift_install_get_ready/microshift-deploy-with-mirror-registry.adoc

[id="microshift-uploading-container-images-to-mirror_{context}"]
= Uploading container images to a mirror registry

[role="_abstract"]
To use your container images at an air-gapped site, upload them to the mirror registry by using the following procedure.

.Prerequisites

* You logged into a host with access to `microshift-quay`.
* The `.pull-secret-mirror.json` file is available locally.
* The `microshift-containers` directory contents are available locally.

.Procedure

. Install the `skopeo` tool used for copying the container images by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y skopeo
----

. Set the environment variables pointing to the pull secret file:
+
[source,terminal]
----
$ IMAGE_PULL_FILE=~/.pull-secret-mirror.json
----

. Set the environment variables pointing to the local container image directory:
+
[source,terminal]
----
$ IMAGE_LOCAL_DIR=~/microshift-containers
----

. Set the environment variables pointing to the mirror registry URL for uploading the container images:
+
[source,terminal,subs="+quotes"]
----
$ TARGET_REGISTRY=_<registry_host>:<port>_
----

** Replace `_<registry_host>:<port>_` with the hostname and port of your mirror registry server.

. Run the following script to upload the container images to the `${TARGET_REGISTRY}` mirror registry:
+
[source,terminal]
----
pushd "${IMAGE_LOCAL_DIR}" >/dev/null
while read -r src_manifest ; do
  local src_img
  src_img=$(dirname "${src_manifest}")
  # Add the target registry prefix and remove SHA
  local -r dst_img="${TARGET_REGISTRY}/${src_img}"
  local -r dst_img_no_tag="${TARGET_REGISTRY}/${src_img%%[@:]*}"
  # Run the image upload
  echo "Uploading '${src_img}' to '${dst_img}'"
  skopeo copy --all --quiet \
     --preserve-digests \
     --authfile "${IMAGE_PULL_FILE}" \
     dir://"${IMAGE_LOCAL_DIR}/${src_img}" docker://"${dst_img}"
done < <(find . -type f -name manifest.json -printf '%P\n')
popd >/dev/null
----

// Module included in the following assemblies:
//
// * microshift/microshift_install_get_ready/microshift-deploy-with-mirror-registry.adoc

[id="microshift-configuring-hosts-for-mirror_{context}"]
= Configuring hosts for mirror registry access

[role="_abstract"]
To configure a {microshift-short} host to use a mirror registry, you must give the {microshift-short} host access to the registry by creating a configuration file that maps the Red Hat registry host names to the mirror.

.Prerequisites

* Your mirror host has access to the internet.
* The mirror host can access the mirror registry.
* You configured the mirror registry for use in your restricted network.
* You downloaded the pull secret and modified it to include authentication to your mirror repository.

.Procedure

. Log in to your {microshift-short} host.

. Enable the SSL certificate trust on any host accessing the mirror registry by completing the following steps:

.. Copy the `rootCA.pem` file from the mirror registry, for example, `<registry_path>/quay-rootCA`, to the {microshift-short} host at the `/etc/pki/ca-trust/source/anchors` directory.
.. Enable the certificate in the system-wide truststore configuration by running the following command:
+
[source,terminal]
----
$ sudo update-ca-trust
----

. Create the `/etc/containers/registries.conf.d/999-microshift-mirror.conf` configuration file that maps the Red Hat registry host names to the mirror registry:
+
.Example mirror configuration file
[source,terminal]
----
[[registry]]
    prefix = ""
    location = "<registry_host>:<port>"
    mirror-by-digest-only = true
    insecure = false

[[registry]]
    prefix = ""
    location = "quay.io"
    mirror-by-digest-only = true
[[registry.mirror]]
    location = "<registry_host>:<port>"
    insecure = false

[[registry]]
    prefix = ""
    location = "registry.redhat.io"
    mirror-by-digest-only = true
[[registry.mirror]]
    location = "<registry_host>:<port>"
    insecure = false

[[registry]]
    prefix = ""
    location = "registry.access.redhat.com"
    mirror-by-digest-only = true
[[registry.mirror]]
    location = "<registry_host>:<port>"
    insecure = false
----

** Replace `<registry_host>:<port>` with the hostname and port of your mirror registry server, for example, `<microshift-quay:8443>`.

. Enable the {microshift-short} service by running the following command:
+
[source,terminal]
----
$ sudo systemctl enable microshift
----

. Reboot the host by running the following command:
+
[source,terminal]
----
$ sudo reboot
----

[id="additional-resources_microshift-deploy-with-mirror-registry_{context}"]
[role="_additional-resources"]
== Additional resources

* Creating a mirror registry with mirror registry for Red Hat OpenShift

* Configuring credentials that allow images to be mirrored
