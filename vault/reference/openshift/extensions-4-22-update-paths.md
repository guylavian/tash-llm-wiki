---
title: "Update paths"
type: reference
domain: openshift
slug: extensions-4-22-update-paths
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/update-paths
version: 4.22
family: extensions
documentKind: "Documentation"
---

# Update paths

[id="update-paths"]
= Update paths

When determining _update paths_, also known as upgrade edges or upgrade constraints, for an installed cluster extension, {olmv1-first} supports {olmv0} semantics starting in OpenShift Container Platform 4.16. This support follows the behavior from {olmv0}, including `replaces`, `skips`, and `skipRange` directives, with a few noted differences.

By supporting {olmv0} semantics, {olmv1} accurately reflects the update graph from catalogs.

.Differences from original {olmv0} implementation

* If there are multiple possible successors, {olmv1} behavior differs in the following ways:
** In {olmv0}, the successor closest to the channel head is chosen.
** In {olmv1}, the successor with the highest semantic version (semver) is chosen.

* Consider the following set of file-based catalog (FBC) channel entries:
+
[source,yaml]
----
# ...
- name: example.v3.0.0
  skips: ["example.v2.0.0"]
- name: example.v2.0.0
  skipRange: >=1.0.0 <2.0.0
----
+
If `1.0.0` is installed, {olmv1} behavior differs in the following ways:
+
--
** {olmv0-caps} will not detect an update path to `v2.0.0` because `v2.0.0` is skipped and not on the `replaces` chain.
** {olmv1} will detect the update path because {olmv1} does not have a concept of a `replaces` chain. {olmv1} finds all entries that have a `replace`, `skip`, or `skipRange` value that covers the currently installed version.
--

[role="_additional-resources"]
.Additional resources
* {olmv0-caps} upgrade semantics

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc

[id="olmv1-version-range-support_{context}"]
= Support for version ranges

In {olmv1-first}, you can specify a version range by using a comparison string in an Operator or extension's custom resource (CR). If you specify a version range in the CR, {olmv1} installs or updates to the latest version of the Operator that can be resolved within the version range.

.Resolved version workflow
* The resolved version is the latest version of the Operator that satisfies the constraints of the Operator and the environment.
* An Operator update within the specified range is automatically installed if it is resolved successfully.
* An update is not installed if it is outside of the specified range or if it cannot be resolved successfully.

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc

[id="olmv1-version-range-comparisons_{context}"]
= Version comparison strings

You can define a version range by adding a comparison string to the `spec.version` field in an Operator or extension's custom resource (CR). A comparison string is a list of space- or comma-separated values and one or more comparison operators enclosed in double quotation marks (`"`). You can add another comparison string by including an `OR`, or double vertical bar (`||`), comparison operator between the strings.

.Basic comparisons
[options="header"]
|===

|Comparison operator |Definition

|`=`
|Equal to

|`!=`
|Not equal to

|`>`
|Greater than

| `<`
|Less than

|`>=`
|Greater than or equal to

|`\<=`
|Less than or equal to

|===

You can specify a version range in an Operator or extension's CR by using a range comparison similar to the following example:

.Example version range comparison
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        version: ">=1.11, <1.13"
----

You can use wildcard characters in all types of comparison strings. {olmv1} accepts `x`, `X`, and asterisks (`*`) as wildcard characters. When you use a wildcard character with the equal sign (`=`) comparison operator, you define a comparison at the patch or minor version level.

.Example wildcard characters in comparison strings
[options="header"]
|===

|Wildcard comparison |Matching string

|`1.11.x`
|`>=1.11.0, <1.12.0`

|`>=1.12.X`
|`>=1.12.0`

|`\<=2.x`
|`<3`

|`*`
|`>=0.0.0`

|===

You can make patch release comparisons by using the tilde (`~`) comparison operator. Patch release comparisons specify a minor version up to the next major version.

.Example patch release comparisons
[options="header"]
|===

|Patch release comparison |Matching string

|`~1.11.0`
|`>=1.11.0, <1.12.0`

|`~1`
|`>=1, <2`

|`~1.12`
|`>=1.12, <1.13`

|`~1.12.x`
|`>=1.12.0, <1.13.0`

|`~1.x`
|`>=1, <2`

|===

You can use the caret (`^`) comparison operator to make a comparison for a major release. If you make a major release comparison before the first stable release is published, the minor versions define the API's level of stability. In the semantic versioning (semver) specification, the first stable release is published as the `1.0.0` version.

.Example major release comparisons
[options="header"]
|===

|Major release comparison |Matching string

|`^0`
|`>=0.0.0, <1.0.0`

|`^0.0`
|`>=0.0.0, <0.1.0`

|`^0.0.3`
|`>=0.0.3, <0.0.4`

|`^0.2`
|`>=0.2.0, <0.3.0`

|`^0.2.3`
|`>=0.2.3, <0.3.0`

|`^1.2.x`
|`>= 1.2.0, < 2.0.0`

|`^1.2.3`
|`>= 1.2.3, < 2.0.0`

|`^2.x`
|`>= 2.0.0, < 3`

|`^2.3`
|`>= 2.3, < 3`

|===

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc
// * operators/olm_v1/arch/olmv1-operator-controller.adoc
// * extensions/arch/olmv1-operator-controller.adoc

[id="olmv1-about-target-versions_{context}"]
= Example custom resources (CRs) that specify a target version

In {olmv1-first}, cluster administrators can declaratively set the target version of an Operator or extension in the custom resource (CR).

You can define a target version by specifying any of the following fields:

* Channel
* Version number
* Version range

If you specify a channel in the CR, {olmv1} installs the latest version of the Operator or extension that can be resolved within the specified channel. When updates are published to the specified channel, {olmv1} automatically updates to the latest release that can be resolved from the channel.

.Example CR with a specified channel
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        channels:
          - latest <1>
----
<1> Optional: Installs the latest release that can be resolved from the specified channel. Updates to the channel are automatically installed. Specify the value of the `channels` parameter as an array.

If you specify the Operator or extension's target version in the CR, {olmv1} installs the specified version. When the target version is specified in the CR, {olmv1} does not change the target version when updates are published to the catalog.

If you want to update the version of the Operator that is installed on the cluster, you must manually edit the Operator's CR. Specifying an Operator's target version pins the Operator's version to the specified release.

.Example CR with the target version specified
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        version: "1.11.1" <1>
----
<1> Optional: Specifies the target version. If you want to update the version of the Operator or extension that is installed, you must manually update this field the CR to the desired target version.

If you want to define a range of acceptable versions for an Operator or extension, you can specify a version range by using a comparison string. When you specify a version range, {olmv1} installs the latest version of an Operator or extension that can be resolved by the Operator Controller.

.Example CR with a version range specified
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        version: ">1.11.1" <1>
----
<1> Optional: Specifies that the desired version range is greater than version `1.11.1`. For more information, see "Support for version ranges".

After you create or update a CR, apply the configuration file by running the following command:

.Command syntax
[source,terminal]
----
$ oc apply -f <extension_name>.yaml
----

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc

[id="olmv1-forcing-an-update-or-rollback_{context}"]
= Forcing an update or rollback

{olmv1} does not support automatic updates to the next major version or rollbacks to an earlier version. If you want to perform a major version update or rollback, you must verify and force the update manually.

[WARNING]
====
You must verify the consequences of forcing a manual update or rollback. Failure to verify a forced update or rollback might have catastrophic consequences such as data loss.
====

.Prerequisites

* You have a catalog installed.
* You have an Operator or extension installed.
* You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension you want to install. For more information, see _Creating a service account_.

.Procedure

. Edit the custom resource (CR) of your Operator or extension as shown in the following example:
+
.Example CR
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace> <1>
    serviceAccount:
      name: <service_account_installer_name> <2>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        channels:
          - <channel_name> <3>
        version: <version_or_version_range> <4>
        upgradeConstraintPolicy: SelfCertified <5>
----
<1> Specifies the namespace where you want the bundle installed, such as `pipelines` or `my-extension`. Extensions are still cluster-scoped and might contain resources that are installed in different namespaces.
<2> Specifies the name of the service account you created to install, update, and manage your extension.
<3> Optional: Specifies channel names as an array, such as `pipelines-1.14` or `latest`.
<4> Optional: Specifies the version or version range, such as `1.14.0`, `1.14.x`, or `>=1.16`, of the package you want to install or update. For more information, see "Example custom resources (CRs) that specify a target version" and "Support for version ranges".
<5> Optional: Specifies the upgrade constraint policy. To force an update or rollback, set the field to `SelfCertified`. If unspecified, the default setting is `CatalogProvided`. The `CatalogProvided` setting only updates if the new version satisfies the upgrade constraints set by the package author.

. Apply the changes to your Operator or extensions CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <extension_name>.yaml
----

[role="_additional-resources"]
.Additional resources
* Support for version ranges
// after #82245 merges, add an xref to _Creating a service account to manage cluster extensions_

// Module included in the following assemblies:
//
// * extensions/ce/update-paths.adoc

[id="olmv1-ocp-compat_{context}"]
= Compatibility with OpenShift Container Platform versions

Before cluster administrators can update their OpenShift Container Platform cluster to its next minor version, they must ensure that all installed Operators are updated to a bundle version that is compatible with the cluster's next minor version (4.y+1).

For example, Kubernetes periodically deprecates certain APIs that are removed in subsequent releases. If an extension is using a deprecated API, it might no longer work after the OpenShift Container Platform cluster is updated to the Kubernetes version where the API has been removed.

If an Operator author knows that a specific bundle version is not supported and will not work correctly, for any reason, on OpenShift Container Platform later than a certain cluster minor version, they can configure the maximum version of OpenShift Container Platform that their Operator is compatible with.

In the Operator project's cluster service version (CSV), authors can set the `olm.maxOpenShiftVersion` annotation to prevent administrators from updating the cluster before updating the installed Operator to a compatible version.

.Example CSV with `olm.maxOpenShiftVersion` annotation
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  annotations:
    "olm.properties": '[{"type": "olm.maxOpenShiftVersion", "value": "<cluster_version>"}]' <1>
----
<1> Specifies the latest minor version of OpenShift Container Platform (4.y) that an Operator is compatible with. For example, setting `value` to `` prevents cluster updates to minor versions later than  when this bundle is installed on a cluster.
+
If the `olm.maxOpenShiftVersion` field is omitted, cluster updates are not blocked by this Operator.

[NOTE]
====
When determining a cluster's next minor version (4.y+1), {olmv1} only considers major and minor versions (x and y) for comparisons. It ignores any _z-stream_ versions (4.y.z), also known as patch releases, or pre-release versions.

For example, if the cluster's current version is `.0`, the next minor version is `{ocp-nplus1}`. If the current version is `.0-rc1`, the next minor version is still `{ocp-nplus1}`.
====

[role="_additional-resources"]
.Additional resources
* Deprecated API Migration Guide (Kubernetes documentation)

// Module included in the following assemblies:
//
// * extensions/ce/update-paths.adoc

[id="olmv1-blocked-cluster-updates_{context}"]
= Cluster updates blocked by olm cluster Operator

If an installed Operator's `olm.maxOpenShiftVersion` field is set and a cluster administrator attempts to update their cluster to a version that the Operator does not provide a valid update path for, the cluster update fails and the `Upgradeable` status for the `olm` cluster Operator is set to `False`.

To resolve the issue, the cluster administrator must either update the installed Operator to a version with a valid update path, if one is available, or they must uninstall the Operator. Then, they can attempt the cluster update again.

[role="_additional-resources"]
.Additional resources
* Understanding cluster Operator condition types
* Upgrading installed Operators
* Deleting Operators from a cluster
* Cluster Operators reference -> {olmv1-first} Operator
