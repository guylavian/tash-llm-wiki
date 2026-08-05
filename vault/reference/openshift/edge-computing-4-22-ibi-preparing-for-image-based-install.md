---
title: "Preparing for image-based installation for {sno} clusters"
type: reference
domain: openshift
slug: edge-computing-4-22-ibi-preparing-for-image-based-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ibi-preparing-for-image-based-install
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Preparing for image-based installation for {sno} clusters

[id="ibi-preparing-for-image-based-install"]
= Preparing for image-based installation for {sno} clusters

To prepare for an image-based installation for {sno} clusters, you must complete the following tasks:

* Create a seed image by using the {lcao}.
* Verify that all software components meet the required versions. For further information, see "Software prerequisites for an image-based installation and deployment".

[role="_additional-resources"]
.Additional resources

* Software prerequisites for an image-based installation and deployment

== Installing the {lcao}

Use the {lcao} to generate a seed image from a seed cluster. You can install the {lcao} using the {oc-first} or the web console.

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-installing-lifecycle-agent-using-cli_{context}"]
= Installing the {lcao} by using the CLI

[role="_abstract"]
You can use the OpenShift CLI (`oc`) to install the {lcao}.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. Create a `Namespace` object YAML file for the {lcao}:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-lifecycle-agent
  annotations:
    workload.openshift.io/allowed: management
----

.. Create the `Namespace` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <namespace_filename>.yaml
----

. Create an `OperatorGroup` object YAML file for the {lcao}:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-lifecycle-agent
  namespace: openshift-lifecycle-agent
spec:
  targetNamespaces:
  - openshift-lifecycle-agent
----

.. Create the `OperatorGroup` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <operatorgroup_filename>.yaml
----

. Create a `Subscription` CR for the {lcao}:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-lifecycle-agent-subscription
  namespace: openshift-lifecycle-agent
spec:
  channel: "stable"
  name: lifecycle-agent
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

.. Create the `Subscription` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <subscription_filename>.yaml
----

.Verification

. To verify that the installation succeeded, inspect the CSV resource by running the following command:
+
[source,terminal]
----
$ oc get csv -n openshift-lifecycle-agent
----
+
Example output:
[source,terminal,subs="attributes+"]
----
NAME                              DISPLAY                     VERSION               REPLACES                           PHASE
lifecycle-agent.v.0           Openshift Lifecycle Agent   .0                Succeeded
----

. Verify that the {lcao} is up and running by running the following command:
+
[source,terminal]
----
$ oc get deploy -n openshift-lifecycle-agent
----

+
Example output:
[source,terminal]
----
NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
lifecycle-agent-controller-manager   1/1     1            1           14s
----

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-installing-lifecycle-agent-using-web-console_{context}"]
= Installing the {lcao} by using the web console

[role="_abstract"]
You can use the OpenShift Container Platform web console to install the {lcao}.

.Prerequisites

* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.
. Search for the *{lcao}* from the list of available Operators, and then click *Install*.
. On the *Install Operator* page, under *A specific namespace on the cluster* select *openshift-lifecycle-agent*.
. Click *Install*.

.Verification

. To confirm that the installation is successful:

.. Click *Ecosystem* -> *Installed Operators*.
.. Ensure that the {lcao} is listed in the *openshift-lifecycle-agent* project with a *Status* of *InstallSucceeded*.
+
[NOTE]
====
During installation an Operator might display a *Failed* status. If the installation later succeeds with an *InstallSucceeded* message, you can ignore the *Failed* message.
====

If the Operator is not installed successfully:

. Click *Ecosystem* -> *Installed Operators*, and inspect the *Operator Subscriptions* and *Install Plans* tabs for any failure or errors under *Status*.
. Click *Workloads* -> *Pods*, and check the logs for pods in the *openshift-lifecycle-agent* project.

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-shared-container-partition_{context}"]
= Configuring a shared container partition between ostree stateroots

[role="_abstract"]
[role="_abstract"]
Apply a `MachineConfig` to both the seed and the target clusters during installation time to create a separate partition and share the `/var/lib/containers` partition between the two `ostree` stateroots that will be used during the upgrade process.

[IMPORTANT]
====
You must complete this procedure at installation time.
====

[role="_abstract"]
Apply a `MachineConfig` to the seed cluster to create a separate partition and share the `/var/lib/containers` partition between the two `ostree` stateroots that will be used during the preinstall process.

.Procedure

* Apply a `MachineConfig` to create a separate partition:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 98-var-lib-containers-partitioned
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      disks:
        - device: /dev/disk/by-path/<root_disk>
          partitions:
            - label: var-lib-containers
              startMiB: <start_of_partition>
              sizeMiB: <partition_size>
      filesystems:
        - device: /dev/disk/by-partlabel/var-lib-containers
          format: xfs
          mountOptions:
            - defaults
            - prjquota
          path: /var/lib/containers
          wipeFilesystem: true
    systemd:
      units:
        - contents: |-
            # Generated by Butane
            [Unit]
            Before=local-fs.target
            Requires=systemd-fsck@dev-disk-by\x2dpartlabel-var\x2dlib\x2dcontainers.service
            After=systemd-fsck@dev-disk-by\x2dpartlabel-var\x2dlib\x2dcontainers.service

            [Mount]
            Where=/var/lib/containers
            What=/dev/disk/by-partlabel/var-lib-containers
            Type=xfs
            Options=defaults,prjquota

            [Install]
            RequiredBy=local-fs.target
          enabled: true
          name: var-lib-containers.mount
----
+
where:
+
`<root_disk>`:: Specifies the root disk, for example `pci-0000:01:00.0-scsi-0:2:0:0`.
`<start_of_partition>`:: Specifies the start of the partition in MiB. If the value is too small, the installation will fail.
`<partition_size>`:: Specifies a minimum size for the partition of 500 GB (512000 MiB) to ensure adequate disk space for precached images. If the value is too small, the deployments after installation will fail.

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-seed-image-config_{context}"]
= Seed image configuration

[role="_abstract"]
The seed image targets a set of {sno} clusters with the same hardware and similar configuration.
This means that the seed image must have all of the components and configuration that the seed cluster shares with the target clusters.
Therefore, the seed image generated from the seed cluster cannot contain any cluster-specific configuration.

You can create a seed image from a {sno} cluster with the same hardware as your bare-metal host, and with a similar target cluster configuration. However, the seed image generated from the seed cluster cannot contain any cluster-specific configuration.

The following table lists the components, resources, and configurations that you must and must not include in your seed image:

.Seed image configuration
[cols="2,1", options="header"]
|====
|Cluster configuration
|Include in seed image

|Performance profile
|Yes

|`MachineConfig` resources for the target cluster
|Yes

|IP version configuration, either IPv4, IPv6, or dual-stack networking
|Yes

|Set of Day 2 Operators, including the {lcao} and the {oadp-short} Operator
|Yes

|Disconnected registry configuration ^[2]^
|Yes

|Valid proxy configuration ^[3]^
|Yes

|FIPS configuration
|Yes

|Dedicated partition on the primary disk for container storage that matches the size of the target clusters
|Yes

a|Local volumes

* `StorageClass` used in `LocalVolume` for LSO
* `LocalVolume` for LSO
* `LVMCluster` CR for LVMS
|No
|{oadp-short} `DataProtectionApplication` CR
|No
|====
. If the seed cluster is installed in a disconnected environment, the target clusters must also be installed in a disconnected environment.
. The proxy configuration must be either enabled or disabled in both the seed and target clusters. However, the proxy servers configured on the clusters does not have to match.

[id="ztp-image-based-upgrade-seed-image-config-ran_{context}"]
== Seed image configuration using the RAN DU profile

The following table lists the components, resources, and configurations that you must and must not include in the seed image when using the RAN DU profile:

.Seed image configuration with RAN DU profile
[cols=2*, width="80%", options="header"]
|====
|Resource
|Include in seed image

|All extra manifests that are applied as part of Day 0 installation
|Yes

|All Day 2 Operator subscriptions
|Yes

|`DisableOLMPprof.yaml`
|Yes

|`TunedPerformancePatch.yaml`
|Yes

|`PerformanceProfile.yaml`
|Yes

|`SriovOperatorConfig.yaml`
|Yes

|`DisableSnoNetworkDiag.yaml`
|Yes

|`StorageClass.yaml`
|No, if it is used in `StorageLV.yaml`

|`StorageLV.yaml`
|No

|`StorageLVMCluster.yaml`
|No

|`SriovVrbClusterConfig.yaml`
|Yes

|====

.Seed image configuration with RAN DU profile for extra manifests
[cols=2*, width="80%", options="header"]
|====
|Resource
|Apply as extra manifest

a|`ClusterLogForwarder.yaml`
a|Yes

[NOTE]
====
The DU profile includes the Cluster Logging Operator, but the profile does not configure or apply any Cluster Logging Operator CRs. To enable log forwarding, include the `ClusterLogForwarder.yaml` CR as an extra manifest. The extra manifest is applied to the target {sno} cluster during the image-based upgrade process.
====

|`ReduceMonitoringFootprint.yaml`
|Yes

|`SriovFecClusterConfig.yaml`
|Yes

|`PtpOperatorConfigForEvent.yaml`
|Yes

|`DefaultCatsrc.yaml`
|Yes

|`PtpConfig.yaml`
|If the interfaces of the target cluster are common with the seed cluster, you can include them in the seed image. Otherwise, apply it as extra manifests.

a|`SriovNetwork.yaml`
`SriovNetworkNodePolicy.yaml`
|If the configuration, including namespaces, is exactly the same on both the seed and target cluster, you can include them in the seed image. Otherwise, apply them as extra manifests.
|====

The following list of resources and configurations can be applied as extra manifests or by using {rh-rhacm} policies:

* `ClusterLogForwarder.yaml`
* `ReduceMonitoringFootprint.yaml`
* `SriovFecClusterConfig.yaml`
* `PtpOperatorConfigForEvent.yaml`
* `DefaultCatsrc.yaml`
* `PtpConfig.yaml`
* `SriovNetwork.yaml`

[IMPORTANT]
====
If you are using {ztp}, enable these resources by using {rh-rhacm} policies to ensure configuration changes can be applied throughout the cluster lifecycle.
====

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-generate-seed-image_{context}"]
= Generating a seed image with the {lcao}

[role="_abstract"]
Use the {lcao} to generate a seed image from a managed cluster. The Operator checks for required system configurations, performs any necessary system cleanup before generating the seed image, and launches the image generation. The seed image generation includes the following tasks:

* Stopping cluster Operators
* Preparing the seed image configuration
* Generating and pushing the seed image to the image repository specified in the `SeedGenerator` CR
* Restoring cluster Operators
* Expiring seed cluster certificates
* Generating new certificates for the seed cluster
* Restoring and updating the `SeedGenerator` CR on the seed cluster

.Prerequisites

* {rh-rhacm} and {mce} are not installed on the seed cluster.
* You have configured a shared container directory on the seed cluster.
* You have installed the minimum version of the {oadp-short} Operator and the {lcao} on the seed cluster.
* Ensure that persistent volumes are not configured on the seed cluster.
* Ensure that the `LocalVolume` CR does not exist on the seed cluster if the Local Storage Operator is used.
* Ensure that the `LVMCluster` CR does not exist on the seed cluster if {lvms} is used.
* Ensure that the `DataProtectionApplication` CR does not exist on the seed cluster if {oadp-short} is used.

.Procedure

. Detach the managed cluster from the hub to delete any {rh-rhacm}-specific resources from the seed cluster that must not be in the seed image:
+
.. Manually detach the seed cluster by running the following command:
+
[source,terminal]
----
$ oc delete managedcluster sno-worker-example
----
+
... Wait until the managed cluster is removed. After the cluster is removed, create the proper `SeedGenerator` CR. The {lcao} cleans up the {rh-rhacm} artifacts.
+
.. If you are using {ztp}, detach your cluster by removing the seed cluster's `ClusterInstance` CR from the `kustomization.yaml`.
+
... If you have a `kustomization.yaml` file that references multiple `ClusterInstance` CRs, remove your seed cluster's `ClusterInstance` CR from the `kustomization.yaml`:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
#- clusterinstance-seed-sno1.yaml
- clusterinstance-target-sno2.yaml
- clusterinstance-target-sno3.yaml
----
+
... If you have a `kustomization.yaml` that references one `ClusterInstance` CR, remove your seed cluster's `ClusterInstance` CR from the `kustomization.yaml` and add the `resources: []` line:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources: []
----
+
... Commit the `kustomization.yaml` changes in your Git repository and push the changes to your repository.
+
The ArgoCD pipeline detects the changes and removes the managed cluster.

. Create the `Secret` object so that you can push the seed image to your registry.
+
.. Create the authentication file by running the following commands:
+
[source,terminal]
----
$ MY_USER=myuserid
----
+
[source,terminal]
----
$ AUTHFILE=/tmp/my-auth.json
----
+
[source,terminal]
----
$ podman login --authfile ${AUTHFILE} -u ${MY_USER} quay.io/${MY_USER}
----
+
[source,terminal]
----
$ base64 -w 0 ${AUTHFILE} ; echo
----
+
.. Copy the output into the `seedAuth` field in the `Secret` YAML file named `seedgen` in the `openshift-lifecycle-agent` namespace:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <secret_name>
  namespace: openshift-lifecycle-agent
type: Opaque
data:
  seedAuth: <encoded_authfile>
----
+
where:
+
`<secret_name>`:: Specifies the name of the `Secret` resource. The value must be `seedgen`.
`<encoded_authfile>`:: Specifies a base64-encoded authfile for write-access to the registry for pushing the generated seed images.
+
.. Apply the `Secret` by running the following command:
+
[source,terminal]
----
$ oc apply -f secretseedgenerator.yaml
----

. Create the `SeedGenerator` CR:
+
[source,yaml]
----
apiVersion: lca.openshift.io/v1
kind: SeedGenerator
metadata:
  name: <seedgenerator_name>
spec:
  seedImage: <seed_container_image>
----
+
where:
+
`<seedgenerator_name>`:: Specifies the name of the `SeedGenerator` CR. The value must be `seedimage`.
`<seed_container_image>`:: Specifies the container image URL, for example, `quay.io/example/seed-container-image:<tag>`. It is recommended to use the `<seed_cluster_name>:<ocp_version>` format.

. Generate the seed image by running the following command:
+
[source,terminal]
----
$ oc apply -f seedgenerator.yaml
----
+
[IMPORTANT]
====
The cluster reboots and loses API capabilities while the {lcao} generates the seed image.
Applying the `SeedGenerator` CR stops the `kubelet` and the CRI-O operations, then it starts the image generation.
====

.Next steps

If you want to generate more seed images, you must provision a new seed cluster with the version that you want to generate a seed image from.

.Verification

* After the cluster recovers and it is available, you can check the status of the `SeedGenerator` CR by running the following command:
+
[source,terminal]
----
$ oc get seedgenerator -o yaml
----
+
The following example shows the output when the seed image generation is complete:
+
[source,yaml]
----
status:
  conditions:
  - lastTransitionTime: "2024-02-13T21:24:26Z"
    message: Seed Generation completed
    observedGeneration: 1
    reason: Completed
    status: "False"
    type: SeedGenInProgress
  - lastTransitionTime: "2024-02-13T21:24:26Z"
    message: Seed Generation completed
    observedGeneration: 1
    reason: Completed
    status: "True"
    type: SeedGenCompleted
  observedGeneration: 1
----
