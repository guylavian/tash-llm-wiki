---
title: "Creating {product-title} clusters using the default options"
type: reference
domain: openshift
slug: rosa-hcp-4-22-rosa-hcp-sts-creating-a-cluster-quickly
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly
version: 4.22
family: rosa_hcp
documentKind: "Documentation"
---

# Creating {product-title} clusters using the default options

[id="rosa-hcp-sts-creating-a-cluster-quickly"]
= Creating OpenShift Container Platform clusters using the default options

[role="_abstract"]
You can create a OpenShift Container Platform cluster quickly by using the default options and automatic AWS Identity and Access Management (IAM) resource creation. You can deploy your cluster by using the {rosa-cli-first}.

[IMPORTANT]
====
You cannot upgrade or convert existing {rosa-classic-title} clusters to {hcp} architecture. You must create a new OpenShift Container Platform cluster.
====

[NOTE]
====
OpenShift Container Platform clusters only support AWS IAM Security Token Service (STS) authentication.
====

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="considerations-regarding-auto-creation-mode_{context}"]
= About automatic IAM resource creation

[role="_abstract"]
The `auto` mode in the {rosa-cli-first} immediately creates the required IAM resources using the current AWS account. The required resources include the account-wide IAM roles and policies, cluster-specific Operator roles and policies, and OpenID Connect (OIDC) identity provider.

Alternatively, you can use `manual` mode, which outputs the `aws` commands needed to create the IAM resources instead of deploying them automatically.

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc

[id="rosa-sts-overview-of-the-default-cluster-specifications_{context}"]
= Overview of the default cluster specifications

[role="_abstract"]
You can quickly create a OpenShift Container Platform cluster by using the default installation options.

.Default OpenShift Container Platform cluster specifications

[cols=".^1,.^3a",options="header"]
|===

|Component
|Default specifications

|Accounts and roles
|
* Default IAM role prefix: `rosa-<6-digit-alphanumeric-string>`
* Default IAM role prefix: `ManagedOpenShift`
* Default IAM role prefix: `HCP-ROSA`
* No cluster admin role created

|Cluster settings
|
* Default cluster version: `4.14`
* Cluster name: `rosa-<6-digit-alphanumeric-string>`
* Default AWS region for installations using the {cluster-manager-first} {hybrid-console-second}: us-east-2 (US East, Ohio)
* Availability: Multi zone for the data plane
* EC2 Instance Metadata Service (IMDS) is enabled and allows the use of IMDSv1 or IMDSv2 (token optional)
* Default cluster version: Latest
* Default AWS region for installations using the {cluster-manager-first} {hybrid-console-second}: us-east-1 (US East, North Virginia)
* Default AWS region for installations using the {rosa-cli} (`rosa`): Defined by your `aws` CLI configuration
* Default EC2 IMDS endpoints (both v1 and v2) are enabled
* EC2 Instance Metadata Service (IMDS) is enabled and allows the use of IMDSv1 or IMDSv2 (token optional)
* Availability: Single zone for the data plane
* Monitoring for user-defined projects: Enabled
* No cluster admin role created
|Encryption
|* Cloud storage is encrypted at rest
* Additional etcd encryption is not enabled
* The default AWS Key Management Service (KMS) key is used as the encryption key for persistent data

|Control plane node configuration
|* Control plane node instance type: m5.2xlarge (8 vCPU, 32 GiB RAM)
* Control plane node count: 3
|Infrastructure node configuration
|* Infrastructure node instance type: r5.xlarge (4 vCPU, 32 GiB RAM)
* Infrastructure node count: 2

|Compute node machine pool
|* Compute node instance type: m5.xlarge (4 vCPU 16, GiB RAM)
* Compute node count: 2
* Compute node count: 3
* Autoscaling: Not enabled
* No additional node labels

|Networking configuration
|
* Cluster privacy: Public
* Cluster privacy: public or private
* You can choose to create a new VPC during the Terraform cluster creation process.
* You must have configured your own Virtual Private Cloud (VPC)
* No cluster-wide proxy is configured

|Classless Inter-Domain Routing (CIDR) ranges
|
* Machine CIDR: 10.0.0.0/16
* Service CIDR: 172.30.0.0/16
* Pod CIDR: 10.128.0.0/14
* Machine CIDR: 10.0.0.0/16
* Service CIDR: 172.30.0.0/16
* Pod CIDR: 10.128.0.0/14
* Host prefix: /23
+
[NOTE]
====
The static IP address `172.20.0.1` is reserved for the internal Kubernetes API address. The machine, pod, and service CIDRs ranges must not conflict with this IP address.
====

|Cluster roles and policies
|* Mode used to create the Operator roles and the OpenID Connect (OIDC) provider: `auto`
* A configured `ocm-role`, which is required for all OpenShift Container Platform clusters.
+
[NOTE]
====
For installations that use {cluster-manager} on the {hybrid-console-second}, the `auto` mode requires an admin-privileged {cluster-manager} role (ocm-role).
====
* Default Operator role prefix: `rosa-<6-digit-alphanumeric-string>`
* Default Operator role prefix: `<cluster_name>-<4_digit_random_string>`

|Storage
|* Node volumes:
** Type: AWS EBS GP3
** Default size: 300GiB (adjustable at creation time)
* Workload persistent volumes:
** Default StorageClass: gp3-csi
** Provisioner: ebs.csi.aws.com
** Dynamic persistent volume provisioning

|Cluster update strategy
|* Individual updates
* 1 hour grace period for node draining

|===

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-fips-encryption.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-ext-auth.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-prerequisites_{context}"]
= OpenShift Container Platform prerequisites

[role="_abstract"]
Before you can create a OpenShift Container Platform cluster,  you must complete the following prerequisites. Use each link to find detailed instructions for completing that specific prerequisite:

* Configure a virtual private cloud (VPC)
* Create account-wide roles
* Create the ocm-role IAM role
* Create an OIDC configuration
* Create Operator roles

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-creating-vpc_{context}"]
= Creating a Virtual Private Cloud for your OpenShift Container Platform clusters

[role="_abstract"]
You must have a Virtual Private Cloud (VPC) to create a OpenShift Container Platform cluster.

You can create a VPC by using one of these methods:

* Create a VPC using the ROSA CLI
* Create a VPC by using a Terraform template
* Manually create the VPC resources in the AWS console

[NOTE]
====
The Terraform instructions are for testing and demonstration purposes. Your own installation requires some modifications to the VPC for your own use. You should also ensure that when you use this Terraform configuration, it is in the same region that you intend to install your cluster. In these examples, `us-east-2` is used.
====

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-create-network_{context}"]
= Creating an AWS VPC using the ROSA CLI

[role="_abstract"]
The `rosa create network` command is available in v.1.2.48 or later of the {rosa-cli}. The command uses AWS CloudFormation to create a VPC and associated networking components necessary to install a OpenShift Container Platform cluster. CloudFormation is a native AWS infrastructure-as-code tool and is compatible with the AWS CLI.

If you do not specify a template, CloudFormation uses a default template that creates resources with the following parameters:

.Default VPC parameters
[cols="2a,3a",options="header"]
|===
|VPC parameter
|Value

| Availability zones
| 1

| Region
| `us-east-1`

| VPC CIDR
| `10.0.0.0/16`
|===

You can create and customize CloudFormation templates to use with the `rosa create network` command. See the additional resources of this section for information on the default VPC template.

.Prerequisites

* You have configured your AWS account
* You have configured your Red Hat accounts
* You have installed the {rosa-cli} and configured it to the latest version

.Procedure

. Create an AWS VPC using the default CloudFormations template by running the following command:
+
[source,terminal]
----
$ rosa create network
----

. Optional: Customize your VPC by specifying additional parameters.
+
You can use the `--param` flag to specify changes to the default VPC template. The following example command specifies custom values for `region`, `Name`, `AvailabilityZoneCount` and `VpcCidr`.
+
[source,terminal]
----
$ rosa create network --param Region=us-east-2 --param Name=quickstart-stack --param AvailabilityZoneCount=3 --param VpcCidr=10.0.0.0/16
----
+
The command takes about 5 minutes to run and provides regular status updates from AWS as resources are created. If there is an issue with CloudFormation, a rollback is attempted. For all other errors that are encountered, please follow the error message instructions or contact AWS support.
// ifdef::rosa-egress-lockdown[]
// . Create a new directory for your CloudFormation templates by running the following command:
// +
// [source,terminal]
// ----
// $ mkdir TEMPLATES
// ----

// . Run the following command to create a local copy of this CloudFormation template to create a private VPC:
// +
// [source,terminal]
// ----
// $ cat<<-EOF>TEMPLATES/rosa-zero-egress-vpc.yaml
// AWSTemplateFormatVersion: '2010-09-09'
// Description: |
//   CloudFormation template for a Zero-Egress VPC for ROSA,
//   equivalent to the provided Terraform configuration.
//   This VPC includes private subnets, a security group for internal traffic,
//   and VPC Endpoints for STS, ECR (API, DKR), and S3 to facilitate
//   communication for ROSA in a private environment.

// Parameters:
//   ClusterName:
//     Type: String
//     Description: The name of the ROSA cluster, used for naming resources.

//   VpcCidrBlock:
//     Type: String
//     Default: 10.0.0.0/16
//     Description: CIDR block for the VPC.

//   PrivateSubnet1CidrBlock:
//     Type: String
//     Default: 10.0.1.0/24
//     Description: CIDR block for the first private subnet.

//   PrivateSubnet2CidrBlock:
//     Type: String
//     Default: 10.0.2.0/24
//     Description: CIDR block for the second private subnet.

//   AvailabilityZone1:
//     Type: AWS::EC2::AvailabilityZone::Name
//     Description: First Availability Zone for the private subnet.

//   AvailabilityZone2:
//     Type: AWS::EC2::AvailabilityZone::Name
//     Description: Second Availability Zone for the private subnet.

// Resources:
//   RosaVPC:
//     Type: AWS::EC2::VPC
//     Properties:
//       CidrBlock: !Ref VpcCidrBlock
//       EnableDnsSupport: true
//       EnableDnsHostnames: true
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-vpc
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName

//   PrivateSubnet1:
//     Type: AWS::EC2::Subnet
//     Properties:
//       VpcId: !Ref RosaVPC
//       CidrBlock: !Ref PrivateSubnet1CidrBlock
//       AvailabilityZone: !Ref AvailabilityZone1
//       MapPublicIpOnLaunch: false # Ensures it's private
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-private-subnet-1
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName
//         - Key: kubernetes.io/role/internal-elb
//           Value: "1" # Tag from Terraform

//   PrivateSubnet2:
//     Type: AWS::EC2::Subnet
//     Properties:
//       VpcId: !Ref RosaVPC
//       CidrBlock: !Ref PrivateSubnet2CidrBlock
//       AvailabilityZone: !Ref AvailabilityZone2
//       MapPublicIpOnLaunch: false # Ensures it's private
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-private-subnet-2
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName
//         - Key: kubernetes.io/role/internal-elb
//           Value: "1" # Tag from Terraform

//   PrivateRouteTable:
//     Type: AWS::EC2::RouteTable
//     Properties:
//       VpcId: !Ref RosaVPC
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-private-route-table
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName

//   PrivateSubnet1RouteTableAssociation:
//     Type: AWS::EC2::SubnetRouteTableAssociation
//     Properties:
//       SubnetId: !Ref PrivateSubnet1
//       RouteTableId: !Ref PrivateRouteTable

//   PrivateSubnet2RouteTableAssociation:
//     Type: AWS::EC2::SubnetRouteTableAssociation
//     Properties:
//       SubnetId: !Ref PrivateSubnet2
//       RouteTableId: !Ref PrivateRouteTable

//   AuthorizeInboundVpcTrafficSecurityGroup:
//     Type: AWS::EC2::SecurityGroup
//     Properties:
//       GroupDescription: Allow all inbound traffic within the VPC
//       VpcId: !Ref RosaVPC
//       SecurityGroupIngress:
//         - IpProtocol: "-1" # All protocols
//           FromPort: -1 # All ports
//           ToPort: -1 # All ports
//           CidrIp: !Ref VpcCidrBlock # Allows all traffic from within the VPC CIDR
//       SecurityGroupEgress:
//         - IpProtocol: "-1" # All protocols
//           FromPort: -1 # All ports
//           ToPort: -1 # All ports
//           CidrIp: "0.0.0.0/0" # Allow all outbound traffic (typically for VPC Endpoints)
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-inbound-vpc-sg
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName

//   STSVpcEndpoint:
//     Type: AWS::EC2::VPCEndpoint
//     Properties:
//       VpcId: !Ref RosaVPC
//       ServiceName: !Sub com.amazonaws.${AWS::Region}.sts
//       VpcEndpointType: Interface
//       PrivateDnsEnabled: true
//       SubnetIds:
//         - !Ref PrivateSubnet1
//         - !Ref PrivateSubnet2
//       SecurityGroupIds:
//         - !GetAtt AuthorizeInboundVpcTrafficSecurityGroup.GroupId # Referencing SG ID
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-sts-endpoint
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName

//   ECRApiVpcEndpoint:
//     Type: AWS::EC2::VPCEndpoint
//     Properties:
//       VpcId: !Ref RosaVPC
//       ServiceName: !Sub com.amazonaws.${AWS::Region}.ecr.api
//       VpcEndpointType: Interface
//       PrivateDnsEnabled: true
//       SubnetIds:
//         - !Ref PrivateSubnet1
//         - !Ref PrivateSubnet2
//       SecurityGroupIds:
//         - !GetAtt AuthorizeInboundVpcTrafficSecurityGroup.GroupId
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-ecr-api-endpoint
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName

//   ECRDkrVpcEndpoint:
//     Type: AWS::EC2::VPCEndpoint
//     Properties:
//       VpcId: !Ref RosaVPC
//       ServiceName: !Sub com.amazonaws.${AWS::Region}.ecr.dkr
//       VpcEndpointType: Interface
//       PrivateDnsEnabled: true
//       SubnetIds:
//         - !Ref PrivateSubnet1
//         - !Ref PrivateSubnet2
//       SecurityGroupIds:
//         - !GetAtt AuthorizeInboundVpcTrafficSecurityGroup.GroupId
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-ecr-dkr-endpoint
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName

//   S3VpcEndpoint:
//     Type: AWS::EC2::VPCEndpoint
//     Properties:
//       VpcId: !Ref RosaVPC
//       ServiceName: !Sub com.amazonaws.${AWS::Region}.s3
//       VpcEndpointType: Gateway
//       RouteTableIds:
//         - !Ref PrivateRouteTable # Associate with the private route table
//       Tags:
//         - Key: Name
//           Value: !Sub ${ClusterName}-s3-endpoint
//         - Key: Terraform
//           Value: "true"
//         - Key: service
//           Value: ROSA
//         - Key: cluster_name
//           Value: !Ref ClusterName

// Outputs:
//   VpcId:
//     Description: The ID of the created VPC.
//     Value: !Ref RosaVPC
//     Export:
//       Name: !Sub ${AWS::StackName}-VpcId

//   PrivateSubnetIds:
//     Description: A comma-separated list of the private subnet IDs.
//     Value: !Join [",", [!Ref PrivateSubnet1, !Ref PrivateSubnet2]]
//     Export:
//       Name: !Sub ${AWS::StackName}-PrivateSubnetIds

//   PrivateRouteTableId:
//     Description: The ID of the private route table.
//     Value: !Ref PrivateRouteTable
//     Export:
//       Name: !Sub ${AWS::StackName}-PrivateRouteTableId

//   SecurityGroupId:
//     Description: The ID of the security group for internal VPC traffic.
//     Value: !GetAtt AuthorizeInboundVpcTrafficSecurityGroup.GroupId
//     Export:
//       Name: !Sub ${AWS::StackName}-SecurityGroupId
// EOF
// ----

// . Create an AWS VPC using the default CloudFormations template by running the following command:
// +
// [source,terminal]
// ----
// $ rosa create network --template-dir TEMPLATES
// ----
// endif::rosa-egress-lockdown[]

.Verification
* When completed, you receive a summary of the created resources:
+
[source,terminal]
----
INFO[0140] Resources created in stack:
INFO[0140] Resource: AttachGateway, Type: AWS::EC2::VPCGatewayAttachment, ID: <gateway_id>
INFO[0140] Resource: EC2VPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: <vpce_id>
INFO[0140] Resource: EcrApiVPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: <vpce_id>
INFO[0140] Resource: EcrDkrVPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: <vpce_id>
INFO[0140] Resource: ElasticIP1, Type: AWS::EC2::EIP, ID: <IP>
INFO[0140] Resource: ElasticIP2, Type: AWS::EC2::EIP, ID: <IP>
INFO[0140] Resource: InternetGateway, Type: AWS::EC2::InternetGateway, ID: igw-016e1a71b9812464e
INFO[0140] Resource: KMSVPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: <vpce_id>
INFO[0140] Resource: NATGateway1, Type: AWS::EC2::NatGateway, ID: <nat-gateway_id>
INFO[0140] Resource: PrivateRoute, Type: AWS::EC2::Route, ID: <route_id>
INFO[0140] Resource: PrivateRouteTable, Type: AWS::EC2::RouteTable, ID: <route_id>
INFO[0140] Resource: PrivateSubnetRouteTableAssociation1, Type: AWS::EC2::SubnetRouteTableAssociation, ID: <route_id>
INFO[0140] Resource: PublicRoute, Type: AWS::EC2::Route, ID: <route_id>
INFO[0140] Resource: PublicRouteTable, Type: AWS::EC2::RouteTable, ID: <route_id>
INFO[0140] Resource: PublicSubnetRouteTableAssociation1, Type: AWS::EC2::SubnetRouteTableAssociation, ID: <route_id>
INFO[0140] Resource: S3VPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: <vpce_id>
INFO[0140] Resource: STSVPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: <vpce_id>
INFO[0140] Resource: SecurityGroup, Type: AWS::EC2::SecurityGroup, ID: <security-group_id>
INFO[0140] Resource: SubnetPrivate1, Type: AWS::EC2::Subnet, ID: <private_subnet_id-1>
INFO[0140] Resource: SubnetPublic1, Type: AWS::EC2::Subnet, ID: <public_subnet_id-1>
INFO[0140] Resource: VPC, Type: AWS::EC2::VPC, ID: <vpc_id>
INFO[0140] Stack rosa-network-stack-5555 created
----
+
--
* The `<private_subnet_id-1>` and `<public_subnet_id-1>` subnet IDs are used to create your cluster when using the `rosa create cluster` command.
* The network stack name (`rosa-network-stack-5555`) is used to delete the resource later.
--

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-vpc-terraform_{context}"]
= Creating a Virtual Private Cloud using Terraform

[role="_abstract"]
Terraform is a tool that allows you to create various resources using an established template. You can use Terraform with default options to create a Virtual Private Cloud for your OpenShift Container Platform cluster.

[NOTE]
====
The Terraform instructions are for testing and demonstration purposes. Your own installation requires some modifications to the VPC for your own use. Use this Terraform script in the same region where you intend to install your cluster. These examples use `us-east-2`.
====

.Prerequisites

* You have installed Terraform version 1.4.0 or newer on your machine.
* You have installed Git on your machine.

.Procedure

. Open a shell prompt and clone the Terraform VPC repository by running the following command:
+
[source,terminal]
----
$ git clone https://github.com/openshift-cs/terraform-vpc-example
----

. Navigate to the created directory by running the following command:
+
[source,terminal]
----
$ cd terraform-vpc-example
----
+
[source,terminal]
----
$ cd terraform-vpc-example/zero-egress
----

. Initiate the Terraform file by running the following command:
+
[source,terminal]
----
$ terraform init
----
+
A message confirming the initialization appears when this process completes.

. To build your VPC Terraform plan based on the existing Terraform template, run the `plan` command. You must include your AWS region, availability zones, CIDR blocks, and private subnets. You can choose to specify a cluster name. A `rosa-zero-egress.tfplan` file is added to the `hypershift-tf` directory after the `terraform plan` completes. For more detailed options, see the Terraform VPC repository's README file.
+
[source,terminal]
----
$ terraform plan -out rosa-zero-egress.tfplan -var region=<aws_region> \
      -var 'availability_zones=<availability_zones>' \
      -var vpc_cidr_block=<vpc_cidr_block> \
      -var 'private_subnets=<private_subnets>'
----
+
--
where:

`<aws_region>`:: Enter your AWS region.
`<availability_zones>`:: Enter the availability zones for the VPC. For example, for a VPC that uses `ap-southeast-1`, you would use the following as availability zones: `["ap-southeast-1a", "ap-southeast-1b", "ap-southeast-1c"]`.
`<vpc_cidr_block>`:: Enter the CIDR block for your VPC. For example, `10.0.0.0/16`.
`<private_subnets>`:: Enter each of the subnets that are created for the VPC. For example, `["10.0.0.0/24", "10.0.1.0/24", "10.0.2.0/24"]`.
--
. To build your VPC Terraform plan based on the existing Terraform template, run the `plan` command. You must include your AWS region. You can choose to specify a cluster name. A `rosa.tfplan` file is added to the `hypershift-tf` directory after the `terraform plan` completes. For more detailed options, see the Terraform VPC repository's README file.
+
[source,terminal]
----
$ terraform plan -out rosa.tfplan -var region=<region>
----

. Apply this plan file to build your VPC by running the following command:
+
[source,terminal]
----
$ terraform apply rosa-zero-egress.tfplan
----
+
[source,terminal]
----
$ terraform apply rosa.tfplan
----
+
.. Optional: Capture the Terraform-provisioned private, public, and machinepool subnet IDs as environment variables to use when creating your OpenShift Container Platform cluster:
+
[source,terminal]
----
$ export SUBNET_IDS=$(terraform output -raw cluster-subnets-string)
----
+
.. Verify that the variables were correctly set with the following command:
+
[source,terminal]
----
$ echo $SUBNET_IDS
----
+
.Example output
[source,terminal]
----
$ subnet-0a6a57e0f784171aa,subnet-078e84e5b10ecf5b0
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-vpc-manual_{context}"]
= Requirements for manually creating an AWS Virtual Private Cloud

[role="_abstract"]
If you do not use a managed infrastructure tool such as Terraform or AWS CloudFormation to create your Virtual Private Cloud (VPC), you can create it manually through the AWS console. A manually created VPC must meet specific requirements for use with OpenShift Container Platform.

// Snippet included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="troubleshooting_shared-vpc-hcp_vpc-creation_{context}"]
= Troubleshooting cluster creation

[role="_abstract"]
If your cluster fails to install, common VPC configuration issues might be the cause.

* Ensure your DHCP option set includes a domain name, and ensure that the domain name does not include any spaces or capital letters.
* If your VPC uses a custom DNS resolver (the `domain name servers` field is not `AmazonProvideDNS`), ensure that it can resolve the private hosted zones in Route53.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc

[id="rosa-hcp-vpc-subnet-tagging_{context}"]
= Tagging your subnets

[role="_abstract"]
If you created your own VPC to create a OpenShift Container Platform cluster, you must tag your VPC subnets.
Before you can use your VPC to create a OpenShift Container Platform cluster, you must tag your VPC subnets.
Automated service preflight checks verify that these resources are tagged correctly before you can use these resources for a cluster.

.Required subnet tags
[cols="3a,8a,8a", options="header"]
|===
| Resource
| Key
| Value

| Public subnet
| `kubernetes.io/role/elb`
| `1` (or no value)

| Private subnet
| `kubernetes.io/role/internal-elb`
| `1` (or no value)

|===

[NOTE]
====
You must tag at least one private subnet and, if applicable, one public subnet.
====

.Prerequisites

* You have created a VPC.
* You have installed the `aws` CLI.

.Procedure

* Tag your resources in your terminal by running the following commands:
.. For public subnets, run:
+
[source,terminal]
----
$ aws ec2 create-tags --resources <public-subnet-id> --region <aws_region> --tags Key=kubernetes.io/role/elb,Value=1
----
.. For private subnets, run:
+
[source,terminal]
----
$ aws ec2 create-tags --resources <private-subnet-id> --region <aws_region> --tags Key=kubernetes.io/role/internal-elb,Value=1
----

.Verification

* Verify that the tag is correctly applied by running the following command:
+
[source,terminal]
----
$ aws ec2 describe-tags --filters "Name=resource-id,Values=<subnet_id>"
----
+
For example:
+
[source,text]
----
TAGS    Name                    <subnet-id>        subnet  <prefix>-subnet-public1-us-east-1a
TAGS    kubernetes.io/role/elb  <subnet-id>        subnet  1
----

// Module included in the following assemblies:
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * support/troubleshooting/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-hcp-prepare-iam-resources.adoc
[id="rosa-sts-ocm-roles-and-permissions-iam-basic-role_{context}"]
= Creating an ocm-role IAM role

[role="_abstract"]
You create your `ocm-role` IAM roles by using the {rosa-cli-first}. If you want to create and manage clusters by using only the {rosa-cli-first} and the OpenShift CLI (`oc`), you can use the `--no-console` profile for the `ocm-role` IAM resource. For more information about the `ocm-role` IAM resource permissions profile, see the _Additional resources_.

[IMPORTANT]
====
You must create the `ocm-role` IAM role before you can create your OpenShift Container Platform cluster.
====

.Prerequisites

* You have an AWS account.
* You have Red{nbsp}Hat Organization Administrator privileges in the {cluster-manager} organization.
* You have the permissions required to install AWS account-wide roles.
* You have installed and configured the latest {rosa-cli}, `rosa`, on your installation host.

.Procedure
* Run one of the following commands to create the required `ocm-role` IAM resource:
+
[IMPORTANT]
====
The process to change your `ocm-role` IAM resource profile requires you to unlink and delete the current `ocm-role` IAM resource and create a new one with the required profile.
====

** To create an `ocm-role` IAM role with standard privileges, run the following command:
+
[source,terminal]
----
$ rosa create ocm-role
----
+
** To create an `ocm-role` IAM role with admin privileges, run the following command:
+
[IMPORTANT]
====
The admin profile supports "auto" mode configuration for OpenShift Container Platform clusters which provisions OIDC Configuration and Operator roles automatically. To achieve this automatic flow, the profile has a wider set of permissions than the standard profile.
====
+
[source,terminal]
----
$ rosa create ocm-role --admin
----
+
This command allows you to create the role by specifying specific attributes. The following example output shows the "auto mode" selected, which lets the {rosa-cli} (`rosa`) create your Operator roles and policies.
See "Methods of account-wide role creation" for more information. The following example shows what your creation flow might look like.
+
[source,terminal]
----
I: Creating ocm role
? Role prefix: ManagedOpenShift
? Enable admin capabilities for the OCM role (optional): No
? Permissions boundary ARN (optional):
? Role Path (optional):
? Role creation mode: auto
I: Creating role using 'arn:aws:iam::<ARN>:user/<UserName>'
? Create the 'ManagedOpenShift-OCM-Role-182' role? Yes
I: Created role 'ManagedOpenShift-OCM-Role-182' with ARN  'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182'
I: Linking OCM role
? OCM Role ARN: arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182
? Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' role with organization '<AWS ARN>'? Yes
I: Successfully linked role-arn 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' with organization account '<AWS ARN>'
----
+
where:
+
--
`Role prefix`:: A prefix value for all of the created AWS resources. In this example, `ManagedOpenShift` prepends all of the AWS resources.
`Enable admin capabilities for the OCM role (optional)`:: Choose if you want this role to have the additional admin permissions.
+
[NOTE]
====
You do not see this prompt if you used the `--admin` option.
====
+
`Permissions boundary ARN (optional)`:: The Amazon Resource Name (ARN) of the policy to set permission boundaries.
`Role Path (optional)`:: Specify an IAM path for the user name.
`Role creation mode`:: Choose the method to create your AWS roles. By using `auto`, the {rosa-cli} generates and links the roles and policies. In the `auto` mode, you receive some different prompts to create the AWS roles.
`Create the 'ManagedOpenShift-OCM-Role-182' role?`:: The `auto` method asks if you want to create a specific `ocm-role` by using your prefix.
`OCM Role ARN`:: Confirm that you want to associate your IAM role with your {cluster-manager}.
`Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' role with organization '<AWS ARN>'?`:: Links the created role with your AWS organization.
--

** To create an `ocm-role` IAM role with the minimum required privileges, run the following command:
+
[NOTE]
====
While the `no-console` profile offers the minimum permissions policy that can still create OpenShift Container Platform clusters, the permissions are insufficient if you want to use {cluster-manager-url} for cluster creation.
====
+
[source,terminal]
----
$ rosa create ocm-role --no-console
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_planning/rosa-hcp-prepare-iam-roles-resources.adoc

[id="rosa-sts-creating-account-wide-sts-roles-and-policies_{context}"]
= Creating the account-wide STS roles and policies

[role="_abstract"]
Before you create a OpenShift Container Platform cluster, you must create the required account-wide IAM roles and policies by using the {rosa-cli-first}.

[NOTE]
====
Specific AWS-managed policies for OpenShift Container Platform must be attached to each role. Customer-managed policies must not be used with these required account roles. For more information regarding AWS-managed policies for OpenShift Container Platform clusters, see AWS managed policies for OpenShift Container Platform.
====

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform in the AWS Console.
* You have installed and configured the latest {rosa-cli-first} on your installation host.
* You have logged in to your Red{nbsp}Hat account by using the {rosa-cli}.

.Procedure

. If they do not exist in your AWS account, create the required account-wide STS roles and attach the policies by running the following command:
+
[source,terminal]
----
$ rosa create account-roles --hosted-cp
----
[source,terminal]
----
$ export PREFIX=<custom_prefix>; rosa create account-roles --hosted-cp --prefix $PREFIX
----
+
When using FIPS encryption, you need to set a custom prefix instead of using the default `ManagedOpenShift` prefix.

. Verify that your worker role has the correct AWS policy by running the following command:
+
[source,terminal]
----
$ aws iam attach-role-policy \
--role-name ManagedOpenShift-HCP-ROSA-Worker-Role \
--policy-arn "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
----
+
--
`--role-name ManagedOpenShift-HCP-ROSA-Worker-Role`::This role needs to include the prefix that was created in the previous step.
--

. Optional: Set your prefix as an environmental variable by running the following command:
+
[source,terminal]
----
$ export ACCOUNT_ROLES_PREFIX=<account_role_prefix>
----

** View the value of the variable by running the following command:
+
[source,terminal]
----
$ echo $ACCOUNT_ROLES_PREFIX
----
+
For example:
+
[source,terminal]
----
ManagedOpenShift
----

[NOTE]
====
As an additional safeguard, after role creation, you can manually update the trust policies of the Support and Installer account-wide roles to include an external ID. For more information, see _About external ID_.
====

[role="_additional-resources"]
.Additional resources

* AWS managed IAM policies for OpenShift Container Platform

// Module included in the following assemblies:
//
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_architecture/rosa-oidc-overview.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc
// * rosa_planning/rosa-hcp-prepare-iam-roles-resources.adoc

[id="rosa-sts-byo-oidc_{context}"]
= Creating an OpenID Connect configuration

[role="_abstract"]
OpenShift Container Platform clusters use OIDC and the AWS Security Token Service (STS) to authenticate Operator access to AWS resources they require to perform their functions. Each production cluster requires its own OIDC configuration. When creating a OpenShift Container Platform cluster, you can create the OpenID Connect (OIDC) configuration before creating your cluster.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have installed and configured the latest {rosa-cli-first} on your installation host.

.Procedure

. To create your OIDC configuration alongside the AWS resources, run the following command:
+
[source,terminal]
----
$ rosa create oidc-config --mode=auto --yes
----
+
This command returns the following information.
+
For example:
+
[source,terminal]
----
? Would you like to create a Managed (Red Hat hosted) OIDC Configuration Yes
I: Setting up managed OIDC configuration
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
	rosa create operator-roles --prefix <user-defined> --oidc-config-id 13cdr6b
If you are going to create a Hosted Control Plane cluster please include '--hosted-cp'
I: Creating OIDC provider using 'arn:aws:iam::4540112244:user/userName'
? Create the OIDC provider? Yes
I: Created OIDC provider with ARN 'arn:aws:iam::4540112244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/13cdr6b'
----
+
When creating your cluster, you must supply the OIDC config ID. The CLI output provides this value for `--mode auto`, otherwise you must determine these values based on `aws` CLI output for `--mode manual`.

. Optional: you can save the OIDC configuration ID as a variable to use later. Run the following command to save the variable:
+
--
[source,terminal]
----
$ export OIDC_ID=<oidc_config_id>
----
`<oidc_config_id>`:: In this example output, the OIDC configuration ID is `13cdr6b`.
--

** View the value of the variable by running the following command:
+
[source,terminal]
----
$ echo $OIDC_ID
----
+
For example:
+
[source,terminal]
----
13cdr6b
----

.Verification

* You can list the possible OIDC configurations available for your clusters that are associated with your user organization. Run the following command:
+
[source,terminal]
----
$ rosa list oidc-config
----
+
For example:
+
[source,terminal]
----
ID                                MANAGED  ISSUER URL                                                             SECRET ARN
2330dbs0n8m3chkkr25gkkcd8pnj3lk2  true     https://dvbwgdztaeq9o.cloudfront.net/2330dbs0n8m3chkkr25gkkcd8pnj3lk2
233hvnrjoqu14jltk6lhbhf2tj11f8un  false    https://oidc-r7u1.s3.us-east-1.amazonaws.com                           aws:secretsmanager:us-east-1:242819244:secret:rosa-private-key-oidc-r7u1-tM3MDN
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_planning/rosa-hcp-prepare-iam-roles-resources.adoc

[id="rosa-operator-config_{context}"]
= Creating Operator roles and policies

[role="_abstract"]
When you deploy a OpenShift Container Platform cluster, you must create the Operator IAM roles. The cluster Operators use the Operator roles and policies to obtain temporary permissions to perform cluster operations, such as managing storage and external access.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have installed and configured the latest {rosa-cli-first} on your installation host.
* You created the account-wide AWS roles.

.Procedure
. To create your Operator roles, run the following command:
+
[source,terminal]
----
$ rosa create operator-roles --hosted-cp --prefix=$PREFIX --oidc-config-id=$OIDC_ID
----
+
The Operator roles are now created and ready to use for creating your OpenShift Container Platform cluster.
. To create your Operator roles, run the following command:
+
[source,terminal]
----
$ rosa create operator-roles --hosted-cp --prefix=$OPERATOR_ROLES_PREFIX --oidc-config-id=$OIDC_ID --installer-role-arn arn:aws:iam::$AWS_ACCOUNT_ID:role/${ACCOUNT_ROLES_PREFIX}-HCP-ROSA-Installer-Role
----
+
The following breakdown provides options for the Operator role creation.
+
[source,terminal]
----
$ rosa create operator-roles --hosted-cp
	--prefix=$OPERATOR_ROLES_PREFIX
	--oidc-config-id=$OIDC_ID
	--installer-role-arn arn:aws:iam::$AWS_ACCOUNT_ID:role/$ACCOUNT_ROLES_PREFIX-HCP-ROSA-Installer-Role
----
+
where:
+
--
`--prefix=`:: You must supply a prefix when creating these Operator roles. Failing to do so produces an error. See the Additional resources of this section for information on the Operator prefix.
`--oidc-config-id=`:: This value is the OIDC configuration ID that you created for your OpenShift Container Platform cluster.
`--installer-role-arn`:: This value is the installer role ARN that you created when you created the OpenShift Container Platform account roles.
--
+
You must include the `--hosted-cp` parameter to create the correct roles for OpenShift Container Platform clusters. This command returns the following information.
+
For example:
+
[source,terminal]
----
? Role creation mode: auto
? Operator roles prefix: <pre-filled_prefix>
? OIDC Configuration ID: 23soa2bgvpek9kmes9s7os0a39i13qm4 | https://dvbwgdztaeq9o.cloudfront.net/23soa2bgvpek9kmes9s7os0a39i13qm4
? Create hosted control plane operator roles: Yes
W: More than one Installer role found
? Installer role ARN: arn:aws:iam::4540112244:role/<prefix>-HCP-ROSA-Installer-Role
? Permissions boundary ARN (optional):
I: Reusable OIDC Configuration detected. Validating trusted relationships to operator roles:
I: Creating roles using 'arn:aws:iam::4540112244:user/<userName>'
I: Created role '<prefix>-openshift-cluster-csi-drivers-ebs-cloud-credentials' with ARN 'arn:aws:iam::4540112244:role/<prefix>-openshift-cluster-csi-drivers-ebs-cloud-credentials'
I: Created role '<prefix>-openshift-cloud-network-config-controller-cloud-credenti' with ARN 'arn:aws:iam::4540112244:role/<prefix>-openshift-cloud-network-config-controller-cloud-credenti'
I: Created role '<prefix>-kube-system-kube-controller-manager' with ARN 'arn:aws:iam::4540112244:role/<prefix>-kube-system-kube-controller-manager'
I: Created role '<prefix>-kube-system-capa-controller-manager' with ARN 'arn:aws:iam::4540112244:role/<prefix>-kube-system-capa-controller-manager'
I: Created role '<prefix>-kube-system-control-plane-operator' with ARN 'arn:aws:iam::4540112244:role/<prefix>-kube-system-control-plane-operator'
I: Created role '<prefix>-kube-system-kms-provider' with ARN 'arn:aws:iam::4540112244:role/<prefix>-kube-system-kms-provider'
I: Created role '<prefix>-openshift-image-registry-installer-cloud-credentials' with ARN 'arn:aws:iam::4540112244:role/<prefix>-openshift-image-registry-installer-cloud-credentials'
I: Created role '<prefix>-openshift-ingress-operator-cloud-credentials' with ARN 'arn:aws:iam::4540112244:role/<prefix>-openshift-ingress-operator-cloud-credentials'
I: To create a cluster with these roles, run the following command:
	rosa create cluster --sts --oidc-config-id 23soa2bgvpek9kmes9s7os0a39i13qm4 --operator-roles-prefix <prefix> --hosted-cp
----
+
where:
+
--
`Operator roles prefix`:: This field is prepopulated with the prefix that you set in the initial creation command.
`OIDC Configuration ID`:: This field requires you to select an OIDC configuration that you created for your OpenShift Container Platform cluster.
--
+
The Operator roles are now created and ready to use for creating your OpenShift Container Platform cluster.

.Verification

* You can list the Operator roles associated with your OpenShift Container Platform account. Run the following command:
+
[source,terminal]
----
$ rosa list operator-roles
----
+
For example:
+
[source,terminal]
----
I: Fetching operator roles
ROLE PREFIX  AMOUNT IN BUNDLE
<prefix>      8
? Would you like to detail a specific prefix Yes
? Operator Role Prefix: <prefix>
ROLE NAME                                                         ROLE ARN                                                                                         VERSION  MANAGED
<prefix>-kube-system-capa-controller-manager                       arn:aws:iam::4540112244:role/<prefix>-kube-system-capa-controller-manager                       4.13     No
<prefix>-kube-system-control-plane-operator                        arn:aws:iam::4540112244:role/<prefix>-kube-system-control-plane-operator                        4.13     No
<prefix>-kube-system-kms-provider                                  arn:aws:iam::4540112244:role/<prefix>-kube-system-kms-provider                                  4.13     No
<prefix>-kube-system-kube-controller-manager                       arn:aws:iam::4540112244:role/<prefix>-kube-system-kube-controller-manager                       4.13     No
<prefix>-openshift-cloud-network-config-controller-cloud-credenti  arn:aws:iam::4540112244:role/<prefix>-openshift-cloud-network-config-controller-cloud-credenti  4.13     No
<prefix>-openshift-cluster-csi-drivers-ebs-cloud-credentials       arn:aws:iam::4540112244:role/<prefix>-openshift-cluster-csi-drivers-ebs-cloud-credentials       4.13     No
<prefix>-openshift-image-registry-installer-cloud-credentials      arn:aws:iam::4540112244:role/<prefix>-openshift-image-registry-installer-cloud-credentials      4.13     No
<prefix>-openshift-ingress-operator-cloud-credentials              arn:aws:iam::4540112244:role/<prefix>-openshift-ingress-operator-cloud-credentials              4.13     No
----
+
After the command runs, it displays all the prefixes associated with your AWS account and notes how many roles are associated with this prefix. If you need to see all of these roles and their details, enter "Yes" on the detail prompt to have these roles listed out with specifics.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-sts-creating-a-cluster-cli_{context}"]
= Creating a OpenShift Container Platform cluster using the CLI

[role="_abstract"]
You can create a OpenShift Container Platform cluster quickly by using the {rosa-cli-first} with default options.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform in the AWS Console.
* You have installed and configured the latest ROSA CLI (`rosa`) on your installation host. Run `rosa version` to see your currently installed version of the ROSA CLI. If a newer version is available, the CLI provides a link to download this upgrade.
* You have logged in to your Red{nbsp}Hat account by using the ROSA CLI.
* You have created an OIDC configuration.
* You have verified that the AWS Elastic Load Balancing (ELB) service role exists in your AWS account.

.Procedure

. Use one of the following commands to create your OpenShift Container Platform cluster:
+
[NOTE]
====
When creating a OpenShift Container Platform cluster, the default machine Classless Inter-Domain Routing (CIDR) is `10.0.0.0/16`. If this does not correspond to the CIDR range for your VPC subnets, add `--machine-cidr <address_block>` to the following commands. To learn more about the default CIDR ranges for OpenShift Container Platform, see CIDR range definitions.
====
+
* If you did not set environmental variables, run the following command:
+
[source,terminal]
----
$ rosa create cluster --cluster-name=<cluster_name> \
    --mode=auto --hosted-cp [--private] \
    --operator-roles-prefix <operator-role-prefix> \
    --external-id <external-id> \
    --oidc-config-id <id-of-oidc-configuration> \
    --subnet-ids=<public-subnet-id>,<private-subnet-id>
----
+
--
where:

`<cluster_name>`:: Specify the name of your cluster. If your cluster name is longer than 15 characters, it contains an autogenerated domain prefix as a subdomain for your provisioned cluster on openshiftapps.com. To customize the subdomain, use the `--domain-prefix` flag. The domain prefix cannot be longer than 15 characters, must be unique, and cannot be changed after cluster creation.
`--private`:: Optional. Use the `--private` argument to create private OpenShift Container Platform clusters. If you use this argument, ensure that you only use your private subnet ID for `--subnet-ids`.
`<operator-role-prefix>`:: By default, the cluster-specific Operator role names are prefixed with the cluster name and a random 4-digit hash. You can optionally specify a custom prefix to replace `<cluster_name>-<hash>` in the role names. The prefix is applied when you create the cluster-specific Operator IAM roles. For information about the prefix, see _About custom Operator IAM role prefixes_.
`<external-id>`:: Optional. A unique identifier that might be required when you assume a role in another account. For more information about external ID, see _About external ID_.

[NOTE]
====
If you specified custom ARN paths when you created the associated account-wide roles, the custom path is automatically detected. The custom path is applied to the cluster-specific Operator roles when you create them in a later step.
====
--

* If you set the environment variables, create a cluster with a private API and private Ingress by running the following command:
+
[source,terminal]
----
$ rosa create cluster --private --cluster-name=<cluster_name> \
    --mode=auto --hosted-cp --operator-roles-prefix=$OPERATOR_ROLES_PREFIX \
    --oidc-config-id=$OIDC_ID --subnet-ids=$SUBNET_IDS
----
+
* If you set the environmental variables, create a cluster with a single, initial machine pool, a publicly available API, and a publicly available Ingress by running the following command:
+
[source,terminal]
----
$ rosa create cluster --cluster-name=<cluster_name> --mode=auto \
    --hosted-cp --operator-roles-prefix=$OPERATOR_ROLES_PREFIX \
    --oidc-config-id=$OIDC_ID --subnet-ids=$SUBNET_IDS
----
+
. Check the status of your cluster by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
The following `State` field changes are listed in the output as the cluster installation progresses:
+
* `pending (Preparing account)`
* `installing (DNS setup in progress)`
* `installing`
* `ready`
+
[NOTE]
====
If the installation fails or the `State` field does not change to `ready` after more than 10 minutes, check the installation troubleshooting documentation for details. For more information, see _Troubleshooting installations_. For steps to contact Red{nbsp}Hat Support for assistance, see _Getting support for Red{nbsp}Hat OpenShift Service on AWS_.
====
+
. Track the progress of the cluster creation by watching the OpenShift Container Platform installation program logs. To check the logs, run the following command:
+
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name> --watch
----
+
Optional: To watch for new log messages as the installation progresses, use the `--watch` argument.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-creating-a-cluster-using-defaults-ocm_{context}"]
= Create a cluster with the default options using {cluster-manager}

[role="_abstract"]
When using {cluster-manager-first} on the {hybrid-console-url} to create a OpenShift Container Platform cluster, you can select the default options to create the cluster quickly. You can also use the admin {cluster-manager} IAM role to enable automatic deployment of the cluster-specific Operator roles and the OpenID Connect (OIDC) provider.

.Procedure

. Navigate to {cluster-manager-url} and select *Create cluster*.

. On the *Create an OpenShift cluster* page, select *Create cluster* in the *OpenShift Container Platform (ROSA)* row.

. Verify that your AWS account ID is listed in the *Associated AWS accounts* drop-down menu and that the installation program, support, worker, and control plane account role Amazon Resource Names (ARNs) are listed on the *Accounts and roles* page.
+
[NOTE]
====
If your AWS account ID is not listed, check that you have successfully associated your AWS account with your Red{nbsp}Hat organization. If your account role ARNs are not listed, check that the required account-wide STS roles exist in your AWS account.
====

. Click *Next*.

. On the *Cluster details* page, provide a name for your cluster in the *Cluster name* field. Leave the default values in the remaining fields and click *Next*.
+
[NOTE]
====
Cluster creation generates a domain prefix as a subdomain for your provisioned cluster on `openshiftapps.com`. If the cluster name is less than or equal to 15 characters, that name is used for the domain prefix. If the cluster name is longer than 15 characters, the domain prefix is randomly generated as a 15-character string. To customize the subdomain, select the *Create custom domain prefix* checkbox, and enter your domain prefix name in the *Domain prefix* field.
====
. On the *Machine pools* page, select your created VPC and at least one of your private subnet IDs.

. On the *Network configuration* page, if your cluster is publicly available, provide your public subnet ID.

. To deploy a cluster quickly, leave the default options in the *Cluster settings*, *Networking*, *Cluster roles and policies*, and *Cluster updates* pages and click *Next* on each page.

. On the *Review your OpenShift Container Platform cluster* page, review the summary of your selections and click *Create cluster* to start the installation.
+
. Optional: On the *Overview* tab, you can enable the delete protection feature by selecting *Enable*, which is located directly under *Delete Protection: Disabled*. This prevents your cluster from being deleted. To disable delete protection, select *Disable*.
By default, clusters are created with the delete protection feature disabled.
+

.Verification

. Go to the *Overview* page for your cluster.
. Check the progress of the installation and view the installation logs.
. Go to  *Details* > *Status* and confirm that your cluster is listed as `Ready`.
+
[NOTE]
====
If the installation fails or the cluster *State* does not change to *Ready* after about 40 minutes, check the installation troubleshooting documentation for details. For more information, see _Troubleshooting installations_. For steps to contact Red{nbsp}Hat Support for assistance, see _Getting support for Red{nbsp}Hat OpenShift Service on AWS_.
====

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-sts-external-id_{context}"]
= About external ID

[role="_abstract"]
An external ID functions as a unique, separate, identifier embedded within your OpenShift Container Platform account-wide roles, blocking unauthorized third-party access.

During cluster creation, you might be asked to supply an external ID. This serves as an additional safeguard that prevents cross-account identity spoofing, ensuring that no one else can trigger automation against your AWS infrastructure.

When Red{nbsp}Hat's automation plane issues an `sts:AssumeRole` API call to your account to manage cluster resources, it must present this exact identifier. If the string does not match the condition block defined in your AWS IAM trust relationship, AWS automatically blocks the request. This ensures Red{nbsp}Hat's automation can only access your environment when explicitly acting on behalf of your organization.

When you assign an external ID, it is applied to both the Support IAM role and the Installer IAM role, through their associated trust policies:

* Support role: when Red{nbsp}Hat Site Reliability Engineers (SREs) need to perform diagnostic, maintenance or any other support function, they assume this role.
+
.Example support trust policy with an external ID `sts_hcp_support_trust_policy.json`
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::710019948333:role/RH-Technical-Support-15234082"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
              "StringEquals": {
                "sts:ExternalID": "<external_id>"
              }
           }
        }
    ]
}
----
+
* Installer role: when {cluster-manager-first} (OCM) automation needs to provision, scale or delete core cluster infrastructure, it assumes this role.
+
.Example installer trust policy with an external ID `sts_hcp_installer_trust_policy.json`
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
           "Effect": "Allow",
           "Principal": {
               "AWS": "arn:aws:iam::710019948333:role/RH-Managed-OpenShift-Installer"
           },
           "Action": "sts:AssumeRole",
           "Condition": {
             "StringEquals": {
               "sts:ExternalID": "<external_id>"
             }
          }
        }
    ]
}
----

.Additional resources
* Example scenario using an external ID
* Securely using external ID for accessing AWS accounts owned by others

[role="_additional-resources"]
[id="additional-resources_rosa-sts-creating-a-cluster-quickly"]
== Additional resources

* Getting started with OpenShift Container Platform using the ROSA CLI in auto mode (AWS documentation)
* Full list of the supported certificates
* AWS CloudFormation documentation
* Default VPC AWS CloudFormation template
* Terraform VPC repository
* Get Started with Amazon VPC
* HashiCorp Terraform documentation
* Subnet Auto Discovery
* About custom Operator IAM role prefixes
* About IAM resources for clusters that use STS
* AWS prerequisites for OpenShift Container Platform
* Creating OpenID Connect (OIDC) identity providers
* Troubleshooting OpenShift Container Platform installations
* Getting support for OpenShift Container Platform
