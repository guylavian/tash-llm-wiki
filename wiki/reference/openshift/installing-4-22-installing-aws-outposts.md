---
title: "Extending an AWS VPC cluster into an AWS Outpost"
type: reference
domain: openshift
slug: installing-4-22-installing-aws-outposts
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-aws-outposts
version: 4.22
family: installing
documentKind: "Documentation"
---

# Extending an AWS VPC cluster into an AWS Outpost

[id="installing-aws-outposts"]
= Extending an AWS VPC cluster into an AWS Outpost

In OpenShift Container Platform version 4.14, you could install a cluster on Amazon Web Services (AWS) with compute nodes running in AWS Outposts as a Technology Preview. As of OpenShift Container Platform version 4.15, this installation method is no longer supported. Instead, you can install a cluster on AWS into an existing VPC, and provision compute nodes on AWS Outposts as a postinstallation configuration task.

After installing a cluster on Amazon Web Services (AWS) into an existing Amazon Virtual Private Cloud (VPC), you can create a compute machine set that deploys compute machines in AWS Outposts.
AWS Outposts is an AWS edge compute service that enables using many features of a cloud-based AWS deployment with the reduced latency of an on-premise environment.
For more information, see the AWS Outposts documentation.

//AWS Outposts on OpenShift Container Platform requirements and limitations
// Module included in the following assemblies:
//
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="aws-outposts-requirements-limitations_{context}"]
= AWS Outposts on OpenShift Container Platform requirements and limitations

You can manage the resources on your AWS Outpost similarly to those on a cloud-based AWS cluster if you configure your OpenShift Container Platform cluster to accommodate the following requirements and limitations:

* To extend an OpenShift Container Platform cluster on AWS into an Outpost, you must have installed the cluster into an existing Amazon Virtual Private Cloud (VPC).

* The infrastructure of an Outpost is tied to an availability zone in an AWS region and uses a dedicated subnet.
Edge compute machines deployed into an Outpost must use the Outpost subnet and the availability zone that the Outpost is tied to.

* When the AWS Kubernetes cloud controller manager discovers an Outpost subnet, it attempts to create service load balancers in the Outpost subnet.
AWS Outposts do not support running service load balancers.
To prevent the cloud controller manager from creating unsupported services in the Outpost subnet, you must include the `kubernetes.io/cluster/unmanaged` tag in the Outpost subnet configuration.
This requirement is a workaround in OpenShift Container Platform version .
For more information, see OCPBUGS-30041.

* OpenShift Container Platform clusters on AWS include the `gp3-csi` and `gp2-csi` storage classes.
These classes correspond to Amazon Elastic Block Store (EBS) gp3 and gp2 volumes.
OpenShift Container Platform clusters use the `gp3-csi` storage class by default, but AWS Outposts does not support EBS gp3 volumes.

* This implementation uses the `node-role.kubernetes.io/outposts` taint to prevent spreading regular cluster workloads to the Outpost nodes.
To schedule user workloads in the Outpost, you must specify a corresponding toleration in the `Deployment` resource for your application.
Reserving the AWS Outpost infrastructure for user workloads avoids additional configuration requirements, such as updating the default CSI to `gp2-csi` so that it is compatible.

* To create a volume in the Outpost, the CSI driver requires the Outpost Amazon Resource Name (ARN).
The driver uses the topology keys stored on the `CSINode` objects to determine the Outpost ARN.
To ensure that the driver uses the correct topology values, you must set the volume binding mode to `WaitForConsumer` and avoid setting allowed topologies on any new storage classes that you create.

* When you extend an AWS VPC cluster into an Outpost, you have two types of compute resources.
The Outpost has edge compute nodes, while the VPC has cloud-based compute nodes.
The cloud-based AWS Elastic Block volume cannot attach to Outpost edge compute nodes, and the Outpost volumes cannot attach to cloud-based compute nodes.
+
As a result, you cannot use CSI snapshots to migrate applications that use persistent storage from cloud-based compute nodes to edge compute nodes or directly use the original persistent volume.
To migrate persistent storage data for applications, you must perform a manual backup and restore operation.

* AWS Outposts does not support AWS Network Load Balancers or AWS Classic Load Balancers.
You must use AWS Application Load Balancers to enable load balancing for edge compute resources in the AWS Outposts environment.
+
To provision an Application Load Balancer, you must use an Ingress resource and install the AWS Load Balancer Operator.
If your cluster contains both edge and cloud-based compute instances that share workloads, additional configuration is required.
+
For more information, see "Using the AWS Load Balancer Operator in an AWS VPC cluster extended into an Outpost".

[role="_additional-resources"]
.Additional resources
* Using the AWS Load Balancer Operator in an AWS VPC cluster extended into an Outpost

[id="aws-outposts-environment-info_{context}"]
== Obtaining information about your environment

To extend an AWS VPC cluster to your Outpost, you must provide information about your OpenShift Container Platform cluster and your Outpost environment.
You use this information to complete network configuration tasks and configure a compute machine set that creates compute machines in your Outpost.
You can use command-line tools to gather the required details.

//Obtaining information from your OpenShift Container Platform cluster
// Module included in the following assemblies:
//
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="aws-outposts-environment-info-oc_{context}"]
= Obtaining information from your OpenShift Container Platform cluster

You can use the {oc-first} to obtain information from your OpenShift Container Platform cluster.

[TIP]
====
You might find it convenient to store some or all of these values as environment variables by using the `export` command.
====

.Prerequisites

* You have installed an OpenShift Container Platform cluster into a custom VPC on AWS.

* You have access to the cluster using an account with `cluster-admin` permissions.

* You have installed the {oc-first}.

.Procedure

. List the infrastructure ID for the cluster by running the following command. Retain this value.
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructures.config.openshift.io cluster
----

. Obtain details about the compute machine sets that the installation program created by running the following commands:

.. List the compute machine sets on your cluster:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io -n openshift-machine-api
----
+
.Example output
[source,text]
----
NAME                           DESIRED   CURRENT   READY   AVAILABLE   AGE
<compute_machine_set_name_1>   1         1         1       1           55m
<compute_machine_set_name_2>   1         1         1       1           55m
----

.. Display the Amazon Machine Image (AMI) ID for one of the listed compute machine sets. Retain this value.
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io <compute_machine_set_name_1> \
  -n openshift-machine-api \
  -o jsonpath='{.spec.template.spec.providerSpec.value.ami.id}'
----

.. Display the subnet ID for the AWS VPC cluster. Retain this value.
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io <compute_machine_set_name_1> \
  -n openshift-machine-api \
  -o jsonpath='{.spec.template.spec.providerSpec.value.subnet.id}'
----

//Obtaining information from your AWS account
// Module included in the following assemblies:
//
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="aws-outposts-environment-info-aws_{context}"]
= Obtaining information from your AWS account

You can use the AWS CLI (`aws`) to obtain information from your AWS account.

[TIP]
====
You might find it convenient to store some or all of these values as environment variables by using the `export` command.
====

.Prerequisites

* You have an AWS Outposts site with the required hardware setup complete.

* Your Outpost is connected to your AWS account.

* You have access to your AWS account by using the AWS CLI (`aws`) as a user with permissions to perform the required tasks.

.Procedure

. List the Outposts that are connected to your AWS account by running the following command:
+
[source,terminal]
----
$ aws outposts list-outposts
----

. Retain the following values from the output of the `aws outposts list-outposts` command:

** The Outpost ID.

** The Amazon Resource Name (ARN) for the Outpost.

** The Outpost availability zone.
+
[NOTE]
====
The output of the `aws outposts list-outposts` command includes two values related to the availability zone: `AvailabilityZone` and `AvailabilityZoneId`. You use the `AvailablilityZone` value to configure a compute machine set that creates compute machines in your Outpost.
====

. Using the value of the Outpost ID, show the instance types that are available in your Outpost by running the following command. Retain the values of the available instance types.
+
[source,terminal]
----
$ aws outposts get-outpost-instance-types \
  --outpost-id <outpost_id_value>
----

. Using the value of the Outpost ARN, show the subnet ID for the Outpost by running the following command. Retain this value.
+
[source,terminal]
----
$ aws ec2 describe-subnets \
  --filters Name=outpost-arn,Values=<outpost_arn_value>
----

[id="aws-outposts-network-config_{context}"]
== Configuring your network for your Outpost

To extend your VPC cluster into an Outpost, you must complete the following network configuration tasks:

* Change the Cluster Network MTU.
* Create a subnet in your Outpost.

//Changing the Cluster Network MTU to support AWS Outposts
// Module included in the following assemblies:
//
// * networking/changing-cluster-network-mtu.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="nw-cluster-mtu-change_{context}"]

= Changing the cluster network MTU

= Changing the cluster network MTU to support AWS Outposts

[role="_abstract"]
You might need to decrease the maximum transmission unit (MTU) value for the cluster network to support an AWS Outposts subnet. During installation, the MTU for the cluster network is detected automatically based on the MTU of the primary network interface of nodes in the cluster.

[IMPORTANT]
====
You cannot roll back an MTU value for nodes during the MTU migration process, but you can roll back the value after the MTU migration process completes.

The migration is disruptive and nodes in your cluster might be temporarily unavailable as the MTU update takes effect.
====

The following procedures describe how to change the cluster network MTU by using machine configs, Dynamic Host Configuration Protocol (DHCP), or an ISO image. If you use either the DHCP or ISO approaches, you must refer to configuration artifacts that you kept after installing your cluster to complete the procedure.

.Prerequisites

* You have installed the {oc-first}.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have identified the target MTU for your cluster. The MTU for the OVN-Kubernetes network plugin must be set to `100` less than the lowest hardware MTU value in your cluster.
* If your nodes are physical machines, ensure that the cluster network and the connected network switches support jumbo frames.
* If your nodes are virtual machines (VMs), ensure that the hypervisor and the connected network switches support jumbo frames.

// Module included in the following assemblies:
//
// * networking/changing-cluster-network-mtu.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="nw-cluster-mtu-checking_{context}"]
= Checking the current cluster MTU value

[role="_abstract"]
To ensure network stability and performance in a hybrid environment where part of your cluster is in the cloud and part is an on-premise environment, you can obtain the current maximum transmission unit (MTU) for the cluster network.

.Procedure

* To obtain the current MTU for the cluster network, enter the following command:
+
[source,terminal]
----
$ oc describe network.config cluster
----
+
.Example output
[source,text]
----
...
Status:
  Cluster Network:
    Cidr:               10.217.0.0/22
    Host Prefix:        23
  Cluster Network MTU:  1400
  Network Type:         OVNKubernetes
  Service Network:
    10.217.4.0/23
...
----

// Module included in the following assemblies:
//
// * networking/changing-cluster-network-mtu.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="nw-cluster-mtu-migration_{context}"]
= Beginning the MTU migration

[role="_abstract"]
Start the maximum transmission unit (MTU) migration by specifying the migration configuration for the cluster network and machine interfaces. The Machine Config Operator performs a rolling reboot of the nodes to prepare the cluster for the MTU change.

.Procedure

. To begin the MTU migration, specify the migration configuration by entering the following command. The Machine Config Operator performs a rolling reboot of the nodes in the cluster in preparation for the MTU change.
+
[source,terminal]
----
$ oc patch Network.operator.openshift.io cluster --type=merge --patch \
  '{"spec": { "migration": { "mtu": { "network": { "from": <overlay_from>, "to": <overlay_to> } , "machine": { "to" : <machine_to> } } } } }'
----
+
--
where:

`<overlay_from>`:: Specifies the current cluster network MTU value.
`<overlay_to>`:: Specifies the target MTU for the cluster network. This value is set relative to the value of `<machine_to>`. For OVN-Kubernetes, this value must be `100` less than the value of `<machine_to>`.
`<machine_to>`:: Specifies the MTU for the primary network interface on the underlying host network.
--
+
[source,terminal]
----
$ oc patch Network.operator.openshift.io cluster --type=merge --patch \
  '{"spec": { "migration": { "mtu": { "network": { "from": 1400, "to": 9000 } , "machine": { "to" : 9100} } } } }'
----
[source,terminal]
----
$ oc patch Network.operator.openshift.io cluster --type=merge --patch \
  '{"spec": { "migration": { "mtu": { "network": { "from": 1400, "to": 1000 } , "machine": { "to" : 1100} } } } }'
----

. As the Machine Config Operator updates machines in each machine config pool, the Operator reboots each node one by one. You must wait until all the nodes are updated. Check the machine config pool status by entering the following command:
+
[source,terminal]
----
$ oc get machineconfigpools
----
+
A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`.
+
[NOTE]
====
By default, the Machine Config Operator updates one machine per pool at a time, causing the total time the migration takes to increase with the size of the cluster.
====

// Module included in the following assemblies:
//
// * networking/changing-cluster-network-mtu.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="nw-cluster-mtu-verifying-configuration_{context}"]
= Verifying the machine configuration

[role="_abstract"]
Verify the machine configuration on your hosts to confirm that the maximum transmission unit (MTU) migration applied successfully. Checking the configuration state and system settings help ensures that the nodes use the correct migration script.

.Procedure

* Confirm the status of the new machine configuration on the hosts:

.. To list the machine configuration state and the name of the applied machine configuration, enter the following command:
+
[source,terminal]
----
$ oc describe node | egrep "hostname|machineconfig"
----
+
.Example output
[source,text]
----
kubernetes.io/hostname=master-0
machineconfiguration.openshift.io/currentConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
machineconfiguration.openshift.io/desiredConfig: rendered-master-c53e221d9d24e1c8bb6ee89dd3d8ad7b
machineconfiguration.openshift.io/reason:
machineconfiguration.openshift.io/state: Done
----

.. Verify that the following statements are true:
+
--
* The value of `machineconfiguration.openshift.io/state` field is `Done`.
* The value of the `machineconfiguration.openshift.io/currentConfig` field is equal to the value of the `machineconfiguration.openshift.io/desiredConfig` field.
--

.. To confirm that the machine config is correct, enter the following command:
+
[source,terminal]
----
$ oc get machineconfig <config_name> -o yaml | grep ExecStart
----
+
--
where:

`<config_name>`:: Specifies the name of the machine config from the `machineconfiguration.openshift.io/currentConfig` field.
--
+
The machine config must include the following update to the systemd configuration:
+
[source,plain]
----
ExecStart=/usr/local/bin/mtu-migration.sh
----

// Module included in the following assemblies:
//
// * networking/changing-cluster-network-mtu.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="nw-cluster-mtu-finalizing-migration_{context}"]
= Finalizing the MTU migration

[role="_abstract"]
Finalize the MTU migration to apply the new maximum transmission unit (MTU) settings to the OVN-Kubernetes network plugin. This updates the cluster configuration and triggers a rolling reboot of the nodes to complete the process.

.Procedure

. To finalize the MTU migration, enter the following command for the OVN-Kubernetes network plugin:
+
[source,terminal]
+
----
$ oc patch Network.operator.openshift.io cluster --type=merge --patch \
  '{"spec": { "migration": null, "defaultNetwork":{ "ovnKubernetesConfig": { "mtu": <mtu> }}}}'
----
+
--
where:

`<mtu>`:: Specifies the new cluster network MTU that you specified with `<overlay_to>`.
--

. After finalizing the MTU migration, each machine config pool node is rebooted one by one. You must wait until all the nodes are updated. Check the machine config pool status by entering the following command:
+
[source,terminal]
----
$ oc get machineconfigpools
----
+
A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`.

.Verification

* Verify that the node in your cluster uses the MTU that you specified by entering the following command:
+
[source,terminal]
----
$ oc describe network.config cluster
----

. To get the current MTU for the cluster network, enter the following command:
+
[source,terminal]
----
$ oc describe network.config cluster
----

. Get the current MTU for the primary network interface of a node:

.. To list the nodes in your cluster, enter the following command:
+
[source,terminal]
----
$ oc get nodes
----

.. To obtain the current MTU setting for the primary network interface on a node, enter the following command:
+
[source,terminal]
----
$ oc adm node-logs <node> -u ovs-configuration | grep configure-ovs.sh | grep mtu | grep <interface> | head -1
----
+
where:
+
--
`<node>`:: Specifies a node from the output from the previous step.
`<interface>`:: Specifies the primary network interface name for the node.
--
+
.Example output
[source,text]
----
ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8051
----

[role="_additional-resources"]
.Additional resources
* Changing the MTU for the cluster network

//Creating subnets for AWS edge compute services
// Module included in the following assemblies:
//
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="installation-creating-aws-vpc-subnets-edge_{context}"]
= Creating subnets for AWS edge compute services

[role="_abstract"]
You can automate creating subnets, route tables, and Carrier Gateways in {aws-short} {zone-type} to extend clusters into ultra-low-latency edge locations for edge workloads. Before you configure a machine set for edge compute nodes in your OpenShift Container Platform cluster, you must create a subnet in {zone-type}.

You can use the provided CloudFormation template and create a CloudFormation stack. You can then use this stack to custom provision a subnet.

[NOTE]
====
If you do not use the provided CloudFormation template to create your AWS infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.
====

.Prerequisites

* You configured an AWS account.
* You added your AWS keys and region to your local AWS profile by running `aws configure`.

.Procedure

. Go to the section of the documentation named "CloudFormation template for the VPC subnet", and copy the syntax from the template. Save the copied template syntax as a YAML file on your local system. This template describes the VPC that your cluster requires.

. Run the following command to deploy the CloudFormation template, which creates a stack of AWS resources that represent the VPC:
+
[source,terminal]
----
$ aws cloudformation create-stack --stack-name <stack_name> \
  --region ${CLUSTER_REGION} \
  --template-body file://<template>.yaml \
  --parameters \
    ParameterKey=VpcId,ParameterValue="${VPC_ID}" \
    ParameterKey=ClusterName,ParameterValue="${CLUSTER_NAME}" \
    ParameterKey=ZoneName,ParameterValue="${ZONE_NAME}" \
    ParameterKey=PublicRouteTableId,ParameterValue="${ROUTE_TABLE_PUB}" \
    ParameterKey=PublicSubnetCidr,ParameterValue="${SUBNET_CIDR_PUB}" \
    ParameterKey=PrivateRouteTableId,ParameterValue="${ROUTE_TABLE_PVT}" \
    ParameterKey=PrivateSubnetCidr,ParameterValue="${SUBNET_CIDR_PVT}" \
    ParameterKey=PrivateSubnetLabel,ParameterValue="private-outpost" \
    ParameterKey=PublicSubnetLabel,ParameterValue="public-outpost" \
    ParameterKey=OutpostArn,ParameterValue="${OUTPOST_ARN}"
----

+
where
+
`<stack_name>`:: Specifies the name for the CloudFormation stack, such as `cluster-wl-<local_zone_shortname>` for Local Zones and `cluster-wl-<wavelength_zone_shortname>` for Wavelength Zones. You need the name of this stack if you remove the cluster.
`<template>`:: Specifies the relative path and the name of the CloudFormation template YAML file that you saved.
`${VPC_ID}`:: Specifies the VPC ID, which is the value `VpcID` in the output of the CloudFormation template for the VPC.
`${CLUSTER_NAME}`:: Specifies the value of *ClusterName* to be used as a prefix of the new AWS resource names.
`${ZONE_NAME}`:: Specifies the value of {zone-type} name to create the subnets.
`${ROUTE_TABLE_PUB}`:: Specifies the Public Route Table Id extracted from the CloudFormation template. For Local Zones, the public route table is extracted from the VPC CloudFormation Stack. For Wavelength Zones, the value must be extracted from the output of the VPC's carrier gateway CloudFormation stack.
`${SUBNET_CIDR_PUB}`:: Specifies a valid CIDR block that is used to create the public subnet. This block must be part of the VPC CIDR block `VpcCidr`.
`${ROUTE_TABLE_PVT}`:: Specifies the *PrivateRouteTableId* extracted from the output of the VPC's CloudFormation stack.
`${SUBNET_CIDR_PVT}`:: Specifies a valid CIDR block that is used to create the private subnet. This block must be part of the VPC CIDR block `VpcCidr`.
+
.Example output
[source,text]
----
arn:aws:cloudformation:us-east-1:123456789012:stack/<stack_name>/dbedae40-820e-11eb-2fd3-12a48460849f
----

+
where
+
`<stack_name>`:: Specifies the name for the CloudFormation stack, such as `cluster-<outpost_name>`.
`<template>`:: Specifies the relative path and the name of the CloudFormation template YAML file that you saved.
`${VPC_ID}`:: Specifies the VPC ID, which is the value `VpcID` in the output of the CloudFormation template for the VPC.
`${CLUSTER_NAME}`:: Specifies the value of *ClusterName* to be used as a prefix of the new AWS resource names.
`${ZONE_NAME}`:: Specifies the value of {zone-type} name to create the subnets.
`${ROUTE_TABLE_PUB}`:: Specifies the Public Route Table ID created in the `${VPC_ID}` used to associate the public subnets on Outposts. Specify the public route table to associate the Outpost subnet created by this stack.
`${SUBNET_CIDR_PUB}`:: Specifies a valid CIDR block that is used to create the public subnet. This block must be part of the VPC CIDR block `VpcCidr`.
`${OUTPOST_ARN}`:: Specifies the Amazon Resource Name (ARN) for the Outpost.
`${SUBNET_CIDR_PVT}`:: Specifies a valid CIDR block that is used to create the private subnet. This block must be part of the VPC CIDR block `VpcCidr`.
`${ROUTE_TABLE_PVT}`:: Specifies the Private Route Table ID created in the `${VPC_ID}` used to associate the private subnets on Outposts. Specify the private route table to associate the Outpost subnet created by this stack.
+
.Example output
[source,text]
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
After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values for the following parameters:
+
--
[horizontal]
`PublicSubnetId`:: The IDs of the public subnet created by the CloudFormation stack.
`PrivateSubnetId`:: The IDs of the private subnet created by the CloudFormation stack.
--
+
Ensure that you provide these parameter values to the other CloudFormation templates that you run to create for your cluster.

//CloudFormation template for the VPC Subnet
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

//Creating a compute machine set that deploys edge compute machines an Outpost
// Module included in the following assemblies:
//
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="aws-outposts-machine-set_{context}"]
= Creating a compute machine set that deploys edge compute machines on an Outpost

To create edge compute machines on AWS Outposts, you must create a new compute machine set with a compatible configuration.

.Prerequisites

* You have an AWS Outposts site.

* You have installed an OpenShift Container Platform cluster into a custom VPC on AWS.

* You have access to the cluster using an account with `cluster-admin` permissions.

* You have installed the {oc-first}.

.Procedure

. List the compute machine sets in your cluster by running the following command:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io -n openshift-machine-api
----
+
.Example output
[source,text]
----
NAME                            DESIRED   CURRENT   READY   AVAILABLE   AGE
<original_machine_set_name_1>   1         1         1       1           55m
<original_machine_set_name_2>   1         1         1       1           55m
----

. Record the names of the existing compute machine sets.

. Create a YAML file that contains the values for a new compute machine set custom resource (CR) by using one of the following methods:

** Copy an existing compute machine set configuration into a new file by running the following command:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io <original_machine_set_name_1> \
  -n openshift-machine-api -o yaml > <new_machine_set_name_1>.yaml
----
+
You can edit this YAML file with your preferred text editor.

** Create an empty YAML file named `<new_machine_set_name_1>.yaml` with your preferred text editor and include the required values for your new compute machine set.
+
If you are not sure which value to set for a specific field, you can view values of an existing compute machine set CR by running the following command:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io <original_machine_set_name_1> \
  -n openshift-machine-api -o yaml
----
+
--
.Example output
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id> # <1>
  name: <infrastructure_id>-<role>-<availability_zone> # <2>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<availability_zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<availability_zone>
    spec:
      providerSpec: # <3>
# ...
----
<1> The cluster infrastructure ID.
<2> A default node label. For AWS Outposts, you use the `outposts` role.
<3> The omitted `providerSpec` section includes values that must be configured for your Outpost.
--

. Configure the new compute machine set to create edge compute machines in the Outpost by editing the `<new_machine_set_name_1>.yaml` file:
+
--
.Example compute machine set for AWS Outposts
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id> # <1>
  name: <infrastructure_id>-outposts-<availability_zone> # <2>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-outposts-<availability_zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: outposts
        machine.openshift.io/cluster-api-machine-type: outposts
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-outposts-<availability_zone>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/outposts: ""
          location: outposts
      providerSpec:
        value:
          ami:
            id: <ami_id> # <3>
          apiVersion: machine.openshift.io/v1beta1
          blockDevices:
            - ebs:
                volumeSize: 120
                volumeType: gp2 # <4>
          credentialsSecret:
            name: aws-cloud-credentials
          deviceIndex: 0
          iamInstanceProfile:
            id: <infrastructure_id>-worker-profile
          instanceType: m5.xlarge # <5>
          kind: AWSMachineProviderConfig
          placement:
            availabilityZone: <availability_zone>
            region: <region> # <6>
          securityGroups:
            - filters:
              - name: tag:Name
                values:
                  - <infrastructure_id>-worker-sg
          subnet:
            id: <subnet_id> # <7>
          tags:
            - name: kubernetes.io/cluster/<infrastructure_id>
              value: owned
          userDataSecret:
            name: worker-user-data
      taints: # <8>
        - key: node-role.kubernetes.io/outposts
          effect: NoSchedule
----
<1> Specifies the cluster infrastructure ID.
<2> Specifies the name of the compute machine set. The name is composed of the cluster infrastructure ID, the `outposts` role name, and the Outpost availability zone.
<3> Specifies the Amazon Machine Image (AMI) ID.
<4> Specifies the EBS volume type. AWS Outposts requires gp2 volumes.
<5> Specifies the AWS instance type. You must use an instance type that is configured in your Outpost.
<6> Specifies the AWS region in which the Outpost availability zone exists.
<7> Specifies the dedicated subnet for your Outpost.
<8> Specifies a taint to prevent workloads from being scheduled on nodes that have the `node-role.kubernetes.io/outposts` label. To schedule user workloads in the Outpost, you must specify a corresponding toleration in the `Deployment` resource for your application.
--

. Save your changes.

. Create a compute machine set CR by running the following command:
+
[source,terminal]
----
$ oc create -f <new_machine_set_name_1>.yaml
----

.Verification

* To verify that the compute machine set is created, list the compute machine sets in your cluster by running the following command:
+
[source,terminal]
----
$ oc get machinesets.machine.openshift.io -n openshift-machine-api
----
+
.Example output
[source,text]
----
NAME                            DESIRED   CURRENT   READY   AVAILABLE   AGE
<new_machine_set_name_1>        1         1         1       1           4m12s
<original_machine_set_name_1>   1         1         1       1           55m
<original_machine_set_name_2>   1         1         1       1           55m
----

* To list the machines that are managed by the new compute machine set, run the following command:
+
[source,terminal]
----
$ oc get -n openshift-machine-api machines.machine.openshift.io \
  -l machine.openshift.io/cluster-api-machineset=<new_machine_set_name_1>
----
+
.Example output
[source,text]
----
NAME                             PHASE          TYPE        REGION      ZONE         AGE
<machine_from_new_1>             Provisioned    m5.xlarge   us-east-1   us-east-1a   25s
<machine_from_new_2>             Provisioning   m5.xlarge   us-east-1   us-east-1a   25s
----

* To verify that a machine created by the new compute machine set has the correct configuration, examine the relevant fields in the CR for one of the new machines by running the following command:
+
[source,terminal]
----
$ oc describe machine <machine_from_new_1> -n openshift-machine-api
----

//Creating user workloads in an Outpost
// Module included in the following assemblies:
//
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

//To-do: reintegrate installation-extend-edge-nodes-aws-local-zones.adoc with create-user-workloads-aws-edge.adoc. Requires global repo update of any xrefs/includes.

[id="create-user-workloads-aws-edge_{context}"]
= Creating user workloads in an Outpost

After you extend an OpenShift Container Platform in an AWS VPC cluster into an Outpost, you can use edge compute nodes with the label `node-role.kubernetes.io/outposts` to create user workloads in the Outpost.

.Prerequisites

* You have extended an AWS VPC cluster into an Outpost.

* You have access to the cluster using an account with `cluster-admin` permissions.

* You have installed the {oc-first}.

* You have created a compute machine set that deploys edge compute machines compatible with the Outpost environment.

.Procedure

. Configure a `Deployment` resource file for an application that you want to deploy to the edge compute node in the edge subnet.
+
.Example `Deployment` manifest
[source,yaml]
----
kind: Namespace
apiVersion: v1
metadata:
  name: <application_name> # <1>
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: <application_name>
  namespace: <application_namespace> # <2>
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: gp2-csi # <3>
  volumeMode: Filesystem
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: <application_name>
  namespace: <application_namespace>
spec:
  selector:
    matchLabels:
      app: <application_name>
  replicas: 1
  template:
    metadata:
      labels:
        app: <application_name>
        location: outposts # <4>
    spec:
      securityContext:
        seccompProfile:
          type: RuntimeDefault
      nodeSelector: # <5>
        node-role.kubernetes.io/outpost: ''
      tolerations: # <6>
      - key: "node-role.kubernetes.io/outposts"
        operator: "Equal"
        value: ""
        effect: "NoSchedule"
      containers:
        - image: openshift/origin-node
          command:
           - "/bin/socat"
          args:
            - TCP4-LISTEN:8080,reuseaddr,fork
            - EXEC:'/bin/bash -c \"printf \\\"HTTP/1.0 200 OK\r\n\r\n\\\"; sed -e \\\"/^\r/q\\\"\"'
          imagePullPolicy: Always
          name: <application_name>
          ports:
            - containerPort: 8080
          volumeMounts:
            - mountPath: "/mnt/storage"
              name: data
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: <application_name>
----
<1> Specify a name for your application.
<2> Specify a namespace for your application. The application namespace can be the same as the application name.
<3> Specify the storage class name. For an edge compute configuration, you must use the `gp2-csi` storage class.
<4> Specify a label to identify workloads deployed in the Outpost.
<5> Specify the node selector label that targets edge compute nodes.
<6> Specify tolerations that match the `key` and `effects` taints in the compute machine set for your edge compute machines. Set the `value` and `operator` tolerations as shown.

. Create the `Deployment` resource by running the following command:
+
[source,terminal]
----
$ oc create -f <application_deployment>.yaml
----

. Configure a `Service` object that exposes a pod from a targeted edge compute node to services that run inside your edge network.
+
.Example `Service` manifest
[source,yaml]
----
apiVersion: v1
kind: Service # <1>
metadata:
  name:  <application_name>
  namespace: <application_namespace>
spec:
  ports:
    - port: 80
      targetPort: 8080
      protocol: TCP
  type: NodePort
  selector: # <2>
    app: <application_name>
----
<1> Defines the `service` resource.
<2> Specify the label type to apply to managed pods.

. Create the `Service` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <application_service>.yaml
----

//To-do: reintegrate installation-extend-edge-nodes-aws-local-zones.adoc with create-user-workloads-aws-edge.adoc. Requires global repo update of any xrefs/includes.

[id="aws-outposts-network-scheduling-workloads_{context}"]
== Scheduling workloads on edge and cloud-based AWS compute resources

When you extend an AWS VPC cluster into an Outpost, the Outpost uses edge compute nodes and the VPC uses cloud-based compute nodes.
The following load balancer considerations apply to an AWS VPC cluster extended into an Outpost:

* Outposts cannot run AWS Network Load Balancers or AWS Classic Load Balancers, but a Classic Load Balancer for a VPC cluster extended into an Outpost can attach to the Outpost edge compute nodes.
For more information, see Using AWS Classic Load Balancers in an AWS VPC cluster extended into an Outpost.

* To run a load balancer on an Outpost instance, you must use an AWS Application Load Balancer.
You can use the AWS Load Balancer Operator to deploy an instance of the AWS Load Balancer Controller.
The controller provisions AWS Application Load Balancers for Kubernetes Ingress resources.
For more information, see Using the AWS Load Balancer Operator in an AWS VPC cluster extended into an Outpost.

//Using Classic Load Balancers in an AWS VPC cluster extended into an Outpost
// Module included in the following assemblies:
//
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="aws-outposts-load-balancer-clb_{context}"]
= Using AWS Classic Load Balancers in an AWS VPC cluster extended into an Outpost

AWS Outposts infrastructure cannot run AWS Classic Load Balancers, but Classic Load Balancers in the AWS VPC cluster can target edge compute nodes in the Outpost if edge and cloud-based subnets are in the same availability zone.
As a result, Classic Load Balancers on the VPC cluster might schedule pods on either of these node types.

Scheduling the workloads on edge compute nodes and cloud-based compute nodes can introduce latency.
If you want to prevent a Classic Load Balancer in the VPC cluster from targeting Outpost edge compute nodes, you can apply labels to the cloud-based compute nodes and configure the Classic Load Balancer to only schedule on nodes with the applied labels.

[NOTE]
====
If you do not need to prevent a Classic Load Balancer in the VPC cluster from targeting Outpost edge compute nodes, you do not need to complete these steps.
====

.Prerequisites

* You have extended an AWS VPC cluster into an Outpost.

* You have access to the cluster using an account with `cluster-admin` permissions.

* You have installed the {oc-first}.

* You have created a user workload in the Outpost with tolerations that match the taints for your edge compute machines.

.Procedure

. Optional: Verify that the edge compute nodes have the `location=outposts` label by running the following command and verifying that the output includes only the edge compute nodes in your Outpost:
+
[source,terminal]
----
$ oc get nodes -l location=outposts
----

. Label the cloud-based compute nodes in the VPC cluster with a key-value pair by running the following command:
+
[source,terminal]
----
$ for NODE in $(oc get node -l node-role.kubernetes.io/worker --no-headers | grep -v outposts | awk '{print$1}'); do oc label node $NODE <key_name>=<value>; done
----
+
where `<key_name>=<value>` is the label you want to use to distinguish cloud-based compute nodes.
+
.Example output
[source,text]
----
node1.example.com labeled
node2.example.com labeled
node3.example.com labeled
----

. Optional: Verify that the cloud-based compute nodes have the specified label by running the following command and confirming that the output includes all cloud-based compute nodes in your VPC cluster:
+
[source,terminal]
----
$ oc get nodes -l <key_name>=<value>
----
+
.Example output
[source,terminal]
----
NAME                   STATUS    ROLES     AGE       VERSION
node1.example.com      Ready     worker    7h        v1.35.4
node2.example.com      Ready     worker    7h        v1.35.4
node3.example.com      Ready     worker    7h        v1.35.4
----

. Configure the Classic Load Balancer service by adding the cloud-based subnet information to the `annotations` field of the `Service` manifest:
+
.Example service configuration
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  labels:
    app: <application_name>
  name: <application_name>
  namespace: <application_namespace>
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-subnets: <aws_subnet> # <1>
    service.beta.kubernetes.io/aws-load-balancer-target-node-labels: <key_name>=<value> # <2>
spec:
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 8080
  selector:
    app: <application_name>
  type: LoadBalancer
----
<1> Specify the subnet ID for the AWS VPC cluster.
<2> Specify the key-value pair that matches the pair in the node label.

. Create the `Service` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

.Verification

. Verify the status of the `service` resource to show the host of the provisioned Classic Load Balancer by running the following command:
+
[source,terminal]
----
$ HOST=$(oc get service <application_name> -n <application_namespace> --template='{{(index .status.loadBalancer.ingress 0).hostname}}')
----

. Verify the status of the provisioned Classic Load Balancer host by running the following command:
+
[source,terminal]
----
$ curl $HOST
----

. In the AWS console, verify that only the labeled instances appear as the targeted instances for the load balancer.

//Using the AWS Load Balancer Operator in an AWS VPC cluster extended into an Outpost
// Module included in the following assemblies:
//
// * networking/aws_load_balancer_operator/understanding-aws-load-balancer-operator.adoc
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="nw-aws-load-balancer-with-outposts_{context}"]
= Using the AWS Load Balancer Operator in an AWS VPC cluster extended into an Outpost

[role="_abstract"]
You can configure the AWS Load Balancer Operator to provision an {aws-short} Application Load Balancer in an {aws-short} VPC cluster extended into an Outpost. {aws-short} Outposts does not support {aws-short} Network Load Balancers. As a result, the {aws-short} Load Balancer Operator cannot provision Network Load Balancers in an Outpost.

You can create an {aws-short} Application Load Balancer either in the cloud subnet or in the Outpost subnet.

An Application Load Balancer in the cloud can attach to cloud-based compute nodes. An Application Load Balancer in the Outpost can attach to edge compute nodes.

You must annotate Ingress resources with the Outpost subnet or the VPC subnet, but not both.

.Prerequisites

* You have extended an {aws-short} VPC cluster into an Outpost.
* You have installed the {oc-first}.
* You have installed the {aws-short} Load Balancer Operator and created the {aws-short} Load Balancer Controller.

.Procedure

* Configure the `Ingress` resource to use a specified subnet:
+
.Example `Ingress` resource configuration
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <application_name>
  annotations:
    alb.ingress.kubernetes.io/subnets: <subnet_id>
spec:
  ingressClassName: alb
  rules:
    - http:
        paths:
          - path: /
            pathType: Exact
            backend:
              service:
                name: <application_name>
                port:
                  number: 80
----
+
where:
+
`<subnet_id>`:: Specifies the subnet to use. To use the Application Load Balancer in an Outpost, specify the Outpost subnet ID. To use the Application Load Balancer in the cloud, you must specify at least two subnets in different availability zones.

[role="_additional-resources"]
.Additional resources
* Creating the AWS Load Balancer Controller

[role="_additional-resources"]
[id="additional-installing-aws-outposts"]
== Additional resources
* Installing a cluster on AWS into an existing VPC
