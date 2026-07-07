---
title: "Preparing PXE assets for {product-title}"
type: reference
domain: openshift
slug: installing-4-22-prepare-pxe-assets-agent
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/prepare-pxe-assets-agent
version: 4.22
family: installing
documentKind: "Documentation"
---

# Preparing PXE assets for {product-title}

[id="prepare-pxe-assets-agent"]
= Preparing PXE assets for OpenShift Container Platform

[role="_abstract"]
You can create the assets needed to PXE boot an OpenShift Container Platform cluster by using the Agent-based Installer.

The assets you create in these procedures will deploy a single-node OpenShift Container Platform installation. You can use these procedures as a basis and modify configurations according to your requirements.

See "Installing an OpenShift Container Platform cluster with the Agent-based Installer" to learn about more configurations available with the Agent-based Installer.

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
* Creating additional manifest files

// Creating the PXE assets
// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/prepare-pxe-assets-agent.adoc

[id="pxe-assets-ocp-agent_{context}"]
= Creating the PXE assets

[role="_abstract"]
Create the assets and optional script to implement in your PXE infrastructure.

.Procedure

. Create the PXE assets by running the following command:
+
[source,terminal]
----
$ openshift-install agent create pxe-files
----
+
The generated PXE assets and optional iPXE script can be found in the `boot-artifacts` directory.
+
.Example filesystem with PXE assets and optional iPXE script
[source,terminal]
----
boot-artifacts
    ├─ agent.x86_64-initrd.img
    ├─ agent.x86_64.ipxe
    ├─ agent.x86_64-rootfs.img
    └─ agent.x86_64-vmlinuz
----
+
[IMPORTANT]
====
The contents of the `boot-artifacts` directory vary depending on the specified architecture.
====
+
[NOTE]
====
{op-system-first} supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the Agent ISO image, with a default `/etc/multipath.conf` configuration.
====

. Upload the PXE assets and optional script to your infrastructure where they will be accessible during the boot process.
+
[NOTE]
====
If you generated an iPXE script, the location of the assets must match the `bootArtifactsBaseURL` value you added to the `agent-config.yaml` file.
====

// Manually adding IBM Z agents
// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/prepare-pxe-infra-agent.adoc

[id="installing-ocp-agent-ibm-z_{context}"]
= Manually adding {ibm-z-title} agents

[role="_abstract"]
After creating the PXE assets, you can add {ibm-z-name} agents.

Only use this procedure for {ibm-z-name} clusters.

Depending on your {ibm-z-name} environment, you can choose from the following options:

* Adding {ibm-z-name} agents with z/VM
* Adding {ibm-z-name} agents with {op-system-base} KVM
* Adding {ibm-z-name} agents with Logical Partition (LPAR)

[NOTE]
====
Currently, ISO boot support on {ibm-z-name} (`s390x`) is available only for {op-system-base-full} KVM, which provides the flexibility to choose either PXE or ISO-based installation. For installations with z/VM and Logical Partition (LPAR), only PXE boot is supported.
====

[id="networking-reqs-ibm-z_{context}"]
== Networking requirements for {ibm-z-title}

In {ibm-z-title} environments, advanced networking technologies such as Open Systems Adapter (OSA), HiperSockets, and Remote Direct Memory Access (RDMA) over Converged Ethernet (RoCE) require specific configurations that deviate from the standard network settings and those needs to be persisted for multiple boot scenarios that occur in the Agent-based Installation.

To persist these parameters during boot, the `ai.ip_cfg_override=1` parameter is required in the `.parm` file. This parameter is used with the configured network cards to ensure a successful and efficient deployment on {ibm-z-title}.

The following table lists the network devices that are supported on each hypervisor for the network configuration override functionality:

[cols="3,2,2,2,2", options="header"]
|====
| Network device
| z/VM
| KVM
| LPAR Classic
| LPAR Dynamic Partition Manager (DPM)

| Virtual Switch
| Supported ^[1]^
| Not applicable ^[2]^
| Not applicable
| Not applicable

| Direct attached Open Systems Adapter (OSA)
| Supported
| Not required ^[3]^
| Supported
| Not required

| RDMA over Converged Ethernet (RoCE)
| Not required
| Not required
| Not required
| Not required

| HiperSockets
| Supported
| Not required
| Supported
| Not required
|====
. Supported: When the `ai.ip_cfg_override` parameter is required for the installation procedure.
. Not Applicable: When a network card is not applicable to be used on the hypervisor.
. Not required: When the `ai.ip_cfg_override` parameter is not required for the installation procedure.

// Configuring network overrides in {ibm-z-title}
// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/prepare-pxe-assets-agent.adoc
[id="configuring-network-overrides-ibm_{context}"]
= Configuring network overrides in an {ibm-z-title} environment

[role="_abstract"]
You can specify a static IP address on {ibm-z-title} machines that use Logical Partition (LPAR) and z/VM. This is useful when the network devices do not have a static MAC address assigned to them.

[NOTE]
====
If you are using an OSA network device in Processor Resource/Systems Manager (PR/SM) mode, the lack of persistent MAC addresses can lead to a dynamic assignment of roles for nodes. This means that the roles of individual nodes are not fixed and can change, as the system is unable to reliably associate specific MAC addresses with designated node roles. If MAC addresses are not persistent for any of the interfaces, roles for the nodes are assigned randomly during Agent-based installation.
====

.Procedure

* If you have an existing `.parm` file, edit it to include the following entry:
+
[source,terminal]
----
ai.ip_cfg_override=1
----
+
This parameter allows the file to add the network settings to the {op-system-first} installer.
+
[NOTE]
====
The `override` parameter overrides the host's network configuration settings.
====
+
--
.Example `.parm` file
[source,terminal]
----
rd.neednet=1 cio_ignore=all,!condev
console=ttysclp0
coreos.live.rootfs_url=<coreos_url>
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns>
rd.znet=qeth,<network_adaptor_range>,layer2=1
rd.<disk_type>=<adapter>
rd.zfcp=<adapter>,<wwpn>,<lun> random.trust_cpu=on
zfcp.allow_lun_scan=0
ai.ip_cfg_override=1
ignition.firstboot ignition.platform.id=metal
random.trust_cpu=on
----
* For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are booting. Only HTTP and HTTPS protocols are supported.

* For installations on direct access storage devices (DASD) type disks, use `rd.` to specify the DASD where {op-system-first} is to be installed. For installations on Fibre Channel Protocol (FCP) disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where {op-system} is to be installed.
* Specify values for `<adapter>`, `<wwpn>`, and `<lun>` as in the following example: `rd.zfcp=0.0.8002,0x500507630400d1e3,0x4000404600000000`.
--
+
[IMPORTANT]
====
The `ip=` kernel parameter uses the following syntax:

`ip=[IP]:[Gateway]:[Netmask]:[Hostname]:[Interface]:[None]:[DNS]`

For VLAN configurations:

* Define both the **base interface** and the **tagged VLAN interface** separately.
* The `vlan=` parameter links the tagged interface (for example, `encbdf0.300`) to the underlying physical interface (`encbdf0`).

For bonded interfaces:

* No changes are required in the default kernel command-line parameters.
* To install nodes by using bonded interfaces, provide the appropriate bond configuration in the `agent-config` file.
====

// Adding {ibm-z-title} agents with z/VM
// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/prepare-pxe-infra-agent.adoc

[id="installing-ocp-agent-ibm-z-zvm_{context}"]
= Adding {ibm-z-title} agents with z/VM

[role="_abstract"]
You can manually add {ibm-z-name} agents with z/VM.

Only use this procedure for {ibm-z-name} clusters with z/VM.

.Prerequisites

* You have a running file server with access to the guest virtual machines (VMs).

.Procedure

. Create a parameter file for the z/VM guest:
+
--
.Example parameter file
[source,text]
----
rd.neednet=1 \
console=ttysclp0 \
coreos.live.rootfs_url=<rootfs_url> \
ip=172.18.78.2::172.18.78.1:255.255.255.0:::none nameserver=172.18.78.1 \
zfcp.allow_lun_scan=0 \
ai.ip_cfg_override=1 \
rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
rd.dasd=0.0.4411 \
rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
fips=1 \
random.trust_cpu=on rd.luks.options=discard \
ignition.firstboot ignition.platform.id=metal \
console=tty1 console=ttyS1,115200n8 \
coreos.inst.persistent-kargs="console=tty1 console=ttyS1,115200n8"
----
* For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are booting. Only HTTP and HTTPS protocols are supported.
* For the `ip` parameter, assign the IP address automatically using DHCP, or manually assign the IP address, as described in "Installing a cluster with z/VM on {ibm-z-name} and {ibm-linuxone-name}".
* The default for `zfcp.allow_lun_scan` is `1`. Omit this entry when using an OSA network adapter.
* For installations on DASD-type disks, use `rd.dasd` to specify the DASD where {op-system-first} is to be installed. Omit this entry for FCP-type disks.
* For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where {op-system} is to be installed. Omit this entry for DASD-type disks.
+
[NOTE]
====
For FCP multipath configurations, provide available multiple paths to the disk instead of a single path, and add `rd.multipath=default` to enable multipath during installation.
====
+
.Example
[source,text]
----
rd.zfcp=<adapter1>,<wwpn1>,<lun1> \
rd.zfcp=<adapter2>,<wwpn2>,<lun2> \
rd.multipath=default
----
* To enable FIPS mode, specify `fips=1`. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file.
--
+
Leave all other parameters unchanged.

. Punch the `kernel.img`,`generic.parm`, and `initrd.img` files to the virtual reader of the z/VM guest virtual machine.
+
For more information, see PUNCH ({ibm-title} Documentation).
+
[TIP]
====
You can use the `CP PUNCH` command or, if you use Linux, the `vmur` command, to transfer files between two z/VM guest virtual machines.
====
+
. Log in to the conversational monitor system (CMS) on the bootstrap machine.

. IPL the bootstrap machine from the reader by running the following command:
+
[source,terminal]
----
$ ipl c
----
+
For more information, see IPL ({ibm-title} Documentation).

[role="_additional-resources"]
.Additional resources

* Installing a cluster with z/VM on {ibm-z-title} and {ibm-linuxone-title}

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

[role="_additional-resources"]
.Additional resources

* Installing a cluster with {op-system-base} KVM on {ibm-z-title} and {ibm-linuxone-title}

// Adding {ibm-z-title} Logical Partition (LPAR) as agents
// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/prepare-pxe-infra-agent.adoc

[id="adding-ibm-z-lpar-agents_{context}"]
= Adding {ibm-z-title} agents in a Logical Partition (LPAR)

[role="_abstract"]
You can manually add {ibm-z-name} agents to your cluster that runs in an LPAR environment.

Use this procedure only for {ibm-z-name} clusters running in an LPAR.

.Prerequisites
* You have Python 3 installed.
* You have a running file server with access to the Logical Partition (LPAR).

.Procedure

. Create a boot parameter file for the agents.
+
--
.Example parameter file
[source,terminal]
----
rd.neednet=1 cio_ignore=all,!condev \
console=ttysclp0 \
ignition.firstboot ignition.platform.id=metal
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
coreos.inst.persistent-kargs=console=ttysclp0 \
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,<network_adaptor_range>,layer2=1
rd.<disk_type>=<adapter> \
fips=1 \
zfcp.allow_lun_scan=0 \
ai.ip_cfg_override=1 \
random.trust_cpu=on rd.luks.options=discard
----
* For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are starting. Only HTTP and HTTPS protocols are supported.
* For the `ip` parameter, manually assign the IP address, as described in "Installing a cluster with z/VM on {ibm-z-title} and {ibm-linuxone-title}".
* For installations on DASD-type disks, use `rd.dasd` to specify the DASD where {op-system-first} is to be installed. For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where {op-system} is to be installed.
+
[NOTE]
====
For FCP multipath configurations, provide available multiple paths to the disk instead of a single path, and add `rd.multipath=default` to enable multipath during installation.
====
+
.Example
[source,terminal]
----
rd.zfcp=<adapter1>,<wwpn1>,<lun1> \
rd.zfcp=<adapter2>,<wwpn2>,<lun2> \
rd.multipath=default
----
+
* To enable FIPS mode, specify `fips=1`. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file.
+
[NOTE]
====
The `.ins` and `initrd.img.addrsize` files are automatically generated for `s390x` architecture as part of boot-artifacts from the installation program and are only used when booting in an LPAR environment.
====
+
.Example filesystem with LPAR boot
[source,terminal]
----
boot-artifacts
    ├─ agent.s390x-generic.ins
    ├─ agent.s390x-initrd.addrsize
    ├─ agent.s390x-rootfs.img
    └─ agent.s390x-kernel.img
    └─ agent.s390x-rootfs.img
----
--

. Rename the `boot-artifacts` file present in the `generic.ins` parameter file to match the names of the `boot-artifacts` file generated by the installation program.

. Transfer the `initrd`, `kernel`, `generic.ins`, and `initrd.img.addrsize` parameter files to the file server. For more information, see Booting Linux in LPAR mode (IBM documentation).

. Start the machine.

. Repeat the procedure for all other machines in the cluster.

[role="_additional-resources"]
.Additional resources

* Installing a cluster in an LPAR on {ibm-z-title} and {ibm-linuxone-title}

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Installing an OpenShift Container Platform cluster with the Agent-based Installer
