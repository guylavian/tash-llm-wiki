---
title: "Installing a cluster on OpenStack on your own infrastructure"
type: reference
domain: openshift
slug: installing-4-22-installing-openstack-user
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-openstack-user
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on OpenStack on your own infrastructure

[id="installing-openstack-user"]
= Installing a cluster on OpenStack on your own infrastructure

In OpenShift Container Platform version , you can install a cluster on
{rh-openstack-first} that runs on user-provisioned infrastructure.

Using your own infrastructure allows you to integrate your cluster with existing infrastructure and modifications. The process requires more labor on your part than installer-provisioned installations, because you must create all {rh-openstack} resources, like Nova servers, Neutron ports, and security groups. However, Red Hat provides Ansible playbooks to help you in the deployment process.

== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You verified that OpenShift Container Platform  is compatible with your {rh-openstack} version by using the Supported platforms for OpenShift clusters section. You can also compare platform support across different versions by viewing the OpenShift Container Platform on {rh-openstack} support matrix.
* You have an {rh-openstack} account where you want to install OpenShift Container Platform.
* You understand performance and scalability practices for cluster scaling, control plane sizing, and etcd. For more information, see Recommended practices for scaling the cluster.
* On the machine from which you run the installation program, you have:
** A single directory in which you can keep the files you create during the installation process
** Python 3

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
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-default-deployment_{context}"]
= Resource guidelines for installing OpenShift Container Platform on {rh-openstack}

To support an OpenShift Container Platform installation, your {rh-openstack-first} quota must meet the following requirements:

.Recommended resources for a default OpenShift Container Platform cluster on {rh-openstack}
[options="header"]
|======================================
|Resource              | Value
|Floating IP addresses | 3
|Ports                 | 15
|Routers               | 1
|Subnets               | 1
|RAM                   | 88 GB
|vCPUs                 | 22
|Volume storage        | 275 GB
|Instances             | 7
|Security groups       | 3
|Security group rules  | 60
|Server groups         | 2 - plus 1 for each additional availability zone in each machine pool
|======================================

A cluster might function with fewer than recommended resources, but its performance is not guaranteed.

[IMPORTANT]
====
If {rh-openstack} object storage (Swift) is available and operated by a user account with the `swiftoperator` role, it is used as the default backend for the OpenShift Container Platform image registry. In this case, the volume storage requirement is 175 GB. Swift space requirements vary depending on the size of the image registry.
====

[NOTE]
By default, your security group and security group rule quotas might be low. If you encounter problems, run `openstack quota set --secgroups 3 --secgroup-rules 60 <project>` as an administrator to increase them.

An OpenShift Container Platform deployment comprises control plane machines, compute machines, and a bootstrap machine.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc

[id="installation-osp-control-machines_{context}"]
= Control plane machines

By default, the OpenShift Container Platform installation process creates three control
plane machines.

Each machine requires:

* An instance from the {rh-openstack} quota
* A port from the {rh-openstack} quota
* A flavor with at least 16 GB memory and 4 vCPUs
* At least 100 GB storage space from the {rh-openstack} quota

[id="installation-osp-compute-machines_{context}"]
= Compute machines

By default, the OpenShift Container Platform installation process creates three compute
machines.

Each machine requires:

* An instance from the {rh-openstack} quota
* A port from the {rh-openstack} quota
* A flavor with at least 8 GB memory and 2 vCPUs
* At least 100 GB storage space from the {rh-openstack} quota

[TIP]
====
Compute machines host the applications that you run on OpenShift Container Platform; aim to
run as many as you can.
====

Additionally, for clusters that use single-root input/output virtualization (SR-IOV), {rh-openstack} compute nodes require a flavor that supports huge pages.

[IMPORTANT]
====
SR-IOV deployments often employ performance optimizations, such as dedicated or isolated CPUs. For maximum performance, configure your underlying {rh-openstack} deployment to use these optimizations, and then run OpenShift Container Platform compute machines on the optimized infrastructure.
====

[role="_additional-resources"]
.Additional resources

* For more information about configuring performant {rh-openstack} compute nodes, see Configuring Compute nodes for performance.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc

[id="installation-osp-bootstrap-machine_{context}"]
= Bootstrap machine

During installation, a bootstrap machine is temporarily provisioned to stand up the
control plane. After the production control plane is ready, the bootstrap
machine is deprovisioned.

The bootstrap machine requires:

* An instance from the {rh-openstack} quota
* A port from the {rh-openstack} quota
* A flavor with at least 16 GB memory and 4 vCPUs
* At least 100 GB storage space from the {rh-openstack} quota

// Module included in the following assemblies:
// * installing/installing_openstack/installing-openstack-installer-user.adoc
// * installing/installing_openstack/uninstalling-openstack-user.adoc
//
//YOU MUST SET AN IFEVAL FOR EACH NEW MODULE

[id="installation-osp-downloading-modules_{context}"]
= Downloading playbook dependencies

The Ansible playbooks that simplify the installation process on user-provisioned infrastructure require several ansible collections and Python modules. On the machine where you will run the installation program, add the {rh-openstack-first} repositories and then install the packages.

The following dependencies are required:

* Python modules:
** `openstackclient`
** `openstacksdk`
** `netaddr`
** `pip`
* Ansible collections:
** `ansible-collections-openstack`, which installs Ansible Core
** `ansible-collection-community-general`
** `ansible-collection-ansible-netcommon`

The Ansible playbooks that simplify the removal process on user-provisioned
infrastructure require several Python modules. On the machine where you will run the process,
add the modules' repositories and then download them.

[NOTE]
These instructions assume that you are using {op-system-base-full} 8.

.Prerequisites

* Python 3 is installed on your machine.

.Procedure

. On a command line, add the repositories:

.. Register with Red Hat Subscription Manager:
+
[source,terminal]
----
$ sudo subscription-manager register # If not done already
----

.. Pull the latest subscription data:
+
[source,terminal]
----
$ sudo subscription-manager attach --pool=$YOUR_POOLID # If not done already
----

.. Disable the current repositories:
+
[source,terminal]
----
$ sudo subscription-manager repos --disable=* # If not done already
----

.. Add the required repositories:
+
[source,terminal]
----
$ sudo subscription-manager repos \
  --enable=rhel-9-for-x86_64-appstream-rpms \
  --enable=rhel-9-for-x86_64-baseos-rpms \
  --enable=openstack-17.1-for-rhel-9-x86_64-rpms
----

. Install the modules:
+
[source,terminal]
----
$ sudo dnf install ansible-collection-ansible-netcommon \
    ansible-collection-community-general \
    ansible-collections-openstack \
    python3-netaddr \
    python3-openstackclient \
    python3-openstacksdk \
    python3-pip
----

. Install the modules:
+
[source,terminal]
----
$ sudo yum install python3-openstackclient ansible python3-openstacksdk
----

. Ensure that the `python` command points to `python3`:
+
[source,terminal]
----
$ sudo alternatives --set python /usr/bin/python3
----

// Module included in the following assemblies:
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-downloading-playbooks_{context}"]
= Downloading the installation playbooks

Download Ansible playbooks that you can use to install OpenShift Container Platform on your own {rh-openstack-first} infrastructure.

.Prerequisites

* The curl command-line tool is available on your machine.

.Procedure

* To download the playbooks to your working directory, run the following script from a command line:
+
[source,terminal,subs=attributes+]
----
$ xargs -n 1 curl -O <<< '
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/bootstrap.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/common.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/compute-nodes.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/control-plane.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/down-bootstrap.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/down-compute-nodes.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/down-control-plane.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/down-network.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/down-security-groups.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/down-containers.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/inventory.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/network.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/security-groups.yaml
        https://raw.githubusercontent.com/openshift/installer/release-/upi/openstack/update-network-resources.yaml'
----

The playbooks are downloaded to your machine.

[IMPORTANT]
====
During the installation process, you can modify the playbooks to configure your deployment.

Retain all playbooks for the life of your cluster. You must have the playbooks to remove your OpenShift Container Platform cluster from {rh-openstack}.
====

[IMPORTANT]
====
You must match any edits you make in the `bootstrap.yaml`, `compute-nodes.yaml`, `control-plane.yaml`, `network.yaml`, and `security-groups.yaml` files to the corresponding playbooks that are prefixed with `down-`. For example, edits to the `bootstrap.yaml` file must be reflected in the `down-bootstrap.yaml` file, too. If you do not edit both files, the supported cluster removal process will fail.
====

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

// include::modules/installation-osp-enabling-swift.adoc[leveloffset=+1]
//Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-creating-image_{context}"]
= Creating the {op-system-first} image

The OpenShift Container Platform installation program requires that a {op-system-first} image be present in the {rh-openstack-first} cluster. Retrieve the latest {op-system} image, then upload it using the {rh-openstack} CLI.

.Prerequisites

* The {rh-openstack} CLI is installed.

.Procedure

. Log in to the Red Hat Customer Portal's https://access.redhat.com/downloads/content/290[Product Downloads page].

. Under *Version*, select the most recent release of OpenShift Container Platform  for {op-system-base-full} 8.
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform.
You must download images with the highest version that is less than or equal to
the OpenShift Container Platform version that you install. Use the image versions that match
your OpenShift Container Platform version if they are available.
====

. Download the _{op-system-first} - OpenStack Image (QCOW)_.

. Decompress the image.
+
[NOTE]
====
You must decompress the {rh-openstack} image before the cluster can use it. The name of the downloaded file might not contain a compression extension, like `.gz` or `.tgz`. To find out if or how the file is compressed, in a command line, enter:

[source,terminal]
----
$ file <name_of_downloaded_file>
----

====

. From the image that you downloaded, create an image that is named `rhcos` in your cluster by using the {rh-openstack} CLI:
+
[source,terminal]
----
$ openstack image create --container-format=bare --disk-format=qcow2 --file rhcos-${RHCOS_VERSION}-openstack.qcow2 rhcos
----
+
[IMPORTANT]
Depending on your {rh-openstack} environment, you might be able to upload the image in either `.raw` or `.qcow2` formats. If you use Ceph, you must use the `.raw` format.
+
[WARNING]
If the installation program finds multiple images with the same name, it chooses one of them at random. To avoid this behavior, create unique names for resources in {rh-openstack}.

After you upload the image to {rh-openstack}, it is usable in the installation process.

//Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
//
// DNS resolution KI

[id="installation-osp-verifying-external-network_{context}"]
= Verifying external network access

The OpenShift Container Platform installation process requires external network access. You must provide an external network value to it, or deployment fails. Before you begin the process, verify that a network with the external router type exists in {rh-openstack-first}.

.Prerequisites
* https://docs.openstack.org/neutron/rocky/admin/config-dns-res.html#case-2-dhcp-agents-forward-dns-queries-from-instances[Configure OpenStack's networking service to have DHCP agents forward instances' DNS queries]

.Procedure

. Using the {rh-openstack} CLI, verify the name and ID of the 'External' network:
+
[source,terminal]
----
$ openstack network list --long -c ID -c Name -c "Router Type"
----
+
.Example output
[source,terminal]
----
+--------------------------------------+----------------+-------------+
| ID                                   | Name           | Router Type |
+--------------------------------------+----------------+-------------+
| 148a8023-62a7-4672-b018-003462f8d7dc | public_network | External    |
+--------------------------------------+----------------+-------------+
----

A network with an external router type appears in the network list. If at least one does not, see Creating a default floating IP network and Creating a default provider network.

[IMPORTANT]
====
If the external network's CIDR range overlaps one of the default network ranges, you must change the matching network ranges in the `install-config.yaml` file before you start the installation process.

The default network ranges are:
[options="header"]
|====
|Network |Range

|`machineNetwork`
|10.0.0.0/16

|`serviceNetwork`
|172.30.0.0/16

|`clusterNetwork`
|10.128.0.0/14
|====
====

[WARNING]
If the installation program finds multiple networks with the same name, it sets one of them at random. To avoid this behavior, create unique names for resources in {rh-openstack}.

[NOTE]
====
If the Neutron trunk service plugin is enabled, a trunk port is created by default. For more information, see https://wiki.openstack.org/wiki/Neutron/TrunkPort[Neutron trunk port].
====

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
//
// Stub module. To be used with other FIP OSP modules only.

[id="installation-osp-accessing-api_{context}"]
= Enabling access to the environment

At deployment, all OpenShift Container Platform machines are created in a {rh-openstack-first}-tenant network. Therefore, they are not accessible directly in most {rh-openstack} deployments.

You can configure OpenShift Container Platform API and application access by using floating IP addresses (FIPs) during installation. You can also complete an installation without configuring FIPs, but the installer will not configure a way to reach the API or applications externally.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-accessing-api-floating_{context}"]
= Enabling access with floating IP addresses

Create floating IP (FIP) addresses for external access to the OpenShift Container Platform

.Procedure

. Using the {rh-openstack-first} CLI, create the API FIP:
+
[source,terminal]
----
$ openstack floating ip create --description "API <cluster_name>.<base_domain>" <external_network>
----

. Using the {rh-openstack-first} CLI, create the apps, or Ingress, FIP:
+
[source,terminal]
----
$ openstack floating ip create --description "Ingress <cluster_name>.<base_domain>" <external_network>
----

. By using the {rh-openstack-first} CLI, create the bootstrap FIP:
+
[source,terminal]
----
$ openstack floating ip create --description "bootstrap machine" <external_network>
----

. Add records that follow these patterns to your DNS server for the API and Ingress FIPs:
+
[source,dns]
----
api.<cluster_name>.<base_domain>.  IN  A  <API_FIP>
*.apps.<cluster_name>.<base_domain>. IN  A <apps_FIP>
----
+
[NOTE]
====
If you do not control the DNS server, you can access the cluster by adding the cluster domain names such as the following to your `/etc/hosts` file:

* `<api_floating_ip> api.<cluster_name>.<base_domain>`
* `<application_floating_ip> grafana-openshift-monitoring.apps.<cluster_name>.<base_domain>`
* `<application_floating_ip> prometheus-k8s-openshift-monitoring.apps.<cluster_name>.<base_domain>`
* `<application_floating_ip> oauth-openshift.apps.<cluster_name>.<base_domain>`
* `<application_floating_ip> console-openshift-console.apps.<cluster_name>.<base_domain>`
* `application_floating_ip integrated-oauth-server-openshift-authentication.apps.<cluster_name>.<base_domain>`

The cluster domain names in the `/etc/hosts` file grant access to the web console and the monitoring interface of your cluster locally. You can also use the `kubectl` or `oc`. You can access the user applications by using the additional entries pointing to the <application_floating_ip>. This action makes the API and applications accessible to only you, which is not suitable for production deployment, but does allow installation for development and testing.
====

. Add the FIPs to the
file as the values of the following

* `os_api_fip`
* `os_bootstrap_fip`
* `os_ingress_fip`

* `platform.openstack.ingressFloatingIP`
* `platform.openstack.apiFloatingIP`

If you use these values, you must also enter an external network as the value of the

[TIP]
====
You can make OpenShift Container Platform resources available outside of the cluster by assigning a floating IP address and updating your firewall configuration.
====

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-accessing-api-no-floating_{context}"]
= Completing installation without floating IP addresses

You can install OpenShift Container Platform on {rh-openstack-first} without providing floating IP addresses.

In the
file, do not define the following

* `platform.openstack.ingressFloatingIP`
* `platform.openstack.apiFloatingIP`

If you cannot provide an external network, you can also leave `platform.openstack.externalNetwork` blank. If you do not provide a value for `platform.openstack.externalNetwork`, a router is not created for you, and, without additional action, the installer will fail to retrieve an image from Glance. You must configure external connectivity on your own.

* `os_api_fip`
* `os_bootstrap_fip`
* `os_ingress_fip`

If you cannot provide an external network, you can also leave `os_external_network` blank. If you do not provide a value for `os_external_network`, a router is not created for you, and, without additional action, the installer will fail to retrieve an image from Glance. Later in the installation process, when you create network resources, you must configure external connectivity on your own.

If you run the installer
from a system that cannot reach the cluster API due to a lack of floating IP addresses or name resolution, installation fails. To prevent installation failure in these cases, you can use a proxy network or run the installer from a system that is on the same network as your machines.

[NOTE]
====
You can enable name resolution by creating DNS records for the API and Ingress ports. For example:

[source,dns]
----
api.<cluster_name>.<base_domain>.  IN  A  <api_port_IP>
*.apps.<cluster_name>.<base_domain>. IN  A <ingress_port_IP>
----

If you do not control the DNS server, you can add the record to your `/etc/hosts` file. This action makes the API accessible to only you, which is not suitable for production deployment but does allow installation for development and testing.
====

//Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-user.adoc

[id="installation-osp-describing-cloud-parameters_{context}"]
= Defining parameters for the installation program

The OpenShift Container Platform installation program relies on a file that is called `clouds.yaml`. The file describes {rh-openstack-first} configuration parameters, including the project name, log in information, and authorization service URLs.

.Procedure

. Create the `clouds.yaml` file:

** If your {rh-openstack} distribution includes the Horizon web UI, generate a `clouds.yaml` file in it.
+
[IMPORTANT]
====
Remember to add a password to the `auth` field. You can also keep secrets in a separate file from `clouds.yaml`.
====

** If your {rh-openstack} distribution does not include the Horizon web UI, or you do not want to use Horizon, create the file yourself. For detailed information about `clouds.yaml`, see https://docs.openstack.org/openstacksdk/latest/user/config/configuration.html#config-files[Config files] in the {rh-openstack} documentation.
+
[source,yaml]
----
clouds:
  shiftstack:
    auth:
      auth_url: http://10.10.14.42:5000/v3
      project_name: shiftstack
      username: <username>
      password: <password>
      user_domain_name: Default
      project_domain_name: Default
  dev-env:
    region_name: RegionOne
    auth:
      username: <username>
      password: <password>
      project_name: 'devonly'
      auth_url: 'https://10.10.14.22:5001/v2.0'
----

. If your {rh-openstack} installation uses self-signed certificate authority (CA) certificates for endpoint authentication:
.. Copy the certificate authority file to your machine.
.. Add the `cacerts` key to the `clouds.yaml` file. The value must be an absolute, non-root-accessible path to the CA certificate:
+
[source,yaml]
----
clouds:
  shiftstack:
    ...
    cacert: "/etc/pki/ca-trust/source/anchors/ca.crt.pem"
----
+
[TIP]
====
After you run the installer with a custom CA certificate, you can update the certificate by editing the value of the `ca-cert.pem` key in the `cloud-provider-config` keymap. On a command line, run:
[source,terminal]
----
$ oc edit configmap -n openshift-config cloud-provider-config
----
====

. Place the `clouds.yaml` file in one of the following locations:
.. The value of the `OS_CLIENT_CONFIG_FILE` environment variable
.. The current directory
.. A Unix-specific user configuration directory, for example `~/.config/openstack/clouds.yaml`
.. A Unix-specific site configuration directory, for example `/etc/openstack/clouds.yaml`
+
The installation program searches for `clouds.yaml` in that order.
[TIP]
To set up an isolated development environment, you can use a bare metal host that runs CentOS 7. See https://github.com/shiftstack-dev-tools/ocp-doit[OpenShift Installer OpenStack Dev Scripts] for details.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-creating-network-resources_{context}"]
= Creating network resources on {rh-openstack}

Create the network resources that an OpenShift Container Platform on {rh-openstack-first} installation on your own infrastructure requires. To save time, run supplied Ansible playbooks that generate security groups, networks, subnets, routers, and ports.

.Prerequisites

* You downloaded the modules in "Downloading playbook dependencies".
* You downloaded the playbooks in "Downloading the installation playbooks".

.Procedure

. For a dual stack cluster deployment, edit the `inventory.yaml` file and uncomment the `os_subnet6` attribute.

. To ensure that your network resources have unique names on the {rh-openstack} deployment, create an environment variable and JSON file for use in the Ansible playbooks:
+
.. Create an environment variable that has a unique name value by running the following command:
+
[source,terminal]
----
$ export OS_NET_ID="openshift-$(dd if=/dev/urandom count=4 bs=1 2>/dev/null |hexdump -e '"%02x"')"
----

.. Verify that the variable is set by running the following command on a command line:
+
[source,terminal]
----
$ echo $OS_NET_ID
----

.. Create a JSON object that includes the variable in a file called `netid.json` by running the following command:
+
[source,terminal]
----
$ echo "{\"os_net_id\": \"$OS_NET_ID\"}" | tee netid.json
----

. On a command line, create the network resources by running the following command:
+
[source,terminal]
----
$ ansible-playbook -i inventory.yaml network.yaml
----
+
[NOTE]
====
The API and Ingress VIP fields will be overwritten in the `inventory.yaml` playbook with the IP addresses assigned to the network ports.
====
+
[NOTE]
====
The resources created by the `network.yaml` playbook are deleted by the `down-network.yaml` playbook.
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
* Installation configuration parameters for OpenStack

// Module included in the following assemblies:
//

// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-custom-subnet_{context}"]
= Custom subnets in {rh-openstack} deployments

Optionally, you can deploy a cluster on a {rh-openstack-first} subnet of your choice. The subnet's GUID is passed as the value of `platform.openstack.machinesSubnet` in the `install-config.yaml` file.

This subnet is used as the cluster's primary subnet. By default, nodes and ports are created on it. You can create nodes and ports on a different {rh-openstack} subnet by setting the value of the `platform.openstack.machinesSubnet` property to the subnet's UUID.

Before you run the OpenShift Container Platform installer with a custom subnet, verify that your configuration meets the following requirements:

* The subnet that is used by `platform.openstack.machinesSubnet` has DHCP enabled.
* The CIDR of `platform.openstack.machinesSubnet` matches the CIDR of `networking.machineNetwork`.
* The installation program user has permission to create ports on this network, including ports with fixed IP addresses.

Clusters that use custom subnets have the following limitations:

* If you plan to install a cluster that uses floating IP addresses, the `platform.openstack.machinesSubnet` subnet must be attached to a router that is connected to the `externalNetwork` network.

* If the `platform.openstack.machinesSubnet` value is set in the `install-config.yaml` file, the installation program does not create a private network or subnet for your {rh-openstack} machines.

* You cannot use the `platform.openstack.externalDNS` property at the same time as a custom subnet. To add DNS to a cluster that uses a custom subnet, configure DNS on the {rh-openstack} network.

[NOTE]
====
By default, the API VIP takes x.x.x.5 and the Ingress VIP takes x.x.x.7 from your network's CIDR block. To override these default values,
set values for `platform.openstack.apiVIPs` and `platform.openstack.ingressVIPs` that are outside of the DHCP allocation pool.
====

[IMPORTANT]
====
The CIDR ranges for networks are not adjustable after cluster installation. Red Hat does not provide direct guidance on determining the range during cluster installation because it requires careful consideration of the number of created pods per namespace.
====

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc

[id="installation-osp-config-yaml_{context}"]
= Sample customized install-config.yaml file for {rh-openstack}

The following example `install-config.yaml` files demonstrate all of the possible {rh-openstack-first} customization options.

[IMPORTANT]
This sample file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program.

.Example single stack `install-config.yaml` file
[%collapsible]
====
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  platform: {}
  replicas: 3
compute:
- name: worker
  platform:
    openstack:
      type: ml.large
  replicas: 3
metadata:
  name: example
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
  networkType: OVNKubernetes
platform:
  openstack:
    cloud: mycloud
    externalNetwork: external
    computeFlavor: m1.xlarge
    apiFloatingIP: 128.0.0.1
fips: false
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----
====

.Example dual stack `install-config.yaml` file
[%collapsible]
====
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  platform: {}
  replicas: 3
compute:
- name: worker
  platform:
    openstack:
      type: ml.large
  replicas: 3
metadata:
  name: example
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  - cidr: fd01::/48
    hostPrefix: 64
  machineNetwork:
  - cidr: 192.168.25.0/24
  - cidr: fd2e:6f44:5dd8:c956::/64
  serviceNetwork:
  - 172.30.0.0/16
  - fd02::/112
  networkType: OVNKubernetes
platform:
  openstack:
    cloud: mycloud
    externalNetwork: external
    computeFlavor: m1.xlarge
    apiVIPs:
    - 192.168.25.10
    - fd2e:6f44:5dd8:c956:f816:3eff:fec3:5955
    ingressVIPs:
    - 192.168.25.132
    - fd2e:6f44:5dd8:c956:f816:3eff:fe40:aecb
    controlPlanePort:
      fixedIPs:
      - subnet:
          name: openshift-dual4
      - subnet:
          name: openshift-dual6
      network:
        name: openshift-dual
fips: false
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----
====

// Module included in the following assemblies:
// * installing/installing_openstack/installing-openstack-installer-user.adoc
//
//YOU MUST SET AN IFEVAL FOR EACH NEW MODULE

[id="installation-osp-fixing-subnet_{context}"]
= Setting a custom subnet for machines

The IP range that the installation program uses by default might not match the Neutron subnet that you create when you install OpenShift Container Platform. If necessary, update the CIDR value for new machines by editing the installation configuration file.

.Prerequisites

* You have the `install-config.yaml` file that was generated by the OpenShift Container Platform installation program.
* You have Python 3 installed.

.Procedure

. On a command line, browse to the directory that contains the `install-config.yaml` and `inventory.yaml` files.

. From that directory, either run a script to edit the `install-config.yaml` file or update the file manually:

** To set the value by using a script, run the following command:
+
[source,terminal]
----
$ python -c 'import os
import sys
import yaml
import re
re_os_net_id = re.compile(r"{{\s*os_net_id\s*}}")
os_net_id = os.getenv("OS_NET_ID")
path = "common.yaml"
facts = None
for _dict in yaml.safe_load(open(path))[0]["tasks"]:
    if "os_network" in _dict.get("set_fact", {}):
        facts = _dict["set_fact"]
        break
if not facts:
    print("Cannot find `os_network` in common.yaml file. Make sure OpenStack resource names are defined in one of the tasks.")
    sys.exit(1)
os_network = re_os_net_id.sub(os_net_id, facts["os_network"])
os_subnet = re_os_net_id.sub(os_net_id, facts["os_subnet"])
path = "install-config.yaml"
data = yaml.safe_load(open(path))
inventory = yaml.safe_load(open("inventory.yaml"))["all"]["hosts"]["localhost"]
machine_net = [{"cidr": inventory["os_subnet_range"]}]
api_vips = [inventory["os_apiVIP"]]
ingress_vips = [inventory["os_ingressVIP"]]
ctrl_plane_port = {"network": {"name": os_network}, "fixedIPs": [{"subnet": {"name": os_subnet}}]}
if inventory.get("os_subnet6_range"): <1>
    os_subnet6 = re_os_net_id.sub(os_net_id, facts["os_subnet6"])
    machine_net.append({"cidr": inventory["os_subnet6_range"]})
    api_vips.append(inventory["os_apiVIP6"])
    ingress_vips.append(inventory["os_ingressVIP6"])
    data["networking"]["networkType"] = "OVNKubernetes"
    data["networking"]["clusterNetwork"].append({"cidr": inventory["cluster_network6_cidr"], "hostPrefix": inventory["cluster_network6_prefix"]})
    data["networking"]["serviceNetwork"].append(inventory["service_subnet6_range"])
    ctrl_plane_port["fixedIPs"].append({"subnet": {"name": os_subnet6}})
data["networking"]["machineNetwork"] = machine_net
data["platform"]["openstack"]["apiVIPs"] = api_vips
data["platform"]["openstack"]["ingressVIPs"] = ingress_vips
data["platform"]["openstack"]["controlPlanePort"] = ctrl_plane_port
del data["platform"]["openstack"]["externalDNS"]
open(path, "w").write(yaml.dump(data, default_flow_style=False))'
----
<1> Applies to dual stack (IPv4/IPv6) environments.

// Module included in the following assemblies:
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-emptying-worker-pools_{context}"]
= Emptying compute machine pools

To proceed with an installation that uses your own infrastructure, set the number of compute machines in the installation configuration file to zero. Later, you create these machines manually.

.Prerequisites

* You have the `install-config.yaml` file that was generated by the OpenShift Container Platform installation program.

.Procedure

. On a command line, browse to the directory that contains `install-config.yaml`.

. From that directory, either run a script to edit the `install-config.yaml` file or update the file manually:

** To set the value by using a script, run:
+
[source,terminal]
----
$ python -c '
import yaml;
path = "install-config.yaml";
data = yaml.safe_load(open(path));
data["compute"][0]["replicas"] = 0;
open(path, "w").write(yaml.dump(data, default_flow_style=False))'
----

** To set the value manually, open the file and set the value of `compute.<first entry>.replicas` to `0`.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-provider-networks_{context}"]
= Cluster deployment on {rh-openstack} provider networks

You can deploy your OpenShift Container Platform clusters on {rh-openstack-first} with a primary network interface on a provider network. Provider networks are commonly used to give projects direct access to a public network that can be used to reach the internet. You can also share provider networks among projects as part of the network creation process.

{rh-openstack} provider networks map directly to an existing physical network in the data center. A {rh-openstack} administrator must create them.

In the following example, OpenShift Container Platform workloads are connected to a data center by using a provider network:

image::openshift-on-openstack-provider-network.png[A diagram that depicts four OpenShift workloads on OpenStack. Each workload is connected by its NIC to an external data center by using a provider network.]

OpenShift Container Platform clusters that are installed on provider networks do not require tenant networks or floating IP addresses. The installer does not create these resources during installation.

Example provider network types include flat (untagged) and VLAN (802.1Q tagged).

[NOTE]
====
A cluster can support as many provider network connections as the network type allows. For example, VLAN networks typically support up to 4096 connections.
====

You can learn more about provider and tenant networks in the {rh-openstack} documentation.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-provider-network-preparation_{context}"]
= {rh-openstack} provider network requirements for cluster installation

Before you install an OpenShift Container Platform cluster, your {rh-openstack-first} deployment and provider network must meet a number of conditions:

* The {rh-openstack} networking service (Neutron) is enabled and accessible through the {rh-openstack} networking API.
* The {rh-openstack} networking service has the port security and allowed address pairs extensions enabled.
* The provider network can be shared with other tenants.
+
[TIP]
====
Use the `openstack network create` command with the `--share` flag to create a network that can be shared.
====
* The {rh-openstack} project that you use to install the cluster must own the provider network, as well as an appropriate subnet.
+
[TIP]
====
To create a network for a project that is named "openshift," enter the following command::
[source,terminal]
----
$ openstack network create --project openshift
----

To create a subnet for a project that is named "openshift," enter the following command::
[source,terminal]
----
$ openstack subnet create --project openshift
----

To learn more about creating networks on {rh-openstack}, read the provider networks documentation.
====
+
If the cluster is owned by the `admin` user, you must run the installer as that user to create ports on the network.
+
[IMPORTANT]
====
Provider networks must be owned by the {rh-openstack} project that is used to create the cluster. If they are not, the {rh-openstack} Compute service (Nova) cannot request a port from that network.
====

* Verify that the provider network can reach the {rh-openstack} metadata service IP address, which is `169.254.169.254` by default.
+
Depending on your {rh-openstack} SDN and networking service configuration, you might need to provide the route when you create the subnet. For example:
+
[source,terminal]
----
$ openstack subnet create --dhcp --host-route destination=169.254.169.254/32,gateway=192.0.2.2 ...
----

* Optional: To secure the network, create role-based access control (RBAC) rules that limit network access to a single project.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-deploying-provider-networks-installer_{context}"]
= Deploying a cluster that has a primary interface on a provider network

You can deploy an OpenShift Container Platform cluster that has its primary network interface on an {rh-openstack-first} provider network.

.Prerequisites

* Your {rh-openstack-first} deployment is configured as described by "{rh-openstack} provider network requirements for cluster installation".

.Procedure

. In a text editor, open the `install-config.yaml` file.
. Set the value of the `platform.openstack.apiVIPs` property to the IP address for the API VIP.
. Set the value of the `platform.openstack.ingressVIPs` property to the IP address for the Ingress VIP.
. Set the value of the `platform.openstack.machinesSubnet` property to the UUID of the provider network subnet.
. Set the value of the `networking.machineNetwork.cidr` property to the CIDR block of the provider network subnet.

[IMPORTANT]
====
The `platform.openstack.apiVIPs` and `platform.openstack.ingressVIPs` properties must both be unassigned IP addresses from the `networking.machineNetwork.cidr` block.
====

.Section of an installation configuration file for a cluster that relies on a {rh-openstack} provider network
[source,yaml]
----
        ...
        platform:
          openstack:
            apiVIPs: <1>
              - 192.0.2.13
            ingressVIPs: <1>
              - 192.0.2.23
            machinesSubnet: fa806b2f-ac49-4bce-b9db-124bc64209bf
            # ...
        networking:
          machineNetwork:
          - cidr: 192.0.2.0/24
----

<1> In OpenShift Container Platform 4.12 and later, the `apiVIP` and `ingressVIP` configuration settings are deprecated. Instead, use a list format to enter values in the `apiVIPs` and `ingressVIPs` configuration settings.

[WARNING]
====
You cannot set the `platform.openstack.externalNetwork` or `platform.openstack.externalDNS` parameters while using a provider network for the primary network interface.
====

When you deploy the cluster, the installer uses the `install-config.yaml` file to deploy the cluster on the provider network.

[TIP]
====
You can add additional networks, including provider networks, to the `platform.openstack.additionalNetworkIDs` list.

After you deploy your cluster, you can attach pods to additional networks. For more information, see Understanding multiple networks.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-user-infra-generate-k8s-manifest-ignition_{context}"]
= Creating the Kubernetes manifest and Ignition config files

[role="_abstract"]
To customize cluster definitions and manually start machines, generate the Kubernetes manifest and Ignition config files.

The installation configuration file transforms into the Kubernetes manifests. The manifests wrap into the Ignition configuration files, which are later used to configure the cluster machines.

[IMPORTANT]
====
* The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

[NOTE]
====
The installation program that generates the manifest and Ignition files is architecture specific and can be obtained from the
client image mirror. The Linux version of the installation program runs on s390x only. This installer program is also available as a macOS version.
====
[NOTE]
====
The installation program that generates the manifest and Ignition files is architecture specific and can be obtained from the
client image mirror. The Linux version of the installation program (without an architecture postfix) runs on ppc64le only. This installer program is also available as a macOS version.
====

.Prerequisites

* You obtained the OpenShift Container Platform installation program.
For a restricted network installation, these files are on your mirror host.
* You created the `install-config.yaml` installation configuration file.

.Procedure

. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----
+
where
+
`<installation_directory>`:: Specifies the installation directory that contains the `install-config.yaml` file you created.

. Remove the Kubernetes manifest files that define the control plane machines:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_master-machines-*.yaml
----
+
By removing these files, you prevent the cluster from automatically generating control plane machines.

. Remove the Kubernetes manifest files that define the control plane machine set:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
----

. Optional: If you do not want the cluster to provision compute machines, remove
the Kubernetes manifest files that define the worker machines:
. Remove the Kubernetes manifest files that define the worker machines:
+
[source,terminal]
----
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
----
+
[IMPORTANT]
====
If you disabled the `MachineAPI` capability when installing a cluster on user-provisioned infrastructure, you must remove the Kubernetes manifest files that define the worker machines. Otherwise, your cluster fails to install.
====
+
Because you create and manage the worker machines yourself, you do not need to initialize these machines.

. Remove the Kubernetes manifest files that define the control plane machines, compute machine sets, and control plane machine sets:
+
[source,terminal]
----
$ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
----
+
Because you create and manage these resources yourself, you do not have to initialize them. You can preserve the compute machine set files to create compute machines by using the machine API, but you must update references to them to match your environment.
+
[WARNING]
====
If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable.
====
+
[IMPORTANT]
====
When you configure control plane nodes from the default unschedulable to schedulable, additional subscriptions are required. This is because control plane nodes then become compute nodes.
====

. Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:
+
.. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
+
.. Locate the `mastersSchedulable` parameter and ensure that it is set to `false`.
+
.. Save and exit the file.

. Optional: If you do not want
the Ingress Operator
to create DNS records on your behalf, remove the `privateZone` and `publicZone`
sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:
. Remove the `privateZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: DNS
metadata:
  creationTimestamp: null
  name: cluster
spec:
  baseDomain: example.openshift.com
  privateZone:
    id: mycluster-100419-private-zone
  publicZone: <1>
    id: example.openshift.com
status: {}
----
`spec.privateZone`: Remove this section completely.
+
If you do so, you must add ingress DNS records manually in a later step.

. Configure the cloud provider for your VPC.
+
.. Open the `<installation_directory>/manifests/cloud-provider-config.yaml` file.
+
.. Add the `network-project-id` parameter and set its value to the ID of project that hosts the shared VPC network.
+
.. Add the `network-name` parameter and set its value to the name of the shared VPC network that hosts the OpenShift Container Platform cluster.
+
.. Replace the value of the `subnetwork-name` parameter with the value of the shared VPC subnet that hosts your compute machines.
+
The contents of the `<installation_directory>/manifests/cloud-provider-config.yaml` resemble the following example:
+
[source,yaml]
----
config: |+
  [global]
  project-id      = example-project
  regional        = true
  multizone       = true
  node-tags       = opensh-ptzzx-master
  node-tags       = opensh-ptzzx-worker
  node-instance-prefix = opensh-ptzzx
  external-instance-groups-prefix = opensh-ptzzx
  network-project-id = example-shared-vpc
  network-name    = example-network
  subnetwork-name = example-worker-subnet
----

. If you deploy a cluster that is not on a private network, open the `<installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml` file and replace the value of the `scope` parameter with `External`. The contents of the file resemble the following example:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: null
  name: default
  namespace: openshift-ingress-operator
spec:
  endpointPublishingStrategy:
    loadBalancer:
      scope: External
    type: LoadBalancerService
status:
  availableReplicas: 0
  domain: ''
  selector: ''
----

. Optional: If your Azure Stack Hub environment uses an internal certificate authority (CA), you must update the `.spec.trustedCA.name` field in the `<installation_directory>/manifests/cluster-proxy-01-config.yaml` file to use `user-ca-bundle`:
+
[source,yaml]
----
...
spec:
  trustedCA:
    name: user-ca-bundle
...
----
+
Later, you must update your bootstrap ignition to include the CA.

. When configuring Azure on user-provisioned infrastructure, you must export
some common variables defined in the manifest files to use later in the Azure
Resource Manager (ARM) templates:
+
.. Export the infrastructure ID by using the following command:
+
[source,terminal]
----
$ export INFRA_ID=<infra_id>
----
+
where:
+
`<infra_id>`:: Specifies that the OpenShift Container Platform cluster has been assigned an identifier (`INFRA_ID`) in the form of `<cluster_name>-<random_string>`. This identifier is used as the base name for most resources created using the provided ARM templates. This is the value of the `.status.infrastructureName` attribute from the `manifests/cluster-infrastructure-02-config.yml` file.
+
.. Export the resource group by using the following command:
+
[source,terminal]
----
$ export RESOURCE_GROUP=<resource_group>
----
+
where:
+
`<resource_group>`:: All resources created in this Azure deployment exists as part of a resource group. The resource group name is also based on the `INFRA_ID`, in the form of `<cluster_name>-<random_string>-rg`. This is the value of the `.status.platformStatus.azure.resourceGroupName` attribute from the `manifests/cluster-infrastructure-02-config.yml` file.

. Manually create your cloud credentials.
+
.. From the directory that contains the installation program, obtain details of the OpenShift Container Platform release image that your `openshift-install` binary is built to use:
+
[source,terminal]
----
$ openshift-install version
----
+
.Example output
[source,text]
----
release image quay.io/openshift-release-dev/ocp-release:4.y.z-x86_64
----
+
.. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----
+
.. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \//
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \//
  --to=<path_to_directory_for_credentials_requests>
----
+
where:
+
`--included`::  Specifies to include only the manifests that your specific cluster configuration requires.
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
  labels:
    controller-tools.k8s.io: "1.0"
  name: openshift-image-registry-azure
  namespace: openshift-cloud-credential-operator
spec:
  secretRef:
    name: installer-cloud-credentials
    namespace: openshift-image-registry
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
----
+
.. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object. The format for the secret data varies for each cloud provider.
+
.Sample `secrets.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
    name: ${secret_name}
    namespace: ${secret_namespace}
stringData:
  azure_subscription_id: ${subscription_id}
  azure_client_id: ${app_id}
  azure_client_secret: ${client_secret}
  azure_tenant_id: ${tenant_id}
  azure_resource_prefix: ${cluster_name}
  azure_resourcegroup: ${resource_group}
  azure_region: ${azure_region}
----
+
.. Create a `cco-configmap.yaml` file in the manifests directory with the Cloud Credential Operator (CCO) disabled:
+
.Sample `ConfigMap` object
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
name: cloud-credential-operator-config
namespace: openshift-cloud-credential-operator
  annotations:
    release.openshift.io/create-only: "true"
data:
  disabled: "true"
----

. To create the Ignition configuration files, run the following command from the directory that contains the installation program:
+
[source,terminal]
----
$ ./openshift-install create ignition-configs --dir <installation_directory>
----
+
where:
+
`<installation_directory>`:: Specifies the same installation directory.
+
Ignition config files are created for the bootstrap, control plane, and compute nodes in the installation directory. The `kubeadmin-password` and `kubeconfig` files are created in the `./<installation_directory>/auth` directory:
+
----
.
├── auth
│   ├── kubeadmin-password
│   └── kubeconfig
├── bootstrap.ign
├── master.ign
├── metadata.json
└── worker.ign
----

. Export the metadata file's `infraID` key as an environment variable:
+
[source,terminal]
----
$ export INFRA_ID=$(jq -r .infraID metadata.json)
----
+
[TIP]
Extract the `infraID` key from `metadata.json` and use it as a prefix for all of the {rh-openstack} resources that you create. By doing so, you avoid name conflicts when making multiple deployments in the same project.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-converting-ignition-resources_{context}"]
= Preparing the bootstrap Ignition files

The OpenShift Container Platform installation process relies on bootstrap machines that are created from a bootstrap Ignition configuration file.

Edit the file and upload it. Then, create a secondary bootstrap Ignition configuration file that
{rh-openstack-first} uses to download the primary file.

.Prerequisites

* You have the bootstrap Ignition file that the installer program generates, `bootstrap.ign`.
* The infrastructure ID from the installer's metadata file is set as an environment variable (`$INFRA_ID`).
** If the variable is not set, see *Creating the Kubernetes manifest and Ignition config files*.
* You have an HTTP(S)-accessible way to store the bootstrap Ignition file.
** The documented procedure uses the {rh-openstack} image service (Glance), but you can also use the {rh-openstack} storage service (Swift), Amazon S3, an internal HTTP server, or an ad hoc Nova server.

.Procedure

. Run the following Python script. The script modifies the bootstrap Ignition file to set the hostname and, if available, CA certificate file when it runs:
+
[source,python]
----
import base64
import json
import os

with open('bootstrap.ign', 'r') as f:
    ignition = json.load(f)

files = ignition['storage'].get('files', [])

infra_id = os.environ.get('INFRA_ID', 'openshift').encode()
hostname_b64 = base64.standard_b64encode(infra_id + b'-bootstrap\n').decode().strip()
files.append(
{
    'path': '/etc/hostname',
    'mode': 420,
    'contents': {
        'source': 'data:text/plain;charset=utf-8;base64,' + hostname_b64
    }
})

ca_cert_path = os.environ.get('OS_CACERT', '')
if ca_cert_path:
    with open(ca_cert_path, 'r') as f:
        ca_cert = f.read().encode()
        ca_cert_b64 = base64.standard_b64encode(ca_cert).decode().strip()

    files.append(
    {
        'path': '/opt/openshift/tls/cloud-ca-cert.pem',
        'mode': 420,
        'contents': {
            'source': 'data:text/plain;charset=utf-8;base64,' + ca_cert_b64
        }
    })

ignition['storage']['files'] = files;

with open('bootstrap.ign', 'w') as f:
    json.dump(ignition, f)
----

. Using the {rh-openstack} CLI, create an image that uses the bootstrap Ignition file:
+
[source,terminal]
----
$ openstack image create --disk-format=raw --container-format=bare --file bootstrap.ign <image_name>
----

. Get the image's details:
+
[source,terminal]
----
$ openstack image show <image_name>
----
+
Make a note of the `file` value; it follows the pattern `v2/images/<image_ID>/file`.
+
[NOTE]
Verify that the image you created is active.

. Retrieve the image service's public address:
+
[source,terminal]
----
$ openstack catalog show image
----

. Combine the public address with the image `file` value and save the result as the storage location. The location follows the pattern `<image_service_public_URL>/v2/images/<image_ID>/file`.

. Generate an auth token and save the token ID:
+
[source,terminal]
----
$ openstack token issue -c id -f value
----

. Insert the following content into a file called `$INFRA_ID-bootstrap-ignition.json` and edit the placeholders to match your own values:
+
[source,json]
----
{
  "ignition": {
    "config": {
      "merge": [{
        "source": "<storage_url>", <1>
        "httpHeaders": [{
          "name": "X-Auth-Token", <2>
          "value": "<token_ID>" <3>
        }]
      }]
    },
    "security": {
      "tls": {
        "certificateAuthorities": [{
          "source": "data:text/plain;charset=utf-8;base64,<base64_encoded_certificate>" <4>
        }]
      }
    },
    "version": "3.2.0"
  }
}
----
<1> Replace the value of `ignition.config.merge.source` with the bootstrap Ignition file storage URL.
<2> Set `name` in `httpHeaders` to `"X-Auth-Token"`.
<3> Set `value` in `httpHeaders` to your token's ID.
<4> If the bootstrap Ignition file server uses a self-signed certificate, include the base64-encoded certificate.

. Save the secondary Ignition config file.

The bootstrap Ignition data will be passed to {rh-openstack} during installation.

[WARNING]
The bootstrap Ignition file contains sensitive information, like `clouds.yaml` credentials. Ensure that you store it in a secure place, and delete it after you complete the installation process.

// . If you are using Swift:
// .. Using the Swift CLI, create a container:
// +
// ----
// $ swift post <container_name>
// ----
//
// .. Upload the bootstrap Ignition file to the container:
// +
// ----
// $ swift upload <container_name> bootstrap.ign
// ----
//
// .. Set the container to be read-accessible:
// +
// ----
// $ swift post <container_name> --read-acl ".r:*,.rlistings"
// ----
//
// .. Retrieve the storage URL:
// +
// ----
// $ swift stat -v
// ----
// ** The URL should follow this format: `<storage_URL>/<container_name>/bootstrap.ign`
// May need to bring this back.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-creating-control-plane-ignition_{context}"]
= Creating control plane Ignition config files on {rh-openstack}

Installing OpenShift Container Platform on {rh-openstack-first} on your own infrastructure requires control plane Ignition config files. You must create multiple config files.

[NOTE]
As with the bootstrap Ignition configuration, you must explicitly define a hostname for each control plane machine.

.Prerequisites

* The infrastructure ID from the installation program's metadata file is set as an environment variable (`$INFRA_ID`).
** If the variable is not set, see "Creating the Kubernetes manifest and Ignition config files".

.Procedure

* On a command line, run the following Python script:
+
[source,terminal]
----
$ for index in $(seq 0 2); do
    MASTER_HOSTNAME="$INFRA_ID-master-$index\n"
    python -c "import base64, json, sys;
ignition = json.load(sys.stdin);
storage = ignition.get('storage', {});
files = storage.get('files', []);
files.append({'path': '/etc/hostname', 'mode': 420, 'contents': {'source': 'data:text/plain;charset=utf-8;base64,' + base64.standard_b64encode(b'$MASTER_HOSTNAME').decode().strip(), 'verification': {}}, 'filesystem': 'root'});
storage['files'] = files;
ignition['storage'] = storage
json.dump(ignition, sys.stdout)" <master.ign >"$INFRA_ID-master-$index-ignition.json"
done
----
+
You now have three control plane Ignition files: `<INFRA_ID>-master-0-ignition.json`, `<INFRA_ID>-master-1-ignition.json`,
and `<INFRA_ID>-master-2-ignition.json`.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-updating-network-resources_{context}"]
= Updating network resources on {rh-openstack}

Update the network resources that an OpenShift Container Platform on {rh-openstack-first} installation on your own infrastructure requires.

.Prerequisites

* Python 3 is installed on your machine.
* You downloaded the modules in "Downloading playbook dependencies".
* You downloaded the playbooks in "Downloading the installation playbooks".

.Procedure

. Optional: Add an external network value to the `inventory.yaml` playbook:
+
.Example external network value in the `inventory.yaml` Ansible Playbook
[source,yaml]
----
...
      # The public network providing connectivity to the cluster. If not
      # provided, the cluster external connectivity must be provided in another
      # way.

      # Required for os_api_fip, os_ingress_fip, os_bootstrap_fip.
      os_external_network: 'external'
...
----
+
[IMPORTANT]
====
If you did not provide a value for `os_external_network` in the `inventory.yaml` file, you must ensure that VMs can access Glance and an external connection yourself.
====

. Optional: Add external network and floating IP (FIP) address values to the `inventory.yaml` playbook:
+
.Example FIP values in the `inventory.yaml` Ansible Playbook
[source,yaml]
----
...
      # OpenShift API floating IP address. If this value is non-empty, the
      # corresponding floating IP will be attached to the Control Plane to
      # serve the OpenShift API.
      os_api_fip: '203.0.113.23'

      # OpenShift Ingress floating IP address. If this value is non-empty, the
      # corresponding floating IP will be attached to the worker nodes to serve
      # the applications.
      os_ingress_fip: '203.0.113.19'

      # If this value is non-empty, the corresponding floating IP will be
      # attached to the bootstrap machine. This is needed for collecting logs
      # in case of install failure.
      os_bootstrap_fip: '203.0.113.20'
----
+
[IMPORTANT]
====
If you do not define values for `os_api_fip` and `os_ingress_fip`, you must perform postinstallation network configuration.

If you do not define a value for `os_bootstrap_fip`, the installation program cannot download debugging information from failed installations.

See "Enabling access to the environment" for more information.
====

. On a command line, create security groups by running the `security-groups.yaml` playbook:
+
[source,terminal]
----
$ ansible-playbook -i inventory.yaml security-groups.yaml
----

. On a command line, update the network resources by running the `update-network-resources.yaml` playbook:
+
[source,terminal]
----
$ ansible-playbook -i inventory.yaml update-network-resources.yaml <1>
----
<1> This playbook will add tags to the network, subnets, ports, and router. It also attaches floating IP addresses to the API and Ingress ports and sets the security groups for those ports.

. Optional: If you want to control the default resolvers that Nova servers use, run the {rh-openstack} CLI command:
+
[source,terminal]
----
$ openstack subnet set --dns-nameserver <server_1> --dns-nameserver <server_2> "$INFRA_ID-nodes"
----

. Optional: You can use the `inventory.yaml` file that you created to customize your installation. For example, you can deploy a cluster that uses bare metal machines.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-deploying-bare-metal-machines_{context}"]
= Deploying a cluster with bare metal machines

If you want your cluster to use bare metal machines, modify the
file. Your cluster can have compute machines running on bare metal.

[NOTE]
====
Be sure that your `install-config.yaml` file reflects whether the {rh-openstack} network that you use for bare metal workers supports floating IP addresses or not.
====

.Prerequisites

* The {rh-openstack} Bare Metal service (Ironic) is enabled and accessible via the {rh-openstack} Compute API.

* Bare metal is available as a {rh-openstack} flavor.

* If your cluster runs on an {rh-openstack} version that is more than 16.1.6 and less than 16.2.4, bare metal workers do not function due to a known issue that causes the metadata service to be unavailable for services on OpenShift Container Platform nodes.

* The {rh-openstack} network supports both VM and bare metal server attachment.

* If you want to deploy the machines on a pre-existing network, a {rh-openstack} subnet is provisioned.

* If you want to deploy the machines on an installer-provisioned network, the {rh-openstack} Bare Metal service (Ironic) is able to listen for and interact with Preboot eXecution Environment (PXE) boot machines that run on tenant networks.

* You created an `install-config.yaml` file as part of the OpenShift Container Platform installation process.

* You created an `inventory.yaml` file as part of the OpenShift Container Platform installation process.

.Procedure

. In the `install-config.yaml` file, edit the flavors for machines:
.. Change the value of `compute.platform.openstack.type` to a bare metal flavor.
.. If you want to deploy your machines on a pre-existing network, change the value of `platform.openstack.machinesSubnet` to the {rh-openstack} subnet UUID of the network.
+
.An example bare metal `install-config.yaml` file
[source,yaml]
----
compute:
  - architecture: amd64
    hyperthreading: Enabled
    name: worker
    platform:
      openstack:
        type: <bare_metal_compute_flavor> <1>
    replicas: 3
...

platform:
    openstack:
      machinesSubnet: <subnet_UUID> <2>
...
----
<1> Change this value to a bare metal flavor to use for compute machines.
<2> If you want to use a pre-existing network, change this value to the UUID of the {rh-openstack} subnet.

Use the updated `install-config.yaml` file to complete the installation process.
The compute machines that are created during deployment use the flavor that you
added to the file.

. In the `inventory.yaml` file, edit the flavors for machines:
.. Change the value of `os_flavor_worker` to a bare metal flavor.
+
.An example bare metal `inventory.yaml` file
[source,yaml]
----
all:
  hosts:
    localhost:
      ansible_connection: local
      ansible_python_interpreter: "{{ansible_playbook_python}}"

      # User-provided values
      os_subnet_range: '10.0.0.0/16'
      os_flavor_master: 'my-vm-flavor'
      os_flavor_worker: 'my-bare-metal-flavor' <1>
      os_image_rhcos: 'rhcos'
      os_external_network: 'external'
...
----
<1> Change this value to a bare metal flavor to use for compute machines.

Use the updated `inventory.yaml` file to complete the installation process.
Machines that are created during deployment use the flavor that you
added to the file.

[NOTE]
====
The installation program may time out while waiting for bare metal machines to boot.

If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:

[source,terminal]
----
$ ./openshift-install wait-for install-complete --log-level debug
----
====

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-creating-bootstrap-machine_{context}"]
= Creating the bootstrap machine on {rh-openstack}

Create a bootstrap machine and give it the network access it needs to run on {rh-openstack-first}. Red Hat provides an Ansible playbook that you run to simplify this process.

.Prerequisites
* You downloaded the modules in "Downloading playbook dependencies".
* You downloaded the playbooks in "Downloading the installation playbooks".
* The `inventory.yaml`, `common.yaml`, and `bootstrap.yaml` Ansible playbooks are in a common directory.
* The `metadata.json` file that the installation program created is in the same directory as the Ansible playbooks.

.Procedure

. On a command line, change the working directory to the location of the playbooks.

. On a command line, run the `bootstrap.yaml` playbook:
+
[source,terminal]
----
$ ansible-playbook -i inventory.yaml bootstrap.yaml
----

. After the bootstrap server is active, view the logs to verify that the Ignition files were received:
+
[source,terminal]
----
$ openstack console log show "$INFRA_ID-bootstrap"
----

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-creating-control-plane_{context}"]
= Creating the control plane machines on {rh-openstack}

Create three control plane machines by using the Ignition config files that you generated. Red Hat provides an Ansible playbook that you run to simplify this process.

.Prerequisites

* You downloaded the modules in "Downloading playbook dependencies".
* You downloaded the playbooks in "Downloading the installation playbooks".
* The infrastructure ID from the installation program's metadata file is set as an environment variable (`$INFRA_ID`).
* The `inventory.yaml`, `common.yaml`, and `control-plane.yaml` Ansible playbooks are in a common directory.
* You have the three Ignition files that were created in "Creating control plane Ignition config files".

.Procedure

. On a command line, change the working directory to the location of the playbooks.

. If the control plane Ignition config files are not already in your working directory, copy them into it.

. On a command line, run the `control-plane.yaml` playbook:
+
[source,terminal]
----
$ ansible-playbook -i inventory.yaml control-plane.yaml
----

. Run the following command to monitor the bootstrapping process:
+
[source,terminal]
----
$ openshift-install wait-for bootstrap-complete
----
+
You will see messages that confirm that the control plane machines are running and have joined the cluster:
+
[source,terminal]
----
INFO API v1.35.4 up
INFO Waiting up to 30m0s for bootstrapping to complete...
...
INFO It is now safe to remove the bootstrap resources
----

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

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-deleting-bootstrap-resources_{context}"]
= Deleting bootstrap resources from {rh-openstack}

Delete the bootstrap resources that you no longer need.

.Prerequisites
* You downloaded the modules in "Downloading playbook dependencies".
* You downloaded the playbooks in "Downloading the installation playbooks".
* The `inventory.yaml`, `common.yaml`, and `down-bootstrap.yaml` Ansible playbooks are in a common directory.
* The control plane machines are running.
** If you do not know the status of the machines, see "Verifying cluster status".

.Procedure

. On a command line, change the working directory to the location of the playbooks.

. On a command line, run the `down-bootstrap.yaml` playbook:
+
[source,terminal]
----
$ ansible-playbook -i inventory.yaml down-bootstrap.yaml
----

The bootstrap port, server, and floating IP address are deleted.

[WARNING]
If you did not disable the bootstrap Ignition file URL earlier, do so now.

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-creating-compute-machines_{context}"]
= Creating compute machines on {rh-openstack}

After standing up the control plane, create compute machines. Red Hat provides an Ansible playbook that you run to simplify this process.

.Prerequisites
* You downloaded the modules in "Downloading playbook dependencies".
* You downloaded the playbooks in "Downloading the installation playbooks".
* The `inventory.yaml`, `common.yaml`, and `compute-nodes.yaml` Ansible playbooks are in a common directory.
* The `metadata.json` file that the installation program created is in the same directory as the Ansible playbooks.
* The control plane is active.

.Procedure

. On a command line, change the working directory to the location of the playbooks.

. On a command line, run the playbook:
+
[source,terminal]
----
$ ansible-playbook -i inventory.yaml compute-nodes.yaml
----

.Next steps

* Approve the certificate signing requests for the machines.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-restricted-networks.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * machine_management/adding-rhel-compute.adoc
// * machine_management/more-rhel-compute.adoc
// * machine_management/user_provisioned/adding-aws-compute-user-infra.adoc
// * machine_management/user_provisioned/adding-bare-metal-compute-user-infra.adoc
// * machine_management/user_provisioned/adding-vsphere-compute-user-infra.adoc
// * post_installation_configuration/node-tasks.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-power.adoc

[id="installation-approve-csrs_{context}"]
= Approving the certificate signing requests for your machines

[role="_abstract"]
When you add machines to a cluster, two pending certificate signing requests (CSRs) are generated for each machine that you added. You must confirm that these CSRs are approved or, if necessary, approve them yourself. The client requests must be approved first, followed by the server requests.

.Prerequisites

* You added machines to your cluster.

.Procedure

. Confirm that the cluster recognizes the machines:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  63m  v1.35.4
master-1  Ready     master  63m  v1.35.4
master-2  Ready     master  64m  v1.35.4
----
+
The output lists all of the machines that you created.
+
[NOTE]
====
The preceding output might not include the compute nodes, also known as worker nodes, until some CSRs are approved.
====

. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:
+
[source,terminal]
----
$ oc get csr
----
+
.Example output
[source,terminal]
----
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
...
----
+
In this example, two machines are joining the cluster. You might see more approved CSRs in the list.
[source,terminal]
----
$ oc get csr
----
+
[source,terminal]
.Example output
----
NAME        AGE   REQUESTOR                                   CONDITION
csr-mddf5   20m   system:node:master-01.example.com   Approved,Issued
csr-z5rln   16m   system:node:worker-21.example.com   Approved,Issued
----

. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:
+
[NOTE]
====
You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates will rotate, and more than two certificates will be present for each node. You must approve all of these certificates. After the client CSR is approved, the Kubelet creates a secondary CSR for the serving certificate, which requires manual approval. Then, subsequent serving certificate renewal requests are automatically approved by the `machine-approver` if the Kubelet requests a new certificate with identical parameters.
====
+
[NOTE]
====
For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If a request is not approved, then the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because a serving certificate is required when the API server connects to the kubelet. Any operation that contacts the Kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the CSR was submitted by the `node-bootstrapper` service account in the `system:node` or `system:admin` groups, and confirm the identity of the node.
====
+
** To approve them individually, run the following command for each valid CSR:
+
[source,terminal]
----
$ oc adm certificate approve <csr_name>
----
+
where:
+
`<csr_name>`:: Specifies the name of a CSR from the list of current CSRs.
+
** To approve all pending CSRs, run the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
----
+
[NOTE]
====
Some Operators might not become available until some CSRs are approved.
Each node submits two CSRs, so you may need to run the command to approve CSRs multiple times.
====

. Now that your client requests are approved, you must review the server requests for each machine that you added to the cluster:
+
[source,terminal]
----
$ oc get csr
----
+
.Example output
[source,terminal]
----
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
...
----

. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:
+
** To approve them individually, run the following command for each valid CSR:
+
[source,terminal]
----
$ oc adm certificate approve <csr_name>
----
+
where:
+
`<csr_name>`:: Specifies the name of a CSR from the list of current CSRs.
+
** To approve all pending CSRs, run the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
----

. After all client and server CSRs have been approved, the machines have the `Ready` status. Verify this by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
[source,terminal]
----
$ oc get nodes -o wide
----
+
.Example output
[source,terminal]
----
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  73m  v1.35.4
master-1  Ready     master  73m  v1.35.4
master-2  Ready     master  74m  v1.35.4
worker-0  Ready     worker  11m  v1.35.4
worker-1  Ready     worker  11m  v1.35.4
----
.Example output
[source,terminal]
----
NAME               STATUS   ROLES                  AGE   VERSION   INTERNAL-IP      EXTERNAL-IP   OS-IMAGE                                                       KERNEL-VERSION                  CONTAINER-RUNTIME
worker-0-ppc64le   Ready    worker                 42d   v1.35.4   192.168.200.21   <none>        Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.ppc64le   cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-1-ppc64le   Ready    worker                 42d   v1.35.4   192.168.200.20   <none>        Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.ppc64le   cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-0-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.38      10.248.0.38   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-1-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.39      10.248.0.39   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-2-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.40      10.248.0.40   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-0-x86       Ready    worker                 75d   v1.35.4   10.248.0.43      10.248.0.43   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-1-x86       Ready    worker                 75d   v1.35.4   10.248.0.44      10.248.0.44   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
----
+
[NOTE]
====
It can take a few minutes after approval of the server CSRs for the machines to transition to the `Ready` status.
====

// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

[id="installation-osp-verifying-installation_{context}"]
= Verifying a successful installation

Verify that the OpenShift Container Platform installation is complete.

.Prerequisites

* You have the installation program (`openshift-install`)

.Procedure

* On a command line, enter:
+
[source,terminal]
----
$ openshift-install --log-level debug wait-for install-complete
----

The program outputs the console URL, as well as the administrator's login information.

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
* If you need to enable external access to node ports, configure ingress cluster traffic by using a node port.
* If you did not configure {rh-openstack} to accept application traffic over floating IP addresses, configure {rh-openstack} access with floating IP addresses.
