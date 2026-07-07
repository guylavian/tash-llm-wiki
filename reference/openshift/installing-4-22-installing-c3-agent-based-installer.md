---
title: "Installing a cluster on {oci-edge-no-rt} by using the Agent-based Installer"
type: reference
domain: openshift
slug: installing-4-22-installing-c3-agent-based-installer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-c3-agent-based-installer
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on {oci-edge-no-rt} by using the Agent-based Installer

[id="installing-c3-agent-based-installer"]
= Installing a cluster on {oci-edge-no-rt} by using the Agent-based Installer

You can use the Agent-based Installer to install a cluster on {oci-edge}, so that you can run cluster workloads on on-premise infrastructure while still using {oci-first} services.

The following procedures describe a cluster installation on {oci-c3} as an example.

// Supported Oracle Edge Cloud Infrastructures
// Module included in the following assemblies:
//
// * installing/installing_oci_edge/installing-c3-agent-based-installer.adoc
// * installing/installing_oci_edge/installing-c3-assisted-installer.adoc

[id="installing-oci-edge-infra-support_{context}"]
= Supported {oci-edge-no-rt} infrastructures

The following table describes the support status of each {oci-edge} infrastructure offering:

.{oci-edge-no-rt} infrastructure support statuses
[cols=".^,.^",options="header"]
|====
|Infrastructure type|Support status

|Private Cloud Appliance
|General Availability

|Oracle Compute Cloud@Customer
|General Availability

|Roving Edge
|Technology Preview

|====

[id="abi-oci-c3-process-checklist_{context}"]
== Installation process workflow

The following workflow describes a high-level outline for the process of installing an OpenShift Container Platform cluster on {oci-edge-no-rt} using the Agent-based Installer:

. Create {oci-first-no-rt} resources and services (Oracle).
. Prepare configuration files for the Agent-based Installer (Red{nbsp}Hat).
. Generate the agent ISO image (Red{nbsp}Hat).
. Convert the ISO image to an {oci} image, upload it to an {oci} Home Region Bucket, and then import the uploaded image to the {oci-edge-no-rt} system (Oracle).
. Disconnected environments: Prepare a web server that is accessible by {oci-edge-no-rt} instances (Red{nbsp}Hat).
. Disconnected environments: Upload the rootfs image to the web server (Red{nbsp}Hat).
. Configure your firewall for OpenShift Container Platform (Red{nbsp}Hat).
. Create control plane nodes and configure load balancers (Oracle).
. Create compute nodes and configure load balancers (Oracle).
. Verify that your cluster runs on {oci-edge-no-rt} (Oracle).

// Creating Compute Cloud@Customer infrastructure resources and services
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-agent-based-installer.adoc

[id="abi-c3-resources-services_{context}"]
= Creating {oci} infrastructure resources and services

You must create an {oci-edge-no-rt} environment on your virtual machine (VM) shape. By creating this environment, you can install OpenShift Container Platform and deploy a cluster on an infrastructure that supports a wide range of cloud options and strong security policies. Having prior knowledge of {oci-first-no-rt} components can help you with understanding the concept of {oci} resources and how you can configure them to meet your organizational needs.

[IMPORTANT]
====
To ensure compatibility with OpenShift Container Platform, you must set `A` as the record type for each DNS record and name records as follows:

* `api.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer
* `api-int.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer
* `*.apps.<cluster_name>.<base_domain>`, which targets the `ingressVIP` parameter of the Ingress load balancer

The `api.{asterisk}` and `api-int.{asterisk}` DNS records relate to control plane machines, so you must ensure that all nodes in your installed OpenShift Container Platform cluster can access these DNS records.
====

.Prerequisites

* You configured an {oci} account to host the OpenShift Container Platform cluster.
See "Access and Considerations" in OpenShift Cluster Setup with
Agent Based Installer on Compute
Cloud@Customer (Oracle documentation).

.Procedure

* Create the required {oci} resources and services.
+
For more information, see "Terraform Script Execution" in OpenShift Cluster Setup with
Agent Based Installer on Compute
Cloud@Customer (Oracle documentation).

[role="_additional-resources"]
.Additional resources

* Learn About Oracle Cloud Basics (Oracle documentation)

// Creating configuration files for installing a cluster on Compute Cloud@Customer
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-agent-based-installer.adoc
// * installing/installing_oci/installing-pca-agent-based-installer.adoc

[id="creating-config-files-cluster-install-c3_{context}"]
= Creating configuration files for installing a cluster on {oci-edge-no-rt}

You must create the `install-config.yaml` and the `agent-config.yaml` configuration files so that you can use the Agent-based Installer to generate a bootable ISO image. The Agent-based installation comprises a bootable ISO that has the Assisted discovery agent and the Assisted Service. Both of these components are required to perform the cluster installation, but the latter component runs on only one of the hosts.

[id="creating-config-files-cluster-install-pca_{context}"]
= Creating configuration files for installing a cluster on {oci-pca-short}

You must create the `install-config.yaml` and the `agent-config.yaml` configuration files so that you can use the Agent-based Installer to generate a bootable ISO image. The Agent-based installation comprises a bootable ISO that has the Assisted discovery agent and the Assisted Service. Both of these components are required to perform the cluster installation, but the latter component runs on only one of the hosts.

[id="creating-config-files-cluster-install-oci_{context}"]
= Creating configuration files for installing a cluster on {oci-distributed-no-rt}

You must create the `install-config.yaml` and the `agent-config.yaml` configuration files so that you can use the Agent-based Installer to generate a bootable ISO image. The Agent-based installation comprises a bootable ISO that has the Assisted discovery agent and the Assisted Service. Both of these components are required to perform the cluster installation, but the latter component runs on only one of the hosts.

[NOTE]
====
You can also use the Agent-based Installer to generate or accept Zero Touch Provisioning (ZTP) custom resources.
====

.Prerequisites
* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing the method for users.
* You have read the "Preparing to install with the Agent-based Installer" documentation.
* You downloaded the Agent-Based Installer and the command-line interface (CLI) from the {hybrid-console}.
* If you are installing in a disconnected environment, you have prepared a mirror registry in your environment and mirrored release images to the registry.
+
[IMPORTANT]
====
Check that your `openshift-install` binary version relates to your local image container registry and not a shared registry, such as {quay}, by running the following command:

[source,terminal]
----
$ ./openshift-install version
----

.Example output for a shared registry binary
[source,terminal,subs="quotes"]
----
./openshift-install 4.22.0
built from commit ae7977b7d1ca908674a0d45c5c243c766fa4b2ca
release image registry.ci.openshift.org/origin/release:4.22ocp-release@sha256:0da6316466d60a3a4535d5fed3589feb0391989982fba59d47d4c729912d6363
release architecture amd64
----
====
* You have logged in to the OpenShift Container Platform with administrator privileges.

.Procedure

. Create an installation directory to store configuration files in by running the following command:
+
[source,terminal]
----
$ mkdir ~/<directory_name>
----

. Configure the `install-config.yaml` configuration file to meet the needs of your organization and save the file in the directory you created.
+
.`install-config.yaml` file that sets an external platform
+
[source,yaml]
----
# install-config.yaml
apiVersion: v1
baseDomain: <base_domain> <1>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  network type: OVNKubernetes
  machineNetwork:
  - cidr: <ip_address_from_cidr> <2>
  serviceNetwork:
  - 172.30.0.0/16
compute:
  - architecture: amd64 <3>
  hyperthreading: Enabled
  name: worker
  replicas: 0
controlPlane:
  architecture: amd64 <3>
  hyperthreading: Enabled
  name: master
  replicas: 3
platform:
   external:
    platformName: oci <4>
    cloudControllerManager: External
sshKey: <public_ssh_key> <5>
pullSecret: '<pull_secret>' <6>
# ...
----
<1> The base domain of your cloud provider.
<2> The IP address from the virtual cloud network (VCN) that the CIDR allocates to resources and components that operate on your network.
<3> Depending on your infrastructure, you can select either `arm64` or `amd64`.
<4> Set `OCI` as the external platform, so that OpenShift Container Platform can integrate with {oci}.
<5> Specify your SSH public key.
<6> The pull secret that you need for authenticate purposes when downloading container images for OpenShift Container Platform components and services, such as Quay.io. See Install OpenShift Container Platform 4 from the {hybrid-console}.

. Create a directory on your local system named `openshift`. This must be a subdirectory of the installation directory.
+
[IMPORTANT]
====
Do not move the `install-config.yaml` or `agent-config.yaml` configuration files to the `openshift` directory.
====

. If you used a stack to provision OCI infrastructure resources: Copy and paste the `dynamic_custom_manifest` output of the OCI stack into a file titled `manifest.yaml` and save the file in the `openshift` directory.

. If you did not use a stack to provision OCI infrastructure resources: Download and prepare custom manifests to create an Agent ISO image:

.. Go to Configuration Files (Oracle documentation) and follow the link to the custom manifests directory on GitHub.

.. Copy the contents of the `condensed-manifest.yml` file and save it locally to a file in the `openshift` directory.

.. In the `condensed-manifest.yml` file, update the sections marked with `TODO` to specify the compartment {ocid-first}, VCN {ocid}, subnet {ocid} from the load balancer, and the security lists {ocid}.

. Configure the Oracle custom manifest files.

.. Go to "Prepare the OpenShift Master Images" in OpenShift Cluster Setup with
Agent Based Installer on Compute
Cloud@Customer (Oracle documentation).

.. Copy and paste the `oci-ccm.yml`, `oci-csi.yml`, and `machineconfig-ccm.yml` files into your `openshift` directory.

.. Edit the `oci-ccm.yml` and `oci-csi.yml` files to specify the compartment {ocid-first}, VCN {ocid}, subnet {ocid} from the load balancer, the security lists {ocid}, and the `c3-cert.pem` section.

. Configure the Oracle custom manifest files.

.. Go to "Prepare the OpenShift Master Images" in OpenShift Cluster Setup with
Agent Based Installer on Private Cloud Appliance (Oracle documentation).

.. Copy and paste the `oci-ccm.yml`, `oci-csi.yml`, and `machineconfig-ccm.yml` files into your `openshift` directory.

.. Edit the `oci-ccm.yml` and `oci-csi.yml` files to specify the compartment {ocid-first}, VCN {ocid}, subnet {ocid} from the load balancer, the security lists {ocid}, and the `c3-cert.pem` section.

. Configure the `agent-config.yaml` configuration file to meet your organization's requirements.
+
.Sample `agent-config.yaml` file for an IPv4 network.
[source,yaml]
----
apiVersion: v1beta1
metadata:
  name: <cluster_name> // <1>
  namespace: <cluster_namespace> <2>
rendezvousIP: <ip_address_from_CIDR> <3>
bootArtifactsBaseURL: <server_URL> <4>
# ...
----
<1> The cluster name that you specified in your DNS record.
<2> The namespace of your cluster on OpenShift Container Platform.
<3> If you use IPv4 as the network IP address format, ensure that you set the `rendezvousIP` parameter to an IPv4 address that the VCN's Classless Inter-Domain Routing (CIDR) method allocates on your network. Also ensure that at least one instance from the pool of instances that you booted with the ISO matches the IP address value you set for the `rendezvousIP` parameter.
<4> The URL of the server where you want to upload the rootfs image. This parameter is required only for disconnected environments.

. Generate a minimal ISO image, which excludes the rootfs image, by entering the following command in your installation directory:
+
[source,terminal]
----
$ ./openshift-install agent create image --log-level debug
----
+
The command also completes the following actions:
+
* Creates a subdirectory, `./<installation_directory>/auth directory:`, and places `kubeadmin-password` and `kubeconfig` files in the subdirectory.
* Creates a `rendezvousIP` file based on the IP address that you specified in the `agent-config.yaml` configuration file.
* Optional: Any modifications you made to `agent-config.yaml` and `install-config.yaml` configuration files get imported to the Zero Touch Provisioning (ZTP) custom resources.
+
[IMPORTANT]
====
The Agent-based Installer uses {op-system-first}. The rootfs image, which is mentioned in a later step, is required for booting, recovering, and repairing your operating system.
====

. Disconnected environments only: Upload the rootfs image to a web server.

..  Go to the `./<installation_directory>/boot-artifacts` directory that was generated when you created the minimal ISO image.

.. Use your preferred web server, such as any Hypertext Transfer Protocol daemon (`httpd`), to upload the rootfs image to the location specified in the `bootArtifactsBaseURL` parameter of the `agent-config.yaml` file.
+
For example, if the `bootArtifactsBaseURL` parameter states `\http://192.168.122.20`, you would upload the generated rootfs image to this location so that the Agent-based installer can access the image from `\http://192.168.122.20/agent.x86_64-rootfs.img`. After the Agent-based installer boots the minimal ISO for the external platform, the Agent-based Installer downloads the rootfs image from the `\http://192.168.122.20/agent.x86_64-rootfs.img` location into the system memory.
+
[NOTE]
====
The Agent-based Installer also adds the value of the `bootArtifactsBaseURL` to the minimal ISO Image's configuration, so that when the Operator boots a cluster's node, the Agent-based Installer downloads the rootfs image into system memory.
====
+
[IMPORTANT]
====
Consider that the full ISO image, which is in excess of `1` GB, includes the rootfs image. The image is larger than the minimal ISO Image, which is typically less than `150` MB.
====

[role="_additional-resources"]
.Additional resources

* About OpenShift Container Platform installation
* Selecting a cluster installation type
* Preparing to install with the Agent-based Installer
* Downloading the Agent-based Installer
* Creating a mirror registry with mirror registry for Red{nbsp}Hat OpenShift
* Mirroring the OpenShift Container Platform image repository
* Optional: Using ZTP manifests

// Configuring your firewall
// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc
// * installing/installing-oci-agent-based-installer.adoc

[id="configuring-firewall_{context}"]
= Configuring your firewall for OpenShift Container Platform

Before you install OpenShift Container Platform, you must configure your firewall to grant access to the sites that OpenShift Container Platform requires. When using a firewall, make additional configurations to the firewall so that OpenShift Container Platform can access the sites that it requires to function.

There are no special configuration considerations for services running on only controller nodes compared to compute nodes.

For a disconnected environment, you must mirror content from both Red{nbsp}Hat and Oracle. This environment requires that you create firewall rules to expose your firewall to specific ports and registries.

[NOTE]
====
If your environment has a dedicated load balancer in front of your OpenShift Container Platform cluster, review the allowlists between your firewall and load balancer to prevent unwanted network restrictions to your cluster.
====

.Procedure

. Allowlist the following container registry URLs for cluster installation and upgrades:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`registry.redhat.io`
|443
|Provides core container images

|`access.redhat.com`
|443
|Hosts a signature store that a container client requires for verifying images pulled from `registry.access.redhat.com`. In a firewall environment, ensure that this resource is on the allowlist.

|`registry.access.redhat.com`
|443
|Hosts all the container images that are stored on the Red Hat Ecosystem Catalog, including core container images.

|`quay.io`
|443
|Provides core container images

|`cdn.quay.io`
|443
|Provides core container images

|`cdn01.quay.io`
|443
|Provides core container images

|`cdn02.quay.io`
|443
|Provides core container images

|`cdn03.quay.io`
|443
|Provides core container images

|`cdn04.quay.io`
|443
|Provides core container images

|`cdn05.quay.io`
|443
|Provides core container images

|`cdn06.quay.io`
|443
|Provides core container images

|`icr.io`
|443
|Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks.

|`cp.icr.io`
|443
|Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks.
|===
+
* You can use the wildcard `*.quay.io` instead of `cdn.quay.io` and `cdn0[1-6].quay.io` in your allowlist.
* You can use the wildcard `*.access.redhat.com` to simplify the configuration and ensure that all subdomains, including `registry.access.redhat.com`, are allowed.
* When adding a site such as `quay.io` to your allowlist, do not add a wildcard entry such as `*.quay.io` to your denylist. In most cases, image registries use a content delivery network (CDN) to serve images. If a firewall blocks access, image downloads are denied when the initial download request redirects to a hostname such as `cdn01.quay.io`.

. Allowlist the following URLs to enable cluster access, authentication, and updates:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`*.apps.<cluster_name>.<base_domain>`
|443
|Allowlist these URLs to enable cluster access, authentication, and updates.

|`api.openshift.com`
|443
|API endpoint for cluster tokens and update checks.

|`console.redhat.com`
|443
|Authentication service for cluster tokens.

|`sso.redhat.com`
|443
|The `https://console.redhat.com` site uses authentication from `sso.redhat.com`
|===
+
For egress traffic, Operators require route access to perform health checks to establish a connection for reaching endpoints. The authentication and web console Operators connect to two routes to verify functionality. Cluster administrators who do not want to allow `*.apps.<cluster_name>.<base_domain>`, must allow the following routes:
+
* `oauth-openshift.apps.<cluster_name>.<base_domain>`
* `canary-openshift-ingress-canary.apps.<cluster_name>.<base_domain>`
* `console-openshift-console.apps.<cluster_name>.<base_domain>`, or the hostname
that is specified in the `spec.route.hostname` field of the
`consoles.operator/cluster` object if the field is not empty.

. Allowlist the following registry URLs that host related artifacts for cluster installation and upgrades, such as installation content, release images, and client tools:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`mirror.openshift.com`
|443
|Required to access mirrored installation content and images. This site is also a source of release image signatures, although the Cluster Version Operator needs only a single functioning source.

|`quayio-production-s3.s3.amazonaws.com`
|443
|Required to access Quay image content in AWS.

// |`registry.access.redhat.com`
// |443
// |Required for `odo` CLI.

|`rhcos.mirror.openshift.com`
|443
|Required to download {op-system-first} images.

|`storage.googleapis.com/openshift-release`
|443
|A source of release image signatures, although the Cluster Version Operator needs only a single functioning source.
|===

. Set your firewall's allowlist to include any site that provides resources for a language or framework that your builds require.

. If you do not disable Telemetry, you must grant access to the following URLs to access Telemetry and {red-hat-lightspeed}:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`cert-api.access.redhat.com`
|443
|Required for Telemetry

|`api.access.redhat.com`
|443
|Required for Telemetry

|`infogw.api.openshift.com`
|443
|Required for Telemetry

|`console.redhat.com`
|443
|Required for Telemetry and for `insights-operator`
|===

. Set your firewall's allowlist to include the following registry URLs:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`api.openshift.com`
|443
|Required both for your cluster token and to check if updates are available for the cluster.

|`rhcos.mirror.openshift.com`
|443
|Required to download {op-system-first} images.
|===

. Set your firewall's allowlist to include the following external URLs. Each repository URL hosts {oci} containers. Consider mirroring images to as few repositories as possible to reduce any performance issues.
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`k8s.gcr.io`
|port
|A Kubernetes registry that hosts container images for a community-based image registry. This image registry is hosted on a custom Google Container Registry (GCR) domain.

|`ghcr.io`
|port
|A GitHub image registry where you can store and manage Open Container Initiative images. Requires an access token to publish, install, and delete private, internal, and public packages.

|`storage.googleapis.com`
|443
|A source of release image signatures, although the Cluster Version Operator needs only a single functioning source.

|`registry.k8s.io`
|port
|Replaces the `k8s.gcr.io` image registry because the `k8s.gcr.io` image registry does not support other platforms and vendors.
|===

. If you use {alibaba}, {aws-first}, {azure-first}, or {gcp-first} to host your cluster, you must grant access to the URLs that offer the cloud provider API and DNS for that cloud:
+
[cols="2a,8a,2a,8a",options="header"]
|===
|Cloud |URL | Port |Function

|Alibaba
|`*.aliyuncs.com`
|443
|Required to access Alibaba Cloud services and resources. Review the Alibaba endpoints_config.go file to find the exact endpoints to allow for the regions that you use.

.17+|AWS
|`aws.amazon.com`
|443
|Used to install and manage clusters in an AWS environment.

|`*.amazonaws.com`

Alternatively, if you choose to not use a wildcard for AWS APIs, you must include the following URLs in your allowlist:
|443
|Required to access AWS services and resources. Review the AWS Service Endpoints in the AWS documentation to find the exact endpoints to allow for the regions that you use.

|`ec2.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`events.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`iam.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`route53.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`*.s3.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`*.s3.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`*.s3.dualstack.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`sts.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`sts.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`tagging.us-east-1.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment. This endpoint is always `us-east-1`, regardless of the region the cluster is deployed in.

|`ec2.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`elasticloadbalancing.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`servicequotas.<aws_region>.amazonaws.com`
|443
|Required. Used to confirm quotas for deploying the service.

|`tagging.<aws_region>.amazonaws.com`
|443
|Allows the assignment of metadata about AWS resources in the form of tags.

|`*.cloudfront.net`
|443
|Used to provide access to CloudFront. If you use the AWS Security Token Service (STS) and the private S3 bucket, you must provide access to CloudFront.

.2+|GCP
|`*.googleapis.com`
|443
|Required to access {gcp-short} services and resources. Review Cloud Endpoints in the {gcp-short} documentation to find the endpoints to allow for your APIs.

|`accounts.google.com`
|443
| Required to access your {gcp-short} account.

.3+|Microsoft Azure
|`management.azure.com`
|443
|Required to access Microsoft Azure services and resources. Review the Microsoft Azure REST API reference in the Microsoft Azure documentation to find the endpoints to allow for your APIs.

|`*.blob.core.windows.net`
|443
|Required to download Ignition files.

|`login.microsoftonline.com`
|443
|Required to access Microsoft Azure services and resources. Review the Azure REST API reference in the Microsoft Azure documentation to find the endpoints to allow for your APIs.

|===

. Allowlist the following URL for optional third-party content:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`registry.connect.redhat.com`
|443
|Required for all third-party images and certified operators.
|===

. If you use a default Red Hat Network Time Protocol (NTP) server, allow the following URLs. NTP operates on User Datagram Protocol (UDP) port 123, so this port must be opened on the firewall.
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`1.rhel.pool.ntp.org`
|123
|Provides NTP services for time synchronization.

|`2.rhel.pool.ntp.org`
|123
|Provides NTP services for time synchronization.

|`3.rhel.pool.ntp.org`
|123
|Provides NTP services for time synchronization.
|===

[NOTE]
====
If you do not use a default Red Hat NTP server, verify the NTP server for your platform and allow it in your firewall.
====

// Running your cluster on Compute Cloud@Customer
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-agent-based-installer.adoc

[id="running-cluster-oci-c3-agent-based_{context}"]
= Running a cluster on {oci-edge-no-rt}

To run a cluster on {oci-edge}, you must first convert your generated Agent ISO image into an {oci} image, upload it to an {oci} Home Region Bucket, and then import the uploaded image to the {oci-edge-no-rt} system.

[NOTE]
====
{oci-edge-no-rt} supports the following OpenShift Container Platform cluster topologies:

* Installing an OpenShift Container Platform cluster on a single node.
* A highly available cluster that has a minimum of three control plane instances and two compute instances.
* A compact three-node cluster that has a minimum of three control plane instances.
====

.Prerequisites

* You generated an Agent ISO image. See the "Creating configuration files for installing a cluster on {oci-edge-no-rt}" section.

.Procedure

. Convert the agent ISO image to an {oci} image, upload it to an {oci} Home Region Bucket, and then import the uploaded image to the {oci-edge-no-rt} system.
See "Prepare the OpenShift Master Images" in OpenShift Cluster Setup with
Agent Based Installer on Compute
Cloud@Customer (Oracle documentation) for instructions.

. Create control plane instances on {oci-edge-no-rt}.
See "Create control plane instances on C3 and Master Node LB Backend Sets" in OpenShift Cluster Setup with
Agent Based Installer on Compute
Cloud@Customer (Oracle documentation) for instructions.

. Create a compute instance from the supplied base image for your cluster topology.
See "Add worker nodes" in OpenShift Cluster Setup with
Agent Based Installer on Compute
Cloud@Customer (Oracle documentation) for instructions.
+
[IMPORTANT]
====
Before you create the compute instance, check that you have enough memory and disk resources for your cluster. Additionally, ensure that at least one compute instance has the same IP address as the address stated under `rendezvousIP` in the `agent-config.yaml` file.
====

// Verifying that your Agent-based cluster installation runs on {oci}
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-agent-based-installer.adoc

[id="verifying-cluster-install-oci-agent-based_{context}"]
= Verifying that your Agent-based cluster installation runs on {oci-edge-no-rt}

Verify that your cluster was installed and is running effectively on {oci-edge-no-rt}.

.Prerequisites

* You created all the required {oci-first-no-rt} resources and services. See the "Creating {oci} infrastructure resources and services" section.
* You created `install-config.yaml` and `agent-config.yaml` configuration files. See the "Creating configuration files for installing a cluster on {oci-edge-no-rt}" section.
* You uploaded the agent ISO image to a default Oracle Object Storage bucket, and you created a compute instance on {oci-edge-no-rt}. For more information, see "Running a cluster on {oci-edge-no-rt}".

[id="verifying-cluster-install-oci-agent-based_{context}"]
= Verifying that your Agent-based cluster installation runs on {oci-pca-short}

Verify that your cluster was installed and is running effectively on {oci-pca-short}.

.Prerequisites

* You created all the required {oci-pca} resources and services. See the "Creating {oci-pca-no-rt} infrastructure resources and services" section.
* You created `install-config.yaml` and `agent-config.yaml` configuration files. See the "Creating configuration files for installing a cluster on {oci-pca-short}" section.
* You uploaded the agent ISO image to a default Oracle Object Storage bucket, and you created a compute instance on {oci-pca-short}. For more information, see "Running a cluster on {oci-pca-short}".

[id="verifying-cluster-install-oci-agent-based_{context}"]
= Verifying that your Agent-based cluster installation runs on {oci-distributed-no-rt}

Verify that your cluster was installed and is running effectively on {oci-distributed}.

.Prerequisites

* You created all the required {oci} resources and services. See the "Creating {oci-distributed-no-rt} infrastructure resources and services" section.
* You created `install-config.yaml` and `agent-config.yaml` configuration files. See the "Creating configuration files for installing a cluster on {oci-distributed-no-rt}" section.
* You uploaded the agent ISO image to a default Oracle Object Storage bucket, and you created a compute instance on {oci-distributed-no-rt}. For more information, see "Running a cluster on {oci-distributed-no-rt}".

.Procedure

After you deploy the compute instance on a self-managed node in your OpenShift Container Platform cluster, you can monitor the cluster’s status by choosing one of the following options:

* From the OpenShift Container Platform CLI, enter the following command:
+
[source,terminal]
----
$ ./openshift-install agent wait-for install-complete --log-level debug
----
+
Check the status of the `rendezvous` host node that runs the bootstrap node.  After the host reboots, the host forms part of the cluster.
+
* Use the `kubeconfig` API to check the status of various OpenShift Container Platform components. For the  `KUBECONFIG` environment variable, set the relative path of the cluster's `kubeconfig` configuration file:
+
[source,terminal]
----
$  export KUBECONFIG=~/auth/kubeconfig
----
+
Check the status of each of the cluster's self-managed nodes. CCM applies a label to each node to designate the node as running in a cluster on {oci}.
+
[source,terminal]
----
$ oc get nodes -A
----
+
.Output example
+
[source,terminal]
----
NAME                                   STATUS ROLES                 AGE VERSION
main-0.private.agenttest.oraclevcn.com Ready  control-plane, master 7m  v1.27.4+6eeca63
main-1.private.agenttest.oraclevcn.com Ready  control-plane, master 15m v1.27.4+d7fa83f
main-2.private.agenttest.oraclevcn.com Ready  control-plane, master 15m v1.27.4+d7fa83f
----
+
Check the status of each of the cluster's Operators, with the CCM Operator status being a good indicator that your cluster is running.
+
[source,terminal]
----
$ oc get co
----
+
.Truncated output example
+
[source,terminal]
----
NAME           VERSION     AVAILABLE  PROGRESSING    DEGRADED   SINCE   MESSAGE
authentication 4.22.0-0    True       False          False      6m18s
baremetal      4.22.0-0    True       False          False      2m42s
network        4.22.0-0    True       True           False      5m58s  Progressing: …
    …
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Gathering log data from a failed Agent-based installation

* Adding worker nodes to an on-premise cluster
