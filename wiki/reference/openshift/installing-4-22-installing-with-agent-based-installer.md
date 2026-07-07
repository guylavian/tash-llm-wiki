---
title: "Installing a cluster with customizations"
type: reference
domain: openshift
slug: installing-4-22-installing-with-agent-based-installer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-with-agent-based-installer
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster with customizations

[id="installing-with-agent-based-installer"]
= Installing a cluster with customizations

[role="_abstract"]
You can install an OpenShift Container Platform cluster using the Agent-based Installer, with customizations to meet your deployment needs.

The following procedures deploy a single-node OpenShift Container Platform cluster in a disconnected environment. You can use these procedures as a basis and modify according to your requirements.

[id="prerequisites_{context}"]
= Prerequisites for installing a cluster with the Agent-based Installer

[role="_abstract"]
Before beginning your cluster installation, you must complete prerequisite tasks that prepare your environment.

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update".
* You read "Selecting a cluster installation method and preparing it for users".
* If you use a firewall or proxy, you configured it to allow the sites that your cluster requires access to. For more information, see "Configuring your firewall".

[id="prerequisites_{context}"]
= Prerequisites for preparing PXE assets

[role="_abstract"]
Before beginning to prepare PXE assets, you must complete prerequisite tasks.

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update".

[role="_additional-resources"]
.Additional resources

* Installation and update
* Selecting a cluster installation method and preparing it for users
* Configuring your firewall

// Downloading the Agent-based Installer
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/prepare-pxe-infra-agent.adoc
// * installing/installing_with_agent_based_installer/installing-using-iscsi.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-retrieve_{context}"]
= Downloading the Agent-based Installer

[role="_abstract"]
Begin the installation process by downloading the Agent-based Installer and the CLI needed for your installation.

.Procedure

. Log in to the {hybrid-console} using your login credentials.

. Navigate to Datacenter.

. Click *Run Agent-based Installer locally*.

. Select the operating system and architecture for the *OpenShift Installer* and *Command line interface*.

. Click *Download Installer* to download and extract the install program.

. Download or copy the pull secret by clicking on *Download pull secret* or *Copy pull secret*.

. Click *Download command-line tools* and place the `openshift-install` binary in a directory that is on your `PATH`.

// Verifying the supported architecture for an Agent-based installation
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/preparing-to-install-with-agent-based-installer.adoc

[id="agent-install-verifying-architectures_{context}"]
= Verifying the supported architecture for an Agent-based installation

[role="_abstract"]
Before installing an OpenShift Container Platform cluster using the Agent-based Installer, you can optionally verify the supported architecture on which you can install the cluster.

.Prerequisites

* You installed the {oc-first}.
* You have downloaded the installation program.

.Procedure

. Log in to the {oc-first}.

. Check your release payload by running the following command:
[source,terminal]
+
----
$ ./openshift-install version
----
+
.Example output
[source,terminal]
----
./openshift-install 4.22.0
built from commit abc123def456
release image quay.io/openshift-release-dev/ocp-release@sha256:123abc456def789ghi012jkl345mno678pqr901stu234vwx567yz0
release architecture amd64
----
+
If you are using the release image with the `multi` payload, the `release architecture` displayed in the output of this command is the default architecture.

. To check the architecture of the payload, run the following command:
[source,terminal]
+
----
$ oc adm release info <release_image> -o jsonpath="{ .metadata.metadata}"
----
+
Replace `<release_image>` with the release image. For example: `quay.io/openshift-release-dev/ocp-release@sha256:123abc456def789ghi012jkl345mno678pqr901stu234vwx567yz0`.
+
.Example output when the release image uses the `multi` payload
[source,terminal]
----
{"release.openshift.io architecture":"multi"}
----
+
If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command.

// Creating the preferred configuration inputs
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// *installing/installing_with_agent_based_installer/prepare-pxe-infra-agent.adoc
// * installing/installing_with_agent_based_installer/installing-using-iscsi.adoc

[id="installing-ocp-agent-inputs_{context}"]
= Creating the preferred configuration inputs

[role="_abstract"]
Create the preferred configuration inputs used to create the agent image.

[NOTE]
====
Configuring the `install-config.yaml` and `agent-config.yaml` files is the preferred method for using the Agent-based Installer. Using {ztp} manifests is optional.
====
Create the preferred configuration inputs used to create the PXE files.

[NOTE]
====
Configuring the `install-config.yaml` and `agent-config.yaml` files is the preferred method for using the Agent-based Installer. Using {ztp} manifests is optional.
====

.Procedure

. Install the `nmstate` dependency by running the following command:
+
[source,terminal]
----
$ sudo dnf install /usr/bin/nmstatectl -y
----

. Place the `openshift-install` binary in a directory that is on your PATH.

. Create a directory to store the install configuration by running the following command:
+
[source,terminal]
----
$ mkdir ~/<directory_name>
----

. Create the `install-config.yaml` file by running the following command:
+
--
[source,terminal]
----
$ cat << EOF > ./<directory_name>/install-config.yaml
apiVersion: v1
baseDomain: test.example.com
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  replicas: 0
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  replicas: 1
metadata:
  name: sno-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 192.168.0.0/16
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
pullSecret: '<pull_secret>'
sshKey: '<ssh_pub_key>'
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
EOF
----

where:

`compute.architecture`:: Specifies the system architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.
+
If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command. For more information, see "Verifying the supported architecture for installing an Agent-based Installer cluster".

`metadata.name`:: Specifies your cluster name. This value is required.

`networking.networkingType`:: Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`platform`:: Specifies your platform. If you set the platform to `vSphere`, `baremetal`, or `none`, you can configure IP address endpoints for cluster nodes in three ways: IPv4, IPv6, or IPv4 and IPv6 in parallel (dual-stack).
+
.Example of dual-stack networking
[source,yaml]
----
networking:
  clusterNetwork:
    - cidr: 172.21.0.0/16
      hostPrefix: 23
    - cidr: fd02::/48
      hostPrefix: 64
  machineNetwork:
    - cidr: 192.168.11.0/16
    - cidr: 2001:DB8::/32
  serviceNetwork:
    - 172.22.0.0/16
    - fd03::/112
  networkType: OVNKubernetes
platform:
  baremetal:
    apiVIPs:
    - 192.168.11.3
    - 2001:DB8::4
    ingressVIPs:
    - 192.168.11.4
    - 2001:DB8::5
----
+
[NOTE]
====
For bare-metal platforms, host settings made in the platform section of the `install-config.yaml` file are used by default, unless they are overridden by configurations made in the `agent-config.yaml` file.
====

`pullSecret`:: Specifies your pull secret.

`sshKey`:: Specifies your SSH public key.

`additionalTrustBundle`:: Specifies the contents of the certificate file that you used for your mirror registry.
The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry.
You must specify this parameter if you are using a disconnected mirror registry.

`imageContentSources`:: Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository.
You must specify this parameter if you are using a disconnected mirror registry.
+
[IMPORTANT]
====
* When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
* When using the `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
* The `ImageContentSourcePolicy` resource is deprecated.
====
--

. Create the `agent-config.yaml` file by running the following command:
+
--
[source,terminal]
----
$ cat > agent-config.yaml << EOF
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: sno-cluster
rendezvousIP: 192.168.111.80
hosts:
  - hostname: master-0
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a5
    rootDeviceHints:
      deviceName: /dev/sdb
    networkConfig:
      interfaces:
        - name: eno1
          type: ethernet
          state: up
          mac-address: 00:ef:44:21:e6:a5
          ipv4:
            enabled: true
            address:
              - ip: 192.168.111.80
                prefix-length: 23
            dhcp: false
      dns-resolver:
        config:
          server:
            - 192.168.111.1
      routes:
        config:
          - destination: 0.0.0.0/0
            next-hop-address: 192.168.111.2
            next-hop-interface: eno1
            table-id: 254
EOF
----

where:

`rendezvousIP`:: Specifies the IP address used to determine which node performs the bootstrapping process as well as running the `assisted-service` component.
You must provide the rendezvous IP address when you do not specify at least one host's IP address in the `networkConfig` parameter. If this address is not provided, one IP address is selected from the provided hosts' `networkConfig`.

`hosts`:: Specifies host configuration. The number of hosts defined must not exceed the total number of hosts defined in the `install-config.yaml` file, which is the sum of the values of the `compute.replicas` and `controlPlane.replicas` parameters. This configuration is optional.

`hosts.hostname`:: Specifies a value that overrides the hostname obtained from either the Dynamic Host Configuration Protocol (DHCP) or a reverse DNS lookup. Each host must have a unique hostname supplied by one of these methods. This configuration is optional.

`hosts.rootDeviceHints`:: Specifies a configuration that enables provisioning of the {op-system-first} image to a particular device. The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value.
+
[NOTE]
====
This parameter is mandatory for FCP multipath configurations on {ibm-z-title}.
====

`hosts.networkConfig`:: Specifies the network interface configuration of a host in NMState format. This configuration is optional.
`minimalISO`:: Specifies whether to generate an ISO image without the rootfs image file, instead providing details about where to pull the rootfs file from.
You must set this parameter to `true` to enable iSCSI booting.
--

. Optional: To create an iPXE script, add the `bootArtifactsBaseURL` to the `agent-config.yaml` file:
+
[source,yaml]
----
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: sno-cluster
rendezvousIP: 192.168.111.80
bootArtifactsBaseURL: <asset_server_URL>
----
+
Where `<asset_server_URL>` is the URL of the server you will upload the PXE assets to.

[role="_additional-resources"]
.Additional resources
* Deploying with dual-stack networking
* Configuring the install-config yaml file
* Configuring a three-node cluster
* About root device hints
* NMState state examples (NMState documentation)
* Configuring regions and zones for a VMware vCenter
* Verifying the supported architecture for installing an Agent-based installer cluster
* Configuring the Agent-based Installer to use mirrored images

[id="installing-ocp-agent-opt-manifests_{context}"]
= Creating additional manifest files

[role="_abstract"]
As an optional task, you can create additional manifests to further configure your cluster beyond the configurations available in the `install-config.yaml` and `agent-config.yaml` files.

[IMPORTANT]
====
Customizations to the cluster made by additional manifests are not validated, are not guaranteed to work, and might result in a nonfunctional cluster.
====

// Creating a directory to contain additional manifests
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc

[id="installing-ocp-agent-manifest-folder_{context}"]
= Creating a directory to contain additional manifests

[role="_abstract"]
If you create additional manifests to configure your Agent-based installation beyond the `install-config.yaml` and `agent-config.yaml` files, you must create an `openshift` subdirectory within your installation directory.
All of your additional machine configurations must be located within this subdirectory.

[NOTE]
====
The most common type of additional manifest you can add is a `MachineConfig` object.
For examples of `MachineConfig` objects you can add during the Agent-based installation, see "Using MachineConfig objects to configure nodes" in the "Additional resources" section.
====

.Procedure

* On your installation host, create an `openshift` subdirectory within the installation directory by running the following command:
+
[source,terminal]
----
$ mkdir <installation_directory>/openshift
----

[role="_additional-resources"]
.Additional resources

* Using MachineConfig objects to configure nodes

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="creating-manifest-file-customized-br-ex-bridge_{context}"]
= Creating a manifest object that includes a customized br-ex bridge

[role="_abstract"]
By default, OpenShift Container Platform automatically configures the Open vSwitch (OVS) `br-ex` bridge on bare-metal nodes. For advanced networking requirements, you can override this default behavior on bare-metal platforms. To do this, create a `MachineConfig` object that includes an NMState configuration file.

By default, OpenShift Container Platform automatically configures the Open vSwitch (OVS) `br-ex` bridge on nodes. For advanced networking requirements, you can override this default behavior on bare-metal platforms. To do this, use the Agent-based Installer to create a `MachineConfig` object that includes an NMState configuration file.

[IMPORTANT]
====
Customizations to the cluster made by additional manifests are not validated and not guaranteed to work. These manifests might result in a nonfunctional cluster.

For more information about an additional manifest file, see "Creating a directory to contain additional manifests".
====

Consider using the customized `br-ex` bridge configuration for any of the following tasks:

* You need to modify the `br-ex` bridge after you installed the cluster.
* You need to modify the maximum transmission unit (MTU) for your cluster.
* You need to update DNS values.
* You need to modify attributes for a different bond interface. Examples include MIImon (Media Independent Interface Monitor), bonding mode or Quality of Service (QoS).
* You need to enable Link Layer Discovery Protocol (LLDP) to discover and troubleshoot switch connectivity.

[NOTE]
====
Use the default OVS `br-ex` bridge for standard environments.

Use the default OVS `br-ex` bridge mechanism for single network interface controller (NIC) environments with default network settings.
====

After you install {op-system-first} and the system reboots, the Machine Config Operator injects Ignition configuration files into each node. This operation ensures that each node receives the `br-ex` bridge network configuration. To prevent configuration conflicts, the default OVS `br-ex` bridge mechanism is disabled.

[WARNING]
====
The following list of interface names are reserved and you cannot use the names with NMstate configurations:

* `br-ext`
* `br-int`
* `br-local`
* `br-nexthop`
* `br0`
* `ext-vxlan`
* `ext`
* `genev_sys_*`
* `int`
* `k8s-*`
* `ovn-k8s-*`
* `patch-br-*`
* `tun0`
* `vxlan_sys_*`
====

.Prerequisites
* Optional: You have installed the `nmstatectl` CLI tool to validate your NMState configuration.
* You checked that an `openshift` subdirectory exists in your installation directory. If the subdirectory does not exist, create the subdirectory.

.Procedure

. Create an NMState configuration file and define a customized `br-ex` bridge network configuration in the file:
+
.Example of an NMState configuration for a customized `br-ex` bridge network
[source,yaml]
----
interfaces:
- name: enp2s0
  type: ethernet
  state: up
  ipv4:
    enabled: false
  ipv6:
    enabled: false
- name: br-ex
  type: ovs-bridge
  state: up
  ipv4:
    enabled: false
    dhcp: false
  ipv6:
    enabled: false
    dhcp: false
  bridge:
    options:
      mcast-snooping-enable: true
    port:
    - name: enp2s0
    - name: br-ex
- name: br-ex
  type: ovs-interface
  state: up
  copy-mac-from: enp2s0
  ipv4:
    enabled: true
    dhcp: true
    auto-route-metric: 48
  ipv6:
    enabled: true
    dhcp: true
    auto-route-metric: 48
# ...
----
+
where:
+
`interfaces.name`:: Name of the interface.
`interfaces.type`:: The type of ethernet.
`interfaces.state`:: The requested state for the interface after creation.
`ipv4.enabled`:: Disables IPv4 and IPv6 in this example.
`port.name`:: The node NIC to which the bridge attaches.
`auto-route-metric`:: Set the parameter to `48` to ensure the `br-ex` default route always has the highest precedence (lowest metric). This configuration prevents routing conflicts with any other interfaces automatically configured by the `NetworkManager` service.

. Use the `cat` command to base64-encode the contents of the NMState configuration:
+
[source,terminal]
----
$ cat <nmstate_configuration>.yml | base64
----
+
where:
+
`<nmstate_configuration>`:: Replace `<nmstate_configuration>` with the name of your NMState resource YAML file.

. Create a `MachineConfig` manifest file and define a customized `br-ex` bridge network configuration analogous to the following example. The installation program automatically applies the updates from the `MachineConfig` object to your cluster.

. Create a `MachineConfig` file as an additional manifest file. Define a customized `br-ex` bridge network configuration analogous to the following example in the file. The Agent-based Installer automatically applies the updates from the `MachineConfig` object to your cluster.
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 10-br-ex-worker
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/worker-0.yml
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/worker-1.yml
# ...
----
+
where:
+
`metadata.name`:: Specifies the name of the policy.
`contents.source`:: Writes the encoded base64 information to the specified path.
`path`:: For each node in your cluster, specify the hostname path to your node and the base-64 encoded Ignition configuration file data for the machine type. The `worker` role is the default role for nodes in your cluster. Use the `.yml` extension for configuration files. For example, use `$(hostname -s).yml` when specifying the short hostname path for each node or all nodes in the `MachineConfig` manifest file.
+
You can apply a single global configuration to all nodes by using the `/etc/nmstate/openshift/cluster.yml` configuration file. In this case, you do not need to specify individual hostname paths for each node, such as `/etc/nmstate/openshift/<node_hostname>.yml`.
+
.Example /etc/nmstate/openshift/cluster.yml configuration file
[source,yaml]
----
# ...
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
        mode: 0644
        overwrite: true
        path: /etc/nmstate/openshift/cluster.yml
# ...
----

. Save the additional manifest file in the `openshift` subdirectory of your installation directory.
+
On completing other configuration inputs for your installation, such as encrypting the disk, you create the ISO image. After booting this image, the customized `br-ex` bridge configuration applies to each node in your cluster.

.Next steps

* Scaling compute nodes to apply the manifest object that includes a customized `br-ex` bridge to each compute node that exists in your cluster. For more information, see "Expanding the cluster" in the _Additional resources_ section.

// Disk partitioning
// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="installation-user-infra-machines-advanced-disk_{context}"]
= Disk partitioning

[role="_abstract"]
Disk partitions are created on OpenShift Container Platform cluster nodes during the {op-system-first} installation. Each {op-system} node of a particular architecture uses the same partition layout, unless you override the default partitioning configuration.

During the {op-system} installation, the size of the root file system is increased to use any remaining available space on the target device.

[IMPORTANT]
====
The use of a custom partition scheme on your node might result in OpenShift Container Platform not monitoring or alerting on some node partitions. For more information on monitoring host file systems when using custom partitioning, see Understanding OpenShift File System Monitoring (eviction conditions).
====

OpenShift Container Platform monitors the following two filesystem identifiers:

* `nodefs`, which is the filesystem that contains `/var/lib/kubelet`.
* `imagefs`, which is the filesystem that contains `/var/lib/containers`.

For the default partition scheme, `nodefs` and `imagefs` monitor the same root filesystem, `/`.

To override the default partitioning when installing {op-system} on an OpenShift Container Platform cluster node, you must create separate partitions. Consider a situation where you want to add a separate storage partition for your containers and container images. For example, by mounting `/var/lib/containers` in a separate partition, the kubelet separately monitors `/var/lib/containers` as the `imagefs` directory and the root file system as the `nodefs` directory.

[IMPORTANT]
====
If you have resized your disk size to host a larger file system, consider creating a separate `/var/lib/containers` partition. Consider resizing a disk that has an `xfs` format to reduce CPU time issues caused by a high number of allocation groups.
====
[id="installation-user-infra-machines-advanced-disk_{context}"]
= Creating disk partitions

[role="_abstract"]
In general, you must use the default disk partitioning that is created during the {op-system} installation. However, there are cases where you might want to create a separate partition for a directory that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` directory or a subdirectory of `/var`. For example:

* `/var/lib/containers`: Holds container-related content that can grow
as more images and containers are added to a system.
* `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.
* `/var`: Holds data that you might want to keep separate for purposes such as auditing.
+
[IMPORTANT]
====
For disk sizes larger than 100GB, and especially larger than 1TB, create a separate `/var` partition.
====

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date to keep that data intact. This method eliminates the need to re-pull containers or copy large log files during system updates.

The use of a separate partition for the `/var` directory or a subdirectory of `/var` also prevents data growth in the partitioned directory from filling up the root file system.

The following procedure sets up a separate `/var` partition by adding a machine config manifest that is wrapped into the Ignition config file for a node type during the preparation phase of an installation.

.Prerequisites
* You have created an `openshift` subdirectory within your installation directory.

.Procedure

. On your installation host, change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:
+
[source,terminal]
----
$ openshift-install create manifests --dir <installation_directory>
----

. Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 98-var-partition
storage:
  disks:
  - device: /dev/disk/by-id/<device_name>
    partitions:
    - label: var
      start_mib: <partition_start_offset>
      size_mib: <partition_size>
      number: 5
  filesystems:
    - device: /dev/disk/by-partlabel/var
      path: /var
      format: xfs
      mount_options: [defaults, prjquota]
      with_mount_unit: true
----
+
where:
+
`<device_name>`:: Specifies the storage device name of the disk that you want to partition.
`<partition_start_offset>`:: Specifies the minimum offset value for the boot disk. For best performance, specify a minimum offset value of 25000 mebibytes. The root file system is automatically resized to fill all available space up to the specified offset. If no offset value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of {op-system} might overwrite the beginning of the data partition.
`<partition_size>`:: Specifies the size of the data partition in mebibytes.
`mount_options`:: The `prjquota` mount option must be enabled for filesystems used for container storage.
+
[NOTE]
====
When creating a separate `/var` partition, you cannot use different instance types for compute nodes, if the different instance types do not have the same device name.
====

. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:
+
[source,terminal]
----
$ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
----

. Create the Ignition config files by running the following command:
+
[source,terminal]
----
$ openshift-install create ignition-configs --dir <installation_directory>
----
+
where:
+
`<installation_directory>`:: Specifies the name of the installation directory.
+
Ignition config files are created for the bootstrap, control plane, and compute nodes in the installation directory:
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
+
The files in the `<installation_directory>/manifest` and `<installation_directory>/openshift` directories are wrapped into the Ignition config files, including the file that contains the `98-var-partition` custom `MachineConfig` object.

. Optional: You can apply the custom disk partitioning by referencing the Ignition config files during the {op-system} installations.

// Using ZTP manifests
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc

[id="installing-ocp-agent-ztp_{context}"]
= Using ZTP manifests

[role="_abstract"]
As an optional task, you can use {ztp-first} manifests to configure your installation beyond the options available through the `install-config.yaml` and `agent-config.yaml` files.

See "Challenges of the network far edge" to learn more about {ztp-first}.

[IMPORTANT]
====
Zero Touch Provisioning (ZTP) is not supported for two-node clusters with fencing (TNF). Although you can use Red Hat Advanced Cluster Management (RHACM) for installations, the additional infrastructure components required for ZTP are not validated for this topology.
====

[NOTE]
====
{ztp} manifests can be generated with or without configuring the `install-config.yaml` and `agent-config.yaml` files beforehand.
If you chose to configure the `install-config.yaml` and `agent-config.yaml` files, the configurations will be imported to the ZTP cluster manifests when they are generated.
====

.Prerequisites

* You have placed the `openshift-install` binary in a directory that is on your `PATH`.

* Optional: You have created and configured the `install-config.yaml` and `agent-config.yaml` files.

.Procedure

. Generate ZTP cluster manifests by running the following command:
+
[source,terminal]
----
$ openshift-install agent create cluster-manifests --dir <installation_directory>
----
+
[IMPORTANT]
====
If you have created the `install-config.yaml` and `agent-config.yaml` files, those files are deleted and replaced by the cluster manifests generated through this command.

Any configurations made to the `install-config.yaml` and `agent-config.yaml` files are imported to the ZTP cluster manifests when you run the `openshift-install agent create cluster-manifests` command.
====

. Navigate to the `cluster-manifests` directory by running the following command:
+
[source,terminal]
----
$ cd <installation_directory>/cluster-manifests
----

. Configure the manifest files in the `cluster-manifests` directory.
For sample files, see the "Sample GitOps ZTP custom resources" section.

. Disconnected clusters: If you did not define mirror configuration in the `install-config.yaml` file before generating the ZTP manifests, perform the following steps:

.. Navigate to the `mirror` directory by running the following command:
+
[source,terminal]
----
$ cd ../mirror
----

.. Configure the manifest files in the `mirror` directory.

[role="_additional-resources"]
.Additional resources
* Sample {ztp} custom resources

* Challenges of the network far edge

// Encrypting the disk
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc

[id="installing-ocp-agent-encrypt_{context}"]
= Encrypting the disk

[role="_abstract"]
As an optional task, you can encrypt your disk or partition while installing OpenShift Container Platform with the Agent-based Installer.

[IMPORTANT]
====
If there are leftover TPM encryption keys from a previous operating system on the bare-metal host, the cluster deployment can get stuck.
To avoid this situation, it is highly recommended to reset the TPM chip in the BIOS before booting the ISO.
====

.Prerequisites

* You have created and configured the `install-config.yaml` and `agent-config.yaml` files, unless you are using ZTP manifests.

* You have placed the `openshift-install` binary in a directory that is on your `PATH`.

.Procedure

. Generate ZTP cluster manifests by running the following command:
+
[source,terminal]
----
$ openshift-install agent create cluster-manifests --dir <installation_directory>
----
+
[IMPORTANT]
====
If you have created the `install-config.yaml` and `agent-config.yaml` files, those files are deleted and replaced by the cluster manifests generated through this command.

Any configurations made to the `install-config.yaml` and `agent-config.yaml` files are imported to the ZTP cluster manifests when you run the `openshift-install agent create cluster-manifests` command.
====
+
[NOTE]
====
If you have already generated ZTP manifests, skip this step.
====

. Navigate to the `cluster-manifests` directory by running the following command:
+
[source,terminal]
----
$ cd <installation_directory>/cluster-manifests
----

. Add the following section to the `agent-cluster-install.yaml` file:
+
[source,yaml]
----
diskEncryption:
    enableOn: all
    mode: tang
    tangServers: "server1": "http://tang-server-1.example.com:7500"
----
+
where:

`diskEncryption.enableOn`:: Specifies which nodes to enable disk encryption on. Valid values are `none`, `all`, `masters`, and `workers`.
`diskEncryption.mode`:: Specifies which disk encryption mode to use. Valid values are `tpmv2` and `tang`.
`diskEncryption.tangServers`:: Specifies the Tang servers if you are using Tang. This value is optional.

[role="_additional-resources"]
.Additional resources

* About disk encryption

// Creating and booting the agent image
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-boot_{context}"]
= Creating and booting the agent image

[role="_abstract"]
After you have prepared the configuration inputs for your installation, create the ISO image and boot it on your machines.

.Prerequisites

* If you plan to boot the agent image from a USB drive, you have installed the `syslinux` package.

.Procedure

. Create the agent image by running the following command:
+
[source,terminal]
----
$ openshift-install --dir <install_directory> agent create image
----
+
[NOTE]
====
{op-system-first} supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the agent ISO image, with a default `/etc/multipath.conf` configuration.
====

. If you plan to boot the ISO image from a USB drive, add a master boot record to the image by running the following command:
+
[source,terminal]
----
$ isohybrid --uefi <agent_iso_image>
----
+
.Example command
[source,terminal]
----
$ isohybrid --uefi agent.x86_64.iso
----

. Boot the `agent.x86_64.iso`, `agent.aarch64.iso`, or `agent.s390x.iso` image on the bare-metal machines.

// Adding {ibm-z-name} agents with {op-system-base} KVM
// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/prepare-pxe-infra-agent.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-based-installer.adoc

[id="installing-ocp-agent-ibm-z-kvm_{context}"]
= Adding {ibm-z-title} agents with {op-system-base} KVM

[role="_abstract"]
You can manually add {ibm-z-name} agents with {op-system-base} KVM.

Only use this procedure for {ibm-z-name} clusters with {op-system-base} KVM.

[NOTE]
====
The `nmstateconfig` parameter must be configured for the KVM boot.
====

.Procedure

. Boot your {op-system-base} KVM machine.

. To deploy the virtual server, run the `virt-install` command with the following parameters:

+
[source,terminal]
----
$ virt-install \
   --name <vm_name> \
   --autostart \
   --ram=16384 \
   --cpu host \
   --vcpus=8 \
   --location <path_to_kernel_initrd_image>,kernel=kernel.img,initrd=initrd.img \
   --disk <qcow_image_path> \
   --network network:macvtap ,mac=<mac_address> \
   --graphics none \
   --noautoconsole \
   --wait=-1 \
   --extra-args "rd.neednet=1 nameserver=<nameserver>" \
   --extra-args "ip=<IP>::<nameserver>::<hostname>:enc1:none" \
   --extra-args "coreos.live.rootfs_url=http://<http_server>:8080/agent.s390x-rootfs.img" \
   --extra-args "random.trust_cpu=on rd.luks.options=discard" \
   --extra-args "ignition.firstboot ignition.platform.id=metal" \
   --extra-args "console=tty1 console=ttyS1,115200n8" \
   --extra-args "coreos.inst.persistent-kargs=console=tty1 console=ttyS1,115200n8" \
   --osinfo detect=on,require=off
----
+
For the `--location` parameter, specify the location of the `kernel` and `initrd` files. The location can be a local server path or a URL using HTTP or HTTPS.

+
.ISO boot
[source,terminal]
----
$ virt-install
    --name <vm_name> \
    --autostart \
    --memory=<memory> \
    --cpu host \
    --vcpus=<vcpus> \
    --cdrom \<path_to_image>/<agent_iso_image> \
    --disk pool=default,size=<disk_pool_size> \
    --network network:default,mac=<mac_address> \
    --graphics none \
    --noautoconsole \
    --os-variant rhel9.0 \
    --wait=-1
----
+
For the `--cdrom` parameter, specify the location of the ISO image on the local server, for example, `<path_to_image>/home/<image>.iso`.
+
[NOTE]
====
For KVM-based installations using DASD devices on {ibm-z-title}, a partition (for example, `/dev/dasdb1`) must be created using the `fdasd` partitioning tool.
====
+

. Optional: Enable FIPS mode.
+
To enable FIPS mode on {ibm-z-name} clusters with {op-system-base} KVM you must use PXE boot instead and run the `virt-install` command with the following parameters:
+
.PXE boot
[source,terminal]
----
$ virt-install \
   --name <vm_name> \
   --autostart \
   --ram=16384 \
   --cpu host \
   --vcpus=8 \
   --location <path_to_kernel_initrd_image>,kernel=kernel.img,initrd=initrd.img \
   --disk <qcow_image_path> \
   --network network:macvtap ,mac=<mac_address> \
   --graphics none \
   --noautoconsole \
   --wait=-1 \
   --extra-args "rd.neednet=1 nameserver=<nameserver>" \
   --extra-args "ip=<IP>::<nameserver>::<hostname>:enc1:none" \
   --extra-args "coreos.live.rootfs_url=http://<http_server>:8080/agent.s390x-rootfs.img" \
   --extra-args "random.trust_cpu=on rd.luks.options=discard" \
   --extra-args "ignition.firstboot ignition.platform.id=metal" \
   --extra-args "console=tty1 console=ttyS1,115200n8" \
   --extra-args "coreos.inst.persistent-kargs=console=tty1 console=ttyS1,115200n8" \
   --extra-args "fips=1" \
   --osinfo detect=on,require=off
----
+
where:

`--location`:: Specifies the location of the kernel/initrd on the HTTP or HTTPS server.
`--extra-args "fips=1"`:: Specifies the enablement of FIPS mode. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file.
+
[NOTE]
====
* For KVM-based installations using DASD devices on {ibm-z-title}, a partition (for example, `/dev/dasdb1`) must be created using the `fdasd` partitioning tool.

* Currently, only PXE boot is supported to enable FIPS mode on {ibm-z-name}.
====

// Configuring a local arbiter node
// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-local-arbiter-node_{context}"]
= Configuring a local arbiter node

You can configure an OpenShift Container Platform cluster with two control plane nodes and one local arbiter node so as to retain high availability (HA) while reducing infrastructure costs for your cluster.

A local arbiter node is a lower-cost, co-located machine that participates in control plane quorum decisions. Unlike a standard control plane node, the arbiter node does not run the full set of control plane services. You can use this configuration to maintain HA in your cluster with only two fully provisioned control plane nodes instead of three.

[IMPORTANT]
====
You can configure a local arbiter node only. Remote arbiter nodes are not supported.
====

To deploy a cluster with two control plane nodes and one local arbiter node, you must define the following nodes in the `install-config.yaml` file:

* 2 control plane nodes
* 1 arbiter node

The arbiter node must meet the following minimum system requirements:

* 2 vCPUs
* 8 GB of RAM
* 50 GB of SSD or equivalent storage

The arbiter node must be located in a network environment with an end-to-end latency of less than 500 milliseconds, including disk I/O. In high-latency environments, you might need to apply the `etcd` slow profile.

The control plane nodes must meet the following minimum system requirements:

* 4 vCPUs
* 16 GB of RAM
* 120 GB of SSD or equivalent storage

Additionally, the control plane nodes must also have enough storage for the workload.

.Prerequisites

* You have downloaded {oc-first} and the installation program.
* You have logged into the {oc-first}.

.Procedure

. Edit the `install-config.yaml` file to define the arbiter node alongside control plane nodes.
+
.Example `install-config.yaml` configuration for deploying an arbiter node
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
compute:
  - architecture: amd64
    hyperthreading: Enabled
    name: worker
    platform: {}
    replicas: 0
arbiter: <1>
  architecture: amd64
  hyperthreading: Enabled
  replicas: 1 <2>
  name: arbiter <3>
  platform:
    baremetal: {}
controlPlane: <4>
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    baremetal: {}
  replicas: 2 <5>
platform:
  baremetal:
# ...
    hosts:
      - name: cluster-master-0
        role: master
# ...
      - name: cluster-master-1
        role: master
        ...
      - name: cluster-arbiter-0
        role: arbiter
# ...
----
<1> Defines the arbiter machine pool. You must configure this field to deploy a cluster with an arbiter node.
<2> Set the `replicas` field to `1` for the arbiter pool. You cannot set this field to a value that is greater than 1.
<3> Specifies a name for the arbiter machine pool.
<4> Defines the control plane machine pool.
<5> When an arbiter pool is defined, two control plane replicas are valid.

. Save the modified `install-config.yaml` file.

// Verifying that the current installation host can pull release images
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-tui_{context}"]
= Verifying that the current installation host can pull release images

[role="_abstract"]
After you boot the agent image and network services are made available to the host, the agent console application performs a pull check to verify that the current host can retrieve release images.

If the primary pull check passes, you can quit the application to continue with the installation. If the pull check fails, the application performs additional checks, as seen in the `Additional checks` section of the TUI, to help you troubleshoot the problem. A failure for any of the additional checks is not necessarily critical as long as the primary pull check succeeds.

If there are host network configuration issues that might cause an installation to fail, you can use the console application to make adjustments to your network configurations.

[IMPORTANT]
====
If the agent console application detects host network configuration issues, the installation workflow will be halted until the user manually stops the console application and signals the intention to proceed.
====

.Procedure

. Wait for the agent console application to check whether or not the configured release image can be pulled from a registry.

. If the agent console application states that the installer connectivity checks have passed, wait for the prompt to time out to continue with the installation.
+
[NOTE]
====
You can still choose to view or change network configuration settings even if the connectivity checks have passed.

However, if you choose to interact with the agent console application rather than letting it time out, you must manually quit the TUI to proceed with the installation.
====

. If the agent console application checks have failed, which is indicated by a red icon beside the `Release image URL` pull check, use the following steps to reconfigure the host's network settings:

.. Read the `Check Errors` section of the TUI.
This section displays error messages specific to the failed checks.
+
image::agent-tui-home.png[The home screen of the agent console application  displaying check errors, indicating a failed check]

.. Select *Configure network* to launch the NetworkManager TUI.

.. Select *Edit a connection* and select the connection you want to reconfigure.

.. Edit the configuration and select *OK* to save your changes.

.. Select *Back* to return to the main screen of the NetworkManager TUI.

.. Select *Activate a Connection*.

.. Select the reconfigured network to deactivate it.

.. Select the reconfigured network again to reactivate it.

.. Select *Back* and then select *Quit* to return to the agent console application.

.. Wait at least five seconds for the continuous network checks to restart using the new network configuration.

.. If the `Release image URL` pull check succeeds and displays a green icon beside the URL, select *Quit* to exit the agent console application and continue with the installation.

// Tracking and verifying installation progress
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-verify_{context}"]
= Tracking and verifying installation progress

[role=_abstract]
After the installation has started, you can track installation progress and verify a successful installation.

.Prerequisites

* You have configured a DNS record for the Kubernetes API server.

.Procedure

. Optional: To know when the bootstrap host (rendezvous host) reboots, run the following command:
+
--
[source,terminal]
----
$ ./openshift-install --dir <install_directory> agent wait-for bootstrap-complete \
    --log-level=info
----

where:

`--dir`:: specifies the path to the directory where the agent ISO was generated.

`--log-level`:: Specifies the level of installation details. Valid values are `info`, `warn`, `debug`, and `error`.
--
+
.Example output
[source,terminal]
----
...................................................................
...................................................................
INFO Bootstrap configMap status is complete
INFO cluster bootstrap is complete
----
+
The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines.

. Track the progress and verify successful installation by running the following command:
+
[source,terminal]
----
$ openshift-install --dir <install_directory> agent wait-for install-complete <1>
----
+
Replace `<install_directory>` with the path to the directory where the agent ISO was generated.
+
.Example output
[source,terminal]
----
...................................................................
...................................................................
INFO Cluster is installed
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run
INFO     export KUBECONFIG=/home/core/installer/auth/kubeconfig
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.sno-cluster.test.example.com
----

+
[NOTE]
====
If you are using the optional method of {ztp} manifests, you can configure IP address endpoints for cluster nodes through the `AgentClusterInstall.yaml` file in three ways:

* IPv4
* IPv6
* IPv4 and IPv6 in parallel (dual-stack)

IPv6 is supported only on bare metal platforms.
====
+
.Example of dual-stack networking
[source,yaml,subs="attributes+"]
----
apiVIP: 192.168.11.3
ingressVIP: 192.168.11.4
clusterDeploymentRef:
  name: mycluster
imageSetRef:
  name: openshift-
networking:
  clusterNetwork:
  - cidr: 172.21.0.0/16
    hostPrefix: 23
  - cidr: fd02::/48
    hostPrefix: 64
  machineNetwork:
  - cidr: 192.168.11.0/16
  - cidr: 2001:DB8::/32
  serviceNetwork:
  - 172.22.0.0/16
  - fd03::/112
  networkType: OVNKubernetes
----

// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc

[id="sample-ztp-custom-resources_{context}"]
= Sample {ztp} custom resources

[role="_abstract"]
You can optionally use {ztp-first} custom resource (CR) objects to install an OpenShift Container Platform cluster with the Agent-based Installer.

You can customize the following {ztp} custom resources to specify more details about your OpenShift Container Platform cluster. The following sample {ztp} custom resources are for a single-node cluster.

.Example `agent-cluster-install.yaml` file

[source,yaml,subs="attributes+"]
----
  apiVersion: extensions.hive.openshift.io/v1beta1
  kind: AgentClusterInstall
  metadata:
    name: test-agent-cluster-install
    namespace: cluster0
  spec:
    clusterDeploymentRef:
      name: ostest
    imageSetRef:
      name: openshift-
    networking:
      clusterNetwork:
      - cidr: 10.128.0.0/14
        hostPrefix: 23
      serviceNetwork:
      - 172.30.0.0/16
    provisionRequirements:
      controlPlaneAgents: 1
      workerAgents: 0
    sshPublicKey: <ssh_public_key>
----

.Example `cluster-deployment.yaml` file

[source,yaml]
----
apiVersion: hive.openshift.io/v1
kind: ClusterDeployment
metadata:
  name: ostest
  namespace: cluster0
spec:
  baseDomain: test.metalkube.org
  clusterInstallRef:
    group: extensions.hive.openshift.io
    kind: AgentClusterInstall
    name: test-agent-cluster-install
    version: v1beta1
  clusterName: ostest
  controlPlaneConfig:
    servingCertificates: {}
  platform:
    agentBareMetal:
      agentSelector:
        matchLabels:
          bla: aaa
  pullSecretRef:
    name: pull-secret
----

.Example `cluster-image-set.yaml` file

[source,yaml,subs="attributes+"]
----
apiVersion: hive.openshift.io/v1
kind: ClusterImageSet
metadata:
  name: openshift-
spec:
  releaseImage: registry.ci.openshift.org/ocp/release:.0-0.nightly-2022-06-06-025509
----

.Example `infra-env.yaml` file

[source,yaml]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: InfraEnv
metadata:
  name: myinfraenv
  namespace: cluster0
spec:
  clusterRef:
    name: ostest
    namespace: cluster0
  cpuArchitecture: aarch64
  pullSecretRef:
    name: pull-secret
  sshAuthorizedKey: <ssh_public_key>
  nmStateConfigLabelSelector:
    matchLabels:
      cluster0-nmstate-label-name: cluster0-nmstate-label-value
----

.Example `nmstateconfig.yaml` file

[source,yaml]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: NMStateConfig
metadata:
  name: master-0
  namespace: openshift-machine-api
  labels:
    cluster0-nmstate-label-name: cluster0-nmstate-label-value
spec:
  config:
    interfaces:
      - name: eth0
        type: ethernet
        state: up
        mac-address: 52:54:01:aa:aa:a1
        ipv4:
          enabled: true
          address:
            - ip: 192.168.122.2
              prefix-length: 23
          dhcp: false
    dns-resolver:
      config:
        server:
          - 192.168.122.1
    routes:
      config:
        - destination: 0.0.0.0/0
          next-hop-address: 192.168.122.1
          next-hop-interface: eth0
          table-id: 254
  interfaces:
    - name: "eth0"
      macAddress: 52:54:01:aa:aa:a1
----

.Example `pull-secret.yaml` file

[source,yaml]
----
apiVersion: v1
kind: Secret
type: kubernetes.io/dockerconfigjson
metadata:
  name: pull-secret
  namespace: cluster0
stringData:
  .dockerconfigjson: <pull_secret>
----

[role="_additional-resources"]
.Additional resources

* Challenges of the network far edge

// Gathering log data from a failed Agent-based installation
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-gather-log_{context}"]
= Gathering log data from a failed Agent-based installation

[role="_abstract"]
If you encounter a failed Agent-based installation, you can gather log data to provide for a support case.

.Prerequisites

* You have configured a DNS record for the Kubernetes API server.

.Procedure

. Run the following command and collect the output:
+
[source,terminal]
----
$ ./openshift-install --dir <installation_directory> agent wait-for bootstrap-complete --log-level=debug
----
+
.Example error message
[source,terminal]
----
...
ERROR Bootstrap failed to complete: : bootstrap process timed out: context deadline exceeded
----

. If the output from the previous command indicates a failure, or if the bootstrap is not progressing, run the following command to connect to the rendezvous host and collect the output:
+
[source,terminal]
----
$ ssh core@<node-ip> agent-gather -O >agent-gather.tar.xz
----
+
[NOTE]
====
Red{nbsp}Hat Support can diagnose most issues using the data gathered from the rendezvous host, but if some hosts are not able to register, gathering this data from every host might be helpful.
====

. If the bootstrap completes and the cluster nodes reboot, run the following command and collect the output:
+
[source,terminal]
----
$ ./openshift-install --dir <install_directory> agent wait-for install-complete --log-level=debug
----

. If the output from the previous command indicates a failure, perform the following steps:

.. Export the `kubeconfig` file to your environment by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=<install_directory>/auth/kubeconfig
----

.. Gather information for debugging by running the following command:
+
[source,terminal]
----
$ oc adm must-gather
----

.. Create a compressed file from the `must-gather` directory that was just created in your working directory by running the following command:
+
[source,terminal]
----
$ tar cvaf must-gather.tar.gz <must_gather_directory>
----

. Excluding the `/auth` subdirectory, attach the installation directory used during the deployment to your support case on the Red{nbsp}Hat Customer Portal.

. Attach all other data gathered from this procedure to your support case.
