---
title: "Installing a cluster with {op-system-base} KVM on {ibm-z-title} and {ibm-linuxone-title}"
type: reference
domain: openshift
slug: installing-4-22-installing-ibm-z-kvm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-ibm-z-kvm
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster with {op-system-base} KVM on {ibm-z-title} and {ibm-linuxone-title}

[id="installing-ibm-z-kvm"]
= Installing a cluster with {op-system-base} KVM on {ibm-z-title} and {ibm-linuxone-title}

[role="_abstract"]
In OpenShift Container Platform version , you can install a cluster on
{ibm-z-name} or {ibm-linuxone-name} infrastructure that you provision.

[NOTE]
====
While this document refers only to {ibm-z-name}, all information in it also applies to {ibm-linuxone-name}.
====

[id="prerequisites-ibm-z-kvm_{context}"]
== Prerequisites

* You have completed the tasks in Preparing to install a cluster on {ibm-z-title} using user-provisioned infrastructure.
* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* Before you begin the installation process, you must clean the installation directory. This ensures that the required installation files are created and updated during the installation process.
* You provisioned persistent storage using {rh-storage} or other supported storage protocols for your cluster. To deploy a private image registry, you must set up persistent storage with `ReadWriteMany` access.
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.
+
[NOTE]
====
Be sure to also review this site list if you are configuring a proxy.
====
* You provisioned a {op-system-base} Kernel Virtual Machine (KVM) system that is hosted on the logical partition (LPAR) and based on {op-system-base} 8.6 or later. See Red Hat Enterprise Linux 8 and 9 Life Cycle.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc

[id="installation-infrastructure-user-infra_{context}"]
= Preparing the user-provisioned infrastructure

[role="_abstract"]
Before you install OpenShift Container Platform on user-provisioned infrastructure, you must prepare the underlying infrastructure.

This section provides details about the high-level steps required to set up your cluster infrastructure in preparation for an OpenShift Container Platform installation. This includes configuring IP networking and network connectivity for your cluster nodes,
preparing a web server for the Ignition files,
enabling the required ports through your firewall, and setting up the required DNS and load balancing infrastructure.

After preparation, your cluster infrastructure must meet the requirements outlined in the _Requirements for a cluster with user-provisioned infrastructure_ section.

.Prerequisites

* You have reviewed the OpenShift Container Platform 4.x Tested Integrations page.
* You have reviewed the infrastructure requirements detailed in the _Requirements for a cluster with user-provisioned infrastructure_ section.

.Procedure

. Set up static IP addresses.

. Set up an HTTP or HTTPS server to provide Ignition files to the cluster nodes.

. If you are using DHCP to provide the IP networking configuration to your cluster nodes, configure your DHCP service.
+
.. Add persistent IP addresses for the nodes to your DHCP server configuration. In your configuration, match the MAC address of the relevant network interface to the intended IP address for each node.
+
.. When you use DHCP to configure IP addressing for the cluster machines, the machines also obtain the DNS server information through DHCP. Define the persistent DNS server address that is used by the cluster nodes through your DHCP server configuration.
+
[NOTE]
====
If you are not using a DHCP service, you must provide the IP networking configuration and the address of the DNS server to the nodes at {op-system} install time. These can be passed as boot arguments if you are installing from an ISO image. See the _Installing {op-system} and starting the OpenShift Container Platform bootstrap process_ section for more information about static IP provisioning and advanced networking options.
====
+
.. Define the hostnames of your cluster nodes in your DHCP server configuration. See the _Setting the cluster node hostnames through DHCP_ section for details about hostname considerations.
+
[NOTE]
====
If you are not using a DHCP service, the cluster nodes obtain their hostname through a reverse DNS lookup.
====
. Choose to perform either a fast track installation of {op-system-first} or a full installation of {op-system-first}. For the full installation, you must set up an HTTP or HTTPS server to provide Ignition files and install images to the cluster nodes. For the fast track installation an HTTP or HTTPS server is not required, however, a DHCP server is required. See sections “Fast-track installation: Creating {op-system-first} machines" and “Full installation: Creating {op-system-first} machines".

. Ensure that your network infrastructure provides the required network connectivity between the cluster components. See the _Networking requirements for user-provisioned infrastructure_ section for details about the requirements.

. Configure your firewall to enable the ports required for the OpenShift Container Platform cluster components to communicate. See _Networking requirements for user-provisioned infrastructure_ section for details about the ports that are required.
+
[IMPORTANT]
====
By default, port `1936` is accessible for an OpenShift Container Platform cluster, because each control plane node needs access to this port.

For ingress health check probes, the `/healthz/ready` endpoint is available on this port.

Avoid using the Ingress load balancer to expose this port, because doing so might result in the exposure of sensitive information, such as statistics and metrics, related to Ingress Controllers.
====

. Setup the required DNS infrastructure for your cluster.
+
.. Configure DNS name resolution for the Kubernetes API, the application wildcard, the bootstrap machine, the control plane machines, and the compute machines.
+
.. Configure reverse DNS resolution for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.
+
See the _User-provisioned DNS requirements_ section for more information about the OpenShift Container Platform DNS requirements.

. Validate your DNS configuration.
+
.. From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses in the responses correspond to the correct components.
+
.. From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names in the responses correspond to the correct components.
+
See the _Validating DNS resolution for user-provisioned infrastructure_ section for detailed DNS validation steps.

. Provision the required API and application ingress load balancing infrastructure. See the _Load balancing requirements for user-provisioned infrastructure_ section for more information about the requirements.
+
[NOTE]
====
Some load balancing solutions require the DNS name resolution for the cluster nodes to be in place before the load balancing is initialized.
====

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc

[id="installation-load-balancing-user-infra-example_{context}"]
= Example load balancer configuration for user-provisioned clusters

[role="_abstract"]
Reference the example API and application Ingress load balancer configuration so that you can understand how to meet the load balancing requirements for user-provisioned clusters.

The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

= Example load balancer configuration for clusters that are deployed with user-managed load balancers

This section provides an example API and application Ingress load balancer configuration that meets the load balancing requirements for clusters that are deployed with user-managed load balancers. The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

[TIP]
====
If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node.
====

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

[NOTE]
====
If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`.
====

.Sample API and application Ingress load balancer configuration
[source,text]
----
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443
  bind *:6443
  mode tcp
  option  httpchk GET /readyz HTTP/1.0
  option  log-health-checks
  balance roundrobin
  server bootstrap bootstrap.ocp4.example.com:6443 verify none check check-ssl inter 10s fall 2 rise 3 backup
  server master0 master0.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master1 master1.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master2 master2.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server bootstrap bootstrap.ocp4.example.com:22623 check inter 1s backup
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:443 check inter 1s
  server compute1 compute1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:80 check inter 1s
  server compute1 compute1.ocp4.example.com:80 check inter 1s
----

where:

`listen api-server-6443`:: Port `6443` handles the Kubernetes API traffic and points to the control plane machines. You must configure health checks on this port to ensure that the API server is available before routing traffic.
`server bootstrap bootstrap.ocp4.example.com`:: The bootstrap entries must be in place before the OpenShift Container Platform cluster installation and they must be removed after the bootstrap process is complete.
`listen machine-config-server`:: Port `22623` handles the machine config server traffic and points to the control plane machines.
`listen ingress-router-443`:: Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.
`listen ingress-router-80`:: Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.
+
[NOTE]
====
If you are deploying a compact three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc

[id="installation-initializing-manual_{context}"]
= Manually creating the installation configuration file

[role="_abstract"]
Installing the cluster requires that you manually create the installation configuration file.

[IMPORTANT]
====
The Cloud Controller Manager Operator performs a connectivity check on a provided hostname or IP address. Ensure that you specify a hostname or an IP address to a reachable vCenter server. If you provide metadata to a non-existent vCenter server, installation of the cluster fails at the bootstrap stage.
====

.Prerequisites

* You have uploaded a custom RHCOS AMI.
* You have an SSH public key on your local machine for use with the installation program. You can use the key for SSH authentication onto your cluster nodes for debugging and disaster recovery.
* You have obtained the OpenShift Container Platform installation program and the pull secret for your
cluster.
* Obtain the `imageContentSources` section from the output of the command to
mirror the repository.
* Obtain the contents of the certificate for your mirror registry.
* You have the `imageContentSourcePolicy.yaml` file that was created when you mirrored your registry.
* You have obtained the contents of the certificate for your mirror registry.

.Procedure

. Create an installation directory to store your required installation assets in:
+
[source,terminal]
----
$ mkdir <installation_directory>
----
+
[IMPORTANT]
====
You must create a directory. Some installation assets, such as bootstrap X.509 certificates have short expiration intervals, so you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
====

. Edit the `install-config.yaml` file to set the `publish: Internal` parameter.
. Edit the `install-config.yaml` file to set the parameters necessary for installation into an existing VPC.
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
. Edit the `install-config.yaml` file to set the parameters necessary for installation into a shared VPC.
.. Define the network, subnets, and project names for the shared VPC:
+
[source,yaml]
----
# ...
platform:
  gcp:
    computeSubnet: <shared_vpc_compute_subnet>
    controlPlaneSubnet: <shared_vpc_control_plane_subnet>
    network: <shared_vpc_name>
    networkProjectID: <host_project_name>
    projectID: <service_project_name>
----
where:

`<shared_vpc_compute_subnet>`:: Specifies the name of the subnet in the shared VPC for compute machines to use.
`<shared_vpc_control_plane_subnet>`:: Specifies the name of the subnet in the shared VPC for control plane machines to use.
`<shared_vpc_name>`:: Specifies the name of the shared VPC.
`<host_project_name>`:: Specifies the name of the host project where the shared VPC exists.
`<service_project_name>`:: Specifies the name of the project where you want to install the cluster.

. Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`.
.. Edit the `install-config.yaml` file to set the `publish: Internal` parameter.
.. If you use your own outbound routing to connect to the internet, set the `outboundType: UserDefinedRouting` parameter.
.. Edit the `install-config.yaml` file so that the value of the `platform.azure.cloudName` parameter is `AzureUSGovernmentCloud`.
+
[NOTE]
====
You must name this configuration file `install-config.yaml`.
====
+
When customizing the sample template, be sure to provide the information that is required for an installation in a restricted network:
+
.. Update the `pullSecret` value to contain the authentication information for your registry:
+
[source,yaml]
----
pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
----
+
For `<mirror_host_name>`, specify the registry domain name that you specified in the certificate for your mirror registry, and for `<credentials>`, specify the base64-encoded user name and password for your mirror registry.
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
For these values, use the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry.
+
.. If network restrictions limit the use of public endpoints to access the required {ibm-cloud-name} services, add the `serviceEndpoints` stanza to `platform.ibmcloud` to specify an alternate service endpoint.
+
[NOTE]
====
You can specify only one alternate service endpoint for each service.
====
+
.Example of using alternate services endpoints
[source,yaml]
----
# ...
serviceEndpoints:
  - name: IAM
    url: <iam_alternate_endpoint_url>
  - name: VPC
    url: <vpc_alternate_endpoint_url>
  - name: ResourceController
    url: <resource_controller_alternate_endpoint_url>
  - name: ResourceManager
    url: <resource_manager_alternate_endpoint_url>
  - name: DNSServices
    url: <dns_services_alternate_endpoint_url>
  - name: COS
    url: <cos_alternate_endpoint_url>
  - name: GlobalSearch
    url: <global_search_alternate_endpoint_url>
  - name: GlobalTagging
    url: <global_tagging_alternate_endpoint_url>
# ...
----
+
.. Optional: Set the publishing strategy to `Internal`:
+
[source,yaml]
----
publish: Internal
----
+
By setting this option, you create an internal Ingress Controller and a private load balancer.
+
[NOTE]
====
If you use the default value of `External`, your network must be able to access the public endpoint for {ibm-cloud-name} Internet Services (CIS). CIS is not enabled for Virtual Private Endpoints.
====
+
[NOTE]
====
You must name this configuration file `install-config.yaml`.
====

+
** Unless you use a registry that {op-system} trusts by default, such as `docker.io`, you must provide the contents of the certificate for your mirror repository in the `additionalTrustBundle` section. In most cases, you must provide the certificate for your mirror.
** You must include the `imageContentSources` section from the output of the command to
mirror the repository.
+
[IMPORTANT]
====
** The `ImageContentSourcePolicy` file is generated as an output of `oc mirror` after the mirroring process is finished.
** The `oc mirror` command generates an `ImageContentSourcePolicy` file which contains the YAML needed to define `ImageContentSourcePolicy`.
Copy the text from this file and paste it into your `install-config.yaml` file.
** You must run the 'oc mirror' command twice. The first time you run the `oc mirror` command, you get a full `ImageContentSourcePolicy` file. The second time you run the `oc mirror` command, you only get the difference between the first and second run.
Because of this behavior, you must always keep a backup of these files in case you need to merge them into one complete `ImageContentSourcePolicy` file. Keeping a backup of these two output files ensures that you have a complete `ImageContentSourcePolicy` file.
====

+
Make the following modifications for Azure Stack Hub:
+
.. Set the `replicas` parameter to `0` for the `compute` pool:
+
[source,yaml]
----
compute:
- hyperthreading: Enabled
  name: worker
  platform: {}
  replicas: 0
----
* `replicas`: Set to `0`.
+
The compute machines will be provisioned manually later.
+
.. Update the `platform.azure` section of the `install-config.yaml` file to configure your Azure Stack Hub configuration:
+
[source,yaml]
----
platform:
  azure:
    armEndpoint: <azurestack_arm_endpoint>
    baseDomainResourceGroupName: <resource_group>
    cloudName: AzureStackCloud
    region: <azurestack_region>
----
+
where:
+
`<azurestack_arm_endpoint>`:: Specifies the Azure Resource Manager endpoint of your Azure Stack Hub environment, like `\https://management.local.azurestack.external`.
`<resource_group>`:: Specifies the name of the resource group that contains the DNS zone for your base domain.
`cloudName`:: Specifies the Azure Stack Hub environment, which is used to configure the Azure SDK with the appropriate Azure API endpoints.
`region`:: Specifies the name of your Azure Stack Hub region.

+
Make the following modifications:
+
.. Specify the required installation parameters.
+
.. Update the `platform.azure` section to specify the parameters that are specific to Azure Stack Hub.
+
.. Optional: Update one or more of the default configuration parameters to customize the installation.
+
For more information about the parameters, see "Installation configuration parameters".

. If you are installing a three-node cluster or a cluster with user-provisioned infrastructure, set the `compute.replicas` parameter to `0`. In a three-node cluster, this ensures that the cluster's control planes are schedulable. For more information, see "Installing a three-node cluster". In a cluster with user-provisioned infrastructure, you must manually deploy compute machines before you finish installing OpenShift Container Platform.

. Back up the `install-config.yaml` file so that you can use it to install many clusters.
+
[IMPORTANT]
====
Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.
====

[role="_additional-resources"]
.Additional resources
* Installation configuration parameters for {ibm-z-name}

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc

[id="installation-bare-metal-config-yaml_{context}"]
= Sample install-config.yaml file for bare metal
= Sample install-config.yaml file for {ibm-z-title}
= Sample install-config.yaml file for {ibm-power-title}
= Sample install-config.yaml file for other platforms

[role="_abstract"]
You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster platform or modify the values of the required parameters.

[source,yaml,subs="attributes+"]
----
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  replicas: 0
  architecture: s390x
  architecture: ppc64le
controlPlane:
  hyperthreading: Enabled
  name: master
  replicas: 3
  architecture: s390x
  architecture: ppc64le
metadata:
  name: test
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: OVNKubernetes
  machineNetwork:
  - cidr: 192.168.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
fips: false
pullSecret: '{"auths": ...}'
pullSecret: '{"auths": ...}'
sshKey: 'ssh-ed25519 AAAA...'
sshKey: 'ssh-ed25519 AAAA...'
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
sshKey: 'ssh-ed25519 AAAA...'
sshKey: 'ssh-ed25519 AAAA...'
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_repository>/ocp4/openshift4
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_repository>/ocp4/openshift4
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_repository>/ocp4/openshift4
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_repository>/ocp4/openshift4
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
----

where:

`baseDomain`:: Specifies the base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.
`compute`:: Specifies the `compute` node configurations, which is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`.
`controlPlane`:: Specifies the `controlPlane` node configurations, which is a single mapping. To meet the requirements of the different data structures, the first line of the `controlPlane` section must not. Only one control plane pool is used.
`hyperthreading`:: Specifies whether to enable or disable simultaneous multithreading (SMT), or hyperthreading. By default, SMT is enabled to increase the performance of the cores in your machines. You can disable it by setting the parameter value to `Disabled`. If you disable SMT, you must disable it in all cluster machines; this includes both control plane and compute machines.
`hyperthreading`:: Specifies simultaneous multithreading (SMT), which you configure as a post-installation task.

[NOTE]
====
Simultaneous multithreading (SMT) is enabled by default. If SMT is not enabled in your BIOS settings, the `hyperthreading` parameter has no effect.
====

[IMPORTANT]
====
If you disable `hyperthreading`, whether in the BIOS or in the `install-config.yaml` file, ensure that your capacity planning accounts for the dramatically decreased machine performance.
====

[NOTE]
====
Simultaneous multithreading (SMT) is enabled by default. If SMT is not available on your OpenShift Container Platform nodes, the `hyperthreading` parameter has no effect.
====

[IMPORTANT]
====
If you disable `hyperthreading`, whether on your OpenShift Container Platform nodes or in the `install-config.yaml` file, ensure that your capacity planning accounts for the dramatically decreased machine performance.
====

`compute.replicas`:: Specifies the number of compute machines that the cluster creates and manages for you on installer-provisioned installations. You must set this value to `0` when you install OpenShift Container Platform on user-provisioned infrastructure. Additionally for user-provisioned installations, you must manually deploy the compute machines before you finish installing the cluster.

[NOTE]
====
If you are installing a three-node cluster, do not deploy any compute machines when you install the {op-system-first} machines.
====

`controlPlane.replicas`:: Specifies the number of control plane machines that you add to the cluster. Because the cluster uses these values as the number of etcd endpoints in the cluster, the value must match the number of control plane machines that you deploy.
`metadata.name`:: Specifies the cluster name that you specified in your DNS records.
`networking.clusterNetwork.cidr`:: Specifies a block of IP addresses from which pod IP addresses are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the pod network. If you need to access the pods from an external network, you must configure load balancers and routers to manage the traffic.

[NOTE]
====
Class E CIDR range is reserved for a future use. To use the Class E CIDR range, you must ensure your networking environment accepts the IP addresses within the Class E CIDR range.
====

`networking.cidr.hostPrefix`:: Specifies the subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23`, then each node is assigned a `/23` subnet out of the given `cidr`, which allows for 510 (2^(32 - 23) - 2) pod IP addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.
`networking.networkType`:: Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.
`networking.serviceNetwork`:: Specifies the IP address pool to use for service IP addresses. You can enter only one IP address pool. This block must not overlap with existing physical networks. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.
`platform`:: Specifies the platform. You must set the platform to `none`. You cannot provide additional platform configuration variables for

[IMPORTANT]
====
Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation.
====
`fips`:: Specifies either enabling or disabling FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.

--
--

`pullSecret`:: Specifies the {cluster-manager-url-pull}. This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.
`pullSecret`:: Specifies the {cluster-manager-url-pull}. This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.
`pullSecret`:: Specifies the registry domain name for `<local_registry>`, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:5000`. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry.
`pullSecret`:: Specifies the registry domain name for `<local_registry>`, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:5000`. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry.
`sshKey`:: Specifies the SSH public key for the `core` user in {op-system-first}.
`sshKey`:: Specifies the SSH public key for the `core` user in {op-system-first}.

[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====

`additionalTrustBundle`:: Specifies the contents of the certificate file that you used for your mirror registry.
`additionalTrustBundle`:: Specifies the contents of the certificate file that you used for your mirror registry.
`additionalTrustBundle`:: Specifies the `additionalTrustBundle` parameter and value. The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry.
`imageContentSources`:: Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository.

[IMPORTANT]
====
* When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
* When using `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
* `ImageContentSourcePolicy` is deprecated. For more information see _Configuring image registry repository mirroring_.
====
`imageContentSources`:: Specifies the `imageContentSources` section from the output of the command to mirror the repository.

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
//
// * installing/installing_aws/installing-aws-user-infra.adoc [Eventually]
// * installing/installing_azure/installing-azure-user-infra.adoc [Eventually]
// * installing/installing_gcp/installing-gcp-user-infra.adoc [Eventually]
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc [Eventually]
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc [Eventually]
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc [Eventually]
// * installing/installing_vsphere/installing-vsphere.adoc [Eventually]
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-three-node-cluster_{context}"]
= Configuring a three-node cluster

[role="_abstract"]
To create smaller, resource-efficient clusters for testing and production, deploy a bare-metal cluster with zero compute machines. This optional configuration uses only three control plane machines, optimizing infrastructure resources for administrators and developers.
To create smaller, resource-efficient clusters for testing and production, deploy a bare-metal cluster with zero compute machines in a minimal three-node cluster. This optional configuration uses only three control plane machines, optimizing infrastructure resources for testing, development, and production purposes.

In three-node OpenShift Container Platform environments, the three control plane machines are schedulable, which means that your application workloads are scheduled to run on them.

.Prerequisites

* You have an existing `install-config.yaml` file.

.Procedure

* Ensure that the number of compute replicas is set to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza:
+
[source,yaml]
----
compute:
- name: worker
  platform: {}
  replicas: 0
# ...
----
+
[NOTE]
====
You must set the value of the `replicas` parameter for the compute machines to `0` when you install OpenShift Container Platform on user-provisioned infrastructure, regardless of the number of compute machines you are deploying. In installer-provisioned installations, the parameter controls the number of compute machines that the cluster creates and manages for you. This does not apply to user-provisioned installations, where the compute machines are deployed manually.
====
+
[NOTE]
====
The preferred resource for control plane nodes is six vCPUs and 21 GB. For three control plane nodes this is the memory + vCPU equivalent of a minimum five-node cluster. You should back the three nodes, each installed on a 120 GB disk, with three IFLs that are SMT2 enabled. The minimum tested setup is three vCPUs and 10 GB on a 120 GB disk for each control plane node.
====
.Next steps

For three-node cluster installations, follow these next steps:

* If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. See the _Load balancing requirements for user-provisioned infrastructure_ section for more information.

* When you create the Kubernetes manifest files in the following procedure, ensure that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file is set to `true`. This enables your application workloads to run on the control plane nodes.

* Do not deploy any compute nodes when you create the {op-system-first} machines.

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
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc

[id="installation-ibm-z-kvm-user-infra-installing-rhcos_{context}"]
= Installing {op-system} and starting the OpenShift Container Platform bootstrap process

To install OpenShift Container Platform on {ibm-z-name} infrastructure that you provision, you must install {op-system-first} as {op-system-base-full} guest virtual machines. When you install {op-system}, you must provide the Ignition config file that was generated by the OpenShift Container Platform installation program for the type of machine you are installing. If you have configured suitable networking, DNS, and load balancing infrastructure, the OpenShift Container Platform bootstrap process begins automatically after the {op-system} machines have rebooted.

You can perform a fast-track installation of {op-system} that uses a prepackaged QEMU copy-on-write (QCOW2) disk image. Alternatively, you can perform a full installation on a new QCOW2 disk image.

To add further security to your system, you can optionally install {op-system} using {ibm-name} Secure Execution before proceeding to the fast-track installation.

// Module included in the following assemblies:
//
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc

[id="configuring-encryption-kvm-ibm-z-linuxone-environment_{context}"]
= Configuring encryption for nodes in an {ibm-z-title} or {ibm-linuxone-title} environment

You can choose between three methods to optionally secure your OpenShift Container Platform control plane and compute nodes on {ibm-z-name} or {ibm-linuxone-name}:

* {ibm-name} Secure Execution
* Linux Unified Key Setup (LUKS) encryption via {ibm-name} Crypto Express (CEX)
* Network Bound Disk Encryption (NBDE)

// Module included in the following assemblies:
//
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc

[id="installing-rhcos-using-ibm-secure-execution_{context}"]
= Installing {op-system} using {ibm-title} Secure Execution

Before you install {op-system} using {ibm-name} Secure Execution, you must prepare the underlying infrastructure.

.Prerequisites

* {ibm-name} z15 or later, or {ibm-linuxone-name} III or later.
* {op-system-base-full} 8 or later.
* You have a bootstrap Ignition file. The file is not protected, enabling others to view and edit it.
* You have verified that the boot image has not been altered after installation.
* You must run all your nodes as {ibm-name} Secure Execution guests.

.Procedure

. Prepare your {op-system-base} KVM host to support {ibm-name} Secure Execution.

** By default, KVM hosts do not support guests in {ibm-name} Secure Execution mode. To support guests in {ibm-name} Secure Execution mode, KVM hosts must boot in LPAR mode with the kernel parameter specification `prot_virt=1`. To enable `prot_virt=1` on {op-system-base} 8, follow these steps:

.. Navigate to `/boot/loader/entries/` to modify your bootloader configuration file `*.conf`.
.. Add the kernel command line parameter `prot_virt=1`.
.. Run the `zipl` command and reboot your system.
+
KVM hosts that successfully start with support for {ibm-name} Secure Execution for Linux issue the following kernel message:
+
[source,terminal]
----
prot_virt: Reserving <amount>MB as ultravisor base storage.
----
.. To verify that the KVM host now supports {ibm-name} Secure Execution, run the following command:
+
[source,terminal]
----
# cat /sys/firmware/uv/prot_virt_host
----
+
.Example output
+
[source,terminal]
----
1
----
The value of this attribute is 1 for Linux instances that detect their environment as consistent with that of a secure host. For other instances, the value is 0.

. Add your host keys to the KVM guest via Ignition.
+
During the first boot, {op-system} looks for your host keys to re-encrypt itself with them. {op-system} searches for files starting with `ibm-z-hostkey-` in the `/etc/se-hostkeys` directory. All host keys, for each machine the cluster is running on, must be loaded into the directory by the administrator. After first boot, you cannot run the VM on any other machines.
+
[NOTE]
====
You need to prepare your Ignition file on a safe system. For example, another {ibm-name} Secure Execution guest.
====
+
For example:
+
[source,terminal]
----
{
  "ignition": { "version": "3.0.0" },
  "storage": {
    "files": [
      {
        "path": "/etc/se-hostkeys/ibm-z-hostkey-<your-hostkey>.crt",
        "contents": {
          "source": "data:;base64,<base64 encoded hostkey document>"
        },
        "mode": 420
      },
      {
        "path": "/etc/se-hostkeys/ibm-z-hostkey-<your-hostkey>.crt",
        "contents": {
          "source": "data:;base64,<base64 encoded hostkey document>"
        },
        "mode": 420
      }
    ]
  }
}
```
----
+
[NOTE]
====
You can add as many host keys as required if you want your node to be able to run on multiple {ibm-z-name} machines.
====
. To generate the Base64 encoded string, run the following command:
+
[source,terminal]
----
base64 <your-hostkey>.crt
----
+
Compared to guests not running {ibm-name} Secure Execution, the first boot of the machine is longer because the entire image is encrypted with a randomly generated LUKS passphrase before the Ignition phase.

. Add Ignition protection
+
To protect the secrets that are stored in the Ignition config file from being read or even modified, you must encrypt the Ignition config file.
+
[NOTE]
====
To achieve the desired security, Ignition logging and local login are disabled by default when running {ibm-name} Secure Execution.
====
.. Fetch the public GPG key for the `secex-qemu.qcow2` image and encrypt the Ignition config with the key by running the following command:
+
[source,terminal]
----
gpg --recipient-file /path/to/ignition.gpg.pub --yes --output /path/to/config.ign.gpg --verbose --armor --encrypt /path/to/config.ign
----

. Follow the fast-track installation of {op-system} to install nodes by using the {ibm-name} Secure Execution QCOW image.
+
[NOTE]
====
Before you start the VM, replace `serial=ignition` with `serial=ignition_crypted`, and add the `launchSecurity` parameter.
====

.Verification

When you have completed the fast-track installation of {op-system} and Ignition runs at the first boot, verify if decryption is successful.

** If the decryption is successful, you can expect an output similar to the following example:
+
.Example output
[source,terminal]
----
[    2.801433] systemd[1]: Starting coreos-ignition-setup-user.service - CoreOS Ignition User Config Setup...

[    2.803959] coreos-secex-ignition-decrypt[731]: gpg: key <key_name>: public key "Secure Execution (secex) 38.20230323.dev.0" imported
[    2.808874] coreos-secex-ignition-decrypt[740]: gpg: encrypted with rsa4096 key, ID <key_name>, created <yyyy-mm-dd>
[  OK  ] Finished coreos-secex-igni…S Secex Ignition Config Decryptor.
----

** If the decryption fails, you can expect an output similar to the following example:
+
.Example output
[source,terminal]
----
Starting coreos-ignition-s…reOS Ignition User Config Setup...
[    2.863675] coreos-secex-ignition-decrypt[729]: gpg: key <key_name>: public key "Secure Execution (secex) 38.20230323.dev.0" imported
[    2.869178] coreos-secex-ignition-decrypt[738]: gpg: encrypted with RSA key, ID <key_name>
[    2.870347] coreos-secex-ignition-decrypt[738]: gpg: public key decryption failed: No secret key
[    2.870371] coreos-secex-ignition-decrypt[738]: gpg: decryption failed: No secret key
----

[role="_additional-resources"]
.Additional resources

* Introducing {ibm-name} Secure Execution for Linux

* Linux as an {ibm-name} Secure Execution host or guest

* Setting up {ibm-name} Secure Execution on {ibm-z-title}

// Module included in the following assemblies:
//
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="configuring-luks-encryption-via-cex-ibm-z-linuxone-environment_{context}"]
= LUKS encryption via CEX in an {ibm-z-title} or {ibm-linuxone-title} environment

Enabling hardware-based Linux Unified Key Setup (LUKS) encryption via {ibm-name} Crypto Express (CEX) in an {ibm-z-name} or {ibm-linuxone-name} environment requires additional steps, which are described in detail in this section.

.Prerequisites

* You have installed the `butane` utility.
* You have reviewed the instructions for how to create machine configs with Butane.

.Procedure

. Create Butane configuration files for the control plane and compute nodes:
** Create a file named `main-storage.bu` by using the following Butane configuration for a control plane node with disk encryption, for example:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: main-storage
  labels:
    machineconfiguration.openshift.io/role: master
boot_device:
  layout: s390x-virt
  luks:
    cex:
      enabled: true
openshift:
  fips: true # <1>
  kernel_arguments:
    - rd.luks.key=/etc/luks/cex.key # <2>
----
<1> Specifies whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.
<2> Specifies the location of the key that is required to decrypt the device. You can not change this value.
. Choose the appropriate method to create Butane configuration files for the control plane and compute nodes:
** For installations on DASD-type disks, create a file named `main-storage.bu` by using the following Butane configuration for a control plane node with disk encryption, for example:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: main-storage
  labels:
    machineconfiguration.openshift.io/role: master
boot_device:
  layout: s390x-eckd
  luks:
    device: /dev/dasda
    cex:
      enabled: true
openshift:
  fips: true # <1>
  kernel_arguments:
    - rd.luks.key=/etc/luks/cex.key # <2>
----
<1> Specifies whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.
<2> Specifies the location of the key that is required to decrypt the device. You can not change this value.
+
** For installations on FCP-type disks, create a file named `main-storage.bu` by using the following Butane configuration for a control plane node with disk encryption, for example:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: main-storage
  labels:
    machineconfiguration.openshift.io/role: master
storage:
  filesystems:
    - device: /dev/mapper/root
      format: xfs
      label: root
      wipe_filesystem: true
  luks:
    - device: /dev/disk/by-label/root
      label: luks-root
      name: root
      wipe_volume: true
      cex:
        enabled: true
openshift:
  fips: true # <1>
  kernel_arguments:
    - rd.luks.key=/etc/luks/cex.key # <2>
----
<1> Specifies whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.
<2> Specifies the location of the key that is required to decrypt the device. You can not change this value.

. Create a parameter file that includes `ignition.platform.id=metal` and `ignition.firstboot`.
+
.Example kernel parameter file for the control plane machine
+
[source,terminal]
----
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
ignition.firstboot ignition.platform.id=metal \
coreos.inst.ignition_url=http://<http_server>/master.ign \// <1>
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \// <2>
ip=<ip_address>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
rd.zfcp=0.0.5677,0x600606680g7f0056,0x034F000000000000
----
<1> Specifies the location of the Ignition configuration file. Use `master.ign` or `worker.ign`. You can only use the HTTP and HTTPS protocols.
<2> Specifies the location of the `rootfs` artifact for the `kernel` and `initramfs` that you want to boot. You can only use the HTTP and HTTPS protocols.
[source,terminal]
----
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
coreos.inst.install_dev=/dev/disk/by-id/scsi-<serial_number> \// <1>
ignition.firstboot ignition.platform.id=metal \
coreos.inst.ignition_url=http://<http_server>/master.ign \// <2>
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \// <3>
ip=<ip_address>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
rd.zfcp=0.0.5677,0x600606680g7f0056,0x034F000000000000 <4>
----
<1> Specifies a unique fully qualified path depending on disk type. This can be DASD-type or FCP-type disks.
<2> Specifies the location of the Ignition configuration file. Use `master.ign` or `worker.ign`. You can only use the HTTP and HTTPS protocols.
<3> Specifies the location of the `rootfs` artifact for the `kernel` and `initramfs` that you want to boot. You can only use the HTTP and HTTPS protocols.
<4> Specifies the root device. For installations on DASD-type disks, replace with `rd.dasd=0.0.xxxx` to specify the DASD device.
+
[NOTE]
====
Write all options in the parameter file as a single line and make sure you have no newline characters.
====

// Module included in the following assemblies:
//
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="configuring-nbde-static-ip-ibm-z-linuxone-environment_{context}"]
= Configuring NBDE with static IP in an {ibm-z-title} or {ibm-linuxone-title} environment

Enabling NBDE disk encryption in an {ibm-z-name} or {ibm-linuxone-name} environment requires additional steps, which are described in detail in this section.

.Prerequisites

* You have set up the External Tang Server. See Network-bound disk encryption for instructions.
* You have installed the `butane` utility.
* You have reviewed the instructions for how to create machine configs with Butane.

.Procedure

. Create Butane configuration files for the control plane and compute nodes.
+
The following example of a Butane configuration for a control plane node creates a file named `master-storage.bu` for disk encryption:
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: master-storage
  labels:
    machineconfiguration.openshift.io/role: master
storage:
  luks:
    - clevis:
        tang:
          - thumbprint: QcPr_NHFJammnRCA3fFMVdNBwjs
            url: http://clevis.example.com:7500
      device: /dev/disk/by-partlabel/root # <1>
      device: /dev/disk/by-partlabel/root
      label: luks-root
      name: root
      wipe_volume: true
  filesystems:
    - device: /dev/mapper/root
      format: xfs
      label: root
      wipe_filesystem: true
openshift:
  fips: true # <2>
  fips: true # <1>
----
<1> Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.
<1> For installations on DASD-type disks, replace with `device: /dev/disk/by-label/root`.
<2> Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the {op-system-first} machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with {op-system} instead.

. Create a customized initramfs file to boot the machine, by running the following command:
+
[source,terminal]
----
$ coreos-installer pxe customize \
    /root/rhcos-bootfiles/rhcos-<release>-live-initramfs.s390x.img \
    --dest-device /dev/disk/by-id/scsi-<serial_number> --dest-karg-append \
    ip=<ip_address>::<gateway_ip>:<subnet_mask>::<network_device>:none \
    --dest-karg-append nameserver=<nameserver_ip> \
    --dest-karg-append rd.neednet=1 -o \
    /root/rhcos-bootfiles/<node_name>-initramfs.s390x.img
----
+
[NOTE]
====
Before first boot, you must customize the initramfs for each node in the cluster, and add PXE kernel parameters.
====

. Create a parameter file that includes `ignition.platform.id=metal` and `ignition.firstboot`.
+
.Example kernel parameter file for the control plane machine
+
[source,terminal]
----
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
coreos.inst.install_dev=/dev/<block_device> \// <1>
ignition.firstboot ignition.platform.id=metal \
coreos.inst.ignition_url=http://<http_server>/master.ign \// <2>
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \// <3>
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
rd.zfcp=0.0.5677,0x600606680g7f0056,0x034F000000000000 \// <4>
zfcp.allow_lun_scan=0
----
<1> Specify the block device type. For installations on DASD-type disks, specify `/dev/dasda`. For installations on FCP-type disks, specify `/dev/sda`.
<1> Specify the block device type. For installations on DASD-type disks, specify `/dev/dasda`. For installations on FCP-type disks, specify `/dev/sda`. For installations on NVMe-type disks, specify `/dev/nvme0n1`.
<2> Specify the location of the Ignition config file. Use `master.ign` or `worker.ign`. Only HTTP and HTTPS protocols are supported.
<3> Specify the location of the `rootfs` artifact for the `kernel` and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported.
<4> For installations on DASD-type disks, replace with `rd.dasd=0.0.xxxx` to specify the DASD device.
[source,terminal]
----
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
ignition.firstboot ignition.platform.id=metal \
coreos.inst.ignition_url=http://<http_server>/master.ign \// <1>
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \// <2>
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
rd.zfcp=0.0.5677,0x600606680g7f0056,0x034F000000000000 \
zfcp.allow_lun_scan=0
----
<1> Specify the location of the Ignition config file. Use `master.ign` or `worker.ign`. Only HTTP and HTTPS protocols are supported.
<2> Specify the location of the `rootfs` artifact for the `kernel` and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported.

+
[NOTE]
====
Write all options in the parameter file as a single line and make sure you have no newline characters.
====

[role="_additional-resources"]
.Additional resources

* Creating machine configs with Butane

// Module included in the following assemblies:
//
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc

[id="installation-user-infra-machines-iso-ibm-z_kvm_{context}"]
= Fast-track installation by using a prepackaged QCOW2 disk image

Complete the following steps to create the machines in a fast-track installation of {op-system-first}, importing a prepackaged {op-system-first} QEMU copy-on-write (QCOW2) disk image.

.Prerequisites

* At least one LPAR running on {op-system-base} 8.6 or later with KVM, referred to as {op-system-base} KVM host in this procedure.
* The KVM/QEMU hypervisor is installed on the {op-system-base} KVM host.
* A domain name server (DNS) that can perform hostname and reverse lookup for the nodes.
* A DHCP server that provides IP addresses.

.Procedure

. Obtain the {op-system-base} QEMU copy-on-write (QCOW2) disk image file from the Product Downloads page on the Red Hat Customer Portal or from the {op-system} image mirror page.
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform.
You must download images with the highest version that is less than or equal
to the OpenShift Container Platform version that you install. Only use the appropriate {op-system} QCOW2 image described in the following procedure.
====
+
. Download the QCOW2 disk image and Ignition files to a common directory on the {op-system-base} KVM host.
+
For example: `/var/lib/libvirt/images`
+
[NOTE]
====
The Ignition files are generated by the OpenShift Container Platform installer.
====
. Create a new disk image with the QCOW2 disk image backing file for each KVM guest node.
+
[source,terminal]
----
$ qemu-img create -f qcow2 -F qcow2 -b /var/lib/libvirt/images/{source_rhcos_qemu} /var/lib/libvirt/images/{vmname}.qcow2 {size}
----
+
. Create the new KVM guest nodes using the Ignition file and the new disk image.
+
[source,terminal]
----
$ virt-install --noautoconsole \
   --connect qemu:///system \
   --name <vm_name> \
   --memory <memory_mb> \
   --vcpus <vcpus> \
   --disk <disk> \
   --launchSecurity type="s390-pv" \ <1>
   --import \
   --network network=<virt_network_parm>,mac=<mac_address> \
   --disk path=<ign_file>,format=raw,readonly=on,serial=ignition,startup_policy=optional <2>
----
<1> If {ibm-name} Secure Execution is enabled, add the `launchSecurity type="s390-pv"` parameter.
<2> If {ibm-name} Secure Execution is enabled, replace `serial=ignition` with `serial=ignition_crypted`.

// Module included in the following assemblies:
//
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc

[id="installation-user-infra-machines-iso-ibm-z-kvm-full_{context}"]
= Full installation on a new QCOW2 disk image

Complete the following steps to create the machines in a full installation on a new QEMU copy-on-write (QCOW2) disk image.

.Prerequisites

* At least one LPAR running  on {op-system-base} 8.6 or later with KVM, referred to as {op-system-base} KVM host in this procedure.
* The KVM/QEMU hypervisor is installed on the {op-system-base} KVM host.
* A domain name server (DNS) that can perform hostname and reverse lookup for the nodes.
* An HTTP or HTTPS server is set up.

.Procedure

. Obtain the {op-system-base} kernel, initramfs, and rootfs files from the Product Downloads page on the Red Hat Customer Portal or from the {op-system} image mirror page.
+
[IMPORTANT]
====
The {op-system} images might not change with every release of OpenShift Container Platform.
You must download images with the highest version that is less than or equal
to the OpenShift Container Platform version that you install. Only use the appropriate {op-system} QCOW2 image described in the following procedure.
====
+
The file names contain the OpenShift Container Platform version number. They resemble the following examples:

** kernel: `rhcos-<version>-live-kernel-<architecture>`
** initramfs: `rhcos-<version>-live-initramfs.<architecture>.img`
** rootfs: `rhcos-<version>-live-rootfs.<architecture>.img`
+
. Move the downloaded {op-system-base} live kernel, initramfs, and rootfs as well as the Ignition files to an HTTP or HTTPS server before you launch `virt-install`.
+
[NOTE]
====
The Ignition files are generated by the OpenShift Container Platform installer.
====
. Create the new KVM guest nodes using the {op-system-base} kernel, initramfs, and Ignition files, the new disk image, and adjusted parm line arguments.
+
[source,terminal]
----
$ virt-install \
   --connect qemu:///system \
   --name <vm_name> \
   --memory <memory_mb> \
   --vcpus <vcpus> \
   --location <media_location>,kernel=<rhcos_kernel>,initrd=<rhcos_initrd> \ / <1>
   --disk <vm_name>.qcow2,size=<image_size>,cache=none,io=native \
   --network network=<virt_network_parm> \
   --boot hd \
   --extra-args "rd.neednet=1" \
   --extra-args "coreos.inst.install_dev=/dev/<block_device>" \
   --extra-args "coreos.inst.ignition_url=http://<http_server>/bootstrap.ign" \// <2>
   --extra-args "coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img" \// <3>
   --extra-args "ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns>" \
   --noautoconsole \
   --wait
----
<1> For the `--location` parameter, specify the location of the kernel/initrd on the HTTP or HTTPS server.
<2> Specify the location of the Ignition config file. Use `bootstrap.ign`, `master.ign`, or `worker.ign`. Only HTTP and HTTPS protocols are supported.
<3> Specify the location of the `rootfs` artifact for the `kernel` and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="installation-user-infra-machines-routing-bonding_{context}"]
= Networking and bonding options for ISO installations
= Networking options for ISO installations

[role="_abstract"]
You can configure advanced options so that you can modify the {op-system-first} manual installation process. The subsequent sections show examples of networking options for an ISO installation.

If you install {op-system} from an ISO image, you can add kernel arguments manually when you boot the image to configure networking for a node. If no networking arguments are specified, DHCP is activated in the initramfs when {op-system} detects that networking is required to fetch the Ignition config file.

[IMPORTANT]
====
When adding networking arguments manually, you must also add the `rd.neednet=1` kernel argument to bring the network up in the initramfs.
====

The following information provides examples for configuring networking and bonding on your {op-system} nodes for ISO installations. The examples describe how to use the `ip=`, `nameserver=`, and `bond=` kernel arguments.

[NOTE]
====
Ordering is important when adding the kernel arguments: `ip=`, `nameserver=`, and then `bond=`.
====

The networking options are passed to the `dracut` tool during system boot. For more information about the networking options supported by `dracut`, see `dracut.cmdline` manual page.

The following information provides examples for configuring networking on your {op-system} nodes for ISO installations. The examples describe how to use the `ip=` and `nameserver=` kernel arguments.

[NOTE]
====
Ordering is important when adding the kernel arguments: `ip=` and `nameserver=`.
====

The networking options are passed to the `dracut` tool during system boot. For more information about the networking options supported by `dracut`, see the `dracut.cmdline` manual page.

[role="_additional-resources"]
.Additional resources

* `dracut.cmdline` manual page

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="configuring-dhcp-or-static-ip-addresses_{context}"]
= Configuring DHCP or static IP addresses

[role="_abstract"]
You can configure an IP address by using either DHCP or an individual static IP address. If you set a static IP, you must then identify the DNS server IP address on each node.

The configuration examples in the procedure, update the IP addresses for the following components:

* The node's IP address to `10.10.10.2`
* The gateway address to `10.10.10.254`
* The netmask to `255.255.255.0`
* The hostname to `core0.example.com`
* The DNS server address to `4.4.4.41`
* The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

.Procedure

. Enter a command like the following command to configure a static IP address:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
nameserver=4.4.4.41
----

. Enter a command like the following command to configure a DHCP IP address:
+
[source,terminal]
----
ip=enp1s0:dhcp
----
+
[NOTE]
====
When you use DHCP to configure IP addressing for the {op-system} machines, the machines also obtain the DNS server information through DHCP. For DHCP-based deployments, you can define the DNS server address that is used by the {op-system} nodes through your DHCP server configuration.
====

. If two or more network interfaces and only one interface exists, disable DHCP on a single interface. In the example, the `enp1s0` interface has a static networking configuration and DHCP is disabled for `enp2s0`, which is not used:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
ip=::::core0.example.com:enp2s0:none
----

. If you need to combine DHCP and static IP configurations on systems with multiple network interfaces, run the following example command:
+
[source,terminal]
----
ip=enp1s0:dhcp
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="configuring-ip-address-without-static-hostname_{context}"]
= Configuring an IP address without a static hostname

[role="_abstract"]
You can configure an IP address without assigning a static hostname. If a static hostname is not set by the user, the static hostname gets picked up and automatically set by a reverse DNS lookup.

The configuration examples in the procedure, update the IP addresses for the following components:

* The node's IP address to `10.10.10.2`
* The gateway address to `10.10.10.254`
* The netmask to `255.255.255.0`
* The DNS server address to `4.4.4.41`
* The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

.Procedure

* To configure an IP address without a static hostname, enter a command like the following command:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0::enp1s0:none
nameserver=4.4.4.41
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="specifying-multiple-network-interfaces_{context}"]
= Specifying multiple network interfaces and DNS servers

[role="_abstract"]
You can specify multiple network interfaces by setting multiple `ip=` entries. You can provide multiple DNS servers by adding a `nameserver=` entry for each server,

.Procedure

* To specify multiple network interfaces for your interfaces, you can enter a command like the following command:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
ip=10.10.10.3::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
----

* To provide multiple DNS servers by adding a `nameserver=` entry for each server, enter a command like the following command:
+
[source,terminal]
----
nameserver=1.1.1.1
nameserver=8.8.8.8
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="configuring-default-gateway-route_{context}"]
= Configuring default gateway and route

[role="_abstract"]
As an optional task, you can configure routes to additional networks by setting an `rd.route=` value.

[NOTE]
====
When you configure one or multiple networks, one default gateway is required. If the additional network gateway is different from the primary network gateway, the default gateway must be the primary network gateway.
====

.Procedure

* To configure the default gateway, enter the following command:
+
[source,terminal]
----
ip=::10.10.10.254::::
----

* To configure the route for an additional network, enter the following command:
+
[source,terminal]
----
rd.route=20.20.20.0/24:20.20.20.254:enp2s0
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="configuring-vlans-individual-interfaces_{context}"]
= Configuring VLANs on individual interfaces

[role="_abstract"]
As an optional task, you can configure VLANs on individual interfaces by using the `vlan=` parameter.

.Procedure

* To configure a VLAN on a network interface and use a static IP address, run the following command:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0.100:none
vlan=enp2s0.100:enp2s0
----

* To configure a VLAN on a network interface and to use DHCP, run the following command:
+
[source,terminal]
----
ip=enp2s0.100:dhcp
vlan=enp2s0.100:enp2s0
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="bonding-multiple-network-interfaces-to-single-interface_{context}"]
= Bonding multiple network interfaces to a single interface

[role="_abstract"]
As an optional task, you can bond multiple network interfaces to a single interface by using the `bond=` option.

The following example demonstrates editing the `/etc/config/network` file and specifying the following syntax for bonding multiple network interfaces to a single interface:

[source,terminal]
----
bond=<name>[:<network_interfaces>][:<options>]
----
* `<name>`: Specifies the bonding device name, for example `bond0`.
* `<network_interfaces>`: Specifies a comma-separated list of physical (ethernet) interfaces, such as `em1,em2`.
* `<options>: Specifies a comma-separated list of bonding options. Enter the `modinfo bonding` command to see available options.

When you create a bonded interface using the `bond=` command, you must specify how the IP address is assigned and other information for the bonded interface.

.Procedure

* To configure the bonded interface to use DHCP, edit the `/etc/config/network` file by setting the IP address for the bond to `dhcp`. For example:
+
[source,terminal]
----
ip=bond0:dhcp
----

* To configure the bonded interface to use a static IP address, edit the `/etc/config/network` file entering the specific IP address you want and related information. For example:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
----
[source,terminal]
----
bond=bond0:em1,em2:mode=active-backup
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none::AA:BB:CC:DD:EE:FF ip=em1:none::AA:BB:CC:DD:EE:FF
ip=em2:none::AA:BB:CC:DD:EE:FF
----
+
{ibm-z-title} supports value `1` for the `fail_over_mac` parameter, so always set the `fail_over_mac=1` option in active-backup mode to avoid problems when shared OSA/RoCE cards are used.

* You can configure VLANs on bonded interfaces by editing the `/etc/config/network` file and specifying the `vlan=` parameter to use DHCP. For example:
+
[source,terminal]
----
ip=bond0.100:dhcp
bond=bond0:em1,em2:mode=active-backup
vlan=bond0.100:bond0
----

* To configure the bonded interface with a VLAN, edit the `/etc/config/network` file and specify a static IP address. For example:
+
[source,terminal]
----
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0.100:none
bond=bond0:em1,em2:mode=active-backup
vlan=bond0.100:bond0
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc

[id="bonding-multiple-sriov-network-interfaces-to-dual-port_{context}"]
= Bonding multiple SR-IOV network interfaces to a dual port NIC interface
= Using network teaming

[role="_abstract"]
You can bond multiple SR-IOV network interfaces to a dual port NIC interface by using the `bond=` option. Ensure you apply the procedure tasks to each node.
You can use network teaming as an alternative to bonding by using the `team=` parameter.

.Procedure

. Create the SR-IOV virtual functions (VFs) following the guidance in Managing SR-IOV devices. Follow the procedure in the "Attaching SR-IOV networking devices to virtual machines" section.
. Create the SR-IOV virtual functions (VFs).

. Create the bond, attach the desired VFs to the bond and set the bond link state up following the guidance in Configuring network bonding. Follow any of the described procedures to create the bond.
+
The following examples illustrate the syntax you must use:
+
* The syntax for configuring a bonded interface is `bond=<name>[:<network_interfaces>][:options]`.
+
`<name>` is the bonding device name (`bond0`), `<network_interfaces>` represents the virtual functions (VFs) by their known name in the kernel and shown in the output of the `ip link` command(`eno1f0`, `eno2f0`), and _options_ is a comma-separated list of bonding options. Enter `modinfo bonding` to see available options.
+
* When you create a bonded interface using `bond=`, you must specify how the IP address is assigned and other information for the bonded interface.
+
** To configure the bonded interface to use DHCP, set the bond's IP address to `dhcp`. For example:
+
[source,terminal]
----
bond=bond0:eno1f0,eno2f0:mode=active-backup
ip=bond0:dhcp::AA:BB:CC:DD:EE:FF
ip=eno1f0:none::AA:BB:CC:DD:EE:FF
ip=eno2f0:none::AA:BB:CC:DD:EE:FF
----
+
** To configure the bonded interface to use a static IP address, enter the specific IP address you want and related information. For example:
+
[source,terminal]
----
bond=bond0:eno1f0,eno2f0:mode=active-backup
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
----

. Optional: You can use network teaming as an alternative to bonding by using the `team=` parameter.
+
* The syntax for configuring a team interface is: `team=name[:network_interfaces]`
+
_name_ is the team device name (`team0`) and _network_interfaces_ represents a comma-separated list of physical (ethernet) interfaces (`em1, em2`).
+
[NOTE]
====
Teaming is planned to be deprecated when {op-system} switches to an upcoming version of {op-system-base}. For more information, see this https://access.redhat.com/solutions/6509691[Red Hat Knowledgebase Article].
====
+
Use the following example to configure a network team:
+
[source,terminal]
----
team=team0:em1,em2
ip=team0:dhcp
----

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-installing-bare-metal_{context}"]
= Waiting for the bootstrap process to complete

[role="_abstract"]
The OpenShift Container Platform bootstrap process begins after the cluster nodes first boot into the persistent {op-system} environment that has been installed to disk. The configuration information provided through the Ignition config files is used to initialize the bootstrap process and install OpenShift Container Platform on the machines. You must wait for the bootstrap process to complete.

.Prerequisites

* You have created the Ignition config files for your cluster.
* You have configured suitable network, DNS, and load balancing infrastructure.
* You have obtained the installation program and generated the Ignition config files for your cluster.
* You installed {op-system} on your cluster machines and provided the Ignition config files that the OpenShift Container Platform installation program generated.
* Your machines have direct internet access or have an HTTP or HTTPS proxy available.

.Procedure

. Monitor the bootstrap process:
+
[source,terminal]
----
$ ./openshift-install --dir <installation_directory> wait-for bootstrap-complete \
    --log-level=info
----
+
where:
+
`<installation_directory>`:: Specifies the path to the directory that stores the installation files.
`--log-level=info`:: Specifies `warn`, `debug`, or `error` instead of `info` to view different installation details.
+
.Example output
[source,terminal]
----
INFO Waiting up to 30m0s for the Kubernetes API at https://api.test.example.com:6443...
INFO API v1.35.4 up
INFO Waiting up to 30m0s for bootstrapping to complete...
INFO It is now safe to remove the bootstrap resources
----
+
The command succeeds when the Kubernetes API server signals that it has been
bootstrapped on the control plane machines.

. After the bootstrap process is complete, remove the bootstrap machine from the
load balancer.
+
[IMPORTANT]
====
You must remove the bootstrap machine from the load balancer at this point. You
can also remove or reformat the bootstrap machine itself.
====

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
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-operators-config_{context}"]
= Initial Operator configuration

[role="_abstract"]
After the control plane initializes, you must immediately configure some Operators so that they all become available.

.Prerequisites

* Your control plane has initialized.

.Procedure

. Watch the cluster components come online:
+
[source,terminal]
----
$ watch -n5 oc get clusteroperators
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
authentication                             .0    True        False         False      19m
baremetal                                  .0    True        False         False      37m
cloud-credential                           .0    True        False         False      40m
cluster-autoscaler                         .0    True        False         False      37m
config-operator                            .0    True        False         False      38m
console                                    .0    True        False         False      26m
csi-snapshot-controller                    .0    True        False         False      37m
dns                                        .0    True        False         False      37m
etcd                                       .0    True        False         False      36m
image-registry                             .0    True        False         False      31m
ingress                                    .0    True        False         False      30m
insights                                   .0    True        False         False      31m
kube-apiserver                             .0    True        False         False      26m
kube-controller-manager                    .0    True        False         False      36m
kube-scheduler                             .0    True        False         False      36m
kube-storage-version-migrator              .0    True        False         False      37m
machine-api                                .0    True        False         False      29m
machine-approver                           .0    True        False         False      37m
machine-config                             .0    True        False         False      36m
marketplace                                .0    True        False         False      37m
monitoring                                 .0    True        False         False      29m
network                                    .0    True        False         False      38m
node-tuning                                .0    True        False         False      37m
openshift-apiserver                        .0    True        False         False      32m
openshift-controller-manager               .0    True        False         False      30m
openshift-samples                          .0    True        False         False      32m
operator-lifecycle-manager                 .0    True        False         False      37m
operator-lifecycle-manager-catalog         .0    True        False         False      37m
operator-lifecycle-manager-packageserver   .0    True        False         False      32m
service-ca                                 .0    True        False         False      38m
storage                                    .0    True        False         False      37m
----

. Configure the Operators that are not available.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="installation-registry-storage-config_{context}"]
= Image registry storage configuration

[role="_abstract"]
Amazon Web Services provides default storage, which means the Image Registry Operator is available after installation. However, if the Registry Operator cannot create an S3 bucket and automatically configure storage, you must manually configure registry storage.
[role="_abstract"]
The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="registry-configuring-storage-baremetal_{context}"]
= Configuring registry storage for bare metal and other manual installations

= Configuring registry storage for {ibm-z-title}

= Configuring registry storage for {ibm-power-title}

[role="_abstract"]
As a cluster administrator, following installation you must configure your registry to use storage.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have a cluster
* You have provisioned persistent storage for your cluster, such as {rh-storage-first}.
+
[IMPORTANT]
====
OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required.
====
+
* You must have a system with at least 100Gi capacity.

.Procedure

. To configure your registry to use storage, change the `spec.storage.pvc` in
the `configs.imageregistry/cluster` resource.
+
[NOTE]
====
When you use shared storage, review your security settings to prevent outside access.
====

. Verify that you do not have a registry pod:
+
[source,terminal]
----
$ oc get pod -n openshift-image-registry -l docker-registry=default
----
+
.Example output
[source,terminal]
----
No resources found in openshift-image-registry namespace
----
+
[NOTE]
=====
If you do have a registry pod in your output, you do not need to continue with this procedure.
=====
. Check the registry configuration:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io
----
+
.Example output
[source,yaml]
----
storage:
  pvc:
    claim:
----
+
Leave the `claim` field blank to allow the automatic creation of an
`image-registry-storage` PVC.
+
. Check the `clusteroperator` status:
+
[source,terminal]
----
$ oc get clusteroperator image-registry
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME             VERSION              AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
image-registry                    True        False         False      6h50m
----
+
. Ensure that your registry is set to managed to enable building and pushing of images.
+
* Run:
+
----
$ oc edit configs.imageregistry/cluster
----
+
Then, change the line
+
----
managementState: Removed
----
+
to
+
----
managementState: Managed
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-registry-storage-non-production_{context}"]
= Configuring storage for the image registry in non-production clusters

[role="_abstract"]
You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory. If you do so, all images are lost if you restart the registry.

.Procedure

* To set the image registry storage to an empty directory:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
----
+
[WARNING]
====
Configure this option only for non-production clusters.
====
+
If you run this command before the Image Registry Operator initializes its
components, the `oc patch` command fails with the following error:
+
[source,terminal]
----
Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
----
+
Wait a few minutes and run the command again.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-complete-user-infra_{context}"]
= Completing installation on user-provisioned infrastructure

[role="_abstract"]
To finalize the installation on user-provisioned infrastructure, complete the cluster deployment after configuring the Operators. This ensures the cluster is fully operational on the infrastructure that you provide.

.Prerequisites

* Your control plane has initialized.
* You have completed the initial Operator configuration.

.Procedure

. Confirm that all the cluster components are online with the following command:
+
[source,terminal]
----
$ watch -n5 oc get clusteroperators
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
authentication                             .0    True        False         False      19m
baremetal                                  .0    True        False         False      37m
cloud-credential                           .0    True        False         False      40m
cluster-autoscaler                         .0    True        False         False      37m
config-operator                            .0    True        False         False      38m
console                                    .0    True        False         False      26m
csi-snapshot-controller                    .0    True        False         False      37m
dns                                        .0    True        False         False      37m
etcd                                       .0    True        False         False      36m
image-registry                             .0    True        False         False      31m
ingress                                    .0    True        False         False      30m
insights                                   .0    True        False         False      31m
kube-apiserver                             .0    True        False         False      26m
kube-controller-manager                    .0    True        False         False      36m
kube-scheduler                             .0    True        False         False      36m
kube-storage-version-migrator              .0    True        False         False      37m
machine-api                                .0    True        False         False      29m
machine-approver                           .0    True        False         False      37m
machine-config                             .0    True        False         False      36m
marketplace                                .0    True        False         False      37muser
monitoring                                 .0    True        False         False      29m
network                                    .0    True        False         False      38m
node-tuning                                .0    True        False         False      37m
openshift-apiserver                        .0    True        False         False      32muser
openshift-controller-manager               .0    True        False         False      30m
openshift-samples                          .0    True        False         False      32m
operator-lifecycle-manager                 .0    True        False         False      37m
operator-lifecycle-manager-catalog         .0    True        False         False      37m
operator-lifecycle-manager-packageserver   .0    True        False         False      32m
service-ca                                 .0    True        False         False      38m
storage                                    .0    True        False         False      37m
----
+
Alternatively, the following command notifies you when all of the clusters are available. The command also retrieves and displays credentials:
+
[source,terminal]
----
$ ./openshift-install --dir <installation_directory> wait-for install-complete
----
+
where:
+
`<installation_directory>`:: Specifies the path to the directory that you
stored the installation files in.
+
.Example output
[source,terminal]
----
INFO Waiting up to 30m0s for the cluster to initialize...
----
+
The command succeeds when the Cluster Version Operator finishes deploying the
OpenShift Container Platform cluster from Kubernetes API server.
+
[IMPORTANT]
====
* The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information.

* It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
====

. Confirm that the Kubernetes API server is communicating with the pods.
+
.. To view a list of all pods, use the following command:
+
[source,terminal]
----
$ oc get pods --all-namespaces
----
+
.Example output
[source,terminal]
----
NAMESPACE                         NAME                                            READY   STATUS      RESTARTS   AGE
openshift-apiserver-operator      openshift-apiserver-operator-85cb746d55-zqhs8   1/1     Running     1          9m
openshift-apiserver               apiserver-67b9g                                 1/1     Running     0          3m
openshift-apiserver               apiserver-ljcmx                                 1/1     Running     0          1m
openshift-apiserver               apiserver-z25h4                                 1/1     Running     0          2m
openshift-authentication-operator authentication-operator-69d5d8bf84-vh2n8        1/1     Running     0          5m
----
+
.. View the logs for a pod that is listed in the output of the previous command by using the following command:
+
[source,terminal]
----
$ oc logs <pod_name> -n <namespace>
----
+
where:
+
`<namespace>`:: Specifies the pod name and namespace, as shown in the output of an earlier command.
+
If the pod logs display, the Kubernetes API server can communicate with the cluster machines.

. For an installation with Fibre Channel Protocol (FCP), additional steps are required to enable multipathing. Do not enable multipathing during installation.
. Additional steps are required to enable multipathing. Do not enable multipathing during installation.
+
See "Enabling multipathing with kernel arguments on {op-system}" in the _Postinstallation machine configuration tasks_ documentation for more information.

. Register your cluster on the Cluster registration page.

.Verification

If you have enabled secure boot during the OpenShift Container Platform bootstrap process, the following verification steps are required:

. Debug the node by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----
+
.Example output
[source,terminal]
----
chroot /host
----

. Confirm that secure boot is enabled by running the following command. Example output states `1` if secure boot is enabled and `0` if secure boot is not enabled.
+
[source,terminal]
----
$ cat /sys/firmware/ipl/secure
----

. List the re-IPL configuration by running the following command:
+
[source,terminal]
----
# lsreipl
----
+
.Example output for an FCP disk
[source,terminal,subs="attributes+"]
----
Re-IPL type: fcp
WWPN: 0x500507630400d1e3
LUN: 0x4001400e00000000
Device: 0.0.810e
bootprog: 0
br_lba: 0
Loadparm: ""
Bootparms: ""
clear: 0
----
+
.Example output for a DASD disk
[source,terminal,subs="attributes+"]
----
for DASD output:
Re-IPL type: ccw
Device: 0.0.525d
Loadparm: ""
clear: 0
----

. Shut down the node by running the following command:
+
[source,terminal]
----
sudo shutdown -h
----

. Initiate a boot from LPAR from the Hardware Management Console (HMC). See Initiating a secure boot from an LPAR in IBM documentation.

. When the node is back, check the secure boot status again.

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

* About remote health monitoring

* How to generate SOSREPORT within OpenShift Container Platform version 4 nodes without SSH

* Remote health reporting

[id="next-steps_ibm-z-kvm"]
== Next steps

* Customize your cluster
