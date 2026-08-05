---
title: "Creating ConfigMap objects for the image-based upgrade with the {lcao}"
type: reference
domain: openshift
slug: edge-computing-4-22-cnf-image-based-upgrade-prep-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-image-based-upgrade-prep-resources
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Creating ConfigMap objects for the image-based upgrade with the {lcao}

[id="cnf-image-based-upgrade-prep-resources"]
= Creating ConfigMap objects for the image-based upgrade with the {lcao}

The {lcao} needs all your {oadp-short} resources, extra manifests, and custom catalog sources wrapped in a `ConfigMap` object to process them for the image-based upgrade.

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-prep-oadp_{context}"]
= Creating {oadp-short} ConfigMap objects for the image-based upgrade with {lcao}

[role="_abstract"]
Create your {oadp-short} resources that are used to back up and restore your resources during the upgrade.

.Prerequisites

* You have generated a seed image from a compatible seed cluster.
* You have created {oadp-short} backup and restore resources.
* You have created a separate partition on the target cluster for the container images that is shared between stateroots. For more information, see "Configuring a shared container partition for the image-based upgrade".
* You have deployed a version of {lcao} that is compatible with the version used with the seed image.
* You have installed the {oadp-short} Operator, the `DataProtectionApplication` CR, and its secret on the target cluster.
* You have created an S3-compatible storage solution and a ready-to-use bucket with proper credentials configured. For more information, see "About installing {oadp-short}".

.Procedure

. Create the {oadp-short} `Backup` and `Restore` CRs for platform artifacts in the same namespace where the {oadp-short} Operator is installed, which is `openshift-adp`.

.. If the target cluster is managed by {rh-rhacm}, add the following `PlatformBackupRestore.yaml` file for backing up and restoring {rh-rhacm} artifacts:
+
--
--
.. If you created persistent volumes on your cluster through {lvms}, add the following `PlatformBackupRestoreLvms.yaml` file for {lvms} artifacts:
+

. If you need to restore applications after the upgrade, create the {oadp-short} `Backup` and `Restore` CRs for your application in the `openshift-adp` namespace.

.. Create the {oadp-short} CRs for cluster-scoped application artifacts in the `openshift-adp` namespace, for example:
+

.. Create the {oadp-short} CRs for your namespace-scoped application artifacts.
+
--
When using LSO, see the following example {oadp-short} CRs:

When using {lvms}, see the following example {oadp-short} CRs:

[IMPORTANT]
====
The same version of the applications must function on both the current and the target release of OpenShift Container Platform.
====
--

. Create the `ConfigMap` object for your {oadp-short} CRs by running the following command:
+
[source,terminal]
----
$ oc create configmap oadp-cm-example --from-file=example-oadp-resources.yaml=<path_to_oadp_crs> -n openshift-adp
----

. Patch the `ImageBasedUpgrade` CR by running the following command:
+
[source,terminal]
----
$ oc patch imagebasedupgrades.lca.openshift.io upgrade \
  -p='{"spec": {"oadpContent": [{"name": "oadp-cm-example", "namespace": "openshift-adp"}]}}' \
  --type=merge -n openshift-lifecycle-agent
----

[role="_additional-resources"]
.Additional resources

* Configuring a shared container partition between ostree stateroots

* About installing {oadp-short}

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-prep-extramanifests_{context}"]
= Creating ConfigMap objects of extra manifests for the image-based upgrade with {lcao}

[role="_abstract"]
Create additional manifests that you want to apply to the target cluster.

[NOTE]
====
If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on.
====

.Procedure

. Create a YAML file that contains your extra manifests, such as SR-IOV.
+
.Example SR-IOV resources
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: "example-sriov-node-policy"
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames: [ens1f0]
  nodeSelector:
    node-role.kubernetes.io/master: ""
  mtu: 1500
  numVfs: 8
  priority: 99
  resourceName: example-sriov-node-policy
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: "example-sriov-network"
  namespace: openshift-sriov-network-operator
spec:
  ipam: |-
    {
    }
  linkState: auto
  networkNamespace: sriov-namespace
  resourceName: example-sriov-node-policy
  spoofChk: "on"
  trust: "off"
----

. Create the `ConfigMap` object by running the following command:
+
[source,terminal]
----
$ oc create configmap example-extra-manifests-cm --from-file=example-extra-manifests.yaml=<path_to_extramanifest> -n openshift-lifecycle-agent
----

. Patch the `ImageBasedUpgrade` CR by running the following command:
+
[source,terminal]
----
$ oc patch imagebasedupgrades.lca.openshift.io upgrade \
  -p='{"spec": {"extraManifests": [{"name": "example-extra-manifests-cm", "namespace": "openshift-lifecycle-agent"}]}}' \
  --type=merge -n openshift-lifecycle-agent
----

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-prep-catalogsources_{context}"]
= Creating ConfigMap objects of custom catalog sources for the image-based upgrade with {lcao}

[role="_abstract"]
You can keep your custom catalog sources after the upgrade by generating a `ConfigMap` object for your catalog sources and adding them to the `spec.extraManifest` field in the `ImageBasedUpgrade` CR.
For more information about catalog sources, see "Catalog source".

.Procedure

. Create a YAML file that contains the `CatalogSource` CR:
+
--
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: CatalogSource
metadata:
  name: example-catalogsources
  namespace: openshift-marketplace
spec:
  sourceType: grpc
  displayName: disconnected-redhat-operators
  image: quay.io/example-org/example-catalog:v1
----
--

. Create the `ConfigMap` object by running the following command:
+
[source,terminal]
----
$ oc create configmap example-catalogsources-cm --from-file=example-catalogsources.yaml=<path_to_catalogsource_cr> -n openshift-lifecycle-agent
----

. Patch the `ImageBasedUpgrade` CR by running the following command:
+
[source,terminal]
----
$ oc patch imagebasedupgrades.lca.openshift.io upgrade \
  -p='{"spec": {"extraManifests": [{"name": "example-catalogsources-cm", "namespace": "openshift-lifecycle-agent"}]}}' \
  --type=merge -n openshift-lifecycle-agent
----

[role="_additional-resources"]
.Additional resources

* Catalog source

* Performing an image-based upgrade for {sno} with {lcao}
