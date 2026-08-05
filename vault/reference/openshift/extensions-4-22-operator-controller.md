---
title: "Operator Controller"
type: reference
domain: openshift
slug: extensions-4-22-operator-controller
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/operator-controller
version: 4.22
family: extensions
documentKind: "Documentation"
---

# Operator Controller

[id="operator-controller"]
= Operator Controller

[role="_abstract"]
Operator Controller is the central component of {olmv1-first} and consumes the other {olmv1} component, catalogd. It extends Kubernetes with an API through which users can install Operators and extensions.

// Module included in the following assemblies:
//
// * operators/olm_v1/arch/olmv1-operator-controller.adoc
// * extensions/arch/olmv1-operator-controller.adoc

[id="olmv1-clusterextension-api_{context}"]
= ClusterExtension API

[role="_abstract"]
To manage installed extensions in {olmv1}, use the `ClusterExtension` API. This consolidated API simplifies extension management by replacing multiple {olmv0} objects with a single cluster-scoped resource.

[IMPORTANT]
====
In {olmv1}, `ClusterExtension` objects are cluster-scoped. This differs from {olmv0} where Operators can be either namespace-scoped or cluster-scoped. In {olmv0}, the scope depends on the configuration of related `Subscription` and `OperatorGroup` objects.

For more information about {olmv0} behavior, see _Multitenancy and Operator colocation_.
====

.Example `ClusterExtension` object
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
spec:
  namespace: <namespace_name>
  config:
    configType: Inline
    inline:
      watchNamespace: <namespace_name>
  serviceAccount:
    name: <service_account_name>
  source:
    sourceType: Catalog
    catalog:
      packageName: <package_name>
      channels:
        - <channel>
      version: "<version>"
----

`config`:: If the extension supports watching a specific namespace, use this field to configure extension behavior. For more information, see "Extension configuration".

[role="_additional-resources"]
.Additional resources

* Operator Lifecycle Manager (OLM) -> Multitenancy and Operator colocation
* Supported extensions

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
// * extensions/arch/operator-controller.adoc

[id="olmv1-object-ownership_{context}"]
= Object ownership for cluster extensions

In {olmv1-first}, a Kubernetes object can only be owned by a single `ClusterExtension` object at a time. This ensures that objects within an OpenShift Container Platform cluster are managed consistently and prevents conflicts between multiple cluster extensions attempting to control the same object.

[id="olmv1-single-ownership_{context}"]
== Single ownership

The core ownership principle enforced by {olmv1} is that each object can only have one cluster extension as its owner. This prevents overlapping or conflicting management by multiple cluster extensions, ensuring that each object is uniquely associated with only one bundle.

.Implications of single ownership

* Bundles that provide a `CustomResourceDefinition` (CRD) object can only be installed once.
+
Bundles provide CRDs, which are part of a `ClusterExtension` object. This means you can install a bundle only once in a cluster. Attempting to install another bundle that provides the same CRD results in failure, as each custom resource can have only one cluster extension as its owner.

* Cluster extensions cannot share objects.
+
The single-owner policy of {olmv1} means that cluster extensions cannot share ownership of any objects. If one cluster extension manages a specific object, such as a `Deployment`, `CustomResourceDefinition`, or `Service` object, another cluster extension cannot claim ownership of the same object. Any attempt to do so is blocked by {olmv1}.

[id="olmv1-error-messages_{context}"]
== Error messages

When a conflict occurs due to multiple cluster extensions attempting to manage the same object, Operator Controller returns an error message indicating the ownership conflict, such as the following:

.Example error message
[source,text]
----
CustomResourceDefinition 'logfilemetricexporters.logging.kubernetes.io' already exists in namespace 'kubernetes-logging' and cannot be managed by operator-controller
----

This error message signals that the object is already being managed by another cluster extension and cannot be reassigned or shared.

[id="olmv1-ownership-considerations_{context}"]
== Considerations

As a cluster or extension administrator, review the following considerations:

Uniqueness of bundles::
Ensure that Operator bundles providing the same CRDs are not installed more than once. This can prevent potential installation failures due to ownership conflicts.

Avoid object sharing::
If you need different cluster extensions to interact with similar resources, ensure they are managing separate objects. Cluster extensions cannot jointly manage the same object due to the single-owner enforcement.

// Module is included in the following assemblies:
//
// * openshift-docs/extensions/arch/operator-controller.adoc

[id="olmv1-clusterobjectsets_{context}"]
= ClusterObjectSets

[role="_abstract"]
As part of {olmv1-first}, the operator-controller creates `ClusterObjectSet` resources when you install or upgrade content with a `ClusterExtension` object. `ClusterObjectSet` objects enable safe, phased rollouts of Kubernetes resources.

A `ClusterObjectSet` object is a cluster-scoped resource. It is not content that you install. It is the controller’s internal record for one revision of your `ClusterExtension` object. It rolls out related resources sequentially with built-in readiness checks between phases.

A `ClusterObjectSet` object solves several problems when managing sets of related Kubernetes resources:

Immutable revision content:: The revision number, phases, objects, and collision protection strategy are immutable, that is, they cannot change once set. This provides a clear audit trail of what was deployed at each revision.

Phased rollout:: Resources are grouped into phases, for example, CRDs before Deployments, and are deployed sequentially. A phase only progresses after all its objects pass readiness probes. Manifests are organized into phases, applied to the cluster, and must pass some status probes before they progress to the next phase. This avoids incomplete installs.

Safe transitions:: During upgrades, both old and new revisions remain active until the new revision succeeds. Object ownership transitions between revisions automatically.

Single ownership:: Each resource can only be managed by one `ClusterObjectSet` at a time, preventing conflicts.

Large resource support:: Object manifests can be stored inline or externalized into secrets, allowing bundles larger than the etcd 1.5 MiB object size limit.

[NOTE]
====
Archived `ClusterObjectSet` revisions stay on the cluster as a history of what was applied for that `ClusterExtension` object.
====

Each `ClusterObjectSet` contains the following content:

A revision number:: A permanent, sequential integer that identifies the version. When the bundle version changes, it creates a new revision. During an upgrade, the old and new revision can both be active until the new one finishes. Older revisions are archived.

A lifecycle state:: This shows the status of the `ClusterObjectSet`, which can be `Active` (managed and reconciled) or `Archived`. The  `lifecycleState` transitions from `Active` to `Archived` but not back.

A list of phases:: Objects within a `ClusterObjectSet` are organized into phases. Each phase groups related resources, and phases are applied sequentially. Within a phase, all objects are applied simultaneously in no particular order.

A collision protection strategy:: Controls whether a `ClusterObjectSet` can adopt pre-existing objects on the cluster.

Status conditions:: Indicates whether the revision is actively rolling out and reports rollout progress, availability, and success.

At most, one `ClusterObjectSet` manages a given cluster object at a time. Very large bundles store manifests in `Secret` objects so that size limits do not block installs or upgrades.

Additionally, support for management of large object bundles created by `ClusterObjectSet` is provided. `ClusterObjectSet` embeds Kubernetes manifests in `.spec.phases[].objects[].object`. Currently, with up to 20 phases and 50 objects per phase, they can exceed the etcd 1.5 MiB object size limit. Large Operators with many CRDs, Deployments, RBAC rules, and webhook configurations frequently hit this limit, causing the API server to reject the `ClusterObjectSet` and fail installation or upgrade.

To solve this, objects can be externalized into `Secret` resources using per-object references. The phases data is immutable and only consumed by the revision reconciler, making it suitable for externalization.
