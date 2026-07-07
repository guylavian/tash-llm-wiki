---
title: "Installing OpenShift on a single node"
type: reference
domain: openshift
slug: installing-4-22-install-sno-installing-sno
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/install-sno-installing-sno
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing OpenShift on a single node

[id="install-sno-installing-sno"]
= Installing OpenShift on a single node

You can install {sno} by using either the web-based Assisted Installer or the `coreos-installer` tool to generate a discovery ISO image. The discovery ISO image writes the {op-system-first} system configuration to the target installation disk, so that you can run a single-cluster node to meet your needs.

Consider using {sno} when you want to run a cluster in a low-resource or an isolated environment for testing, troubleshooting, training, or small-scale project purposes.

[id="installing-sno-assisted-installer"]
== Installing {sno} using the Assisted Installer

To install OpenShift Container Platform on a single node, use the web-based Assisted Installer wizard to guide you through the process and manage the installation.

See the Assisted Installer for OpenShift Container Platform documentation for details and configuration options.

// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="install-sno-generating-the-discovery-iso-with-the-assisted-installer_{context}"]
= Generating the discovery ISO with the Assisted Installer

Installing OpenShift Container Platform on a single node requires a discovery ISO, which the Assisted Installer can generate.

.Procedure

. On the administration host, open a browser and navigate to {cluster-manager-first}.

. Click *Create New Cluster* to create a new cluster.

. In the *Cluster name* field, enter a name for the cluster.

. In the *Base domain* field, enter a base domain. For example:
+
----
example.com
----
+
All DNS records must be subdomains of this base domain and include the cluster name, for example:
+
----
<cluster_name>.example.com
----
+
[NOTE]
====
You cannot change the base domain or cluster name after cluster installation.
====

. Select *Install single node OpenShift (SNO)* and complete the rest of the wizard steps. Download the discovery ISO.

. Complete the remaining Assisted Installer wizard steps.
+
[IMPORTANT]
=====
Ensure that you take note of the discovery ISO URL for installing with virtual media.

If you enable {VirtProductName} during this process, you must have a second local storage device of at least 50GiB for your virtual machines.
=====

[role="_additional-resources"]
.Additional resources

* Persistent storage using logical volume manager storage
* What you can do with OpenShift Virtualization

// Installing single-node OpenShift with the Assisted Installer
// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="install-sno-installing-with-the-assisted-installer_{context}"]
= Installing {sno} with the Assisted Installer

Use the Assisted Installer to install the single-node cluster.

.Prerequisites

* Ensure that the boot drive order in the server BIOS settings defaults to booting the server from the target installation disk.

.Procedure

. Attach the discovery ISO image to the target host.

. Boot the server from the discovery ISO image. The discovery ISO image writes the system configuration to the target installation disk and automatically triggers a server restart.

. On the administration host, return to the browser. Wait for the host to appear in the list of discovered hosts. If necessary, reload the *Assisted Clusters* page and select the cluster name.

. Complete the install wizard steps. Add networking details, including a subnet from the available subnets. Add the SSH public key if necessary.

. Monitor the installation's progress. Watch the cluster events. After the installation process finishes writing the operating system image to the server's hard disk, the server restarts.

. Optional: Remove the discovery ISO image.
+
The server restarts several times automatically, deploying the control plane.

You can install {sno-okd} using the Assisted Service or you can generate an installation ISO using `openshift-installer`.

[id="installing-sno-assisted-installer"]
== Installing {sno-okd} using the Assisted Service

To install {sno-okd} with the Assisted Service, please refer to the following documentation:
* Install OKD using Assisted Service

[role="_additional-resources"]
.Additional resources

* Creating a bootable ISO image on a USB drive

* Booting from an HTTP-hosted ISO image using the Redfish API
* Adding worker nodes to {sno} clusters

* Adding worker nodes to {sno-okd} clusters

[id="install-sno-installing-sno-manually"]
== Installing {sno} manually
[id="install-sno-installing-sno-manually"]
== Installing {sno-okd} manually

To install OpenShift Container Platform on a single node, first generate the installation ISO, and then boot the server from the ISO. You can monitor the installation using the `openshift-install` installation program.

[role="_additional-resources"]
.Additional resources

* Networking requirements for user-provisioned infrastructure

* User-provisioned DNS requirements

* Configuring DHCP or static IP addresses

// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="generating-the-install-iso-manually_{context}"]
= Generating the installation ISO with coreos-installer

Installing OpenShift Container Platform on a single node requires an installation ISO, which you can generate with the following procedure.

.Prerequisites

* Install `podman`.

[NOTE]
====
See "Requirements for installing OpenShift on a single node" for networking requirements, including DNS records.
====

.Procedure

. Set the OpenShift Container Platform version:
+
[source,terminal]
----
$ export OCP_VERSION=<ocp_version> <1>
----
+
<1> Replace `<ocp_version>` with the current version, for example, `latest-`
. Set the OpenShift Container Platform version:
+
[source,terminal]
----
$ OKD_VERSION=<okd_version> <1>
----
+
<1> Replace `<okd_version>` with the current version, for example, `4.14.0-0.okd-2024-01-26-175629`

. Set the target cluster architecture:
+
[source,terminal]
----
$ export ARCH=<architecture> <1>
----
<1> Replace `<architecture>` with the target host architecture, for example, `aarch64` or `x86_64`.

. Set the installation host architecture:
+
[source,terminal]
----
$ export HOST_ARCH=$(uname -m)
----
+
This command detects the architecture of the installation host. If the installation host architecture differs from the target cluster architecture, the downloaded binaries must match the installation host. For example, if you are installing an `aarch64` cluster from an `x86_64` bastion host, `HOST_ARCH` is `x86_64`.

. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/$HOST_ARCH/clients/ocp/$OCP_VERSION/openshift-client-linux.tar.gz -o oc.tar.gz
----
+
[source,terminal]
----
$ tar zxf oc.tar.gz
----
+
[source,terminal]
----
$ chmod +x oc
----
. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -L https://github.com/okd-project/okd/releases/download/$OKD_VERSION/openshift-client-linux-$OKD_VERSION.tar.gz -o oc.tar.gz
----
+
[source,terminal]
----
$ tar zxf oc.tar.gz
----
+
[source,terminal]
----
$ chmod +x oc
----

. Download the OpenShift Container Platform installer and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/$HOST_ARCH/clients/ocp/$OCP_VERSION/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
----
. Download the OpenShift Container Platform installer and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -L https://github.com/okd-project/okd/releases/download/$OKD_VERSION/openshift-install-linux-$OKD_VERSION.tar.gz -o openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ tar zxvf openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ chmod +x openshift-install
----

. Retrieve the {op-system} ISO URL by running the following command:
+
[source,terminal]
----
$ export ISO_URL=$(./openshift-install coreos print-stream-json | grep location | grep $ARCH | grep iso | cut -d\" -f4)
----

. Download the {op-system} ISO:
+
[source,terminal]
----
$ curl -L $ISO_URL -o rhcos-live.iso
----
. Download the {op-system} ISO:
+
[source,terminal]
----
$ curl -L $ISO_URL -o fcos-live.iso
----

. Prepare the `install-config.yaml` file:
+
[source,yaml]
----
apiVersion: v1
baseDomain: <domain> <1>
compute:
- name: worker
  replicas: 0 <2>
controlPlane:
  name: master
  replicas: 1 <3>
metadata:
  name: <name> <4>
networking: <5>
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16 <6>
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
bootstrapInPlace:
  installationDisk: /dev/disk/by-id/<disk_id> <7>
pullSecret: '<pull_secret>' <8>
sshKey: |
  <ssh_key> <9>
----
<1> Add the cluster domain name.
<2> Set the `compute` replicas to `0`. This makes the control plane node schedulable.
<3> Set the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.
<4> Set the `metadata` name to the cluster name.
<5> Set the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.
<6> Set the `cidr` value to match the subnet of the {sno} cluster.
<6> Set the `cidr` value to match the subnet of the {sno-okd} cluster.
<7> Set the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.
<8> Copy the {cluster-manager-url-pull} and add the contents to this configuration setting.
<9> Add the public SSH key from the administration host so that you can log in to the cluster after installation.

. Generate OpenShift Container Platform assets by running the following commands:
+
[source,terminal]
----
$ mkdir ocp
----
+
[source,terminal]
----
$ cp install-config.yaml ocp
----
+
[source,terminal]
----
$ ./openshift-install --dir=ocp create single-node-ignition-config
----
+
. Embed the ignition data into the {op-system} ISO by running the following commands:
+
[source,terminal]
----
$ alias coreos-installer='podman run --privileged --pull always --rm \
        -v /dev:/dev -v /run/udev:/run/udev -v $PWD:/data \
        -w /data quay.io/coreos/coreos-installer:release'
----
+
[source,terminal]
----
$ coreos-installer iso ignition embed -fi ocp/bootstrap-in-place-for-live-iso.ign rhcos-live.iso
----
+
[IMPORTANT]
====
The SSL certificates for the {op-system} ISO installation image are only valid for 24 hours. If you use the ISO image to install a node more than 24 hours after creating the image, the installation can fail. To re-create the image after 24 hours, delete the `ocp` directory and re-create the OpenShift Container Platform assets.
====
. Generate OpenShift Container Platform assets by running the following commands:
+
[source,terminal]
----
$ mkdir sno
----
+
[source,terminal]
----
$ cp install-config.yaml sno
----
+
[source,terminal]
----
$ ./openshift-install --dir=sno create single-node-ignition-config
----

. Embed the ignition data into the {op-system} ISO by running the following commands:
+
[source,terminal]
----
$ alias coreos-installer='podman run --privileged --pull always --rm \
        -v /dev:/dev -v /run/udev:/run/udev -v $PWD:/data \
        -w /data quay.io/coreos/coreos-installer:release'
----
+
[source,terminal]
----
$ coreos-installer iso ignition embed -fi sno/bootstrap-in-place-for-live-iso.ign fcos-live.iso
----

[role="_additional-resources"]
.Additional resources

* See Requirements for installing OpenShift on a single node for more information about installing OpenShift Container Platform on a single node.
* See Cluster capabilities for more information about enabling cluster capabilities that were disabled before installation.
* See Optional cluster capabilities in OpenShift Container Platform  for more information about the features provided by each capability.

// Monitoring the cluster installation using openshift-install
// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="install-sno-monitoring-the-installation-manually_{context}"]
= Monitoring the cluster installation using openshift-install

Use `openshift-install` to monitor the progress of the single-node cluster installation.

.Prerequisites

* Ensure that the boot drive order in the server BIOS settings defaults to booting the server from the target installation disk.

.Procedure

. Attach the discovery ISO image to the target host.

. Boot the server from the discovery ISO image. The discovery ISO image writes the system configuration to the target installation disk and automatically triggers a server restart.

. On the administration host, monitor the installation by running the following command:
+
[source,terminal]
----
$ ./openshift-install --dir=ocp wait-for install-complete
----
+
[source,terminal]
----
$ ./openshift-install --dir=sno wait-for install-complete
----

. Optional: Remove the discovery ISO image.
+
The server restarts several times while deploying the control plane.

.Verification

* After the installation is complete, check the environment by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=ocp/auth/kubeconfig
----
+
[source,terminal]
----
$ export KUBECONFIG=sno/auth/kubeconfig
----
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                         STATUS   ROLES           AGE     VERSION
control-plane.example.com    Ready    master,worker   10m     v1.35.4
----
[source,terminal]
----
NAME                         STATUS   ROLES           AGE     VERSION
control-plane.example.com    Ready    master,worker   10m     v1.27.9+e36e183
----

[role="_additional-resources"]
.Additional resources

* Creating a bootable ISO image on a USB drive
* Booting from an HTTP-hosted ISO image using the Redfish API
* Adding worker nodes to {sno} clusters

[id="install-sno-installing-sno-with-agent-based-installer"]
== Installing {sno} with the Agent-based Installer

You can use the Agent-based Installer to deploy {sno} on bare-metal servers running ARM (`aarch64`) architecture. The Agent-based Installer generates a self-contained bootable ISO image by using the OpenShift Container Platform installer for offline and automated deployments.

The following procedure describes how to create the required configuration files, generate the agent ISO image, and boot the target ARM server to install {sno}.

[role="_additional-resources"]
.Additional resources

* Preparing to install with the Agent-based Installer

// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="install-sno-installing-with-agent-based-installer_{context}"]
= Installing {sno} with the Agent-based Installer on ARM architecture

[role="_abstract"]
You can use the Agent-based Installer to install {sno} on an `aarch64` (ARM) server. The Agent-based Installer generates a bootable ISO image that you use to boot the target machine and deploy the cluster.

.Prerequisites

* You downloaded the `openshift-install` binary for your installation host architecture from the {hybrid-console-url}. When you select the architecture on the console, ensure that it matches your installation host and that you select `ARM64` (`aarch64`) as the target cluster architecture.
* You have a valid pull secret from the {hybrid-console-url}.
* You have an SSH public key on the administration host.
* You configured DNS records for `api.<cluster_name>.<base_domain>` and `*.apps.<cluster_name>.<base_domain>` to point to the node IP address.

[NOTE]
====
See "Requirements for installing OpenShift on a single node" for networking requirements, including DNS records.
====

.Procedure

. Create a directory to store the installation configuration by running the following command:
+
[source,terminal]
----
$ mkdir ~/<install_directory>
----

. Create the `install-config.yaml` file in the installation directory as in the following example:
+
[source,yaml]
----
apiVersion: v1
baseDomain: <domain>
compute:
- architecture: arm64
  hyperthreading: Enabled
  name: worker
  replicas: 0
controlPlane:
  architecture: arm64
  hyperthreading: Enabled
  name: master
  replicas: 1
metadata:
  name: <cluster_name>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: <machine_network_cidr>
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
pullSecret: '<pull_secret>'
sshKey: '<ssh_pub_key>'
----
+
The following table describes the required parameters:
+
.Required `install-config.yaml` parameters
[cols="2,3",options="header"]
|===
|Parameter |Description

|`baseDomain`
|Specify the cluster base domain name.

|`compute[].architecture`
|Set to `arm64` for ARM-based deployments. Must match the `controlPlane` architecture.

|`compute[].replicas`
|Set to `0` to make the control plane node schedulable.

|`controlPlane.architecture`
|Set to `arm64` for ARM-based deployments. Must match the `compute` architecture.

|`controlPlane.replicas`
|Set to `1` to ensure the cluster runs on a single node.

|`metadata.name`
|Specify the cluster name.

|`machineNetwork[].cidr`
|Set the CIDR value to match the subnet of the {sno} cluster.

|`networkType`
|Set to `OVNKubernetes`. This is the only supported network plugin for single-node clusters.

|`pullSecret`
|Copy the {cluster-manager-url-pull} and add the contents to this configuration setting.

|`sshKey`
|Provide the public SSH key from the administration host so that you can log in to the cluster after installation.
|===

. Create the `agent-config.yaml` file in the same installation directory as in the following example:
+
[source,yaml]
----
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: <cluster_name>
rendezvousIP: <node_ip>
----
+
Replace `<cluster_name>` with the cluster name. This value must match the `metadata.name` value in `install-config.yaml`. Replace `<node_ip>` with the IP address of the node. For {sno}, this is the IP address of the single node.

. Generate the agent ISO image by running the following command:
+
[source,terminal]
----
$ openshift-install --dir ~/<install_directory> agent create image
----
+
The command creates the `agent.aarch64.iso` image in the installation directory.

. Transfer the `agent.aarch64.iso` image to the target ARM server and boot from it. You can use one of the following methods:
+
--
* Attach the ISO image by using a virtual media interface such as Redfish or a BMC console.
* Write the ISO image to a USB drive and boot from it.
* Host the ISO image on an HTTP server and boot from it by using the Redfish API.
--
+
The ISO image writes the system configuration to the target installation disk and installs OpenShift Container Platform.

. Monitor the installation progress from the administration host by running the following command:
+
[source,terminal]
----
$ openshift-install --dir ~/<install_directory> agent wait-for install-complete --log-level=info
----
+
.Example output
[source,terminal]
----
...................................................................
INFO Cluster is installed
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run
INFO     export KUBECONFIG=~/<install_directory>/auth/kubeconfig
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.<cluster_name>.<domain>
----

.Verification

* After the installation is complete, verify the cluster by running the following commands:
+
[source,terminal]
----
$ export KUBECONFIG=~/<install_directory>/auth/kubeconfig
----
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                    STATUS   ROLES                         AGE     VERSION
<node_name>             Ready    control-plane,master,worker   10m     v1.34.2
----

[id="install-sno-installing-sno-on-cloud-providers"]
== Installing {sno} on cloud providers

* Adding worker nodes to {sno-okd} clusters

[id="install-sno-installing-sno-on-cloud-providers"]
== Installing {sno-okd} on cloud providers

// This module is included in the following assemblies:
//
// installing/installing_sno/install-sno-preparing-to-install-sno.adoc

[id="additional-requirements-for-installing-sno-on-a-cloud-provider_{context}"]
= Additional requirements for installing {sno} on a cloud provider

The documentation for installer-provisioned installation on cloud providers is based on a high availability cluster consisting of three control plane nodes. When referring to the documentation, consider the differences between the requirements for a {sno} cluster and a high availability cluster.

* A high availability cluster requires a temporary bootstrap machine, three control plane machines, and at least two compute machines. For a {sno} cluster, you need only a temporary bootstrap machine and one cloud instance for the control plane node and no compute nodes.

* The minimum resource requirements for high availability cluster installation include a control plane node with 4 vCPUs and 100GB of storage. For a {sno} cluster, you must have a minimum of 4 vCPUs and 120GB of storage.
+
[IMPORTANT]
====
Running {sno} on 4 vCPUs leaves very little "headroom" for user applications, and creates a high risk of resource contention and performance degradation.

To ensure cluster stability at this threshold, you must take steps to minimize the total resource footprint of the cluster, such as limiting the amount of workloads running on the cluster or limiting cluster capabilities.
For more information, see "Cluster capabilities".

Otherwise, it is recommended to provide more compute resources to the cluster.
====
= Additional requirements for installing {sno-okd} on a cloud provider

The documentation for installer-provisioned installation on cloud providers is based on a high availability cluster consisting of three control plane nodes. When referring to the documentation, consider the differences between the requirements for a {sno-okd} cluster and a high availability cluster.

* A high availability cluster requires a temporary bootstrap machine, three control plane machines, and at least two compute machines. For a {sno-okd} cluster, you need only a temporary bootstrap machine and one cloud instance for the control plane node and no worker nodes.

* The minimum resource requirements for high availability cluster installation include a control plane node with 4 vCPUs and 100GB of storage. For a {sno-okd} cluster, you must have a minimum of 4 vCPU cores and 120GB of storage.
+
[IMPORTANT]
====
Running {sno-okd} on 4 vCPUs leaves very little "headroom" for user applications, and creates a high risk of resource contention and performance degradation.

To ensure cluster stability at this threshold, you must take steps to minimize the total resource footprint of the cluster, such as limiting the amount of workloads running on the cluster or limiting cluster capabilities.
For more information, see "Cluster capabilities".

Otherwise, it is recommended to provide more compute resources to the cluster.
====

* The `controlPlane.replicas` setting in the `install-config.yaml` file should be set to `1`.

* The `compute.replicas` setting in the `install-config.yaml` file should be set to `0`.
This makes the control plane node schedulable.

[role="_additional-resources"]
.Additional resources

* Cluster capabilities

// This module is included in the following assemblies:
//
// installing/installing_sno/install-sno-installing-sno.adoc

[id="supported-cloud-providers-for-single-node-openshift_{context}"]
= Supported cloud providers for {sno}

= Supported cloud providers for {sno-okd}

The following table contains a list of supported cloud providers and CPU architectures.

.Supported cloud providers
[options="header"]
|====
|Cloud provider |CPU architecture
|Amazon Web Service (AWS)|x86_64 and AArch64
|Microsoft Azure|x86_64
|{gcp-first} | x86_64 and AArch64
|====

// This module is included in the following assemblies:
//
// installing/installing_sno/install-sno-installing-sno.adoc

[id="installing-sno-on-aws_{context}"]
= Installing {sno} on AWS

Installing a single-node cluster on AWS requires installer-provisioned installation using the "Installing a cluster on AWS with customizations" procedure.

[role="_additional-resources"]

.Additional resources

* Installing a cluster on AWS with customizations

// This module is included in the following assemblies:
//
// installing/installing_sno/install-sno-installing-sno.adoc

[id="installing-sno-on-azure_{context}"]
= Installing {sno} on Azure

= Installing {sno-okd} on Azure

Installing a single node cluster on Azure requires installer-provisioned installation using the "Installing a cluster on Azure with customizations" procedure.

[role="_additional-resources"]
.Additional resources

* Installing a cluster on Azure with customizations

// This module is included in the following assemblies:
//
// installing/installing_sno/install-sno-installing-sno.adoc

[id="installing-sno-on-gcp_{context}"]
= Installing {sno} on {gcp-short}

= Installing {sno-okd} on {gcp-short}

Installing a single node cluster on {gcp-short} requires installer-provisioned installation using the "Installing a cluster on {gcp-short} with customizations" procedure.

[role="_additional-resources"]
.Additional resources

* Installing a cluster on {gcp-short} with customizations

// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="installing-with-usb-media_{context}"]
= Creating a bootable ISO image on a USB drive

You can install software using a bootable USB drive that contains an ISO image. Booting the server with the USB drive prepares the server for the software installation.

.Procedure

. On the administration host, insert a USB drive into a USB port.

. Create a bootable USB drive, for example:
+
[source,terminal]
----
# dd if=<path_to_iso> of=<path_to_usb> status=progress
----
+
where:
+
--
<path_to_iso>:: is the relative path to the downloaded ISO file, for example, `rhcos-live.iso`.
<path_to_usb>:: is the location of the connected USB drive, for example, `/dev/sdb`.
--
+
--
<path_to_iso>:: is the relative path to the downloaded ISO file, for example, `fcos-live.iso`.
<path_to_usb>:: is the location of the connected USB drive, for example, `/dev/sdb`.
--
+
After the ISO is copied to the USB drive, you can use the USB drive to install software on the server.

// Module included in the following assemblies:
//
// * installing/installing_sno/install-sno-installing-sno.adoc

[id="install-booting-from-an-iso-over-http-redfish_{context}"]
= Booting from an HTTP-hosted ISO image using the Redfish API

You can provision hosts in your network using ISOs that you install using the Redfish Baseboard Management Controller (BMC) API.

[NOTE]
====
This example procedure demonstrates the steps on a Dell server.
====

[IMPORTANT]
====
Ensure that you have the latest firmware version of iDRAC that is compatible with your hardware. If you have any issues with the hardware or firmware, you must contact the provider.
====

.Prerequisites

* Download the installation {op-system-first} ISO.
* Use a Dell PowerEdge server that is compatible with iDRAC9.

.Procedure

. Copy the ISO file to an HTTP server accessible in your network.

. Boot the host from the hosted ISO file, for example:

.. Call the Redfish API to set the hosted ISO as the `VirtualMedia` boot media by running the following command:
+
[source,terminal]
----
$ curl -k -u <bmc_username>:<bmc_password> -d '{"Image":"<hosted_iso_file>", "Inserted": true}' -H "Content-Type: application/json" -X POST <host_bmc_address>/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD/Actions/VirtualMedia.InsertMedia
----
+
Where:
+
--
<bmc_username>:<bmc_password>:: Is the username and password for the target host BMC.
<hosted_iso_file>:: Is the URL for the hosted installation ISO, for example: `http://webserver.example.com/rhcos-live-minimal.iso`. The ISO must be accessible from the target host machine.
<host_bmc_address>:: Is the BMC IP address of the target host machine.
--

.. Set the host to boot from the `VirtualMedia` device by running the following command:
+
[source,terminal]
----
$ curl -k -u <bmc_username>:<bmc_password> -X PATCH -H 'Content-Type: application/json' -d '{"Boot": {"BootSourceOverrideTarget": "Cd", "BootSourceOverrideMode": "UEFI", "BootSourceOverrideEnabled": "Once"}}' <host_bmc_address>/redfish/v1/Systems/System.Embedded.1
----

.. Reboot the host:
+
[source,terminal]
----
$ curl -k -u <bmc_username>:<bmc_password> -d '{"ResetType": "ForceRestart"}' -H 'Content-type: application/json' -X POST <host_bmc_address>/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset
----

.. Optional: If the host is powered off, you can boot it using the `{"ResetType": "On"}` switch. Run the following command:
+
[source,terminal]
----
$ curl -k -u <bmc_username>:<bmc_password> -d '{"ResetType": "On"}' -H 'Content-type: application/json' -X POST <host_bmc_address>/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset
----

// Module included in the following assemblies:
//
// * installing/installing_sno/install-sno-installing-sno.adoc

[id="create-custom-live-rhcos-iso_{context}"]
= Creating a custom live {op-system} ISO for remote server access

In some cases, you cannot attach an external disk drive to a server, however, you need to access the server remotely to provision a node.
It is recommended to enable SSH access to the server.
You can create a live {op-system} ISO with SSHd enabled and with predefined credentials so that you can access the server after it boots.

.Prerequisites

* You installed the `butane` utility.

.Procedure

. Download the `coreos-installer` binary from the `coreos-installer` image mirror page.

. Download the latest live {op-system} ISO from mirror.openshift.com.

. Create the `embedded.yaml` file that the `butane` utility uses to create the Ignition file:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: sshd
  labels:
    machineconfiguration.openshift.io/role: worker
passwd:
  users:
    - name: core <1>
      ssh_authorized_keys:
        - '<ssh_key>'
----
<1> The `core` user has sudo privileges.

. Run the `butane` utility to create the Ignition file using the following command:
+
[source,terminal]
----
$ butane -pr embedded.yaml -o embedded.ign
----

. After the Ignition file is created, you can include the configuration in a new live {op-system} ISO, which is named `rhcos-sshd-.0-x86_64-live.x86_64.iso`, with the `coreos-installer` utility:
+
[source,terminal,subs="attributes+"]
----
$ coreos-installer iso ignition embed -i embedded.ign rhcos-.0-x86_64-live.x86_64.iso -o rhcos-sshd-.0-x86_64-live.x86_64.iso
----

.Verification

* Check that the custom live ISO can be used to boot the server by running the following command:
+
[source,terminal,subs="attributes+"]
----
# coreos-installer iso ignition show rhcos-sshd-.0-x86_64-live.x86_64.iso
----

+
.Example output
[source,json]
----
{
  "ignition": {
    "version": "3.2.0"
  },
  "passwd": {
    "users": [
      {
        "name": "core",
        "sshAuthorizedKeys": [
          "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZnG8AIzlDAhpyENpK2qKiTT8EbRWOrz7NXjRzopbPu215mocaJgjjwJjh1cYhgPhpAp6M/ttTk7I4OI7g4588Apx4bwJep6oWTU35LkY8ZxkGVPAJL8kVlTdKQviDv3XX12l4QfnDom4tm4gVbRH0gNT1wzhnLP+LKYm2Ohr9D7p9NBnAdro6k++XWgkDeijLRUTwdEyWunIdW1f8G0Mg8Y1Xzr13BUo3+8aey7HLKJMDtobkz/C8ESYA/f7HJc5FxF0XbapWWovSSDJrr9OmlL9f4TfE+cQk3s+eoKiz2bgNPRgEEwihVbGsCN4grA+RzLCAOpec+2dTJrQvFqsD alosadag@sonnelicht.local"
        ]
      }
    ]
  }
}
----

[id="install-sno-with-ibm-z"]
== Installing {sno} with {ibm-z-title} and {ibm-linuxone-title}

Installing a single-node cluster on {ibm-z-name} and {ibm-linuxone-name} requires user-provisioned installation using one of the following procedures:

* Installing a cluster with z/VM on {ibm-z-name} and {ibm-linuxone-name}
* Installing a cluster with {op-system-base} KVM on {ibm-z-name} and {ibm-linuxone-name}
* Installing a cluster in an LPAR on {ibm-z-name} and {ibm-linuxone-name}

[NOTE]
====
Installing a single-node cluster on {ibm-z-name} simplifies installation for development and test environments and requires less resource requirements at entry level.
====

=== Hardware requirements

* The equivalent of two Integrated Facilities for Linux (IFL), which are SMT2 enabled, for each cluster.
* At least one network connection to both connect to the `LoadBalancer` service and to serve data for traffic outside the cluster.

[NOTE]
====
You can use dedicated or shared IFLs to assign sufficient compute resources. Resource sharing is one of the key strengths of {ibm-z-name}. However, you must adjust capacity correctly on each hypervisor layer and ensure sufficient resources for every OpenShift Container Platform cluster.
====

// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="installing-sno-on-ibm-z_{context}"]
= Installing {sno} with z/VM on {ibm-z-title} and {ibm-linuxone-title}

.Prerequisites

* You have installed `podman`.

.Procedure

. Set the OpenShift Container Platform version by running the following command:
+
[source,terminal]
----
$ OCP_VERSION=<ocp_version> <1>
----
+
<1> Replace `<ocp_version>` with the current version. For example, `latest-`.

. Set the host architecture by running the following command:
+
[source,terminal]
----
$ ARCH=<architecture> <1>
----
<1> Replace `<architecture>` with the target host architecture `s390x`.

. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
----
+
[source,terminal]
----
$ tar zxf oc.tar.gz
----
+
[source,terminal]
----
$ chmod +x oc
----

. Download the OpenShift Container Platform installer and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ tar zxvf openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ chmod +x openshift-install
----

. Prepare the `install-config.yaml` file:
+
[source,yaml]
----
apiVersion: v1
baseDomain: <domain> <1>
compute:
- name: worker
  replicas: 0 <2>
controlPlane:
  name: master
  replicas: 1 <3>
metadata:
  name: <name> <4>
networking: <5>
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16 <6>
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
bootstrapInPlace:
  installationDisk: /dev/disk/by-id/<disk_id> <7>
pullSecret: '<pull_secret>' <8>
sshKey: |
  <ssh_key> <9>
----
<1> Add the cluster domain name.
<2> Set the `compute` replicas to `0`. This makes the control plane node schedulable.
<3> Set the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.
<4> Set the `metadata` name to the cluster name.
<5> Set the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.
<6> Set the `cidr` value to match the subnet of the {sno} cluster.
<7> Set the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.
<8> Copy the {cluster-manager-url-pull} and add the contents to this configuration setting.
<9> Add the public SSH key from the administration host so that you can log in to the cluster after installation.

. Generate OpenShift Container Platform assets by running the following commands:
+
[source,terminal]
----
$ mkdir ocp
----
+
[source,terminal]
----
$ cp install-config.yaml ocp
----
+
[source,terminal]
----
$ ./openshift-install --dir=ocp create single-node-ignition-config
----

. Obtain the {op-system-base} `kernel`, `initramfs`, and `rootfs`  artifacts from the Product Downloads page on the Red Hat Customer Portal or from the {op-system} image mirror page.
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure.
====
+
The file names contain the OpenShift Container Platform version number. They resemble the following examples:
+
`kernel`:: `rhcos-<version>-live-kernel-<architecture>`
`initramfs`:: `rhcos-<version>-live-initramfs.<architecture>.img`
`rootfs`:: `rhcos-<version>-live-rootfs.<architecture>.img`
+
[NOTE]
====
The `rootfs` image is the same for FCP and DASD.
====

. Move the following artifacts and files to an HTTP or HTTPS server:

** Downloaded {op-system-base} live `kernel`, `initramfs`, and `rootfs` artifacts
** Ignition files

. Create parameter files for a particular virtual machine:
+
.Example parameter file
+
[source,terminal]
----
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
ignition.firstboot ignition.platform.id=metal \
ignition.config.url=http://<http_server>:8080/ignition/bootstrap-in-place-for-live-iso.ign \// <1>
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \// <2>
ip=<ip>::<gateway>:<mask>:<hostname>::none nameserver=<dns> \// <3>
rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
rd.dasd=0.0.4411 \// <4>
rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \// <5>
zfcp.allow_lun_scan=0
----
<1> For the `ignition.config.url=` parameter, specify the Ignition file for the machine role. Only HTTP and HTTPS protocols are supported.
<2> For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `kernel`and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported.
<3> For the `ip=` parameter, assign the IP address automatically using DHCP or manually as described in "Installing a cluster with z/VM on {ibm-z-name} and {ibm-linuxone-name}".
<4> For installations on DASD-type disks, use `rd.dasd=` to specify the DASD where {op-system} is to be installed. Omit this entry for FCP-type disks.
<5> For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where {op-system} is to be installed. Omit this entry for DASD-type disks.
+
Leave all other parameters unchanged.

. Transfer the following artifacts, files, and images to z/VM. For example by using FTP:

** `kernel` and `initramfs` artifacts
** Parameter files
** {op-system} images
+
For details about how to transfer the files with FTP and boot from the virtual reader, see Installing under Z/VM.

. Punch the files to the virtual reader of the z/VM guest virtual machine that is to become your bootstrap node.

. Log in to CMS on the bootstrap machine.

. IPL the bootstrap machine from the reader by running the following command:
+
----
$ cp ipl c
----

. After the first reboot of the virtual machine, run the following commands directly after one another:

.. To boot a DASD device after first reboot, run the following commands:
+
--
[source,terminal]
----
$ cp i <devno> clear loadparm prompt
----

where:

`<devno>`:: Specifies the device number of the boot device as seen by the guest.

[source,terminal]
----
$ cp vi vmsg 0 <kernel_parameters>
----

where:

`<kernel_parameters>`:: Specifies a set of kernel parameters to be stored as system control program data (SCPDATA). When booting Linux, these kernel parameters are concatenated to the end of the existing kernel parameters that are used by your boot configuration. The combined parameter string must not exceed 896 characters.
--
.. To boot an FCP device after first reboot, run the following commands:
+
--
[source,terminal]
----
$ cp set loaddev portname <wwpn> lun <lun>
----

where:

`<wwpn>`:: Specifies the target port and `<lun>` the logical unit in hexadecimal format.

[source,terminal]
----
$ cp set loaddev bootprog <n>
----

where:

`<n>`:: Specifies the kernel to be booted.

[source,terminal]
----
$ cp set loaddev scpdata {APPEND|NEW} '<kernel_parameters>'
----

where:

`<kernel_parameters>`:: Specifies a set of kernel parameters to be stored as system control program data (SCPDATA). When booting Linux, these kernel parameters are concatenated to the end of the existing kernel parameters that are used by your boot configuration. The combined parameter string must not exceed 896 characters.

`<APPEND|NEW>`:: Optional: Specify `APPEND` to append kernel parameters to existing SCPDATA. This is the default. Specify `NEW` to replace existing SCPDATA.

.Example
[source,terminal]
----
$ cp set loaddev scpdata 'rd.zfcp=0.0.8001,0x500507630a0350a4,0x4000409D00000000
ip=encbdd0:dhcp::02:00:00:02:34:02 rd.neednet=1'
----

To start the IPL and boot process, run the following command:

[source,terminal]
----
$ cp i <devno>
----

where:

`<devno>`:: Specifies the device number of the boot device as seen by the guest.
--

// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="installing-sno-on-ibm-z-kvm_{context}"]
= Installing {sno} with {op-system-base} KVM on {ibm-z-title} and {ibm-linuxone-title}

.Prerequisites

* You  have installed `podman`.

.Procedure

. Set the OpenShift Container Platform version by running the following command:
+
[source,terminal]
----
$ OCP_VERSION=<ocp_version> <1>
----
+
<1> Replace `<ocp_version>` with the current version. For example, `latest-`.

. Set the host architecture by running the following command:
+
[source,terminal]
----
$ ARCH=<architecture> <1>
----
<1> Replace `<architecture>` with the target host architecture `s390x`.

. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
----
+
[source,terminal]
----
$ tar zxf oc.tar.gz
----
+
[source,terminal]
----
$ chmod +x oc
----

. Download the OpenShift Container Platform installer and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ tar zxvf openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ chmod +x openshift-install
----

. Prepare the `install-config.yaml` file:
+
[source,yaml]
----
apiVersion: v1
baseDomain: <domain> <1>
compute:
- name: worker
  replicas: 0 <2>
controlPlane:
  name: master
  replicas: 1 <3>
metadata:
  name: <name> <4>
networking: <5>
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16 <6>
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
bootstrapInPlace:
  installationDisk: /dev/disk/by-id/<disk_id> <7>
pullSecret: '<pull_secret>' <8>
sshKey: |
  <ssh_key> <9>
----
<1> Add the cluster domain name.
<2> Set the `compute` replicas to `0`. This makes the control plane node schedulable.
<3> Set the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.
<4> Set the `metadata` name to the cluster name.
<5> Set the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.
<6> Set the `cidr` value to match the subnet of the {sno} cluster.
<7> Set the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.
<8> Copy the {cluster-manager-url-pull} and add the contents to this configuration setting.
<9> Add the public SSH key from the administration host so that you can log in to the cluster after installation.

. Generate OpenShift Container Platform assets by running the following commands:
+
[source,terminal]
----
$ mkdir ocp
----
+
[source,terminal]
----
$ cp install-config.yaml ocp
----
+
[source,terminal]
----
$ ./openshift-install --dir=ocp create single-node-ignition-config
----

. Obtain the {op-system-base} `kernel`, `initramfs`, and `rootfs` artifacts from the Product Downloads page on the Red Hat Customer Portal or from the {op-system} image mirror page.
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure.
====
+
The file names contain the OpenShift Container Platform version number. They resemble the following examples:
+
`kernel`:: `rhcos-<version>-live-kernel-<architecture>`
`initramfs`:: `rhcos-<version>-live-initramfs.<architecture>.img`
`rootfs`:: `rhcos-<version>-live-rootfs.<architecture>.img`
+
. Before you launch `virt-install`, move the following files and artifacts to an HTTP or HTTPS server:

** Downloaded {op-system-base} live `kernel`, `initramfs`, and `rootfs` artifacts
** Ignition files

. Create the KVM guest nodes by using the following components:

** {op-system-base} `kernel` and `initramfs` artifacts
** Ignition files
** The new disk image
** Adjusted parm line arguments

[source,terminal]
----
$ virt-install \
   --name <vm_name> \
   --autostart \
   --memory=<memory_mb> \
   --cpu host \
   --vcpus <vcpus> \
   --location <media_location>,kernel=<rhcos_kernel>,initrd=<rhcos_initrd> \// <1>
   --disk size=100 \
   --network network=<virt_network_parm> \
   --graphics none \
   --noautoconsole \
   --extra-args "rd.neednet=1 ignition.platform.id=metal ignition.firstboot" \
   --extra-args "ignition.config.url=http://<http_server>/bootstrap.ign" \// <2>
   --extra-args "coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img" \// <3>
   --extra-args "ip=<ip>::<gateway>:<mask>:<hostname>::none" \ <4>
   --extra-args "nameserver=<dns>" \
   --extra-args "console=ttysclp0" \
   --wait
----
<1> For the `--location` parameter, specify the location of the kernel/initrd on the HTTP or HTTPS server.
<2> Specify the location of the `bootstrap.ign` config file. Only HTTP and HTTPS protocols are supported.
<3> For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported.
<4> For the `ip=` parameter, assign the IP address manually as described in "Installing a cluster with {op-system-base} KVM on {ibm-z-name} and {ibm-linuxone-name}".

// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="installing-sno-on-ibm-z-lpar_{context}"]
= Installing {sno} in an LPAR on {ibm-z-title} and {ibm-linuxone-title}

.Prerequisites

* If you are deploying a single-node cluster there are zero compute nodes, the Ingress Controller pods run on the control plane nodes. In single-node cluster deployments, you must configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. See the _Load balancing requirements for user-provisioned infrastructure_ section for more information.

.Procedure

. Set the OpenShift Container Platform version by running the following command:
+
[source,terminal]
----
$ OCP_VERSION=<ocp_version> <1>
----
+
<1> Replace `<ocp_version>` with the current version. For example, `latest-`.

. Set the host architecture by running the following command:
+
[source,terminal]
----
$ ARCH=<architecture> <1>
----
<1> Replace `<architecture>` with the target host architecture `s390x`.

. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
----
+
[source,terminal]
----
$ tar zxvf oc.tar.gz
----
+
[source,terminal]
----
$ chmod +x oc
----

. Download the OpenShift Container Platform installer and make it available for use by entering the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ tar zxvf openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ chmod +x openshift-install
----

. Prepare the `install-config.yaml` file:
+
[source,yaml]
----
apiVersion: v1
baseDomain: <domain> <1>
compute:
- name: worker
  replicas: 0 <2>
controlPlane:
  name: master
  replicas: 1 <3>
metadata:
  name: <name> <4>
networking: <5>
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16 <6>
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
pullSecret: '<pull_secret>' <7>
sshKey: |
  <ssh_key> <8>
----
<1> Add the cluster domain name.
<2> Set the `compute` replicas to `0`. This makes the control plane node schedulable.
<3> Set the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.
<4> Set the `metadata` name to the cluster name.
<5> Set the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.
<6> Set the `cidr` value to match the subnet of the {sno} cluster.
<7> Copy the {cluster-manager-url-pull} and add the contents to this configuration setting.
<8> Add the public SSH key from the administration host so that you can log in to the cluster after installation.

. Generate OpenShift Container Platform assets by running the following commands:
+
[source,terminal]
----
$ mkdir ocp
----
+
[source,terminal]
----
$ cp install-config.yaml ocp
----

. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory> <1>
----
+
<1> For `<installation_directory>`, specify the installation directory that contains the `install-config.yaml` file you created.

. Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `true`.
+
--
.. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
.. Locate the `mastersSchedulable` parameter and ensure that it is set to `true` as shown in the following `spec` stanza:
+
[source,yaml]
----
spec:
  mastersSchedulable: true
status: {}
----
.. Save and exit the file.
--

. Create the Ignition configuration files by running the following command from the directory that contains the installation program:
+
[source,terminal]
----
$ ./openshift-install create ignition-configs --dir <installation_directory> <1>
----
<1> For `<installation_directory>`, specify the same installation directory.

. Obtain the {op-system-base} `kernel`, `initramfs`, and `rootfs`  artifacts from the Product Downloads page on the Red Hat Customer Portal or from the {op-system} image mirror page.
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure.
====
+
The file names contain the OpenShift Container Platform version number. They resemble the following examples:
+
`kernel`:: `rhcos-<version>-live-kernel-<architecture>`
`initramfs`:: `rhcos-<version>-live-initramfs.<architecture>.img`
`rootfs`:: `rhcos-<version>-live-rootfs.<architecture>.img`
+
[NOTE]
====
The `rootfs` image is the same for FCP and DASD.
====

. Move the following artifacts and files to an HTTP or HTTPS server:

** Downloaded {op-system-base} live `kernel`, `initramfs`, and `rootfs` artifacts
** Ignition files

. Create a parameter file for the bootstrap in an LPAR:
+
.Example parameter file for the bootstrap machine
+
[source,terminal]
----
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
coreos.inst.install_dev=/dev/<block_device> \// <1>
coreos.inst.ignition_url=http://<http_server>/bootstrap.ign \// <2>
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \// <3>
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \// <4>
rd.znet=qeth,0.0.1140,0.0.1141,0.0.1142,layer2=1,portno=0 \
rd.dasd=0.0.4411 \// <5>
rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \// <6>
zfcp.allow_lun_scan=0
----
<1> Specify the block device on the system to install to. For installations on DASD-type disk use `dasda`, for installations on FCP-type disks use `sda`.
<2> Specify the location of the `bootstrap.ign` config file. Only HTTP and HTTPS protocols are supported.
<3> For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `kernel`and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported.
<4> For the `ip=` parameter, assign the IP address manually as described in "Installing a cluster in an LPAR on {ibm-z-name} and {ibm-linuxone-name}".
<5> For installations on DASD-type disks, use `rd.dasd=` to specify the DASD where {op-system} is to be installed. Omit this entry for FCP-type disks.
<6> For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where {op-system} is to be installed. Omit this entry for DASD-type disks.
+
You can adjust further parameters if required.

. Create a parameter file for the control plane in an LPAR:
+
.Example parameter file for the control plane machine
+
[source,terminal]
----
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
coreos.inst.install_dev=/dev/<block_device> \
coreos.inst.ignition_url=http://<http_server>/master.ign \// <1>
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,0.0.1140,0.0.1141,0.0.1142,layer2=1,portno=0 \
rd.dasd=0.0.4411 \
rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
zfcp.allow_lun_scan=0
----
<1> Specify the location of the `master.ign` config file. Only HTTP and HTTPS protocols are supported.

. Transfer the following artifacts, files, and images to the LPAR. For example by using FTP:

** `kernel` and `initramfs` artifacts
** Parameter files
** {op-system} images
+
For details about how to transfer the files with FTP and boot, see Installing in an LPAR.

. Boot the bootstrap machine.

. Boot the control plane machine.

[id="installing-sno-with-ibmpower"]
== Installing {sno} with {ibm-power-title}

Installing a single-node cluster on {ibm-power-name} requires user-provisioned installation using the "Installing a cluster with {ibm-power-name}" procedure.

[NOTE]
====
Installing a single-node cluster on {ibm-power-name} simplifies installation for development and test environments and requires less resource requirements at entry level.
====

=== Hardware requirements

* The equivalent of two Integrated Facilities for Linux (IFL), which are SMT2 enabled, for each cluster.
* At least one network connection to connect to the `LoadBalancer` service and to serve data for traffic outside of the cluster.

[NOTE]
====
You can use dedicated or shared IFLs to assign sufficient compute resources. Resource sharing is one of the key strengths of {ibm-power-name}. However, you must adjust capacity correctly on each hypervisor layer and ensure sufficient resources for every OpenShift Container Platform cluster.
====

[role="_additional-resources"]
.Additional resources

* Installing a cluster on {ibm-power-name}

// This module is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="setting-up-bastion-for-sno_{context}"]
= Setting up bastion for {sno} with {ibm-power-title}

Prior to installing {sno} on {ibm-power-name}, you must set up bastion. Setting up a bastion server for {sno} on {ibm-power-name} requires the configuration of the following services:

* PXE is used for the {sno} cluster installation. PXE requires the following services to be configured and run:
** DNS to define api, api-int, and *.apps
** DHCP service to enable PXE and assign an IP address to {sno} node
** HTTP to provide ignition and {op-system} rootfs image
** TFTP to enable PXE
* You must install `dnsmasq` to support DNS, DHCP and PXE, httpd for HTTP.

Use the following procedure to configure a bastion server that meets these requirements.

.Procedure

. Use the following command to install `grub2`, which is required to enable PXE for PowerVM:
+
[source,terminal]
----
grub2-mknetdir --net-directory=/var/lib/tftpboot
----
+
.Example `/var/lib/tftpboot/boot/grub2/grub.cfg` file
[source,terminal]
----
default=0
fallback=1
timeout=1
if [ ${net_default_mac} == fa:b0:45:27:43:20 ]; then
menuentry "CoreOS (BIOS)" {
   echo "Loading kernel"
   linux "/rhcos/kernel" ip=dhcp rd.neednet=1 ignition.platform.id=metal ignition.firstboot coreos.live.rootfs_url=http://192.168.10.5:8000/install/rootfs.img ignition.config.url=http://192.168.10.5:8000/ignition/sno.ign
   echo "Loading initrd"
   initrd  "/rhcos/initramfs.img"
}
fi
----

. Use the following commands to download {op-system} image files from the mirror repo for PXE.

.. Enter the following command to assign the `RHCOS_URL` variable the follow 4.12 URL:
+
[source,terminal]
----
$ export RHCOS_URL=https://mirror.openshift.com/pub/openshift-v4/ppc64le/dependencies/rhcos/4.12/latest/
----

.. Enter the following command to navigate to the `/var/lib/tftpboot/rhcos` directory:
+
[source,terminal]
----
$ cd /var/lib/tftpboot/rhcos
----

.. Enter the following command to download the specified {op-system} kernel file from the URL stored in the `RHCOS_URL` variable:
+
[source,terminal]
----
$ wget ${RHCOS_URL}/rhcos-live-kernel-ppc64le -o kernel
----

.. Enter the following command to download the {op-system} `initramfs` file from the URL stored in the `RHCOS_URL` variable:
+
[source,terminal]
----
$ wget ${RHCOS_URL}/rhcos-live-initramfs.ppc64le.img -o initramfs.img
----

.. Enter the following command to navigate to the `/var//var/www/html/install/` directory:
+
[source,terminal]
----
$ cd /var//var/www/html/install/
----

.. Enter the following command to download, and save, the {op-system} `root filesystem` image file from the URL stored in the `RHCOS_URL` variable:
+
[source,terminal]
----
$ wget ${RHCOS_URL}/rhcos-live-rootfs.ppc64le.img -o rootfs.img
----

. To create the ignition file for a {sno} cluster, you must create the `install-config.yaml` file.

.. Enter the following command to create the work directory that holds the file:
+
[source,terminal]
----
$ mkdir -p ~/sno-work
----

.. Enter the following command to navigate to the `~/sno-work` directory:
+
[source,terminal]
----
$ cd ~/sno-work
----

.. Use the following sample file can to create the required `install-config.yaml` in the `~/sno-work` directory:
+
[source,yaml]
----
apiVersion: v1
baseDomain: <domain> <1>
compute:
- name: worker
  replicas: 0 <2>
controlPlane:
  name: master
  replicas: 1 <3>
metadata:
  name: <name> <4>
networking: <5>
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16 <6>
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
bootstrapInPlace:
  installationDisk: /dev/disk/by-id/<disk_id> <7>
pullSecret: '<pull_secret>' <8>
sshKey: |
  <ssh_key> <9>
----
<1> Add the cluster domain name.
<2> Set the `compute` replicas to `0`. This makes the control plane node schedulable.
<3> Set the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures that the cluster runs on a single node.
<4> Set the `metadata` name to the cluster name.
<5> Set the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.
<6> Set the `cidr` value to match the subnet of the {sno} cluster.
<7> Set the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.
<8> Copy the {cluster-manager-url-pull} and add the contents to this configuration setting.
<9> Add the public SSH key from the administration host so that you can log in to the cluster after installation.

. Download the `openshift-install` image to create the ignition file and copy it to the `http` directory.

.. Enter the following command to download the `openshift-install-linux-4.12.0` .tar file:
+
[source,terminal]
----
$ wget https://mirror.openshift.com/pub/openshift-v4/ppc64le/clients/ocp/4.12.0/openshift-install-linux-4.12.0.tar.gz
----

.. Enter the following command to unpack the `openshift-install-linux-4.12.0.tar.gz` archive:
+
[source,terminal]
----
$ tar xzvf openshift-install-linux-4.12.0.tar.gz
----

.. Enter the following command to
+
[source,terminal]
----
$ ./openshift-install --dir=~/sno-work create create single-node-ignition-config
----

.. Enter the following command to create the ignition file:
+
[source,terminal]
----
$ cp ~/sno-work/single-node-ignition-config.ign /var/www/html/ignition/sno.ign
----

.. Enter the following command to restore SELinux file for the `/var/www/html` directory:
+
[source,terminal]
----
$ restorecon -vR /var/www/html || true
----
+
Bastion now has all the required files and is properly configured in order to install {sno}.

// This is included in the following assemblies:
//
// installing_sno/install-sno-installing-sno.adoc

[id="installing-sno-on-ibm-power_{context}"]
= Installing {sno} with {ibm-power-title}

.Prerequisites

* You have set up bastion.

.Procedure

There are two steps for the {sno} cluster installation. First the {sno} logical partition (LPAR) needs to boot up with PXE, then you need to monitor the installation progress.

. Use the following command to boot powerVM with netboot:
+
[source,terminal]
----
$ lpar_netboot -i -D -f -t ent -m <sno_mac> -s auto -d auto -S <server_ip> -C <sno_ip> -G <gateway> <lpar_name> default_profile <cec_name>
----
+
where:
+
--
sno_mac:: Specifies the MAC address of the {sno} cluster.
sno_ip:: Specifies the IP address of the {sno} cluster.
server_ip:: Specifies the IP address of bastion (PXE server).
gateway:: Specifies the Network's gateway IP.
lpar_name:: Specifies the {sno} lpar name in HMC.
cec_name:: Specifies the System name where the sno_lpar resides
--

. After the {sno} LPAR boots up with PXE, use the `openshift-install` command to monitor the progress of installation:

.. Run the following command after the bootstrap is complete:
+
[source,terminal]
----
./openshift-install wait-for bootstrap-complete
----

.. Run the following command after it returns successfully:
+
[source,terminal]
----
./openshift-install wait-for install-complete
----
