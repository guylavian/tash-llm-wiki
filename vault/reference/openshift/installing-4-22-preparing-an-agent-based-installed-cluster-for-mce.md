---
title: "Preparing an Agent-based installed cluster for the {mce}"
type: reference
domain: openshift
slug: installing-4-22-preparing-an-agent-based-installed-cluster-for-mce
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/preparing-an-agent-based-installed-cluster-for-mce
version: 4.22
family: installing
documentKind: "Documentation"
---

# Preparing an Agent-based installed cluster for the {mce}

[id="preparing-an-agent-based-installed-cluster-for-mce"]
= Preparing an Agent-based installed cluster for the {mce}

[role="_abstract"]
You can install the {mce-short} and deploy a hub cluster with the Agent-based Installer.

The following procedure is partially automated and requires manual steps after the initial cluster is deployed.

// Module included in the following assemblies:
//
// * installing_with_agent_based_installer/preparing-an-agent-based-installed-cluster-for-mce.adoc

[id="prerequisites_{context}"]
= Prerequisites

[role="_abstract"]
Before installing the {mce-short} and deploying a hub cluster with the Agent-based Installer, you must complete several prerequisites.

The following prerequisites must be completed:

* You have read the following documentation:
** "Cluster lifecycle with multicluster engine operator overview"
** "Persistent storage using local volumes"
** "Using {ztp} to provision clusters at the network far edge"
** "Preparing to install with the Agent-based Installer"
** "About disconnected installation mirroring"
* You have access to the internet to obtain the necessary container images.
* You have installed the OpenShift CLI (`oc`).
* If you are installing in a disconnected environment, you must have a configured local mirror registry for disconnected installation mirroring.

[role="_additional-resources"]
.Additional resources

* Cluster lifecycle with multicluster engine operator overview
* Persistent storage using local volumes
* Using {ztp} to provision clusters at the network far edge
* Preparing to install with the Agent-based Installer
* About disconnected installation mirroring

// Preparing an Agent-based cluster deployment for the multicluster engine for Kubernetes operator while disconnected
// Module included in the following assemblies:
//
// * installing_with_agent_based_installer/preparing-an-agent-based-installed-cluster-for-mce.adoc

[id="preparing-an-initial-cluster-deployment-for-mce-disconnected_{context}"]

= Preparing an Agent-based cluster deployment for the {mce} while disconnected

[role="_abstract"]
You can mirror the required OpenShift Container Platform container images, the {mce-short}, and the Local Storage Operator (LSO) into your local mirror registry in a disconnected environment.
Ensure that you note the local DNS hostname and port of your mirror registry.

[NOTE]
====
To mirror your OpenShift Container Platform image repository to your mirror registry, you can use either the `oc adm release image` or `oc mirror` command. In this procedure, the `oc mirror` command is used as an example.
====

.Procedure

. Create an `<assets_directory>` folder to contain valid `install-config.yaml` and `agent-config.yaml` files. This directory is used to store all the assets.

. To mirror an OpenShift Container Platform image repository, the multicluster engine, and the LSO, create a `ImageSetConfiguration.yaml` file with the following settings:
+
.Example `ImageSetConfiguration.yaml`

[source,yaml,subs="attributes+"]
----
  kind: ImageSetConfiguration
  apiVersion: mirror.openshift.io/v1alpha2
  archiveSize: 4
  storageConfig:
    imageURL: <your-local-registry-dns-name>:<your-local-registry-port>/mirror/oc-mirror-metadata
    skipTLS: true
  mirror:
    platform:
      architectures:
        - "amd64"
      channels:
        - name: stable-
          type: ocp
    additionalImages:
      - name: registry.redhat.io/ubi9/ubi:latest
    operators:
      - catalog: registry.redhat.io/redhat/redhat-operator-index:v
        packages:
          - name: multicluster-engine
          - name: local-storage-operator
----
+
where:

`archiveSize`:: Specifies the maximum size, in GiB, of each file within the image set.
`storageConfig`:: Specifies the back-end location to receive the image set metadata. This location can be a registry or local directory. It is required to specify `storageConfig` values.
`storageConfig.imageURL`:: Specifies the registry URL for the storage backend.
`channels.name`:: Specifies the channel that contains the OpenShift Container Platform images for the version you are installing.
`operators.catalog`:: Specifies the Operator catalog that contains the OpenShift Container Platform images that you are installing.
`packages`:: Specifies only certain Operator packages and channels to include in the image set. Remove this field to retrieve all packages in the catalog.
In this example, a `package.name` value of `multicluster-engine` includes the multicluster engine packages and channels, and `local-storage-operator` includes the LSO packages and channels.
+
[NOTE]
====
This file is required by the `oc mirror` command when mirroring content.
====

. To mirror a specific OpenShift Container Platform image repository, the multicluster engine, and the LSO, run the following command:
+
[source,terminal]
----
$ oc mirror --dest-skip-tls --config ocp-mce-imageset.yaml docker://<your-local-registry-dns-name>:<your-local-registry-port>
----

. Update the registry and certificate in the `install-config.yaml` file:
+
.Example `imageContentSources.yaml`

[source,yaml]
----
  imageContentSources:
    - source: "quay.io/openshift-release-dev/ocp-release"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/openshift/release-images"
    - source: "quay.io/openshift-release-dev/ocp-v4.0-art-dev"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/openshift/release"
    - source: "registry.redhat.io/ubi9"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/ubi9"
    - source: "registry.redhat.io/multicluster-engine"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/multicluster-engine"
    - source: "registry.redhat.io/rhel8"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/rhel8"
    - source: "registry.redhat.io/redhat"
      mirrors:
        - "<your-local-registry-dns-name>:<your-local-registry-port>/redhat"
----
+
Additionally, ensure your certificate is present in the `additionalTrustBundle` field of the `install-config.yaml`.
+
.Example `install-config.yaml`
[source,yaml]
----
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  zzzzzzzzzzz
  -----END CERTIFICATE-------
----
+
[IMPORTANT]
====
The `oc mirror` command  creates a folder called `oc-mirror-workspace` with several outputs.
This includes the `imageContentSourcePolicy.yaml` file that identifies all the mirrors you need for OpenShift Container Platform and your selected Operators.
====

. Generate the cluster manifests by running the following command:
+
[source,terminal]
----
$ openshift-install agent create cluster-manifests
----
This command updates the cluster manifests folder to include a `mirror` folder that contains your mirror configuration.

// Preparing an Agent-based cluster deployment for the {mce-short} while connected
// Module included in the following assemblies:
//
// * installing_with_agent_based_installer/preparing-an-agent-based-installed-cluster-for-mce.adoc

[id="preparing-an-initial-cluster-deployment-for-mce-connected_{context}"]
= Preparing an Agent-based cluster deployment for the {mce} while connected

[role="_abstract"]
Create the required manifests for the {mce-short}, the Local Storage Operator (LSO), and to deploy an agent-based OpenShift Container Platform cluster as a hub cluster.

.Procedure

. Create a sub-folder named  `openshift` in the `<assets_directory>` folder. This sub-folder is used to store the extra manifests that will be applied during the installation to further customize the deployed cluster.
The `<assets_directory>` folder contains all the assets including the `install-config.yaml` and `agent-config.yaml` files.
+
[NOTE]
====
The installer does not validate extra manifests.
====

. For the multicluster engine, create the following manifests and save them in the `<assets_directory>/openshift` folder:
+
.Example `mce_namespace.yaml`
[source,yaml]
----
  apiVersion: v1
  kind: Namespace
  metadata:
    labels:
      openshift.io/cluster-monitoring: "true"
    name: multicluster-engine
----
+
.Example `mce_operatorgroup.yaml`
[source,yaml]
----
  apiVersion: operators.coreos.com/v1
  kind: OperatorGroup
  metadata:
    name: multicluster-engine-operatorgroup
    namespace: multicluster-engine
  spec:
    targetNamespaces:
    - multicluster-engine
----
+
.Example `mce_subscription.yaml`
[source,yaml]
----
  apiVersion: operators.coreos.com/v1alpha1
  kind: Subscription
  metadata:
    name: multicluster-engine
    namespace: multicluster-engine
  spec:
    channel: "stable-2.3"
    name: multicluster-engine
    source: redhat-operators
    sourceNamespace: openshift-marketplace
----
+
[NOTE]
====
You can install a distributed unit (DU) at scale with the {rh-rhacm-first} using the assisted installer (AI). These distributed units must be enabled in the hub cluster.
The AI service requires persistent volumes (PVs), which are manually created.
====

. For the AI service, create the following manifests and save them in the `<assets_directory>/openshift` folder:
+
.Example `lso_namespace.yaml`
[source,yaml]
----
  apiVersion: v1
  kind: Namespace
  metadata:
    annotations:
      openshift.io/cluster-monitoring: "true"
    name: openshift-local-storage
----
+
.Example `lso_operatorgroup.yaml`
[source,yaml]
----
  apiVersion: operators.coreos.com/v1
  kind: OperatorGroup
  metadata:
    name: local-operator-group
    namespace: openshift-local-storage
  spec:
    targetNamespaces:
      - openshift-local-storage
----
+
.Example `lso_subscription.yaml`
[source,yaml]
----
  apiVersion: operators.coreos.com/v1alpha1
  kind: Subscription
  metadata:
    name: local-storage-operator
    namespace: openshift-local-storage
  spec:
    installPlanApproval: Automatic
    name: local-storage-operator
    source: redhat-operators
    sourceNamespace: openshift-marketplace
----
+
[NOTE]
====
After creating all the manifests, your filesystem must display as follows:

.Example Filesystem
[source,terminal]
----
<assets_directory>
    ├─ install-config.yaml
    ├─ agent-config.yaml
    └─ /openshift
        ├─ mce_namespace.yaml
        ├─ mce_operatorgroup.yaml
        ├─ mce_subscription.yaml
        ├─ lso_namespace.yaml
        ├─ lso_operatorgroup.yaml
        └─ lso_subscription.yaml
----
====

. Create the agent ISO image by running the following command:
+
[source,terminal]
----
$ openshift-install agent create image --dir <assets_directory>
----

. When the image is ready, boot the target machine and wait for the installation to complete.

. To monitor the installation, run the following command:
+
[source,terminal]
----
$ openshift-install agent wait-for install-complete --dir <assets_directory>
----
+
[NOTE]
====
To configure a fully functional hub cluster, you must create the following manifests and manually apply them by running the command `$ oc apply -f <manifest-name>`.
The order of the manifest creation is important and where required, the waiting condition is displayed.
====

. For the PVs that are required by the AI service, create the following manifests:
+
[source,yaml]
----
  apiVersion: local.storage.openshift.io/v1
  kind: LocalVolume
  metadata:
   name: assisted-service
   namespace: openshift-local-storage
  spec:
   logLevel: Normal
   managementState: Managed
   storageClassDevices:
     - devicePaths:
         - /dev/vda
         - /dev/vdb
       storageClassName: assisted-service
       volumeMode: Filesystem
----
+
. Use the following command to wait for the availability of the PVs, before applying the subsequent manifests:
+
[source,terminal]
----
$ oc wait localvolume -n openshift-local-storage assisted-service --for condition=Available --timeout 10m
----
+
[NOTE]
====
 The `devicePath` is an example and may vary depending on the actual hardware configuration used.
====
+
. Create a manifest for a multicluster engine instance.
+
.Example `MultiClusterEngine.yaml`
[source,yaml]
----
  apiVersion: multicluster.openshift.io/v1
  kind: MultiClusterEngine
  metadata:
    name: multiclusterengine
  spec: {}
----

. Create a manifest to enable the AI service.
+
.Example `agentserviceconfig.yaml`
[source,yaml]
----
  apiVersion: agent-install.openshift.io/v1beta1
  kind: AgentServiceConfig
  metadata:
    name: agent
    namespace: assisted-installer
  spec:
   databaseStorage:
    storageClassName: assisted-service
    accessModes:
    - ReadWriteOnce
    resources:
     requests:
      storage: 10Gi
   filesystemStorage:
    storageClassName: assisted-service
    accessModes:
    - ReadWriteOnce
    resources:
     requests:
      storage: 10Gi
----

. Create a manifest to deploy subsequently spoke clusters.
+
.Example `clusterimageset.yaml`
[source,yaml,subs="attributes+"]
----
  apiVersion: hive.openshift.io/v1
  kind: ClusterImageSet
  metadata:
    name: ""
  spec:
    releaseImage: quay.io/openshift-release-dev/ocp-release:.0-x86_64
----

. Create a manifest to import the agent installed cluster (that hosts the multicluster engine and the Assisted Service) as the hub cluster.
+
.Example `autoimport.yaml`
[source,yaml]
----
  apiVersion: cluster.open-cluster-management.io/v1
  kind: ManagedCluster
  metadata:
   labels:
     local-cluster: "true"
     cloud: auto-detect
     vendor: auto-detect
   name: local-cluster
  spec:
   hubAcceptsClient: true
----

. Wait for the managed cluster to be created.
+
[source,terminal]
----
$ oc wait -n multicluster-engine managedclusters local-cluster --for condition=ManagedClusterJoined=True --timeout 10m
----

.Verification

* To confirm that the managed cluster installation is successful, run the following command:
+
[source,terminal]
----
$ oc get managedcluster
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS             JOINED   AVAILABLE  AGE
local-cluster   true           https://<your cluster url>:6443   True     True       77m
----

[role="_additional-resources"]
.Additional resources

* The Local Storage Operator
