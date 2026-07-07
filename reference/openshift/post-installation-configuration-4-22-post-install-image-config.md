---
title: "Configuring image streams and image registries"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-post-install-image-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/post-install-image-config
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Configuring image streams and image registries

[id="post-install-image-config"]
= Configuring image streams and image registries

You can update the global pull secret for your cluster by either replacing the current pull secret or appending a new pull secret. The procedure is required when users use a separate registry to store images than the registry used during installation. For more information, see Using image pull secrets.

For information about images and configuring image streams or image registries, see the following documentation:

* Overview of images
* Image Registry Operator in OpenShift Container Platform
* Configuring image registry settings

[id="post-install-image-config-disconnected"]
== Configuring image streams for a disconnected cluster

After installing OpenShift Container Platform in a disconnected environment, configure the image streams for the Cluster Samples Operator and the `must-gather` image stream.

// Module included in the following assemblies:
//
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * openshift_images/configuring-samples-operator.adoc

[id="installation-images-samples-disconnected-mirroring-assist_{context}"]
= Cluster Samples Operator assistance for mirroring

[role="_abstract"]
During installation, OpenShift Container Platform creates a config map named `imagestreamtag-to-image` in the `openshift-cluster-samples-operator` namespace.

The `imagestreamtag-to-image` config map contains an entry, the populating image, for each image stream tag.

The format of the key for each entry in the data field in the config map is `<image_stream_name>_<image_stream_tag_name>`.

During a disconnected installation of OpenShift Container Platform, the status of the Cluster Samples Operator is set to `Removed`. If you choose to change it to `Managed`, it installs samples.

[NOTE]
====
The use of samples in a network-restricted or discontinued environment might require access to services external to your network. Some example services include: Github, Maven Central, npm, RubyGems, PyPi and others. There might be additional steps to take that allow the Cluster Samples Operators objects to reach the services they require.
====

Use the following principles to determine which images you need to mirror for your image streams to import:

* While the Cluster Samples Operator is set to `Removed`, you can create your mirrored registry, or determine which existing mirrored registry you want to use.
* Mirror the samples you want to the mirrored registry using the new config map as your guide.
* Add any of the image streams you did not mirror to the `skippedImagestreams` list of the Cluster Samples Operator configuration object.
* Set `samplesRegistry` of the Cluster Samples Operator configuration object to the mirrored registry.
* Then set the Cluster Samples Operator to `Managed` to install the image streams you have mirrored.

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * openshift_images/samples-operator-alt-registry.adoc

[id="installation-restricted-network-samples_{context}"]
= Using Cluster Samples Operator image streams with alternate or mirrored registries

[role="_abstract"]
You can use an alternate or mirror registry to host your images streams instead of using the Red{nbsp}Hat registry.

Most image streams in the `openshift` namespace managed by the Cluster Samples Operator point to images located in the Red{nbsp}Hat registry at registry.redhat.io.
Mirroring does not apply to these image streams.

[NOTE]
====
The `cli`, `installer`, `must-gather`, and `tests` image streams, while part of the install payload, are not managed by the Cluster Samples Operator. These are not addressed in this procedure.
====

[IMPORTANT]
====
The Cluster Samples Operator must be set to `Managed` in a disconnected environment. To install the image streams, you must have a mirrored registry.
====

.Prerequisites
* Access to the cluster as a user with the `cluster-admin` role.
* Access to the cluster as a user with the `dedicated-admin` role.
* Create a pull secret for your mirror registry.

.Procedure

. Access the images of a specific image stream to mirror, for example:
+
[source,terminal]
----
$ oc get is <imagestream> -n openshift -o json | jq .spec.tags[].from.name | grep registry.redhat.io
----
+
. Mirror images from registry.redhat.io associated with any image streams you need
in the restricted network environment into one of the defined mirrors, for example:
into your defined preferred registry, for example:
+
[source,terminal]
----
$ oc image mirror registry.redhat.io/rhscl/ruby-25-rhel7:latest ${MIRROR_ADDR}/rhscl/ruby-25-rhel7:latest
----

. Create the image configuration object for the cluster by running the following command:
+
[source,terminal]
----
$ oc create configmap registry-config --from-file=${MIRROR_ADDR_HOSTNAME}..5000=$path/ca.crt -n openshift-config
----

. Add the required trusted CAs for the mirror in the image configuration object:
+
[source,terminal]
----
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-config"}}}' --type=merge
----

. Update the `samplesRegistry` field in the Cluster Samples Operator configuration object to contain the `hostname` portion of the mirror location defined in the mirror configuration:
+
[source,terminal]
----
$ oc edit configs.samples.operator.openshift.io -n openshift-cluster-samples-operator
----
+
[IMPORTANT]
====
This step is required because the image stream import process does not use the mirror or search mechanism at this time.
====

. Add any image streams that are not mirrored into the `skippedImagestreams` field of the Cluster Samples Operator configuration object. Or if you do not want to support any of the sample image streams, set the Cluster Samples Operator to `Removed` in the Cluster Samples Operator configuration object.
+
[NOTE]
====
The Cluster Samples Operator issues alerts if image stream imports are failing but the Cluster Samples Operator is either periodically retrying or does not appear to be retrying them.
====
+
Many of the templates in the `openshift` namespace reference the image streams. You can use `Removed` to purge both the image streams and templates. This eliminates the possibility of attempts to use the templates if they are not functional because of any missing image streams.

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc

[id="installation-preparing-restricted-cluster-to-gather-support-data_{context}"]
= Preparing your cluster to gather support data

Clusters using a restricted network must import the default must-gather image to gather debugging data for Red Hat support. The must-gather image is not imported by default, and clusters on a restricted network do not have access to the internet to pull the latest image from a remote repository.

.Procedure

. If you have not added your mirror registry's trusted CA to your cluster's image configuration object as part of the Cluster Samples Operator configuration, perform the following steps:
.. Create the cluster's image configuration object:
+
[source,terminal]
----
$ oc create configmap registry-config --from-file=${MIRROR_ADDR_HOSTNAME}..5000=$path/ca.crt -n openshift-config
----

.. Add the required trusted CAs for the mirror in the cluster's image
configuration object:
+
[source,terminal]
----
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-config"}}}' --type=merge
----

. Import the default must-gather image from your installation payload:
+
[source,terminal]
----
$ oc import-image is/must-gather -n openshift
----

When running the `oc adm must-gather` command, use the `--image` flag and point to the payload image, as in the following example:
[source,terminal]
----
$ oc adm must-gather --image=$(oc adm release info --image-for must-gather)
----

// Module included in the following assemblies:
// * openshift_images/cluster-tasks.adoc

[id="images-cluster-sample-imagestream-import_{context}"]
= Configuring periodic importing of Cluster Sample Operator image stream tags

You can ensure that you always have access to the latest versions of the Cluster Sample Operator images by periodically importing the image stream tags when new versions become available.

.Procedure

. Fetch all the imagestreams in the `openshift` namespace by running the following command:
+
[source,terminal]
----
oc get imagestreams -n openshift
----

. Fetch the tags for every imagestream in the `openshift` namespace by running the following command:
+
[source,terminal]
----
$ oc get is <image-stream-name> -o jsonpath="{range .spec.tags[*]}{.name}{'\t'}{.from.name}{'\n'}{end}" -n openshift
----
+
For example:
+
[source,terminal]
----
$ oc get is ubi8-openjdk-17 -o jsonpath="{range .spec.tags[*]}{.name}{'\t'}{.from.name}{'\n'}{end}" -n openshift
----
+
.Example output
[source,terminal]
----
1.11	registry.access.redhat.com/ubi8/openjdk-17:1.11
1.12	registry.access.redhat.com/ubi8/openjdk-17:1.12
----

. Schedule periodic importing of images for each tag present in the image stream by running the following command:
+
[source,terminal]
----
$ oc tag <repository/image> <image-stream-name:tag> --scheduled -n openshift
----
+
For example:
+
[source,terminal]
----
$ oc tag registry.access.redhat.com/ubi8/openjdk-17:1.11 ubi8-openjdk-17:1.11 --scheduled -n openshift
----
+
[source,terminal]
----
$ oc tag registry.access.redhat.com/ubi8/openjdk-17:1.12 ubi8-openjdk-17:1.12 --scheduled -n openshift
----
+
[NOTE]
====
Using the `--scheduled` flag is recommended to periodically re-import an image when working with an external container image registry. The `--scheduled` flag helps to ensure that you receive the latest versions and security updates. Additionally, this setting allows the import process to automatically retry if a temporary error initially prevents the image from being imported.

By default, scheduled image imports occur every 15 minutes cluster-wide.
====

. Verify the scheduling status of the periodic import by running the following command:
+
[source,terminal]
----
oc get imagestream <image-stream-name> -o jsonpath="{range .spec.tags[*]}Tag: {.name}{'\t'}Scheduled: {.importPolicy.scheduled}{'\n'}{end}" -n openshift
----
+
For example:
+
[source,terminal]
----
oc get imagestream ubi8-openjdk-17 -o jsonpath="{range .spec.tags[*]}Tag: {.name}{'\t'}Scheduled: {.importPolicy.scheduled}{'\n'}{end}" -n openshift
----
+
.Example output
[source,terminal]
----
Tag: 1.11	Scheduled: true
Tag: 1.12	Scheduled: true
----
