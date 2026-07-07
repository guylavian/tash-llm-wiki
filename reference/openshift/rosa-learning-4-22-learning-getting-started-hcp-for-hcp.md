---
title: "Creating a cluster"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-hcp-for-hcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-hcp-for-hcp
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Creating a cluster

[id="learning-getting-started-hcp-guide"]
= Creating a cluster

[role="_abstract"]
Follow this workshop to deploy a sample OpenShift Container Platform cluster, where you can set up the prerequisites such as {rosa-cli-first}, and create an admin user. You can then use your cluster in the next workshops.

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-hcp-for-hcp.adoc
[id="learning-getting-started-objects-prereqs-objectives_{context}"]
= Workshop objectives

[role="_abstract"]
This workshop teaches you how to create a cluster along with all of the needed prerequisites.

* Learn to create your cluster prerequisites:
** Create a sample virtual private cloud (VPC)
** Create sample OpenID Connect (OIDC) resources
* Create sample environment variables
* Deploy a sample OpenShift Container Platform cluster

[id="learning-getting-started-objects-prereqs-overall_{context}"]
== Prerequisites

* OpenShift Container Platform version 1.2.31 or later
* Amazon Web Service (AWS) command-line interface (CLI)
* {rosa-cli-first}
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-hcp-for-hcp.adoc
[id="learning-getting-started-create-vpc_{context}"]
= Creating a VPC

[role="_abstract"]
Before deploying a OpenShift Container Platform cluster, you must have both a Virtual Private Cloud (VPC) and OpenID Connect (OIDC) resources. We will create these resources first. OpenShift Container Platform uses the bring your own VPC (BYO-VPC) model.

.Procedure
. Make sure your AWS CLI (`aws`) is configured to use a region where OpenShift Container Platform is available. See the regions supported by the AWS CLI by running the following command:
+
[source,terminal]
----
$ rosa list regions --hosted-cp
----

. Create the VPC. For this workshop, the following script creates the VPC and its required components. It uses the region configured in your `aws` CLI.
+
[source,bash]
----
#!/bin/bash

set -e
##########
# This script will create the network requirements for a ROSA cluster. This will be
# a public cluster. This creates:
# - VPC
# - Public and private subnets
# - Internet Gateway
# - Relevant route tables
# - NAT Gateway
#
# This will automatically use the region configured for the aws cli
#
##########

VPC_CIDR=10.0.0.0/16
PUBLIC_CIDR_SUBNET=10.0.1.0/24
PRIVATE_CIDR_SUBNET=10.0.0.0/24

# Create VPC
echo -n "Creating VPC..."
VPC_ID=$(aws ec2 create-vpc --cidr-block $VPC_CIDR --query Vpc.VpcId --output text)

# Create tag name
aws ec2 create-tags --resources $VPC_ID --tags Key=Name,Value=$CLUSTER_NAME

# Enable dns hostname
aws ec2 modify-vpc-attribute --vpc-id $VPC_ID --enable-dns-hostnames
echo "done."

# Create Public Subnet
echo -n "Creating public subnet..."
PUBLIC_SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block $PUBLIC_CIDR_SUBNET --query Subnet.SubnetId --output text)

aws ec2 create-tags --resources $PUBLIC_SUBNET_ID --tags Key=Name,Value=$CLUSTER_NAME-public
echo "done."

# Create private subnet
echo -n "Creating private subnet..."
PRIVATE_SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block $PRIVATE_CIDR_SUBNET --query Subnet.SubnetId --output text)

aws ec2 create-tags --resources $PRIVATE_SUBNET_ID --tags Key=Name,Value=$CLUSTER_NAME-private
echo "done."

# Create an internet gateway for outbound traffic and attach it to the VPC.
echo -n "Creating internet gateway..."
IGW_ID=$(aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text)
echo "done."

aws ec2 create-tags --resources $IGW_ID --tags Key=Name,Value=$CLUSTER_NAME

aws ec2 attach-internet-gateway --vpc-id $VPC_ID --internet-gateway-id $IGW_ID > /dev/null 2>&1
echo "Attached IGW to VPC."

# Create a route table for outbound traffic and associate it to the public subnet.
echo -n "Creating route table for public subnet..."
PUBLIC_ROUTE_TABLE_ID=$(aws ec2 create-route-table --vpc-id $VPC_ID --query RouteTable.RouteTableId --output text)

aws ec2 create-tags --resources $PUBLIC_ROUTE_TABLE_ID --tags Key=Name,Value=$CLUSTER_NAME
echo "done."

aws ec2 create-route --route-table-id $PUBLIC_ROUTE_TABLE_ID --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID > /dev/null 2>&1
echo "Created default public route."

aws ec2 associate-route-table --subnet-id $PUBLIC_SUBNET_ID --route-table-id $PUBLIC_ROUTE_TABLE_ID > /dev/null 2>&1
echo "Public route table associated"

# Create a NAT gateway in the public subnet for outgoing traffic from the private network.
echo -n "Creating NAT Gateway..."
NAT_IP_ADDRESS=$(aws ec2 allocate-address --domain vpc --query AllocationId --output text)

NAT_GATEWAY_ID=$(aws ec2 create-nat-gateway --subnet-id $PUBLIC_SUBNET_ID --allocation-id $NAT_IP_ADDRESS --query NatGateway.NatGatewayId --output text)

aws ec2 create-tags --resources $NAT_IP_ADDRESS --resources $NAT_GATEWAY_ID --tags Key=Name,Value=$CLUSTER_NAME
sleep 10
echo "done."

# Create a route table for the private subnet to the NAT gateway.
echo -n "Creating a route table for the private subnet to the NAT gateway..."
PRIVATE_ROUTE_TABLE_ID=$(aws ec2 create-route-table --vpc-id $VPC_ID --query RouteTable.RouteTableId --output text)

aws ec2 create-tags --resources $PRIVATE_ROUTE_TABLE_ID $NAT_IP_ADDRESS --tags Key=Name,Value=$CLUSTER_NAME-private

aws ec2 create-route --route-table-id $PRIVATE_ROUTE_TABLE_ID --destination-cidr-block 0.0.0.0/0 --gateway-id $NAT_GATEWAY_ID > /dev/null 2>&1

aws ec2 associate-route-table --subnet-id $PRIVATE_SUBNET_ID --route-table-id $PRIVATE_ROUTE_TABLE_ID > /dev/null 2>&1

echo "done."

# echo "***********VARIABLE VALUES*********"
# echo "VPC_ID="$VPC_ID
# echo "PUBLIC_SUBNET_ID="$PUBLIC_SUBNET_ID
# echo "PRIVATE_SUBNET_ID="$PRIVATE_SUBNET_ID
# echo "PUBLIC_ROUTE_TABLE_ID="$PUBLIC_ROUTE_TABLE_ID
# echo "PRIVATE_ROUTE_TABLE_ID="$PRIVATE_ROUTE_TABLE_ID
# echo "NAT_GATEWAY_ID="$NAT_GATEWAY_ID
# echo "IGW_ID="$IGW_ID
# echo "NAT_IP_ADDRESS="$NAT_IP_ADDRESS

echo "Setup complete."
echo ""
echo "To make the cluster create commands easier, please run the following commands to set the environment variables:"
echo "export PUBLIC_SUBNET_ID=$PUBLIC_SUBNET_ID"
echo "export PRIVATE_SUBNET_ID=$PRIVATE_SUBNET_ID"
----

. The script outputs commands. Set the commands as environment variables to store the subnet IDs for later use. Run the following commands:
+
[source,terminal]
----
$ export PUBLIC_SUBNET_ID=$PUBLIC_SUBNET_ID
$ export PRIVATE_SUBNET_ID=$PRIVATE_SUBNET_ID
----

. Confirm your environment variables by running the following command:
+
[source,terminal]
----
$ echo "Public Subnet: $PUBLIC_SUBNET_ID"; echo "Private Subnet: $PRIVATE_SUBNET_ID"
----
+
*For example*:
+
[source,terminal]
----
Public Subnet: subnet-0faeeeb0000000000
Private Subnet: subnet-011fe340000000000
----
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-hcp-for-hcp.adoc
[id="learning-getting-started-oidc-config_{context}"]
= Creating your OIDC configuration

[role="_abstract"]
In this workshop, we will use the automatic mode when creating the OpenID Connect (OIDC) configuration. We will also store the OIDC ID as an environment variable for later use. The command uses the {rosa-cli} to create your cluster's unique OIDC configuration.

.Procedure
* Create the OIDC configuration by running the following command:
+
[source,terminal]
----
$ export OIDC_ID=$(rosa create oidc-config --mode auto --managed --yes -o json | jq -r '.id')
----
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-hcp-for-hcp.adoc
[id="learning-getting-started-env-variables_{context}"]
= Creating additional environment variables

[role="_abstract"]
To simplify your command-line execution and reduce repetitive typing, configure environment variables for your cluster deployments. Using these variables makes it faster and more efficient to run the command to create a OpenShift Container Platform cluster.

.Procedure
* Run the following command to set up environment variables:
+
[source,terminal]
----
$ export CLUSTER_NAME=<cluster_name>
$ export REGION=<VPC_region>
----
+
[TIP]
====
Run `rosa whoami` to find the VPC region.
====
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-hcp-for-hcp.adoc
[id="learning-getting-started-create-cluster_{context}"]
= Creating a cluster

[role="_abstract"]
To deploy and manage containerized applications in a cloud environment, create a OpenShift Container Platform cluster. You can efficiently perform this installation process by using the {rosa-cli}.

.Procedure
. *Optional:* Run the following command to create the account-wide roles and policies, including the Operator policies and the AWS IAM roles and policies:
+
[IMPORTANT]
====
Only complete this step if this is the _first time_ you are deploying OpenShift Container Platform in this account and you have _not_ yet created your account roles and policies.
====
+
[source,terminal]
----
$ rosa create account-roles --mode auto --yes
----

. Run the following command to create the cluster:
+
[source,terminal]
----
$ rosa create cluster --cluster-name $CLUSTER_NAME \
--subnet-ids ${PUBLIC_SUBNET_ID},${PRIVATE_SUBNET_ID} \
--hosted-cp \
--region $REGION \
--oidc-config-id $OIDC_ID \
--sts --mode auto --yes
----
+
The cluster is ready after about 10 minutes. The cluster will have a control plane across three AWS availability zones in your selected region and create two worker nodes in your AWS account.
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-hcp-for-hcp.adoc
[id="learning-getting-started-cluster-status_{context}"]
= Checking the installation status

[role="_abstract"]
To verify that your environment is operating correctly and to monitor the health of your deployments, youu can check the status of your cluster. You can quickly perform this check by using the {rosa-cli-first}.

.Procedure
. Run one of the following commands to check the status of the cluster:
+
* For a detailed view of the cluster status, run:
+
[source,terminal]
----
$ rosa describe cluster --cluster $CLUSTER_NAME
----
+
* For an abridged view of the cluster status, run:
+
[source,terminal]
----
$ rosa list clusters
----
+
* To watch the log as it progresses, run:
+
[source,terminal]
----
$ rosa logs install --cluster $CLUSTER_NAME --watch
----

. Once the state changes to “ready” your cluster is installed. It might take a few more minutes for the worker nodes to come online.

[role="_additional-resources"]
.Additional resources
* VPC documentation
