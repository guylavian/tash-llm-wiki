---
title: "Preparing the hub cluster for {ztp}"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-preparing-the-hub-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-preparing-the-hub-cluster
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Preparing the hub cluster for {ztp}

[id="ztp-preparing-the-hub-cluster"]
= Preparing the hub cluster for {ztp}

To use {rh-rhacm} in a disconnected environment, create a mirror registry that mirrors the OpenShift Container Platform release images and Operator Lifecycle Manager (OLM) catalog that contains the required Operator images. OLM manages, installs, and upgrades Operators and their dependencies in the cluster. You can also use a disconnected mirror host to serve the {op-system} ISO and RootFS disk images that are used to provision the bare-metal hosts.

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_ran_du_ref_design_specs/telco-ran-du-rds.adoc

[id="ztp-telco-ran-software-versions_{context}"]
= Telco RAN DU  validated software components

[role="_abstract"]
The Red Hat telco RAN DU  solution has been validated using the following Red Hat software products for OpenShift Container Platform managed clusters.

.Telco RAN DU managed cluster validated software components
[cols=2*, width="80%", options="header"]
|====
|Component
|Software version

|OpenShift Container Platform
|4.22

|Cluster Logging Operator
|6.5

|Local Storage Operator
|4.22

|OpenShift API for Data Protection (OADP)
|1.6

|PTP Operator
|4.22

|SR-IOV Operator
|4.22

|SRIOV-FEC Operator
|2.12

|Lifecycle Agent Operator
|4.22
|====

* Cluster Logging Operator will be updated to 6.6 when the aligned Cluster Logging Operator version is released.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc]

[id="ztp-gitops-ztp-max-spoke-clusters_{context}"]
= Recommended hub cluster specifications and managed cluster limits for {ztp}

With {ztp-first}, you can manage thousands of clusters in geographically dispersed regions and networks.
The Red Hat Performance and Scale lab successfully created and managed 3500 virtual {sno} clusters with a reduced DU profile from a single {rh-rhacm-first} hub cluster in a lab environment.

In real-world situations, the scaling limits for the number of clusters that you can manage will vary depending on various factors affecting the hub cluster.
For example:

Hub cluster resources::
Available hub cluster host resources (CPU, memory, storage) are an important factor in determining how many clusters the hub cluster can manage.
The more resources allocated to the hub cluster, the more managed clusters it can accommodate.

Hub cluster storage::
The hub cluster host storage IOPS rating and whether the hub cluster hosts use NVMe storage can affect hub cluster performance and the number of clusters it can manage.

Network bandwidth and latency::
Slow or high-latency network connections between the hub cluster and managed clusters can impact how the hub cluster manages multiple clusters.

Managed cluster size and complexity::
The size and complexity of the managed clusters also affects the capacity of the hub cluster.
Larger managed clusters with more nodes, namespaces, and resources require additional processing and management resources.
Similarly, clusters with complex configurations such as the RAN DU profile or diverse workloads can require more resources from the hub cluster.

Number of managed policies::
The number of policies managed by the hub cluster scaled over the number of managed clusters bound to those policies is an important factor that determines how many clusters can be managed.

Monitoring and management workloads::
{rh-rhacm} continuously monitors and manages the managed clusters.
The number and complexity of monitoring and management workloads running on the hub cluster can affect its capacity.
Intensive monitoring or frequent reconciliation operations can require additional resources, potentially limiting the number of manageable clusters.

{rh-rhacm} version and configuration::
Different versions of {rh-rhacm} can have varying performance characteristics and resource requirements.
Additionally, the configuration settings of {rh-rhacm}, such as the number of concurrent reconciliations or the frequency of health checks, can affect the managed cluster capacity of the hub cluster.

Use the following representative configuration and network specifications to develop your own Hub cluster and network specifications.

[IMPORTANT]
====
The following guidelines are based on internal lab benchmark testing only and do not represent complete bare-metal host specifications.
====

.Representative three-node hub cluster machine specifications
[cols=2*, width="90%", options="header"]
|====
|Requirement
|Description

|Server hardware
|3 x Dell PowerEdge R650 rack servers

|NVMe hard disks
a|* 50 GB disk for `/var/lib/etcd`
* 2.9 TB disk for `/var/lib/containers`

|SSD hard disks
a|* 1 SSD split into 15 200GB thin-provisioned logical volumes provisioned as `PV` CRs
* 1 SSD serving as an extra large `PV` resource

|Number of applied DU profile policies
|5
|====

[IMPORTANT]
====
The following network specifications are representative of a typical real-world RAN network and were applied to the scale lab environment during testing.
====

.Simulated lab environment network specifications
[cols=2*, width="90%", options="header"]
|====
|Specification
|Description

|Round-trip time (RTT) latency
|50 ms

|Packet loss
|0.02% packet loss

|Network bandwidth limit
|20 Mbps
|====

[role="_additional-resources"]
.Additional resources

* Creating and managing {sno} clusters with {rh-rhacm}

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="installing-disconnected-rhacm_{context}"]
= Installing {ztp} in a disconnected environment

Use {rh-rhacm-first}, {gitops-title}, and {cgu-operator-first} on the hub cluster in the disconnected environment to manage the deployment of multiple managed clusters.

.Prerequisites

* You have installed the OpenShift Container Platform CLI (`oc`).

* You have logged in as a user with `cluster-admin` privileges.

* You have configured a disconnected mirror registry for use in the cluster.
+
[NOTE]
====
The disconnected mirror registry that you create must contain a version of {cgu-operator} backup and pre-cache images that matches the version of {cgu-operator} running in the hub cluster. The spoke cluster must be able to resolve these images in the disconnected mirror registry.
====

.Procedure

* Install {rh-rhacm} in the hub cluster. See Installing {rh-rhacm} in a disconnected environment.

* Install {gitops-shortname} and {cgu-operator} in the hub cluster.

[role="_additional-resources"]
.Additional resources

* Installing OpenShift GitOps

* Installing {cgu-operator}

* Mirroring an Operator catalog

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="ztp-acm-adding-images-to-mirror-registry_{context}"]
= Adding {op-system} ISO and RootFS images to the disconnected mirror host

Before you begin installing clusters in the disconnected environment with {rh-rhacm-first}, you must first host {op-system-first} images for it to use. Use a disconnected mirror to host the {op-system} images.

.Prerequisites

* Deploy and configure an HTTP server to host the {op-system} image resources on the network. You must be able to access the HTTP server from your computer, and from the machines that you create.

[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. You require ISO and RootFS images to install {op-system} on the hosts. {op-system} QCOW2 images are not supported for this installation type.
====

.Procedure

. Log in to the mirror host.
. Obtain the {op-system} ISO and RootFS images from mirror.openshift.com, for example:

.. Export the required image names and OpenShift Container Platform version as environment variables:
+
[source,terminal]
----
$ export ISO_IMAGE_NAME=<iso_image_name> <1>
----
+
[source,terminal]
----
$ export ROOTFS_IMAGE_NAME=<rootfs_image_name> <2>
----
+
[source,terminal]
----
$ export OCP_VERSION=<ocp_version> <3>
----
<1> ISO image name, for example, `rhcos-.1-x86_64-live.x86_64.iso`
<2> RootFS image name, for example, `rhcos-.1-x86_64-live-rootfs.x86_64.img`
<3> OpenShift Container Platform version, for example, `.1`

.. Download the required images:
+
[source,terminal,subs="attributes+"]
----
$ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos//${OCP_VERSION}/${ISO_IMAGE_NAME} -O /var/www/html/${ISO_IMAGE_NAME}
----
+
[source,terminal,subs="attributes+"]
----
$ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos//${OCP_VERSION}/${ROOTFS_IMAGE_NAME} -O /var/www/html/${ROOTFS_IMAGE_NAME}
----

.Verification steps

* Verify that the images downloaded successfully and are being served on the disconnected mirror host, for example:
+
[source,terminal]
----
$ wget http://$(hostname)/${ISO_IMAGE_NAME}
----
+
.Example output
+
[source,terminal,subs="attributes+"]
----
Saving to: rhcos-.1-x86_64-live.x86_64.iso
rhcos-.1-x86_64-live.x86_64.iso-  11%[====>    ]  10.01M  4.71MB/s
----

[role="_additional-resources"]
.Additional resources

* Creating a mirror registry

* Mirroring images for a disconnected installation

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="enabling-assisted-installer-service-on-bare-metal_{context}"]
= Enabling the assisted service

{rh-rhacm-first} uses the assisted service to deploy OpenShift Container Platform clusters. The assisted service is deployed automatically when you enable the MultiClusterHub Operator on {rh-rhacm-first}. After that, you need to configure the `Provisioning` resource to watch all namespaces and to update the `AgentServiceConfig` custom resource (CR) with references to the ISO and RootFS images that are hosted on the mirror registry HTTP server.

.Prerequisites

* You have installed the {oc-first}.

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have {rh-rhacm} with `MultiClusterHub` enabled.

.Procedure

. Enable the `Provisioning` resource to watch all namespaces and configure mirrors for disconnected environments. For more information, see Enabling the central infrastructure management service.

. Open the `AgentServiceConfig` CR to update the `spec.osImages` field by running the following command:
+
[source,terminal]
----
$ oc edit AgentServiceConfig
----

. Update the `spec.osImages` field in the `AgentServiceConfig` CR:
+
[source,yaml,subs="attributes+"]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: AgentServiceConfig
metadata:
 name: agent
spec:
# ...
  osImages:
    - cpuArchitecture: x86_64
      openshiftVersion: ""
      rootFSUrl: https://<host>/<path>/rhcos-live-rootfs.x86_64.img
      url: https://<host>/<path>/rhcos-live.x86_64.iso
----
+
where:
+
--
`<host>` :: Specifies the fully qualified domain name (FQDN) for the target mirror registry HTTP server.
`<path>` :: Specifies the path to the image on the target mirror registry.
--

. Save and quit the editor to apply the changes.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="ztp-configuring-the-cluster-for-a-disconnected-environment_{context}"]
= Configuring the hub cluster to use a disconnected mirror registry

You can configure the hub cluster to use a disconnected mirror registry for a disconnected environment.

.Prerequisites

* You have a disconnected hub cluster installation with {rh-rhacm-first} {rh-rhacm-version} installed.

* You have hosted the `rootfs` and `iso` images on an HTTP server. See the _Additional resources_ section for guidance about _Mirroring the OpenShift Container Platform image repository_.

[WARNING]
====
If you enable TLS for the HTTP server, you must confirm the root certificate is signed by an authority trusted by the client and verify the trusted certificate chain between your OpenShift Container Platform hub and managed clusters and the HTTP server. Using a server configured with an untrusted certificate prevents the images from being downloaded to the image creation service. Using untrusted HTTPS servers is not supported.
====

.Procedure

. Create a `ConfigMap` containing the mirror registry config:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: assisted-installer-mirror-config
  namespace: multicluster-engine <1>
  labels:
    app: assisted-service
data:
  ca-bundle.crt: | <2>
    -----BEGIN CERTIFICATE-----
    <certificate_contents>
    -----END CERTIFICATE-----

  registries.conf: | <3>
    unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

    [[registry]]
       prefix = ""
       location = "quay.io/example-repository" <4>
       mirror-by-digest-only = true

       [[registry.mirror]]
       location = "mirror1.registry.corp.com:5000/example-repository" <5>
----
<1> The `ConfigMap` namespace must be set to `multicluster-engine`.
<2> The mirror registry’s certificate that is used when creating the mirror registry.
<3> The configuration file for the mirror registry. The mirror registry configuration adds mirror information to the `/etc/containers/registries.conf` file in the discovery image. The mirror information is stored in the `imageContentSources` section of the `install-config.yaml` file when the information is passed to the installation program. The Assisted Service pod that runs on the hub cluster fetches the container images from the configured mirror registry.
<4> The URL of the mirror registry. You must use the URL from the `imageContentSources` section by running the `oc adm release mirror` command when you configure the mirror registry. For more information, see the _Mirroring the OpenShift Container Platform image repository_ section.
<5> The registries defined in the `registries.conf` file must be scoped by repository, not by registry. In this example, both the `quay.io/example-repository` and the `mirror1.registry.corp.com:5000/example-repository` repositories are scoped by the `example-repository` repository.

+
This updates `mirrorRegistryRef` in the `AgentServiceConfig` custom resource, as shown below:
+
.Example output
+
[source,yaml]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: AgentServiceConfig
metadata:
  name: agent
  namespace: multicluster-engine <1>
spec:
  databaseStorage:
    volumeName: <db_pv_name>
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: <db_storage_size>
  filesystemStorage:
    volumeName: <fs_pv_name>
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: <fs_storage_size>
  mirrorRegistryRef:
    name: assisted-installer-mirror-config <2>
  osImages:
    - openshiftVersion: <ocp_version> <3>
      url: <iso_url> <4>
----
<1> Set the `AgentServiceConfig` namespace to `multicluster-engine` to match the `ConfigMap` namespace.
<2> Set `mirrorRegistryRef.name` to match the definition specified in the related `ConfigMap` CR.
<3> Set the OpenShift Container Platform version to either the x.y or x.y.z format.
<4> Set the URL for the ISO hosted on the `httpd` server.

[IMPORTANT]
====
A valid NTP server is required during cluster installation. Ensure that a suitable NTP server is available and can be reached from the installed clusters through the disconnected network.
====

[role="_additional-resources"]
.Additional resources

* Mirroring the OpenShift Container Platform repository

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="ztp-configuring-the-hub-cluster-to-use-unauthenticated-registries_{context}"]
= Configuring the hub cluster to use unauthenticated registries

You can configure the hub cluster to use unauthenticated registries.
Unauthenticated registries does not require authentication to access and download images.

.Prerequisites

* You have installed and configured a hub cluster and installed {rh-rhacm-first} on the hub cluster.

* You have installed the OpenShift Container Platform CLI (oc).

* You have logged in as a user with `cluster-admin` privileges.

* You have configured an unauthenticated registry for use with the hub cluster.

.Procedure

. Update the `AgentServiceConfig` custom resource (CR) by running the following command:
+
[source,terminal]
----
$ oc edit AgentServiceConfig agent
----

. Add the `unauthenticatedRegistries` field in the CR:
+
[source,yaml]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: AgentServiceConfig
metadata:
  name: agent
spec:
  unauthenticatedRegistries:
  - example.registry.com
  - example.registry2.com
  ...
----
+
Unauthenticated registries are listed under `spec.unauthenticatedRegistries` in the `AgentServiceConfig` resource.
Any registry on this list is not required to have an entry in the pull secret used for the spoke cluster installation.
`assisted-service` validates the pull secret by making sure it contains the authentication information for every image registry used for installation.

[NOTE]
====
Mirror registries are automatically added to the ignore list and do not need to be added under `spec.unauthenticatedRegistries`.
Specifying the `PUBLIC_CONTAINER_REGISTRIES` environment variable in the `ConfigMap` overrides the default values with the specified value.
The `PUBLIC_CONTAINER_REGISTRIES` defaults are https://quay.io[quay.io] and https://registry.svc.ci.openshift.org[registry.svc.ci.openshift.org].
====

.Verification

Verify that you can access the newly added registry from the hub cluster by running the following commands:

. Open a debug shell prompt to the hub cluster:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Test access to the unauthenticated registry by running the following command:
+
[source,terminal]
----
sh-4.4# podman login -u kubeadmin -p $(oc whoami -t) <unauthenticated_registry>
----
+
where:
+
--
<unauthenticated_registry>:: Is the new registry, for example, `unauthenticated-image-registry.openshift-image-registry.svc:5000`.
--
+
.Example output
[source,terminal]
----
Login Succeeded!
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="ztp-configuring-hub-cluster-with-argocd_{context}"]
= Configuring the hub cluster with ArgoCD

You can configure the hub cluster with a set of ArgoCD applications that generate the required installation and policy custom resources (CRs) for each site with {ztp-first}.

[NOTE]
====
{rh-rhacm-first} uses `ClusterInstance` CRs to generate the Day 1 managed cluster installation CRs for ArgoCD. Each ArgoCD application can manage a maximum of 1000 `ClusterInstance` CRs.
====

.Prerequisites

* You have a OpenShift Container Platform hub cluster with {rh-rhacm-first} and {gitops-title} installed.

* You have extracted the reference deployment from the {ztp} plugin container as described in the "Preparing the {ztp} site configuration repository" section. Extracting the reference deployment creates the `out/argocd/deployment` directory referenced in the following procedure.

.Procedure

. Prepare the ArgoCD pipeline configuration:

.. Create a Git repository with the directory structure similar to the example directory. For more information, see "Preparing the {ztp} site configuration repository".

.. Configure access to the repository using the ArgoCD UI. Under *Settings* configure the following:

*** *Repositories* - Add the connection information. The URL must end in `.git`, for example, `https://repo.example.com/repo.git` and credentials.

*** *Certificates* - Add the public certificate for the repository, if needed.

.. Modify the two ArgoCD applications, `out/argocd/deployment/clusters-app.yaml` and `out/argocd/deployment/policies-app.yaml`, based on your Git repository:

*** Update the URL to point to the Git repository. The URL ends with `.git`, for example, `https://repo.example.com/repo.git`.

*** The `targetRevision` indicates which Git repository branch to monitor.

*** `path` specifies the path to the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs, respectively.

[start=2]

. Optional: If you have existing ArgoCD applications, verify that the `PrunePropagationPolicy=background` policy is set in the `Application` resource by running the following command:
+
--
[source,terminal]
----
$ oc -n openshift-gitops get applications.argoproj.io  \
clusters -o jsonpath='{.spec.syncPolicy.syncOptions}' |jq
----

.Example output for an existing policy
[source,terminal]
----
[
  "CreateNamespace=true",
  "PrunePropagationPolicy=background",
  "RespectIgnoreDifferences=true"
]
----
--

.. If the `spec.syncPolicy.syncOption` field does not contain a `PrunePropagationPolicy` parameter or `PrunePropagationPolicy` is set to the `foreground` value, set the policy to `background` in the `Application` resource. See the following example:
+
[source,yaml]
----
kind: Application
spec:
  syncPolicy:
    syncOptions:
    - PrunePropagationPolicy=background
----

+
Setting the `background` deletion policy ensures that the `ManagedCluster` CR and all its associated resources are deleted.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="ztp-preparing-the-ztp-git-repository_{context}"]
= Preparing the {ztp} site configuration repository

Before you can use the {ztp-first} pipeline, you need to prepare the Git repository to host the site configuration data.

.Prerequisites

* You have configured the hub cluster GitOps applications for generating the required installation and policy custom resources (CRs).

* You have deployed the managed clusters using {ztp}.

.Procedure

. Create a directory structure with separate paths for the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs.
+
[NOTE]
====
Keep `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs in separate directories.
Both the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` directories must contain a `kustomization.yaml` file that explicitly includes the files in that directory.
====

. Export the `argocd` directory from the `ztp-site-generate` container image using the following commands:
+
[source,terminal,subs="attributes+"]
----
$ podman pull registry.redhat.io/openshift4/ztp-site-generate-rhel8:v
----
+
[source,terminal]
----
$ mkdir -p ./out
----
+
[source,terminal,subs="attributes+"]
----
$ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v extract /home/ztp --tar | tar x -C ./out
----

. Check that the `out` directory contains the following subdirectories:
+
* `out/extra-manifest` contains the source CR files that you use to create extra manifest `ConfigMap` resources through the `configMapGenerator` in the `kustomization.yaml` file. The `ClusterInstance` CR references these `ConfigMap` resources using the `extraManifestsRefs` field.
* `out/source-crs` contains the source CR files that `PolicyGenerator` uses to generate the {rh-rhacm-first} policies.
* `out/argocd/deployment` contains patches and YAML files to apply on the hub cluster for use in the next step of this procedure.
* `out/argocd/example/clusterinstance` contains the examples for `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files that represent the recommended configuration.

. Copy the `out/source-crs` folder and contents to the `PolicyGenerator` or `PolicyGentemplate` directory.

. The out/extra-manifests directory contains the reference manifests for a RAN DU cluster.
Copy the `out/extra-manifests` directory into the `ClusterInstance` folder.
This directory should contain CRs from the `ztp-site-generate` container only.
Do not add user-provided CRs here.
If you want to work with user-provided CRs you must create another directory for that content.
For example:
+
[source,text]
----
example/
  ├── acmpolicygenerator
  │   ├── kustomization.yaml
  │   └── source-crs/
  ├── policygentemplates <1>
  │   ├── kustomization.yaml
  │   └── source-crs/
  └── clusterinstance
        ├── extra-manifests
        └── kustomization.yaml
----
<1> Using `PolicyGenTemplate` CRs to manage and deploy policies to manage clusters will be deprecated in a future OpenShift Container Platform release.
Equivalent and improved functionality is available by using {rh-rhacm-first} and `PolicyGenerator` CRs.

. Commit the directory structure and the `kustomization.yaml` files and push to your Git repository.
The initial push to Git should include the `kustomization.yaml` files.

You can use the directory structure under `out/argocd/example` as a reference for the structure and content of your Git repository.
That structure includes `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` reference CRs for single-node, three-node, and standard clusters.
Remove references to cluster types that you are not using.

For all cluster types, you must:

* Add the `source-crs` subdirectory to the `acmpolicygenerator` or `policygentemplates` directory.
* Add the `extra-manifests` directory to the `clusterinstance` directory.

The following example describes a set of CRs for a network of single-node clusters:

[source,text]
----
example/
  ├── acmpolicygenerator
  │   ├── acm-common-ranGen.yaml
  │   ├── acm-example-sno-site.yaml
  │   ├── acm-group-du-sno-ranGen.yaml
  │   ├── group-du-sno-validator-ranGen.yaml
  │   ├── kustomization.yaml
  │   ├── source-crs/
  │   └── ns.yaml
  └── clusterinstance
        ├── example-sno.yaml
        ├── extra-manifests/ <1>
        ├── custom-manifests/ <2>
        ├── KlusterletAddonConfigOverride.yaml
        └── kustomization.yaml
----
<1> Contains reference manifests from the `ztp-container`.
<2> Contains custom manifests.

[role="_additional-resources"]
.Additional resources

* Configuring managed cluster policies by using PolicyGenerator resources

* Comparing {rh-rhacm} PolicyGenerator and PolicyGenTemplate resource patching

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="ztp-preparing-the-ztp-git-repository-ver-ind_{context}"]
= Preparing the {ztp} site configuration repository for version independence

You can use {ztp} to manage source custom resources (CRs) for managed clusters that are running different versions of OpenShift Container Platform.
This means that the version of OpenShift Container Platform running on the hub cluster can be independent of the version running on the managed clusters.

[NOTE]
====
The following procedure assumes you are using `PolicyGenerator` resources instead of `PolicyGentemplate` resources for cluster policies management.
====

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. Create a directory structure with separate paths for the `ClusterInstance` and `PolicyGenerator` CRs.

. Within the `PolicyGenerator` directory, create a directory for each OpenShift Container Platform version you want to make available.
For each version, create the following resources:
* `kustomization.yaml` file that explicitly includes the files in that directory
* `source-crs` directory to contain reference CR configuration files from the `ztp-site-generate` container
+
If you want to work with user-provided CRs, you must create a separate directory for them.

. In the `/clusterinstance` directory, create a subdirectory for each OpenShift Container Platform version you want to make available. For each version, create at least one directory for reference CRs to be copied from the container. There is no restriction on the naming of directories or on the number of reference directories. If you want to work with custom manifests, you must create a separate directory for them.
+
The following example describes a structure using user-provided manifests and CRs for different versions of OpenShift Container Platform:
+
[source,text]
----
├── acmpolicygenerator
│   ├── kustomization.yaml <1>
│   ├── version_4.13 <2>
│   │   ├── common-ranGen.yaml
│   │   ├── group-du-sno-ranGen.yaml
│   │   ├── group-du-sno-validator-ranGen.yaml
│   │   ├── helix56-v413.yaml
│   │   ├── kustomization.yaml <3>
│   │   ├── ns.yaml
│   │   └── source-crs/ <4>
│   │      └── reference-crs/ <5>
│   │      └── custom-crs/ <6>
│   └── version_4.14 <2>
│       ├── common-ranGen.yaml
│       ├── group-du-sno-ranGen.yaml
│       ├── group-du-sno-validator-ranGen.yaml
│       ├── helix56-v414.yaml
│       ├── kustomization.yaml <3>
│       ├── ns.yaml
│       └── source-crs/ <4>
│         └── reference-crs/ <5>
│         └── custom-crs/ <6>
└── clusterinstance
    ├── kustomization.yaml
    ├── version_4.13
    │   ├── helix56-v413.yaml
    │   ├── kustomization.yaml
    │   ├── extra-manifest/ <7>
    │   └── custom-manifest/ <8>
    └── version_4.14
        ├── helix57-v414.yaml
        ├── kustomization.yaml
        ├── extra-manifest/
        └── custom-manifest/

----
<1> Create a top-level `kustomization` YAML file.
<2> Create the version-specific directories within the custom `/acmpolicygenerator` directory.
<3> Create a `kustomization.yaml` file for each version.
<4> Create a `source-crs` directory for each version to contain reference CRs from the `ztp-site-generate` container.
<5> Create the `reference-crs` directory for policy CRs that are extracted from the ZTP container.
<6> Optional: Create a `custom-crs` directory for user-provided CRs.
<7> Create a directory within the custom `/clusterinstance` directory to contain extra manifests from the `ztp-site-generate` container.
<8> Create a folder to hold user-provided manifests.
+
[NOTE]
====
In the example directory structure, each version subdirectory in the custom `/clusterinstance` directory contains two further subdirectories, one containing the reference manifests copied from the container, the other for custom manifests that you provide.
The names assigned to those directories are examples.
====

. Create ConfigMaps from the manifest directories and reference them in the `ClusterInstance` CR using the `extraManifestsRefs` field.
+
.Example kustomization.yaml with configMapGenerator
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

configMapGenerator:
- name: extra-manifests-cm
  namespace: helix56-v413
  files:
  - extra-manifest/workload-partitioning.yaml <1>
  - extra-manifest/enable-crun-master.yaml
  - custom-manifest/custom-config.yaml <2>
  # ...

generatorOptions:
  disableNameSuffixHash: true
----
<1> Extra manifest files from the `ztp-site-generate` container.
<2> User-provided custom manifest files.

. Edit the `ClusterInstance` CR to reference the `ConfigMap` CR:
+
.Example ClusterInstance CR
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: helix56-v413
  namespace: helix56-v413
spec:
  # ...
  extraManifestsRefs:
  - name: extra-manifests-cm <1>
----
<1> Reference the ConfigMap containing the extra manifests.

. Edit the top-level `kustomization.yaml` file to control which OpenShift Container Platform versions are active. The following is an example of a `kustomization.yaml` file at the top level:
+
[source,yaml]
----
resources:
- version_4.13 <1>
#- version_4.14 <2>
----
<1> Activate version 4.13.
<2> Use comments to deactivate a version.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-preparing-the-hub-cluster.adoc

[id="ztp-configuring-the-hub-cluster-for-backup-and-restore_{context}"]
= Configuring the hub cluster for backup and restore

You can use {ztp} to configure a set of policies to back up `BareMetalHost` resources.
This allows you to recover data from a failed hub cluster and deploy a replacement cluster using {rh-rhacm-first}.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. Create a policy to add the `cluster.open-cluster-management.io/backup=cluster-activation` label to all `BareMetalHost` resources that have the `infraenvs.agent-install.openshift.io` label.
Save the policy as `BareMetalHostBackupPolicy.yaml`.
+
The following example adds the `cluster.open-cluster-management.io/backup` label to all `BareMetalHost` resources that have the `infraenvs.agent-install.openshift.io` label:
+
.Example Policy
[source,yaml]
----
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: bmh-cluster-activation-label
  annotations:
    policy.open-cluster-management.io/description: Policy used to add the cluster.open-cluster-management.io/backup=cluster-activation label to all BareMetalHost resources
spec:
  disabled: false
  policy-templates:
    - objectDefinition:
        apiVersion: policy.open-cluster-management.io/v1
        kind: ConfigurationPolicy
        metadata:
          name: set-bmh-backup-label
        spec:
          object-templates-raw: |
            {{- /* Set cluster-activation label on all BMH resources */ -}}
            {{- $infra_label := "infraenvs.agent-install.openshift.io" }}
            {{- range $bmh := (lookup "metal3.io/v1alpha1" "BareMetalHost" "" "" $infra_label).items }}
                - complianceType: musthave
                  objectDefinition:
                    kind: BareMetalHost
                    apiVersion: metal3.io/v1alpha1
                    metadata:
                      name: {{ $bmh.metadata.name }}
                      namespace: {{ $bmh.metadata.namespace }}
                      labels:
                        cluster.open-cluster-management.io/backup: cluster-activation <1>
            {{- end }}
          remediationAction: enforce
          severity: high
---
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Placement
metadata:
  name: bmh-cluster-activation-label-pr
spec:
  predicates:
    - requiredClusterSelector:
        labelSelector:
          matchExpressions:
            - key: name
              operator: In
              values:
                - local-cluster
---
apiVersion: policy.open-cluster-management.io/v1
kind: PlacementBinding
metadata:
  name: bmh-cluster-activation-label-binding
placementRef:
  name: bmh-cluster-activation-label-pr
  apiGroup: cluster.open-cluster-management.io
  kind: Placement
subjects:
  - name: bmh-cluster-activation-label
    apiGroup: policy.open-cluster-management.io
    kind: Policy
---
apiVersion: cluster.open-cluster-management.io/v1beta2
kind: ManagedClusterSetBinding
metadata:
  name: default
  namespace: default
spec:
  clusterSet: default
----
<1> If you apply the `cluster.open-cluster-management.io/backup: cluster-activation` label to `BareMetalHost` resources, the {rh-rhacm} cluster backs up those resources.
You can restore the `BareMetalHost` resources if the active cluster becomes unavailable, when restoring the hub activation resources.

. Apply the policy by running the following command:
+
[source,terminal]
----
$ oc apply -f BareMetalHostBackupPolicy.yaml
----

.Verification

. Find all `BareMetalHost` resources with the label `infraenvs.agent-install.openshift.io`  by running the following command:
+
[source,terminal]
----
$ oc get BareMetalHost -A -l infraenvs.agent-install.openshift.io
----
+
.Example output
[source,yaml]
----
NAMESPACE      NAME             STATE   CONSUMER   ONLINE   ERROR   AGE
baremetal-ns   baremetal-name                      false            50s
----

. Verify that the policy has applied the label `cluster.open-cluster-management.io/backup=cluster-activation` to all these resources, by running the following command:
+
[source,terminal]
----
$ oc get BareMetalHost -A -l infraenvs.agent-install.openshift.io,cluster.open-cluster-management.io/backup=cluster-activation
----
+
.Example output
[source,yaml]
----
NAMESPACE      NAME             STATE   CONSUMER   ONLINE   ERROR   AGE
baremetal-ns   baremetal-name                      false            50s
----
+
The output must show the same list as in the previous step, which listed all `BareMetalHost` resources with the label `infraenvs.agent-install.openshift.io`.
This confirms that all the `BareMetalHost` resources with the `infraenvs.agent-install.openshift.io` label also have the `cluster.open-cluster-management.io/backup: cluster-activation` label.
+
The following example shows a `BareMetalHost` resource with the `infraenvs.agent-install.openshift.io` label.
The resource must also have the `cluster.open-cluster-management.io/backup: cluster-activation` label, which was added by the policy created in step 1.
+
[source,yaml]
----
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  labels:
    cluster.open-cluster-management.io/backup: cluster-activation
    infraenvs.agent-install.openshift.io: value
  name: baremetal-name
  namespace: baremetal-ns
----

You can now use {rh-rhacm-title} to restore a managed cluster.

[IMPORTANT]
====
When you restore `BareMetalHosts` resources as part of restoring the cluster activation data, you must restore the `BareMetalHosts` status.
The following {rh-rhacm} `Restore` resource example restores activation resources, including `BareMetalHosts`, and also restores the status for the `BareMetalHosts` resources:
[source,yaml]
----
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Restore
metadata:
  name: restore-acm-bmh
  namespace: open-cluster-management-backup
spec:
  cleanupBeforeRestore: CleanupRestored
  veleroManagedClustersBackupName: latest <1>
  veleroCredentialsBackupName: latest
  veleroResourcesBackupName: latest
  restoreStatus:
    includedResources:
      - BareMetalHosts<2>
----
====
<1> Set `veleroManagedClustersBackupName: latest` to restore activation resources.
<2> Restores the status for `BareMetalHosts` resources.

[role="_additional-resources"]
.Additional resources

* Restoring managed cluster activation data

* Active-passive configuration

* Restoring activation resources
