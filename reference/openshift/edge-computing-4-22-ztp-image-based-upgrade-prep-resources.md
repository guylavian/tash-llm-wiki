---
title: "Creating ConfigMap objects for the image-based upgrade with the {lcao} using {ztp}"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-image-based-upgrade-prep-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-image-based-upgrade-prep-resources
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Creating ConfigMap objects for the image-based upgrade with the {lcao} using {ztp}

[id="ztp-image-based-upgrade-prep-resources"]
= Creating ConfigMap objects for the image-based upgrade with the {lcao} using {ztp}

[role="_abstract"]
Create your {oadp-short} resources, extra manifests, and custom catalog sources wrapped in a `ConfigMap` object to prepare for the image-based upgrade.

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="ztp-image-based-upgrade-prep-oadp_{context}"]
= Creating {oadp-short} resources for the image-based upgrade with {ztp}

Prepare your {oadp-short} resources to restore your application after an upgrade.

.Prerequisites

* You have provisioned one or more managed clusters with {ztp}.
* You have logged in as a user with `cluster-admin` privileges.
* You have generated a seed image from a compatible seed cluster.
* You have created a separate partition on the target cluster for the container images that is shared between stateroots. For more information, see "Configuring a shared container partition between ostree stateroots when using {ztp}".
* You have deployed a version of {lcao} that is compatible with the version used with the seed image.
* You have installed the {oadp-short} Operator, the `DataProtectionApplication` CR, and its secret on the target cluster.
* You have created an S3-compatible storage solution and a ready-to-use bucket with proper credentials configured. For more information, see "Installing and configuring the {oadp-short} Operator with {ztp}".
* The `openshift-adp` namespace for the OADP `ConfigMap` object must exist on all managed clusters and the hub for the OADP `ConfigMap` to be generated and copied to the clusters.

.Procedure

. Ensure that your Git repository that you use with the ArgoCD policies application contains the following directory structure:
+
--
[source,terminal]
----
├── source-crs/
│   ├── ibu/
│   │    ├── ImageBasedUpgrade.yaml
│   │    ├── PlatformBackupRestore.yaml
│   │    ├── PlatformBackupRestoreLvms.yaml
│   │    ├── PlatformBackupRestoreWithIBGU.yaml
├── ...
├── kustomization.yaml
----

The `source-crs/ibu/PlatformBackupRestoreWithIBGU.yaml` file is provided in the ZTP container image.

.PlatformBackupRestoreWithIBGU.yaml

[NOTE]
====
If you perform the image-based upgrade directly on managed clusters, use the `PlatformBackupRestore.yaml` file.
====

If you use {lvms} to create persistent volumes, you can use the `source-crs/ibu/PlatformBackupRestoreLvms.yaml` provided in the ZTP container image to back up your {lvms} resources.

.PlatformBackupRestoreLvms.yaml
--

. If you need to restore applications after the upgrade, create the {oadp-short} `Backup` and `Restore` CRs for your application in the `openshift-adp` namespace:

.. Create the {oadp-short} CRs for cluster-scoped application artifacts in the `openshift-adp` namespace:
+
.Example {oadp-short} CRs for cluster-scoped application artifacts for LSO and {LVMS}

.. Create the {oadp-short} CRs for your namespace-scoped application artifacts in the `source-crs/custom-crs` directory:
+
--
.Example {oadp-short} CRs namespace-scoped application artifacts when LSO is used

.Example {oadp-short} CRs namespace-scoped application artifacts when {lvms} is used

[IMPORTANT]
====
The same version of the applications must function on both the current and the target release of OpenShift Container Platform.
====
--

. Create a `kustomization.yaml` with the following content:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

configMapGenerator: # <1>
- files:
  - source-crs/ibu/PlatformBackupRestoreWithIBGU.yaml
  #- source-crs/custom-crs/ApplicationClusterScopedBackupRestore.yaml
  #- source-crs/custom-crs/ApplicationApplicationBackupRestoreLso.yaml
  name: oadp-cm
  namespace: openshift-adp # <2>
generatorOptions:
  disableNameSuffixHash: true
----
<1> Creates the `oadp-cm` `ConfigMap` object on the hub cluster with `Backup` and `Restore` CRs.
<2> The namespace must exist on all managed clusters and the hub for the OADP `ConfigMap` to be generated and copied to the clusters.

. Push the changes to your Git repository.

[role="_additional-resources"]
.Additional resources

* Configuring a shared container partition between ostree stateroots when using {ztp}

* Installing and configuring the {oadp-short} Operator with {ztp}

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="ztp-image-based-upgrade-prep-label-extramanifests_{context}"]
= Labeling extra manifests for the image-based upgrade with {ztp}

Label your extra manifests so that the {lcao} can extract resources that are labeled with the `lca.openshift.io/target-ocp-version: <target_version>` label.

.Prerequisites

* You have provisioned one or more managed clusters with {ztp}.
* You have logged in as a user with `cluster-admin` privileges.
* You have generated a seed image from a compatible seed cluster.
* You have created a separate partition on the target cluster for the container images that is shared between stateroots. For more information, see "Configuring a shared container directory between ostree stateroots when using {ztp}".
* You have deployed a version of {lcao} that is compatible with the version used with the seed image.

.Procedure

. Label your required extra manifests with the `lca.openshift.io/target-ocp-version: <target_version>` label in your existing site `PolicyGenTemplate` CR:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1
kind: PolicyGenTemplate
metadata:
  name: example-sno
spec:
  bindingRules:
    sites: "example-sno"
    du-profile: "4.15"
  mcp: "master"
  sourceFiles:
    - fileName: SriovNetwork.yaml
      policyName: "config-policy"
      metadata:
        name: "sriov-nw-du-fh"
        labels:
          lca.openshift.io/target-ocp-version: "4.15" <1>
      spec:
        resourceName: du_fh
        vlan: 140
    - fileName: SriovNetworkNodePolicy.yaml
      policyName: "config-policy"
      metadata:
        name: "sriov-nnp-du-fh"
        labels:
          lca.openshift.io/target-ocp-version: "4.15"
      spec:
        deviceType: netdevice
        isRdma: false
        nicSelector:
          pfNames: ["ens5f0"]
        numVfs: 8
        priority: 10
        resourceName: du_fh
    - fileName: SriovNetwork.yaml
      policyName: "config-policy"
      metadata:
        name: "sriov-nw-du-mh"
        labels:
          lca.openshift.io/target-ocp-version: "4.15"
      spec:
        resourceName: du_mh
        vlan: 150
    - fileName: SriovNetworkNodePolicy.yaml
      policyName: "config-policy"
      metadata:
        name: "sriov-nnp-du-mh"
        labels:
          lca.openshift.io/target-ocp-version: "4.15"
      spec:
        deviceType: vfio-pci
        isRdma: false
        nicSelector:
          pfNames: ["ens7f0"]
        numVfs: 8
        priority: 10
        resourceName: du_mh
    - fileName: DefaultCatsrc.yaml <2>
      policyName: "config-policy"
      metadata:
        name: default-cat-source
        namespace: openshift-marketplace
        labels:
            lca.openshift.io/target-ocp-version: "4.15"
      spec:
          displayName: default-cat-source
          image: quay.io/example-org/example-catalog:v1
----
<1> Ensure that the `lca.openshift.io/target-ocp-version` label matches either the y-stream or the z-stream of the target OpenShift Container Platform version that is specified in the `spec.seedImageRef.version` field of the `ImageBasedUpgrade` CR. The {lcao} only applies the CRs that match the specified version.
<2> If you do not want to use custom catalog sources, remove this entry.

. Push the changes to your Git repository.

[role="_additional-resources"]
.Additional resources

* Configuring a shared container partition between ostree stateroots when using {ztp}

* Performing an image-based upgrade for {sno} clusters using {ztp}
