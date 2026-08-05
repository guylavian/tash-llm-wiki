---
title: "Setting up the environment for an {product-title} installation"
type: reference
domain: openshift
slug: installing-4-22-install-ibm-cloud-installation-workflow
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/install-ibm-cloud-installation-workflow
version: 4.22
family: installing
documentKind: "Documentation"
---

# Setting up the environment for an {product-title} installation

[id="install-ibm-cloud-installation-workflow"]
= Setting up the environment for an OpenShift Container Platform installation

// Module included in the following assemblies:
//
// * installing/installing_ibm_cloud_classic/install-ibm-cloud-installing-on-ibm-cloud.adoc
//
// As of Dec. 6, 2024, the following link does not have a variable defined. Link is located in the Red Hat Subscription Manager Note on line 66. Please update link to use a defined variable when available:
// https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/basic-reg-rhel-cli

[id="preparing-the-provisioner-node-for-openshift-install-on-ibm-cloud_{context}"]
= Preparing the provisioner node on {ibm-cloud-bm} infrastructure

Perform the following steps to prepare the provisioner node.

.Procedure

. Log in to the provisioner node via `ssh`.

. Create a non-root user (`kni`) and provide that user with `sudo` privileges:
+
[source,terminal]
----
# useradd kni
----
+
[source,terminal]
----
# passwd kni
----
+
[source,terminal]
----
# echo "kni ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/kni
----
+
[source,terminal]
----
# chmod 0440 /etc/sudoers.d/kni
----

. Create an `ssh` key for the new user:
+
[source,terminal]
----
# su - kni -c "ssh-keygen -f /home/kni/.ssh/id_rsa -N ''"
----

. Log in as the new user on the provisioner node:
+
[source,terminal]
----
# su - kni
----

. Use Red Hat Subscription Manager to register the provisioner node:
+
[source,terminal]
----
$ sudo subscription-manager register --username=<user> --password=<pass> --auto-attach
----
+
[source,terminal]
----
$ sudo subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms \
                                  --enable=rhel-8-for-x86_64-baseos-rpms
----
+
[NOTE]
====
For more information about Red Hat Subscription Manager, see Registering a {op-system-base} system with command-line tools.
====

. Install the following packages:
+
[source,terminal]
----
$ sudo dnf install -y libvirt qemu-kvm mkisofs python3-devel jq ipmitool
----

. Modify the user to add the `libvirt` group to the newly created user:
+
[source,terminal]
----
$ sudo usermod --append --groups libvirt kni
----

. Start `firewalld`:
+
[source,terminal]
----
$ sudo systemctl start firewalld
----

. Enable `firewalld`:
+
[source,terminal]
----
$ sudo systemctl enable firewalld
----

. Start the `http` service:
+
[source,terminal]
----
$ sudo firewall-cmd --zone=public --add-service=http --permanent
----
+
[source,terminal]
----
$ sudo firewall-cmd --reload
----

. Start and enable the `libvirtd` service:
+
[source,terminal]
----
$ sudo systemctl enable libvirtd --now
----

. Set the ID of the provisioner node:
+
[source,terminal]
----
$ PRVN_HOST_ID=<ID>
----
+
You can view the ID with the following `ibmcloud` command:
+
[source,terminal]
----
$ ibmcloud sl hardware list
----

. Set the ID of the public subnet:
+
[source,terminal]
----
$ PUBLICSUBNETID=<ID>
----
+
You can view the ID with the following `ibmcloud` command:
+
[source,terminal]
----
$ ibmcloud sl subnet list
----

. Set the ID of the private subnet:
+
[source,terminal]
----
$ PRIVSUBNETID=<ID>
----
+
You can view the ID with the following `ibmcloud` command:
+
[source,terminal]
----
$ ibmcloud sl subnet list
----

. Set the provisioner node public IP address:
+
[source,terminal]
----
$ PRVN_PUB_IP=$(ibmcloud sl hardware detail $PRVN_HOST_ID --output JSON | jq .primaryIpAddress -r)
----

. Set the CIDR for the public network:
+
[source,terminal]
----
$ PUBLICCIDR=$(ibmcloud sl subnet detail $PUBLICSUBNETID --output JSON | jq .cidr)
----

. Set the IP address and CIDR for the public network:
+
[source,terminal]
----
$ PUB_IP_CIDR=$PRVN_PUB_IP/$PUBLICCIDR
----

. Set the gateway for the public network:
+
[source,terminal]
----
$ PUB_GATEWAY=$(ibmcloud sl subnet detail $PUBLICSUBNETID --output JSON | jq .gateway -r)
----

. Set the private IP address of the provisioner node:
+
[source,terminal]
----
$ PRVN_PRIV_IP=$(ibmcloud sl hardware detail $PRVN_HOST_ID --output JSON | \
                 jq .primaryBackendIpAddress -r)
----

. Set the CIDR for the private network:
+
[source,terminal]
----
$ PRIVCIDR=$(ibmcloud sl subnet detail $PRIVSUBNETID --output JSON | jq .cidr)
----

. Set the IP address and CIDR for the private network:
+
[source,terminal]
----
$ PRIV_IP_CIDR=$PRVN_PRIV_IP/$PRIVCIDR
----

. Set the gateway for the private network:
+
[source,terminal]
----
$ PRIV_GATEWAY=$(ibmcloud sl subnet detail $PRIVSUBNETID --output JSON | jq .gateway -r)
----

. Set up the bridges for the `baremetal` and `provisioning` networks:
+
[source,terminal]
----
$ sudo nohup bash -c "
    nmcli --get-values UUID con show | xargs -n 1 nmcli con delete
    nmcli connection add ifname provisioning type bridge con-name provisioning
    nmcli con add type bridge-slave ifname eth1 master provisioning
    nmcli connection add ifname baremetal type bridge con-name baremetal
    nmcli con add type bridge-slave ifname eth2 master baremetal
    nmcli connection modify baremetal ipv4.addresses $PUB_IP_CIDR ipv4.method manual ipv4.gateway $PUB_GATEWAY
    nmcli connection modify provisioning ipv4.addresses 172.22.0.1/24,$PRIV_IP_CIDR ipv4.method manual
    nmcli connection modify provisioning +ipv4.routes \"10.0.0.0/8 $PRIV_GATEWAY\"
    nmcli con down baremetal
    nmcli con up baremetal
    nmcli con down provisioning
    nmcli con up provisioning
    init 6
"
----
+
[NOTE]
====
For `eth1` and `eth2`, substitute the appropriate interface name, as needed.
====

. If required, SSH back into the `provisioner` node:
+
[source,terminal]
----
# ssh kni@provisioner.<cluster-name>.<domain>
----

. Verify the connection bridges have been properly created:
+
[source,terminal]
----
$ sudo nmcli con show
----
+
.Example output
[source,terminal]
----
NAME               UUID                                  TYPE      DEVICE
baremetal          4d5133a5-8351-4bb9-bfd4-3af264801530  bridge    baremetal
provisioning       43942805-017f-4d7d-a2c2-7cb3324482ed  bridge    provisioning
virbr0             d9bca40f-eee1-410b-8879-a2d4bb0465e7  bridge    virbr0
bridge-slave-eth1  76a8ed50-c7e5-4999-b4f6-6d9014dd0812  ethernet  eth1
bridge-slave-eth2  f31c3353-54b7-48de-893a-02d2b34c4736  ethernet  eth2
----

. Create a `pull-secret.txt` file:
+
[source,terminal]
----
$ vim pull-secret.txt
----
+
In a web browser, navigate to Install on Bare Metal with user-provisioned infrastructure. In step 1, click **Download pull secret**. Paste the contents into the `pull-secret.txt` file and save the contents in the `kni` user's home directory.

// This is included in the following assemblies:
//
// installing_ibm_cloud_classic/install-ibm-cloud-installing-on-ibm-cloud.adoc

[id="configuring-the-public-subnet_{context}"]
= Configuring the public subnet

All of the OpenShift Container Platform cluster nodes must be on the public subnet. {ibm-cloud-bm} does not provide a DHCP server on the subnet. Set it up separately on the provisioner node.

You must reset the BASH variables defined when preparing the provisioner node. Rebooting the provisioner node after preparing it will delete the BASH variables previously set.

.Procedure

. Install `dnsmasq`:
+
[source,terminal]
----
$ sudo dnf install dnsmasq
----

. Open the `dnsmasq` configuration file:
+
[source,terminal]
----
$ sudo vi /etc/dnsmasq.conf
----

. Add the following configuration to the `dnsmasq` configuration file:
+
[source,text]
----
interface=baremetal
except-interface=lo
bind-dynamic
log-dhcp

dhcp-range=<ip_addr>,<ip_addr>,<pub_cidr> <1>
dhcp-option=baremetal,121,0.0.0.0/0,<pub_gateway>,<prvn_priv_ip>,<prvn_pub_ip> <2>

dhcp-hostsfile=/var/lib/dnsmasq/dnsmasq.hostsfile
----
+
<1> Set the DHCP range. Replace both instances of `<ip_addr>` with one unused IP address from the public subnet so that the `dhcp-range` for the `baremetal` network begins and ends with the same the IP address. Replace `<pub_cidr>` with the CIDR of the public subnet.
+
<2> Set the DHCP option. Replace `<pub_gateway>` with the IP address of the gateway for the `baremetal` network. Replace `<prvn_priv_ip>` with the IP address of the provisioner node's private IP address on the `provisioning` network. Replace `<prvn_pub_ip>` with the IP address of the provisioner node's public IP address on the `baremetal` network.
+
To retrieve the value for `<pub_cidr>`, execute:
+
[source,terminal]
----
$ ibmcloud sl subnet detail <publicsubnetid> --output JSON | jq .cidr
----
+
Replace `<publicsubnetid>` with the ID of the public subnet.
+
To retrieve the value for `<pub_gateway>`, execute:
+
[source,terminal]
----
$ ibmcloud sl subnet detail <publicsubnetid> --output JSON | jq .gateway -r
----
+
Replace `<publicsubnetid>` with the ID of the public subnet.
+
To retrieve the value for `<prvn_priv_ip>`, execute:
+
[source,terminal]
----
$ ibmcloud  sl hardware detail <id> --output JSON | \
            jq .primaryBackendIpAddress -r
----
+
Replace `<id>` with the ID of the provisioner node.
+
To retrieve the value for `<prvn_pub_ip>`, execute:
+
[source,terminal]
----
$ ibmcloud sl hardware detail <id> --output JSON | jq .primaryIpAddress -r
----
+
Replace `<id>` with the ID of the provisioner node.

. Obtain the list of hardware for the cluster:
+
[source,terminal]
----
$ ibmcloud sl hardware list
----

. Obtain the MAC addresses and IP addresses for each node:
+
[source,terminal]
----
$ ibmcloud sl hardware detail <id> --output JSON | \
  jq '.networkComponents[] | \
  "\(.primaryIpAddress) \(.macAddress)"' | grep -v null
----
+
Replace `<id>` with the ID of the node.
+
.Example output
[source,terminal]
----
"10.196.130.144 00:e0:ed:6a:ca:b4"
"141.125.65.215 00:e0:ed:6a:ca:b5"
----
+
Make a note of the MAC address and IP address of the public network. Make a separate note of the MAC address of the private network, which you will use later in the `install-config.yaml` file. Repeat this procedure for each node until you have all the public MAC and IP addresses for the public `baremetal` network, and the MAC addresses of the private `provisioning` network.

. Add the MAC and IP address pair of the public `baremetal` network for each node into the `dnsmasq.hostsfile` file:
+
[source,terminal]
----
$ sudo vim /var/lib/dnsmasq/dnsmasq.hostsfile
----
+
.Example input
[source,text]
----
00:e0:ed:6a:ca:b5,141.125.65.215,master-0
<mac>,<ip>,master-1
<mac>,<ip>,master-2
<mac>,<ip>,worker-0
<mac>,<ip>,worker-1
...
----
+
Replace `<mac>,<ip>` with the public MAC address and public IP address of the corresponding node name.

. Start `dnsmasq`:
+
[source,terminal]
----
$ sudo systemctl start dnsmasq
----

. Enable `dnsmasq` so that it starts when booting the node:
+
[source,terminal]
----
$ sudo systemctl enable dnsmasq
----

. Verify `dnsmasq` is running:
+
[source,terminal]
----
$ sudo systemctl status dnsmasq
----
+
.Example output
[source,terminal]
----
● dnsmasq.service - DNS caching server.
Loaded: loaded (/usr/lib/systemd/system/dnsmasq.service; enabled; vendor preset: disabled)
Active: active (running) since Tue 2021-10-05 05:04:14 CDT; 49s ago
Main PID: 3101 (dnsmasq)
Tasks: 1 (limit: 204038)
Memory: 732.0K
CGroup: /system.slice/dnsmasq.service
└─3101 /usr/sbin/dnsmasq -k
----

. Open ports `53` and `67` with UDP protocol:
+
[source,terminal]
----
$ sudo firewall-cmd --add-port 53/udp --permanent
----
+
[source,terminal]
----
$ sudo firewall-cmd --add-port 67/udp --permanent
----

. Add `provisioning` to the external zone with masquerade:
+
[source,terminal]
----
$ sudo firewall-cmd --change-zone=provisioning --zone=external --permanent
----
+
This step ensures network address translation for IPMI calls to the management subnet.

. Reload the `firewalld` configuration:
+
[source,terminal]
----
$ sudo firewall-cmd --reload
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc

[id="retrieving-the-openshift-installer_{context}"]
= Retrieving the OpenShift Container Platform installer

Use the `stable-4.x` version of the installation program and your selected architecture to deploy the generally available stable version of OpenShift Container Platform:

[source,terminal,subs="attributes+"]
----
$ export VERSION=stable-
----
[source,terminal,subs="attributes+"]
----
$ export RELEASE_ARCH=<architecture>
----
[source,terminal,subs="attributes+"]
----
$ export RELEASE_IMAGE=$(curl -s https://mirror.openshift.com/pub/openshift-v4/$RELEASE_ARCH/clients/ocp/$VERSION/release.txt | grep 'Pull From: quay.io' | awk -F ' ' '{print $3}')
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc

[id="extracting-the-openshift-installer_{context}"]
= Extracting the OpenShift Container Platform installer

After retrieving the installer, the next step is to extract it.

.Procedure

. Set the environment variables:
+
[source,terminal]
----
$ export cmd=openshift-baremetal-install
----
+
[source,terminal]
----
$ export pullsecret_file=~/pull-secret.txt
----
+
[source,terminal]
----
$ export extract_dir=$(pwd)
----

. Get the `oc` binary:
+
[source,terminal]
----
$ curl -s https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$VERSION/openshift-client-linux.tar.gz | tar zxvf - oc
----

. Extract the installer:
+
[source,terminal]
----
$ sudo cp oc /usr/local/bin
----
+
[source,terminal]
----
$ oc adm release extract --registry-config "${pullsecret_file}" --command=$cmd --to "${extract_dir}" ${RELEASE_IMAGE}
----
+
[source,terminal]
----
$ sudo cp openshift-baremetal-install /usr/local/bin
----

// This is included in the following assemblies:
//
// installing_ibm_cloud_classic/install-ibm-cloud-installing-on-ibm-cloud.adoc

[id="configuring-the-install-config-file_{context}"]
= Configuring the install-config.yaml file

The `install-config.yaml` file requires some additional details. Most of the information is teaching the installer and the resulting cluster enough about the available {ibm-cloud-bm} hardware so that it is able to fully manage it. The material difference between installing on bare metal and installing on {ibm-cloud-bm} is that you must explicitly set the privilege level for IPMI in the BMC section of the `install-config.yaml` file.

.Procedure

. Configure `install-config.yaml`. Change the appropriate variables to match the environment, including `pullSecret` and `sshKey`.
+
[source,yaml]
----
apiVersion: v1
baseDomain: <domain>
metadata:
  name: <cluster_name>
networking:
  machineNetwork:
  - cidr: <public-cidr>
  networkType: OVNKubernetes
compute:
- name: worker
  replicas: 2
controlPlane:
  name: master
  replicas: 3
  platform:
    baremetal: {}
platform:
  baremetal:
    apiVIP: <api_ip>
    ingressVIP: <wildcard_ip>
    provisioningNetworkInterface: <NIC1>
    provisioningNetworkCIDR: <CIDR>
    hosts:
      - name: openshift-master-0
        role: master
        bmc:
          address: ipmi://10.196.130.145?privilegelevel=OPERATOR <1>
          username: root
          password: <password>
        bootMACAddress: 00:e0:ed:6a:ca:b4 <2>
        rootDeviceHints:
          deviceName: "/dev/sda"
      - name: openshift-worker-0
        role: worker
        bmc:
          address: ipmi://<out-of-band-ip>?privilegelevel=OPERATOR <1>
          username: <user>
          password: <password>
        bootMACAddress: <NIC1_mac_address> <2>
        rootDeviceHints:
          deviceName: "/dev/sda"
pullSecret: '<pull_secret>'
sshKey: '<ssh_pub_key>'
----
+
<1> The `bmc.address` provides a `privilegelevel` configuration setting with the value set to `OPERATOR`. This is required for {ibm-cloud-bm} infrastructure.
<2> Add the MAC address of the private `provisioning` network NIC for the corresponding node.
+
[NOTE]
====
You can use the `ibmcloud` command-line utility to retrieve the password.

[source,terminal]
----
$ ibmcloud sl hardware detail <id> --output JSON | \
  jq '"(.networkManagementIpAddress) (.remoteManagementAccounts[0].password)"'
----

Replace `<id>` with the ID of the node.
====

. Create a directory to store the cluster configuration:
+
[source,terminal]
----
$ mkdir ~/clusterconfigs
----

. Copy the `install-config.yaml` file into the directory:
+
[source,terminal]
----
$ cp install-config.yaml ~/clusterconfigs
----

. Ensure all bare metal nodes are powered off prior to installing the OpenShift Container Platform cluster:
+
[source,terminal]
----
$ ipmitool -I lanplus -U <user> -P <password> -H <management_server_ip> power off
----

. Remove old bootstrap resources if any are left over from a previous deployment attempt:
+
[source,bash]
----
for i in $(sudo virsh list | tail -n +3 | grep bootstrap | awk {'print $2'});
do
  sudo virsh destroy $i;
  sudo virsh undefine $i;
  sudo virsh vol-delete $i --pool $i;
  sudo virsh vol-delete $i.ign --pool $i;
  sudo virsh pool-destroy $i;
  sudo virsh pool-undefine $i;
done
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc

[id="additional-install-config-parameters_{context}"]
= Additional installation configuration parameters

[role="_abstract"]
Some parameters, such as the cluster domain name, are required in the `install-config.yaml` file when installing a cluster on bare metal. Others, such as the provisioning network CIDR, are optional.

[cols="4,1,5"]
[options="header"]
.Required parameters
|===
|Parameters |Default |Description

| `baseDomain`
|
| The domain name for the cluster. For example, `example.com`.

| `bootMode`
| `UEFI`
a| The boot mode for a node. Options are `legacy`, `UEFI`, and `UEFISecureBoot`. If `bootMode` is not set, Ironic sets it while inspecting the node.

[NOTE]
====
For hardware that implements `BootMode` read-only, such as HP or Cisco, do not leave this parameter blank. You must manually set the system to UEFI mode before installation and explicitly set this parameter to UEFI.
====
a|
----
platform:
  baremetal:
    bootstrapExternalStaticDNS
----
|
| The static network DNS of the bootstrap node. You must set this value when deploying a cluster with static IP addresses when there is no Dynamic Host Configuration Protocol (DHCP) server on the bare-metal network. If you do not set this value, the installation program will use the value from `bootstrapExternalStaticGateway`, which causes problems when the IP address values of the gateway and DNS are different.

a|
----
platform:
  baremetal:
    bootstrapExternalStaticIP
----
|
| The static IP address for the bootstrap VM. You must set this value when deploying a cluster with static IP addresses when there is no DHCP server on the bare metal network.

a|
----
platform:
  baremetal:
    bootstrapExternalStaticGateway
----
|
| The static IP address of the gateway for the bootstrap VM. You must set this value when deploying a cluster with static IP addresses when there is no DHCP server on the bare metal network.

| `sshKey`
|
| The `sshKey` parameter sets the key in the `~/.ssh/id_rsa.pub` file required to access the control plane nodes and compute nodes. Typically, this key is from the `provisioner` node.

| `pullSecret`
|
| The `pullSecret` parameter sets a copy of the pull secret downloaded from the Install OpenShift on Bare Metal page when preparing the provisioner node.

a|
----
metadata:
    name:
----
|
|The OpenShift Container Platform cluster name. For example, `openshift`.

a|
----
networking:
    machineNetwork:
    - cidr:
----
|
|The public CIDR (Classless Inter-Domain Routing) of the external network. For example, `10.0.0.0/24`.

a|
----
compute:
  - name: worker
----
|
|The OpenShift Container Platform cluster requires a name for each compute node even if there are zero nodes.

a|
----
compute:
    replicas: 2
----
|
|Replicas sets the number of compute nodes in the OpenShift Container Platform cluster.

a|
----
controlPlane:
    name: master
----
|
|The OpenShift Container Platform cluster requires a name for control plane nodes.

a|
----
controlPlane:
    replicas: 3
----
|
|Replicas sets the number of control plane nodes included as part of the OpenShift Container Platform cluster.

a| `provisioningNetworkInterface` |  | The name of the network interface on nodes connected to the provisioning network. For OpenShift Container Platform 4.9 and later releases, use the `bootMACAddress` parameter to enable Ironic to identify the IP address of the NIC instead of using the `provisioningNetworkInterface` parameter to identify the name of the NIC.

| `defaultMachinePlatform` | | The default configuration used for machine pools without a platform configuration.

| `apiVIPs` | a| (Optional) The virtual IP address for Kubernetes API communication.

You must either provide this setting in the `install-config.yaml` file as a reserved IP from the `MachineNetwork` parameter or preconfigured in the DNS so that the default name resolves correctly. Use the virtual IP address and not the FQDN when adding a value to the `apiVIPs` configuration setting in the `install-config.yaml` file. For dual-stack networking, the primary IP address can be either an IPv4 network or an IPv6 network. If not set, the installation program uses `api.<cluster_name>.<base_domain>` to derive the IP address from the DNS.

[NOTE]
====
Before OpenShift Container Platform 4.12, the cluster installation program only accepted an IPv4 address or an IPv6 address for the `apiVIP` parameter. From OpenShift Container Platform 4.12 or later, the `apiVIP` parameter is deprecated. Instead, use a list format for the `apiVIPs` parameter to specify an IPv4 address, an IPv6 address or both IP address formats.
====

| `bmcCACert` | | `redfish` and `redfish-virtualmedia` need this parameter to manage BMC addresses when using self-signed certificates with `disableCertificateVerification` set to `False`.

| `ingressVIPs` | a| (Optional) The virtual IP address for ingress traffic.

You must either provide this setting in the `install-config.yaml` file as a reserved IP from the `MachineNetwork` parameter or preconfigured in the DNS so that the default name resolves correctly. Use the virtual IP address and not the FQDN when adding a value to the `ingressVIPs` configuration setting in the `install-config.yaml` file. For dual-stack networking, the primary IP address can be either an IPv4 network or an IPv6 network. If not set, the installation program uses `test.apps.<cluster_name>.<base_domain>` to derive the IP address from the DNS.

[NOTE]
====
Before OpenShift Container Platform 4.12, the cluster installation program only accepted an IPv4 address or an IPv6 address for the `ingressVIP` parameter. In OpenShift Container Platform 4.12 and later, the `ingressVIP` parameter is deprecated. Instead, use a list format for the `ingressVIPs` parameter to specify an IPv4 addresses, an IPv6 addresses or both IP address formats.
====

|===

[cols="1,1,3", options="header"]
.Optional Parameters
|===
|Parameters
|Default
|Description

a|
----
platform:
  baremetal:
    additionalNTPServers:
    - <ip_address_or_domain_name>
----
|
| An optional list of additional NTP servers to add to each host. You can use an IP address or a domain name to specify each NTP server. Additional NTP servers are user-defined NTP servers that enable preinstallation clock synchronization when the cluster host clocks are out of synchronization.

|`provisioningDHCPRange`
|`172.22.0.10,172.22.0.100`
|Defines the IP range for nodes on the provisioning network.

a|`provisioningNetworkCIDR`
|`172.22.0.0/24`
|The CIDR for the network to use for provisioning. When not using the default address range on the provisioning network, you must set this configuration parameter.

|`clusterProvisioningIP`
|The third IP address of the `provisioningNetworkCIDR`.
|The IP address within the cluster where the provisioning services run. Defaults to the third IP address of the provisioning subnet. For example, `172.22.0.3`.

|`bootstrapProvisioningIP`
|The second IP address of the `provisioningNetworkCIDR`.
|The IP address on the bootstrap VM where the provisioning services run while the installation program is deploying the control plane nodes. Defaults to the second IP address of the provisioning subnet. For example, `172.22.0.2` or `2620:52:0:1307::2`.

| `externalBridge`
| `baremetal`
| The name of the bare metal bridge of the hypervisor attached to the bare metal network.

| `provisioningBridge`
| `provisioning`
| The name of the provisioning bridge on the `provisioner` host attached to the provisioning network.

|`architecture`
|
|Defines the host architecture for your cluster. Valid values are `amd64` or `arm64`.

| `defaultMachinePlatform`
|
| The default configuration used for machine pools without a platform configuration.

| `bootstrapOSImage`
|
| A URL to override the default operating system image for the bootstrap node. The URL must contain a SHA-256 hash of the image. For example:
`https://mirror.openshift.com/rhcos-<version>-qemu.qcow2.gz?sha256=<uncompressed_sha256>`.

| `provisioningNetwork`
|
| The `provisioningNetwork` parameter determines whether the cluster uses the provisioning network. If it does, the parameter also determines if the cluster manages the network.

`Disabled`: Set this parameter to `Disabled` to disable the requirement for a provisioning network. When set to `Disabled`, you must only use virtual media based provisioning, or install the cluster by using the Assisted Installer. If `Disabled` and using power management, BMCs must be accessible from the bare metal network. If `Disabled`, you must provide two IP addresses on the bare metal network for the provisioning services to use.

`Managed`: Set this parameter to `Managed`, which is the default, to fully manage the provisioning network, including DHCP, TFTP, and so on.

`Unmanaged`: Set this parameter to `Unmanaged` to enable the provisioning network but take care of manual configuration of DHCP. Virtual media provisioning is recommended but PXE is still available if required.

| `httpProxy`
|
| Set this parameter to the appropriate HTTP proxy used within your environment.

| `httpsProxy`
|
| Set this parameter to the appropriate HTTPS proxy used within your environment.

| `noProxy`
|
| Set this parameter to the appropriate list of exclusions for proxy usage within your environment.

|===

== Hosts

The `hosts` parameter is a list of separate bare metal assets used to build the cluster.

[width="100%", cols="4,1,4",  options="header"]
.Hosts
|===
|Name |Default |Description
| `name`
|
| The name of the `BareMetalHost` resource to associate with the details. For example, `openshift-master-0`.

| `role`
|
| The role of the bare metal node. Either `master` (control plane node) or `worker` (compute node).

| `bmc`
|
| Connection details for the baseboard management controller. See the BMC addressing section for additional details.

a|
----
bmc:
    address:
----
|
| The protocol and address of the BMC as a URL.

a|
----
bmc:
    username:
----
|
| The username of the BMC.

a|
----
bmc:
    password:
----
|
| The password of the BMC.

a|
----
bmc:
    disableCertificateVerification:
----
| `False`
| `redfish` and `redfish-virtualmedia` need this parameter to manage BMC addresses. For OpenShift Container Platform 4.16 and earlier, the value should be `True` when using a self-signed certificate. OpenShift Container Platform supports self-signed certificates with certificate verification when used with the `bmcVerifyCA` parameter.

a|
----
platform:
  baremetal:
    bmcVerifyCA:
----
|
| A local or self-signed CA certificate that the installation program will use to secure communication with the BMC. If you specify your own CA certificate, ensure that `disableCertificateVerification` is set to `False` so that the user-provided CA certificate is validated.

| `bootMACAddress`
|
a| The MAC address of the NIC that the host uses for the provisioning network. Ironic retrieves the IP address by using the `bootMACAddress` parameter. Then, it binds to the host.

[NOTE]
====
You must provide a valid MAC address from the host if you disabled the provisioning network.
====

| `networkConfig`
|
| Set this optional parameter to configure the network interface of a host. See "(Optional) Configuring host network interfaces" for additional details.

|===

// This is included in the following assemblies:
//
// ipi-install-configuration-files.adoc

[id='root-device-hints_{context}']
= Root device hints

The `rootDeviceHints` parameter enables the installer to provision the {op-system-first} image to a particular device. The installer examines the devices in the order it discovers them, and compares the discovered values with the hint values. The installer uses the first discovered device that matches the hint value. The configuration can combine multiple hints, but a device must match all hints for the installer to select it.

.Subfields

|===
| Subfield | Description

| `deviceName` a| A string containing a Linux device name such as `/dev/vda` or `/dev/disk/by-path/`.
[NOTE]
====
It is recommended to use the `/dev/disk/by-path/<device_path>` link to the storage location.
====

The hint must match the actual value exactly.

| `hctl` | A string containing a SCSI bus address like `0:0:0:0`. The hint must match the actual value exactly.

| `model` | A string containing a vendor-specific device identifier. The hint can be a substring of the actual value.

| `vendor` | A string containing the name of the vendor or manufacturer of the device. The hint can be a sub-string of the actual value.

| `serialNumber` | A string containing the device serial number. The hint must match the actual value exactly.

| `minSizeGigabytes` | An integer representing the minimum size of the device in gigabytes.

| `wwn` | A string containing the unique storage identifier. The hint must match the actual value exactly.

| `wwnWithExtension` | A string containing the unique storage identifier with the vendor extension appended. The hint must match the actual value exactly.

| `wwnVendorExtension` | A string containing the unique vendor storage identifier. The hint must match the actual value exactly.

| `rotational` | A boolean indicating whether the device should be a rotating disk (true) or not (false).

|===

.Example usage

[source,yaml]
----
     - name: master-0
       role: master
       bmc:
         address: ipmi://10.10.0.3:6203
         username: admin
         password: redhat
       bootMACAddress: de:ad:be:ef:00:40
       rootDeviceHints:
         deviceName: "/dev/sda"
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc

[id="creating-the-openshift-manifests_{context}"]
= Creating the OpenShift Container Platform manifests

. Create the OpenShift Container Platform manifests.
+
[source,terminal]
----
$ ./openshift-baremetal-install --dir ~/clusterconfigs create manifests
----
+
[source,terminal]
----
INFO Consuming Install Config from target directory
WARNING Making control-plane schedulable by setting MastersSchedulable to true for Scheduler cluster settings
WARNING Discarding the OpenShift Manifest that was provided in the target directory because its dependencies are dirty and it needs to be regenerated
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc

[id='deploying-the-cluster-via-the-openshift-installer_{context}']
= Deploying the cluster via the OpenShift Container Platform installer

Run the OpenShift Container Platform installer:

[source,terminal]
----
$ ./openshift-baremetal-install --dir ~/clusterconfigs --log-level debug create cluster
----

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-installation-workflow.adoc

[id="ipi-install-following-the-progress-of-the-installation_{context}"]
= Following the progress of the installation

During the deployment process, you can check the installation's overall status by issuing the `tail` command to the `.openshift_install.log` log file in the install directory folder:

[source,terminal]
----
$ tail -f /path/to/install-dir/.openshift_install.log
----
