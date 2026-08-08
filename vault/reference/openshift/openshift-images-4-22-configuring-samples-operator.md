---
title: "Configuring the Cluster Samples Operator"
type: reference
domain: openshift
slug: openshift-images-4-22-configuring-samples-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/openshift_images/configuring-samples-operator
version: 4.22
family: openshift_images
documentKind: "Documentation"
---

# Configuring the Cluster Samples Operator

[id="configuring-samples-operator"]
= Configuring the Cluster Samples Operator

[id="configuring-samples-operator"]
= Overview of the Cluster Samples Operator

[role="_abstract"]
You can configure the Cluster Samples Operator to manage the installation and updates of {op-system-base-full}-based OpenShift Container Platform image streams and templates in the `openshift` namespace.

[role="_abstract"]
The Cluster Samples Operator manages OpenShift Container Platform image streams and templates in the `openshift` namespace, providing you with ready-to-use application components.

// Module included in the following assemblies:
//
// * openshift_images/configuring_samples_operator.adoc

[id="samples-operator-overview_{context}"]
= Understanding the Cluster Samples Operator

[role="_abstract"]
During installation, the Operator creates the default configuration object for itself and then creates the sample image streams and templates, including quick start templates.

[NOTE]
====
To facilitate image stream imports from other registries that require credentials, a cluster administrator can create any additional secrets that contain the content of a Docker `config.json` file in the `openshift` namespace needed for image import.
====

The Cluster Samples Operator configuration is a cluster-wide resource. The deployment of the Operator is within the `openshift-cluster-samples-operator` namespace.

The image for the Cluster Samples Operator has image stream and template definitions for the associated OpenShift Container Platform release. When each sample is created or updated, the Cluster Samples Operator includes an annotation that denotes the version of OpenShift Container Platform. The Operator uses this annotation to ensure that each sample matches the release version. Samples outside of its inventory are ignored, as are skipped samples. Modifications to any samples that are managed by the Operator, where that version annotation is modified or deleted, are reverted automatically.

[NOTE]
====
The Jenkins images are part of the image payload from installation and are tagged into the image streams directly.
====

The Cluster Samples Operator configuration resource includes a finalizer which cleans up the following upon deletion:

* Operator managed image streams.
* Operator managed templates.
* Operator generated configuration resources.
* Cluster status resources.

Upon deletion of the samples resource, the Cluster Samples Operator recreates the resource by using the default configuration.

If the Cluster Samples Operator is removed during installation, you can use the Cluster Samples Operator with an alternate registry so that content can be imported. Then you can set the Cluster Samples Operator to `Managed` to get the samples. Use the following instructions:

* Using the Cluster Samples Operator with an alternate registry

For more information about configuring credentials, see the following Using image pull secrets

// Module included in the following assemblies:
//
// * openshift_images/configuring_samples_operator.adoc

[id="samples-operator-bootstrapped_{context}"]
= Cluster Samples Operator use of management state

[role="_abstract"]
The Cluster Samples Operator is bootstrapped as `Managed` by default or if global proxy is configured.

In the `Managed` state, the Cluster Samples Operator is actively managing its resources and keeping the component active to pull sample image streams and images from the registry and ensure that the requisite sample templates are installed.

Certain circumstances result in the Cluster Samples Operator bootstrapping itself as `Removed` including:

* If the Cluster Samples Operator cannot reach the registry after three minutes on initial startup after a clean installation.
* If the Cluster Samples Operator detects that it is on an IPv6 network.
// cannot configure the Samples Operator
* If the image controller configuration parameters prevent the creation of image streams by using the default image registry, or by using the image registry specified by `samplesRegistry` setting. For more information, see the following links:

** Image controller configuration parameters
** Cluster Samples Operator configuration parameters

[NOTE]
====
For OpenShift Container Platform, the default image registry is
`registry.redhat.io`.
`registry.access.redhat.com` or `quay.io`.
====

However, if the Cluster Samples Operator detects that it is on an IPv6 network and an OpenShift Container Platform global proxy is configured, then the IPv6 check supersedes all the checks. As a result, the Cluster Samples Operator bootstraps itself as `Removed`.
However, if the Cluster Samples Operator detects that it is on an IPv6 network and a OpenShift Container Platform global proxy is configured, then the IPv6 check supersedes all the checks. As a result, the Cluster Samples Operator bootstraps itself as `Removed`.

[IMPORTANT]
====
IPv6 installations are not currently supported by the registry. The Cluster Samples Operator pulls most of the sample image streams and images from the registry.
====

// Restricted network not supported ROSA/OSD
// Module included in the following assemblies:
//
// * openshift_images/configuring_samples_operator.adoc

[id="samples-operator-restricted-network-install-con_{context}"]
= Restricted network installation

[role="_abstract"]
The Cluster Samples Operator boostrapping itself as `Removed` when unable to access `registry.redhat.io` facilitates restricted network installations when the network restriction is already in place.

As a cluster administrator, you have more time to decide if samples are needed when the Operator is boostrapped `Removed`. This is because the Cluster Samples Operator does not submit alerts that sample image stream imports are failing when the management state is `Removed`. When the Cluster Samples Operator management state is `Managed`, and the Operator attempts to install sample image streams, failing-import alerts start two hours after initial installation.

// Module included in the following assemblies:
//
// * openshift_images/configuring_samples_operator.adoc

[id="samples-operator-restricted-nw-install-with-access_{context}"]
= Restricted network installation with initial network access

[role="_abstract"]
If a cluster that eventually runs on a restricted network is first installed while network access exists, the Cluster Samples Operator installs content from `registry.redhat.io`.

In this case, you can defer samples installation until you have decided which samples are needed by overriding the default configuration of `Managed` for a connected installation.

If you want the Cluster Samples Operator to bootstrap with the management state as `Removed` during an installation that has initial network access, override the Cluster Samples Operator default configuration by using the following instructions:

* Customizing nodes

To host samples in your restricted environment, use the following instructions:

* Using the Cluster Samples Operator with an alternate registry

You must also put the following additional YAML file in the `openshift` directory created by the `openshift-install create manifest` process:

.Example Cluster Samples Operator YAML file with `managementState: Removed`
[source,yaml]
----
apiVersion: samples.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  architectures:
  - x86_64
  managementState: Removed
----

// Module included in the following assemblies:
//
// * openshift_images/configuring_samples_operator.adoc

[id="samples-operator-retries_{context}"]
= Cluster Samples Operator tracking and error recovery of image stream imports

[role="_abstract"]
After creation or update of a samples image stream, the Cluster Samples Operator monitors the progress of each image stream tag's image import.

If an import fails, the Cluster Samples Operator retries the import through the image stream image import API at a rate of about every 15 minutes until either one of the following occurs:

* The import succeeds.
* The Cluster Samples Operator configuration is changed such that either the image stream is added to the `skippedImagestreams` list, or the management state is changed to `Removed`.

// Restricted network not supported ROSA/OSD
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

// cannot patch resource "configs" in API group "samples.operator.openshift.io"
// Module included in the following assemblies:
//
// * openshift_images/configuring_samples_operator.adoc

[id="samples-operator-configuration_{context}"]
= Cluster Samples Operator configuration parameters

[role="_abstract"]
The samples resource offers the following configuration fields:

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`managementState`
|`Managed`: The Cluster Samples Operator updates the samples as the configuration dictates.

`Unmanaged`: The Cluster Samples Operator ignores updates to its configuration resource object and any image streams or templates in the `openshift` namespace.

`Removed`: The Cluster Samples Operator removes the set of `Managed` image streams and templates in the `openshift` namespace. It ignores new samples created by the cluster administrator or any samples in the skipped lists. After the removals are complete, the Cluster Samples Operator works like it is in the `Unmanaged` state and ignores any watch events on the sample resources, image streams, or templates.

|`samplesRegistry`
|Allows you to specify which registry is accessed by image streams for their image content. `samplesRegistry` defaults to `registry.redhat.io` for OpenShift Container Platform.

[NOTE]
====
Creation or update of RHEL content does not commence if the secret for pull access is not in place when either `Samples Registry` is not explicitly set, leaving an empty string, or when it is set to registry.redhat.io. In both cases, image imports work off of registry.redhat.io, which requires credentials.

Creation or update of RHEL content is not gated by the existence of the pull secret if the `Samples Registry` is overridden to a value other than the empty string or registry.redhat.io.
====

|`architectures`
|Placeholder to choose an architecture type.

|`skippedImagestreams`
|Image streams that are in the Cluster Samples Operator's inventory but that the cluster administrator wants the Operator to ignore or not manage. You can add a list of image stream names to this parameter. For example, `["httpd","perl"]`.

|`skippedTemplates`
|Templates that are in the Cluster Samples Operator's inventory, but that the cluster administrator wants the Operator to ignore or not manage.

|===

Secret, image stream, and template watch events can come in before the initial samples resource object is created, the Cluster Samples Operator detects and re-queues the event.

[id="samples-operator-config-restrictions_{context}"]
== Configuration restrictions

When the Cluster Samples Operator starts supporting multiple architectures, you cannot change the architecture list while the Operator is in the `Managed` state.

To change the architectures values, a cluster administrator must:

* Mark the `Management State` as `Removed`, saving the change.
* In a subsequent change, edit the architecture and change the `Management State` back to `Managed`.

The Cluster Samples Operator still processes secrets while in `Removed` state. You can create the secret before switching to `Removed`, while in `Removed` before switching to `Managed`, or after switching to `Managed` state. There are delays in creating the samples until the secret event is processed if you create the secret after switching to `Managed`. This helps facilitate the changing of the registry, where you choose to remove all the samples before switching to ensure a clean slate. Removing all samples before switching is not required.

[id="samples-operator-conditions_{context}"]
== Samples resource conditions

The samples resource maintains the following conditions in its status:

[cols="3a,8a",options="header"]
|===
|Condition |Description

|`SamplesExists`
|Indicates the samples are created in the `openshift` namespace.

|`ImageChangesInProgress`
|`True` when image streams are created or updated, but not all of the tag spec generations and tag status generations match.

`False` when all of the generations match, or unrecoverable errors occurred during import, the last seen error is in the message field. The list of pending image streams is in the reason field.

This condition is deprecated in OpenShift Container Platform.

|`ConfigurationValid`
|`True` or `False` based on whether any of the restricted changes noted previously are submitted.

|`RemovePending`
|Indicator that there is a `Management State: Removed` setting pending, but the Cluster Samples Operator is waiting for the deletions to complete.

|`ImportImageErrorsExist`
|Indicator of which image streams had errors during the image import phase for one of their tags.

`True` when an error has occurred. The list of image streams with an error is in the reason field. The details of each error reported are in the message field.

|`MigrationInProgress`
|`True` when the Cluster Samples Operator detects that the version is different from the Cluster Samples Operator version with which the current samples set are installed.

This condition is deprecated in OpenShift Container Platform.

|===

// Module included in the following assemblies:
//
// * openshift_images/configuring_samples_operator.adoc

[id="samples-operator-crd_{context}"]
= Accessing the Cluster Samples Operator configuration

[role="_abstract"]
You can configure the Cluster Samples Operator by editing the file with the provided parameters.

.Prerequisites

* You installed the {oc-first}.

.Procedure

*  Access the Cluster Samples Operator configuration by running the following command:
+
[source,terminal]
----
$ oc edit configs.samples.operator.openshift.io/cluster
----
+
The Cluster Samples Operator configuration resembles the following example:
+
[source,yaml]
----
apiVersion: samples.operator.openshift.io/v1
kind: Config
# ...
----

// Module included in the following assemblies:
//
// * openshift_images/configuring-samples-operator.adoc
// * openshift_images/configuring-samples-operator.adoc

[id="images-samples-operator-deprecated-image-stream_{context}"]
= Removing deprecated image stream tags from the Cluster Samples Operator

[role="_abstract"]
The Cluster Samples Operator leaves deprecated image stream tags in an image stream because users can have deployments that use the deprecated image stream tags.

You can remove deprecated image stream tags by editing the image stream with the  `oc tag` command.

[NOTE]
====
Deprecated image stream tags that the samples providers have removed from their image streams are not included on initial installations.
====

.Prerequisites

* You installed the {oc-first}.

.Procedure

* Remove deprecated image stream tags by editing the image stream with the following `oc tag` command:
+
[source,terminal]
----
$ oc tag -d <image_stream_name:tag>
----
+
.Example output
[source,terminal]
----
Deleted tag default/<image_stream_name:tag>.
----

//Similar procedure in images-imagestreams-remove-tag.adoc
