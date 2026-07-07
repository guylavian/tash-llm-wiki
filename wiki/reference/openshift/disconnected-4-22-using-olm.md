---
title: "Using Operator Lifecycle Manager in disconnected environments"
type: reference
domain: openshift
slug: disconnected-4-22-using-olm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected/using-olm
version: 4.22
family: disconnected
documentKind: "Documentation"
---

# Using Operator Lifecycle Manager in disconnected environments

[id="olm-restricted-networks"]
= Using Operator Lifecycle Manager in disconnected environments

For OpenShift Container Platform clusters in disconnected environments, Operator Lifecycle Manager (OLM) by default cannot access the Red{nbsp}Hat-provided software catalog sources hosted on remote registries because those remote sources require full internet connectivity.

However, as a cluster administrator you can still enable your cluster to use OLM in a disconnected environment if you have a workstation that has full internet access. The workstation, which requires full internet access to pull the remote software catalog content, is used to prepare local mirrors of the remote sources, and push the content to a mirror registry.

The mirror registry can be located on a bastion host, which requires connectivity to both your workstation and the disconnected cluster, or a completely disconnected, or _airgapped_, host, which requires removable media to physically move the mirrored content to the disconnected environment.

This guide describes the following process that is required to enable OLM in disconnected environments:

* Disable the default remote software catalog sources for OLM.
* Use a workstation with full internet access to create and push local mirrors of the software catalog content to a mirror registry.
* Configure OLM to install and manage Operators from local sources on the mirror registry instead of the default remote sources.

After enabling OLM in a disconnected environment, you can continue to use your unrestricted workstation to keep your local software catalog sources updated as newer versions of Operators are released.

[IMPORTANT]
====
While OLM can manage Operators from local sources, the ability for a given Operator to run successfully in a disconnected environment still depends on the Operator itself meeting the following criteria:

* List any related images, or other container images that the Operator might require to perform their functions, in the `relatedImages` parameter of its `ClusterServiceVersion` (CSV) object.
* Reference all specified images by a digest (SHA) and not by a tag.

You can search software on the Red{nbsp}Hat Ecosystem Catalog for a list of Red{nbsp}Hat Operators that support running in disconnected mode by filtering with the following selections:

[horizontal]
Type:: Containerized application
Deployment method:: Operator
Infrastructure features:: Disconnected
====

[role="_additional-resources"]
.Additional resources

* Red{nbsp}Hat-provided Operator catalogs

[id="olm-restricted-network-prereqs"]
== Prerequisites

* You are logged in to your OpenShift Container Platform cluster as a user with `cluster-admin` privileges.

* If you are using OLM in a disconnected environment on {ibm-z-name}, you must have at least 12 GB allocated to the directory where you place your registry.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc-user-infra.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * operators/admin/olm-restricted-networks.adoc
// * operators/admin/olm-managing-custom-catalogs.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc

[id="olm-restricted-networks-operatorhub_{context}"]
= Disabling the default software catalog sources

Operator catalogs that source content provided by Red Hat and community projects are configured for the software catalog by default during an OpenShift Container Platform installation.
In a restricted network environment, you must disable the default catalogs as a cluster administrator.
You can then configure the OperatorHub custom resource definition (CRD) to use local catalog sources for the software catalog.
As a cluster administrator, you can disable the set of default catalogs.

.Procedure

* Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:
+
[source,terminal]
----
$ oc patch OperatorHub cluster --type json \
    -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
----

[TIP]
====
Alternatively, you can use the web console to manage catalog sources. From the *Administration* -> *Cluster Settings* -> *Configuration* -> *OperatorHub* page, click the *Sources* tab, where you can create, update, delete, disable, and enable individual sources.
====

[id="olm-mirror-catalog_olm-restricted-networks"]
== Mirroring an Operator catalog

For instructions about mirroring Operator catalogs for use with disconnected clusters, see Mirroring Operator catalogs for use with disconnected clusters.

[IMPORTANT]
====
As of OpenShift Container Platform 4.11, the default Red{nbsp}Hat-provided Operator catalog releases in the file-based catalog format. The default Red{nbsp}Hat-provided Operator catalogs for OpenShift Container Platform 4.6 through 4.10 released in the deprecated SQLite database format.

The `opm` subcommands, flags, and functionality related to the SQLite database format are also deprecated and will be removed in a future release. The features are still supported and must be used for catalogs that use the deprecated SQLite database format.

Many of the `opm` subcommands and flags for working with the SQLite database format, such as `opm index prune`, do not work with the file-based catalog format. For more information about working with file-based catalogs, see Operator Framework packaging format, Managing custom catalogs, and Mirroring images for a disconnected installation by using the oc-mirror plugin v2.
====

// Module included in the following assemblies:
//
// * post_installation_configuration/preparing-for-users.adoc
// * operators/admin/olm-restricted-networks.adoc
// * operators/admin/managing-custom-catalogs.adoc

[id="olm-creating-catalog-from-index_{context}"]
= Adding a catalog source to a cluster

Adding a catalog source to an OpenShift Container Platform cluster enables the discovery and installation of Operators for users.
Cluster administrators
Administrators with the `dedicated-admin` role
can create a `CatalogSource` object that references an index image. The software catalog uses catalog sources to populate the user interface.

// In OSD/ROSA, a dedicated-admin can see catalog sources here, but can't add, edit, or delete them.
[TIP]
====
Alternatively, you can use the web console to manage catalog sources. From the *Administration* -> *Cluster Settings* -> *Configuration* -> *OperatorHub* page, click the *Sources* tab, where you can create, update, delete, disable, and enable individual sources.
====

// In OSD/ROSA, a dedicated-admin can update catalog sources in the console by searching for them.
[TIP]
====
Alternatively, you can use the web console to manage catalog sources. From the *Home* -> *Search* page, select a project, click the *Resources* drop-down and search for `CatalogSource`. You can create, update, delete, disable, and enable individual sources.
====

.Prerequisites

* You built and pushed an index image to a registry.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

. Create a `CatalogSource` object that references your index image.
If you used the `oc adm catalog mirror` command to mirror your catalog to a target registry, you can use the generated `catalogSource.yaml` file in your manifests directory as a starting point.

.. Modify the following to your specifications and save it as a `catalogSource.yaml` file:
+
--
[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: my-operator-catalog <1>
  namespace: {namespace} <2>
spec:
  sourceType: grpc
  grpcPodConfig:
    securityContextConfig: <security_mode> <3>
  image: <registry>/<namespace>/{index-image}:{tag} <4>
  displayName: My Operator Catalog
  publisher: <publisher_name> <5>
  updateStrategy:
    registryPoll: <6>
      interval: 30m
----
<1> If you mirrored content to local files before uploading to a registry, remove any backslash (`/`) characters from the `metadata.name` field to avoid an "invalid resource name" error when you create the object.
<2> If you want the catalog source to be available globally to users in all namespaces, specify the `{namespace}` namespace. Otherwise, you can specify a different namespace for the catalog to be scoped and available only for that namespace.
<3> Specify the value of `legacy` or `restricted`. If the field is not set, the default value is `legacy`. In a future OpenShift Container Platform release, it is planned that the default value will be `restricted`.
+
[NOTE]
====
If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`.
====
<4> Specify your index image. If you specify a tag after the image name, for example `:{tag}`, the catalog source pod uses an image pull policy of `Always`, meaning the pod always pulls the image prior to starting the container. If you specify a digest, for example `@sha256:<id>`, the image pull policy is `IfNotPresent`, meaning the pod pulls the image only if it does not already exist on the node.
<5> Specify your name or an organization name publishing the catalog.
<6> Catalog sources can automatically check for new versions to keep up to date.
--
.. Modify the following to your specifications and save it as a `catalogSource.yaml` file:
+
--
[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: my-operator-catalog
  namespace: {namespace} <1>
  annotations:
    olm.catalogImageTemplate: <2>
      "<registry>/<namespace>/<index_image_name>:v{kube_major_version}.{kube_minor_version}.{kube_patch_version}"
spec:
  sourceType: grpc
  grpcPodConfig:
    securityContextConfig: <security_mode> <3>
  image: <registry>/<namespace>/<index_image_name>:<tag> <4>
  displayName: My Operator Catalog
  publisher: <publisher_name> <5>
  updateStrategy:
    registryPoll: <6>
      interval: 30m
----
<1> If you want the catalog source to be available globally to users in all namespaces, specify the `{namespace}` namespace. Otherwise, you can specify a different namespace for the catalog to be scoped and available only for that namespace.
<2> Optional: Set the `olm.catalogImageTemplate` annotation to your index image name and use one or more of the Kubernetes cluster version variables as shown when constructing the template for the image tag.
<3> Specify the value of `legacy` or `restricted`. If the field is not set, the default value is `legacy`. In a future OpenShift Container Platform release, it is planned that the default value will be `restricted`.
+
[NOTE]
====
If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`.
====
<4> Specify your index image. If you specify a tag after the image name, for example `:{tag}`, the catalog source pod uses an image pull policy of `Always`, meaning the pod always pulls the image prior to starting the container. If you specify a digest, for example `@sha256:<id>`, the image pull policy is `IfNotPresent`, meaning the pod pulls the image only if it does not already exist on the node.
<5> Specify your name or an organization name publishing the catalog.
<6> Catalog sources can automatically check for new versions to keep up to date.
--

.. Use the file to create the `CatalogSource` object:
+
[source,terminal]
----
$ oc apply -f catalogSource.yaml
----

. Verify the following resources are created successfully.

.. Check the pods:
+
[source,terminal,subs="attributes+"]
----
$ oc get pods -n {namespace}
----
+
.Example output
[source,terminal]
----
NAME                                    READY   STATUS    RESTARTS  AGE
my-operator-catalog-6njx6               1/1     Running   0         28s
marketplace-operator-d9f549946-96sgr    1/1     Running   0         26h
----

.. Check the catalog source:
+
[source,terminal,subs="attributes+"]
----
$ oc get catalogsource -n {namespace}
----
+
.Example output
[source,terminal]
----
NAME                  DISPLAY               TYPE PUBLISHER  AGE
my-operator-catalog   My Operator Catalog   grpc            5s
----

.. Check the package manifest:
+
[source,terminal,subs="attributes+"]
----
$ oc get packagemanifest -n {namespace}
----
+
.Example output
[source,terminal]
----
NAME                          CATALOG               AGE
jaeger-product                My Operator Catalog   93s
----

You can now install the Operators from the *Software Catalog* page on your OpenShift Container Platform web console.

[role="_additional-resources"]
.Additional resources

* Accessing images for Operators from private registries
* Image template for custom catalog sources
* Image pull policy

[id="next-steps_olm-restricted-networks"]
== Next steps

* Updating installed Operators
