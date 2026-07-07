---
title: "Installing managed clusters with {rh-rhacm} and ClusterInstance resources"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-deploying-far-edge-sites
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Installing managed clusters with {rh-rhacm} and ClusterInstance resources

[id="ztp-deploying-far-edge-sites"]
= Installing managed clusters with {rh-rhacm} and ClusterInstance resources

You can provision OpenShift Container Platform clusters at scale with {rh-rhacm-first} using the assisted service and the GitOps plugin policy generator with core-reduction technology enabled. The {ztp-first} pipeline performs the cluster installations. {ztp} can be used in a disconnected environment.

[role="_additional-resources"]
.Additional resources

* Configuring managed cluster policies by using PolicyGenerator resources

* Comparing {rh-rhacm} PolicyGenerator and PolicyGenTemplate resource patching

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-talo-integration_{context}"]
= {ztp} and {cgu-operator-full}

{ztp-first} generates installation and configuration CRs from manifests stored in Git. These artifacts are applied to a centralized hub cluster where {rh-rhacm-first}, the assisted service, and the {cgu-operator-first} use the CRs to install and configure the managed cluster. The configuration phase of the {ztp} pipeline uses the {cgu-operator} to orchestrate the application of the configuration CRs to the cluster. There are several key integration points between {ztp} and the {cgu-operator}.

Inform policies::
By default, {ztp} creates all policies with a remediation action of `inform`. These policies cause {rh-rhacm} to report on compliance status of clusters relevant to the policies but does not apply the desired configuration. During the {ztp} process, after OpenShift installation, the {cgu-operator} steps through the created `inform` policies and enforces them on the target managed cluster(s). This applies the configuration to the managed cluster. Outside of the {ztp} phase of the cluster lifecycle, this allows you to change policies without the risk of immediately rolling those changes out to affected managed clusters. You can control the timing and the set of remediated clusters by using {cgu-operator}.

Automatic creation of ClusterGroupUpgrade CRs::
To automate the initial configuration of newly deployed clusters, {cgu-operator} monitors the state of all `ManagedCluster` CRs on the hub cluster. Any `ManagedCluster` CR that does not have a `ztp-done` label applied, including newly created `ManagedCluster` CRs, causes the {cgu-operator} to automatically create a `ClusterGroupUpgrade` CR with the following characteristics:

* The `ClusterGroupUpgrade` CR is created and enabled in the `ztp-install` namespace.
* `ClusterGroupUpgrade` CR has the same name as the `ManagedCluster` CR.
* The cluster selector includes only the cluster associated with that `ManagedCluster` CR.
* The set of managed policies includes all policies that {rh-rhacm} has bound to the cluster at the time the `ClusterGroupUpgrade` is created.
* Pre-caching is disabled.
* Timeout set to 4 hours (240 minutes).

+
The automatic creation of an enabled `ClusterGroupUpgrade` ensures that initial zero-touch deployment of clusters proceeds without the need for user intervention. Additionally, the automatic creation of a `ClusterGroupUpgrade` CR for any `ManagedCluster` without the `ztp-done` label allows a failed {ztp} installation to be restarted by simply deleting the `ClusterGroupUpgrade` CR for the cluster.

Waves::
Each policy generated from a `PolicyGenerator` or `PolicyGentemplate` CR includes a `ztp-deploy-wave` annotation. This annotation is based on the same annotation from each CR which is included in that policy. The wave annotation is used to order the policies in the auto-generated `ClusterGroupUpgrade` CR. The wave annotation is not used other than for the auto-generated `ClusterGroupUpgrade` CR.
+
[NOTE]
====
All CRs in the same policy must have the same setting for the `ztp-deploy-wave` annotation. The default value of this annotation for each CR can be overridden in the `PolicyGenerator` or `PolicyGentemplate`. The wave annotation in the source CR is used for determining and setting the policy wave annotation. This annotation is removed from each built CR which is included in the generated policy at runtime.
====
+
The {cgu-operator} applies the configuration policies in the order specified by the wave annotations. The {cgu-operator} waits for each policy to be compliant before moving to the next policy. It is important to ensure that the wave annotation for each CR takes into account any prerequisites for those CRs to be applied to the cluster. For example, an Operator must be installed before or concurrently with the configuration for the Operator. Similarly, the `CatalogSource` for an Operator must be installed in a wave before or concurrently with the Operator Subscription. The default wave value for each CR takes these prerequisites into account.
+
[NOTE]
====
Multiple CRs and policies can share the same wave number. Having fewer policies can result in faster deployments and lower CPU usage. It is a best practice to group many CRs into relatively few waves.
====
+
To check the default wave value in each source CR, run the following command against the `out/source-crs` directory that is extracted from the `ztp-site-generate` container image:
+
[source,terminal]
----
$ grep -r "ztp-deploy-wave" out/source-crs
----

Phase labels::
The `ClusterGroupUpgrade` CR is automatically created and includes directives to annotate the `ManagedCluster` CR with labels at the start and end of the {ztp} process.
+
When {ztp} configuration postinstallation commences, the `ManagedCluster` has the `ztp-running` label applied. When all policies are remediated to the cluster and are fully compliant, these directives cause the {cgu-operator} to remove the `ztp-running` label and apply the `ztp-done` label.
+
For deployments that make use of the `informDuValidator` policy, the `ztp-done` label is applied when the cluster is fully ready for deployment of applications. This includes all reconciliation and resulting effects of the {ztp} applied configuration CRs. The `ztp-done` label affects automatic `ClusterGroupUpgrade` CR creation by {cgu-operator}. Do not manipulate this label after the initial {ztp} installation of the cluster.

Linked CRs::
The automatically created `ClusterGroupUpgrade` CR has the owner reference set as the `ManagedCluster` from which it was derived. This reference ensures that deleting the `ManagedCluster` CR causes the instance of the `ClusterGroupUpgrade` to be deleted along with any supporting resources.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-ztp-building-blocks_{context}"]
= Overview of deploying managed clusters with {ztp}

{rh-rhacm-first} uses {ztp-first} to deploy single-node OpenShift Container Platform clusters, three-node clusters, and standard clusters. You manage site configuration data as OpenShift Container Platform custom resources (CRs) in a Git repository. {ztp} uses a declarative GitOps approach for a develop once, deploy anywhere model to deploy the managed clusters.

The deployment of the clusters includes:

* Installing the host operating system (RHCOS) on a blank server

* Deploying OpenShift Container Platform

* Creating cluster policies and site subscriptions

* Making the necessary network configurations to the server operating system

* Deploying profile Operators and performing any needed software-related configuration, such as performance profile, PTP, and SR-IOV

[id="ztp-overview-managed-site-installation-process_{context}"]
== Overview of the managed site installation process

After you apply the managed site custom resources (CRs) on the hub cluster, the following actions happen automatically:

. A Discovery image ISO file is generated and booted on the target host.

. When the ISO file successfully boots on the target host it reports the host hardware information to {rh-rhacm}.

. After all hosts are discovered, OpenShift Container Platform is installed.

. When OpenShift Container Platform finishes installing, the hub installs the `klusterlet` service on the target cluster.

. The requested add-on services are installed on the target cluster.

The Discovery image ISO process is complete when the `Agent` CR  for the managed cluster is created on the hub cluster.

[IMPORTANT]
====
The target bare-metal host must meet the networking, firmware, and hardware requirements listed in Recommended {sno} cluster configuration for vDU application workloads.
====

[NOTE]
====
To deploy clusters with virtualized control planes running on {VirtProductName} VMs instead of physical servers, you can use KubeVirt Redfish to expose VMs as Redfish endpoints.
For more information about using virtualized control planes, see "Understanding virtualized control planes".
====

[role="_additional-resources"]
.Additional resources

* Understanding virtualized control planes for setup instructions

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
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc
[id="setting-managed-bare-metal-host-kernel-arguments_{context}"]
= Configuring Discovery ISO kernel arguments for installations using {ztp}

The {ztp-first} workflow uses the Discovery ISO as part of the OpenShift Container Platform installation process on managed bare-metal hosts. You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO. This is useful for cluster installations with specific environmental requirements.

For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation.

[NOTE]
====
In OpenShift Container Platform , you can only add kernel arguments. You can not replace or delete kernel arguments.
====

.Prerequisites

* You have installed the OpenShift CLI (oc).
* You have logged in to the hub cluster as a user with cluster-admin privileges.

.Procedure

. Create the `InfraEnv` CR and edit the `spec.kernelArguments` specification to configure kernel arguments.

.. Save the following YAML in an `InfraEnv-example.yaml` file:
+
[NOTE]
====
The `InfraEnv` CR in this example uses template syntax such as `{{ .Cluster.ClusterName }}` that is populated based on values in the `ClusterInstance` CR. The `ClusterInstance` CR automatically populates values for these templates during deployment. Do not edit the templates manually.
====
+
[source,yaml]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: InfraEnv
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"
  name: "{{ .Cluster.ClusterName }}"
  namespace: "{{ .Cluster.ClusterName }}"
spec:
  clusterRef:
    name: "{{ .Cluster.ClusterName }}"
    namespace: "{{ .Cluster.ClusterName }}"
  kernelArguments:
    - operation: append <1>
      value: audit=0 <2>
    - operation: append
      value: trace=1
  sshAuthorizedKey: "{{ .Site.SshPublicKey }}"
  proxy: "{{ .Cluster.ProxySettings }}"
  pullSecretRef:
    name: "{{ .Site.PullSecretRef.Name }}"
  ignitionConfigOverride: "{{ .Cluster.IgnitionConfigOverride }}"
  nmStateConfigLabelSelector:
    matchLabels:
      nmstate-label: "{{ .Cluster.ClusterName }}"
  additionalNTPSources: "{{ .Cluster.AdditionalNTPSources }}"
----
<1> Specify the append operation to add a kernel argument.
<2> Specify the kernel argument you want to configure. This example configures the audit kernel argument and the trace kernel argument.

. Commit the `InfraEnv-example.yaml` file to your Git repository and push your changes. The following example shows a sample Git repository structure:
+
[source,text]
----
~/example-ztp/install
          └── site-install
               ├── clusterinstance-example.yaml
               ├── InfraEnv-example.yaml
               └── kustomization.yaml
----

. Update the `kustomization.yaml` file to use the `configMapGenerator` field to package the `InfraEnv` CR into a `ConfigMap`:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - clusterinstance-example.yaml <1>
configMapGenerator:
  - name: custom-infraenv-cm <2>
    namespace: example-cluster <3>
    files:
      - InfraEnv-example.yaml
generatorOptions:
  disableNameSuffixHash: true
----
<1> The name of the `ClusterInstance` CR.
<2> The name of the `ConfigMap` that contains the custom `InfraEnv` CR.
<3> The namespace must match the `ClusterInstance` namespace.

. In your `ClusterInstance` CR, reference the `ConfigMap` in the `spec.templateRefs` field:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "example-cluster"
  namespace: "example-cluster"
spec:
  clusterName: "example-cluster"
  templateRefs:
    - name: custom-infraenv-cm <1>
      namespace: example-cluster
# ...
----
<1> Reference to the `ConfigMap` CR that contains the custom `InfraEnv` CR template.

. Commit the `ClusterInstance` CR and `kustomization.yaml` to your Git repository and push your changes.
+
When the Argo CD pipeline syncs the changes, the SiteConfig Operator uses the custom `InfraEnv-example` CR from the generated `ConfigMap` to configure the infrastructure environment, including the custom kernel arguments.

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
// * edge_computing/ztp-deploying-far-edge-sites.adoc

[id="ztp-deploying-a-site_{context}"]
= Deploying a managed cluster with ClusterInstance and {ztp}

Use the following procedure to create a `ClusterInstance` custom resource (CR) and related files and initiate the {ztp-first} cluster deployment.

[NOTE]
====
You require {rh-rhacm-first} version 2.12 or later to install the SiteConfig Operator and use the `ClusterInstance` CR.
====

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You installed the SiteConfig Operator in the hub cluster.

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You configured the hub cluster for generating the required installation and policy CRs.

* You created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and you must configure it as a source repository for the ArgoCD application. See "Preparing the {ztp} site configuration repository" for more information.
+
[NOTE]
====
When you create the source repository, ensure that you patch the ArgoCD application with the `argocd/deployment/argocd-openshift-gitops-patch.json` patch-file that you extract from the `ztp-site-generate` container. See "Configuring the hub cluster with ArgoCD".
====

* To be ready for provisioning managed clusters, you require the following for each bare-metal host:
+
Network connectivity:: Your network requires DNS. Managed cluster hosts should be reachable from the hub cluster. Ensure that Layer 3 connectivity exists between the hub cluster and the managed cluster host.
+
Baseboard Management Controller (BMC) details:: {ztp} uses BMC username and password details to connect to the BMC during cluster installation. The {ztp} plugin manages the `ManagedCluster` CRs on the hub cluster based on the `ClusterInstance` CR in your site Git repo. You create individual `BMCSecret` CRs for each host manually.

.Procedure

. Create the required managed cluster secrets on the hub cluster. These resources must be in a namespace with a name matching the cluster name. For example, in `out/argocd/example/clusterinstance/example-sno.yaml`, the cluster name and namespace is `example-sno`.

.. Export the cluster namespace by running the following command:
+
[source,terminal]
----
$ export CLUSTERNS=example-sno
----

.. Create the namespace:
+
[source,terminal]
----
$ oc create namespace $CLUSTERNS
----

. Create pull secret and BMC `Secret` CRs for the managed cluster. The pull secret must contain all the credentials necessary for installing OpenShift Container Platform and all required Operators. See "Creating the managed bare-metal host secrets" for more information.
+
[NOTE]
====
The secrets are referenced from the `ClusterInstance` custom resource (CR) by name. The namespace must match the `ClusterInstance` namespace.
====

. Create a `ClusterInstance` CR for your cluster in your local clone of the Git repository:

.. Choose the appropriate example for your CR from the  `out/argocd/example/clusterinstance/` folder.
The folder includes example files for single node, three-node, and standard clusters:
+
*** `example-sno.yaml`
*** `example-3node.yaml`
*** `example-standard.yaml`

.. Change the cluster and host details in the example file to match the type of cluster you want. For example:
+
.Example {sno} ClusterInstance CR
[source,yaml]
----
----
+
[NOTE]
====
For more information about BMC addressing, see the "Additional resources" section. The `installConfigOverrides` and  `ignitionConfigOverride` fields are expanded in the example for ease of readability.
====
+
[NOTE]
====
To override the default `BareMetalHost` CR for a node, create a custom node template in a `ConfigMap` and reference it in the node-level `spec.nodes.templateRefs` field in the `ClusterInstance` CR. Ensure that you set the `argocd.argoproj.io/sync-wave: "3"` annotation in your override `BareMetalHost` CR.
====

.. You can inspect the default set of extra-manifest `MachineConfig` CRs in `out/argocd/extra-manifest`. It is automatically applied to the cluster when it is installed.

.. Optional: To provision additional install-time manifests on the provisioned cluster, package your extra manifest CRs in a `ConfigMap` and reference it in the `extraManifestsRefs` field of the `ClusterInstance` CR. For more information, see "Customizing extra installation manifests in the {ztp} pipeline".
+
[IMPORTANT]
====
For optimal cluster performance, enable crun for master and worker nodes in {sno}, {sno} with additional worker nodes, {3no}, and standard clusters.

Enable crun in a `ContainerRuntimeConfig` CR as an additional Day 0 install-time manifest to avoid the cluster having to reboot.

The `enable-crun-master.yaml` and `enable-crun-worker.yaml` CR files are in the `out/source-crs/optional-extra-manifest/` folder that you can extract from the `ztp-site-generate` container.
====

. Add the `ClusterInstance` CR to the `kustomization.yaml` file in the `generators` section, similar to the example shown in `out/argocd/example/clusterinstance/kustomization.yaml`.

. Commit the `ClusterInstance` CR and associated `kustomization.yaml` changes in your Git repository and push the changes.
+
The ArgoCD pipeline detects the changes and begins the managed cluster deployment.

.Verification

* Verify that the custom roles and labels are applied after the node is deployed:
+
[source,terminal]
----
$ oc describe node example-node.example.com
----

.Example output
[source,terminal]
----
Name:   example-node.example.com
Roles:  control-plane,example-label,master,worker
Labels: beta.kubernetes.io/arch=amd64
        beta.kubernetes.io/os=linux
        custom-label/parameter1=true
        kubernetes.io/arch=amd64
        kubernetes.io/hostname=cnfdf03.telco5gran.eng.rdu2.redhat.com
        kubernetes.io/os=linux
        node-role.kubernetes.io/control-plane=
        node-role.kubernetes.io/example-label= <1>
        node-role.kubernetes.io/master=
        node-role.kubernetes.io/worker=
        node.openshift.io/os_id=rhcos
----
<1> The custom label is applied to the node.

[role="_additional-resources"]
.Additional resources

* {sno-caps} ClusterInstance CR installation reference

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-install-ztp.adoc

[id="ztp-configuring-ipsec-using-ztp-and-siteconfig_{context}"]
= Configuring IPsec encryption for {sno} clusters using {ztp} and ClusterInstance resources

You can enable IPsec encryption in managed {sno} clusters that you install using {ztp} and {rh-rhacm-first}.
You can encrypt traffic between the managed cluster and IPsec endpoints external to the managed cluster. All network traffic between nodes on the OVN-Kubernetes cluster network is encrypted with IPsec in Transport mode.

[IMPORTANT]
====
You can also configure IPsec encryption for {sno} clusters with an additional worker node by following this procedure. It is recommended to use the `MachineConfig` custom resource (CR) to configure IPsec encryption for {sno} clusters and {sno} clusters with an additional worker node because of their low resource availability.
====

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have installed the SiteConfig Operator in the hub cluster.

* You have configured {rh-rhacm} and the hub cluster for generating the required installation and policy custom resources (CRs) for managed clusters.

* You have created a Git repository where you manage your custom site configuration data.
The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

* You have installed the `butane` utility version 0.20.0 or later.

* You have a PKCS#12 certificate for the IPsec endpoint and a CA cert in PEM format.

.Procedure

. Extract the latest version of the `ztp-site-generate` container source and merge it with your repository where you manage your custom site configuration data.

. Configure `optional-extra-manifest/ipsec/ipsec-endpoint-config.yaml` with the required values that configure IPsec in the cluster. For example:
+
[source,yaml]
----
interfaces:
- name: hosta_conn
  type: ipsec
  libreswan:
    left: '%defaultroute'
    leftid: '%fromcert'
    leftmodecfgclient: false
    leftcert: left_server <1>
    leftrsasigkey: '%cert'
    right: <external_host> <2>
    rightid: '%fromcert'
    rightrsasigkey: '%cert'
    rightsubnet: <external_address> <3>
    ikev2: insist <4>
    type: tunnel
----
<1> The value of this field must match with the name of the certificate used on the remote system.
<2> Replace `<external_host>` with the external host IP address or DNS hostname.
<3> Replace `<external_address>` with the IP subnet of the external host on the other side of the IPsec tunnel.
<4> Use the IKEv2 VPN encryption protocol only. Do not use IKEv1, which is deprecated.

. Add the following certificates to the `optional-extra-manifest/ipsec` folder:

** `left_server.p12`: The certificate bundle for the IPsec endpoints

** `ca.pem`: The certificate authority that you signed your certificates with
+
The certificate files are required for the Network Security Services (NSS) database on each host. These files are imported as part of the Butane configuration in later steps.

. Open a shell prompt at the `optional-extra-manifest/ipsec` folder of the Git repository where you maintain your custom site configuration data.

. Run the `optional-extra-manifest/ipsec/build.sh` script to generate the required Butane and `MachineConfig` CRs files.
+
If the PKCS#12 certificate is protected with a password, set the `-W` argument.
+
.Example output
[source,terminal]
----
out
 └── argocd
      └── example
           └── optional-extra-manifest
                └── ipsec
                     ├── 99-ipsec-master-endpoint-config.bu <1>
                     ├── 99-ipsec-master-endpoint-config.yaml <1>
                     ├── 99-ipsec-worker-endpoint-config.bu <1>
                     ├── 99-ipsec-worker-endpoint-config.yaml <1>
                     ├── build.sh
                     ├── ca.pem <2>
                     ├── left_server.p12 <2>
                     ├── enable-ipsec.yaml
                     ├── ipsec-endpoint-config.yml
                     └── README.md
----
<1> The `ipsec/build.sh` script generates the Butane and endpoint configuration CRs.
<2> You provide `ca.pem` and `left_server.p12` certificate files that are relevant to your network.

. Create an `ipsec-manifests/` folder in the repository where you manage your custom site configuration data.
Add the `enable-ipsec.yaml` and `99-ipsec-*` YAML files to the directory.
For example:
+
[source,terminal]
----
site-configs/
  ├── hub-1/
  │   └── clusterinstance-site1-sno-du.yaml
  ├── ipsec-manifests/
  │   ├── enable-ipsec.yaml
  │   ├── 99-ipsec-worker-endpoint-config.yaml
  │   └── 99-ipsec-master-endpoint-config.yaml
  └── kustomization.yaml
----

. Create a `kustomization.yaml` file that uses `configMapGenerator` to package your IPsec manifests into a `ConfigMap`:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - hub-1/clusterinstance-site1-sno-du.yaml
configMapGenerator:
  - name: ipsec-manifests-cm
    namespace: site1-sno-du <1>
    files:
      - ipsec-manifests/enable-ipsec.yaml
      - ipsec-manifests/99-ipsec-master-endpoint-config.yaml
      - ipsec-manifests/99-ipsec-worker-endpoint-config.yaml
generatorOptions:
  disableNameSuffixHash: true <2>
----
<1> The namespace must match the `ClusterInstance` namespace.
<2> Disables the hash suffix so the `ConfigMap` name is predictable.

. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  clusterName: "site1-sno-du"
  networkType: "OVNKubernetes"
  extraManifestsRefs:
    - name: ipsec-manifests-cm <1>
# ...
----
<1> Reference to the `ConfigMap` containing the IPsec manifests.
+
[NOTE]
====
If you have other extra manifests, you can either include them in the same `ConfigMap` or create multiple `ConfigMap` resources and reference each of those in the `extraManifestsRefs` field.
====

. Commit the `ClusterInstance` CR, IPsec manifest files, and `kustomization.yaml` changes in your Git repository and push the changes to provision the managed cluster and configure IPsec encryption.
+
The Argo CD pipeline detects the changes and begins the managed cluster deployment.
+
During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests.

.Verification

For information about verifying the IPsec encryption, see "Verifying the IPsec encryption".

[role="_additional-resources"]
.Additional resources

* Verifying the IPsec encryption

* Configuring IPsec encryption

* Encryption protocol and IPsec mode

* Installing managed clusters with {rh-rhacm} and ClusterInstance resources

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-install-ztp.adoc

[id="ztp-configuring-ipsec-using-ztp-and-siteconfig-for-mno_{context}"]
= Configuring IPsec encryption for multi-node clusters using {ztp} and ClusterInstance resources

You can enable IPsec encryption in managed multi-node clusters that you install using {ztp} and {rh-rhacm-first}.
You can encrypt traffic between the managed cluster and IPsec endpoints external to the managed cluster. All network traffic between nodes on the OVN-Kubernetes cluster network is encrypted with IPsec in Transport mode.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have installed the SiteConfig Operator in the hub cluster.

* You have configured {rh-rhacm} and the hub cluster for generating the required installation and policy custom resources (CRs) for managed clusters.

* You have created a Git repository where you manage your custom site configuration data.
The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

* You have installed the `butane` utility version 0.20.0 or later.

* You have a PKCS#12 certificate for the IPsec endpoint and a CA cert in PEM format.

* You have installed the NMState Operator.

.Procedure

. Extract the latest version of the `ztp-site-generate` container source and merge it with your repository where you manage your custom site configuration data.

. Configure the `optional-extra-manifest/ipsec/ipsec-config-policy.yaml` file with the required values that configure IPsec in the cluster.
+
.`ConfigurationPolicy` object for creating an IPsec configuration
[source,yaml]
----
apiVersion: policy.open-cluster-management.io/v1
kind: ConfigurationPolicy
metadata:
  name: policy-config
spec:
  namespaceSelector:
    include: ["default"]
    exclude: []
    matchExpressions: []
    matchLabels: {}
  remediationAction: inform
  severity: low
  evaluationInterval:
    compliant:
    noncompliant:
  object-templates-raw: |
    {{- range (lookup "v1" "Node" "" "").items }}
    - complianceType: musthave
      objectDefinition:
        kind: NodeNetworkConfigurationPolicy
        apiVersion: nmstate.io/v1
        metadata:
          name: {{ .metadata.name }}-ipsec-policy
        spec:
          nodeSelector:
            kubernetes.io/hostname: {{ .metadata.name }}
          desiredState:
            interfaces:
            - name: hosta_conn
              type: ipsec
              libreswan:
                left: '%defaultroute'
                leftid: '%fromcert'
                leftmodecfgclient: false
                leftcert: left_server <1>
                leftrsasigkey: '%cert'
                right: <external_host> <2>
                rightid: '%fromcert'
                rightrsasigkey: '%cert'
                rightsubnet: <external_address> <3>
                ikev2: insist <4>
                type: tunnel
----
<1> The value of this field must match with the name of the certificate used on the remote system.
<2> Replace `<external_host>` with the external host IP address or DNS hostname.
<3> Replace `<external_address>` with the IP subnet of the external host on the other side of the IPsec tunnel.
<4> Use the IKEv2 VPN encryption protocol only. Do not use IKEv1, which is deprecated.

. Add the following certificates to the `optional-extra-manifest/ipsec` folder:

** `left_server.p12`: The certificate bundle for the IPsec endpoints

** `ca.pem`: The certificate authority that you signed your certificates with
+
The certificate files are required for the Network Security Services (NSS) database on each host. These files are imported as part of the Butane configuration in later steps.

. Open a shell prompt at the `optional-extra-manifest/ipsec` folder of the Git repository where you maintain your custom site configuration data.

. Run the `optional-extra-manifest/ipsec/import-certs.sh` script to generate the required Butane and `MachineConfig` CRs to import the external certs.
+
If the PKCS#12 certificate is protected with a password, set the `-W` argument.
+
.Example output
[source,terminal]
----
out
 └── argocd
      └── example
           └── optional-extra-manifest
                └── ipsec
                     ├── 99-ipsec-master-import-certs.bu <1>
                     ├── 99-ipsec-master-import-certs.yaml <1>
                     ├── 99-ipsec-worker-import-certs.bu <1>
                     ├── 99-ipsec-worker-import-certs.yaml <1>
                     ├── import-certs.sh
                     ├── ca.pem <2>
                     ├── left_server.p12 <2>
                     ├── enable-ipsec.yaml
                     ├── ipsec-config-policy.yaml
                     └── README.md
----
<1> The `ipsec/import-certs.sh` script generates the Butane and endpoint configuration CRs.
<2> Add the `ca.pem` and `left_server.p12` certificate files that are relevant to your network.

. Create an `ipsec-manifests/` folder in the repository where you manage your custom site configuration data and add the `enable-ipsec.yaml` and `99-ipsec-*` YAML files to the directory.
+
.Example site configuration directory
[source,terminal]
----
site-configs/
  ├── hub-1/
  │   └── clusterinstance-site1-mno-du.yaml
  ├── ipsec-manifests/
  │   ├── enable-ipsec.yaml
  │   ├── 99-ipsec-master-import-certs.yaml
  │   └── 99-ipsec-worker-import-certs.yaml
  └── kustomization.yaml
----

. Create a `kustomization.yaml` file that uses `configMapGenerator` to package your IPsec manifests into a `ConfigMap`:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - hub-1/clusterinstance-site1-mno-du.yaml
configMapGenerator:
  - name: ipsec-manifests-cm
    namespace: site1-mno-du <1>
    files:
      - ipsec-manifests/enable-ipsec.yaml
      - ipsec-manifests/99-ipsec-master-import-certs.yaml
      - ipsec-manifests/99-ipsec-worker-import-certs.yaml
generatorOptions:
  disableNameSuffixHash: true <2>
----
<1> The namespace must match the `ClusterInstance` namespace.
<2> Disables the hash suffix so the `ConfigMap` name is predictable.

. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-mno-du"
  namespace: "site1-mno-du"
spec:
  clusterName: "site1-mno-du"
  networkType: "OVNKubernetes"
  extraManifestsRefs:
    - name: ipsec-manifests-cm <1>
# ...
----
<1> Reference to the `ConfigMap` containing the IPsec certificate import manifests.
+
[NOTE]
====
If you have other extra manifests, you can either include them in the same `ConfigMap` or create multiple `ConfigMap` resources and reference them all in `extraManifestsRefs`.
====

. Include the `ipsec-config-policy.yaml` config policy file in the `source-crs` directory in GitOps and reference the file in one of the `PolicyGenerator` CRs.

. Commit the `ClusterInstance` CR, IPsec manifest files, and `kustomization.yaml` changes in your Git repository and push the changes to provision the managed cluster and configure IPsec encryption.
+
The Argo CD pipeline detects the changes and begins the managed cluster deployment.
+
During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests. The IPsec configuration policy is applied as a Day 2 operation after the cluster is provisioned.

.Verification

For information about verifying the IPsec encryption, see "Verifying the IPsec encryption".

[role="_additional-resources"]
.Additional resources

* Verifying the IPsec encryption

* Configuring IPsec encryption

* Encryption protocol and IPsec mode

* Installing managed clusters with {rh-rhacm} and ClusterInstance resources

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-install-ztp.adoc

[id="ztp-verifying-ipsec_{context}"]
= Verifying the IPsec encryption

You can verify that the IPsec encryption is successfully applied in a managed OpenShift Container Platform cluster.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have configured the IPsec encryption.

.Procedure

. Start a debug pod for the managed cluster by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Check that the IPsec policy is applied in the cluster node by running the following command:
+
[source,terminal]
----
sh-5.1# ip xfrm policy
----
+
.Example output
[source,terminal]
----
src 172.16.123.0/24 dst 10.1.232.10/32
  dir out priority 1757377 ptype main
  tmpl src 10.1.28.190 dst 10.1.232.10
    proto esp reqid 16393 mode tunnel
src 10.1.232.10/32 dst 172.16.123.0/24
  dir fwd priority 1757377 ptype main
  tmpl src 10.1.232.10 dst 10.1.28.190
    proto esp reqid 16393 mode tunnel
src 10.1.232.10/32 dst 172.16.123.0/24
  dir in priority 1757377 ptype main
  tmpl src 10.1.232.10 dst 10.1.28.190
    proto esp reqid 16393 mode tunnel
----

. Check that the IPsec tunnel is up and connected by running the following command:
+
[source,terminal]
----
sh-5.1# ip xfrm state
----
+
.Example output
[source,terminal]
----
src 10.1.232.10 dst 10.1.28.190
  proto esp spi 0xa62a05aa reqid 16393 mode tunnel
  replay-window 0 flag af-unspec esn
  auth-trunc hmac(sha1) 0x8c59f680c8ea1e667b665d8424e2ab749cec12dc 96
  enc cbc(aes) 0x2818a489fe84929c8ab72907e9ce2f0eac6f16f2258bd22240f4087e0326badb
  anti-replay esn context:
   seq-hi 0x0, seq 0x0, oseq-hi 0x0, oseq 0x0
   replay_window 128, bitmap-length 4
   00000000 00000000 00000000 00000000
src 10.1.28.190 dst 10.1.232.10
  proto esp spi 0x8e96e9f9 reqid 16393 mode tunnel
  replay-window 0 flag af-unspec esn
  auth-trunc hmac(sha1) 0xd960ddc0a6baaccb343396a51295e08cfd8aaddd 96
  enc cbc(aes) 0x0273c02e05b4216d5e652de3fc9b3528fea94648bc2b88fa01139fdf0beb27ab
  anti-replay esn context:
   seq-hi 0x0, seq 0x0, oseq-hi 0x0, oseq 0x0
   replay_window 128, bitmap-length 4
   00000000 00000000 00000000 00000000
----

. Ping a known IP in the external host subnet by running the following command:
For example, ping an IP address in the `rightsubnet` range that you set in the `ipsec/ipsec-endpoint-config.yaml` file:
+
[source,terminal]
----
sh-5.1# ping 172.16.110.8
----
+
.Example output
[source,terminal]
----
PING 172.16.110.8 (172.16.110.8) 56(84) bytes of data.
64 bytes from 172.16.110.8: icmp_seq=1 ttl=64 time=153 ms
64 bytes from 172.16.110.8: icmp_seq=2 ttl=64 time=155 ms
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-clusterinstance-config-reference_{context}"]
= ClusterInstance CR installation reference

For a detailed API reference for the `ClusterInstance` custom resource, see ClusterInstance API in the {rh-rhacm-first} documentation.

[role="_additional-resources"]
.Additional resources

* Customizing extra installation manifests in the {ztp} pipeline

* Preparing the {ztp} site configuration repository

* Configuring the hub cluster with ArgoCD

* Signalling {ztp} cluster deployment completion with validator inform policies

* Creating the managed bare-metal host secrets

* BMC addressing

* About root device hints

// Module included in the following assemblies:
//
// * edge_computing/ztp-deploying-far-edge-sites.adoc

[id="ztp-configuring-host-firmware-with-gitops-ztp_{context}"]
= Managing host firmware settings with {ztp}

Hosts require the correct firmware configuration to ensure high performance and optimal efficiency.
You can deploy custom host firmware configurations for managed clusters with {ztp}.

Tune hosts with specific hardware profiles in your lab and ensure they are optimized for your requirements.
When you have completed host tuning to your satisfaction, you extract the host profile and save it in your {ztp} repository.
Then, you use the host profile to configure firmware settings in the managed cluster hosts that you deploy with {ztp}.

You specify the required hardware profiles by creating `HostFirmwareSettings` CRs, packaging them in `ConfigMap` resources, and referencing them in the `templateRefs` field of your `ClusterInstance` CR.
The SiteConfig Operator generates the required `HostFirmwareSettings` and `BareMetalHost` CRs that are applied to the hub cluster.

Use the following best practices to manage your host firmware profiles.

Identify critical firmware settings with hardware vendors::
Work with hardware vendors to identify and document critical host firmware settings required for optimal performance and compatibility with the deployed host platform.

Use common firmware configurations across similar hardware platforms::
Where possible, use a standardized host firmware configuration across similar hardware platforms to reduce complexity and potential errors during deployment.

Test firmware configurations in a lab environment::
Test host firmware configurations in a controlled lab environment before deploying in production to ensure that settings are compatible with hardware, firmware, and software.

Manage firmware profiles in source control::
Manage host firmware profiles in Git repositories to track changes, ensure consistency, and facilitate collaboration with vendors.

[role="_additional-resources"]
.Additional resources

* Recommended firmware configuration for vDU cluster hosts

// Module included in the following assemblies:
//
// * edge_computing/ztp-deploying-far-edge-sites.adoc

[id="ztp-retrieving-the-host-firmware-schema_{context}"]
= Retrieving the host firmware schema for a managed cluster

You can discover the host firmware schema for managed clusters.
The host firmware schema for bare-metal hosts is populated with information that the Ironic API returns.
The API returns information about host firmware interfaces, including firmware setting types, allowable values, ranges, and flags.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have installed {rh-rhacm-first} and logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have provisioned a cluster that is managed by {rh-rhacm}.

.Procedure

* Discover the host firmware schema for the managed cluster.
Run the following command:
+
[source,terminal]
----
$ oc get firmwareschema -n <managed_cluster_namespace> -o yaml
----
+
.Example output
[source,terminal]
----
apiVersion: v1
items:
- apiVersion: metal3.io/v1alpha1
  kind: FirmwareSchema
  metadata:
    creationTimestamp: "2024-09-11T10:29:43Z"
    generation: 1
    name: schema-40562318
    namespace: compute-1
    ownerReferences:
    - apiVersion: metal3.io/v1alpha1
      kind: HostFirmwareSettings
      name: compute-1.example.com
      uid: 65d0e89b-1cd8-4317-966d-2fbbbe033fe9
    resourceVersion: "280057624"
    uid: 511ad25d-f1c9-457b-9a96-776605c7b887
  spec:
    schema:
      AccessControlService:
        allowable_values:
        - Enabled
        - Disabled
        attribute_type: Enumeration
        read_only: false
      # ...
----

// Module included in the following assemblies:
//
// * edge_computing/ztp-deploying-far-edge-sites.adoc

[id="ztp-retrieving-the-host-firmware-settings_{context}"]
= Retrieving the host firmware settings for a managed cluster

You can retrieve the host firmware settings for managed clusters.
This is useful when you have deployed changes to the host firmware and you want to monitor the changes and ensure that they are applied successfully.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have installed {rh-rhacm-first} and logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have provisioned a cluster that is managed by {rh-rhacm}.

.Procedure

. Retrieve the host firmware settings for the managed cluster.
Run the following command:
+
--
[source,terminal]
----
$ oc get hostfirmwaresettings -n <cluster_namespace> <node_name> -o yaml
----

.Example output
[source,terminal]
----
apiVersion: v1
items:
- apiVersion: metal3.io/v1alpha1
  kind: HostFirmwareSettings
  metadata:
    creationTimestamp: "2024-09-11T10:29:43Z"
    generation: 1
    name: compute-1.example.com
    namespace: kni-qe-24
    ownerReferences:
    - apiVersion: metal3.io/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: BareMetalHost
      name: compute-1.example.com
      uid: 0baddbb7-bb34-4224-8427-3d01d91c9287
    resourceVersion: "280057626"
    uid: 65d0e89b-1cd8-4317-966d-2fbbbe033fe9
  spec:
    settings: {}
  status:
    conditions:
    - lastTransitionTime: "2024-09-11T10:29:43Z"
      message: ""
      observedGeneration: 1
      reason: Success
      status: "True" <1>
      type: ChangeDetected
    - lastTransitionTime: "2024-09-11T10:29:43Z"
      message: Invalid BIOS setting
      observedGeneration: 1
      reason: ConfigurationError
      status: "False" <2>
      type: Valid
    lastUpdated: "2024-09-11T10:29:43Z"
    schema:
      name: schema-40562318
      namespace: compute-1
    settings: <3>
      AccessControlService: Enabled
      AcpiHpet: Enabled
      AcpiRootBridgePxm: Enabled
      # ...
----
<1> Indicates that a change in the host firmware settings has been detected
<2> Indicates that the host has an invalid firmware setting
<3> The complete list of configured host firmware settings is returned under the `status.settings` field
--

. Optional: Check the status of the `HostFirmwareSettings` (`hfs`) custom resource in the cluster:
+
[source,terminal]
----
$ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="ChangeDetected")].status}'
----
+
.Example output
[source,terminal]
----
True
----

. Optional: Check for invalid firmware settings in the cluster host.
Run the following command:
+
[source,terminal]
----
$ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="Valid")].status}'
----
+
.Example output
[source,terminal]
----
False
----

// Module included in the following assemblies:
//
// * edge_computing/ztp-deploying-far-edge-sites.adoc

[id="ztp-deploying-user-defined-firmware-configuration-with-gitops-ztp_{context}"]
= Deploying user-defined firmware to cluster hosts with {ztp}

You can deploy user-defined firmware settings to cluster hosts by creating custom node templates that include `HostFirmwareSettings` CRs, and referencing them in the `ClusterInstance` CR.
You can configure hardware profiles to apply to hosts in the following scenarios:

* All hosts in the cluster
* Individual hosts in the cluster

[IMPORTANT]
====
You can configure host hardware profiles to be applied in a hierarchy.
Node-level profiles override cluster-wide settings.
====

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have installed {rh-rhacm-first} version 2.12 or later and logged in to the hub cluster as a user with `cluster-admin` privileges.

* You have installed the SiteConfig Operator in the hub cluster.

* You created a Git repository where you manage your custom site configuration data.
The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

.Procedure

. Create the `HostFirmwareSettings` CR that contains the firmware settings you want to apply.
For example, create the following YAML file:
+
.host-firmware-settings.yaml
[source,yaml]
----
apiVersion: metal3.io/v1alpha1
kind: HostFirmwareSettings
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  settings:
    BootMode: "Uefi"
    LogicalProc: "Enabled"
    ProcVirtualization: "Enabled"
----

. Save the `HostFirmwareSettings` CR file relative to the `kustomization.yaml` file that you use to provision the cluster.
For example:
+
[source,terminal]
----
site-configs/
  └── site1-sno-du/
        ├── clusterinstance-site1-sno-du.yaml
        ├── kustomization.yaml
        └── host-firmware-settings.yaml
----

. Create a `ConfigMap` to store the `HostFirmwareSettings` CR.
You can use a `kustomization.yaml` file with `configMapGenerator` to create the `ConfigMap`.
For example:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - clusterinstance-site1-sno-du.yaml
configMapGenerator:
  - name: host-firmware-settings-cm
    namespace: site1-sno-du <1>
    files:
      - host-firmware-settings.yaml <2>
generatorOptions:
  disableNameSuffixHash: true
----
<1> The namespace must match the `ClusterInstance` namespace.
<2> The name of the `HostFirmwareSettings` CR.

. To apply a hardware profile to all hosts in the cluster, reference the `ConfigMap` in the `spec.templateRefs` field of your `ClusterInstance` CR.
For example:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  clusterName: "site1-sno-du"
  # ...
  templateRefs:
    - name: host-firmware-settings-cm <1>
      namespace: site1-sno-du
  nodes:
    - hostName: "node1.example.com"
      # ...
----
<1> Applies the firmware profile to all hosts in the cluster.

. Optional: To apply a hardware profile to a specific host in the cluster, reference the `ConfigMap` in the `spec.nodes[].templateRefs` field.
For example:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  clusterName: "site1-sno-du"
  # ...
  nodes:
    - hostName: "node1.example.com"
      # ...
      templateRefs:
        - name: host-firmware-node1-cm <1>
          namespace: site1-sno-du
    - hostName: "node2.example.com"
      # ...
----
<1> Applies the firmware profile only to the `node1.example.com` host.
+
[NOTE]
====
Node-level `templateRefs` settings override cluster-level `templateRefs` settings.
====

. Commit the `ClusterInstance` CR, `ConfigMap`, and associated `kustomization.yaml` changes in your Git repository and push the changes.
+
The Argo CD pipeline detects the changes and begins the managed cluster deployment.
+
[NOTE]
====
Cluster deployment proceeds even if an invalid firmware setting is detected.
To apply a correction using {ztp}, re-deploy the cluster with the corrected hardware profile.
====

.Verification

* Check that the firmware settings have been applied in the managed cluster host.
For example, run the following command:
+
[source,terminal]
----
$ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="Valid")].status}'
----
+
** where `<managed_cluster_namespace>` is the namespace of the managed cluster and `<managed_cluster_name>` is the name of the managed cluster.
+
.Example output
[source,terminal]
----
True
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-monitoring-deployment-progress_{context}"]
= Monitoring managed cluster installation progress

The Argo CD pipeline syncs the `ClusterInstance` CR from the Git repository to the hub cluster. The SiteConfig Operator then processes the `ClusterInstance` CR and generates the required cluster configuration CRs. You can monitor the progress of the cluster installation from the {rh-rhacm} dashboard or from the command line.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

.Procedure

When the synchronization is complete, the installation generally proceeds as follows:

. The Assisted Service Operator installs OpenShift Container Platform on the cluster. You can monitor the progress of cluster installation from the {rh-rhacm} dashboard or from the command line by running the following commands:

.. Export the cluster name:
+
[source,terminal]
----
$ export CLUSTER=<clusterName>
----

.. Query the `AgentClusterInstall` CR for the managed cluster:
+
[source,terminal]
----
$ oc get agentclusterinstall -n $CLUSTER $CLUSTER -o jsonpath='{.status.conditions[?(@.type=="Completed")]}' | jq
----

.. Get the installation events for the cluster:
+
[source,terminal]
----
$ curl -sk $(oc get agentclusterinstall -n $CLUSTER $CLUSTER -o jsonpath='{.status.debugInfo.eventsURL}')  | jq '.[-2,-1]'
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-troubleshooting-ztp-gitops-installation-crs_{context}"]
= Troubleshooting {ztp} by validating the installation CRs

The ArgoCD pipeline uses the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` custom resources (CRs) to generate the cluster configuration CRs and {rh-rhacm-first} policies. Use the following steps to troubleshoot issues that might occur during this process.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

.Procedure

. Check that the installation CRs were created by using the following command:
+
[source,terminal]
----
$ oc get AgentClusterInstall -n <cluster_name>
----
+
If no object is returned, use the following steps to troubleshoot the ArgoCD pipeline flow from `ClusterInstance` files to the installation CRs.

. Verify that the `ManagedCluster` CR was generated using the `ClusterInstance` CR on the hub cluster:
+
[source,terminal]
----
$ oc get managedcluster
----

. If the `ManagedCluster` is missing, check if the `clusters` application failed to synchronize the files from the Git repository to the hub cluster:
+
[source,terminal]
----
$ oc get applications.argoproj.io -n openshift-gitops clusters -o yaml
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-troubleshooting-ztp-gitops-supermicro-tls_{context}"]
= Troubleshooting {ztp} virtual media booting on SuperMicro servers

SuperMicro X11 servers do not support virtual media installations when the image is served using the `https` protocol. As a result, {sno} deployments for this environment fail to boot on the target node. To avoid this issue, log in to the hub cluster and disable Transport Layer Security (TLS) in the `Provisioning` resource. This ensures the image is not served with TLS even though the image address uses the `https` scheme.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

.Procedure

. Disable TLS in the `Provisioning` resource by running the following command:
+
[source,terminal]
----
$ oc patch provisioning provisioning-configuration --type merge -p '{"spec":{"disableVirtualMediaTLS": true}}'
----

. Continue the steps to deploy your {sno} cluster.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-site-cleanup_{context}"]
= Removing a managed cluster site from the {ztp} pipeline

You can remove a managed site and the associated installation and configuration policy CRs from the {ztp-first} pipeline.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

.Procedure

. Remove a site and the associated CRs by removing the associated `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files from the `kustomization.yaml` file.

. Add the following `syncOptions` field to the ArgoCD application that manages the target site.
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
When you run the {ztp} pipeline again, the generated CRs are removed.

. Optional: If you want to permanently remove a site, you should also remove the `ClusterInstance` and site-specific `PolicyGenerator` or `PolicyGentemplate` files from the Git repository.

. Optional: If you want to remove a site temporarily, for example when redeploying a site, you can leave the `ClusterInstance` and site-specific `PolicyGenerator` or `PolicyGentemplate` CRs in the Git repository.

[role="_additional-resources"]
.Additional resources

* Removing a cluster from management.

* Deprovisioning clusters

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-removing-obsolete-content_{context}"]
= Removing obsolete content from the {ztp} pipeline

If a change to the `PolicyGenerator` or `PolicyGentemplate` configuration results in obsolete policies, for example, if you rename policies, use the following procedure to remove the obsolete policies.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

.Procedure

. Remove the affected `PolicyGenerator` or `PolicyGentemplate` files from the Git repository, commit and push to the remote repository.

. Wait for the changes to synchronize through the application and the affected policies to be removed from the hub cluster.

. Add the updated `PolicyGenerator` or `PolicyGentemplate` files back to the Git repository, and then commit and push to the remote repository.
+
[NOTE]
====
Removing {ztp-first} policies from the Git repository, and as a result also removing them from the hub cluster, does not affect the configuration of the managed cluster. The policy and CRs managed by that policy remains in place on the managed cluster.
====

. Optional: As an alternative, after making changes to `PolicyGenerator` or `PolicyGentemplate` CRs that result in obsolete policies, you can remove these policies from the hub cluster manually. You can delete policies from the {rh-rhacm} console using the *Governance* tab or by running the following command:
+
[source,terminal]
----
$ oc delete policy -n <namespace> <policy_name>
----

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

[id="ztp-tearing-down-the-pipeline_{context}"]
= Tearing down the {ztp} pipeline

You can remove the ArgoCD pipeline and all generated {ztp-first} artifacts.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

.Procedure

. Detach all clusters from {rh-rhacm-first} on the hub cluster.

. Delete the `kustomization.yaml` file in the `deployment` directory using the following command:
+
[source,terminal]
----
$ oc delete -k out/argocd/deployment
----

. Commit and push your changes to the site repository.
