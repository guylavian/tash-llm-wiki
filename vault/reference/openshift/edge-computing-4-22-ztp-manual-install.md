---
title: "Manually installing a {sno} cluster with {ztp}"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-manual-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-manual-install
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Manually installing a {sno} cluster with {ztp}

[id="ztp-manual-install"]
= Manually installing a {sno} cluster with {ztp}

You can deploy a managed {sno} cluster by using {rh-rhacm-first} and the assisted service.

[NOTE]
====
If you are creating multiple managed clusters, use the `ClusterInstance` method described in Deploying far edge sites with ZTP.
====

[IMPORTANT]
====
The target bare-metal host must meet the networking, firmware, and hardware requirements listed in Recommended cluster configuration for vDU application workloads.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

[id="ztp-generating-install-and-config-crs-manually_{context}"]
= Extracting reference and example CRs from the ztp-site-generate container

Use the `ztp-site-generate` container to extract reference custom resources (CRs) and example `ClusterInstance` CRs to prepare for cluster installation and Day 2 configuration.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You installed `podman`.

.Procedure

. Create an output folder by running the following command:
+
[source,terminal]
----
$ mkdir -p ./out
----

. Log in to the Ecosystem container registry with your credentials by running the following command:
+
[source,terminal]
----
$ podman login registry.redhat.io
----

. Extract the reference and example CRs from the `ztp-site-generate` container image by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v extract /home/ztp --tar | tar x -C ./out
----
+
The `./out` directory contains the reference `{policy-gen-cr}` and `ClusterInstance` CRs in the `out/argocd/example/` folder.
+
.Example output
[source,terminal]
----
out
 └── argocd
      └── example
           ├── acmpolicygenerator
           │     ├── {policy-prefix}common-ranGen.yaml
           │     ├── {policy-prefix}example-sno-site.yaml
           │     ├── {policy-prefix}group-du-sno-ranGen.yaml
           │     ├── ...
           │     ├── kustomization.yaml
           │     └── ns.yaml
           └── clusterinstance
                 ├── example-sno.yaml
                 ├── example-3node.yaml
                 ├── example-standard.yaml
                 └── ...
----

. Create a `ClusterInstance` CR for your cluster.
+
Use the example `ClusterInstance` CRs in the `out/argocd/example/clusterinstance/` folder that you previously extracted from the `ztp-site-generate` container as a reference. The folder includes example files for single node, three-node, and standard clusters:
+
* `example-sno.yaml`
* `example-3node.yaml`
* `example-standard.yaml`
+
Change the cluster and host details in the example file to match the type of cluster you want to install. For example:
+
.Example {sno} ClusterInstance CR
[source,yaml]
----
----
+
[NOTE]
====
Optional: To provision additional install-time manifests on the provisioned cluster, create the extra manifest CRs and apply them to the hub cluster. Then reference them in the `extraManifestsRefs` field of the `ClusterInstance` CR. For more information, see "Customizing extra installation manifests in the {ztp} pipeline".
====

. Optional: Generate Day 2 configuration CRs from the reference `{policy-gen-cr}` CRs:

.. Create an output folder for the configuration CRs by running the following command:
+
[source,terminal]
----
$ mkdir -p ./ref
----

.. Generate the configuration CRs by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ podman run -it --rm -v `pwd`/out/argocd/example/policygentemplates:/resources:Z -v `pwd`/ref:/output:Z,U registry.redhat.io/openshift4/ztp-site-generate-rhel8:v generator config -N . /output
----
+
The command generates example group and cluster-specific configuration CRs in the `./ref` folder. You can apply these CRs to the cluster after installation is complete.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

[id="ztp-creating-the-site-secrets_{context}"]
= Creating the managed bare-metal host secrets

Add the required `Secret` custom resources (CRs) for the managed bare-metal host to the hub cluster. You need a secret for the {ztp-first} pipeline to access the Baseboard Management Controller (BMC) and a secret for the assisted installer service to pull cluster installation images from the registry.

[NOTE]
====
The secrets are referenced from the `ClusterInstance` CR by name. The namespace
must match the `ClusterInstance` namespace.
====

.Procedure

. Create a YAML secret file containing credentials for the host Baseboard Management Controller (BMC) and a pull secret required for installing OpenShift and all add-on cluster Operators:

.. Save the following YAML as the file `example-sno-secret.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: example-sno-bmc-secret
  namespace: example-sno <1>
data: <2>
  password: <base64_password>
  username: <base64_username>
type: Opaque
---
apiVersion: v1
kind: Secret
metadata:
  name: pull-secret
  namespace: example-sno  <3>
data:
  .dockerconfigjson: <pull_secret> <4>
type: kubernetes.io/dockerconfigjson
----
<1> Must match the namespace configured in the related `ClusterInstance` CR
<2> Base64-encoded values for `password` and `username`
<3> Must match the namespace configured in the related `ClusterInstance` CR
<4> Base64-encoded pull secret

. Add the relative path to `example-sno-secret.yaml` to the `kustomization.yaml` file that you use to install the cluster.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

[id="setting-managed-bare-metal-host-kernel-arguments_{context}"]
= Configuring Discovery ISO kernel arguments for manual installations using {ztp}

The {ztp-first} workflow uses the Discovery ISO as part of the OpenShift Container Platform installation process on managed bare-metal hosts. You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO. This is useful for cluster installations with specific environmental requirements. For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation.

[NOTE]
====
In OpenShift Container Platform , you can only add kernel arguments. You can not replace or delete kernel arguments.
====

.Prerequisites

* You have installed the OpenShift CLI (oc).
* You have logged in to the hub cluster as a user with cluster-admin privileges.
* You have applied a `ClusterInstance` CR to the hub cluster.

.Procedure

. Edit the `spec.kernelArguments` specification in the `InfraEnv` CR to configure kernel arguments:

[source,yaml,options="nowrap",role="white-space-pre"]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: InfraEnv
metadata:
  name: <cluster_name>
  namespace: <cluster_name>
spec:
  kernelArguments:
    - operation: append <1>
      value: audit=0 <2>
    - operation: append
      value: trace=1
  clusterRef:
    name: <cluster_name>
    namespace: <cluster_name>
  pullSecretRef:
    name: pull-secret
----
<1> Specify the append operation to add a kernel argument.
<2> Specify the kernel argument you want to configure. This example configures the audit kernel argument and the trace kernel argument.

[NOTE]
====
The `ClusterInstance` CR generates the `InfraEnv` resource as part of the day-0 installation CRs.
====

.Verification
To verify that the kernel arguments are applied, after the Discovery image verifies that OpenShift Container Platform is ready for installation, you can SSH to the target host before the installation process begins. At that point, you can view the kernel arguments for the Discovery ISO in the `/proc/cmdline` file.

. Begin an SSH session with the target host:
+
[source,terminal]
----
$ ssh -i /path/to/privatekey core@<host_name>
----

. View the system's kernel arguments by using the following command:
+
[source,terminal]
----
$ cat /proc/cmdline
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

[id="ztp-manually-install-a-single-managed-cluster_{context}"]
= Installing a single managed cluster

You can manually deploy a single managed cluster using the assisted service and {rh-rhacm-first}.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have extracted the reference and example CRs from the `ztp-site-generate` container and you configured the `ClusterInstance` CR.

* You have created the baseboard management controller (BMC) `Secret` and the image pull-secret `Secret` custom resources (CRs). See "Creating the managed bare-metal host secrets" for details.

* Your target bare-metal host meets the networking and hardware requirements for managed clusters.

.Procedure

. Create a `ClusterImageSet` for each specific cluster version to be deployed, for example `clusterImageSet-.yaml`. A `ClusterImageSet` has the following format:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hive.openshift.io/v1
kind: ClusterImageSet
metadata:
  name: openshift-.0 <1>
spec:
   releaseImage: quay.io/openshift-release-dev/ocp-release:.0-x86_64 <2>
----
<1> The descriptive version that you want to deploy.
<2> Specifies the `releaseImage` to deploy and determines the operating system image version. The discovery ISO is based on the image version as set by `releaseImage`, or the latest version if the exact version is unavailable.

. Apply the `clusterImageSet` CR:
+
[source,terminal,subs="attributes+"]
----
$ oc apply -f clusterImageSet-.yaml
----

. Create the `Namespace` CR in the `cluster-namespace.yaml` file:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
     name: <cluster_name> <1>
     labels:
        name: <cluster_name> <1>
----
<1>  The name of the managed cluster to provision.

. Apply the `Namespace` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f cluster-namespace.yaml
----

. Apply the `ClusterInstance` CR that you configured to the hub cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f clusterinstance.yaml
----
+
The SiteConfig Operator processes the `ClusterInstance` CR and automatically generates the required installation CRs, including `BareMetalHost`, `AgentClusterInstall`, `ClusterDeployment`, `InfraEnv`, and `NMStateConfig`. The assisted service then begins the cluster installation.

[role="_additional-resources"]
.Additional resources

* BMC addressing

* About root device hints

* {sno-caps} ClusterInstance CR installation reference

* Connectivity prerequisites for managed cluster networks

* Deploying {lvms} on {sno} clusters

* Configuring {lvms} using {policy-gen-cr} CRs

* Configuring managed cluster policies by using PolicyGenerator resources

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

[id="ztp-checking-the-managed-cluster-status_{context}"]
= Monitoring the managed cluster installation status

Ensure that cluster provisioning was successful by checking the cluster status.

.Prerequisites

* All of the custom resources have been configured and provisioned, and the `Agent`
custom resource is created on the hub for the managed cluster.

.Procedure

. Check the status of the managed cluster:
+
[source,terminal]
----
$ oc get managedcluster
----
+
`True` indicates the managed cluster is ready.

. Check the agent status:
+
[source,terminal]
----
$ oc get agent -n <cluster_name>
----

. Use the `describe` command to provide an in-depth description of the agent’s condition. Statuses to be aware of include `BackendError`, `InputError`, `ValidationsFailing`, `InstallationFailed`, and `AgentIsConnected`. These statuses are relevant to the `Agent` and `AgentClusterInstall` custom resources.
+
[source,terminal]
----
$ oc describe agent -n <cluster_name>
----

. Check the cluster provisioning status:
+
[source,terminal]
----
$ oc get agentclusterinstall -n <cluster_name>
----

. Use the `describe` command to provide an in-depth description of the cluster provisioning status:
+
[source,terminal]
----
$ oc describe agentclusterinstall -n <cluster_name>
----

. Check the status of the managed cluster’s add-on services:
+
[source,terminal]
----
$ oc get managedclusteraddon -n <cluster_name>
----

. Retrieve the authentication information of the `kubeconfig` file for the managed cluster:
+
[source,terminal]
----
$ oc get secret -n <cluster_name> <cluster_name>-admin-kubeconfig -o jsonpath={.data.kubeconfig} | base64 -d > <directory>/<cluster_name>-kubeconfig
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

[id="ztp-troubleshooting-the-managed-cluster_{context}"]
= Troubleshooting the managed cluster

Use this procedure to diagnose any installation issues that might occur with the managed cluster.

.Procedure

. Check the status of the managed cluster:
+
[source,terminal]
----
$ oc get managedcluster
----
+
.Example output
[source,terminal]
----
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED   AVAILABLE   AGE
SNO-cluster     true                                   True     True      2d19h
----
+
If the status in the `AVAILABLE` column is `True`, the managed cluster is being managed by the hub.
+
If the status in the `AVAILABLE` column is `Unknown`, the managed cluster is not being managed by the hub.
Use the following steps to continue checking to get more information.

. Check the `AgentClusterInstall` install status:
+
[source,terminal]
----
$ oc get clusterdeployment -n <cluster_name>
----
+
.Example output
[source,terminal]
----
NAME        PLATFORM            REGION   CLUSTERTYPE   INSTALLED    INFRAID    VERSION  POWERSTATE AGE
Sno0026    agent-baremetal                               false                          Initialized
2d14h
----
+
If the status in the `INSTALLED` column is `false`, the installation was unsuccessful.

. If the installation failed, enter the following command to review the status of the `AgentClusterInstall` resource:
+
[source,terminal]
----
$ oc describe agentclusterinstall -n <cluster_name> <cluster_name>
----

. Resolve the errors and reset the cluster:

.. Remove the cluster’s managed cluster resource:
+
[source,terminal]
----
$ oc delete managedcluster <cluster_name>
----
.. Remove the cluster’s namespace:
+
[source,terminal]
----
$ oc delete namespace <cluster_name>
----
+
This deletes all of the namespace-scoped custom resources created for this cluster. You must wait for the `ManagedCluster` CR deletion to complete before proceeding.

.. Recreate the custom resources for the managed cluster.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

[id="ztp-installation-crs_{context}"]
= {rh-rhacm} generated cluster installation CRs reference

{rh-rhacm-first} supports deploying OpenShift Container Platform on single-node clusters, three-node clusters, and standard clusters with a specific set of installation custom resources (CRs) that you generate using `ClusterInstance` CRs for each cluster.

[NOTE]
====
Every managed cluster has its own namespace, and all of the installation CRs except for `ManagedCluster` and `ClusterImageSet` are under that namespace. `ManagedCluster` and `ClusterImageSet` are cluster-scoped, not namespace-scoped. The namespace and the CR names match the cluster name.
====

The following table lists the installation CRs that are automatically applied by the {rh-rhacm} assisted service when it installs clusters using the `ClusterInstance` CRs that you configure.

.Cluster installation CRs generated by {rh-rhacm}
[cols="1,3,3", options="header"]
|===
|CR |Description |Usage

|`BareMetalHost`
|Contains the connection information for the Baseboard Management Controller (BMC) of the target bare-metal host.
|Provides access to the BMC to load and start the discovery image on the target server by using the Redfish protocol.

|`InfraEnv`
|Contains information for installing OpenShift Container Platform on the target bare-metal host.
|Used with `ClusterDeployment` to generate the discovery ISO for the managed cluster.

|`AgentClusterInstall`
|Specifies details of the managed cluster configuration such as networking and the number of control plane nodes. Displays the cluster `kubeconfig` and credentials when the installation is complete.
|Specifies the managed cluster configuration information and provides status during the installation of the cluster.

|`ClusterDeployment`
|References the `AgentClusterInstall` CR to use.
|Used with `InfraEnv` to generate the discovery ISO for the managed cluster.

|`NMStateConfig`
|Provides network configuration information such as `MAC` address to `IP` mapping, DNS server, default route, and other network settings.
|Sets up a static IP address for the managed cluster’s Kube API server.

|`Agent`
|Contains hardware information about the target bare-metal host.
|Created automatically on the hub when the target machine's discovery image boots.

|`ManagedCluster`
|When a cluster is managed by the hub, it must be imported and known. This Kubernetes object provides that interface.
|The hub uses this resource to manage and show the status of managed clusters.

|`KlusterletAddonConfig`
|Contains the list of services provided by the hub to be deployed to the `ManagedCluster` resource.
|Tells the hub which addon services to deploy to the `ManagedCluster` resource.

|`Namespace`
|Logical space for `ManagedCluster` resources existing on the hub. Unique per site.
|Propagates resources to the `ManagedCluster`.

| `Secret`
|Two CRs are created: `BMC Secret` and `Image Pull Secret`.
a| * `BMC Secret` authenticates into the target bare-metal host using its username and password.
* `Image Pull Secret` contains authentication information for the OpenShift Container Platform image installed on the target bare-metal host.

|`ClusterImageSet`
|Contains OpenShift Container Platform image information such as the repository and image name.
|Passed into resources to provide OpenShift Container Platform images.
|===
