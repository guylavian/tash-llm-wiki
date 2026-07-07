---
title: "Creating custom Operator catalogs using the oc-mirror plugin"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-operators-oc-mirror
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-operators-oc-mirror
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Creating custom Operator catalogs using the oc-mirror plugin

[id="microshift-operators-oc-mirror"]
= Creating custom Operator catalogs using the oc-mirror plugin

[role="_abstract"]
You can create custom catalogs with widely available Operators and mirror them by using the oc-mirror {oc-first} plugin. Custom catalogs give you the tool so that you can host Operators locally, or control a variety of factors, such as versions and access.

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators-oc-mirror.adoc

[id="microshift-olm-rh-ops-mirror_{context}"]
= Using Red Hat-provided Operator catalogs and mirror registries

[role="_abstract"]
You can filter catalogs and delete images to get specific Operators and mirror them by using the oc-mirror {oc-first} plugin. You can also use Operators in disconnected settings or embedded in a {op-system-base-full} image.

* To understand more about how to configure your systems for mirroring, follow the links in the following "Additional resources" section.

* If you are ready to deploy Operators from Red Hat-provided Operator catalogs, mirror them, or to embed them in a {op-system-base} image, start with the following section, "Inspecting catalog contents by using the oc-mirror plugin."

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators-oc-mirror.adoc

[id="microshift-using-oc-mirror_{context}"]
= About the oc-mirror plugin for creating a mirror registry

[role="_abstract"]
You can use the oc-mirror {oc-first} plugin with {microshift-short} to filter and delete images from Operator catalogs. You can then mirror the filtered catalog contents to a mirror registry or use the container images in disconnected or offline deployments.

The procedure to mirror content from Red Hat-hosted registries connected to the internet to a disconnected image registry is the same, independent of the registry you select. After you mirror the contents of your catalog, configure each node to retrieve this content from your mirror registry.

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators-oc-mirror.adoc

[id="microshift-connectivity-considerations_{context}"]
= Connectivity considerations when populating a mirror registry

[role="_abstract"]
When you populate your mirror registry, you can use connected or disconnected mirroring depending on your use case.

Connected mirroring::
If you have a host that can access both the internet and your mirror registry, but not your node, you can directly mirror the content from that machine.

Disconnected mirroring::
If you do not have a host that can access both the internet and your mirror registry, you must mirror the images to a file system and then bring that host or removable media into your disconnected environment.
+
[IMPORTANT]
====
A container registry must be reachable by every machine in the node that you provision. Installing, updating, and other operations, such as relocating workloads, fail if the registry is unreachable.
====

To avoid problems caused by an unreachable registry, use the following standard practices:

* Run mirror registries in a highly available way.
* Ensure that the mirror registry at least matches the production availability of your node.

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators-oc-mirror.adoc

[id="microshift-oc-mirror-list-operators-catalogs_{context}"]
= Inspecting catalog contents by using the oc-mirror plugin

[role="_abstract"]
Use the following example procedure to select a catalog and list Operators to add to your oc-mirror plugin image set configuration file.

[NOTE]
====
If you use your own catalogs and Operators, you can push the images directly to your internal registry.
====

.Prerequisites

* You uninstalled {oc-first}.
* You installed the Operator Lifecycle Manager (OLM).
* You installed the oc-mirror plugin.

.Procedure

. Get a list of available Red{nbsp}Hat-provided Operator catalogs to filter by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc mirror list operators --version  --catalogs --v2
----

. Get a list of Operators in the Red Hat Operators catalog by running the following command:
+
[source,terminal]
----
$ oc mirror list operators --catalog=<catalog_source> --v2
----
+
Replace `<catalog_source>` with your catalog source, such as `registry.redhat.io/redhat/redhat-operator-index:v` or `quay.io/operatorhubio/catalog:latest`.

. Select an Operator. This example uses the `amq-broker-rhel9` Operator.

. Optional: To inspect the channels and versions of the Operator you want to filter, enter the following commands:

.. Get a list of channels by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc mirror list operators --catalog=registry.redhat.io/redhat/redhat-operator-index:v --package=amq-broker-rhel9 --v2
----
.. Get a list of versions within a channel by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc mirror list operators --catalog=registry.redhat.io/redhat/redhat-operator-index:v --package=amq-broker-rhel9 --channel=7.13.x --v2
----

.Next steps

* Create and edit an image set configuration file using the information gathered in this procedure.
* Mirror the images from the transformed image set configuration file to a mirror registry or disk.

//First, make the image sets
// Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators-oc-mirror.adoc

[id="microshift-oc-mirror-creating-imageset-config_{context}"]
= Creating an image set configuration file

[role="_abstract"]
You must create an `ImageSetConfiguration` YAML file to specify both the Operators to mirror and the configuration settings for the oc-mirror plugin. Edit the contents of the file so that the entries are compatible with both {microshift-short} and the Operator you plan to use.

[NOTE]
====
`oc mirror` v2 uses a cache system instead of metadata. The cache system prevents the need to start the entire mirroring process over when a single step fails. Instead, you can troubleshoot the failed step and the process does not re-mirror images that existed before the failure.
====

.Prerequisites

* You created a container image registry credentials file. For more information, see the following reference:

** Configuring credentials that allow images to be mirrored

.Procedure

. Create and edit the `ImageSetConfiguration` YAML for {microshift-short} by using the following example as a guide:
+
.Example edited {microshift-short} image set configuration file
[source,yaml,subs="attributes+"]
----
kind: ImageSetConfiguration
apiVersion: mirror.openshift.io/v2alpha1
mirror:
  operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:v{ocp-version}
    packages:
    - name: amq-broker-rhel9
      channels:
      - name: 7.13.x
  additionalImages:
   - name: quay.io/rh_ee_aguidi/multi-platform-container:latest
   - name: quay.io/rh_ee_aguidi/empty-image:latest
----
+
where:

`mirror.operators.catalog`:: Specifies the Operator catalog to retrieve images from.

`mirror.operators.packages.name`:: Specifies the Operator packages to include in the image set. Remove this field to retrieve all packages in the catalog.

`mirror.operators.packages.channels.name`:: Specifies only certain channels of the Operator packages to include in the image set. You must always include the default channel for the Operator package even if you do not use the bundles in that channel. You can find the default channel by running the following command: `oc mirror list operators --catalog=<catalog_name> --package=<package_name>`.

`mirror.additionalImages`:: Specifies any additional images to include in the image set. If you do not need to specify additional images, delete this field.
+
--
[IMPORTANT]
====
The `platform` field, related fields, and Helm are not supported by {microshift-short}.
====
--

. Save the updated file as `ImageSetConfiguration.yaml`.

.Next steps

* Use the oc-mirror plugin to mirror an image set directly to a target mirror registry.
* Configure CRI-O.
* Apply the catalog sources to your node.

//OCP module, reference for valid imageset parameters for microshift; see conditionals
// Module included in the following assemblies:
//
// * disconnected/about-installing-oc-mirror-v2.adoc
// * microshift_running_apps/microshift_operators//microshift-operators-oc-mirror.com

[id="oc-mirror-imageset-config-parameters-v2_{context}"]
= ImageSet configuration parameters for oc-mirror plugin v2

[role="_abstract"]
The oc-mirror plugin v2 requires an image set configuration file that defines what images to mirror.

The following table lists the available parameters for the `ImageSetConfiguration resource.

[NOTE]
====
* When selecting bundles for mirroring, the oc-mirror plugin v2 does not automatically detect group/version/kind (GVK) and bundle dependencies. You must explicitly specify the required Operators, their channels, and the Operator versions in the `ImageSetConfiguration` file. For more information, see "opm CLI reference".

* Using the `minVersion` and `maxVersion` properties to filter for a specific Operator version range can result in a multiple channel heads error. The error message states that there are `multiple channel heads`. This is because when the filter is applied, the update graph of the Operator is truncated.

* OLM requires that every Operator channel contains versions that form an update graph with exactly one end point, that is, the latest version of the Operator. When the filter range is applied, that graph can turn into two or more separate graphs or a graph that has more than one end point.

* To avoid this error, do not filter out the latest version of an Operator. If you still run into the error, depending on the Operator, either the `maxVersion` property must be increased or the `minVersion` property must be decreased. Because every Operator graph can be different, you might need to adjust these values until the error resolves.
====

.`ImageSetConfiguration` parameters
[cols="2,2a,1a",options="header"]
|===
|Parameter
|Description
|Values

|`apiVersion`
|The API version of the `ImageSetConfiguration` content.
|String
Example: `mirror.openshift.io/v2alpha1`

|`archiveSize`
|The maximum size, in GiB, of each archive file within the image set.
|Integer
Example: `4`

|`kubeVirtContainer`
|When set to `true`, includes images from the HyperShift KubeVirt CoreOS container.
|Boolean
Example `ImageSetConfiguration` file:
[source,yaml,subs=attributes+]
----
apiVersion: mirror.openshift.io/v2alpha1
kind: ImageSetConfiguration
mirror:
  platform:
    channels:
    - name: stable-4.16
      minVersion: 4.16.0
      maxVersion: 4.16.0
    kubeVirtContainer: true
----

|`mirror`
|The configuration of the image set.
|Object

|`mirror.additionalImages`
|The additional images configuration of the image set.
|Array of objects

Example:
[source,yaml]
----
additionalImages:
  - name: registry.redhat.io/ubi8/ubi:latest
----

|`mirror.additionalImages.name`
|The tag or digest of the image to mirror.
|String
Example: `registry.redhat.io/ubi8/ubi:latest`

|`mirror.additionalImages.targetRepo`
|Optional. Specifies the custom repository path and URL for the target image on the disconnected registry. This value overrides the default repository path.
|String

|`mirror.additionalImages.targetTag`
|Optional. Specifies the tag applied to the mirrored image. If you do not configure this field, the image is mirrored using the tag provided in the `name` field. If no tag is provided in the `name` field, `oc-mirror` calculates and applies a tag based on the image's partial digest.
|String

|`mirror.blockedImages`
|List of images with a tag or digest (SHA) to block from mirroring.
|Array of strings
Example: `docker.io/library/alpine`

|`mirror.helm`
|The helm configuration of the image set. The oc-mirror plugin does not support helm charts with manually modified `values.yaml` files.
|Object

|`mirror.helm.local`
|The local helm charts to mirror.
|Array of objects. For example:

[source,yaml]
----
local:
  - name: podinfo
    path: /test/podinfo-5.0.0.tar.gz
----

|`mirror.helm.local.charts.imagePaths`
|The custom path of a container image inside of the local helm chart.
+
[NOTE]
====
`oc-mirror` detects and mirrors container images from the helm chart by searching well-known paths. You can also specify custom paths using this field.
====
+
[NOTE]
====
Operand images, dynamically deployed by Operator controllers at runtime, are typically referenced by environment variables within the controller's deployment template. Before OpenShift Container Platform 4.20, while `oc-mirror` could access these environment variables, it attempted to mirror all values, including non-image references, for example, log levels, leading to failures. With this update, you can mirror only the container images referenced in these environment variables.
====
|Array of string. For example:  `"- {.spec.template.spec.custom[*].image}"`.

|`mirror.helm.local.name`
|The name of the local helm chart to mirror.
|String. For example: `podinfo`.

|`mirror.helm.local.path`
|The path of the local helm chart to mirror.
|String. For example: `/test/podinfo-5.0.0.tar.gz`.

|`mirror.helm.repositories`
|The remote helm repositories to mirror from.
|Array of objects. For example:

[source,yaml]
----
repositories:
  - name: podinfo
    url: https://example.github.io/podinfo
    charts:
      - name: podinfo
        version: 5.0.0
         imagePaths:
         - "{.spec.template.spec.custom[*].image}"
----

|`mirror.helm.repositories.name`
|The name of the helm repository to mirror from.
|String. For example: `podinfo`.

|`mirror.helm.repositories.url`
|The URL of the helm repository to mirror from.
|String. For example: [x-]`https://example.github.io/podinfo`.

|`mirror.helm.repositories.charts`
|The remote helm charts to mirror.
|Array of objects.

|`mirror.helm.repositories.charts.name`
|The name of the helm chart to mirror.
|String. For example: `podinfo`.

|`mirror.helm.repositories.charts.imagePaths`
|The custom path of a container image inside of the helm chart.
+
[NOTE]
====
`oc-mirror` detects and mirrors container images from the helm chart by searching well-known paths. You can also specify custom paths using this field.
====
+
[NOTE]
====
Operand images, dynamically deployed by Operator controllers at runtime, are typically referenced by environment variables within the controller's deployment template. Before OpenShift Container Platform 4.20, while `oc-mirror` could access these environment variables, it attempted to mirror all values, including non-image references, for example, log levels, leading to failures. With this update, you can mirror only the container images referenced in these environment variables.
====
|Array of string. For example:  `"- {.spec.template.spec.custom[*].image}"`.

|`mirror.operators`
|The Operators configuration of the image set.
|Array of objects

Example:
[source,yaml,subs="attributes+"]
----
operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:
    packages:
      - name: elasticsearch-operator
        minVersion: '2.4.0'
----

|`mirror.operators.catalog`
|The Operator catalog to include in the image set.
|String
Example: `registry.redhat.io/redhat/redhat-operator-index:v4.15`

|`mirror.operators.full`
|When `true`, downloads the full catalog, Operator package, or Operator channel.
|Boolean
The default value is `false`.

|`mirror.operators.packages`
|The Operator packages configuration.
|Array of objects

Example:
[source,yaml,subs="attributes+"]
----
operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:
    packages:
      - name: elasticsearch-operator
        minVersion: '5.2.3-31'
----

|`mirror.operators.packages.name`
|The Operator package name to include in the image set.
|String
Example: `elasticsearch-operator`

|`mirror.operators.packages.channels`
|Operator package channel configuration
|Object

|`mirror.operators.packages.channels.name`
|The Operator channel name, unique within a package, to include in the image set.
+
[NOTE]
====
You must use explicit registry hostnames for all images listed under `additionalImages`. Without explicit hostnames, the plugin mirrors the images to unexpected target paths.
====
|String
Example: `fast` or `stable-v4.15`

|`mirror.operators.packages.channels.maxVersion`
|The highest version of the Operator mirror across all channels in which it exists.
|String
Example: `5.2.3-31`

|`mirror.operators.packages.channels.minVersion`
|The lowest version of the Operator to mirror across all channels in which it exists
|String
Example: `5.2.3-31`

|`mirror.operators.packages.maxVersion`
|The highest version of the Operator to mirror across all channels in which it exists.
|String
Example: `5.2.3-31`

|`mirror.operators.packages.minVersion`
|The lowest version of the Operator to mirror across all channels in which it exists.
|String
Example: `5.2.3-31`

|`mirror.operators.targetCatalog`
|An alternative name and optional namespace hierarchy to mirror the referenced catalog as
|String
Example: `my-namespace/my-operator-catalog`

|`mirror.operators.targetCatalogSourceTemplate`
|Path on disk for a template to use to complete catalogSource custom resource generated by oc-mirror plugin v2.
|String
Example: `/tmp/catalog-source_template.yaml`
Example of a template file:
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: discarded
  namespace: openshift-marketplace
spec:
  image: discarded
  sourceType: grpc
  updateStrategy:
    registryPoll:
      interval: 30m0s
----

|`mirror.operators.targetTag`
|An alternative tag to append to the `targetName` or `targetCatalog`.
|String
Example: `v1`

|`mirror.platform`
|The platform configuration of the image set.
|Object

|`mirror.platform.architectures`
|The architecture of the platform release payload to mirror.
|Array of strings
Example:
[source,yaml]
----
architectures:
  - amd64
  - arm64
  - multi
  - ppc64le
  - s390x
----

The default value is `amd64`. The value `multi` ensures that the mirroring is supported for all available architectures, eliminating the need to specify individual architectures

|`mirror.platform.channels`
|The platform channel configuration of the image set.
|Array of objects
Example:
[source,yaml,subs="attributes+"]
----
channels:
  - name: stable-4.12
  - name: stable-
----

|`mirror.platform.channels.full`
|When `true`, sets the `minVersion` to the first release in the channel and the `maxVersion` to the last release in the channel.
|Boolean
The default value is `false`

|`mirror.platform.channels.name`
|Name of the release channel
|String
Example: `stable-4.15`

|`mirror.platform.channels.minVersion`
|The minimum version of the referenced platform to be mirrored.
|String
Example: `4.12.6`

|`mirror.platform.channels.maxVersion`
|The highest version of the referenced platform to be mirrored.
|String
Example: `4.15.1`

|`mirror.platform.channels.shortestPath`
|Toggles shortest path mirroring or full range mirroring.
|Boolean
The default value is `false`

|`mirror.platform.channels.type`
|Type of the platform to be mirrored
|String
Example: `ocp` or `okd`. The default is `ocp`.

|`mirror.platform.graph`
|Indicates whether the OSUS graph is added to the image set and subsequently published to the mirror.
|Boolean
The default value is `false`

|`mirror.operators.packages.defaultChannel`
|Must be defined when excluding the default channel from the filtering.
|Array of objects. For example:

[source,yaml]
----
 mirror:
  operators:
    - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.22
      packages:
        - name: rhods-operator
          defaultChannel: fast
          channels:
            - name: fast
----
|===

[id="delete-imagset-config-parameters_{context}"]
== DeleteImageSetConfiguration parameters

To remove images with the oc-mirror plugin v2, you must use a `DeleteImageSetConfiguration.yaml` configuration file that defines which images to delete from the mirror registry. The following table lists the available parameters for the `DeleteImageSetConfiguration` resource.

.`DeleteImageSetConfiguration` parameters
[cols="2,2a,1a",options="header"]
|===
|Parameter
|Description
|Values

|`apiVersion`
|The API version for the `DeleteImageSetConfiguration` content.
|String
Example: `mirror.openshift.io/v2alpha1`

|`delete`
|The configuration of the image set to delete.
|Object

|`delete.additionalImages`
|The additional images configuration of the delete image set.
|Array of objects
Example:
[source,yaml]
----
additionalImages:
  - name: registry.redhat.io/ubi8/ubi:latest
----

|`delete.additionalImages.name`
|The tag or digest of the image to delete.
|String
Example: `registry.redhat.io/ubi8/ubi:latest`

|`delete.additionalImages.targetRepo`
|Specifies the repository path and URL of the image you want to delete.
|String

|`delete.additionalImages.targetTag`
|Specifies the tag applied to the image you want to delete.
|String

|`delete.operators`
|The Operators configuration of the delete image set.
|Array of objects
Example:
[source,yaml]
----
operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:
    packages:
      - name: elasticsearch-operator
        minVersion: '2.4.0'
----

|`delete.operators.catalog`
|The Operator catalog to include in the delete image set.
|String
Example: `registry.redhat.io/redhat/redhat-operator-index:v4.15`

|`delete.operators.full`
|When true, deletes the full catalog, Operator package, or Operator channel.
|Boolean
The default value is `false`

|`delete.operators.packages`
|Operator packages configuration
|Array of objects
Example:
[source,yaml]
----
operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:
    packages:
      - name: elasticsearch-operator
        minVersion: '5.2.3-31'
----

|`delete.operators.packages.name`
|The Operator package name to include in the delete image set.
|String
Example: `elasticsearch-operator`

|`delete.operators.packages.channels`
|Operator package channel configuration
|Object

|`delete.operators.packages.channels.name`
|The Operator channel name, unique within a package, to include in the delete image set.
|String
Example: `fast` or `stable-v4.15`

|`delete.operators.packages.channels.maxVersion`
|The highest version of the Operator to delete within the selected channel.
|String
Example: `5.2.3-31`

|`delete.operators.packages.channels.minVersion`
|The lowest version of the Operator to delete within the selection in which it exists.
|String
Example: `5.2.3-31`

|`delete.operators.packages.maxVersion`
|The highest version of the Operator to delete across all channels in which it exists.
|String
Example: `5.2.3-31`

|`delete.operators.packages.minVersion`
|The lowest version of the Operator to delete across all channels in which it exists.
|String
Example: `5.2.3-31`

|`delete.platform`
|The platform configuration of the image set
|Object

|`delete.platform.architectures`
|The architecture of the platform release payload to delete.
|Array of strings
Example:
[source,yaml]
----
architectures:
  - amd64
  - arm64
  - multi
  - ppc64le
  - s390x
----

The default value is `amd64`

|`delete.platform.channels`
|The platform channel configuration of the image set.
|Array of objects

Example:
[source,yaml,subs="attributes+"]
----
channels:
  - name: stable-4.12
  - name: stable-
----

|`delete.platform.channels.full`
|When `true`, sets the `minVersion` to the first release in the channel and the `maxVersion` to the last release in the channel.
|Boolean
The default value is `false`

|`delete.platform.channels.name`
|Name of the release channel
|String
Example: `stable-4.15`

|`delete.platform.channels.minVersion`
|The minimum version of the referenced platform to be deleted.
|String
Example: `4.12.6`

|`delete.platform.channels.maxVersion`
|The highest version of the referenced platform to be deleted.
|String
Example: `4.15.1`

|`delete.platform.channels.shortestPath`
|Toggles between deleting the shortest path and deleting the full range.
|Boolean
The default value is `false`

|`delete.platform.channels.type`
|Type of the platform to be deleted
|String
Example: `ocp` or `okd`
The default is `ocp`

|`delete.platform.graph`
|Determines whether the OSUS graph is deleted as well on the mirror registry as well.
|Boolean
The default value is `false`
|===

//mirroring from mirror to mirror
// Module included in the following assemblies:
//
// * microshift_running_apps/microshift_operators/microshift-operators-oc-mirror.adoc

[id="microshift-oc-mirror-mirror-to-mirror_{context}"]
= Mirroring from mirror to mirror

[role="_abstract"]
You can use the oc-mirror plugin to mirror an image set directly to a target mirror registry that is accessible during image set creation.

.Prerequisites

* You have access to the internet to get the required container images.
* You installed the {oc-first}.
* You installed the `oc-mirror` CLI plugin.
* You created the image set configuration file.

.Procedure

* Mirror the images from the specified image set configuration to a specified registry by running the following command:
+
[source,terminal,subs="quotes+"]
----
$ oc-mirror --config imageset-config.yaml --workspace file://_<v2_workspace>_ \//
  docker://_<remote_registry>_ --v2
----
+
** You must use the `--workspace` flag for the mirror-to-mirror process. Replace _<v2_workspace>_ with the directory you want to use to store custom resources for the mirroring process.
** Replace _<remote_registry>_ with the name of the registry to mirror the image set file to. The registry must start with `docker://`. If you specify a top-level namespace for the mirror registry, you must also use this same namespace on later executions.
+
.Example output
[source,terminal]
----
Rendering catalog image "registry.example.com/redhat/redhat-operator-index:v{ocp-version}" with file-based catalog
----
+
--
[IMPORTANT]
====
You must use the `ImageDigestMirrorSet` YAML file as reference content for manual configuration of CRI-O in {microshift-short}. You cannot apply the resource directly into a {microshift-short} node.
====
--

.Verification
. List the contents of the `cluster-resources` subdirectory by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ ls _<v2_workspace>_/working-dir/cluster-resources/
----
+
Replace _<v2_workspace>_ with the directory you used to store custom resources for the mirroring process.

.Next steps

* Convert the `ImageDigestMirrorSet` YAML content for use in manually configuring CRI-O.
* If required, mirror the images from mirror to disk for disconnected or offline use.

.Troubleshooting

* Unable to retrieve source image.

//Convert the imageset file and add configuration to CRI-O
//Module included in the following assemblies:
//
// * microshift_running_apps/microshift_operators/microshift-operators-oc-mirror.adoc

[id="microshift-oc-mirror-transform-imageset-to-crio_{context}"]
= Configuring CRI-O for using a registry mirror for Operators

[role="_abstract"]
To use a registry mirror for Operators with {microshift-short}, you must transform the `ImageDigestMirrorSet` YAML file created by the oc-mirror plugin into a format that is compatible with the MicroShift CRI-O container runtime configuration.
.Prerequisites

* The {oc-first} is installed.
* You installed Operator Lifecycle Manager (OLM).
* You installed the oc-mirror plugin.
* You installed the `yq` binary.
* The `ImageDigestMirrorSet` and `CatalogSource` YAML files are available in the `cluster-resources` subdirectory.

.Procedure

. Confirm the contents of the `ImageDigestMirrorSet` YAML file by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ cat _<v2_workspace>_/working-dir/cluster-resources/imagedigestmirrorset.yaml
----
+
Replace _<v2_workspace>_ with the directory name that you used when you generated mirroring resources.
+
.Example output
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: ImageDigestMirrorSet
metadata:
  labels:
    operators.openshift.org/catalog: "true"
  name: operator-0
spec:
  imageDigestMirrors:
  - mirrors:
    - registry.example.com/amq7
    source: registry.redhat.io/amq7
----

. Transform the `imagedigestmirrorset.yaml` into a format ready for CRI-O configuration by running the following command:
+
[source,terminal]
----
$ yq '.spec.imageDigestMirrors[] as $item ireduce([]; . + [{"mirror": $item.mirrors[], "source": ($item | .source)}]) | .[] |
  "[[registry]]
      prefix = \"" + .source + "\"
      location = \"" + .mirror + "\"
      mirror-by-digest-only = true
      insecure = true
      "' ./mirror1/working-dir/cluster-resources/imagedigestmirrorset.yaml
----
+
.Example output
[source,terminal]
----
[[registry]]
      prefix = "registry.redhat.io/amq7"
      location = "registry.example.com/amq7"
      mirror-by-digest-only = true
      insecure = true
----

. Add the output to the CRI-O configuration file in the `/etc/containers/registries.conf.d/` directory:
+
.Example `crio-config.yaml` mirror configuration file
[source,yaml]
----
[[registry]]
      prefix = "registry.redhat.io/amq7"
      location = "registry.example.com/amq7"
      mirror-by-digest-only = true
      insecure = true

[[registry]]
    prefix = ""
    location = "quay.io"
    mirror-by-digest-only = true
[[registry.mirror]]
    location = "<registry_host>:<port>"
    insecure = false
----
+
where

`registry.mirror.location`:: Specifies the hostname and port of your mirror registry server, for example `microshift-quay:8443`.

. Apply the CRI-O configuration changes by restarting {microshift-short} with the following command:
+
[source,terminal]
----
$ sudo systemctl restart crio
----

//Apply changes to node so it can use Operators
//Module included in the following assemblies:
//
// * microshift_running_apps/microshift_operators/microshift-operators-oc-mirror.adoc

[id="microshift-oc-mirror-install-catalog-in-node_{context}"]
= Installing a custom catalog created with the oc-mirror plugin

[role="_abstract"]
After you mirror your image set to the mirror registry, you must apply the generated `CatalogSource` custom resource (CR) into the node. Operator Lifecycle Manager (OLM) uses the `CatalogSource` CR to retrieve information about the available Operators in the mirror registry. You must then create and apply a subscription CR to subscribe to your custom catalog.

.Prerequisites

* You mirrored the image set to your registry mirror.
* You added image reference information to the CRI-O container runtime configuration.

.Procedure

. Apply the catalog source configuration file from the results directory to create the catalog source object by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f ./_<v2_workspace>_/working-dir/cluster-resources/catalogSource-cs-redhat-catalog.yaml
----
+
Replace _<v2_workspace>_ with the directory you used to store custom resources for the mirroring process.
+
.Example output
[source,terminal]
----
catalogsource.operators.coreos.com/cs-redhat-catalog created
----

. For reference, see the following example file:
+
.Example catalog source configuration file
[source,yaml,subs="+attributes"]
----
apiVersion: operators.coreos.com/v2alpha1
kind: CatalogSource
metadata:
  name: redhat-catalog
  namespace: openshift-marketplace
spec:
  sourceType: grpc
  image: registry.example.com/redhat/redhat-catalog:v{ocp-version}
  updateStrategy:
    registryPoll:
      interval: 60m
----
+
where

`metadata.namespace`:: Specifies the global namespace. Setting the `metadata.namespace` to `openshift-marketplace` enables the catalog to reference catalogs in all namespaces. Subscriptions in any namespace can reference catalogs created in the `openshift-marketplace` namespace.

. Verify that the `CatalogSource` resources were successfully installed by running the following command:
+
[source,terminal]
----
$ oc get catalogsource --all-namespaces
----
+
.Example output
[source,terminal]
----
NAMESPACE               NAME                  DISPLAY               TYPE   PUBLISHER   AGE
openshift-marketplace   certified-operators   Certified Operators   grpc   Red Hat     37m
openshift-marketplace   community-operators   Community Operators   grpc   Red Hat     37m
openshift-marketplace   redhat-marketplace    Red Hat Marketplace   grpc   Red Hat     37m
openshift-marketplace   redhat-catalog        Red Hat Catalog     grpc   Red Hat     37m
----

. Verify that the catalog source is running by using the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-marketplace
----
+
.Example output
[source,terminal]
----
NAME                             READY   STATUS    RESTARTS   AGE
cs-redhat-catalog-4227b   2/2     Running   0          2m5s
----

. Create a `Subscription` CR, similar to the following example:
+
.Example `Subscription` CR
[source,yaml]
----
apiVersion: operators.coreos.com/v2alpha1
kind: Subscription
metadata:
  name: amq-broker
  namespace: openshift-operators
spec:
  channel: 7.13.x
  name: amq-broker-rhel9
  source: cs-redhat-catalog
  sourceNamespace: openshift-marketplace
----

. Apply the Subscription CR configuration by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f ./_<subscription_cr.yaml>_
----
+
Specify the name of your subscription in _<subscription_cr.yaml>_, for example `amq--broker-subscription-cr.yaml`.
+
.Example output
[source,terminal]
----
subscription.operators.coreos.com/amq-broker created
----

[id="Additional-resources_microshift-operators-oc-mirror_{context}"]
[role="_additional-resources"]
== Additional resources

* Mirroring images for a disconnected installation by using the oc adm command
* Migrating from oc-mirror plugin v1 to v2
* About custom resources generated by oc-mirror plugin v2
* About the --cache-dir and --workspace flags
* Using Operator Lifecycle Manager in disconnected environments
* Deleting images from a disconnected environment
* Configuring hosts for mirror registry access
* Configuring network settings for fully disconnected hosts
* Mirroring container images for disconnected installations
* Embedding in a {op-system-ostree} image for offline use
