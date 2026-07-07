---
title: "Installing a cluster with compute nodes on AWS Local Zones"
type: reference
domain: openshift
slug: installing-4-22-installing-aws-localzone
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-aws-localzone
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster with compute nodes on AWS Local Zones

[id="installing-aws-localzone"]
= Installing a cluster with compute nodes on AWS Local Zones

You can quickly install an OpenShift Container Platform cluster on Amazon Web Services (AWS) {zone-type} by setting the zone names in the edge compute pool of the `install-config.yaml` file, or install a cluster in an existing Amazon Virtual Private Cloud (VPC) with Local Zone subnets.

AWS {zone-type} is an infrastructure that place Cloud Resources close to metropolitan regions. For more information, see the AWS Local Zones Documentation.

// Infrastructure prerequisites
[id="aws-zones-prerequisites_{context}"]
== Infrastructure prerequisites

* You reviewed details about OpenShift Container Platform installation and update processes.
* You are familiar with Selecting a cluster installation method and preparing it for users.
* You configured an AWS account to host the cluster.
+
[WARNING]
====
If you have an AWS profile stored on your computer, it must not use a temporary session token that you generated while using a multifactor authentication device. The cluster continues to use your current AWS credentials to create AWS resources for the entire life of the cluster, so you must use key-based, long-term credentials. To generate appropriate keys, see Managing Access Keys for IAM Users in the AWS documentation. You can supply the keys when you run the installation program.
====
* You downloaded the AWS CLI and installed it on your computer. See Install the AWS CLI Using the Bundled Installer (Linux, macOS, or UNIX) in the AWS documentation.
* If you use a firewall, you configured it to allow the sites that your cluster must access.
* You noted the region and supported AWS Local Zones locations to create the network resources in.
* You read the AWS Local Zones features in the AWS documentation.
* You added permissions for creating network resources that support AWS Local Zones to the Identity and Access Management (IAM) user or role. The following example enables a zone group that can give a user or role access for creating network resources that support AWS {zone-type}.
+
.Example of an additional IAM policy with the `ec2:ModifyAvailabilityZoneGroup` permission attached to an IAM user or role.
+
[source,yaml]
----
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ec2:ModifyAvailabilityZoneGroup"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
----

[id="installation-about-local-zone-edge-compute-pool_{context}"]
== About AWS Local Zones and edge compute pool

Read the following sections to understand infrastructure behaviors and cluster limitations in an AWS {zone-type} environment.

// Cluster limitations
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with worker nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with worker nodes on AWS Wavelength Zones)

[id="cluster-limitations-aws-zone_{context}"]
= Cluster limitations in AWS Local Zones

Some limitations exist when you try to deploy a cluster with a default installation configuration in an Amazon Web Services (AWS) Local Zone.
= Cluster limitations in AWS Wavelength Zones

Some limitations exist when you try to deploy a cluster with a default installation configuration in an Amazon Web Services (AWS) Wavelength Zone.

[IMPORTANT]
====
The following list details limitations when deploying a cluster in a pre-configured AWS zone:

- The maximum transmission unit (MTU) between an Amazon EC2 instance in a zone and an Amazon EC2 instance in the Region is `1300`. This causes the cluster-wide network MTU to change according to the network plugin that is used with the deployment.
- Network resources such as Network Load Balancer (NLB), Classic Load Balancer, and Network Address Translation (NAT) Gateways are not globally supported.
- For an OpenShift Container Platform cluster on AWS, the AWS Elastic Block Storage (EBS) `gp3` type volume is the default for node volumes and the default for the storage class. This volume type is not globally available on zone locations. By default, the nodes running in zones are deployed with the `gp2` EBS volume. The `gp2-csi` `StorageClass` parameter must be set when creating workloads on zone nodes.
====

If you want the installation program to automatically create Local Zone subnets for your OpenShift Container Platform cluster, specific configuration limitations apply with this method.

If you want the installation program to automatically create Wavelength Zone subnets for your OpenShift Container Platform cluster, specific configuration limitations apply with this method. The following note details some of these limitations. For other limitations, ensure that you read the "Quotas and considerations for Wavelength Zones" document that Red Hat provides in the "Infrastructure prerequisites" section.

[IMPORTANT]
====
The following configuration limitation applies when you set the installation program to automatically create subnets for your OpenShift Container Platform cluster:

- When the installation program creates private subnets in AWS {zone-type}, the program associates each subnet with the route table of its parent zone. This operation ensures that each private subnet can route egress traffic to the internet by way of NAT Gateways in an AWS Region.
- If the parent-zone route table does not exist during cluster installation, the installation program associates any private subnet with the first available private route table in the Amazon Virtual Private Cloud (VPC). This approach is valid only for AWS {zone-type} subnets in an OpenShift Container Platform cluster.
====

// About edge compute pools
// Module included in the following assemblies:
// * installing/installing_aws/installing-aws-localzone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)
// * installing/installing_aws/installing-aws-wavelength.adoc (Installing a cluster on AWS with compute nodes on AWS Wavelength Zones)
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc

[id="edge-machine-pools-aws-local-zones_{context}"]
= About edge compute pools

[role="_abstract"]
The edge compute pool configuration is common between {aws-first} {zone-type} locations. You can use the edge compute pool to create new labels to deploy applications onto {aws-first} {zone-type} nodes. Edge compute nodes are tainted compute nodes that run in {aws-short} {zone-type} locations.

When deploying a cluster that uses {zone-type}, consider the following points:

* Amazon EC2 instances in the {zone-type} are more expensive than Amazon EC2 instances in the Availability Zones.
* The latency is lower between the applications running in {aws-short} {zone-type} and the user. A latency impact exists for some workloads if, for example, ingress traffic is mixed between {zone-type} and Availability Zones.

[IMPORTANT]
====
Generally, the maximum transmission unit (MTU) between an Amazon EC2 instance in a {zone-type} and an Amazon EC2 instance in the Region is 1300. The cluster network MTU must be always less than the EC2 MTU to account for the overhead. The specific overhead is determined by the network plugin. For example: OVN-Kubernetes has an overhead of `100 bytes`.

The network plugin can provide additional features, such as IPsec, that also affect the MTU sizing.

For more information, see How Local Zones work in the {aws-short} documentation.
For more information, see How AWS Wavelength work in the {aws-short} documentation.
You can access the following resources to learn more about a respective zone type:

* See How Local Zones work in the {aws-short} documentation.

* See How AWS Wavelength work in the {aws-short} documentation.
====

OpenShift Container Platform 4.12 introduced a new compute pool, _edge_, that is designed for use in remote zones. The edge compute pool configuration is common between {aws-first} {zone-type} locations. Because of the type and size limitations of resources like EC2 and EBS on {zone-type} resources, the default instance type can vary from the traditional compute pool.

The default Elastic Block Store (EBS) for {zone-type} locations is `gp2`, which differs from the non-edge compute pool. The instance type used for each {zone-type} on an edge compute pool also might differ from other compute pools, depending on the instance offerings on the zone.

The edge compute pool creates new labels that developers can use to deploy applications onto AWS {zone-type} nodes. The new labels are:

* `node-role.kubernetes.io/edge=''`
* `machine.openshift.io/zone-type=local-zone`
* `machine.openshift.io/zone-type=wavelength-zone`
* Local Zones only: `machine.openshift.io/zone-type=local-zone`
* Wavelength Zones only: `machine.openshift.io/zone-type=wavelength-zone`
* `machine.openshift.io/zone-group=$ZONE_GROUP_NAME`

By default, the machine sets for the edge compute pool define the taint of `NoSchedule` to prevent other workloads from spreading on {zone-type} instances. Users can only run user workloads if they define tolerations in the pod specification.

[role="_additional-resources"]
.Additional resources

* MTU value selection
* Changing the MTU for the cluster network
* Understanding taints and tolerations
* Storage classes
* Ingress Controller sharding

[id="installation-prereqs-aws-local-zone_{context}"]
== Installation prerequisites

Before you install a cluster in an AWS {zone-type} environment, you must configure your infrastructure so that it can adopt Local Zone capabilities.

// Opting in to AWS Local Zones
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with worker nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with worker nodes on AWS Wavelength Zones)
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc

[id="installation-aws-add-zone-locations_{context}"]

= Opting in to an AWS {zone-type}

= Opting in to an AWS {zone-type}

= Opting in to AWS Local Zones or Wavelength Zones

[role="_abstract"]
Create a subnet in an {aws-first} {zone-type} when you need workloads to run physically closer to users or data sources than a standard {aws-short} {zone-type}. If you plan to create subnets in {aws-short} {zone-type}, you must opt in to each zone group separately.

.Prerequisites

* You have installed the AWS CLI.
* You have determined an AWS Region for where you want to deploy your OpenShift Container Platform cluster.
* You have attached a permissive IAM policy to a user or role account that opts in to the zone group.

.Procedure

. List the zones that are available in your AWS Region by running the following command:
+
.Example command for listing available AWS Local Zones in an AWS Region
[source,terminal]
----
$ aws --region "<value_of_AWS_Region>" ec2 describe-availability-zones \
    --query 'AvailabilityZones[].[{ZoneName: ZoneName, GroupName: GroupName, Status: OptInStatus}]' \
    --filters Name=zone-type,Values=local-zone \
    --all-availability-zones
----
+
.Example command for listing available AWS Wavelength Zones in an AWS Region
[source,terminal]
----
$ aws --region "<value_of_AWS_Region>" ec2 describe-availability-zones \
    --query 'AvailabilityZones[].[{ZoneName: ZoneName, GroupName: GroupName, Status: OptInStatus}]' \
    --filters Name=zone-type,Values=wavelength-zone \
    --all-availability-zones
----
+
Depending on the AWS Region, the list of available zones might be long. The command returns the following fields:
+
`ZoneName`:: The name of the {zone-type}.
`GroupName`:: The group that comprises the zone. To opt in to the Region, save the name.
`Status`:: The status of the {zone-type} group. If the status is `not-opted-in`, you must opt in the `GroupName` as described in the next step.

. Opt in to the zone group on your AWS account by running the following command:
+
[source,terminal]
----
$ aws ec2 modify-availability-zone-group \
    --group-name "<value_of_GroupName>" \
    --opt-in-status opted-in
----

`<value_of_GroupName>`:: Replace with the name of the group of the {zone-type} where you want to create subnets.
For example, specify `us-east-1-nyc-1` to use the zone `us-east-1-nyc-1a` (US East New York).
As an example for Wavelength Zones, specify `us-east-1-wl1` to use the zone `us-east-1-wl1-nyc-wlz-1` (US East New York).

// Obtaining an AWS Marketplace image
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

[id="prep-installation-aws-local-zone_{context}"]
== Preparing for the installation

Before you extend nodes to {zone-type}, you must prepare certain resources for the cluster installation environment.

// Minimum resource requirements for cluster installation
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

// Tested instance types for AWS
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

[role="_additional-resources"]
.Additional resources

* AWS Local Zones features ({aws-short} documentation)

// Creating the installation configuration file
// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc

[id="installation-generate-aws-user-infra-install-config_{context}"]
= Creating the installation configuration file

Generate and customize the installation configuration file that the
installation program needs to deploy your cluster.

.Prerequisites

* You obtained the OpenShift Container Platform installation program
for user-provisioned infrastructure
and the pull secret for your cluster.
For a restricted network installation, these files are on your mirror host.
* You checked that you are deploying your cluster to an AWS Region with an accompanying {op-system-first} AMI published by Red Hat. If you are deploying to an AWS Region that requires a custom AMI, such as an AWS GovCloud Region, you must create the `install-config.yaml` file manually.

.Procedure

. Create the `install-config.yaml` file.
.. Change to the directory that contains the installation program and run the following command:
+
[source,terminal]
----
$ ./openshift-install create install-config --dir <installation_directory> <1>
----
<1> For `<installation_directory>`, specify the directory name to store the
files that the installation program creates.
+
[IMPORTANT]
====
Specify an empty directory. Some installation assets, like bootstrap X.509
certificates have short expiration intervals, so you must not reuse an
installation directory. If you want to reuse individual files from another
cluster installation, you can copy them into your directory. However, the file
names for the installation assets might change between releases. Use caution
when copying installation files from an earlier OpenShift Container Platform version.
====
.. At the prompts, provide the configuration details for your cloud:
... Optional: Select an SSH key to use to access your cluster machines.
+
[NOTE]
====
For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
====
... Select *aws* as the platform to target.
... If you do not have an AWS profile stored on your computer, enter the AWS
access key ID and secret access key for the user that you configured to run the
installation program.
+
[NOTE]
====
The AWS access key ID and secret access key are stored in `~/.aws/credentials` in the home directory of the current user on the installation host. You are prompted for the credentials by the installation program if the credentials for the exported profile are not present in the file. Any credentials that you provide to the installation program are stored in the file.
====
... Select the AWS Region to deploy the cluster to.
... Select the base domain for the Route 53 service that you configured for your cluster.
... Enter a descriptive name for your cluster.
... Paste the {cluster-manager-url-pull}.
This field is optional.

. Edit the `install-config.yaml` file to give the additional information that
is required for an installation in a restricted network.
.. Update the `pullSecret` value to contain the authentication information for
your registry:
+
[source,yaml]
----
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
----
+
For `<local_registry>`, specify the registry domain name, and optionally the
port, that your mirror registry uses to serve content. For example
`registry.example.com` or `registry.example.com:5000`. For `<credentials>`,
specify the base64-encoded user name and password for your mirror registry.
.. Add the `additionalTrustBundle` parameter and value. The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry.
+
[source,yaml]
----
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
----
.. Add the image content resources:
+
[source,yaml]
----
imageContentSources:
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
----
+
Use the `imageContentSources` section from the output of the command to mirror the repository or the values that you used when you mirrored the content from the media that you brought into your restricted network.

.. Optional: Set the publishing strategy to `Internal`:
+
[source,yaml]
----
publish: Internal
----
+
By setting this option, you create an internal Ingress Controller and a private load balancer.

. If you are installing a three-node cluster, modify the `install-config.yaml` file by setting the `compute.replicas` parameter to `0`. This ensures that the cluster's control planes are schedulable. For more information, see "Installing a three-node cluster on AWS".

. Optional: Back up the `install-config.yaml` file.
+
[IMPORTANT]
====
The `install-config.yaml` file is consumed during the installation process. If
you want to reuse the file, you must back it up now.
====

// Examples of installation configuration files with edge compute pools
// Module included in the following assemblies:
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with worker nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with worker nodes on AWS Wavelength Zones)

[id="installation-aws-edge-compute-pools-examples_{context}"]
= Examples of installation configuration files with edge compute pools

The following examples show `install-config.yaml` files that contain an edge machine pool configuration.

.Configuration that uses an edge pool with a custom instance type
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
metadata:
  name: ipi-edgezone
compute:
- name: edge
  platform:
    aws:
      type: r5.2xlarge
platform:
  aws:
    region: us-west-2
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----

Instance types differ between locations. To verify availability in the {zone-type} in which the cluster runs, see the AWS documentation.

.Configuration that uses an edge pool with a custom Amazon Elastic Block Store (EBS) type
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
metadata:
  name: ipi-edgezone
compute:
- name: edge
  platform:
    aws:
      zones:
      - us-west-2-lax-1a
      - us-west-2-lax-1b
      - us-west-2-phx-2a
      rootVolume:
        type: gp3
        size: 120
platform:
  aws:
    region: us-west-2
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----

Elastic Block Storage (EBS) types differ between locations. Check the AWS documentation to verify availability in the {zone-type} in which the cluster runs.

.Configuration that uses an edge pool with custom security groups
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
metadata:
  name: ipi-edgezone
compute:
- name: edge
  platform:
    aws:
      additionalSecurityGroupIDs:
        - sg-1 <1>
        - sg-2
platform:
  aws:
    region: us-west-2
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----
<1> Specify the name of the security group as it is displayed on the Amazon EC2 console. Ensure that you include the `sg` prefix.

// Customizing Cluster Network MTU
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with compute nodes on AWS Wavelength Zones)

[id="installation-aws-cluster-network-mtu_{context}"]
= Customizing the cluster network MTU

Before you deploy a cluster on AWS, you can customize the cluster network maximum transmission unit (MTU) for your cluster network to meet the needs of your infrastructure.

By default, when you install a cluster with supported {zone-type} capabilities, the MTU value for the cluster network is automatically adjusted to the lowest value that the network plugin accepts.

[IMPORTANT]
====
Setting an unsupported MTU value for EC2 instances that operate in the {zone-type} infrastructure can cause issues for your OpenShift Container Platform cluster.
====

If the Local Zone supports higher MTU values in between EC2 instances in the Local Zone and the AWS Region, you can manually configure the higher value to increase the network performance of the cluster network.

If the Wavelength Zone supports higher MTU values in between EC2 instances running in the Wavelength Zone and the AWS Region, you must manually configure the higher value to increase the network performance of the cluster network.

You can customize the MTU for a cluster by specifying the `networking.clusterNetworkMTU` parameter in the `install-config.yaml` configuration file.

[IMPORTANT]
====
All subnets in {zone-type} must support the higher MTU value, so that each node in that zone can successfully communicate with services in the AWS Region and deploy your workloads.
====

.Example of overwriting the default MTU value
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
metadata:
  name: edge-zone
networking:
  clusterNetworkMTU: 8901
compute:
- name: edge
  platform:
    aws:
      zones:
      - us-west-2-lax-1a
      - us-west-2-lax-1b
platform:
  aws:
    region: us-west-2
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----

[role="_additional-resources"]
.Additional resources

* For more information about the maximum supported maximum transmission unit (MTU) value, see AWS resources supported in Local Zones in the AWS documentation.

// Cluster installation options for an AWS Local Zone environment
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)
// * installing/installing-aws-wavelength.adoc (Installing a cluster on AWS with compute nodes on AWS Wavelength Zones)

[id="aws-cluster-installation-options-aws-lzs_{context}"]
= Cluster installation options for an AWS Local Zones environment

= Cluster installation options for an AWS Wavelength Zones environment

Choose one of the following installation options to install an OpenShift Container Platform cluster on AWS with edge compute nodes defined in {zone-type}:

* Fully automated option: Installing a cluster to quickly extend compute nodes to edge compute pools, where the installation program automatically creates infrastructure resources for the OpenShift Container Platform cluster.
* Existing VPC option: Installing a cluster on AWS into an existing VPC, where you supply {zone-type} subnets to the `install-config.yaml` file.

.Next steps

Choose one of the following options to install an OpenShift Container Platform cluster in an AWS {zone-type} environment:

* Installing a cluster quickly in AWS Local Zones
* Installing a cluster in an existing VPC with defined AWS Local Zone subnets

// Installing a cluster quickly in AWS Local Zones
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with compute nodes on AWS Wavelength Zones)

[id="installation-cluster-quickly-extend-compute-nodes_{context}"]
= Install a cluster quickly in AWS Local Zones

= Install a cluster quickly in AWS Wavelength Zones

For OpenShift Container Platform , you can quickly install a cluster on Amazon Web Services (AWS) to extend compute nodes to {zone-type} locations. By using this installation route, the installation program automatically creates network resources and {zone-type} subnets for each zone that you defined in your configuration file. To customize the installation, you must modify parameters in the `install-config.yaml` file before you deploy the cluster.

// Modifying an installation configuration to use AWS Local Zones
// Module included in the following assemblies:
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with worker nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with worker nodes on AWS Wavelength Zones)

[id="install-creating-install-config-aws-edge-zones_{context}"]
= Modifying an installation configuration file to use AWS Local Zones

= Modifying an installation configuration file to use AWS Wavelength Zones

Modify an `install-config.yaml` file to include AWS {zone-type}.

.Prerequisites

* You have configured an AWS account.
* You added your AWS keys and AWS Region to your local AWS profile by running `aws configure`.
* You are familiar with the configuration limitations that apply when you specify the installation program to automatically create subnets for your OpenShift Container Platform cluster.
* You opted in to the {zone-type} group for each zone.
* You created an `install-config.yaml` file by using the procedure "Creating the installation configuration file".

.Procedure

. Modify the `install-config.yaml` file by specifying {zone-type} names in the `platform.aws.zones` property of the edge compute pool.
+
[source,yaml]
----
# ...
platform:
  aws:
    region: <region_name> <1>
compute:
- name: edge
  platform:
    aws:
      zones: <2>
      - <local_zone_name>
#...
----
+
[source,yaml]
----
# ...
platform:
  aws:
    region: <region_name> <1>
compute:
- name: edge
  platform:
    aws:
      zones: <2>
      - <wavelength_zone_name>
#...
----
<1> The AWS Region name.
<2> The list of {zone-type} names that you use must exist in the same AWS Region specified in the `platform.aws.region` field.
+
.Example of a configuration to install a cluster in the `us-west-2` AWS Region that extends edge nodes to {zone-type} in `Los Angeles` and `Las Vegas` locations
+
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
metadata:
  name: cluster-name
platform:
  aws:
    region: us-west-2
compute:
- name: edge
  platform:
    aws:
      zones:
      - us-west-2-lax-1a
      - us-west-2-lax-1b
      - us-west-2-las-1a
pullSecret: '{"auths": ...}'
sshKey: 'ssh-ed25519 AAAA...'
#...
----
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
metadata:
  name: cluster-name
platform:
  aws:
    region: us-west-2
compute:
- name: edge
  platform:
    aws:
      zones:
      - us-west-2-wl1-lax-wlz-1
      - us-west-2-wl1-las-wlz-1
pullSecret: '{"auths": ...}'
sshKey: 'ssh-ed25519 AAAA...'
#...
----

. Deploy your cluster.

[role="_additional-resources"]
.Additional resources

* Creating the installation configuration file

* Cluster limitations in AWS Local Zones

.Next steps
* Deploying the cluster

[id="creating-aws-local-zone-environment-existing_{context}"]
== Installing a cluster in an existing VPC that has Local Zone subnets

You can install a cluster into an existing Amazon Virtual Private Cloud (VPC) on Amazon Web Services (AWS). The installation program provisions the rest of the required infrastructure, which you can further customize. To customize the installation, change parameters in the `install-config.yaml` file before you install the cluster.

Installing a cluster on AWS into an existing VPC requires extending compute nodes to the edge of the Cloud Infrastructure by using AWS {zone-type}.

Local Zone subnets extend regular compute nodes to edge networks. Each edge compute nodes runs a user workload. After you create an Amazon Web Service (AWS) Local Zone environment, and you deploy your cluster, you can use edge compute nodes to create user workloads in Local Zone subnets.

[NOTE]
====
If you want to create private subnets, you must either change the provided CloudFormation template or create your own template.
====

You can use a provided CloudFormation template to create network resources. Additionally, you can change a template to customize your infrastructure or use the information that they contain to create AWS resources according to your company's policies.

[IMPORTANT]
====
The documentation provides the steps for performing an installer-provisioned infrastructure installation for example purposes only. Installing a cluster in an existing VPC requires that you have knowledge of the cloud provider and the installation process of OpenShift Container Platform. You can use a CloudFormation template to assist you with completing these steps or to help model your own cluster installation. Instead of using the CloudFormation template to create resources, you can decide to use other methods for generating these resources.
====

// Creating a VPC in AWS
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with compute nodes on AWS Wavelength Zones)

[id="installation-creating-aws-vpc-localzone_{context}"]
= Creating a VPC in AWS

You can create a Virtual Private Cloud (VPC), and subnets for all {zone-type} locations, in Amazon Web Services (AWS) for your OpenShift Container Platform cluster to extend compute nodes to edge locations. You can further customize your VPC to meet your requirements, including a VPN and route tables. You can also add new {zone-type} subnets not included at initial deployment.

You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources that represent the VPC.

[NOTE]
====
If you do not use the provided CloudFormation template to create your AWS infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You configured an AWS account.
* You added your AWS keys and AWS Region to your local AWS profile by running `aws configure`.
* You opted in to the AWS {zone-type} on your AWS account.

.Procedure

. Create a JSON file that contains the parameter values that the CloudFormation template requires:
+
[source,json]
----
[
  {
    "ParameterKey": "VpcCidr", <1>
    "ParameterValue": "10.0.0.0/16" <2>
  },
  {
    "ParameterKey": "AvailabilityZoneCount", <3>
    "ParameterValue": "3" <4>
  },
  {
    "ParameterKey": "SubnetBits", <5>
    "ParameterValue": "12" <6>
  }
]
----
<1> The CIDR block for the VPC.
<2> Specify a CIDR block in the format `x.x.x.x/16-24`.
<3> The number of availability zones to deploy the VPC in.
<4> Specify an integer between `1` and `3`.
<5> The size of each subnet in each availability zone.
<6> Specify an integer between  `5` and `13`, where `5` is `/27` and `13` is `/19`.

. Go to the section of the documentation named "CloudFormation template for the VPC", and then copy the syntax from the provided template. Save the copied template syntax as a YAML file on your local system. This template describes the VPC that your cluster requires.

. Launch the CloudFormation template to create a stack of AWS resources that represent the VPC by running the following command:
+
[IMPORTANT]
====
You must enter the command on a single line.
====
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <name> \// <1>
     --template-body file://<template>.yaml \// <2>
     --parameters file://<parameters>.json  <3>
----
<1> `<name>` is the name for the CloudFormation stack, such as `cluster-vpc`.
You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path to and name of the CloudFormation template
YAML file that you saved.
<3> `<parameters>` is the relative path and the name of the CloudFormation
parameters JSON file.
+
.Example output
[source,terminal]
----
arn:aws:cloudformation:us-east-1:123456789012:stack/cluster-vpc/dbedae40-2fd3-11eb-820e-12a48460849f
----

. Confirm that the template components exist by running the following command:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <name>
----
+
After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values for the following parameters. You must provide these parameter values to the other CloudFormation templates that you run to create your cluster.
+
[horizontal]
`VpcId`:: The ID of your VPC.
`PublicSubnetIds`:: The IDs of the new public subnets.
`PrivateSubnetIds`:: The IDs of the new private subnets.
`PublicRouteTableId`:: The ID of the new public route table ID.

// CloudFormation template for the VPC
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with compute nodes on AWS Wavelength Zones)

[id="installation-cloudformation-vpc-localzone_{context}"]
= CloudFormation template for the VPC

You can use the following CloudFormation template to deploy the VPC that you need for your OpenShift Container Platform cluster.

.CloudFormation template for the VPC
[%collapsible]
====
[source,yaml]
----
AWSTemplateFormatVersion: 2010-09-09
Description: Template for Best Practice VPC with 1-3 AZs

Parameters:
  VpcCidr:
    AllowedPattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(1[6-9]|2[0-4]))$
    ConstraintDescription: CIDR block parameter must be in the form x.x.x.x/16-24.
    Default: 10.0.0.0/16
    Description: CIDR block for VPC.
    Type: String
  AvailabilityZoneCount:
    ConstraintDescription: "The number of availability zones. (Min: 1, Max: 3)"
    MinValue: 1
    MaxValue: 3
    Default: 1
    Description: "How many AZs to create VPC subnets for. (Min: 1, Max: 3)"
    Type: Number
  SubnetBits:
    ConstraintDescription: CIDR block parameter must be in the form x.x.x.x/19-27.
    MinValue: 5
    MaxValue: 13
    Default: 12
    Description: "Size of each subnet to create within the availability zones. (Min: 5 = /27, Max: 13 = /19)"
    Type: Number

Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
    - Label:
        default: "Network Configuration"
      Parameters:
      - VpcCidr
      - SubnetBits
    - Label:
        default: "Availability Zones"
      Parameters:
      - AvailabilityZoneCount
    ParameterLabels:
      AvailabilityZoneCount:
        default: "Availability Zone Count"
      VpcCidr:
        default: "VPC CIDR"
      SubnetBits:
        default: "Bits Per Subnet"

Conditions:
  DoAz3: !Equals [3, !Ref AvailabilityZoneCount]
  DoAz2: !Or [!Equals [2, !Ref AvailabilityZoneCount], Condition: DoAz3]

Resources:
  VPC:
    Type: "AWS::EC2::VPC"
    Properties:
      EnableDnsSupport: "true"
      EnableDnsHostnames: "true"
      CidrBlock: !Ref VpcCidr
  PublicSubnet:
    Type: "AWS::EC2::Subnet"
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [0, !Cidr [!Ref VpcCidr, 6, !Ref SubnetBits]]
      AvailabilityZone: !Select
      - 0
      - Fn::GetAZs: !Ref "AWS::Region"
  PublicSubnet2:
    Type: "AWS::EC2::Subnet"
    Condition: DoAz2
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [1, !Cidr [!Ref VpcCidr, 6, !Ref SubnetBits]]
      AvailabilityZone: !Select
      - 1
      - Fn::GetAZs: !Ref "AWS::Region"
  PublicSubnet3:
    Type: "AWS::EC2::Subnet"
    Condition: DoAz3
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [2, !Cidr [!Ref VpcCidr, 6, !Ref SubnetBits]]
      AvailabilityZone: !Select
      - 2
      - Fn::GetAZs: !Ref "AWS::Region"
  InternetGateway:
    Type: "AWS::EC2::InternetGateway"
  GatewayToInternet:
    Type: "AWS::EC2::VPCGatewayAttachment"
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway
  PublicRouteTable:
    Type: "AWS::EC2::RouteTable"
    Properties:
      VpcId: !Ref VPC
  PublicRoute:
    Type: "AWS::EC2::Route"
    DependsOn: GatewayToInternet
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway
  PublicSubnetRouteTableAssociation:
    Type: "AWS::EC2::SubnetRouteTableAssociation"
    Properties:
      SubnetId: !Ref PublicSubnet
      RouteTableId: !Ref PublicRouteTable
  PublicSubnetRouteTableAssociation2:
    Type: "AWS::EC2::SubnetRouteTableAssociation"
    Condition: DoAz2
    Properties:
      SubnetId: !Ref PublicSubnet2
      RouteTableId: !Ref PublicRouteTable
  PublicSubnetRouteTableAssociation3:
    Condition: DoAz3
    Type: "AWS::EC2::SubnetRouteTableAssociation"
    Properties:
      SubnetId: !Ref PublicSubnet3
      RouteTableId: !Ref PublicRouteTable
  PrivateSubnet:
    Type: "AWS::EC2::Subnet"
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [3, !Cidr [!Ref VpcCidr, 6, !Ref SubnetBits]]
      AvailabilityZone: !Select
      - 0
      - Fn::GetAZs: !Ref "AWS::Region"
  PrivateRouteTable:
    Type: "AWS::EC2::RouteTable"
    Properties:
      VpcId: !Ref VPC
  PrivateSubnetRouteTableAssociation:
    Type: "AWS::EC2::SubnetRouteTableAssociation"
    Properties:
      SubnetId: !Ref PrivateSubnet
      RouteTableId: !Ref PrivateRouteTable
  NAT:
    DependsOn:
    - GatewayToInternet
    Type: "AWS::EC2::NatGateway"
    Properties:
      AllocationId:
        "Fn::GetAtt":
        - EIP
        - AllocationId
      SubnetId: !Ref PublicSubnet
  EIP:
    Type: "AWS::EC2::EIP"
    Properties:
      Domain: vpc
  Route:
    Type: "AWS::EC2::Route"
    Properties:
      RouteTableId:
        Ref: PrivateRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId:
        Ref: NAT
  PrivateSubnet2:
    Type: "AWS::EC2::Subnet"
    Condition: DoAz2
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [4, !Cidr [!Ref VpcCidr, 6, !Ref SubnetBits]]
      AvailabilityZone: !Select
      - 1
      - Fn::GetAZs: !Ref "AWS::Region"
  PrivateRouteTable2:
    Type: "AWS::EC2::RouteTable"
    Condition: DoAz2
    Properties:
      VpcId: !Ref VPC
  PrivateSubnetRouteTableAssociation2:
    Type: "AWS::EC2::SubnetRouteTableAssociation"
    Condition: DoAz2
    Properties:
      SubnetId: !Ref PrivateSubnet2
      RouteTableId: !Ref PrivateRouteTable2
  NAT2:
    DependsOn:
    - GatewayToInternet
    Type: "AWS::EC2::NatGateway"
    Condition: DoAz2
    Properties:
      AllocationId:
        "Fn::GetAtt":
        - EIP2
        - AllocationId
      SubnetId: !Ref PublicSubnet2
  EIP2:
    Type: "AWS::EC2::EIP"
    Condition: DoAz2
    Properties:
      Domain: vpc
  Route2:
    Type: "AWS::EC2::Route"
    Condition: DoAz2
    Properties:
      RouteTableId:
        Ref: PrivateRouteTable2
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId:
        Ref: NAT2
  PrivateSubnet3:
    Type: "AWS::EC2::Subnet"
    Condition: DoAz3
    Properties:
      VpcId: !Ref VPC
      CidrBlock: !Select [5, !Cidr [!Ref VpcCidr, 6, !Ref SubnetBits]]
      AvailabilityZone: !Select
      - 2
      - Fn::GetAZs: !Ref "AWS::Region"
  PrivateRouteTable3:
    Type: "AWS::EC2::RouteTable"
    Condition: DoAz3
    Properties:
      VpcId: !Ref VPC
  PrivateSubnetRouteTableAssociation3:
    Type: "AWS::EC2::SubnetRouteTableAssociation"
    Condition: DoAz3
    Properties:
      SubnetId: !Ref PrivateSubnet3
      RouteTableId: !Ref PrivateRouteTable3
  NAT3:
    DependsOn:
    - GatewayToInternet
    Type: "AWS::EC2::NatGateway"
    Condition: DoAz3
    Properties:
      AllocationId:
        "Fn::GetAtt":
        - EIP3
        - AllocationId
      SubnetId: !Ref PublicSubnet3
  EIP3:
    Type: "AWS::EC2::EIP"
    Condition: DoAz3
    Properties:
      Domain: vpc
  Route3:
    Type: "AWS::EC2::Route"
    Condition: DoAz3
    Properties:
      RouteTableId:
        Ref: PrivateRouteTable3
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId:
        Ref: NAT3
  S3Endpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      PolicyDocument:
        Version: 2012-10-17
        Statement:
        - Effect: Allow
          Principal: '*'
          Action:
          - '*'
          Resource:
          - '*'
      RouteTableIds:
      - !Ref PublicRouteTable
      - !Ref PrivateRouteTable
      - !If [DoAz2, !Ref PrivateRouteTable2, !Ref "AWS::NoValue"]
      - !If [DoAz3, !Ref PrivateRouteTable3, !Ref "AWS::NoValue"]
      ServiceName: !Join
      - ''
      - - com.amazonaws.
        - !Ref 'AWS::Region'
        - .s3
      VpcId: !Ref VPC

Outputs:
  VpcId:
    Description: ID of the new VPC.
    Value: !Ref VPC
  PublicSubnetIds:
    Description: Subnet IDs of the public subnets.
    Value:
      !Join [
        ",",
        [!Ref PublicSubnet, !If [DoAz2, !Ref PublicSubnet2, !Ref "AWS::NoValue"], !If [DoAz3, !Ref PublicSubnet3, !Ref "AWS::NoValue"]]
      ]
  PrivateSubnetIds:
    Description: Subnet IDs of the private subnets.
    Value:
      !Join [
        ",",
        [!Ref PrivateSubnet, !If [DoAz2, !Ref PrivateSubnet2, !Ref "AWS::NoValue"], !If [DoAz3, !Ref PrivateSubnet3, !Ref "AWS::NoValue"]]
      ]
  PublicRouteTableId:
    Description: Public Route table ID
    Value: !Ref PublicRouteTable
  PrivateRouteTableIds:
    Description: Private Route table IDs
    Value:
      !Join [
        ",",
        [
          !Join ["=", [
            !Select [0, "Fn::GetAZs": !Ref "AWS::Region"],
            !Ref PrivateRouteTable
          ]],
          !If [DoAz2,
               !Join ["=", [!Select [1, "Fn::GetAZs": !Ref "AWS::Region"], !Ref PrivateRouteTable2]],
               !Ref "AWS::NoValue"
          ],
          !If [DoAz3,
               !Join ["=", [!Select [2, "Fn::GetAZs": !Ref "AWS::Region"], !Ref PrivateRouteTable3]],
               !Ref "AWS::NoValue"
          ]
        ]
      ]
----
====

// Creating subnets in Local Zones
// Module included in the following assemblies:
//
// * installing/installing-aws-local-zone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)

[id="installation-creating-aws-vpc-subnets-lz_{context}"]
= Creating subnets in Local Zones

Before you configure a machine set for edge compute nodes in your OpenShift Container Platform cluster, you must create the subnets in {zone-type}. Complete the following procedure for each Local Zone that you want to deploy compute nodes to.

You can use the provided CloudFormation template and create a CloudFormation stack. You can then use this stack to custom provision a subnet.

[NOTE]
====
If you do not use the provided CloudFormation template to create your AWS infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You configured an AWS account.
* You added your AWS keys and region to your local AWS profile by running `aws configure`.
* You opted in to the {zone-type} group.

.Procedure

. Go to the section of the documentation named "CloudFormation template for the VPC subnet", and copy the syntax from the template. Save the copied template syntax as a YAML file on your local system. This template describes the VPC that your cluster requires.

. Run the following command to deploy the CloudFormation template, which creates a stack of AWS resources that represent the VPC:
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <stack_name> \// <1>
  --region ${CLUSTER_REGION} \
  --template-body file://<template>.yaml \// <2>
  --parameters \
    ParameterKey=VpcId,ParameterValue="${VPC_ID}" \// <3>
    ParameterKey=ClusterName,ParameterValue="${CLUSTER_NAME}" \// <4>
    ParameterKey=ZoneName,ParameterValue="${ZONE_NAME}" \// <5>
    ParameterKey=PublicRouteTableId,ParameterValue="${ROUTE_TABLE_PUB}" \// <6>
    ParameterKey=PublicSubnetCidr,ParameterValue="${SUBNET_CIDR_PUB}" \// <7>
    ParameterKey=PrivateRouteTableId,ParameterValue="${ROUTE_TABLE_PVT}" \// <8>
    ParameterKey=PrivateSubnetCidr,ParameterValue="${SUBNET_CIDR_PVT}" <9>
----
<1> `<stack_name>` is the name for the CloudFormation stack, such as `cluster-wl-<local_zone_shortname>`. You need the name of this stack if you remove the cluster.
<2> `<template>` is the relative path and the name of the CloudFormation template
YAML file that you saved.
<3> `${VPC_ID}` is the VPC ID, which is the value `VpcID` in the output of the CloudFormation template for the VPC.
<4> `${ZONE_NAME}` is the value of {zone-type} name to create the subnets.
<5> `${CLUSTER_NAME}` is the value of *ClusterName* to be used as a prefix of the new AWS resource names.
<6> `${SUBNET_CIDR_PUB}` is a valid CIDR block that is used to create the public subnet. This block must be part of the VPC CIDR block `VpcCidr`.
<7> `${ROUTE_TABLE_PVT}` is the *PrivateRouteTableId* extracted from the output of the VPC's CloudFormation stack.
<8> `${SUBNET_CIDR_PVT}` is a valid CIDR block that is used to create the private subnet. This block must be part of the VPC CIDR block `VpcCidr`.

.Example output

[source,terminal]
----
arn:aws:cloudformation:us-east-1:123456789012:stack/<stack_name>/dbedae40-820e-11eb-2fd3-12a48460849f
----

.Verification

* Confirm that the template components exist by running the following command:
+
[source,terminal]
----
$ aws cloudformation describe-stacks --stack-name <stack_name>
----
+
After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values for the following parameters. Ensure that you provide these parameter values to the other CloudFormation templates that you run to create for your cluster.
+
[horizontal]
`PublicSubnetId`:: The IDs of the public subnet created by the CloudFormation stack.
`PrivateSubnetId`:: The IDs of the private subnet created by the CloudFormation stack.

// CloudFormation template for the subnet that uses AWS Local Zones
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with worker nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with compute nodes on AWS Wavelength Zones)
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="installation-cloudformation-subnet-localzone_{context}"]
= CloudFormation template for the VPC subnet

[role="_abstract"]

.CloudFormation template for VPC subnets
[%collapsible]
====
[source,yaml,subs="attributes+"]
----
AWSTemplateFormatVersion: 2010-09-09
Description: Template for Best Practice Subnets (Public and Private)

Parameters:
  VpcId:
    Description: VPC ID that comprises all the target subnets.
    Type: String
    AllowedPattern: ^(?:(?:vpc)(?:-[a-zA-Z0-9]+)?\b|(?:[0-9]{1,3}\.){3}[0-9]{1,3})$
    ConstraintDescription: VPC ID must be with valid name, starting with vpc-.*.
  ClusterName:
    Description: Cluster name or prefix name to prepend the Name tag for each subnet.
    Type: String
    AllowedPattern: ".+"
    ConstraintDescription: ClusterName parameter must be specified.
  ZoneName:
    Description: Zone Name to create the subnets, such as us-west-2-lax-1a.
    Type: String
    AllowedPattern: ".+"
    ConstraintDescription: ZoneName parameter must be specified.
  PublicRouteTableId:
    Description: Public Route Table ID to associate the public subnet.
    Type: String
    AllowedPattern: ".+"
    ConstraintDescription: PublicRouteTableId parameter must be specified.
  PublicSubnetCidr:
    AllowedPattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(1[6-9]|2[0-4]))$
    ConstraintDescription: CIDR block parameter must be in the form x.x.x.x/16-24.
    Default: 10.0.128.0/20
    Description: CIDR block for public subnet.
    Type: String
  PrivateRouteTableId:
    Description: Private Route Table ID to associate the private subnet.
    Type: String
    AllowedPattern: ".+"
    ConstraintDescription: PrivateRouteTableId parameter must be specified.
  PrivateSubnetCidr:
    AllowedPattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(1[6-9]|2[0-4]))$
    ConstraintDescription: CIDR block parameter must be in the form x.x.x.x/16-24.
    Default: 10.0.128.0/20
    Description: CIDR block for private subnet.
    Type: String
  PrivateSubnetLabel:
    Default: "private"
    Description: Subnet label to be added when building the subnet name.
    Type: String
  PublicSubnetLabel:
    Default: "public"
    Description: Subnet label to be added when building the subnet name.
    Type: String
  OutpostArn:
    Default: ""
    Description: OutpostArn when creating subnets on AWS Outpost.
    Type: String

Conditions:
  OutpostEnabled: !Not [!Equals [!Ref "OutpostArn", ""]]

Resources:
  PublicSubnet:
    Type: "AWS::EC2::Subnet"
    Properties:
      VpcId: !Ref VpcId
      CidrBlock: !Ref PublicSubnetCidr
      AvailabilityZone: !Ref ZoneName
      OutpostArn: !If [ OutpostEnabled, !Ref OutpostArn, !Ref "AWS::NoValue"]
      Tags:
      - Key: Name
        Value: !Join ['-', [!Ref ClusterName, "public", !Ref ZoneName]]
        Value: !Join ['-', [ !Ref ClusterName, !Ref PublicSubnetLabel, !Ref ZoneName]]
      - Key: kubernetes.io/cluster/unmanaged
        Value: true

  PublicSubnetRouteTableAssociation:
    Type: "AWS::EC2::SubnetRouteTableAssociation"
    Properties:
      SubnetId: !Ref PublicSubnet
      RouteTableId: !Ref PublicRouteTableId

  PrivateSubnet:
    Type: "AWS::EC2::Subnet"
    Properties:
      VpcId: !Ref VpcId
      CidrBlock: !Ref PrivateSubnetCidr
      AvailabilityZone: !Ref ZoneName
      OutpostArn: !If [ OutpostEnabled, !Ref OutpostArn, !Ref "AWS::NoValue"]
      Tags:
      - Key: Name
        Value: !Join ['-', [!Ref ClusterName, "private", !Ref ZoneName]]
        Value: !Join ['-', [!Ref ClusterName, !Ref PrivateSubnetLabel, !Ref ZoneName]]
      - Key: kubernetes.io/cluster/unmanaged
        Value: true

  PrivateSubnetRouteTableAssociation:
    Type: "AWS::EC2::SubnetRouteTableAssociation"
    Properties:
      SubnetId: !Ref PrivateSubnet
      RouteTableId: !Ref PrivateRouteTableId

Outputs:
  PublicSubnetId:
    Description: Subnet ID of the public subnets.
    Value:
      !Join ["", [!Ref PublicSubnet]]

  PrivateSubnetId:
    Description: Subnet ID of the private subnets.
    Value:
      !Join ["", [!Ref PrivateSubnet]]
----

where:

`kubernetes.io/cluster/unmanaged`:: You must include the `kubernetes.io/cluster/unmanaged` tag in the public subnet configuration for AWS Outposts.
`kubernetes.io/cluster/unmanaged`:: You must include the `kubernetes.io/cluster/unmanaged` tag in the private subnet configuration for AWS Outposts.
====

[role="_additional-resources"]
.Additional resources

* You can view details about the CloudFormation stacks that you create by navigating to the AWS CloudFormation console.

// Modifying an installation configuration file to use AWS Wavelength Zones subnets
// Module included in the following assemblies:
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with worker nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with worker nodes on AWS Wavelength Zones)

[id="installing-aws-edge-zones-custom-vpc-config_{context}"]
= Modifying an installation configuration file to use AWS Local Zones subnets

= Modifying an installation configuration file to use AWS Wavelength Zones subnets

Modify your `install-config.yaml` file to include {zone-type} subnets.

.Prerequisites

* You created subnets by using the procedure "Creating subnets in {zone-type}".
* You created an `install-config.yaml` file by using the procedure "Creating the installation configuration file".

.Procedure

* Modify the `install-config.yaml` configuration file by specifying {zone-type} subnets in the `platform.aws.subnets` parameter.
+
.Example installation configuration file with {zone-type} subnets
[source,yaml]
----
# ...
platform:
  aws:
    region: us-west-2
    subnets: <1>
    - publicSubnetId-1
    - publicSubnetId-2
    - publicSubnetId-3
    - privateSubnetId-1
    - privateSubnetId-2
    - privateSubnetId-3
    - publicSubnetId-LocalZone-1
# ...
----
<1> List of subnet IDs created in the zones: Availability and {zone-type}.
.Example installation configuration file with {zone-type} subnets
[source,yaml]
----
# ...
platform:
  aws:
    region: us-west-2
    subnets: <1>
    - publicSubnetId-1
    - publicSubnetId-2
    - publicSubnetId-3
    - privateSubnetId-1
    - privateSubnetId-2
    - privateSubnetId-3
    - publicOrPrivateSubnetID-Wavelength-1
# ...
----
<1> List of subnet IDs created in the zones: Availability and {zone-type}.

[role="_additional-resources"]
.Additional resources

* For more information about viewing the CloudFormation stacks that you created, see AWS CloudFormation console.
* For more information about AWS profile and credential configuration, see Configuration and credential file settings in the AWS documentation.

.Next steps
* Deploying the cluster

// Optional: AWS security groups
// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc

[id="installation-aws-security-groups_{context}"]
= Optional: AWS security groups

[role="_abstract"]
By default, the installation program creates and attaches security groups to control plane and compute machines. The rules associated with the default security groups cannot be modified.

However, you can apply additional existing AWS security groups, which are associated with your existing VPC, to control plane and compute machines. Applying custom security groups can help you meet the security needs of your organization, in such cases where you need to control the incoming or outgoing traffic of these machines.

As part of the installation process, you apply custom security groups by modifying the `install-config.yaml` file before deploying the cluster.

For more information, see "Applying existing AWS security groups to the cluster".
For more information, see "Edge compute pools and AWS Local Zones".

[IMPORTANT]
====
By default, {aws-short} allows 5 security groups per network interface. The installation program creates 2 security groups for compute machines and 3 security groups for control plane machines. If you are installing a cluster into a shared VPC, there are three scenarios in which you must increase this quota:

* You specified 4 or more custom security groups for compute machines using the `compute.platform.aws.additionalSecurityGroupIDs` parameter in the `install-config.yaml` file.
* You specified 3 or more custom security groups for control plane machines using the `controlPlane.platform.aws.additionalSecurityGroupIDs` parameter in the `install-config.yaml` file.
* You specified 3 or more custom security groups for all machines using the `platform.aws.defaultMachinePlatform` parameter in the `install-config.yaml` file.

You must increase the quota of security groups per network interface to a number greater than or equal to `3 + (number of control plane custom security groups OR number of default machine platform custom security groups)`, or `2 + (number of compute custom security groups OR number of default machine platform custom security groups)`, whichever is higher. If you do not specify a sufficient quota, the installation will succeed, but it will generate `SecurityGroupsPerInterfaceLimitExceeded` errors in the installation log, and the additional security groups will not be applied. The maximum allowed quota is 16 and the maximum number of user-specified security groups is 10.
====

// Optional: Assign public IP to edge compute nodes (optional)
// Module included in the following assemblies:
//
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with commpute nodes on AWS Wavelength Zones)

[id="installing-with-edge-node-public_{context}"]
= Optional: Assign public IP addresses to edge compute nodes

If your workload requires deploying the edge compute nodes in public subnets on {zone-type} infrastructure, you can configure the machine set manifests when installing a cluster.

AWS {zone-type} infrastructure accesses the network traffic in a specified zone, so applications can take advantage of lower latency when serving end users that are closer to that zone.

The default setting that deploys compute nodes in private subnets might not meet your needs, so consider creating edge compute nodes in public subnets when you want to apply more customization to your infrastructure.

[IMPORTANT]
====
By default, OpenShift Container Platform deploy the compute nodes in private subnets. For best performance, consider placing compute nodes in subnets that have their Public IP addresses attached to the subnets.

You must create additional security groups, but ensure that you only open the groups' rules over the internet when you really need to.
====

.Procedure

. Change to the directory that contains the installation program and generate the manifest files. Ensure that the installation manifests get created at the `openshift` and `manifests` directory level.
+
[source,terminal]
----
$ ./openshift-install create manifests --dir <installation_directory>
----

. Edit the machine set manifest that the installation program generates for the {zone-type}, so that the manifest gets deployed in public subnets. Specify `true` for the `spec.template.spec.providerSpec.value.publicIP` parameter.
+
.Example machine set manifest configuration for installing a cluster quickly in {zone-type}
[source,yaml]
----
spec:
  template:
    spec:
      providerSpec:
        value:
          publicIp: true
          subnet:
            filters:
              - name: tag:Name
                values:
                  - ${INFRA_ID}-public-${ZONE_NAME}
----
+
.Example machine set manifest configuration for installing a cluster in an existing VPC that has {zone-type} subnets
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <infrastructure_id>-edge-<zone>
  namespace: openshift-machine-api
spec:
  template:
    spec:
      providerSpec:
        value:
          publicIp: true
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

[id="verify-aws-local-zone-deployed-cluster-status_{context}"]
== Verifying the status of the deployed cluster

Verify that your OpenShift Container Platform successfully deployed on AWS {zone-type}.

// Logging in to the cluster by using the CLI
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

// Logging in to the cluster by using the web console
// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-china.adoc.
// * installing/installing_aws/installing-aws-secret-region.adoc
// *installing/validation_and_troubleshooting/validating-an-installation.adoc
// *installing/installing_aws/installing-aws-user-infra.adoc
// *installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// *installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing_aws/installing-aws-wavelength-zone.adoc

[id="logging-in-by-using-the-web-console_{context}"]
= Logging in to the cluster by using the web console

The `kubeadmin` user exists by default after an OpenShift Container Platform installation. You can log in to your cluster as the `kubeadmin` user by using the OpenShift Container Platform web console.

.Prerequisites

* You have access to the installation host.
* You completed a cluster installation and all cluster Operators are available.

.Procedure

. Obtain the password for the `kubeadmin` user from the `kubeadmin-password` file on the installation host:
+
[source,terminal]
----
$ cat <installation_directory>/auth/kubeadmin-password
----
+
[NOTE]
====
Alternatively, you can obtain the `kubeadmin` password from the `<installation_directory>/.openshift_install.log` log file on the installation host.
====

. List the OpenShift Container Platform web console route:
+
[source,terminal]
----
$ oc get routes -n openshift-console | grep 'console-openshift'
----
+
[NOTE]
====
Alternatively, you can obtain the OpenShift Container Platform route from the `<installation_directory>/.openshift_install.log` log file on the installation host.
====
+
.Example output
[source,terminal]
----
console     console-openshift-console.apps.<cluster_name>.<base_domain>            console     https   reencrypt/Redirect   None
----

. Navigate to the route detailed in the output of the preceding command in a web browser and log in as the `kubeadmin` user.

[role="_additional-resources"]
.Additional resources

* Accessing the web console

// Verifying nodes that were created with edge compute pool
// Module included in the following assemblies
// * installing/installing-aws-localzone.adoc (Installing a cluster on AWS with compute nodes on AWS Local Zones)
// * installing/installing-aws-wavelength-zone.adoc (Installing a cluster on AWS with compute nodes on AWS Wavelength Zones)
// * post_installation_configuration/aws-compute-edge-tasks.adoc

[id="machine-edge-pool-review-nodes_{context}"]
= Verifying nodes that were created with edge compute pool

After you install a cluster that uses AWS {zone-type} infrastructure, check the status of the machine that was created by the machine set manifests created during installation.

. To check the machine sets created from the subnet you added to the `install-config.yaml` file, run the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                  DESIRED   CURRENT   READY   AVAILABLE   AGE
cluster-7xw5g-edge-us-east-1-nyc-1a   1         1         1       1           3h4m
cluster-7xw5g-worker-us-east-1a       1         1         1       1           3h4m
cluster-7xw5g-worker-us-east-1b       1         1         1       1           3h4m
cluster-7xw5g-worker-us-east-1c       1         1         1       1           3h4m
----
.Example output
[source,terminal]
----
NAME                                         DESIRED   CURRENT   READY   AVAILABLE   AGE
cluster-7xw5g-edge-us-east-1-wl1-nyc-wlz-1   1         1         1       1           3h4m
cluster-7xw5g-worker-us-east-1a              1         1         1       1           3h4m
cluster-7xw5g-worker-us-east-1b              1         1         1       1           3h4m
cluster-7xw5g-worker-us-east-1c              1         1         1       1           3h4m
----

. To check the machines that were created from the machine sets, run the following command:
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api
----
+
.Example output
----
NAME                                        PHASE     TYPE          REGION      ZONE               AGE
cluster-7xw5g-edge-us-east-1-nyc-1a-wbclh   Running   c5d.2xlarge   us-east-1   us-east-1-nyc-1a   3h
cluster-7xw5g-master-0                      Running   m6i.xlarge    us-east-1   us-east-1a         3h4m
cluster-7xw5g-master-1                      Running   m6i.xlarge    us-east-1   us-east-1b         3h4m
cluster-7xw5g-master-2                      Running   m6i.xlarge    us-east-1   us-east-1c         3h4m
cluster-7xw5g-worker-us-east-1a-rtp45       Running   m6i.xlarge    us-east-1   us-east-1a         3h
cluster-7xw5g-worker-us-east-1b-glm7c       Running   m6i.xlarge    us-east-1   us-east-1b         3h
cluster-7xw5g-worker-us-east-1c-qfvz4       Running   m6i.xlarge    us-east-1   us-east-1c         3h
----
.Example output
----
NAME                                        PHASE     TYPE          REGION      ZONE               AGE
cluster-7xw5g-edge-us-east-1-wl1-nyc-wlz-1-wbclh  Running   c5d.2xlarge   us-east-1   us-east-1-wl1-nyc-wlz-1  3h
cluster-7xw5g-master-0                            Running   m6i.xlarge    us-east-1   us-east-1a               3h4m
cluster-7xw5g-master-1                            Running   m6i.xlarge    us-east-1   us-east-1b               3h4m
cluster-7xw5g-master-2                            Running   m6i.xlarge    us-east-1   us-east-1c               3h4m
cluster-7xw5g-worker-us-east-1a-rtp45             Running   m6i.xlarge    us-east-1   us-east-1a               3h
cluster-7xw5g-worker-us-east-1b-glm7c             Running   m6i.xlarge    us-east-1   us-east-1b               3h
cluster-7xw5g-worker-us-east-1c-qfvz4             Running   m6i.xlarge    us-east-1   us-east-1c               3h
----

. To check nodes with edge roles, run the following command:
+
[source,terminal]
----
$ oc get nodes -l node-role.kubernetes.io/edge
----
+
.Example output
[source,terminal]
----
NAME                           STATUS   ROLES         AGE    VERSION
ip-10-0-207-188.ec2.internal   Ready    edge,worker   172m   v1.25.2+d2e245f
----

.Next steps

* Validating an installation.
* If necessary, you can Remote health reporting.
