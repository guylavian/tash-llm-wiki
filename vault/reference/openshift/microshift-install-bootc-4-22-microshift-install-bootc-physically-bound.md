---
title: "Creating a fully self-contained bootc image"
type: reference
domain: openshift
slug: microshift-install-bootc-4-22-microshift-install-bootc-physically-bound
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_bootc/microshift-install-bootc-physically-bound
version: 4.22
family: microshift_install_bootc
documentKind: "Documentation"
---

# Creating a fully self-contained bootc image

[id="microshift-install-bootc-physically-bound"]
= Creating a fully self-contained bootc image

[role="_abstract"]
You can use physically-bound container images if you need your bootc image to include everything required to run workloads.

Edge-computing scenarios involving embedded systems on specialized devices, high security, or high hardware control scenarios are likely candidates.

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-install-bootc-physically-bound.adoc

[id="microshift-install-bootc-physically-bound_{context}"]
= About physically bound bootc image building

[role="_abstract"]
When a bootc image is fully self-contained, everything you need to run workloads is embedded with the bootc image, including {microshift-short} and application container images. The underlying mechanism is to pre-pull physically-bound images during image build and then make them available at runtime.

Because embedded images might change with each system update, you cannot pull the images directly to the default container storage. Additional image stores do not work in this case because of current implementation limits. These limits do not allow bootc image updates for those container images.

The manifest, layer tarballs, and signatures are exported as individual files into the directory. The `dir` transport type preserves the digest of the image, which is crucial for the original digest to reference the image.

Technical details to understand include the following items:

* Each image goes into the same top-level directory, but a separate subdirectory.
* Subdirectories are named after the image reference string `SHA`.
* An image list file maps image references to their name `SHA`.
* You must install the `microshift-release-info` RPM to get the image references required by {microshift-short}.
* You must have image references for your workloads. Apply the same methods to workload image references that you use for {microshift-short} image references.
* When you build the container, you must install the `microshift-release-info` RPM. The `release-x86_64.json` and `release-aarch64.json` files from this RPM reside in the `/usr/share/microshift/release/` directory. These files contain image references required by {microshift-short}.

[IMPORTANT]
====
You must keep track of the name of the image. A tag, digest, or a mix of both can reference images. Choosing the best way to reference the images you need can impact the quality and robustness of workloads.
====

// Module included in the following assemblies:
//
// microshift_install_bootc/microshift-install-bootc-physically-bound.adoc

[id="microshift-embed-cont-images-bootc-image_{context}"]
= Embedding container images into a bootc image

[role="_abstract"]
You embed container images by adding instructions to an existing Containerfile to copy the images you want and list them in a file to keep track of the copied image names.

Then, you must copy images locally from the `/usr/lib/containers/storage` directory to the local container storage.

[IMPORTANT]
====
You cannot store images in the default or additional container storage directory when you build bootc images. For example, if you update the additional container store setting in `/etc/containers/storage.conf` to point to the `/usr/lib/containers/storage` directory, bootc image updates fail.
====

.Prerequisites

* You have root access to the host.
* You installed Podman.
* You installed skopeo.
* You have workload image references.
* You have a Containerfile for building {microshift-short} images.

.Procedure

. Add the pull secret to the container build procedure to ensure that images can be pulled by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ podman build --secret id=pullsecret,src=/_<path/to/pull/secret>_.json
----
+
Specify the path to your pull secret in _<path/to/pull/secret>_.

. Add the instructions to physically embed the image at build time by adding the following to your Containerfile:
+
[source,text]
----
ENV IMAGE_STORAGE_DIR=/usr/lib/containers/storage
ENV IMAGE_LIST_FILE=${IMAGE_STORAGE_DIR}/image-list.txt

RUN dnf install -y microshift-release-info
RUN --mount=type=secret,id=pullsecret,dst=/run/secrets/pull-secret.json \
    images="$(jq -r ".images[]" /usr/share/microshift/release/release-"$(uname -m)".json)" ; \
    mkdir -p "${IMAGE_STORAGE_DIR}" ; \
    for img in ${images} ; do \
        sha="$(echo "${img}" | sha256sum | awk '{print $1}')" ; \
        skopeo copy --all --preserve-digests \
            --authfile /run/secrets/pull-secret.json \
            "docker://${img}" "dir:$IMAGE_STORAGE_DIR/${sha}" ; \
        echo "${img},${sha}" >> "${IMAGE_LIST_FILE}" ; \
    done
----
When run, the Containerfile extracts the list of {microshift-short} container image dependencies from the `microshift-release-info` RPM and pulls them into a custom `/usr/lib/containers/storage` directory. The resulting image list file is saved at `/usr/lib/containers/storage/image-list.txt`.

. Next, you must copy container images from the custom directory to the main container storage directory so that they are available to {microshift-short}. Add a script and a systemd service to your Containerfile to copy the embedded images from the `/usr/lib/containers/storage` directory to the local container storage. Copying happens at runtime before each {microshift-short} start. Use the following example:
+
[source,text]
----
RUN cat > /usr/bin/microshift-copy-images <<EOF
#!/bin/bash
set -eux -o pipefail
while IFS="," read -r img sha ; do
    skopeo copy --preserve-digests \
        "dir:${IMAGE_STORAGE_DIR}/\${sha}" \
        "containers-storage:\${img}"
done < "${IMAGE_LIST_FILE}"
EOF

RUN chmod 755 /usr/bin/microshift-copy-images && \
    mkdir -p /usr/lib/systemd/system/microshift.service.d

RUN cat > /usr/lib/systemd/system/microshift.service.d/microshift-copy-images.conf <<EOF
[Service]
ExecStartPre=/usr/bin/microshift-copy-images
EOF
----

.Next steps
. Build the image.
. Test and deploy per your use case.

[id="_additional-resources_microshift-install-bootc-physically-bound_{context}"]
== Additional resources

* Building the bootc image
