---
title: "Installing a cluster on {gcp-short} with customizations"
type: reference
domain: openshift
slug: installing-4-22-installing-gcp-customizations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-gcp-customizations
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on {gcp-short} with customizations

[id="installing-gcp-customizations"]
= Installing a cluster on {gcp-short} with customizations

In OpenShift Container Platform version , you can install a cluster on {gcp-first} by using installer-provisioned infrastructure with customizations, including network configuration options. In each, you modify parameters in the `install-config.yaml` file before you install the cluster.

By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations.

You must set most of the network configuration parameters during installation, and you can modify only `kubeProxy` configuration parameters in a running cluster.

== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You configured a {gcp-short} project to host the cluster.
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.

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
* Installation configuration parameters for {gcp-first}

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud_public/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud_public/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud_public/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud_public/installing-ibm-cloud-restricted.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc
// * installing/installing_bare_metal_ipi/ipi-install-prerequisites.adoc
// * installing/installing_ibm_z/installing-ibm-z-reqs.adoc

[id="installation-minimum-resource-requirements_{context}"]
= Minimum resource requirements for cluster installation

[role="_abstract"]
Each created cluster must meet minimum requirements so that the cluster runs as expected.

.Minimum resource requirements
[cols="2,2,2,2,2,2",options="header"]
|===

|Machine
|Operating System
|vCPU ^[1]^
|vCPU
|Virtual RAM
|CPU ^[1]^
|RAM
|Storage
|Input/Output Per Second (IOPS)^[2]^
|Input/Output Per Second (IOPS)^[1]^
|Input/Output Per Second (IOPS)

|Bootstrap
|16 GB
|100 GB
|300
|N/A

|Control plane
|{op-system}
|16 GB
|100 GB
|300
|N/A

|Compute
|2
|8 GB
|100 GB
|300
|N/A

|Compute
|{op-system}
|2
|8 GB
|100 GB
|300
|N/A
|===
[.small]
--
1. One physical core (IFL) provides two logical cores (threads) when SMT-2 is enabled. The hypervisor can provide two or more vCPUs.
1. One CPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = CPUs.
1. One vCPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
2. OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.
3. As with all user-provisioned installations, if you choose to use {op-system-base} compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of {op-system-base} 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.
2. OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.
1. OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.
2. As with all user-provisioned installations, if you choose to use {op-system-base} compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of {op-system-base} 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.
--
[NOTE]
====
For OpenShift Container Platform version 4.22, {op-system} is based on {op-system-base} version 9.8, which has the micro-architecture requirements. The following list contains the minimum instruction set architectures (ISA) that each architecture requires:

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* IBM Power architecture requires Power 9 ISA
* s390x architecture requires z14 ISA

For more information, see Architectures ({op-system-base} documentation).
====

[IMPORTANT]
====
You are required to use Azure virtual machines that have the `premiumIO` parameter set to `true`.
====

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

[IMPORTANT]
====
Do not use memory ballooning in OpenShift Container Platform clusters. Memory ballooning can cause cluster-wide instabilities, service degradation, or other undefined behaviors.

* Control plane machines should have committed memory equal to or greater than the published minimum resource requirements for a cluster installation.

* Compute machines should have a minimum reservation equal to or greater than the published minimum resource requirements for a cluster installation.

These minimum CPU and memory requirements do not account for resources required by user workloads.

For more information, see the Red Hat Knowledgebase article Memory Ballooning and OpenShift.
====

[role="_additional-resources"]
.Additional resources

* Optimizing storage

// Module included in the following assemblies:
//
// installing/installing_gcp/installing-gcp-customizations.adoc
// installing/installing_gcp/installing-gcp-network-customizations.adoc
// installing/installing_gcp/installing-gcp-private.adoc
// installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// installing/installing_gcp/installing-gcp-user-infra.adoc
// installing/installing_gcp/installing-gcp-vpc.adoc
// installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-tested-machine-types_{context}"]
= Tested instance types for {gcp-short}

The following {gcp-full} instance types have been tested with OpenShift Container Platform.

[NOTE]
====
Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see regions and zones (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see machine series support for Hyperdisk (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in _Storage_.
====

.Machine series
[%collapsible]
====

====

// module included in the following assemblies
//
// installing/installing_gcp/installing-gcp-customizations.adoc
// installing/installing_gcp/installing-gcp-network-customizations.adoc
// installing/installing_gcp/installing-gcp-private.adoc
// installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// installing/installing_gcp/installing-gcp-user-infra.adoc
// installing/installing_gcp/installing-gcp-vpc.adoc
// installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-tested-machine-types-arm_{context}"]
= Tested instance types for {gcp-short} on 64-bit ARM infrastructures

The following {gcp-first} 64-bit ARM instance types have been tested with OpenShift Container Platform.

.Machine series for 64-bit ARM machines
[%collapsible]
====

====

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-custom-machine-types_{context}"]
= Using custom machine types

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:
+
--
`custom-<number_of_cpus>-<amount_of_memory_in_mb>`

For example, `custom-6-20480`.
--

As part of the installation process, you specify the custom machine type in the `install-config.yaml` file.

.Sample `install-config.yaml` file with a custom machine type

[source,yaml]
----
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: custom-6-20480
  replicas: 2
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: custom-6-20480
  replicas: 3
----

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-enabling-shielded-vms_{context}"]
= Enabling Shielded VMs

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google's documentation on Shielded VMs.

[NOTE]
====
Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.
====

.Procedure

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:
.. To use shielded VMs for only control plane machines:
+
[source,yaml]
----
controlPlane:
  platform:
    gcp:
       secureBoot: Enabled
----
+
.. To use shielded VMs for only compute machines:
+
[source,yaml]
----
compute:
- platform:
    gcp:
       secureBoot: Enabled
----
+
.. To use shielded VMs for all machines:
+
[source,yaml]
----
platform:
  gcp:
    defaultMachinePlatform:
       secureBoot: Enabled
----

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-gcp-enabling-confidential-vms_{context}"]
= Enabling Confidential VMs

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google's documentation on Confidential Computing. You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

[NOTE]
====
Confidential VMs are currently not supported on 64-bit ARM architectures.
====

.Procedure

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:
.. To use confidential VMs for only control plane machines:
+
[source,yaml]
----
controlPlane:
  platform:
    gcp:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging <1>
       type: n2d-standard-8 <2>
       onHostMaintenance: Terminate <3>
----
+
--
<1> Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional {gcp-first} configuration parameters".
<2> Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see Supported operating systems and machine types.
<3> Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
--
+
.. To use confidential VMs for only compute machines:
+
[source,yaml]
----
compute:
- platform:
    gcp:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging
       type: n2d-standard-8
       onHostMaintenance: Terminate
----
+
.. To use confidential VMs for all machines:
+
[source,yaml]
----
platform:
  gcp:
    defaultMachinePlatform:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging
       type: n2d-standard-8
       onHostMaintenance: Terminate
----

[role="_additional-resources"]
.Additional resources
* Additional {gcp-first} configuration parameters

[id="installation-gcp-enabling-user-managed-DNS_{context}"]
= Enabling a user-managed DNS

[role="_abstract"]
You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud.

For example, your organization's security policies might not allow the use of public DNS services such as {gcp-full} DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

.Prerequisites

* You installed the `jq` package.

.Procedure
* Before you deploy your cluster, use a text editor to open the `install-config.yaml` file  and add the following stanza:
** To enable user-managed DNS:
+
[source,yaml]
----
platform:
  gcp:
    userProvisionedDNS: Enabled
----
+
where:

`Enabled`:: Enables user-provisioned DNS management.

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

[role="_additional-resources"]
.Additional resources
* Additional {gcp-first} configuration parameters

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc

[id="installation-gcp-config-yaml_{context}"]
= Sample customized install-config.yaml file for {gcp-full}

[role="_abstract"]
To specify more details about your OpenShift Container Platform cluster's platform or modify the values of the required parameters, you can customize the `install-config.yaml` file.

[IMPORTANT]
====
This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.
====

[source,yaml]
----
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
controlPlane:
  name: master
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
compute:
- name: worker
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  gcp:
    projectID: sample-project
    region: us-east1
----
where:

`controlPlane`:: Specifies parameters that apply to control plane machines.
`compute`:: Specifies parameters that apply to compute machines.
`networking`:: Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.
`platform`:: Specifies parameters that apply to the infrastructure platform that hosts the cluster.

[role="_additional-resources"]
.Additional resources

* Installation configuration parameters for GCP
* Enabling customer-managed encryption keys for a compute machine set

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

// Module included in the following assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc

[id="installing-gcp-user-defined-labels-and-tags_{context}"]
= Managing user-defined labels and tags for {gcp-short}

{gcp-first} provides labels and tags that help to identify and organize the resources created for a specific OpenShift Container Platform cluster, making them easier to manage.

You can define labels and tags for each {gcp-short} resource only during OpenShift Container Platform cluster installation.

[IMPORTANT]
====
User-defined labels and tags are not supported for OpenShift Container Platform clusters upgraded to OpenShift Container Platform .
====

[NOTE]
====
You cannot update the tags that are already added. Also, a new tag-supported resource creation fails if the configured tag keys or tag values are deleted.
====

.User-defined labels

User-defined labels and OpenShift Container Platform specific labels are applied only to resources created by OpenShift Container Platform installation program and its core components such as:

* {gcp-short} filestore CSI Driver Operator
* {gcp-short} PD CSI Driver Operator
* Image Registry Operator
* Machine API provider for {gcp-short}

User-defined labels are not attached to the resources created by any other Operators or the Kubernetes in-tree components.

User-defined labels and OpenShift Container Platform labels are available on the following {gcp-short} resources:

* Compute disk
* Compute forwarding rule
* Compute image
* Compute instance
* DNS managed zone
* Filestore backup
* Filestore instance
* Storage bucket

.Limitations to user-defined labels

* Labels for `ComputeAddress` are supported in the {gcp-short} beta version. OpenShift Container Platform does not add labels to the resource.

.User-defined tags

User-defined tags are applied only to resources created by OpenShift Container Platform installation program and its core components, such as the following resources:

* {gcp-short} FileStore CSI Driver Operator
* {gcp-short} PD CSI Driver Operator
* Image Registry Operator
* Machine API provider for {gcp-short}

User-defined tags are not attached to the resources created by any other Operators or the Kubernetes in-tree components.

User-defined tags are available on the following {gcp-short} resources:

* Compute disk
* Compute instance
* Filestore backup
* Filestore instance
* Storage bucket

.Limitations to the user-defined tags

* Tags must not be restricted to particular service accounts, because Operators create and use service accounts with minimal roles.
* OpenShift Container Platform does not create any key and value resources of the tag.
* OpenShift Container Platform specific tags are not added to any resource.

[role="_additional-resources"]
.Additional resources

* For more information about identifying the `OrganizationID`, see: OrganizationID
* For more information about identifying the `ProjectID`, see: ProjectID
* For more information about labels, see Labels Overview.
* For more information about tags, see Tags Overview.

// Criteria for user-defined labels and tags
// Module included in the following assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc

[id="installing-gcp-cluster-label-tag-reference_{context}"]
= Criteria for user-defined labels and tags

Before configuring user-defined labels and tags for {gcp-full}, consider the importance of meeting the requirements for these tag and labels to ensure proper resource governance.

The following list details the requirements for user-defined labels:

* A label key and value must have a minimum of 1 character and can have a maximum of 63 characters.
* A label key and value must contain only lowercase letters, numeric characters, an underscore (`_`), and a dash (`-`).
* A label key must start with a lowercase letter.
* You can configure a maximum of 32 labels per resource.
** Each resource has a maximum of 64 labels, where OpenShift Container Platform reserves 32 labels for internal use.

The following list details the requirements for user-defined tags:

* Tag key and tag value must already exist. OpenShift Container Platform does not create the key and the value.
* A tag `parentID` can be either `OrganizationID` or `ProjectID`:
** `OrganizationID` must consist of decimal numbers without leading zeros.
** `ProjectID` must be 6 to 30 characters in length, that includes only lowercase letters, numbers, and hyphens.
** `ProjectID` must start with a letter, and cannot end with a hyphen.
* A tag key must contain only uppercase and lowercase alphanumeric characters, a hyphen (`-`), an underscore (`_`), and a period (`.`).
* A tag value must contain only uppercase and lowercase alphanumeric characters and any of the following characters:
** A colon (`:`)
** A comma (`,`)
** A curly braces (`{}`)
** A hyphen (`-`)
** A parentheses (`()`)
** A percent sign (`%`)
** A plus (`+`)
** A pound sign (`$`)
** A space.
** A square braces (`[]`)
** An ampersand (`&`)
** An asterisk (`*`)
** An at sign (`@`)
** An equals sign (`=`)
** An underscore (`_`)
** A period (`.`)
* A tag key and value must begin and end with an alphanumeric character.
* Tag value must be one of the predefined values for the key.
* You can configure a maximum of 50 tags.
* Do not define a tag key with the same value as any of the existing tag keys that get inherited from the parent resource.

//Configuring user-defined labels and tags for GCP
// Module included in the following assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc

[id="installing-gcp-cluster-creation_{context}"]
= Configuring user-defined labels and tags for {gcp-short}

Configuring user-defined labels and tags for {gcp-full} means that you can apply key-value pairs to your cloud resources for the purposes of organizing, managing, and automating your infrastructure.

.Prerequisites

* The installation program requires that a service account includes a `TagUser` role, so that the program can create the OpenShift Container Platform cluster with defined tags at both organization and project levels.

.Procedure

* Update the `install-config.yaml` file to define the list of required labels and tags.
+
[NOTE]
====
If you set labels and tags during creation of the `install-config.yaml` configuration file, you cannot create new or update existing labels and tags after creation of the cluster.
====
+
.Sample `install-config.yaml` file
+
[source,yaml]
----
apiVersion: v1
credentialsMode: Passthrough <1>
platform:
 gcp:
   userLabels: <2>
   - key: <label_key><3>
     value: <label_value><4>
   userTags: <5>
   - parentID: <OrganizationID/ProjectID><6>
     key: <tag_key_short_name>
     value: <tag_value_short_name>
# ...
----
<1> In passthrough mode, the Cloud Credential Operator (CCO) passes the provided cloud credential to the components that request cloud credentials.
<2> Adds keys and values as labels to the resources created on {gcp-short}.
<3> Defines the label name.
<4> Defines the label content.
<5> Adds keys and values as tags to the resources created on {gcp-short}.
<6> The ID of the hierarchical resource where you defined the tags at the organization or the project level.

//Querying user-defined labels and tags for GCP
// Module included in the following assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc

[id="installing-gcp-querying-labels-tags-gcp_{context}"]
= Querying user-defined labels and tags for {gcp-short}

After creating the OpenShift Container Platform cluster, you can access the list of the labels and tags defined for the {gcp-short} resources  in the `infrastructures.config.openshift.io/cluster` object as shown in the following sample `infrastructure.yaml` file.

.Sample `infrastructure.yaml` file
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Infrastructure
metadata:
 name: cluster
spec:
 platformSpec:
   type: GCP
status:
 infrastructureName: <cluster_id><1>
 platform: GCP
 platformStatus:
   gcp:
     resourceLabels:
     - key: <label_key>
       value: <label_value>
     resourceTags:
     - key: <tag_key_short_name>
       parentID: <OrganizationID/ProjectID>
       value: <tag_value_short_name>
   type: GCP
----
<1> The cluster ID that is generated during cluster installation.

Along with the user-defined labels, resources have a label defined by the OpenShift Container Platform. The format of the OpenShift Container Platform labels is `kubernetes-io-cluster-<cluster_id>:owned`.

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

[id="installing-gcp-manual-modes_{context}"]
== Alternatives to storing administrator-level secrets in the kube-system project

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

* To manage long-term cloud credentials manually, follow the procedure in Manually creating long-term credentials.

* To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in Configuring a {gcp-short} cluster to use short-term credentials.

//Manually creating long-term credentials
// Module included in the following assemblies:
//
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-network-customizations.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//Platforms that must manually create IAM

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="manually-create-iam_{context}"]

//For providers that support multiple modes of operation
= Manually creating long-term credentials

//For providers who only support manual mode
= Manually manage cloud credentials

//For providers that support multiple modes of operation
[role="_abstract"]
The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

//For providers who only support manual mode
The Cloud Credential Operator (CCO) only supports your cloud provider in manual mode. As a result, you must specify the identity and access management (IAM) secrets for your cloud provider.

.Procedure

. Add the following granular permissions to the {gcp-short} account that the installation program uses:
+
* compute.machineTypes.list
* compute.regions.list
* compute.zones.list
* dns.changes.create
* dns.changes.get
* dns.managedZones.create
* dns.managedZones.delete
* dns.managedZones.get
* dns.managedZones.list
* dns.networks.bindPrivateDNSZone
* dns.resourceRecordSets.create
* dns.resourceRecordSets.delete
* dns.resourceRecordSets.list

. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:
+
.Sample configuration file snippet
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
credentialsMode: Manual
# ...
----

. If you have not previously created installation manifest files, do so by running the following command:
+
[source,terminal]
----
$ openshift-install create manifests --dir <installation_directory>
----
+
where `<installation_directory>` is the directory in which the installation program creates files.

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
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=<path_to_directory_for_credentials_requests>
----
+
where:
+
`--included`:: Specifies only the manifests that your specific cluster configuration requires.
`<path_to_directory_with_installation_configuration>`:: Specifies the location of the `install-config.yaml` file.
`<path_to_directory_for_credentials_requests>`:: Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.
+
This command creates a YAML file for each `CredentialsRequest` object.
+
.Sample `CredentialsRequest` object
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - effect: Allow
      action:
      - iam:GetUser
      - iam:GetUserPolicy
      - iam:ListAccessKeys
      resource: "*"
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
    kind: GCPProviderSpec
    predefinedRoles:
    - roles/storage.admin
    - roles/iam.serviceAccountUser
    skipServiceCheck: true
  ...
----

. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.
+
.Sample `CredentialsRequest` object with secrets
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - effect: Allow
      action:
      - s3:CreateBucket
      - s3:DeleteBucket
      resource: "*"
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
    kind: GCPProviderSpec
      predefinedRoles:
      - roles/iam.securityReviewer
      - roles/iam.roleViewer
      skipServiceCheck: true
      ...
  secretRef:
    name: <component_secret>
    namespace: <component_namespace>
  ...
----
+
.Sample `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <component_secret>
  namespace: <component_namespace>
data:
  aws_access_key_id: <base64_encoded_aws_access_key_id>
  aws_secret_access_key: <base64_encoded_aws_secret_access_key>
data:
  azure_subscription_id: <base64_encoded_azure_subscription_id>
  azure_client_id: <base64_encoded_azure_client_id>
  azure_client_secret: <base64_encoded_azure_client_secret>
  azure_tenant_id: <base64_encoded_azure_tenant_id>
  azure_resource_prefix: <base64_encoded_azure_resource_prefix>
  azure_resourcegroup: <base64_encoded_azure_resourcegroup>
  azure_region: <base64_encoded_azure_region>
data:
  service_account.json: <base64_encoded_gcp_service_account_file>
----
+
[IMPORTANT]
====
Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.
====

//Platforms that must manually create IAM

//AWS install assemblies

//GCP install assemblies

//Azure will also be moved as part of work on `ccoctl` support for Azure

//global Azure install assemblies

//Supertask: Configuring a GCP cluster to use short-term credentials
[id="installing-gcp-with-short-term-creds_{context}"]
=== Configuring a {gcp-short} cluster to use short-term credentials

To install a cluster that is configured to use {gcp-short} Workload Identity, you must configure the Cloud Credential Operator (CCO) utility and create the required {gcp-short} resources for your cluster. Cluster Operators use the credentials created by the CCO. The installation program does not use these credentials.

//Task part 1: Configuring the Cloud Credential Operator utility
// Module included in the following assemblies:
//
//Postinstall and update content
// * post_installation_configuration/changing-cloud-credentials-configuration.adoc
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc
//
//Platforms that must use `ccoctl` and update content
// * installing/installing_ibm_cloud/configuring-iam-ibm-cloud.adoc
// * installing/installing_ibm_powervs/preparing-to-install-on-ibm-power-vs.doc
// * installing/installing_nutanix/preparing-to-install-on-nutanix.adoc
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//Postinstall  and update content

//Platforms that must use `ccoctl`

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="cco-ccoctl-configuring_{context}"]

[role="_abstract"]
//Nutanix-only intro because it needs context in its install procedure.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on Nutanix, you must set the CCO to `manual` mode as part of the installation process.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on {ibm-power-server-name}, you must set the CCO to `manual` mode as part of the installation process.

//The upgrade and postinstall procs also have a different intro, so they are excluded here.
To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

//Intro for the postinstall procs.
To configure an existing cluster to create and manage cloud credentials from outside of the cluster, extract and prepare the Cloud Credential Operator utility (`ccoctl`) binary.

//Intro for the upgrade procs.
To upgrade a cluster that uses the Cloud Credential Operator (CCO) in manual mode to create and manage cloud credentials from outside of the cluster, extract and prepare the CCO utility (`ccoctl`) binary.

[NOTE]
====
The `ccoctl` utility is a Linux binary that must run in a Linux environment.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the {oc-first}.

//Upgrade prereqs
* Your cluster was configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

//Permissions requirements (per platform, for install and key rotation)

.Procedure

. Set a variable for the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----
----
$ RELEASE_IMAGE=$(oc get clusterversion -o jsonpath={..desired.image})
----

. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
----
+
[NOTE]
====
Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
====

. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc image extract $CCO_IMAGE \
  --file="/usr/bin/ccoctl.<rhel_version>" \
  -a ~/.pull-secret
----
+
For `<rhel_version>`, specify the value that corresponds to the version of {op-system-base-full} that the host uses.
If no value is specified, `ccoctl.rhel8` is used by default.
The following values are valid:
+
* `rhel8`: Specify this value for hosts that use {op-system-base} 8.
* `rhel9`: Specify this value for hosts that use {op-system-base} 9.

+
[NOTE]
====
The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
====

. Change the permissions to make `ccoctl` executable by running the following command:
+
[source,terminal]
----
$ chmod 775 ccoctl
----

.Verification

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:
+
[source,terminal]
----
$ ./ccoctl
----
+
.Example output
[source,terminal]
----
OpenShift credentials provisioning tool

Usage:
  ccoctl [command]

Available Commands:
  aws          Manage credentials objects for AWS cloud
  azure        Manage credentials objects for Azure
  gcp          Manage credentials objects for Google cloud
  help         Help about any command
  ibmcloud     Manage credentials objects for IBM Cloud
  nutanix      Manage credentials objects for Nutanix

Flags:
  -h, --help   help for ccoctl

Use "ccoctl [command] --help" for more information about a command.
----

//Postinstall and update content

//Platforms that must use `ccoctl` and update content

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

//Task part 2: Creating the required GCP resources
// Module included in the following assemblies:
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="cco-ccoctl-creating-at-once_{context}"]
= Creating AWS resources with a single command

[role="_abstract"]
If the process the `ccoctl` tool uses to create AWS resources automatically meets the requirements of your organization, you can use the `ccoctl aws create-all` command to automate the creation of AWS resources.

Otherwise, you can create the AWS resources individually. For more information, see "Creating AWS resources individually".

= Creating {gcp-short} resources with the Cloud Credential Operator utility

[role="_abstract"]
You can use the `ccoctl gcp create-all` command to automate the creation of {gcp-short} resources.
= Creating Azure resources with the Cloud Credential Operator utility

[role="_abstract"]
You can use the `ccoctl azure create-all` command to automate the creation of Azure resources.

[NOTE]
====
By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.
====

.Prerequisites

You must have:

* Extracted and prepared the `ccoctl` binary.

* Access to your Microsoft Azure account by using the Azure CLI.

.Procedure

. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----

. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=<path_to_directory_for_credentials_requests>
----
+
where:
+
`--included`:: Specifies to include only the manifests that your specific cluster configuration requires.
`<path_to_directory_with_installation_configuration>`:: Specifies the location of the `install-config.yaml` file.
`<path_to_directory_for_credentials_requests>`:: Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.
+
[NOTE]
====
This command might take a few moments to run.
====

. To enable the `ccoctl` utility to detect your Azure credentials automatically, log in to the Azure CLI by running the following command:
+
[source,terminal]
----
$ az login
----

. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-all \
  --name=<name> \
  --region=<aws_region> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --output-dir=<path_to_ccoctl_output_dir> \
  --create-private-s3-bucket \
  --permissions-boundary-arn=<policy_arn>
----
+
where:
+
`<name>`:: Specifies the name used to tag any cloud resources that are created for tracking.
`<aws_region>`:: Specifies the AWS region in which cloud resources will be created.
`<path_to_credentials_requests_directory>`:: Specifies the directory containing the files for the component `CredentialsRequest` objects.
`<path_to_ccoctl_output_dir>`:: Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run. This parameter is optional.
`--create-private-s3-bucket`:: Specifies that the OpenID Connect (OIDC) configuration files should be stored in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL. Note that by default, the `ccoctl` utility stores the OIDC configuration files in a public S3 bucket and uses the S3 URL as the public OIDC endpoint. This parameter is optional.
`<policy_arn>`:: Specifies the Amazon Resource Name (ARN) of the {aws-short} IAM policy to use as the permissions boundary for the IAM roles created by the `ccoctl` utility. This parameter is optional.
+
[NOTE]
====
If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
====
[source,terminal]
----
$ ccoctl gcp create-all \
  --name=<name> \
  --region=<gcp_region> \
  --project=<gcp_project_id> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --key-storage-method=<key_storage_method>
----
+
where:
+
`<name>`:: Specifies the user-defined name for all created {gcp-short} resources used for tracking. If you plan to install the {gcp-short} Filestore Container Storage Interface (CSI) Driver Operator, retain this value.
`<gcp_region>`:: Specifies the {gcp-short} region in which cloud resources will be created.
`<gcp_project_id>`:: Specifies the {gcp-short} project ID in which cloud resources will be created.
`<path_to_credentials_requests_directory>`:: Specifies the directory containing the files of `CredentialsRequest` manifests to create {gcp-short} service accounts.
`<key_storage_method>`:: Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket. This parameter is optional.
+
[NOTE]
====
If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
====
[source,terminal]
----
$ ccoctl azure create-all \
  --name=<azure_infra_name> \
  --output-dir=<ccoctl_output_dir> \
  --region=<azure_region> \
  --subscription-id=<azure_subscription_id> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --dnszone-resource-group-name=<azure_dns_zone_resource_group_name> \
  --tenant-id=<azure_tenant_id> \
  --network-resource-group-name <azure_resource_group> \
  --preserve-existing-roles
----
+
where:
+
`<azure_infra_name>`:: Specifies the user-defined name for all created Azure resources used for tracking.
`<ccoctl_output_dir>`:: Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run. This parameter is optional.
`<azure_region>`:: Specifies the Azure region in which cloud resources will be created.
`<azure_subscription_id>`:: Specifies the Azure subscription ID to use.
`<path_to_credentials_requests_directory>`:: Specifies the directory containing the files for the component `CredentialsRequest` objects.
`<azure_dns_zone_resource_group_name>`:: Specifies the name of the resource group containing the cluster's base domain Azure DNS zone.
`<azure_tenant_id>`:: Specifies the Azure tenant ID to use.
`<azure_resource_group>`:: Specifies the virtual network resource group if it is different from the cluster resource group. This parameter is optional.
`--preserve-existing-roles`:: Specifies that any custom role assignments you define on managed identities are not removed during OpenShift Container Platform updates. This parameter is optional.
+
[NOTE]
====
If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

To see additional optional parameters and explanations of how to use them, run the `azure create-all --help` command.
====

.Verification

* To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:
+
[source,terminal]
----
$ ls <path_to_ccoctl_output_dir>/manifests
----
+
.Example output
[source,text]
----
cluster-authentication-02-config.yaml
openshift-cloud-credential-operator-cloud-credential-operator-iam-ro-creds-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capa-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-ebs-cloud-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-aws-cloud-credentials-credentials.yaml
----
+
You can verify that the IAM roles are created by querying AWS. For more information, refer to AWS documentation on listing IAM roles.
+
.Example output
[source,text]
----
cluster-authentication-02-config.yaml
openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-gcp-cloud-credentials-credentials.yaml
----
+
You can verify that the IAM service accounts are created by querying {gcp-short}. For more information, refer to {gcp-short} documentation on listing IAM service accounts.
+
.Example output
[source,text]
----
azure-ad-pod-identity-webhook-config.yaml
cluster-authentication-02-config.yaml
openshift-cloud-controller-manager-azure-cloud-credentials-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capz-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-azure-disk-credentials-credentials.yaml
openshift-cluster-csi-drivers-azure-file-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-azure-cloud-credentials-credentials.yaml
----
+
You can verify that the Microsoft Entra ID service accounts are created by querying Azure. For more information, refer to Azure documentation on listing Entra ID service accounts.

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

//Restricting service account impersonation to the compute nodes service account
// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc

[id="restricting-sa-impersonation-compute-sa-gcp_{context}"]
= Restricting service account impersonation to the compute nodes service account

[role="_abstract"]
After the Cloud Credential Operator utility (`ccoctl`) creates the resources for the cluster, you can restrict the {gcp-first} `iam.serviceAccounts.actAs` permission that the `ccoctl` utility granted to the Machine API controller service account to the compute nodes service account.

[NOTE]
====
Restricting service account impersonation to the compute nodes service account is optional.
If your organization does not require this change, you can continue to "Incorporating the Cloud Credential Operator utility manifests".
====

When the `ccoctl` utility assigns custom and {gcp-short} predefined roles to OpenShift Container Platform components service accounts, it grants the `iam.serviceAccounts.actAs` permission to the Machine API controller service account at the {gcp-first} project level.
To reduce the scope of the `iam.serviceAccounts.actAs` permission, you identify the custom role of the Machine API controller service account and replace it with a role that has a more restricted set of permissions.
To allow this component to work, you then grant the Machine API controller service account the Service Account User role on the service account of the compute nodes instead.

.Prerequisites

* You have configured an account with the cloud platform that hosts your cluster.
* You have used the `ccoctl` utility to create the cloud provider resources for your cluster.
* You have access to your `install-config.yaml` file.
* You have logged in to the {gcp-full} CLI (`gcloud`) as a user with permissions to manage service accounts and roles.

.Procedure

. Obtain the following values from your `install-config.yaml` file:

** The {gcp-short} project name.
In the YAML file, this is the value of the `platform.gcp.projectID` parameter.

** The cluster name.
In the YAML file, this is the value of the `metadata.name` parameter.

** The service account for the compute nodes.
In the YAML file, this is the value of the `compute[0].platform.gcp.serviceAccount` parameter.

. Obtain the service account for the Machine API controller that the `ccoctl` utility created by running the following command:
+
[source,terminal]
----
$ gcloud iam service-accounts list \
  --filter="displayName=<cluster_name>-openshift-machine-api-gcp" \
  --format='value(email)'
----
+
where `<cluster_name>` is the value specified for the `metadata.name` parameter in your `install-config.yaml` file.

. Obtain the role ID of the custom role for the Machine API controller service account by running the following command:
+
[source,terminal]
----
$ gcloud projects get-iam-policy <project_name> \
  --flatten='bindings[].members' \
  --format='table(bindings.role)' \
  --filter="bindings.members:<machine_api_controller_service_account>"
----
+
where `<machine_api_controller_service_account>` is the Machine API controller service account.

. List the custom role permissions for the Machine API controller service account by running the following command:
+
[source,terminal]
----
$ gcloud iam roles describe <machine_api_role> \
  --project <project_name>
----
+
where `<machine_api_role>` is the role ID of the custom role for the Machine API controller service account.
+
.Example output
[source,text]
----
etag: <etag_value>
includedPermissions:
- compute.acceleratorTypes.get
- compute.acceleratorTypes.list
- compute.disks.create
- compute.disks.createTagBinding
...
- compute.zones.get
- compute.zones.list
- iam.serviceAccounts.actAs
- iam.serviceAccounts.get
- iam.serviceAccounts.list
- resourcemanager.tagValues.get
- resourcemanager.tagValues.list
- serviceusage.quotas.get
- serviceusage.services.get
- serviceusage.services.list
name: projects/<project_name>/roles/<machine_api_role>
stage: GA
title: <project_name>-openshift-machine-api-gcp
----
+
where `<project_name>` is the {gcp-short} project name specified in the `install-config.yaml` file.
+
[NOTE]
====
This truncated example output might not match the permissions list for your cluster.
====

. Create a custom role that includes all of the permissions from your output except for the `iam.serviceAccounts.actAs` permission by running a command similar to the following:
+
[source,terminal]
----
$ gcloud iam roles create <machine_api_role>_without_actas \
--project=<project_name> \
--title=<machine_api_role>_without_actas \
--description="Required permissions for the Machine API controller without the iam.serviceAccounts.actAs permission" \
--permissions=compute.acceleratorTypes.get,\
compute.acceleratorTypes.list,\
compute.disks.create,\
compute.disks.createTagBinding,\
...
compute.zones.get,\
compute.zones.list,\
iam.serviceAccounts.get,\
iam.serviceAccounts.list,\
resourcemanager.tagValues.get,\
resourcemanager.tagValues.list,\
serviceusage.quotas.get,\
serviceusage.services.get,\
serviceusage.services.list
----
+
In this example, the new role name is the original custom role name, `<machine_api_role>`, with a `_without_actas` string added to the end.
+
[IMPORTANT]
====
This truncated example command might not match the permissions list for your cluster.
You must use the list of permissions from the output of the `gcloud iam roles describe <machine_api_role> --project <project_name>` command on your cluster.
====

. Remove the custom role that includes the `iam.serviceAccounts.actAs` permission from the Machine API controller service account by running the following command:
+
[source,terminal]
----
$ gcloud projects remove-iam-policy-binding <project_name> \
  --member "serviceAccount:<machine_api_controller_service_account>" \
  --role "projects/<project_name>/roles/<machine_api_role>"
----
+
where `<machine_api_role>` is the original custom role.

. Grant the custom role that excludes the `iam.serviceAccounts.actAs` permission to the Machine API controller service account by running the following command:
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding <project_name> \
  --member "serviceAccount:<machine_api_controller_service_account>" \
  --role "projects/<project_name>/roles/<machine_api_role>_without_actas
----
+
where `<machine_api_role>_without_actas` is the new custom role.

. Optional: To verify that the Machine API controller service account has the correct role, check the attached role ID by running the following command:
+
[source,terminal]
----
$ gcloud projects get-iam-policy <project_name> \
  --flatten='bindings[].members' \
  --format='table(bindings.role)' \
  --filter="bindings.members:<machine_api_controller_service_account>"
----
+
.Example output
[source,text]
----
ROLE
projects/<project_name>/roles/<machine_api_role>_without_actas
----

. Grant the Machine API controller service account the Service Account User role on the service account of the compute nodes by running the following command:
+
[source,terminal]
----
$ gcloud iam service-accounts add-iam-policy-binding <compute_nodes_service_account> \
  --member="serviceAccount:<machine_api_controller_service_account>" \
  --role=roles/iam.serviceAccountUser
----
+
where `<compute_nodes_service_account>` is the service account for your compute nodes.
This value is the `compute[0].platform.gcp.serviceAccount` parameter in your `install-config.yaml` file.

//Task part 3: Incorporating the Cloud Credential Operator utility manifests
// Module included in the following assemblies:
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//global Azure install assemblies

//GCP install assemblies

[id="cco-ccoctl-install-creating-manifests_{context}"]
= Incorporating the Cloud Credential Operator utility manifests

[role="_abstract"]
To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

.Prerequisites

* You have configured an account with the cloud platform that hosts your cluster.
* You have configured the Cloud Credential Operator utility (`ccoctl`).
* You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

.Procedure

. Add the following granular permissions to the {gcp-short} account that the installation program uses:
+
* compute.machineTypes.list
* compute.regions.list
* compute.zones.list
* dns.changes.create
* dns.changes.get
* dns.managedZones.create
* dns.managedZones.delete
* dns.managedZones.get
* dns.managedZones.list
* dns.networks.bindPrivateDNSZone
* dns.resourceRecordSets.create
* dns.resourceRecordSets.delete
* dns.resourceRecordSets.list

. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:
+
.Sample configuration file snippet
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
credentialsMode: Manual
# ...
----

. If you used the `ccoctl` utility to create a new Azure resource group instead of using an existing resource group, modify the `resourceGroupName` parameter in the `install-config.yaml` as shown:
+
.Sample configuration file snippet
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
# ...
platform:
  azure:
    resourceGroupName: <azure_infra_name>
# ...
----
+
The `<azure_infra_name>` value must match the user-defined name for Azure resources that was specified with the `--name` argument of the `ccoctl azure create-all` command.

. If you have not previously created installation manifest files, do so by running the following command:
+
[source,terminal]
----
$ openshift-install create manifests --dir <installation_directory>
----
+
where `<installation_directory>` is the directory in which the installation program creates files.

. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
----

. Copy the `tls` directory that contains the private key to the installation directory:
+
[source,terminal,subs="+quotes"]
----
$ cp -a /<path_to_ccoctl_output_dir>/tls .
----

//global Azure install assemblies

//GCP install assemblies

// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-customizations.adoc

[id="installation-gcp-marketplace_{context}"]
= Using the {gcp-short} Marketplace offering

Using the {gcp-short} Marketplace offering lets you deploy an OpenShift Container Platform cluster, which is billed on pay-per-use basis (hourly, per core) through {gcp-short}, while still being supported directly by Red{nbsp}Hat.

By default, the installation program downloads and installs the {op-system-first} image that is used to deploy compute machines. To deploy an OpenShift Container Platform cluster using an {op-system} image from the {gcp-short} Marketplace, override the default behavior by modifying the `install-config.yaml` file to reference the location of {gcp-short} Marketplace offer.

[NOTE]
====
====

.Prerequisites

* You have an existing `install-config.yaml` file.

.Procedure

. Edit the `compute.platform.gcp.osImage` parameters to specify the location of the {gcp-short} Marketplace image:
** Set the `project` parameter to `redhat-marketplace-public`
** Set the `name` parameter to one of the following offers:
+
OpenShift Container Platform:: `redhat-coreos-ocp-413-x86-64-202305021736`
{opp}:: `redhat-coreos-opp-413-x86-64-202305021736`
{oke}:: `redhat-coreos-oke-413-x86-64-202305021736`
. Save the file and reference it when deploying the cluster.

.Sample `install-config.yaml` file that specifies a {gcp-short} Marketplace image for compute machines
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
controlPlane:
# ...
compute:
  platform:
    gcp:
      osImage:
        project: redhat-marketplace-public
        name: redhat-coreos-ocp-413-x86-64-202305021736
# ...
----

// Network Operator specific configuration
// TODO -  possibly delete this file
// Or does it add actual value?

// Module included in the following assemblies:
//
// * networking/cluster-network-operator.adoc
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc

[id="nw-network-config_{context}"]
= Network configuration phases

[role="_abstract"]
There are two phases prior to OpenShift Container Platform installation where you can customize the network configuration. Customize settings in the `install-config.yaml` file and in the Cluster Network Operator manifest across two configuration phases.

Phase 1:: You can customize the following network-related fields in the `install-config.yaml` file before you create the manifest files:
+
* `networking.networkType`
* `networking.clusterNetwork`
* `networking.serviceNetwork`
* `networking.machineNetwork`
* `nodeNetworking`
+
For more information, see "Installation configuration parameters".
+
[NOTE]
====
Set the `networking.machineNetwork` to match the Classless Inter-Domain Routing (CIDR) where the preferred subnet is located.
====
+
[IMPORTANT]
====
The CIDR range `172.17.0.0/16` is reserved by `libVirt`. You cannot use any other CIDR range that overlaps with the `172.17.0.0/16` CIDR range for networks in your cluster.
====

Phase 2:: After creating the manifest files by running `openshift-install create manifests`, you can define a customized Cluster Network Operator manifest with only the fields you want to modify. You can use the manifest to specify an advanced network configuration.

During phase 2, you cannot override the values that you specified in phase 1 in the `install-config.yaml` file. However, you can customize the network plugin during phase 2.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc

[id="modifying-nwoperator-config-startup_{context}"]
= Specifying advanced network configuration

[role="_abstract"]
To integrate your OpenShift Container Platform cluster with your existing network environment, you can specify advanced network configuration in a manifest before you install the cluster. Advanced network configuration can be configured only during cluster installation.

[IMPORTANT]
====
Customizing your network configuration by modifying the OpenShift Container Platform manifest files created by the installation program is not supported. Applying a manifest file that you create, as in the following procedure, is supported.
====

.Prerequisites

* You have created the `install-config.yaml` file and completed any modifications to it.

.Procedure

. Change to the directory that contains the installation program and create the manifests:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----
+
The `<installation_directory>` specifies the name of the directory that contains the `install-config.yaml` file for your cluster.

. Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
----

. Specify the advanced network configuration for your cluster in the `cluster-network-03-config.yml` file, such as in the following example:
+
.Enable IPsec for the OVN-Kubernetes network provider
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      ipsecConfig:
        mode: Full
----

. Optional: Back up the `manifests/cluster-network-03-config.yml` file. The
installation program consumes the `manifests/` directory when you create the
Ignition config files.

. Remove the Kubernetes manifest files that define the control plane machines and compute `MachineSets`:
+
[source,terminal]
----
$ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml
----
+
Because you create and manage these resources yourself, you do not have
to initialize them.
+
* You can preserve the `MachineSet` files to create compute machines by using the machine API, but you must update references to them to match your environment.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * networking/cluster-network-operator.adoc
// * networking/network_security/logging-network-security.adoc
// * post_installation_configuration/network-configuration.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc

// Installation assemblies need different details than the CNO operator does

[id="nw-operator-cr_{context}"]
= Cluster Network Operator configuration

[role="_abstract"]
To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes.

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group:

`clusterNetwork`:: IP address pools from which pod IP addresses are allocated.
`serviceNetwork`:: IP address pool for services.
//Installation no longer supports SDN, so excluding it from install docs here. Deleted in 4.17.

`defaultNetwork.type`:: Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation.

// For the post installation assembly, no further content is provided.
[NOTE]
====
After cluster installation, you can only modify the `clusterNetwork` IP address range. The `serviceNetwork` range cannot be modified post-installation, either directly or by using the `ServiceCIDR` API.
====

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`.

[id="nw-operator-cr-cno-object_{context}"]
== Cluster Network Operator configuration object

The fields for the Cluster Network Operator (CNO) are described in the following table:

.Cluster Network Operator configuration object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|The name of the CNO object. This name is always `cluster`.

|`spec.clusterNetwork`
|`array`
|A list specifying the blocks of IP addresses from which pod IP addresses are allocated and the subnet prefix length assigned to each individual node in the cluster. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:

[source,yaml]
----
spec:
  clusterNetwork:
  - cidr: 10.128.0.0/19
    hostPrefix: 23
  - cidr: fd01::/48
    hostPrefix: 64
----

If you install a cluster on {aws-short} with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.

|`spec.serviceNetwork`
|`array`
|A block of IP addresses for services. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:

[source,yaml]
----
spec:
  serviceNetwork:
  - 172.30.0.0/14
  - fd02::/112
----

If you install a cluster on {aws-short} with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.

This value is ready-only and inherited from the `Network.config.openshift.io` object named `cluster` during cluster installation.
You can customize this field only in the `install-config.yaml` file before you create the manifests. The value is read-only in the manifest file.

|`spec.defaultNetwork`
|`object`
|Configures the network plugin for the cluster network.

|`spec.additionalRoutingCapabilities.providers`
|`array`
|This setting enables a dynamic routing provider. The FRR routing capability provider is required for the route advertisement feature. The only supported value is `FRR`.

--
- `FRR`: The FRR routing provider
--

[source,yaml]
----
spec:
  additionalRoutingCapabilities:
    providers:
    - FRR
----

|====

[IMPORTANT]
====
For a cluster that needs to deploy objects across multiple networks, ensure that you specify the same value for the `clusterNetwork.hostPrefix` parameter for each network type that is defined in the `install-config.yaml` file. Setting a different value for each `clusterNetwork.hostPrefix` parameter can impact the OVN-Kubernetes network plugin, where the plugin cannot effectively route object traffic among different nodes.
====

[id="nw-operator-cr-defaultnetwork_{context}"]
== defaultNetwork object configuration

The values for the `defaultNetwork` object are defined in the following table:

.`defaultNetwork` object
[cols=".^3,.^2,.^5a",options="header"]
|====
|Field|Type|Description

|`type`
|`string`
|`OVNKubernetes`. The {openshift-networking} network plugin is selected during installation. This value cannot be changed after cluster installation.
[NOTE]
====
OpenShift Container Platform uses the OVN-Kubernetes network plugin by default.
====

|`ovnKubernetesConfig`
|`object`
|This object is only valid for the OVN-Kubernetes network plugin.

|====

[id="nw-operator-configuration-parameters-for-ovn-sdn_{context}"]
== Configuration for the OVN-Kubernetes network plugin

The following table describes the configuration fields for the OVN-Kubernetes network plugin:

.`ovnKubernetesConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`mtu`
|`integer`
|
The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This is detected automatically based on the MTU of the primary network interface. You do not normally need to override the detected MTU.

If the auto-detected value is not what you expect it to be, confirm that the MTU on the primary network interface on your nodes is correct. You cannot use this option to change the MTU value of the primary network interface on the nodes.

If your cluster requires different MTU values for different nodes, you must set this value to `100` less than the lowest MTU value in your cluster. For example, if some nodes in your cluster have an MTU of `9001`, and some have an MTU of `1500`, you must set this value to `1400`.
The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This value is normally configured automatically.

|`genevePort`
|`integer`
|
The port to use for all Geneve packets. The default value is `6081`. This value cannot be changed after cluster installation.
The UDP port for the Geneve overlay network.

|`ipsecConfig`
|`object`
|
Specify a configuration object for customizing the IPsec configuration.
An object describing the IPsec mode for the cluster.

|`ipv4`
|`object`
|Specifies a configuration object for IPv4 settings.

|`ipv6`
|`object`
|Specifies a configuration object for IPv6 settings.

|`policyAuditConfig`
|`object`
|Specify a configuration object for customizing network policy audit logging. If unset, the defaults audit log settings are used.

|`routeAdvertisements`
|`string`
a|Specifies whether to advertise cluster network routes. The default value is `Disabled`.
--
- `Enabled`: Import routes to the cluster network and advertise cluster network routes as configured in `RouteAdvertisements` objects.
- `Disabled`: Do not import routes to the cluster network or advertise cluster network routes.
--

|`gatewayConfig`
|`object`
|Optional: Specify a configuration object for customizing how egress traffic is sent to the node gateway. Valid values are `Shared` and `Local`. The default value is `Shared`. In the default setting, the Open vSwitch (OVS) outputs traffic directly to the node IP interface. If you are using hardware offloading, Red Hat recommends to use the default `Shared` gateway mode to bypass the host routing plane. In the `Local` setting, it traverses the host network; consequently, it gets applied to the routing table of the host.

[NOTE]
====
While migrating egress traffic, you can expect some disruption to workloads and service traffic until the Cluster Network Operator (CNO) successfully rolls out the changes.
====

|====

.`ovnKubernetesConfig.ipv4` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalTransitSwitchSubnet`
|string
|
If your existing network infrastructure overlaps with the `100.88.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.

The default value is `100.88.0.0/16`.

|`internalJoinSubnet`
|string
|
If your existing network infrastructure overlaps with the `100.64.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the `clusterNetwork.cidr` value is `10.128.0.0/14` and the `clusterNetwork.hostPrefix` value is `/23`, then the maximum number of nodes is `2^(23-14)=512`.

The default value is `100.64.0.0/16`.

|====

.`ovnKubernetesConfig.ipv6` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalTransitSwitchSubnet`
|string
|
If your existing network infrastructure overlaps with the `fd97::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.

The default value is `fd97::/64`.

|`internalJoinSubnet`
|string
|
If your existing network infrastructure overlaps with the `fd98::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.

The default value is `fd98::/64`.

|====

// tag::policy-audit[]
.`policyAuditConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`rateLimit`
|integer
|The maximum number of messages to generate every second per node. The default value is `20` messages per second.

|`maxFileSize`
|integer
|The maximum size for the audit log in bytes. The default value is `50000000` or 50 MB.

|`maxLogFiles`
|integer
|The maximum number of log files that are retained.

|`destination`
|string
|
One of the following additional audit log targets:

`libc`:: The libc `syslog()` function of the journald process on the host.
`udp:<host>:<port>`:: A syslog server. Replace `<host>:<port>` with the host and port of the syslog server.
`unix:<file>`:: A Unix Domain Socket file specified by `<file>`.
`null`:: Do not send the audit logs to any additional target.

|`syslogFacility`
|string
|The syslog facility, such as `kern`, as defined by RFC5424. The default value is `local0`.

|====
// end::policy-audit[]

[id="gatewayConfig-object_{context}"]
.`gatewayConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`routingViaHost`
|`boolean`
|Set this field to `true` to send egress traffic from pods to the host networking stack.
For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack.
By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table.
The default value is `false`.

This field has an interaction with the Open vSwitch hardware offloading feature.
If you set this field to `true`, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack.

|`ipForwarding`
|`object`
|You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the `ipForwarding` specification in the `Network` resource. Specify `Restricted` to only allow IP forwarding for Kubernetes related traffic. Specify `Global` to allow forwarding of all IP traffic. For new installations, the default is `Restricted`. For updates to OpenShift Container Platform 4.14 or later, the default is `Global`.
[NOTE]
====
The default value of `Restricted` sets the IP forwarding to drop.
====

|`ipv4`
|`object`
|Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses.

|`ipv6`
|`object`
|Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses.

|====

[id="gatewayconfig-ipv4-object_{context}"]
.`gatewayConfig.ipv4` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalMasqueradeSubnet`
|`string`
|
The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `169.254.169.0/29`.
[IMPORTANT]
====
For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.
====

|====

[id="gatewayconfig-ipv6-object_{context}"]
.`gatewayConfig.ipv6` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`internalMasqueradeSubnet`
|`string`
|
The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `fd69::/125`.
[IMPORTANT]
====
For OpenShift Container Platform 4.17 and later versions, clusters use `fd69::/112` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.
====

|====

[id="nw-operator-cr-ipsec_{context}"]
.`ipsecConfig` object
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`mode`
|`string`
a|Specifies the behavior of the IPsec implementation. Must be one of the following values:

--
- `Disabled`: IPsec is not enabled on cluster nodes.
- `External`: IPsec is enabled for network traffic with external hosts.
- `Full`: IPsec is enabled for pod traffic and network traffic with external hosts.
--

|====

[NOTE]
====
You can only change the configuration for your cluster network plugin during cluster installation, except for the `gatewayConfig` field that can be changed at runtime as a postinstallation activity.
====

.Example OVN-Kubernetes configuration with IPSec enabled
[source,yaml]
----
defaultNetwork:
  type: OVNKubernetes
  ovnKubernetesConfig:
    mtu: 1400
    genevePort: 6081
    ipsecConfig:
      mode: Full
----

[id="nw-operator-example-cr_{context}"]
== Cluster Network Operator example configuration

A complete CNO configuration is specified in the following example:

.Example Cluster Network Operator object
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  serviceNetwork:
  - 172.30.0.0/16
  networkType: OVNKubernetes
----

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

[id="installation-gcp-provisioning-own-dns-records_{context}"]
= Provisioning your own DNS records

[role="_abstract"]
Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

[IMPORTANT]
====
Before you use this feature, you must add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".
====

.Prerequisites

* You installed your cluster.
* You installed the `gcloud` CLI tool.

.Procedure

. Determine the infrastructure ID of your cluster by running the following command:
+
[source,terminal]
----
$ infra_id=$(jq -r .infraID <installation_directory>/metadata.json)
----
+
where:
+
`<installation_directory>`:: Specifies the directory where you ran the installation program.

. Find the IP address of the API server:

.. If you installed a private cluster, determine the IP address of the API server by running the following command:
+
[source,terminal]
----
$ gcloud compute forwarding-rules describe "${infra_id}-api-internal" --project=<project_name> --region <region_name> --format json | jq -r .IPAddress
----
+
where:
+
`<project_name>`:: Specifies the name of your {gcp-full} project.
`<region_name>`:: Specifies the region where you installed your cluster.

.. If you installed a public cluster, determine the IP address of the API server by running the following command:
+
[source,terminal]
----
$ gcloud compute forwarding-rules describe --global "${infra_id}-apiserver" --format json | jq -r .IPAddress
----
. Use the IP address to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

. Find the IP address of the Ingress service:

.. If you installed a private cluster, find the IP address of the Ingress service by running the following command:
+
[source,terminal]
----
$ gcloud compute forwarding-rules list --project=<project_name> --filter="subnetwork:(projects/<project_name>/regions/<region_name>/subnetworks/<compute_subnet_name>)" --format="json" | jq -r '.[].IPAddress'
----
+
where:
+
`<project_name>`:: Specifies the name of your {gcp-full} project.
`<region_name>`:: Specifies the region where you installed your cluster.
`<compute_subnet_name>`:: Specifies the name of the subnet that contains your compute nodes.

.. If you installed a public cluster, find the IP address by using the forwarding rule:

... Find the forwarding rule for the Ingress service by running the following command:
+
[source,terminal]
----
$ ingress_forwarding_rule=$(gcloud compute target-pools list --format=json --filter="instances[]~${infra_id}" | jq -r .[].name)
----
... Use the forwarding rule value to find the IP address of the Ingress service by running the following command:
+
[source,terminal]
----
$ gcloud compute forwarding-rules describe --region "<region_name>" "${ingress_forwarding_rule}" --format json | jq -r .IPAddress
----
+
where:
+
`<region_name>`:: Specifies the region where you installed your cluster.

. Use the IP address to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

[role="_additional-resources"]
.Additional resources
* Additional {gcp-first} configuration parameters

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp_user_infra/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="cli-logging-in-kubeadmin_{context}"]
= Logging in to the cluster by using the CLI

[role="_abstract"]
To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and is created during OpenShift Container Platform installation.

.Prerequisites
* You deployed an OpenShift Container Platform cluster.
* You installed the {oc-first}.
* Ensure the bootstrap process completed successfully.

.Procedure

. Export the `kubeadmin` credentials by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
----
+
where:
+
`<installation_directory>`:: Specifies the path to the directory that stores the installation files.

. Verify you can run `oc` commands successfully using the exported configuration by running the following command:
+
[source,terminal]
----
$ oc whoami
----
+
.Example output
[source,terminal]
----
system:admin
----

[role="_additional-resources"]
.Additional resources

* See Accessing the web console for more details about accessing and understanding the OpenShift Container Platform web console.

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
.Additional resources

* See About remote health monitoring for more information about the Telemetry service

== Next steps

* Customize your cluster.
* If necessary, you can
Remote health reporting.
