---
title: "Installation requirements for user-provisioned infrastructure on AWS"
type: reference
domain: openshift
slug: installing-4-22-upi-aws-installation-reqs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/upi-aws-installation-reqs
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installation requirements for user-provisioned infrastructure on AWS

[id="upi-aws-installation-reqs"]
= Installation requirements for user-provisioned infrastructure on AWS

Before you begin an installation on infrastructure that you provision, be sure that your AWS environment meets the following installation requirements.

For a cluster that contains user-provisioned infrastructure, you must deploy all
of the required machines.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_z/installing-ibm-z-reqs.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="installation-machine-requirements_{context}"]
= Required machines for cluster installation

[role="_abstract"]
You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

[IMPORTANT]
====
For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.
====

.Minimum required hosts
[options="header"]
|===

|Hosts |Description

|One temporary bootstrap machine
|The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster
on the three control plane machines. You can remove the bootstrap machine after
you install the cluster.

|Three control plane machines
|The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane.

|At least two compute machines, which are also known as worker machines.
|The workloads requested by OpenShift Container Platform users run on the compute machines.

|===

[NOTE]
====
As an exception, you can run zero compute machines in a bare metal cluster that consists of three control plane machines only. This provides smaller, more resource efficient clusters for cluster administrators and developers to use for testing, development, and production. Running one compute machine is not supported.
====

[IMPORTANT]
====
To improve high availability of your cluster, distribute the control plane machines over different hypervisor instances on at least two physical machines.
To maintain high availability of your cluster, use separate physical hosts for
these cluster machines.
====

The bootstrap and control plane machines must use {op-system-first} as the operating system. However, the compute machines can choose between {op-system-first}, {op-system-base-full} 8.6 and later.
The bootstrap, control plane, and compute machines must use {op-system-first} as the operating system.

Note that {op-system} is based on {op-system-base-full} 9.8 and inherits all of its hardware certifications and requirements.
See Red Hat Enterprise Linux technology capabilities and limits.

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
// installing/installing_aws/installing-aws-china.adoc
// installing/installing_aws/installing-aws-customizations.adoc
// installing/installing_aws/installing-aws-government-region.adoc
// installing/installing_aws/installing-aws-private.adoc
// installing/installing_aws/installing-aws-secret-region.adoc
// installing/installing_aws/installing-aws-user-infra.adoc
// installing/installing_aws/installing-aws-vpc.adoc
// installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc

[id="installation-aws-tested-machine-types_{context}"]
= Tested instance types for AWS

The following Amazon Web Services (AWS) instance types have been tested with
OpenShift Container Platform.
OpenShift Container Platform for use with AWS Local Zones.
OpenShift Container Platform for use with AWS Wavelength Zones.

[NOTE]
====
Use the machine types included in the following charts for your AWS instances. If you use an instance type that is not listed in the chart, ensure that the instance size you use matches the minimum resource requirements that are listed in the section named "Minimum resource requirements for cluster installation".
====

.Machine types based on 64-bit x86 architecture
[%collapsible]
====

====
.Machine types based on 64-bit x86 architecture for AWS Local Zones
[%collapsible]
====
* `c5.*`
* `c5d.*`
* `m6i.*`
* `m5.*`
* `r5.*`
* `t3.*`
====
.Machine types based on 64-bit x86 architecture for AWS Wavelength Zones
[%collapsible]
====
* `r5.*`
* `t3.*`
====
.Machine types based on 64-bit x86 architecture for secret regions
[%collapsible]
====
* `c4.*`
* `c5.*`
* `i3.*`
* `m4.*`
* `m5.*`
* `r4.*`
* `r5.*`
* `t3.*`
====

// Module included in the following assemblies:
//
// installing/installing_aws/installing-aws-china.adoc
// installing/installing_aws/installing-aws-customizations.adoc
// installing/installing_aws/installing-aws-government-region.adoc
// installing/installing_aws/installing-aws-private.adoc
// installing/installing_aws/installing-aws-user-infra.adoc
// installing/installing_aws/installing-aws-vpc.adoc
// installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-arm-tested-machine-types_{context}"]
= Tested instance types for AWS on 64-bit ARM infrastructures

The following Amazon Web Services (AWS) 64-bit ARM instance types have been tested with OpenShift Container Platform.

[NOTE]
====
Use the machine types included in the following charts for your AWS ARM instances. If you use an instance type that is not listed in the chart, ensure that the instance size you use matches the minimum resource requirements that are listed in "Minimum resource requirements for cluster installation".
====

.Machine types based on 64-bit ARM architecture
[%collapsible]
====

====

// Module included in the following assemblies:
//
// installing/installing_aws/installing-aws-user-infra.adoc
// installing/installing_aws/installing-restricted-networks-aws.adoc
// installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// installing/installing_azure/installing-azure-user-infra.adoc
// installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// installing/installing_bare_metal/upi/installing-bare-metal.adoc
// installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// installing/installing_gcp/installing-gcp-user-infra.adoc
// installing/installing_gcp/installing-restricted-networks-gcp.adoc
// installing/installing_ibm_power/installing-ibm-power.adoc
// installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// installing/installing_ibm_z/installing-ibm-z.adoc
// installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// machine_management/adding-rhel-compute.adoc
// machine_management/more-rhel-compute.adoc
// post_installation_configuration/node-tasks.adoc
// installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc

[id="csr-management_{context}"]
= Certificate signing requests management

[role="_abstract"]
On user-provisioned infrastructure, you must provide a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that is requested by using kubelet credentials because it cannot confirm that the correct machine issued the request. You must determine and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-user-infra-requirements_{context}"]
= Required AWS infrastructure components

To install OpenShift Container Platform on user-provisioned infrastructure in Amazon Web Services (AWS), you must manually create both the machines and their supporting infrastructure.

For more information about the integration testing for different platforms, see the OpenShift Container Platform 4.x Tested Integrations page.

By using the provided CloudFormation templates, you can create stacks of AWS resources that represent the following components:

* An AWS Virtual Private Cloud (VPC)
* Networking and load balancing components
* Security groups and roles
* An OpenShift Container Platform bootstrap node
* OpenShift Container Platform control plane nodes
* An OpenShift Container Platform compute node

Alternatively, you can manually create the components or you can reuse existing infrastructure that meets the cluster requirements. Review the CloudFormation templates for more details about how the components interrelate.

[id="installation-aws-user-infra-other-infrastructure_{context}"]
== Other infrastructure components

* A VPC
* DNS entries
* Load balancers (classic or network) and listeners
* A public and a private Route 53 zone
* Security groups
* IAM roles
* S3 buckets

If you are working in a disconnected environment, you are unable to reach the public IP addresses for EC2, ELB, and S3 endpoints. Depending on the level to which you want to restrict internet traffic during the installation, the following configuration options are available:

[id="create-vpc-endpoints_{context}"]
=== Option 1: Create VPC endpoints

Create a VPC endpoint and attach it to the subnets that the clusters are using. Name the endpoints as follows:

* `ec2.<aws_region>.amazonaws.com`
* `elasticloadbalancing.<aws_region>.amazonaws.com`
* `s3.<aws_region>.amazonaws.com`

With this option, network traffic remains private between your VPC and the required AWS services.

[id="create-proxy-without-vpc-endpoints_{context}"]
=== Option 2: Create a proxy without VPC endpoints
As part of the installation process, you can configure an HTTP or HTTPS proxy. With this option, internet traffic goes through the proxy to reach the required AWS services.

[id="create-proxy-with-vpc-endpoints_{context}"]
=== Option 3: Create a proxy with VPC endpoints
As part of the installation process, you can configure an HTTP or HTTPS proxy with VPC endpoints. Create a VPC endpoint and attach it to the subnets that the clusters are using. Name the endpoints as follows:

* `ec2.<aws_region>.amazonaws.com`
* `elasticloadbalancing.<aws_region>.amazonaws.com`
* `s3.<aws_region>.amazonaws.com`

When configuring the proxy in the `install-config.yaml` file, add these endpoints to the `noProxy` field. With this option, the proxy prevents the cluster from accessing the internet directly. However, network traffic remains private between your VPC and the required AWS services.

.Required VPC components

You must provide a suitable VPC and subnets that allow communication to your
machines.

[cols="2a,7a,3a,3a",options="header"]
|===

|Component
|AWS type
2+|Description

|VPC
|* `AWS::EC2::VPC`
* `AWS::EC2::VPCEndpoint`
2+|You must provide a public VPC for the cluster to use. The VPC uses an
endpoint that references the route tables for each subnet to improve communication with the registry that is hosted in S3.

|Public subnets
|* `AWS::EC2::Subnet`
* `AWS::EC2::SubnetNetworkAclAssociation`
2+|Your VPC must have public subnets for between 1 and 3 availability zones
and associate them with appropriate Ingress rules.

|Internet gateway
|
* `AWS::EC2::InternetGateway`
* `AWS::EC2::VPCGatewayAttachment`
* `AWS::EC2::RouteTable`
* `AWS::EC2::Route`
* `AWS::EC2::SubnetRouteTableAssociation`
* `AWS::EC2::NatGateway`
* `AWS::EC2::EIP`
2+|You must have a public internet gateway, with public routes, attached to the
VPC. In the provided templates, each public subnet has a NAT gateway with an EIP address. These NAT gateways allow cluster resources, like private subnet instances, to reach the internet and are not required for some restricted network or proxy scenarios.

.7+|Network access control
.7+| * `AWS::EC2::NetworkAcl`
* `AWS::EC2::NetworkAclEntry`
2+|You must allow the VPC to access the following ports:
h|Port
h|Reason

|`80`
|Inbound HTTP traffic

|`443`
|Inbound HTTPS traffic

|`22`
|Inbound SSH traffic

|`1024` - `65535`
|Inbound ephemeral traffic

|`0` - `65535`
|Outbound ephemeral traffic

|Private subnets
|* `AWS::EC2::Subnet`
* `AWS::EC2::RouteTable`
* `AWS::EC2::SubnetRouteTableAssociation`
2+|Your VPC can have private subnets. The provided CloudFormation templates
can create private subnets for between 1 and 3 availability zones.
If you use private subnets, you must provide appropriate routes and tables
for them.

|===

.Required DNS and load balancing components

Your DNS and load balancer configuration needs to use a public hosted zone and
can use a private hosted zone similar to the one that the installation program
uses if it provisions the cluster's infrastructure. You must
create a DNS entry that resolves to your load balancer. An entry for
`api.<cluster_name>.<domain>` must point to the external load balancer, and an
entry for `api-int.<cluster_name>.<domain>` must point to the internal load
balancer.

The cluster also requires load balancers and listeners for port 6443, which are
required for the Kubernetes API and its extensions, and port 22623, which are
required for the Ignition config files for new machines. The targets will be the
control plane nodes. Port 6443 must be accessible to both clients external to the
cluster and nodes within the cluster. Port 22623 must be accessible to nodes
within the cluster.

[cols="2a,2a,8a",options="header"]
|===

|Component
|AWS type
|Description

|DNS
|`AWS::Route53::HostedZone`
|The hosted zone for your internal DNS.

|Public load balancer
|`AWS::ElasticLoadBalancingV2::LoadBalancer`
|The load balancer for your public subnets.

|External API server record
|`AWS::Route53::RecordSetGroup`
|Alias records for the external API server.

|External listener
|`AWS::ElasticLoadBalancingV2::Listener`
|A listener on port 6443 for the external load balancer.

|External target group
|`AWS::ElasticLoadBalancingV2::TargetGroup`
|The target group for the external load balancer.

|Private load balancer
|`AWS::ElasticLoadBalancingV2::LoadBalancer`
|The load balancer for your private subnets.

|Internal API server record
|`AWS::Route53::RecordSetGroup`
|Alias records for the internal API server.

|Internal listener
|`AWS::ElasticLoadBalancingV2::Listener`
|A listener on port 22623 for the internal load balancer.

|Internal target group
|`AWS::ElasticLoadBalancingV2::TargetGroup`
|The target group for the internal load balancer.

|Internal listener
|`AWS::ElasticLoadBalancingV2::Listener`
|A listener on port 6443 for the internal load balancer.

|Internal target group
|`AWS::ElasticLoadBalancingV2::TargetGroup`
|The target group for the internal load balancer.

|===

.Security groups

The control plane and worker machines require access to the following ports:

[cols="2a,2a,2a,2a",options="header"]
|===

|Group
|Type
|IP Protocol
|Port range

.4+|`MasterSecurityGroup`
.4+|`AWS::EC2::SecurityGroup`
|`icmp`
|`0`

|`tcp`
|`22`

|`tcp`
|`6443`

|`tcp`
|`22623`

.2+|`WorkerSecurityGroup`
.2+|`AWS::EC2::SecurityGroup`
|`icmp`
|`0`

|`tcp`
|`22`

.2+|`BootstrapSecurityGroup`
.2+|`AWS::EC2::SecurityGroup`

|`tcp`
|`22`

|`tcp`
|`19531`

|===

.Control plane Ingress

The control plane machines require the following Ingress groups. Each Ingress group is
a `AWS::EC2::SecurityGroupIngress` resource.

[cols="2a,5a,2a,2a",options="header"]
|===

|Ingress group
|Description
|IP protocol
|Port range

|`MasterIngressEtcd`
|etcd
|`tcp`
|`2379`- `2380`

|`MasterIngressVxlan`
|Vxlan packets
|`udp`
|`6081`

|`MasterIngressWorkerVxlan`
|Vxlan packets
|`udp`
|`6081`

|`MasterIngressInternal`
|Internal cluster communication and Kubernetes proxy metrics
|`tcp`
|`9000` - `9999`

|`MasterIngressWorkerInternal`
|Internal cluster communication
|`tcp`
|`9000` - `9999`

|`MasterIngressKube`
|Kubernetes kubelet, scheduler and controller manager
|`tcp`
|`10250` - `10259`

|`MasterIngressWorkerKube`
|Kubernetes kubelet, scheduler and controller manager
|`tcp`
|`10250` - `10259`

|`MasterIngressIngressServices`
|Kubernetes Ingress services
|`tcp`
|`30000` - `32767`

|`MasterIngressWorkerIngressServices`
|Kubernetes Ingress services
|`tcp`
|`30000` - `32767`

|`MasterIngressGeneve`
|Geneve packets
|`udp`
|`6081`

|`MasterIngressWorkerGeneve`
|Geneve packets
|`udp`
|`6081`

|`MasterIngressIpsecIke`
|IPsec IKE packets
|`udp`
|`500`

|`MasterIngressWorkerIpsecIke`
|IPsec IKE packets
|`udp`
|`500`

|`MasterIngressIpsecNat`
|IPsec NAT-T packets
|`udp`
|`4500`

|`MasterIngressWorkerIpsecNat`
|IPsec NAT-T packets
|`udp`
|`4500`

|`MasterIngressIpsecEsp`
|IPsec ESP packets
|`50`
|`All`

|`MasterIngressWorkerIpsecEsp`
|IPsec ESP packets
|`50`
|`All`

|`MasterIngressInternalUDP`
|Internal cluster communication
|`udp`
|`9000` - `9999`

|`MasterIngressWorkerInternalUDP`
|Internal cluster communication
|`udp`
|`9000` - `9999`

|`MasterIngressIngressServicesUDP`
|Kubernetes Ingress services
|`udp`
|`30000` - `32767`

|`MasterIngressWorkerIngressServicesUDP`
|Kubernetes Ingress services
|`udp`
|`30000` - `32767`

|===

.Worker Ingress

The worker machines require the following Ingress groups. Each Ingress group is
a `AWS::EC2::SecurityGroupIngress` resource.

[cols="2a,5a,2a,2a",options="header"]
|===

|Ingress group
|Description
|IP protocol
|Port range

|`WorkerIngressVxlan`
|Vxlan packets
|`udp`
|`6081`

|`WorkerIngressWorkerVxlan`
|Vxlan packets
|`udp`
|`6081`

|`WorkerIngressInternal`
|Internal cluster communication
|`tcp`
|`9000` - `9999`

|`WorkerIngressWorkerInternal`
|Internal cluster communication
|`tcp`
|`9000` - `9999`

|`WorkerIngressKube`
|Kubernetes kubelet, scheduler, and controller manager
|`tcp`
|`10250`

|`WorkerIngressWorkerKube`
|Kubernetes kubelet, scheduler, and controller manager
|`tcp`
|`10250`

|`WorkerIngressIngressServices`
|Kubernetes Ingress services
|`tcp`
|`30000` - `32767`

|`WorkerIngressWorkerIngressServices`
|Kubernetes Ingress services
|`tcp`
|`30000` - `32767`

|`WorkerIngressGeneve`
|Geneve packets
|`udp`
|`6081`

|`WorkerIngressMasterGeneve`
|Geneve packets
|`udp`
|`6081`

|`WorkerIngressIpsecIke`
|IPsec IKE packets
|`udp`
|`500`

|`WorkerIngressMasterIpsecIke`
|IPsec IKE packets
|`udp`
|`500`

|`WorkerIngressIpsecNat`
|IPsec NAT-T packets
|`udp`
|`4500`

|`WorkerIngressMasterIpsecNat`
|IPsec NAT-T packets
|`udp`
|`4500`

|`WorkerIngressIpsecEsp`
|IPsec ESP packets
|`50`
|`All`

|`WorkerIngressMasterIpsecEsp`
|IPsec ESP packets
|`50`
|`All`

|`WorkerIngressInternalUDP`
|Internal cluster communication
|`udp`
|`9000` - `9999`

|`WorkerIngressMasterInternalUDP`
|Internal cluster communication
|`udp`
|`9000` - `9999`

|`WorkerIngressIngressServicesUDP`
|Kubernetes Ingress services
|`udp`
|`30000` - `32767`

|`WorkerIngressMasterIngressServicesUDP`
|Kubernetes Ingress services
|`udp`
|`30000` - `32767`

|===

.Roles and instance profiles

You must grant the machines permissions in AWS. The provided CloudFormation
templates grant the machines `Allow` permissions for the following `AWS::IAM::Role` objects
and provide a `AWS::IAM::InstanceProfile` for each set of roles. If you do
not use the templates, you can grant the machines the following broad permissions
or the following individual permissions.

[cols="2a,2a,2a,2a",options="header"]
|===

|Role
|Effect
|Action
|Resource

.4+|Master
|`Allow`
|`ec2:*`
|`*`

|`Allow`
|`elasticloadbalancing:*`
|`*`

|`Allow`
|`iam:PassRole`
|`*`

|`Allow`
|`s3:GetObject`
|`*`

|Worker
|`Allow`
|`ec2:Describe*`
|`*`

.3+|Bootstrap
|`Allow`
|`ec2:Describe*`
|`*`

|`Allow`
|`ec2:AttachVolume`
|`*`

|`Allow`
|`ec2:DetachVolume`
|`*`

|`Allow`
|`s3:GetObject`
|`*`

|===

[id="installation-aws-user-infra-cluster-machines_{context}"]
== Cluster machines

You need `AWS::EC2::Instance` objects for the following machines:

* A bootstrap machine. This machine is required during installation, but you can remove it after your cluster deploys.
* Three control plane machines. The control plane machines are not governed by a control plane machine set.
* Compute machines. You must create at least two compute machines, which are also known as worker machines, during installation. These machines are not governed by a compute machine set.

You can also create and control them by using a MachineSet after your
control plane initializes and you can access the cluster API by using the `oc`
command-line interface.

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-account.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-aws-permissions_{context}"]
= Required {aws-short} permissions for the IAM user

[role="_abstract"]
To deploy all components of an OpenShift Container Platform cluster, you must grant the all the required permissions to the IAM user that you create in {aws-first}.

[NOTE]
====
Your IAM user must have the permission `tag:GetResources` in the region `us-east-1` to delete the base cluster resources. As part of the {aws-short} API requirement, the OpenShift Container Platform installation program performs various actions in this region.
====

When you attach the `AdministratorAccess` policy to the IAM user that you create in {aws-first}, you grant that user all of the required permissions. To deploy all components of an OpenShift Container Platform
cluster, the IAM user requires the following permissions:

.Required EC2 permissions for installation
[%collapsible]
====
* `ec2:AttachNetworkInterface`
* `ec2:AuthorizeSecurityGroupEgress`
* `ec2:AuthorizeSecurityGroupIngress`
* `ec2:CopyImage`
* `ec2:CreateNetworkInterface`
* `ec2:CreateSecurityGroup`
* `ec2:CreateTags`
* `ec2:CreateVolume`
* `ec2:DeleteSecurityGroup`
* `ec2:DeleteSnapshot`
* `ec2:DeleteTags`
* `ec2:DeregisterImage`
* `ec2:DescribeAccountAttributes`
* `ec2:DescribeAddresses`
* `ec2:DescribeAvailabilityZones`
* `ec2:DescribeDhcpOptions`
* `ec2:DescribeImages`
* `ec2:DescribeInstanceAttribute`
* `ec2:DescribeInstanceCreditSpecifications`
* `ec2:DescribeInstances`
* `ec2:DescribeInstanceTypes`
* `ec2:DescribeInstanceTypeOfferings`
* `ec2:DescribeInternetGateways`
* `ec2:DescribeKeyPairs`
* `ec2:DescribeNatGateways`
* `ec2:DescribeNetworkAcls`
* `ec2:DescribeNetworkInterfaces`
* `ec2:DescribePrefixLists`
* `ec2:DescribePublicIpv4Pools` (only required if `publicIpv4Pool` is specified in `install-config.yaml`)
* `ec2:DescribeRegions`
* `ec2:DescribeRouteTables`
* `ec2:DescribeSecurityGroupRules`
* `ec2:DescribeSecurityGroups`
* `ec2:DescribeSubnets`
* `ec2:DescribeTags`
* `ec2:DescribeVolumes`
* `ec2:DescribeVpcAttribute`
* `ec2:DescribeVpcClassicLink`
* `ec2:DescribeVpcClassicLinkDnsSupport`
* `ec2:DescribeVpcEndpoints`
* `ec2:DescribeVpcs`
* `ec2:DisassociateAddress` (only required if `publicIpv4Pool` is specified in `install-config.yaml`)
* `ec2:GetEbsDefaultKmsKeyId`
* `ec2:ModifyInstanceAttribute`
* `ec2:ModifyNetworkInterfaceAttribute`
* `ec2:RevokeSecurityGroupEgress`
* `ec2:RevokeSecurityGroupIngress`
* `ec2:RunInstances`
* `ec2:TerminateInstances`
====

.Required permissions for creating network resources during installation
[%collapsible]
====
* `ec2:AllocateAddress`
* `ec2:AssociateAddress`
* `ec2:AssociateDhcpOptions`
* `ec2:AssociateRouteTable`
* `ec2:AttachInternetGateway`
* `ec2:CreateDhcpOptions`
* `ec2:CreateInternetGateway`
* `ec2:CreateNatGateway`
* `ec2:CreateRoute`
* `ec2:CreateRouteTable`
* `ec2:CreateSubnet`
* `ec2:CreateVpc`
* `ec2:CreateVpcEndpoint`
* `ec2:ModifySubnetAttribute`
* `ec2:ModifyVpcAttribute`

[NOTE]
=====
If you use an existing Virtual Private Cloud (VPC), your account does not require these permissions for creating network resources.
=====
====

.Required Elastic Load Balancing permissions (ELB) for installation
[%collapsible]
====
* `elasticloadbalancing:AddTags`
* `elasticloadbalancing:ApplySecurityGroupsToLoadBalancer`
* `elasticloadbalancing:AttachLoadBalancerToSubnets`
* `elasticloadbalancing:ConfigureHealthCheck`
* `elasticloadbalancing:CreateListener`
* `elasticloadbalancing:CreateLoadBalancer`
* `elasticloadbalancing:CreateLoadBalancerListeners`
* `elasticloadbalancing:CreateTargetGroup`
* `elasticloadbalancing:DeleteLoadBalancer`
* `elasticloadbalancing:DeregisterInstancesFromLoadBalancer`
* `elasticloadbalancing:DeregisterTargets`
* `elasticloadbalancing:DescribeInstanceHealth`
* `elasticloadbalancing:DescribeListeners`
* `elasticloadbalancing:DescribeLoadBalancerAttributes`
* `elasticloadbalancing:DescribeLoadBalancers`
* `elasticloadbalancing:DescribeTags`
* `elasticloadbalancing:DescribeTargetGroupAttributes`
* `elasticloadbalancing:DescribeTargetHealth`
* `elasticloadbalancing:ModifyLoadBalancerAttributes`
* `elasticloadbalancing:ModifyTargetGroup`
* `elasticloadbalancing:ModifyTargetGroupAttributes`
* `elasticloadbalancing:RegisterInstancesWithLoadBalancer`
* `elasticloadbalancing:RegisterTargets`
* `elasticloadbalancing:SetLoadBalancerPoliciesOfListener`
* `elasticloadbalancing:SetSecurityGroups`

[IMPORTANT]
=====
OpenShift Container Platform uses both the ELB and ELBv2 API services to provision load balancers. The permission list shows permissions required by both services. A known issue exists in the {aws-short} web console where both services use the same `elasticloadbalancing` action prefix but do not recognize the same actions. You can ignore the warnings about the service not recognizing certain `elasticloadbalancing` actions.
=====
====

.Required IAM permissions for installation
[%collapsible]
====
* `iam:AddRoleToInstanceProfile`
* `iam:CreateInstanceProfile`
* `iam:CreateRole`
* `iam:DeleteInstanceProfile`
* `iam:DeleteRole`
* `iam:DeleteRolePolicy`
* `iam:GetInstanceProfile`
* `iam:GetRole`
* `iam:GetRolePolicy`
* `iam:GetUser`
* `iam:ListInstanceProfilesForRole`
* `iam:ListRoles`
* `iam:ListUsers`
* `iam:PassRole`
* `iam:PutRolePolicy`
* `iam:RemoveRoleFromInstanceProfile`
* `iam:SimulatePrincipalPolicy`
* `iam:TagInstanceProfile`
* `iam:TagRole`

[NOTE]
=====
* If you specify an existing IAM role in the `install-config.yaml` file, the following IAM permissions are not required: `iam:CreateRole`,`iam:DeleteRole`, `iam:DeleteRolePolicy`, and `iam:PutRolePolicy`.

* If you have not created a load balancer in your {aws-short} account, the IAM user also requires the `iam:CreateServiceLinkedRole` permission.
=====
====

.Required Route 53 permissions for installation
[%collapsible]
====
* `route53:ChangeResourceRecordSets`
* `route53:ChangeTagsForResource`
* `route53:CreateHostedZone`
* `route53:DeleteHostedZone`
* `route53:GetChange`
* `route53:GetHostedZone`
* `route53:ListHostedZones`
* `route53:ListHostedZonesByName`
* `route53:ListResourceRecordSets`
* `route53:ListTagsForResource`
* `route53:UpdateHostedZoneComment`
====

.Required Amazon Simple Storage Service (S3) permissions for installation
[%collapsible]
====
* `s3:CreateBucket`
* `s3:DeleteBucket`
* `s3:GetAccelerateConfiguration`
* `s3:GetBucketAcl`
* `s3:GetBucketCors`
* `s3:GetBucketLocation`
* `s3:GetBucketLogging`
* `s3:GetBucketObjectLockConfiguration`
* `s3:GetBucketPolicy`
* `s3:GetBucketRequestPayment`
* `s3:GetBucketTagging`
* `s3:GetBucketVersioning`
* `s3:GetBucketWebsite`
* `s3:GetEncryptionConfiguration`
* `s3:GetLifecycleConfiguration`
* `s3:GetReplicationConfiguration`
* `s3:ListBucket`
* `s3:PutBucketAcl`
* `s3:PutBucketPolicy`
* `s3:PutBucketTagging`
* `s3:PutEncryptionConfiguration`
====

.S3 permissions that cluster Operators require
[%collapsible]
====
* `s3:DeleteObject`
* `s3:GetObject`
* `s3:GetObjectAcl`
* `s3:GetObjectTagging`
* `s3:GetObjectVersion`
* `s3:PutObject`
* `s3:PutObjectAcl`
* `s3:PutObjectTagging`
====

.Required permissions to delete base cluster resources
[%collapsible]
====
* `autoscaling:DescribeAutoScalingGroups`
* `ec2:DeleteNetworkInterface`
* `ec2:DeletePlacementGroup`
* `ec2:DeleteVolume`
* `elasticloadbalancing:DeleteTargetGroup`
* `elasticloadbalancing:DescribeTargetGroups`
* `iam:DeleteAccessKey`
* `iam:DeleteUser`
* `iam:DeleteUserPolicy`
* `iam:ListAttachedRolePolicies`
* `iam:ListInstanceProfiles`
* `iam:ListRolePolicies`
* `iam:ListUserPolicies`
* `s3:DeleteObject`
* `s3:ListBucketVersions`
* `tag:GetResources`
====

.Required permissions to delete network resources
[%collapsible]
====
* `ec2:DeleteDhcpOptions`
* `ec2:DeleteInternetGateway`
* `ec2:DeleteNatGateway`
* `ec2:DeleteRoute`
* `ec2:DeleteRouteTable`
* `ec2:DeleteSubnet`
* `ec2:DeleteVpc`
* `ec2:DeleteVpcEndpoints`
* `ec2:DetachInternetGateway`
* `ec2:DisassociateRouteTable`
* `ec2:ReleaseAddress`
* `ec2:ReplaceRouteTableAssociation`

[NOTE]
=====
If you use an existing VPC, your account does not require these permissions to delete network resources. Instead, your account only requires the `tag:UntagResources` permission to delete network resources.
=====
====

.Optional permissions for installing a cluster with a custom Key Management Service (KMS) key
[%collapsible]
====
* `kms:CreateGrant`
* `kms:Decrypt`
* `kms:DescribeKey`
* `kms:Encrypt`
* `kms:GenerateDataKey`
* `kms:GenerateDataKeyWithoutPlainText`
* `kms:ListGrants`
* `kms:RevokeGrant`

[NOTE]
=====
If you provide an Amazon Machine Image (AMI) that is encrypted with a customer-managed key, you must provide the `kms:ReEncrypt*` permissions in addition to these permissions.
=====
====

.Required permissions to delete a cluster with shared instance roles
[%collapsible]
====
* `iam:UntagRole`
====

.Required permissions to delete a cluster with shared instance profiles
[%collapsible]
====
* `tag:UntagResources`
====

.Additional IAM and S3 permissions that are required to create manifests
[%collapsible]
====
* `iam:GetUserPolicy`
* `iam:ListAccessKeys`
* `iam:PutUserPolicy`
* `iam:TagUser`
* `s3:AbortMultipartUpload`
* `s3:GetBucketPublicAccessBlock`
* `s3:ListBucket`
* `s3:ListBucketMultipartUploads`
* `s3:PutBucketPublicAccessBlock`
* `s3:PutLifecycleConfiguration`

[NOTE]
=====
If you are managing your cloud provider credentials with mint mode, the IAM user also requires the `iam:CreateAccessKey` and `iam:CreateUser` permissions.
=====
====

.Optional permissions for instance and quota checks for installation
[%collapsible]
====
* `servicequotas:ListAWSDefaultServiceQuotas`
====

.Optional permissions for the cluster owner account when installing a cluster on a shared VPC
[%collapsible]
====
* `sts:AssumeRole`
====

.Required permissions for enabling Bring your own public IPv4 addresses (BYOIP) feature for installation
[%collapsible]
====
* `ec2:DescribePublicIpv4Pools`
* `ec2:DisassociateAddress`
====

.Required permissions to install a cluster with dual-stack networking
[%collapsible]
====
* `ec2:DescribeEgressOnlyInternetGateways`
* `ec2:CreateEgressOnlyInternetGateway`
====

.Required permissions to delete a cluster with dual-stack networking
[%collapsible]
====
* `ec2:DeleteEgressOnlyInternetGateway`
====

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc

[id="installation-aws-marketplace-subscribe_{context}"]
= Obtaining an AWS Marketplace image

If you are deploying an OpenShift Container Platform cluster using an AWS Marketplace image, you must first subscribe through AWS. Subscribing to the offer provides you with the AMI ID that the installation program uses to deploy compute nodes.

[NOTE]
====
====

.Prerequisites

* You have an AWS account to purchase the offer. This account does not have to be the same account that is used to install the cluster.

.Procedure

. Complete the OpenShift Container Platform subscription from the AWS Marketplace.
. Record the AMI ID for your specific AWS Region. As part of the installation process, you must update the `install-config.yaml` file with this value before deploying the cluster.
. Record the AMI ID for your specific AWS Region. If you use the CloudFormation template to deploy your compute nodes, you must update the `worker0.type.properties.ImageID` parameter with the AMI ID value.
+
.Sample `install-config.yaml` file with AWS Marketplace compute nodes

[source,yaml]
----
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    aws:
      amiID: ami-06c4d345f7c207239 <1>
      type: m5.4xlarge
  replicas: 3
metadata:
  name: test-cluster
platform:
  aws:
    region: us-east-2 <2>
sshKey: ssh-ed25519 AAAA...
pullSecret: '{"auths": ...}'
----
<1> The AMI ID from your AWS Marketplace subscription.
<2> Your AMI ID is associated with a specific AWS Region. When creating the installation configuration file, ensure that you select the same AWS Region that you specified when configuring your subscription.
