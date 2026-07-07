---
title: "Installing {VirtProductName} on {ibm-cloud-title} bare-metal nodes"
type: reference
domain: openshift
slug: virt-4-22-virt-install-ibm-cloud-bm-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-install-ibm-cloud-bm-nodes
version: 4.22
family: virt
documentKind: "Documentation"
---

# Installing {VirtProductName} on {ibm-cloud-title} bare-metal nodes

[id="virt-install-ibm-cloud-bm-nodes"]

= Installing {VirtProductName} on {ibm-cloud-title} bare-metal nodes

[role="_abstract"]
Install {VirtProductName} on {ibm-cloud-title} bare-metal nodes using Assisted Installer. The cluster has 6 bare-metal nodes (3 control and 3 compute). An additional virtual machine is required for bootstrapping and to act as a Samba server, DHCP server, network gateway, and load balancer.

== Prerequisites

* An account in {ibm-cloud-title} with permissions to order and operate bare-metal nodes.
* An {ibm-cloud-title} SSL VPN user, to access the SuperMicro IPMI interface of a node.
* Install the OpenShift CLI (`oc`).

// Module included in the following assemblies:
//
// * virt/install/virt-install-ibm-cloud-bm-nodes.adoc

[id="virt-install-ibm-cloud-config-new-cluster_{context}"]
= Configuring {ibm-cloud-title} for the new cluster

[role="_abstract"]
Configure and provision the {ibm-cloud-title} environment to establish the operational framework and nodes for your {VirtProductName} cluster.

.Procedure

. Create a new virtual server instance in {ibm-cloud-title} at Virtual Server for Classic to be the Bastion server. This instance is used to run the installation and provide environment services.

. Change the default properties of the new virtual server instance to the following values. Use the provided defaults for all other values.
+
* *Type of virtual server:* Public
* *Operating system:* CentOS
* Your public SSH RSA key

. Note the private VLAN and subnet the virtual server instance is assigned to at VLANs.

. Provision 6 bare-metal nodes in {ibm-cloud-title} at Bare metal server provision. Use the following values when provisioning the nodes:

* *Domain*: A subdomain you can add records to.
* *Quantity*: 6
* *Location*: The same location as the virtual server instance.
* *Storage disks*: RAID 1
* *Network Interface*: Private
* *Private VLAN*: The same as noted for the virtual server instance.

. Confirm all nodes are provisioned and ready at Device list.

. Rename the control plane nodes to `control0-<domain-name>`, `control1-<domain-name>`, and `control2-<domain-name>`. Replace `<domain-name>` with the domain used when provisioning the nodes.

. Rename the compute nodes to `compute0-<domain-name>`, `compute1-<domain-name>`, and `compute2-<domain-name>`. Replace `<domain-name>` with the domain used when provisioning the nodes.

. Configure the Bastion virtual server instance as a default network gateway.

. Configure DHCP by editing `/etc/dhcp/dhcpd.conf` on the Bastion virtual server instance. For example:
+
[source,text]
----
# Set DNS name and DNS server's IP address or hostname
option domain-name  <dns_domain_name>;
option domain-name-servers  <dns_ip_addresses>;

# Declare DHCP Server
authoritative;

# The default DHCP lease time
default-lease-time <default_lease_value>;

# Set the maximum lease time
max-lease-time <max_lease_value>;

# Set Network address, subnet mask and gateway

subnet <subnet_ip_address> netmask <subnet_mask> {
  # Range of IP addresses to allocate
  range dynamic-bootp <dynamic_boot_lower_address> <dynamic_boot_upper_address>;
  # Provide broadcast address
  option broadcast-address <broadcast_ip_address>;
  # Set default gateway
  option routers <default_gateway_ip_address>;
----
+
where:
+
`<dns_domain_name>`:: Specifies the default domain name for DNS clients.
`<dns_ip_addresses>`:: Specifies a comma-separated list of DNS server IP addresses.
`<default_lease_value>`:: Specifies the default number of seconds a client keeps an assigned address.
`<max_lease_value>`:: Specifies the maximum number of seconds a client keeps an assigned address.
`<subnet_ip_address>`:: Specifies the start of the subnet IP address range.
`<subnet_mask>`:: Specifies the subnet mask of the subnet IP address range.
`<broad_ip_address>`:: Specifies the broadcast IP address to use when to use sending a message to every device on the subnet.
`<default_gateway_ip_address>`:: Specifies the default gateway of the subnet.

. Restart DHCP on the Bastion virtual server instance:
+
[source,terminal]
----
$ systemctl restart dhcpd
----

. Enable IP forwarding on the Bastion virtual server instance:
+
[source,terminal]
----
$ sysctl -w net.ipv4.ip_forward=1
----

. Verify IP forwarding is enabled on the Bastion virtual server instance:
+
[source,terminal]
----
$ sysctl -p /etc/sysctl.conf
----

. Restart the network service on the Bastion virtual server instance:
+
[source,terminal]
----
$ service network restart
----

. Verify if `firewalld` is enabled on the Bastion virtual server instance:
+
[source,terminal]
----
$ firewall-cmd --state
----

. If the `firewalld` service is not enabled on the Bastion virtual server instance, enable the service:
+
[source,terminal]
----
$ systemctl enable firewalld
----

. Start the `firewalld` service:
+
[source,terminal]
----
$ systemctl start firewalld
----

. Add network address translation (NAT) rules to the `firewalld` service:
+
[source,terminal]
----
$ firewall-cmd --add-masquerade --permanent
----

. Restart the `firewalld` service:
+
[source,terminal]
----
$ firewall-cmd --reload
----

// Module included in the following assemblies:
//
// * virt/install/virt-install-ibm-cloud-bm-nodes.adoc

[id="virt-install-ibm-cloud-initialize-new-cluster_{context}"]
= Initializing the new cluster configuration

[role="_abstract"]
Initialize the new cluster configuration using the {VirtProductName} Assisted Installer service and Samba on the Bastion virtual server instance.

.Procedure
. Log in to the *Assisted Installer* service.

. Create a new cluster. The new cluster has the following properties:

* *Cluster name*: The name used to identify the cluster under the base domain.
* *Base domain*: The domain used to provision the bare-metal nodes.

. Click *Next*.

. Click *Generate Discovery ISO*.

. Provide your public SSH RSA key when prompted.

. Copy and save the generated `wget` command for the ISO file. This will be used later to connect to the cluster nodes.

. Install Samba server on the Bastion virtual server instance:
+
[source,terminal]
----
$ dnf install samba
----

. Enable Samba server on the Bastion virtual server instance:
+
[source,terminal]
----
$ systemctl enable smb --now
----

. Configure NAT rules for the Samba server:
+
[source,terminal]
----
$ firewall-cmd --permanent --zone=FedoraWorkstation --add-service=samba
$ firewall-cmd --reload
----

. Configure a root user password:
+
[source,terminal]
----
$ sudo smbpasswd -a root
----

. Create a share directory:
+
[source,terminal]
----
$ mkdir <share_directory>
----
+
Replace `<share_directory>` with the share directory name.

. Navigate to the share directory and download the Assisted Installer ISO file using the generated `wget` command.

// Module included in the following assemblies:
//
// * virt/install/virt-install-ibm-cloud-bm-nodes.adoc

[id="virt-install-ibm-cloud-cluster-network-access_{context}"]
= Configuring cluster networking and access

[role="_abstract"]
Configure networking and access to allow for remote management of the cluster.

.Procedure

. Edit `/etc/samba/smb.conf` to use the following configuration:
+
[source,text]
----
[global]
      log level = 3
          workgroup = SAMBA
          security = user

          passdb backend = tdbsam

          printing = cups
          printcap name = cups
          load printers = yes
          cups options = raw

      server min protocol = NT1
      ntlm auth = yes

[share]
      comment = ISO Files
      path = /root/share
      browseable = yes
      public = no
      read only = no
      directory mode = 0555
      valid users = root
----
+
[NOTE]
====
For a more detailed example of the `smb.conf` file, see the `smb.conf.example` file in the same directory.
====

. Save the file.

. Verify the new Samba configuration:
+
[source,terminal]
----
$ testparm
----

. Restart the Samba service:
+
[source,terminal]
----
$ systemctl restart smb
----

. Verify that the Samba service is running and active:
+
[source,terminal]
----
$ systemctl status smb
----

. Configure SSL VPN access to {ibm-cloud-title}:
.. Perform the procedure at Getting started with {ibm-cloud-title} Virtual Private Networking in the {ibm-cloud-title} documentation.
.. Download and install the MotionPro SSL VPN client.
.. Connect to the appropriate {ibm-cloud-title} endpoint:
+
[source,terminal]
----
$ sudo MotionPro --host $<vpn_endpoint> --user $<vpn_username> --passwd $<vpn_password>
----
+
where:
+
`<vpn_endpoint>`:: Specifies the appropriate SSL VPN endpoint.
`<vpn_username>`:: Specifies the SSL VPN user name you configured.
`<vpn_password>`:: Specifies the SSL VPN password you configured.
+
[NOTE]
====
Connecting to the {ibm-cloud-title} SSL VPN disconnects you from any open VPN connections.
====

// Module included in the following assemblies:
//
// * virt/install/virt-install-ibm-cloud-bm-nodes.adoc

[id="virt-install-ibm-cloud-complete-cluster-config_{context}"]
= Completing the cluster configuration

[role="_abstract"]
Complete the cluster configuration by installing software on the control plane and compute nodes and configuring DNS for external access.

.Procedure

. For each bare-metal server, perform the following tasks:
.. Access the server using the IPMI console.
+
[NOTE]
====
The IP address and credentials for IPMI console access is available in the *Remote management* section for each server.
====

.. Mount the Assisted Installer ISO file with the following attributes:
+
* *Virtual Media*: CD-ROM Image
* *Share host*: The private IP address of the Bastion server.
* *Path to image*: The location of the Assisted Installer ISO file.
* *User*: root
* *Password*: The root user password you configured.

.. Click *Save and Mount*.
.. Verify the ISO mounted successfully.
.. Restart the server by selecting *Remote Control* -> *Power Control* -> *Reset Server* -> *Perform Action*.

. Return to the *Assisted Installer* service.

. Select the *Install {VirtProductName}* and *Install {rh-storage}* checkboxes in the *Assisted Installer* options.

. Select a role for each host.
+
[NOTE]
====
The cluster consists of 3 control plane and 3 compute nodes.
====

. Wait for the *Assisted Installer* interface to indicate each node is ready.

. Click *Next*.

. Select *Cluster Managed Network*.

. Select the *API VIP* and *Ingress VIP* checkboxes to obtain them from DHCP or leave them unchecked to enter static values.

. Click *Install*.

. For each bare-metal server, perform the following tasks:
.. Access the server using the IPMI console.
+
[NOTE]
====
The IP address and credentials for IPMI console access is available in the *Remote management* section for each server.
====

.. Select *Virtual Media* -> *CD-Rom Image*.
.. Click *Unmount*.
.. Select *Remote Control* -> *Power Control* -> *Reset Server* -> *Perform Action* to restart the server.

. Locate the *Cluster Credentials* section of the installation summary.

. Perform the following tasks in the *Cluster Credentials* section:
.. Download the `kubeconfig` file.
.. Save the `kubeadmin` password.

. Install `haproxy` on the Bastion virtual server instance.

. Configure `haproxy` for your environment. The following is an example configuration:
+
[source,text]
----
#---------------------------------------------------------------------
# Example configuration for a possible web application.  See the
# full configuration options online.
#
#   https://www.haproxy.org/download/1.8/doc/configuration.txt
#
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Global settings
#---------------------------------------------------------------------
global
  # to have these messages end up in /var/log/haproxy.log you will
  # need to:
  #
  # 1) configure syslog to accept network log events.  This is done
  # by adding the '-r' option to the SYSLOGD_OPTIONS in
  # /etc/sysconfig/syslog
  #
  # 2) configure local2 events to go to the /var/log/haproxy.log
  #   file. A line like the following can be added to
  #   /etc/sysconfig/syslog
  #
  # local2.*                    /var/log/haproxy.log
  #
  log       127.0.0.1 local2

  chroot    /var/lib/haproxy
  pidfile   /var/run/haproxy.pid
  maxconn   4000
  user      haproxy
  group     haproxy
  daemon

  # turn on stats unix socket
  stats socket /var/lib/haproxy/stats

  # utilize system-wide crypto-policies
  #ssl-default-bind-ciphers PROFILE=SYSTEM
  #ssl-default-server-ciphers PROFILE=SYSTEM

#---------------------------------------------------------------------
# common defaults that all the 'listen' and 'backend' sections will
# use if not designated in their block
#---------------------------------------------------------------------
defaults
  mode                  tcp
  log                   global
  option                httplog
  option                dontlognull
  option http-server-close
  option forwardfor     except 127.0.0.0/8
  option                redispatch
  retries               3
  timeout http-request  10s
  timeout queue         1m
  timeout connect       10s
  timeout client        1m
  timeout server        1m
  timeout http-keep-alive 10s
  timeout check         10s
  maxconn               3000
#---------------------------------------------------------------------
# main frontend which proxys to the backends
#---------------------------------------------------------------------

frontend api
  bind <api_ip_address>:<api_port>
  default_backend controlplaneapi

frontend apiinternal
  bind <apiinternal_ip_address>:<apiinternal_port>
  default_backend controlplaneapiinternal

frontend secure
  bind <frontend_secure_ip_address>:<frontend_secure_port>
  default_backend secure

frontend insecure
  bind <frontend_insecure_ip_address>:<frontend_insecure_port>
  default_backend insecure

#---------------------------------------------------------------------
# static backend
#---------------------------------------------------------------------

backend controlplaneapi
  balance source
  server api <controlplaneapi_ip_address>:<controlplaneapi_port> check

backend controlplaneapiinternal
  balance source
  server api <controlplaneapiinternal_ip_address>:<controlplaneapiinternal_port> check

backend secure
  balance source
  server ingress <backend_secure_ip_address>:<backend_secure_port> check

backend insecure
  balance source
  server ingress <backend_insecure_ip_address>:<backend_insecure_port> check
----
+
where:
+
`<api_ip_address>:<api_port>`:: Specifies the front end IP address and port used by the Kubernetes API server.
`<apiinternal_ip_address>:<apiinternal_port>`:: Specifies the front end IP address and port used for internal cluster management.
`<frontend_secure_ip_address>:<frontend_secure_port>`:: Specifies the front end IP address and port used for HTTPS traffic for hosted applications.
`<frontend_insecure_ip_address>:<frontend_insecure_port>`:: Specifies the front end IP address and port used for HTTP traffic for hosted applications.
`<controlplaneapi_ip_address>:<controlplaneapi_port>`:: Specifies the back end IP address and port used by the Kubernetes API server.
`<controlplaneapiinternal_ip_address>:<controlplaneapiinternal_port>`:: Specifies the back end IP address and port used for internal cluster management.
`<backend_secure_ip_address>:<backend_secure_port>`:: Specifies the back end IP address and port used for HTTPS traffic for hosted applications.
`<backend_insecure_ip_address>:<backend_insecure_port>`:: Specifies the back end IP address and port used for HTTP traffic for hosted applications.
+
[NOTE]
====
Replace the example values with values applicable to your network configuration.
====

. Save the `haproxy` configuration.

. Configure two DNS Address records (A records) for the subdomain that are externally available over the Internet:
+
[source,text]
----
<bastion_public_ip_address> api.<cluster_name>.<cluster_domain>
<bastion_public_ip_address> *.apps..<cluster_name>.<cluster_domain>
----
+
where:
+
`<bastion_public_ip_address>`:: Specifies the externally available IP address of the Bastion virtual server instance.
`<cluster_name>`:: Specifies the name assigned to the cluster.
`<cluster_domain>`:: Specifies the domain assigned to the cluster.

.Verification

. Perform the following tasks to verify cluster access using command line access:
.. Set your environment with the `kubeconfig` file:
+
[source,terminal]
----
$ export KUBECONFIG=<kubeconfig_file_path>
----
+
where:
+
`<kubeconfig_file_path>`:: Specifies the path to the downloaded `kubeconfig` file.

.. Check cluster node status:
+
[source,terminal]
----
$ oc get nodes
----
+
[NOTE]
====
The command output should show all nodes as `Ready` in the `STATUS` column and the `ROLES` column should show that control plane and compute nodes are present.
====
.. Check the cluster version:
+
[source, terminal]
----
$ oc get clusterversion
----
+
[NOTE]
====
The command output should say `Condition: Available`.
====

. Perform the following tasks to verify cluster access using the web console:
.. Paste the access URL provided by Assisted Installer into your web browser.
+
[NOTE]
====
By default, clusters use self-signed certificates. This may cause your browser to display a message that says *Connection not private* or a similar warning. You can close this warning and continue.
====
.. Navigate to the URL.
.. Log in to the cluster with the username `kubeadmin` and the `kubeadmin` password provided in the *Cluster Credentials* section.
