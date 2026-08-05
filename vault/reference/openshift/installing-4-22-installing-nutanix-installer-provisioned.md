---
title: "Installing a cluster on Nutanix"
type: reference
domain: openshift
slug: installing-4-22-installing-nutanix-installer-provisioned
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-nutanix-installer-provisioned
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on Nutanix

[id="installing-nutanix-installer-provisioned"]
= Installing a cluster on Nutanix

In OpenShift Container Platform version , you can choose one of the following options to install a cluster on your Nutanix instance:

**Using installer-provisioned infrastructure**: Use the procedures in the following sections to use installer-provisioned infrastructure. Installer-provisioned infrastructure is ideal for installing in connected or disconnected network environments. The installer-provisioned infrastructure includes an installation program that provisions the underlying infrastructure for the cluster.

**Using the Assisted Installer**: The {ai-full} hosted at console.redhat.com. The {ai-full} cannot be used in disconnected environments. The {ai-full} does not provision the underlying infrastructure for the cluster, so you must provision the infrastructure before you run the {ai-full}. Installing with the {ai-full} also provides integration with Nutanix, enabling autoscaling. See Installing an on-premise cluster using the {ai-full} for additional details.

**Using user-provisioned infrastructure**: Complete the relevant steps outlined in the Installing a cluster on any platform documentation.

== Prerequisites

* You have reviewed details about the OpenShift Container Platform installation and update processes.
* The installation program requires access to port 9440 on Prism Central and Prism Element. You verified that port 9440 is accessible.
* If you use a firewall, you have met these prerequisites:
** You confirmed that port 9440 is accessible. Control plane nodes must be able to reach Prism Central and Prism Element on port 9440 for the installation to succeed.
** You configured the firewall to grant access to the sites that OpenShift Container Platform requires. This includes the use of Telemetry.
* If your Nutanix environment is using the default self-signed SSL certificate, replace it with a certificate that is signed by a CA. The installation program requires a valid CA-signed certificate to access to the Prism Central API. For more information about replacing the self-signed certificate, see the  https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Security-Guide-v6_1:mul-security-ssl-certificate-pc-t.html[Nutanix AOS Security Guide].
+
If your Nutanix environment uses an internal CA to issue certificates, you must configure a cluster-wide proxy as part of the installation process. For more information, see Configuring a custom PKI.
+
[IMPORTANT]
====
Use 2048-bit certificates. The installation fails if you use 4096-bit certificates with Prism Central 2022.x.
====
// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-network-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china-region.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_openstack/installing-openstack-user-sr-iov.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc
// * architecture/architecture.adoc
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc

[id="cluster-entitlements_{context}"]
= Internet access for OpenShift Container Platform

[role="_abstract"]
In OpenShift Container Platform , you require access to the internet to
install
obtain the images that are necessary to install
your cluster.

You must have internet access to perform the following actions:

* Access {cluster-manager-url} to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

[IMPORTANT]
====
If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.
====

// Module included in the following assemblies:
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc

[id="nutanix-entitlements_{context}"]
= Internet access for Prism Central

Prism Central requires internet access to obtain the {op-system-first} image that is required to install the cluster. The {op-system} image for Nutanix is available at `rhcos.mirror.openshift.com`.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-network-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc

[id="ssh-agent-using_{context}"]
= Generating a key pair for cluster node SSH access

[role="_abstract"]
During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to the {op-system-first} nodes through their Ignition config files and is used to authenticate SSH access to the nodes. The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication.

The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication. After the key is passed to the nodes, you can use the key pair to SSH in to the {op-system} nodes as the user `core`. To access the nodes through SSH, the private key identity must be managed by SSH for your local user.

If you want to SSH in to your cluster nodes to perform installation debugging or disaster recovery, you must provide the SSH public key during the installation process. The `./openshift-install gather` command also requires the SSH public key to be in place on the cluster nodes.

[IMPORTANT]
====
Do not skip this procedure in production environments, where disaster recovery and debugging is required.
====

[NOTE]
====
You must use a local key, not one that you configured with platform-specific approaches.
====

[NOTE]
====
On clusters running {op-system-first}, the SSH keys specified in the Ignition config files are written to the `/home/core/.ssh/authorized_keys.d/core` file. However, the Machine Config Operator manages SSH keys in the `/home/core/.ssh/authorized_keys` file and configures *sshd* to ignore the `/home/core/.ssh/authorized_keys.d/core` file.
As a result, newly provisioned OpenShift Container Platform nodes are not accessible using SSH until the Machine Config Operator reconciles the machine configs with the `authorized_keys` file. After you can access the nodes using SSH, you can delete the `/home/core/.ssh/authorized_keys.d/core` file.
====

.Procedure

. If you do not have an existing SSH key pair on your local machine to use for authentication onto your cluster nodes, create one. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ ssh-keygen -t ed25519 -N '' -f <path>/<file_name>
----
Specifies the path and file name, such as `~/.ssh/id_ed25519`, of the new SSH key. If you have an existing key pair, ensure your public key is in the your `~/.ssh` directory.
+
[NOTE]
====
If you plan to install an OpenShift Container Platform cluster that uses the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures, do not create a key that uses the `ed25519` algorithm. Instead, create a key that uses the `rsa` or `ecdsa` algorithm.
====

. View the public SSH key:
+
[source,terminal]
----
$ cat <path>/<file_name>.pub
----
+
For example, run the following to view the `~/.ssh/id_ed25519.pub` public key:
+
[source,terminal]
----
$ cat ~/.ssh/id_ed25519.pub
----

. Add the SSH private key identity to the SSH agent for your local user, if it has not already been added. SSH agent management of the key is required for password-less SSH authentication onto your cluster nodes, or if you want to use the `./openshift-install gather` command.
+
[NOTE]
====
On some distributions, default SSH private key identities such as `~/.ssh/id_rsa` and `~/.ssh/id_dsa` are managed automatically.
====
+
.. If the `ssh-agent` process is not already running for your local user, start it as a background task:
+
[source,terminal]
----
$ eval "$(ssh-agent -s)"
----
+
.Example output
[source,terminal]
----
Agent pid 31874
----
+
[NOTE]
====
If your cluster is in FIPS mode, only use FIPS-compliant algorithms to generate the SSH key. The key must be either RSA or ECDSA.
====

. Add your SSH private key to the `ssh-agent`:
+
[source,terminal]
----
$ ssh-add <path>/<file_name>
----
Specifies the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`
+
.Example output
[source,terminal]
----
Identity added: /home/<you>/<path>/<file_name> (<computer_name>)
----

.Next steps

* When you install OpenShift Container Platform, provide the SSH public key to the installation program.
If you install a cluster on infrastructure that you provision, you must provide the key to the installation program.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-ibm-z-preparing-to-install.adoc

[id="installation-obtaining-installer_{context}"]
= Obtaining the installation program

[role="_abstract"]
Before you install OpenShift Container Platform, download the installation file on
the mirror host, so that installation assets exist for deployment in your environment.
a bastion host on your cloud network or a machine that has access to the to the network through a VPN. This ensures that installation assets exist for deployment in your environment.

For more information about private cluster installation requirements, see "Private clusters".
//mpytlak: Added "private" in the context of a review for the {ibm-cloud-title} private work. In an effort to keep updates to other platforms separate, I will open a doc story for each platform that supports a private install.

.Prerequisites

* You have a machine that runs Linux, for example Red Hat Enterprise Linux 8, with 500 MB of local disk space.
+
[IMPORTANT]
====
If you attempt to run the installation program on macOS, a known issue related to the `golang` compiler causes the installation of the OpenShift Container Platform cluster to fail. For more information about this issue, see the section named "Known Issues" in the _OpenShift Container Platform  release notes_ document.
====

.Procedure

. Go to the Cluster Type page on the {hybrid-console}. If you have a Red{nbsp}Hat account, log in with your credentials. If you do not, create an account.
+
[TIP]
====
You can also download the binaries for a specific OpenShift Container Platform release.
====

. Select your infrastructure provider from the *Run it yourself* section of the page.

. Select your host operating system and architecture from the dropdown menus under *OpenShift Installer* and click *Download Installer*.

. Place the downloaded file in the directory where you want to store the installation configuration files.

. Download the installation program from https://github.com/openshift/okd/releases.
+
[IMPORTANT]
====
* The installation program creates several files on the computer that you use to install your cluster. You must keep the installation program and the files that the installation program creates after you finish installing the cluster. Both of the files are required to delete the cluster.

* Deleting the files created by the installation program does not remove your cluster, even if the cluster failed during installation. To remove your cluster, complete the OpenShift Container Platform uninstallation procedures for your specific cloud provider.
====

. Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ tar -xvf openshift-install-linux.tar.gz
----

. Download your installation {cluster-manager-url-pull}. This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.
+
Using a {cluster-manager-url-pull} is not required. You can use a pull secret for another private registry. Or, if you do not need the cluster to pull images from a private registry, you can use `{"auths":{"fake":{"auth":"aWQ6cGFzcwo="}}}` as the pull secret when prompted during the installation.
+
If you do not use the {cluster-manager-url-pull}:
+
* Red{nbsp}Hat Operators are not available.
* The Telemetry and {insights-operator}s do not send data to Red{nbsp}Hat.
* Content from the Red{nbsp}Hat Ecosystem Catalog Container images registry, such as image streams and Operators, are not available.
+
[TIP]
====
Alternatively, you can retrieve the installation program from the Red{nbsp}Hat Customer Portal, where you can specify a version of the installation program to download.
However, you must have an active subscription to access this page.
====

// Module included in the following assemblies:
//
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc

[id="installation-adding-nutanix-root-certificates_{context}"]
= Adding Nutanix root CA certificates to your system trust

Because the installation program requires access to the Prism Central API, you must add your Nutanix trusted root CA certificates to your system trust before you install an OpenShift Container Platform cluster.

.Procedure

. From the Prism Central web console, download the Nutanix root CA certificates.
. Extract the compressed file that contains the Nutanix root CA certificates.
. Add the files for your operating system to the system trust. For example, on a Fedora operating system, run the following command:
+
[source,terminal]
----
# cp certs/lin/* /etc/pki/ca-trust/source/anchors
----

. Update your system trust. For example, on a Fedora operating system, run the following command:
+
[source,terminal]
----
# update-ca-trust extract
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_vmc/installing-vmc-customizations.adoc
// * installing/installing_vmc/installing-vmc-network-customizations.adoc
// * installing/installing_vmc/installing-restricted-networks-vmc.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_nutanix/configuring-iam-nutanix.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_gcp/installing-openstack-installer-restricted.adoc
// Consider also adding the installation-configuration-parameters.adoc module.
//YOU MUST SET AN IFEVAL FOR EACH NEW MODULE

[id="installation-initializing_{context}"]
= Creating the installation configuration file

[role="_abstract"]
You can customize the OpenShift Container Platform cluster you install on
Amazon Web Services (AWS).
{gcp-first}.
{ibm-cloud-name}.
{rh-openstack-first}.
VMware vSphere.
Nutanix.
{ibm-power-vc-name}.
Microsoft Azure.

[IMPORTANT]
====
Do not specify `windows`, `microsoft`, or other variants of these words in the `metadata.name` parameter of the `install-config.yaml` file. Specifying one of these words for the cluster name causes the installation program to generate an error message like the following example message:

[source,terminal]
----
The resource name 'windows-xxxx-identity' or a part of the name is a trademarked or reserved word.
----

Additionally, specifying `login` at the beginning of the name in the `metadata.name` parameter of the `install-config.yaml` file results in the generation of an error message. You can specify `login` in the middle or end of the name.
====

.Prerequisites

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
For a restricted network installation, these files are on your mirror host.
* You have the `imageContentSources` values that were generated during mirror registry creation.
* You have the `imageContentSourcePolicy.yaml` file that was created when you mirrored your registry.
* You have the location of the {op-system-first} image you download.
* You have the `imageContentSourcePolicy.yaml` file that was created when you mirrored your registry.
* You have obtained the contents of the certificate for your mirror registry.
* You have retrieved a {op-system-first} image and uploaded it to an accessible location.
* You have an Azure subscription ID and tenant ID.
* If you are installing the cluster using a service principal, you have its application ID and password.
* If you are installing the cluster using a system-assigned managed identity, you have enabled it on the virtual machine that you will run the installation program from.
* If you are installing the cluster using a user-assigned managed identity, you have met these prerequisites:
** You have its client ID.
** You have assigned it to the virtual machine that you will run the installation program from.
* You have verified that you have met the Nutanix networking requirements. For more information, see "Preparing to install on Nutanix".
* Configure a {gcp-short} account.

.Procedure

. Optional: If you have run the installation program on this computer before, and want to use an alternative service principal or managed identity, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file.
+
Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation.

. Create the `install-config.yaml` file.
+
.. Change to the directory that contains the installation program and run the following command:
+
[source,terminal]
----
$ ./openshift-install create install-config --dir <installation_directory>
----
* `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the
files that the installation program creates.
+
When specifying the directory:
* Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
* Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
+
[NOTE]
=====
Always delete the `~/.powervs` directory to avoid reusing a stale configuration. Run the following command:
[source,terminal]
----
$ rm -rf ~/.powervs
----
=====
+
.. At the prompts, provide the configuration details for your cloud:
+
... Optional: Select an SSH key to use to access your cluster machines.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
+
... Select *AWS* as the platform to target.
+
... If you do not have an Amazon Web Services (AWS) profile stored on your computer, enter the AWS
access key ID and secret access key for the user that you configured to run the
installation program.
+
... Select the AWS region to deploy the cluster to.
+
... Select the base domain for the Route 53 service that you configured for your cluster.
+
... Select *azure* as the platform to target.
+
If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values.
+
... Enter the following Azure parameter values for your subscription:
**** *azure subscription id*: Enter the subscription ID to use for the cluster.
**** *azure tenant id*: Enter the tenant ID.
+
... Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the *azure service principal client id*:
**** If you are using a service principal, enter its application ID.
**** If you are using a system-assigned managed identity, leave this value blank.
**** If you are using a user-assigned managed identity, specify its client ID.
+
... Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the *azure service principal client secret*:
**** If you are using a service principal, enter its password.
**** If you are using a system-assigned managed identity, leave this value blank.
**** If you are using a user-assigned managed identity, leave this value blank.
+
... Select the region to deploy the cluster to.
+
... Select the base domain to deploy the cluster to. The base domain corresponds
to the Azure DNS Zone that you created for your cluster.
+
... Select *gcp* as the platform to target.
+
... If you have not configured the service account key for your {gcp-short} account on
your computer, you must obtain it from {gcp-short} and paste the contents of the file
or enter the absolute path to the file.
+
... Select the project ID to provision the cluster in. The default value is
specified by the service account that you configured.
+
... Select the region to deploy the cluster to.
+
... Select the base domain to deploy the cluster to. The base domain corresponds
to the public DNS zone that you created for your cluster.
+
... Select *ibmcloud* as the platform to target.
+
... Select the region to deploy the cluster to.
+
... Select the base domain to deploy the cluster to. The base domain corresponds
to the public DNS zone that you created for your cluster.
+
... Select *powervs* as the platform to target.
+
... Select the region to deploy the cluster to.
+
... Select the zone to deploy the cluster to.
+
... Select the base domain to deploy the cluster to. The base domain corresponds
to the public DNS zone that you created for your cluster.
+
... Select *openstack* as the platform to target.
+
... Specify the {rh-openstack-first} external network name to use for installing the cluster.
+
... Specify the floating IP address to use for external access to the OpenShift API.
+
... Specify a {rh-openstack} flavor with at least 16 GB RAM to use for control plane nodes
and 8 GB RAM for compute nodes.
+
... Select the base domain to deploy the cluster to. All DNS records will be
sub-domains of this base and will also include the cluster name.
+
... Select *vsphere* as the platform to target.
+
... Specify the name of your vCenter instance.
+
... Specify the user name and password for the vCenter account that has the required permissions to create the cluster.
+
The installation program connects to your vCenter instance.
+
... Select the data center in your vCenter instance to connect to.
+
[NOTE]
====
After you create the installation configuration file, you can modify the file to create a multiple vSphere data center environment. This means that you can deploy an OpenShift Container Platform cluster to multiple vSphere data centers. For more information about creating this environment, see the section named _VMware vSphere region and zone enablement_.
====
+
... Select the default vCenter datastore to use.
+
[WARNING]
====
You can specify the path of any datastore that exists in a datastore cluster. By default, Storage Distributed Resource Scheduler (SDRS), which uses Storage vMotion, is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable Storage DRS to avoid data loss issues for your OpenShift Container Platform cluster.

You cannot specify more than one datastore path. If you must specify VMs across multiple datastores, use a `datastore` object to specify a failure domain in your cluster's `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement".
====
+
... Select the vCenter cluster to install the OpenShift Container Platform cluster in. The installation program uses the root resource pool of the vSphere cluster as the default resource pool.
+
... Select the network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.
+
... Enter the virtual IP address that you configured for control plane API access.
+
... Enter the virtual IP address that you configured for cluster ingress.
+
... Enter the base domain. This base domain must be the same one that you used in the DNS records that you configured.
+
... Select *nutanix* as the platform to target.
+
... Enter the Prism Central domain name or IP address.
+
... Enter the port that is used to log into Prism Central.
+
... Enter the credentials that are used to log into Prism Central.
+
The installation program connects to Prism Central.
+
... Select the Prism Element that will manage the OpenShift Container Platform cluster.
+
... Select the network subnet to use.
+
... Enter the virtual IP address that you configured for control plane API access.
+
... Enter the virtual IP address that you configured for cluster ingress.
+
... Enter the base domain. This base domain must be the same one that you configured in the DNS records.
+
... Enter a descriptive name for your cluster.
+
[IMPORTANT]
====
All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see Resolve reserved resource name errors in the Azure documentation.
====
+
+
... Paste the {cluster-manager-url-pull}.
The cluster name you enter must match the cluster name you specified when configuring the DNS records.
+
... Enter a name for your cluster. The name must be 14 or fewer characters long.

. Modify the `install-config.yaml` file. The AWS Outposts installation has the following limitations which require manual modification of the `install-config.yaml` file:
+
* Unlike AWS Regions, which offer near-infinite scale, AWS Outposts are limited by their provisioned capacity, EC2 family and generations, configured instance sizes, and availability of compute capacity that is not already consumed by other workloads. Therefore, when creating new OpenShift Container Platform cluster, you need to provide the supported instance type in the `compute.platform.aws.type` section in the configuration file.
* When deploying OpenShift Container Platform cluster with remote workers running in AWS Outposts, only one Availability Zone can be used for the compute instances - the Availability Zone in which the Outpost instance was created in. Therefore, when creating new OpenShift Container Platform cluster, it recommended to provide the relevant Availability Zone in the `compute.platform.aws.zones` section in the configuration file, in order to limit the compute instances to this Availability Zone.
* Amazon Elastic Block Store (EBS) gp3 volumes are not supported by the AWS Outposts service. This volume type is the default type used by the OpenShift Container Platform cluster. Therefore, when creating new OpenShift Container Platform cluster, you must change the volume type in the `compute.platform.aws.rootVolume.type` section to gp2.
You will find more information about how to change these values below.

. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.
.. Define the network and subnets for the VPC to install the cluster in under the parent `platform.gcp` field:
+
[source,yaml]
----
platform:
  gcp:
    network: <existing_vpc>
    controlPlaneSubnet: <control_plane_subnet>
    computeSubnet: <compute_subnet>
----
+
For the `platform.gcp.network` parameter, specify the name for the existing Google VPC. For the `platform.gcp.controlPlaneSubnet` and `platform.gcp.computeSubnet` parameters, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
.. Define the network and subnets for the VNet to install the cluster under the `platform.azure` field:
+
[source,yaml]
----
networkResourceGroupName: <vnet_resource_group>
virtualNetwork: <vnet>
controlPlaneSubnet: <control_plane_subnet>
computeSubnet: <compute_subnet>
----
+
where:
+
`<vnet_resource_group>`:: Specifies the resource group name that contains the existing virtual network (VNet).
`<vnet>`:: Specifies the existing virtual network name.
`<control_plane_subnet>`:: Specifies the existing subnet name to deploy the control plane machines.
`<compute_subnet>`:: Specifies the existing subnet name to deploy compute machines.
+
[NOTE]
====
If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster's control planes are schedulable. For more information, see "Installing a three-node cluster on {platform}".
====

. In the `install-config.yaml` file, set the value of `platform.openstack.clusterOSImage` to the image location or name. For example:
+
[source,yaml]
----
platform:
  openstack:
      clusterOSImage: http://mirror.example.com/images/rhcos-43.81.201912131630.0-openstack.x86_64.qcow2.gz?sha256=ffebbd68e8a1f2a245ca19522c16c86f67f9ac8e4e0c1f0a812b068b16f7265d
----

. Choose one of the following methods to speficy an {op-system} image for your cluster than runs in a {vmw-full} vCenter environment.
+
.. The `clusterOSImage` parameter method: In the `install-config.yaml` file, set the value of `platform.vsphere.clusterOSImage` to the image location or name. For example:
+
[source,yaml]
----
platform:
  vsphere:
      clusterOSImage: http://mirror.example.com/images/rhcos-43.81.201912131630.0-vmware.x86_64.ova?sha256=ffebbd68e8a1f2a245ca19522c16c86f67f9ac8e4e0c1f0a812b068b16f7265d
----
+
.. The `topology.template` parameter method:
+
... Download the *{op-system-first} - vSphere* image in Open Virtual Appliance (OVA) format to your local system. For more information, see "Creating the RHCOS image for restricted network installations".
+
... From the *Hosts and Clusters* tab on the {vmw-short} Client, right-click your cluster name and select *Deploy OVF Template*.
+
... On the *Select an OVF* tab, specify the name of the {op-system} OVA file that you downloaded.
+
... On the *Select a name and folder* tab, set a *Virtual machine name* for your template, such as `Template-{op-system}`.
+
... Click the name of your vSphere cluster and select the folder you created in the previous step.
+
... On the *Select a compute resource* tab, click the name of your vSphere cluster.
+
... On the *Select storage* tab, configure the storage options for your VM.
+
... When creating the OVF template, do not specify values on the *Customize template* tab or configure the template any further.
+
... In the `install-config.yaml` file, set the value of `topology.template` to the path where you imported the image to your {vmw-short} vCenter instance.
. In the `install-config.yaml` file, set the value of `platform.nutanix.clusterOSImage` to the image location or name. For example:
+
[source,yaml]
----
platform:
  nutanix:
      clusterOSImage: http://mirror.example.com/images/rhcos-47.83.202103221318-0-nutanix.x86_64.qcow2
----
. Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network.
+
.. Update the `pullSecret` value to contain the authentication information for
your registry:
+
[source,yaml]
----
pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
----
+
For `<mirror_host_name>`, specify the registry domain name
that you specified in the certificate for your mirror registry, and for
`<credentials>`, specify the base64-encoded user name and password for
your mirror registry.
+
.. Add the `additionalTrustBundle` parameter and value.
+
[source,yaml]
----
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
----
+
The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority, or the self-signed certificate that you generated for the mirror registry.
+
.. Define the subnets for the VPC to install the cluster in, as in the following example:
+
[source,yaml]
----
platform:
  aws:
    vpc:
      subnets:
        - id: subnet-<id_1>
        - id: subnet-<id_2>
        - id: subnet-<id_3>
----
+
.. Define the network and subnets for the VNet to install the cluster under the `platform.azure` field:
+
[source,yaml]
----
networkResourceGroupName: <vnet_resource_group>
virtualNetwork: <vnet>
controlPlaneSubnet: <control_plane_subnet>
computeSubnet: <compute_subnet>
----
+
where:
+
`<vnet_resource_group>`:: Specifies the resource group name that contains the existing virtual network (VNet).
`<vnet>`:: Specifies the existing virtual network name.
`<control_plane_subnet>`:: Specifies the existing subnet name to deploy the control plane machines.
`<compute_subnet>`:: Specifies the existing subnet name to deploy compute machines.
+
.. Define the network and subnets for the VPC to install the cluster in under the parent `platform.gcp` field:
+
[source,yaml]
----
platform:
  gcp:
    network: <existing_vpc>
    controlPlaneSubnet: <control_plane_subnet>
    computeSubnet: <compute_subnet>
----
+
For `platform.gcp.network`, specify the name for the existing Google VPC. For `platform.gcp.controlPlaneSubnet` and `platform.gcp.computeSubnet`, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
+
.. Define the network for the VPC to install the cluster in under the parent `platform.powervs` field:
+
[source,yaml]
----
vpcName: <existing_vpc>
----
+
For `platform.powervs.vpcName`, specify the name for the existing {ibm-cloud-name} VPC.
+
.. Define the network and subnets for the VPC to install the cluster in under the parent `platform.ibmcloud` field:
+
[source,yaml]
----
vpcName: <existing_vpc>
controlPlaneSubnets: <control_plane_subnet>
computeSubnets: <compute_subnet>
----
+
For `platform.ibmcloud.vpcName`, specify the name for the existing {ibm-cloud-title} Virtual Private Cloud (VPC) network. For `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
+
.. Add the image content resources, which resemble the following YAML excerpt:
+
[source,yaml]
----
imageContentSources:
- mirrors:
  - <mirror_host_name>:5000/<repo_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <mirror_host_name>:5000/<repo_name>/release
  source: registry.redhat.io/ocp/release
----
+
For these values, use the `imageContentSources` that you recorded during mirror registry creation.
For these values, use the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry.
+
.. If your Virtual Private Cloud (VPC) network is unable to access the public endpoints for the required {ibm-cloud-name} service endpoints, add the following stanza to `platform.ibmcloud` to override them using {ibm-cloud-name} Virtual Private Endpoints (VPE).
+
[source,yaml]
----
# ...
serviceEndpoints:
  - name: IAM
    url: <iam_private_endpoint_url>
  - name: VPC
    url: <vpc_private_endpoint_url>
  - name: ResourceController
    url: <resource_controller_private_endpoint_url>
  - name: ResourceManager
    url: <resource_manager_private_endpoint_url>
  - name: DNSServices
    url: <dns_services_private_endpoint_url>
  - name: COS
    url: <cos_private_endpoint_url>
  - name: GlobalSearch
    url: <global_search_private_endpoint_url>
  - name: GlobalTagging
    url: <global_tagging_private_endpoint_url>
# ...
----
+
[NOTE]
====
Only one VPE can be specified per service.
====
+
.. Optionally, set the publishing strategy to `Internal`:
+
[source,yaml]
----
publish: Internal
----
+
By setting this option, you create an internal Ingress Controller and a private load balancer.
+
[IMPORTANT]
====
Azure Firewall does not work seamlessly with Azure Public Load balancers. Thus, when using Azure Firewall for restricting internet access, the `publish` field in `install-config.yaml` should be set to `Internal`.
====
+
[NOTE]
====
If you use the default value of `External`, your network must be able to access the public endpoint for {ibm-cloud-name} Internet Services (CIS). CIS is not enabled for Virtual Private Endpoints.
====

. Make any other modifications to the `install-config.yaml` file that you require.
+
For more information about the parameters, see "Installation configuration parameters".

. Optional: Update one or more of the default configuration parameters in the `install.config.yaml` file to customize the installation.
+
For more information about the parameters, see "Installation configuration parameters".
+
[NOTE]
====
If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that cluster's control planes are schedulable. For more information, see "Installing a three-node cluster on {platform}".
====

. Back up the `install-config.yaml` file so that you can use
it to install multiple clusters.
+
[IMPORTANT]
====
The `install-config.yaml` file is consumed during the installation process. If
you want to reuse the file, you must back it up now.
====
+
If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform.

[role="_additional-resources"]
.Additional resources
* Installation configuration parameters for Nutanix

// Module included in the following assemblies:
//
// * installing/installing_nutanix/configuring-iam-nutanix.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc

[id="installation-nutanix-config-yaml_{context}"]
= Sample customized install-config.yaml file for Nutanix

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster's platform or modify the values of the required parameters.

[IMPORTANT]
====
This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.
====

[source,yaml]
----
apiVersion: v1
baseDomain: example.com <1>
compute: <2>
- hyperthreading: Enabled <3>
  name: worker
  replicas: 3
  platform:
    nutanix: <4>
      cpus: 2
      coresPerSocket: 2
      memoryMiB: 8196
      osDisk:
        diskSizeGiB: 120
      categories: <5>
      - key: <category_key_name>
        value: <category_value>
controlPlane: <2>
  hyperthreading: Enabled <3>
  name: master
  replicas: 3
  platform:
    nutanix: <4>
      cpus: 4
      coresPerSocket: 2
      memoryMiB: 16384
      osDisk:
        diskSizeGiB: 120
      categories: <5>
      - key: <category_key_name>
        value: <category_value>
metadata:
  creationTimestamp: null
  name: test-cluster <1>
networking:
  clusterNetwork:
    - cidr: 10.128.0.0/14
      hostPrefix: 23
  machineNetwork:
    - cidr: 10.0.0.0/16
  networkType: OVNKubernetes <6>
  serviceNetwork:
    - 172.30.0.0/16
platform:
  nutanix:
    apiVIPs:
      - 10.40.142.7 <1>
    defaultMachinePlatform:
      bootType: Legacy
      categories: <5>
      - key: <category_key_name>
        value: <category_value>
      project: <7>
        type: name
        name: <project_name>
    ingressVIPs:
      - 10.40.142.8 <1>
    prismCentral:
      endpoint:
        address: your.prismcentral.domainname <1>
        port: 9440 <1>
      password: <password> <1>
      username: <username> <1>
    prismElements:
    - endpoint:
        address: your.prismelement.domainname
        port: 9440
      uuid: 0005b0f1-8f43-a0f2-02b7-3cecef193712
    subnetUUIDs:
    - c7938dc6-7659-453e-a688-e26020c68e43
    clusterOSImage: http://example.com/images/rhcos-47.83.202103221318-0-nutanix.x86_64.qcow2 <8>
credentialsMode: Manual
publish: External
pullSecret: '{"auths": ...}' <1>
fips: false <9>
sshKey: ssh-ed25519 AAAA... <10>
sshKey: ssh-ed25519 AAAA... <9>
----
<1> Required. The installation program prompts you for this value.
<2> The `controlPlane` section is a single mapping, but the compute section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Although both sections currently define a single machine pool, it is possible that future versions of OpenShift Container Platform will support defining multiple compute pools during installation. Only one control plane pool is used.
<3> Whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.
+
[IMPORTANT]
====
If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.
====
<4> Optional: Provide additional configuration for the machine pool parameters for the compute and control plane machines.
<5> Optional: Provide one or more pairs of a prism category key and a prism category value. These category key-value pairs must exist in Prism Central. You can provide separate categories to compute machines, control plane machines, or all machines.
<6> The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.
<7> Optional: Specify a project with which VMs are associated. Specify either `name` or `uuid` for the project type, and then provide the corresponding UUID or project name. You can associate projects to compute machines, control plane machines, or all machines.
<8> Optional: By default, the installation program downloads and installs the {op-system-first} image. If Prism Central does not have internet access, you can override the default behavior by hosting the {op-system} image on any HTTP server and pointing the installation program to the image.
<9> Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.
+
[IMPORTANT]
====
When running {op-system-base-full} or {op-system-first} booted in FIPS mode, OpenShift Container Platform core components use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.
====
<10> Optional: You can provide the `sshKey` value that you use to access the machines in your cluster.
<7> Optional: By default, the installation program downloads and installs the {op-system-first} image. If Prism Central does not have internet access, you can override the default behavior by hosting the {op-system} image on any HTTP server and pointing the installation program to the image.
<8> Optional: You can provide the `sshKey` value that you use to access the machines in your cluster.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====

[source,yaml]
----
apiVersion: v1
baseDomain: example.com <1>
compute: <2>
- hyperthreading: Enabled <3>
  name: worker
  replicas: 3
  platform:
    nutanix: <4>
      cpus: 2
      coresPerSocket: 2
      memoryMiB: 8196
      osDisk:
        diskSizeGiB: 120
      categories: <5>
      - key: <category_key_name>
        value: <category_value>
controlPlane: <2>
  hyperthreading: Enabled <3>
  name: master
  replicas: 3
  platform:
    nutanix: <4>
      cpus: 4
      coresPerSocket: 2
      memoryMiB: 16384
      osDisk:
        diskSizeGiB: 120
      categories: <5>
      - key: <category_key_name>
        value: <category_value>
metadata:
  creationTimestamp: null
  name: test-cluster <1>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes <6>
  serviceNetwork:
  - 172.30.0.0/16
platform:
  nutanix:
    apiVIP: 10.40.142.7 <1>
    ingressVIP: 10.40.142.8 <1>
    defaultMachinePlatform:
      bootType: Legacy
      categories: <5>
      - key: <category_key_name>
        value: <category_value>
      project: <7>
        type: name
        name: <project_name>
    prismCentral:
      endpoint:
        address: your.prismcentral.domainname <1>
        port: 9440 <1>
      password: <password> <1>
      username: <username> <1>
    prismElements:
    - endpoint:
        address: your.prismelement.domainname
        port: 9440
      uuid: 0005b0f1-8f43-a0f2-02b7-3cecef193712
    subnetUUIDs:
    - c7938dc6-7659-453e-a688-e26020c68e43
    clusterOSImage: http://example.com/images/rhcos-47.83.202103221318-0-nutanix.x86_64.qcow2 <8>
credentialsMode: Manual
publish: External
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}' <9>
fips: false <10>
sshKey: ssh-ed25519 AAAA... <11>
sshKey: ssh-ed25519 AAAA... <10>
additionalTrustBundle: | <12>
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources: <13>
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
additionalTrustBundle: | <11>
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources: <12>
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
----
<1> Required. The installation program prompts you for this value.
<2> The `controlPlane` section is a single mapping, but the compute section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Although both sections currently define a single machine pool, it is possible that future versions of OpenShift Container Platform will support defining multiple compute pools during installation. Only one control plane pool is used.
<3> Whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.
+
[IMPORTANT]
====
If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.
====
<4> Optional: Provide additional configuration for the machine pool parameters for the compute and control plane machines.
<5> Optional: Provide one or more pairs of a prism category key and a prism category value. These category key-value pairs must exist in Prism Central. You can provide separate categories to compute machines, control plane machines, or all machines.
<6> The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.
<7> Optional: Specify a project with which VMs are associated. Specify either `name` or `uuid` for the project type, and then provide the corresponding UUID or project name. You can associate projects to compute machines, control plane machines, or all machines.
<8> Optional: By default, the installation program downloads and installs the {op-system-first} image. If Prism Central does not have internet access, you can override the default behavior by hosting the {op-system} image on any HTTP server or Nutanix Objects and pointing the installation program to the image.
<9> For `<local_registry>`, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example `registry.example.com` or `registry.example.com:5000`. For `<credentials>`,
specify the base64-encoded user name and password for your mirror registry.
<10> Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.
+
[IMPORTANT]
====
When running {op-system-base-full} or {op-system-first} booted in FIPS mode, OpenShift Container Platform core components use the {op-system-base} cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.
====
<11> Optional: You can provide the `sshKey` value that you use to access the machines in your cluster.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
<10> Optional: You can provide the `sshKey` value that you use to access the machines in your cluster.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
<12> Provide the contents of the certificate file that you used for your mirror registry.
<13> Provide these values from the `metadata.name: release-0` section of the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry.
<11> Provide the contents of the certificate file that you used for your mirror registry.
<12> Provide these values from the `metadata.name: release-0` section of the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry.

// Module included in the following assemblies:
//
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing_nutanix/installing-restricted-networks-nutanix-installer-provisioned.adoc

[id="installation-configuring-nutanix-failure-domains_{context}"]
= Configuring failure domains

Failure domains improve the fault tolerance of an OpenShift Container Platform cluster by distributing control plane and compute machines across multiple Nutanix Prism Elements (clusters).

[TIP]
====
It is recommended that you configure three failure domains to ensure high-availability.
====

.Prerequisites

* You have an installation configuration file (`install-config.yaml`).

.Procedure

. Edit the `install-config.yaml` file and add the following stanza to configure the first failure domain:
+
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
compute:
# ...
platform:
  nutanix:
    failureDomains:
    - name: <failure_domain_name>
      prismElement:
        name: <prism_element_name>
        uuid: <prism_element_uuid>
      subnetUUIDs:
      - <network_uuid>
# ...
----
+
where:

`<failure_domain_name>`:: Specifies a unique name for the failure domain. The name is limited to 64 or fewer characters, which can include lower-case letters, digits, and a dash (`-`). The dash cannot be in the leading or ending position of the name.
`<prism_element_name>`:: Optional. Specifies the name of the Prism Element.
`<prism_element_uuid`>:: Specifies the UUID of the Prism Element.
`<network_uuid`>:: Specifies the one or more UUIDs of the Prism Element subnet objects. Among them, one of the subnet's IP address prefixes (CIDRs) must contain the virtual IP addresses that the OpenShift Container Platform cluster uses. A maximum of 32 subnets for each failure domain (Prism Element) in an OpenShift Container Platform cluster is supported. All `subnetUUID` values must be unique.

. As required, configure additional failure domains.
. To distribute control plane and compute machines across the failure domains, do one of the following:

** If compute and control plane machines can share the same set of failure domains, add the failure domain names under the cluster's default machine configuration.
+
.Example of control plane and compute machines sharing a set of failure domains
+
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
compute:
# ...
platform:
  nutanix:
    defaultMachinePlatform:
      failureDomains:
        - failure-domain-1
        - failure-domain-2
        - failure-domain-3
# ...
----
** If compute and control plane machines must use different failure domains, add the failure domain names under the respective machine pools.
+
.Example of control plane and compute machines using different failure domains
+
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
compute:
# ...
controlPlane:
  platform:
    nutanix:
      failureDomains:
        - failure-domain-1
        - failure-domain-2
        - failure-domain-3
# ...
compute:
  platform:
    nutanix:
      failureDomains:
        - failure-domain-1
        - failure-domain-2
# ...
----

. Save the file.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing_aws-customizations.adoc
// * installing/installing_aws/installing_aws-private.adoc
// * installing/installing_aws/installing_aws-vpc.adoc
// * installing/installing_aws/installing_aws-china.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/
//installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * networking/configuring-a-custom-pki.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-configure-proxy_{context}"]
= Configuring the cluster-wide proxy during installation

[role="_abstract"]
Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform
cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

[NOTE]
====
For bare-metal installations, if you do not assign node IP addresses from the range that is specified in the `networking.machineNetwork[].cidr` field in the `install-config.yaml` file, you must include them in the `proxy.noProxy` field.
====

.Prerequisites
* You have an existing `install-config.yaml` file.

* You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, all cluster egress traffic is proxied, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object's `spec.noProxy` field to bypass the proxy if necessary.
+
[NOTE]
====
The `Proxy` object `status.noProxy` field is populated with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.

For installations on Amazon Web Services (AWS), {gcp-first}, Microsoft Azure, and {rh-openstack-first}, the `Proxy` object `status.noProxy` field is also populated with the instance metadata endpoint (`169.254.169.254`).
====

.Procedure

. Edit your `install-config.yaml` file and add the proxy settings. For example:
+
[source,yaml]
----
apiVersion: v1
baseDomain: my.domain.com
proxy:
  httpProxy: http://<username>:<pswd>@<ip>:<port>
  httpsProxy: https://<username>:<pswd>@<ip>:<port>
  noProxy: example.com
  noProxy: ec2.<aws_region>.amazonaws.com,elasticloadbalancing.<aws_region>.amazonaws.com,s3.<aws_region>.amazonaws.com
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
# ...
----
+
where:
+
`proxy.httpProxy`:: Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.
`proxy.httpsProxy`:: Specifies a proxy URL to use for creating HTTPS connections outside the cluster.
`proxy.noProxy`:: Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations.
If you have added the Amazon `EC2`, `Elastic Load Balancing`, and `S3` VPC endpoints to your VPC, you must add these endpoints to the `noProxy` field.
You must include vCenter's IP address and the IP range that you use for its machines.
`additionalTrustBundle`:: If provided, the installation program generates a config map that is named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you provide `additionalTrustBundle` and at least one proxy setting, the `Proxy` object is configured to reference the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the {op-system} trust bundle. The `additionalTrustBundle` field is required unless the proxy's identity certificate is signed by an authority from the {op-system} trust bundle.
`additionalTrustBundlePolicy`:: Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when `http/https` proxy is configured. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.
+
[NOTE]
====
The installation program does not support the proxy `readinessEndpoints` field.
====
+
[NOTE]
====
If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:

[source,terminal]
----
$ ./openshift-install wait-for install-complete --log-level debug
----
====

. Save the file and reference it when installing OpenShift Container Platform.
+
The installation program creates a cluster-wide proxy that is named `cluster` that uses the proxy settings in the provided `install-config.yaml` file. If no proxy settings are provided, a `cluster` `Proxy` object is still created, but it will have a nil `spec`.
+
[NOTE]
====
Only the `Proxy` object named `cluster` is supported, and no additional proxies can be created.
====

// Installing the OpenShift CLI on Linux
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-linux_{context}"]
= Installing the OpenShift CLI on Linux

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install the {oc-first} binary on Linux.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.

. Download `oc.tar.gz`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Linux Clients* entry and save the file.
. Navigate to the Download {OCP} page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Linux Clients* entry and save the file.
. Unpack the archive:
+
[source,terminal]
----
$ tar xvf <file>
----

. Place the `oc` binary in a directory that is on your `PATH`.
+
To check your `PATH`, execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

.Verification

* After you install the OpenShift CLI, it is available using the `oc` command:
+
[source,terminal]
----
$ oc <command>
----

// Installing the OpenShift CLI on Windows
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-windows_{context}"]
= Installing the OpenShift CLI on Windows

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install {oc-first} binary on Windows.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.
. Download `oc.zip`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Windows Client* entry and save the file.
. Navigate to the Download {OCP} page on the Red Hat Customer Portal.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Windows Client* entry and save the file.
. Extract the archive with a ZIP program.

. Move the `oc` binary to a directory that is on your `PATH` variable.
+
To check your `PATH` variable, open the command prompt and execute the following command:
+
[source,terminal]
----
C:\> path
----

.Verification

* After you install the OpenShift CLI, it is available using the `oc` command:
+
[source,terminal]
----
C:\> oc <command>
----

// Installing the OpenShift CLI on macOS
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-macos_{context}"]
= Installing the OpenShift CLI on macOS

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install the {oc-first} binary on macOS.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.
. Download `oc.tar.gz`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v macOS Clients* entry and save the file.
+
[NOTE]
====
For macOS arm64, choose the *OpenShift v macOS arm64 Client* entry.
====
. Navigate to the Download {OCP} on the Red{nbsp}Hat Customer Portal.
. Select the appropriate version from the *Version* drop-down list.

. Click *Download Now* next to the *OpenShift v macOS Clients* entry and save the file.

. Unpack and unzip the archive.

. Move the `oc` binary to a directory on your `PATH` variable.
+
To check your `PATH` variable, open a terminal and execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

.Verification

* Verify your installation by using an `oc` command:
+
[source,terminal]
----
$ oc <command>
----

// Module included in the following assemblies:
//
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc

[id="manually-create-iam-nutanix_{context}"]
= Configuring IAM for Nutanix

Installing the cluster requires that the Cloud Credential Operator (CCO) operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets.

.Prerequisites

* You have configured the `ccoctl` binary.

* You have an `install-config.yaml` file.

.Procedure

. Create a YAML file that contains the credentials data in the following format:
+
.Credentials data format
[source,yaml]
----
credentials:
- type: basic_auth <1>
  data:
    prismCentral: <2>
      username: <username_for_prism_central>
      password: <password_for_prism_central>
    prismElements: <3>
    - name: <name_of_prism_element>
      username: <username_for_prism_element>
      password: <password_for_prism_element>
----
<1> Specify the authentication type. Only basic authentication is supported.
<2> Specify the Prism Central credentials.
<3> Optional: Specify the Prism Element credentials.

. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----

. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \// <1>
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \// <2>
  --to=<path_to_directory_for_credentials_requests> <3>
----
<1> The `--included` parameter includes only the manifests that your specific cluster configuration requires.
<2> Specify the location of the `install-config.yaml` file.
<3> Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.
+
.Sample `CredentialsRequest` object
[source,yaml]
----
  apiVersion: cloudcredential.openshift.io/v1
  kind: CredentialsRequest
  metadata:
    annotations:
      include.release.openshift.io/self-managed-high-availability: "true"
    labels:
      controller-tools.k8s.io: "1.0"
    name: openshift-machine-api-nutanix
    namespace: openshift-cloud-credential-operator
  spec:
    providerSpec:
      apiVersion: cloudcredential.openshift.io/v1
      kind: NutanixProviderSpec
    secretRef:
      name: nutanix-credentials
      namespace: openshift-machine-api
----

. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:
+
[source,terminal]
----
$ ccoctl nutanix create-shared-secrets \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \// <1>
  --output-dir=<ccoctl_output_dir> \// <2>
  --credentials-source-filepath=<path_to_credentials_file> <3>
----
+
<1> Specify the path to the directory that contains the files for the component `CredentialsRequests` objects.
<2> Optional: Specify the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run.
<3> Optional: Specify the directory that contains the credentials data YAML file. By default, `ccoctl` expects this file to be in `<home_directory>/.nutanix/credentials`.

. Edit the `install-config.yaml` configuration file so that the `credentialsMode` parameter is set to `Manual`.
+
.Example `install-config.yaml` configuration file
[source,yaml]
----
apiVersion: v1
baseDomain: cluster1.example.com
credentialsMode: Manual <1>
...
----
<1> Add this line to set the `credentialsMode` parameter to `Manual`.

. Create the installation manifests by running the following command:
+
[source,terminal]
----
$ openshift-install create manifests --dir <installation_directory> <1>
----
<1> Specify the path to the directory that contains the `install-config.yaml` file for your cluster.

. Copy the generated credential files to the target manifests directory by running the following command:
+
[source,terminal]
----
$ cp <ccoctl_output_dir>/manifests/*credentials.yaml ./<installation_directory>/manifests
----

.Verification

* Ensure that the appropriate secrets exist in the `manifests` directory.
+
[source,terminal]
----
$ ls ./<installation_directory>/manifests
----
+
.Example output
[source,text]
----
cluster-config.yaml
cluster-dns-02-config.yml
cluster-infrastructure-02-config.yml
cluster-ingress-02-config.yml
cluster-network-01-crd.yml
cluster-network-02-config.yml
cluster-proxy-01-config.yaml
cluster-scheduler-02-config.yml
cvo-overrides.yaml
kube-cloud-config.yaml
kube-system-configmap-root-ca.yaml
machine-config-server-tls-secret.yaml
openshift-config-secret-pull-secret.yaml
openshift-cloud-controller-manager-nutanix-credentials-credentials.yaml
openshift-machine-api-nutanix-credentials-credentials.yaml
----

// Module included in the following assemblies:
//
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc

[id="nutanix-ccm-config_{context}"]
= Adding config map and secret resources required for Nutanix CCM

Installations on Nutanix require additional `ConfigMap` and `Secret` resources to integrate with the Nutanix Cloud Controller Manager (CCM).

.Prerequisites

* You have created a `manifests` directory within your installation directory.

.Procedure

. Navigate to the `manifests` directory:
+
[source,terminal]
----
$ cd <path_to_installation_directory>/manifests
----

. Create the `cloud-conf` `ConfigMap` file with the name `openshift-cloud-controller-manager-cloud-config.yaml` and add the following information:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cloud-conf
  namespace: openshift-cloud-controller-manager
data:
  cloud.conf: "{
      \"prismCentral\": {
          \"address\": \"<prism_central_FQDN/IP>\", <1>
          \"port\": 9440,
            \"credentialRef\": {
                \"kind\": \"Secret\",
                \"name\": \"nutanix-credentials\",
                \"namespace\": \"openshift-cloud-controller-manager\"
            }
       },
       \"topologyDiscovery\": {
           \"type\": \"Prism\",
           \"topologyCategories\": null
       },
       \"enableCustomLabeling\": true
     }"
----
<1> Specify the Prism Central FQDN/IP.

. Verify that the file `cluster-infrastructure-02-config.yml` exists and has the following information:
+
[source,yaml]
----
spec:
  cloudConfig:
    key: config
    name: cloud-provider-config
----

// Services for a user-managed load balancer
// Module included in the following assemblies:

// Bare metal
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc
// * installing/installing_bare_metal/bare-metal-postinstallation-configuration.adoc
// OpenStack
// * networking/load-balancing-openstack.adoc
// Nutanix
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// vSphere
// * installing/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing-restricted-networks-installer-provisioned-vsphere.adoc

[id="nw-osp-services-external-load-balancer_{context}"]
= Services for a user-managed load balancer

[role="_abstract"]
You can configure an OpenShift Container Platform cluster
on {rh-openstack-first}
to use a user-managed load balancer in place of the default load balancer.

[IMPORTANT]
====
Configuring a user-managed load balancer depends on your vendor's load balancer.

The information and examples in this section are for guideline purposes only. Consult the vendor documentation for more specific information about the vendor's load balancer.
====

Red Hat supports the following services for a user-managed load balancer:

* Ingress Controller
* OpenShift API
* OpenShift MachineConfig API

You can choose whether you want to configure one or all of these services for a user-managed load balancer. Configuring only the Ingress Controller service is a common configuration option. To better understand each service, view the following diagrams:

.Example network workflow that shows an Ingress Controller operating in an OpenShift Container Platform environment
image::external-load-balancer-default.png[An image that shows an example network workflow of an Ingress Controller operating in an OpenShift Container Platform environment.]

.Example network workflow that shows an OpenShift API operating in an OpenShift Container Platform environment
image::external-load-balancer-openshift-api.png[An image that shows an example network workflow of an OpenShift API operating in an OpenShift Container Platform environment.]

.Example network workflow that shows an OpenShift `MachineConfig` API operating in an OpenShift Container Platform environment
image::external-load-balancer-machine-config-api.png[An image that shows an example network workflow of an OpenShift `MachineConfig` API operating in an OpenShift Container Platform environment.]

The following configuration options are supported for user-managed load balancers:

* Use a node selector to map the Ingress Controller to a specific set of nodes. You must assign a static IP address to each node in this set, or configure each node to receive the same IP address from the Dynamic Host Configuration Protocol (DHCP). Infrastructure nodes commonly receive this type of configuration.

* Target all IP addresses on a subnet. This configuration can reduce the effort required to maintain the load balancer, because you can create and destroy nodes within those networks without reconfiguring the load balancer targets. If you deploy your ingress pods by using a machine set on a smaller network, such as a `/27` or `/28`, you can simplify your load balancer targets.
+
[TIP]
====
You can list all IP addresses that exist in a network by checking the machine config pool's resources.
====

Before you configure a user-managed load balancer for your OpenShift Container Platform cluster, consider the following information:

* For a front-end IP address, you can use the same IP address for the front-end IP address, the Ingress Controller load balancer, and API load balancer. Check the vendor's documentation for this capability.

* For a back-end IP address, ensure that an IP address for an OpenShift Container Platform control plane node does not change during the lifetime of the user-managed load balancer. You can achieve this by completing one of the following actions:
** Assign a static IP address to each control plane node.
** Configure each node to receive the same IP address from the DHCP every time the node requests a DHCP lease. Depending on the vendor, the DHCP lease might be in the form of an IP reservation or a static DHCP assignment.

* Manually define each node that runs the Ingress Controller in the user-managed load balancer for the Ingress Controller back-end service. For example, if the Ingress Controller moves to an undefined node, a connection outage can occur.

// Configuring a user-managed load balancer
// Module included in the following assemblies:

// Bare metal
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc
// * installing/installing_bare_metal/bare-metal-postinstallation-configuration.adoc
// OpenStack
// * networking/load-balancing-openstack.adoc
// Nutanix
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// vSphere
// * installing/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing-restricted-networks-installer-provisioned-vsphere.adoc

[id="nw-osp-configuring-external-load-balancer_{context}"]
= Configuring a user-managed load balancer

[role="_abstract"]
You can configure an OpenShift Container Platform cluster
on {rh-openstack-first}
to use a user-managed load balancer in place of the default load balancer.

[IMPORTANT]
====
Before you configure a user-managed load balancer, ensure that you read the "Services for a user-managed load balancer" section.
====

Read the following prerequisites that apply to the service that you want to configure for your user-managed load balancer.

[NOTE]
====
MetalLB, which runs on a cluster, functions as a user-managed load balancer.
====

.Prerequisites

The following list details OpenShift API prerequisites:

* You defined a front-end IP address.
* TCP ports 6443 and 22623 are exposed on the front-end IP address of your load balancer. Check the following items:
** Port 6443 provides access to the OpenShift API service.
** Port 22623 can provide ignition startup configurations to nodes.
* The front-end IP address and port 6443 are reachable by all users of your system with a location external to your OpenShift Container Platform cluster.
* The front-end IP address and port 22623 are reachable only by OpenShift Container Platform nodes.
* The load balancer backend can communicate with OpenShift Container Platform control plane nodes on port 6443 and 22623.

The following list details Ingress Controller prerequisites:

* You defined a front-end IP address.
* TCP port 443 and port 80 are exposed on the front-end IP address of your load balancer.
* The front-end IP address, port 80 and port 443 are reachable by all users of your system with a location external to your OpenShift Container Platform cluster.
* The front-end IP address, port 80 and port 443 are reachable by all nodes that operate in your OpenShift Container Platform cluster.
* The load balancer backend can communicate with OpenShift Container Platform nodes that run the Ingress Controller on ports 80, 443, and 1936.

The following list details prerequisites for health check URL specifications:

You can configure most load balancers by setting health check URLs that determine if a service is available or unavailable. OpenShift Container Platform provides these health checks for the OpenShift API, Machine Configuration API, and Ingress Controller backend services.

The following example shows a Kubernetes API health check specification for a backend service:

[source,terminal]
----
Path: HTTPS:6443/readyz
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 10
Interval: 10
----

The following example shows a Machine Config API health check specification for a backend service:

[source,terminal]
----
Path: HTTPS:22623/healthz
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 10
Interval: 10
----

The following example shows a Ingress Controller health check specification for a backend service:

[source,terminal]
----
Path: HTTP:1936/healthz/ready
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 5
Interval: 10
----

.Procedure

. Configure the HAProxy Ingress Controller, so that you can enable access to the cluster from your load balancer on ports 6443, 22623, 443, and 80. Depending on your needs, you can specify the IP address of a single subnet or IP addresses from multiple subnets in your HAProxy configuration.
+
.Example HAProxy configuration with one listed subnet
[source,terminal,subs="quotes"]
----
# ...
listen my-cluster-api-6443
    bind 192.168.1.100:6443
    mode tcp
    balance roundrobin
  option httpchk
  http-check connect
  http-check send meth GET uri /readyz
  http-check expect status 200
    server my-cluster-master-2 192.168.1.101:6443 check inter 10s rise 2 fall 2
    server my-cluster-master-0 192.168.1.102:6443 check inter 10s rise 2 fall 2
    server my-cluster-master-1 192.168.1.103:6443 check inter 10s rise 2 fall 2

listen my-cluster-machine-config-api-22623
    bind 192.168.1.100:22623
    mode tcp
    balance roundrobin
  option httpchk
  http-check connect
  http-check send meth GET uri /healthz
  http-check expect status 200
    server my-cluster-master-2 192.168.1.101:22623 check inter 10s rise 2 fall 2
    server my-cluster-master-0 192.168.1.102:22623 check inter 10s rise 2 fall 2
    server my-cluster-master-1 192.168.1.103:22623 check inter 10s rise 2 fall 2

listen my-cluster-apps-443
    bind 192.168.1.100:443
    mode tcp
    balance roundrobin
  option httpchk
  http-check connect
  http-check send meth GET uri /healthz/ready
  http-check expect status 200
    server my-cluster-worker-0 192.168.1.111:443 check port 1936 inter 10s rise 2 fall 2
    server my-cluster-worker-1 192.168.1.112:443 check port 1936 inter 10s rise 2 fall 2
    server my-cluster-worker-2 192.168.1.113:443 check port 1936 inter 10s rise 2 fall 2

listen my-cluster-apps-80
   bind 192.168.1.100:80
   mode tcp
   balance roundrobin
  option httpchk
  http-check connect
  http-check send meth GET uri /healthz/ready
  http-check expect status 200
    server my-cluster-worker-0 192.168.1.111:80 check port 1936 inter 10s rise 2 fall 2
    server my-cluster-worker-1 192.168.1.112:80 check port 1936 inter 10s rise 2 fall 2
    server my-cluster-worker-2 192.168.1.113:80 check port 1936 inter 10s rise 2 fall 2
# ...
----
+
.Example HAProxy configuration with multiple listed subnets
[source,terminal,subs="quotes"]
----
# ...
listen api-server-6443
    bind *:6443
    mode tcp
      server master-00 192.168.83.89:6443 check inter 1s
      server master-01 192.168.84.90:6443 check inter 1s
      server master-02 192.168.85.99:6443 check inter 1s
      server bootstrap 192.168.80.89:6443 check inter 1s

listen machine-config-server-22623
    bind *:22623
    mode tcp
      server master-00 192.168.83.89:22623 check inter 1s
      server master-01 192.168.84.90:22623 check inter 1s
      server master-02 192.168.85.99:22623 check inter 1s
      server bootstrap 192.168.80.89:22623 check inter 1s

listen ingress-router-80
    bind *:80
    mode tcp
    balance source
      server worker-00 192.168.83.100:80 check inter 1s
      server worker-01 192.168.83.101:80 check inter 1s

listen ingress-router-443
    bind *:443
    mode tcp
    balance source
      server worker-00 192.168.83.100:443 check inter 1s
      server worker-01 192.168.83.101:443 check inter 1s

listen ironic-api-6385
    bind *:6385
    mode tcp
    balance source
      server master-00 192.168.83.89:6385 check inter 1s
      server master-01 192.168.84.90:6385 check inter 1s
      server master-02 192.168.85.99:6385 check inter 1s
      server bootstrap 192.168.80.89:6385 check inter 1s

listen inspector-api-5050
    bind *:5050
    mode tcp
    balance source
      server master-00 192.168.83.89:5050 check inter 1s
      server master-01 192.168.84.90:5050 check inter 1s
      server master-02 192.168.85.99:5050 check inter 1s
      server bootstrap 192.168.80.89:5050 check inter 1s
# ...
----

. Use the `curl` CLI command to verify that the user-managed load balancer and its resources are operational:
+
.. Verify that the cluster machine configuration API is accessible to the Kubernetes API server resource, by running the following command and observing the response:
+
[source,terminal]
----
$ curl https://<loadbalancer_ip_address>:6443/version --insecure
----
+
If the configuration is correct, you receive a JSON object in response:
+
[source,json]
----
{
  "major": "1",
  "minor": "11+",
  "gitVersion": "v1.11.0+ad103ed",
  "gitCommit": "ad103ed",
  "gitTreeState": "clean",
  "buildDate": "2019-01-09T06:44:10Z",
  "goVersion": "go1.10.3",
  "compiler": "gc",
  "platform": "linux/amd64"
}
----
+
.. Verify that the cluster machine configuration API is accessible to the Machine config server resource, by running the following command and observing the output:
+
[source,terminal]
----
$ curl -v https://<loadbalancer_ip_address>:22623/healthz --insecure
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 200 OK
Content-Length: 0
----
+
.. Verify that the controller is accessible to the Ingress Controller resource on port 80, by running the following command and observing the output:
+
[source,terminal]
----
$ curl -I -L -H "Host: console-openshift-console.apps.<cluster_name>.<base_domain>" http://<load_balancer_front_end_IP_address>
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 302 Found
content-length: 0
location: https://console-openshift-console.apps.ocp4.private.opequon.net/
cache-control: no-cache
----
+
.. Verify that the controller is accessible to the Ingress Controller resource on port 443, by running the following command and observing the output:
+
[source,terminal]
----
$ curl -I -L --insecure --resolve console-openshift-console.apps.<cluster_name>.<base_domain>:443:<Load Balancer Front End IP Address> https://console-openshift-console.apps.<cluster_name>.<base_domain>
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 200 OK
referrer-policy: strict-origin-when-cross-origin
set-cookie: csrf-token=UlYWOyQ62LWjw2h003xtYSKlh1a0Py2hhctw0WmV2YEdhJjFyQwWcGBsja261dGLgaYO0nxzVErhiXt6QepA7g==; Path=/; Secure; SameSite=Lax
x-content-type-options: nosniff
x-dns-prefetch-control: off
x-frame-options: DENY
x-xss-protection: 1; mode=block
date: Wed, 04 Oct 2023 16:29:38 GMT
content-type: text/html; charset=utf-8
set-cookie: 1e2670d92730b515ce3a1bb65da45062=1bf5e9573c9a2760c964ed1659cc1673; path=/; HttpOnly; Secure; SameSite=None
cache-control: private
----

. Configure the DNS records for your cluster to target the front-end IP addresses of the user-managed load balancer. You must update records to your DNS server for the cluster API and applications over the load balancer. The following examples shows modified DNS records:
+
[source,dns]
----
<load_balancer_ip_address>  A  api.<cluster_name>.<base_domain>
A record pointing to Load Balancer Front End
----
+
[source,dns]
----
<load_balancer_ip_address>   A apps.<cluster_name>.<base_domain>
A record pointing to Load Balancer Front End
----
+
[IMPORTANT]
====
DNS propagation might take some time for each DNS record to become available. Ensure that each DNS record propagates before validating each record.
====

. For your OpenShift Container Platform cluster to use the user-managed load balancer, you must specify the following configuration in your cluster's `install-config.yaml` file:
+
[source,yaml]
----
# ...
platform:
  bare-metal:
  openstack:
  nutanix:
  vsphere:
    loadBalancer:
      type: <loadBalancer_type>
    apiVIPs:
    - <api_ip>
    ingressVIPs:
    - <ingress_ip>
# ...
----
+
where:
+
`<loadBalancer_type>`:: Specifies the load balancer type. Set to `UserManaged` to specify a user-managed load balancer for your cluster. The parameter defaults to `OpenShiftManagedDefault`, which denotes the default internal load balancer. For services defined in an `openshift-kni-infra` namespace, a user-managed load balancer can deploy the `coredns` service to pods in your cluster but ignores `keepalived` and `haproxy` services.
`<api_ip>`:: Specifies the user-managed load balancer's public IP address for the Kubernetes API. Mandatory parameter.
`<ingress_ip>`:: Specifies the user-managed load balancer's public IP address for ingress traffic. Mandatory parameter.

.Verification

. Use the `curl` CLI command to verify that the user-managed load balancer and DNS record configuration are operational:
+
.. Verify that you can access the cluster API, by running the following command and observing the output:
+
[source,terminal]
----
$ curl https://api.<cluster_name>.<base_domain>:6443/version --insecure
----
+
If the configuration is correct, you receive a JSON object in response:
+
[source,json]
----
{
  "major": "1",
  "minor": "11+",
  "gitVersion": "v1.11.0+ad103ed",
  "gitCommit": "ad103ed",
  "gitTreeState": "clean",
  "buildDate": "2019-01-09T06:44:10Z",
  "goVersion": "go1.10.3",
  "compiler": "gc",
  "platform": "linux/amd64"
  }
----
+
.. Verify that you can access the cluster machine configuration, by running the following command and observing the output:
+
[source,terminal]
----
$ curl -v https://api.<cluster_name>.<base_domain>:22623/healthz --insecure
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 200 OK
Content-Length: 0
----
+
.. Verify that you can access each cluster application on port 80, by running the following command and observing the output:
+
[source,terminal]
----
$ curl http://console-openshift-console.apps.<cluster_name>.<base_domain> -I -L --insecure
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 302 Found
content-length: 0
location: https://console-openshift-console.apps.<cluster-name>.<base domain>/
cache-control: no-cacheHTTP/1.1 200 OK
referrer-policy: strict-origin-when-cross-origin
set-cookie: csrf-token=39HoZgztDnzjJkq/JuLJMeoKNXlfiVv2YgZc09c3TBOBU4NI6kDXaJH1LdicNhN1UsQWzon4Dor9GWGfopaTEQ==; Path=/; Secure
x-content-type-options: nosniff
x-dns-prefetch-control: off
x-frame-options: DENY
x-xss-protection: 1; mode=block
date: Tue, 17 Nov 2020 08:42:10 GMT
content-type: text/html; charset=utf-8
set-cookie: 1e2670d92730b515ce3a1bb65da45062=9b714eb87e93cf34853e87a92d6894be; path=/; HttpOnly; Secure; SameSite=None
cache-control: private
----
+
.. Verify that you can access each cluster application on port 443, by running the following command and observing the output:
+
[source,terminal]
----
$ curl https://console-openshift-console.apps.<cluster_name>.<base_domain> -I -L --insecure
----
+
If the configuration is correct, the output from the command shows the following response:
+
[source,terminal]
----
HTTP/1.1 200 OK
referrer-policy: strict-origin-when-cross-origin
set-cookie: csrf-token=UlYWOyQ62LWjw2h003xtYSKlh1a0Py2hhctw0WmV2YEdhJjFyQwWcGBsja261dGLgaYO0nxzVErhiXt6QepA7g==; Path=/; Secure; SameSite=Lax
x-content-type-options: nosniff
x-dns-prefetch-control: off
x-frame-options: DENY
x-xss-protection: 1; mode=block
date: Wed, 04 Oct 2023 16:29:38 GMT
content-type: text/html; charset=utf-8
set-cookie: 1e2670d92730b515ce3a1bb65da45062=1bf5e9573c9a2760c964ed1659cc1673; path=/; HttpOnly; Secure; SameSite=None
cache-control: private
----

// Deploying the cluster
// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-specialized-region.adoc
// * installing/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-ibm-cloud-customizations.adoc
// * installing/installing_gcp/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// If you use this module in any other assembly, you must update the ifeval
// statements.

[id="installation-launching-installer_{context}"]
= Deploying the cluster

[role="_abstract"]
To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

[IMPORTANT]
====
You can run the `create cluster` command of the installation program only once, during initial installation.
====

.Prerequisites

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
+
If the {op-system-first} image is available locally, the host running the installation program does not require internet access.
* You have an Azure subscription ID and tenant ID.
* You have the application ID and password of a service principal.
* If you are installing the cluster using a service principal, you have its application ID and password.
* If you are installing the cluster using a system-assigned managed identity, you have enabled it on the virtual machine that you will run the installation program from.
* If you are installing the cluster using a user-assigned managed identity, you have met these prerequisites:
** You have its client ID.
** You have assigned it to the virtual machine that you will run the installation program from.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.
* Optional: Before you create the cluster, you configured an external load balancer in place of the default load balancer.
+
[IMPORTANT]
====
You do not need to specify API and Ingress static addresses for your installation program. If you choose this configuration, you must take additional actions to define network targets that accept an IP address from each referenced vSphere subnet. See the section "Configuring a user-managed load balancer".
====

.Procedure
. Remove any existing {gcp-short} credentials that do not use the service account key
for the {gcp-short} account that you configured for your cluster and that are stored in the
following locations:
** The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON`
environment variables
** The `~/.gcp/osServiceAccount.json` file
** The `gcloud cli` default credentials

. Optional: If you have run the installation program on this computer before, and want to use an alternative service principal, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file.
+
Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation.
. Optional: If you have run the installation program on this computer before, and want to use an alternative service principal or managed identity, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file.
+
Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation.
. Export the `OPENSHIFT_INSTALL_OS_IMAGE_OVERRIDE` variable to specify the location of the {op-system-first} image by running the following command:
+
[source,terminal]
----
$ export OPENSHIFT_INSTALL_OS_IMAGE_OVERRIDE="<path_to_image>/rhcos-<image_version>-ibmcloud.x86_64.qcow2.gz"
----
. In the directory that contains the installation program, initialize the cluster deployment by running the following command:
* In the directory that contains the installation program, initialize the cluster deployment by running the following command:
+
[source,terminal]
----
$ ./openshift-install create cluster --dir <installation_directory> \
    --log-level=info
----
+
** For `<installation_directory>`, specify the
location of your customized `./install-config.yaml` file.
directory name to store the files that the installation program creates.
** To view different installation details, specify `warn`, `debug`, or
`error` instead of `info`.

+
If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values.
. Enter the following Azure parameter values for your subscription:
** *azure subscription id*: Enter the subscription ID to use for the cluster.
** *azure tenant id*: Enter the tenant ID.
. Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the *azure service principal client id*:
** If you are using a service principal, enter its application ID.
** If you are using a system-assigned managed identity, leave this value blank.
** If you are using a user-assigned managed identity, specify its client ID.
. Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the *azure service principal client secret*:
** If you are using a service principal, enter its password.
** If you are using a system-assigned managed identity, leave this value blank.
** If you are using a user-assigned managed identity,leave this value blank.
+
[NOTE]
====
If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform.
====

+
When specifying the directory:
* Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
* Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

. Provide values at the prompts:

.. Optional: Select an SSH key to use to access your cluster machines.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
.. Select *aws* as the platform to target.
.. If you do not have an Amazon Web Services (AWS) profile stored on your computer, enter the AWS access key ID and secret access key for the user that you configured to run the
installation program.
+
[NOTE]
====
The AWS access key ID and secret access key are stored in `~/.aws/credentials` in the home directory of the current user on the installation host. You are prompted for the credentials by the installation program if the credentials for the exported profile are not present in the file. Any credentials that you provide to the installation program are stored in the file.
====
.. Select the AWS region to deploy the cluster to.
.. Select the base domain for the Route 53 service that you configured for your cluster.
.. Select *azure* as the platform to target.
+
If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values.
.. Specify the following Azure parameter values for your subscription and service principal:
*** *azure subscription id*: Enter the subscription ID to use for the cluster.
*** *azure tenant id*: Enter the tenant ID.
*** *azure service principal client id*: Enter its application ID.
*** *azure service principal client secret*: Enter its password.
.. Select the region to deploy the cluster to.
.. Select the base domain to deploy the cluster to. The base domain corresponds to the Azure DNS Zone that you created for your cluster.
.. Select *gcp* as the platform to target.
.. If you have not configured the service account key for your {gcp-short} account on
your host, you must obtain it from {gcp-short} and paste the contents of the file
or enter the absolute path to the file.
.. Select the project ID to provision the cluster in. The default value is
specified by the service account that you configured.
.. Select the region to deploy the cluster to.
.. Select the base domain to deploy the cluster to. The base domain corresponds
to the public DNS zone that you created for your cluster.
.. test
.. Select *openstack* as the platform to target.
.. Specify the {rh-openstack-first} external network name to use for installing the cluster.
.. Specify the Floating IP address to use for external access to the OpenShift API.
.. Specify the {rh-openstack} flavor with at least 16 GB RAM to use for control plane
and compute nodes.
.. Select the base domain to deploy the cluster to. All DNS records will be
sub-domains of this base and will also include the cluster name.
.. Select *vsphere* as the platform to target.
.. Specify the name of your vCenter instance.
.. Specify the user name and password for the vCenter account that has the required permissions to create the cluster.
+
The installation program connects to your vCenter instance.
+
[IMPORTANT]
====
Some VMware vCenter Single Sign-On (SSO) environments with Active Directory (AD) integration might primarily require you to use the traditional login method, which requires the `<domain>\` construct.

To ensure that vCenter account permission checks complete properly, consider using the User Principal Name (UPN) login method, such as `<username>@<fully_qualified_domainname>`.
====

.. Select the data center in your vCenter instance to connect to.
.. Select the default vCenter datastore to use.
+
[NOTE]
====
Datastore and cluster names cannot exceed 60 characters; therefore, ensure the combined string length does not exceed the 60 character limit.
====
.. Select the vCenter cluster to install the OpenShift Container Platform cluster in. The installation program uses the root resource pool of the vSphere cluster as the default resource pool.
.. Select the network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.
.. Enter the virtual IP address that you configured for control plane API access.
.. Enter the virtual IP address that you configured for cluster ingress.
.. Enter the base domain. This base domain must be the same one that you used in the DNS records that you configured.
.. Enter a descriptive name for your cluster.
The cluster name must be the same one that you used in the DNS records that you configured.
+
[NOTE]
====
Datastore and cluster names cannot exceed 60 characters; therefore, ensure the combined string length does not exceed the 60 character limit.
====
+
[IMPORTANT]
====
All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see
Resolve reserved resource name errors in the Azure documentation.
====
If you provide a name that is longer
than 6 characters, only the first 6 characters will be used in the infrastructure
ID that is generated from the cluster name.
.. Paste the {cluster-manager-url-pull}.
.. Paste the {cluster-manager-url-pull}.
* If you do not have a {cluster-manager-url-pull}, you can paste the pull secret another private registry.
* If you do not need the cluster to pull images from a private registry, you can paste `{"auths":{"fake":{"auth":"aWQ6cGFzcwo="}}}` as the pull secret.

+
[NOTE]
====
If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform.
====

. Optional: Remove or disable the `AdministratorAccess` policy from the IAM
account that you used to install the cluster.
+
[NOTE]
====
The elevated permissions provided by the `AdministratorAccess` policy are required only during installation.
====

. Optional: You can reduce the number of permissions for the service account that you used to install the cluster.
** If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.
** If you included the `Service Account Key Admin` role,
you can remove it.

.Verification

When the cluster deployment completes successfully:

* The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.

* Credential information also outputs to `<installation_directory>/.openshift_install.log`.
+
[IMPORTANT]
====
Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.
====
+
.Example output
[source,terminal]
----
...
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
INFO Login to the console with user: "kubeadmin", and password: "password"
INFO Time elapsed: 36m22s
----
+
[IMPORTANT]
====
* The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

// Module included in the following assemblies:
//
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc

[id="registry-configuring-storage-nutanix_{context}"]
= Configuring the default storage container

After you install the cluster, you must install the Nutanix CSI Operator and configure the default storage container for the cluster.

For more information, see the Nutanix documentation for installing the CSI Operator and configuring registry storage.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone.adoc
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_openstack/installing-openstack-user-sr-iov.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="cluster-telemetry_{context}"]
= Telemetry access for OpenShift Container Platform

[role="_abstract"]
To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to {cluster-manager-url}.

After you confirm that your {cluster-manager-url} inventory is correct, either maintained automatically by Telemetry or manually by using {cluster-manager},use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat's subscription services" in the _Additional resources_ section.

[role="_additional-resources"]
== Additional resources

* About remote health monitoring

== Next steps
* Remote health reporting
* Customize your cluster
