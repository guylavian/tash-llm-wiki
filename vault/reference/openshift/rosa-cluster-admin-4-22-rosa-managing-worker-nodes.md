---
title: "Managing compute nodes"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-managing-worker-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-managing-worker-nodes
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Managing compute nodes

[id="rosa-managing-worker-nodes"]
= Managing compute nodes

[role="_abstract"]
With OpenShift Container Platform, you can manage compute (also known as worker) nodes to create and configure optimal compute capacity for your workloads.

The majority of changes for compute nodes are configured on machine pools. A machine pool is a group of compute nodes in a cluster that have the same configuration, providing ease of management.

You can edit machine pool configuration options such as scaling, adding node labels, and adding taints.

You can also create new machine pools with Capacity Reservations.

.Overview of AWS Capacity Reservations

If you have reserved compute capacity using AWS Capacity Reservations for a specific instance type and Availability Zone (AZ), you can use it for your OpenShift Container Platform worker nodes. Both On-Demand Capacity Reservations and Capacity Blocks for machine learning (ML) workloads are supported.

Purchase and manage a Capacity Reservation directly with AWS. After reserving the capacity, add a Capacity Reservation ID to a new machine pool when you create it in your OpenShift Container Platform cluster. You can also use a Capacity Reservation shared with you from another AWS account within your AWS Organization.

Once you configure Capacity Reservations in OpenShift Container Platform, you can use your AWS account to monitor reserved capacity usage across all workloads in the account.

Using Capacity Reservations on machine pools in OpenShift Container Platform clusters has the following prerequisites and limitations:

* You installed and configured the latest {rosa-cli}.
* Your OpenShift Container Platform cluster is version 4.19 or later.
* The cluster already has a machine pool that is not using a Capacity Reservation or taints. The machine pool must have at least 2 worker nodes.
* You have purchased a Capacity Reservation for the instance type required in the AZ of the machine pool that you are creating.
* You can only add a Capacity Reservation ID to a new machine pool.
* You cannot use autoscaling with Capacity Reservations if you create a machine pool using the {rosa-cli}. However, you can enable both autoscaling and Capacity Reservations on machine pools created using {cluster-manager}.

You can create a machine pool with a Capacity Reservation using either {cluster-manager} or the {rosa-cli}.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="creating_a_machine_pool_{context}"]
= Creating a machine pool

A machine pool is created when you install a OpenShift Container Platform cluster. After installation, you can create additional machine pools for your cluster by using {cluster-manager} or the {rosa-cli-first}.
[NOTE]
====
For users of `rosa` version 1.2.25 and earlier versions, the machine pool created along with the cluster is identified as `Default`. For users of `rosa` version 1.2.26 and later, the machine pool created along with the cluster is identified as `worker`.
====
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

[id="creating_machine_pools_ocm_{context}"]
= Creating a machine pool

= Creating a machine pool using OpenShift Cluster Manager

[role="_abstract"]
A machine pool is created when you install an OpenShift Container Platform cluster. After installation, you can create additional machine pools for your cluster by using {cluster-manager}.
You can create additional machine pools for your OpenShift Container Platform cluster by using {cluster-manager}.

[IMPORTANT]
====
The compute, also known as worker, node instance types, autoscaling options, and node counts that are available depend on your
OpenShift Container Platform
OpenShift Container Platform
subscriptions, resource quotas and deployment scenario. For more information, contact your sales representative or Red{nbsp}Hat support.
====

.Prerequisites

* You created a OpenShift Container Platform cluster.
* You created an OpenShift Container Platform cluster.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.

. Under the *Machine pools* tab, click *Add machine pool*.

. Add a *Machine pool name*.

. Select a *Compute node instance type* from the list. The instance type defines the vCPU and memory allocation for each compute node in the machine pool.
+
[NOTE]
====
You cannot change the instance type for a machine pool after the pool is created.
====

. Optional: If you are using {VirtProductName} on a OpenShift Container Platform cluster, you might want to run Windows VMs. In order to be license-compliant with Microsoft Windows in AWS, the hosts (x86-64 bare metal EC2 instances) running these VMs must be enabled with AWS EC2 Windows License Included. To enable the machine pool for AWS Windows License Included, select the *Enable machine pool for AWS Windows License Included* checkbox.
+
You can only select this option when the host cluster is a OpenShift Container Platform cluster version 4.19 and later and the instance type is x86-64 bare metal EC2.
+
[IMPORTANT]
====
Enabling AWS Windows LI on a machine pool applies the associated licensing fees on that specific machine pool. This includes billing for the full vCPU allocation of each AWS Windows LI enabled host in your OpenShift Container Platform cluster. Windows LI enabled machine pools will also deny vCPU over-allocation on {VirtProductName} VMs. For more information, see Microsoft Licensing on AWS and the OpenShift Container Platform instance types.
====

. Configure the node count by choosing one of the following options:
+
** *Enable autoscaling*: Select *Enable autoscaling* to automatically scale the number of machines in your machine pool to meet the deployment needs. Set the minimum and maximum node count limits for autoscaling. The cluster autoscaler does not reduce or increase the machine pool node count beyond the limits that you specify.
+
[NOTE]
====
The *Enable autoscaling* option is only available for OpenShift Container Platform if you have the `capability.cluster.autoscale_clusters` subscription. For more information, contact your sales representative or Red{nbsp}Hat support.
====
+
*** If you deployed your cluster using a single availability zone, set the *Minimum and maximum node count*. This defines the minimum and maximum compute node limits in the availability zone.
*** If you deployed your cluster using multiple availability zones, set the *Minimum nodes per zone* and *Maximum nodes per zone*. This defines the minimum and maximum compute node limits per zone.
** *Manual node count*: If you do not enable autoscaling, select a compute node count:
*** If you deployed your cluster using a single availability zone, select a *Compute node count* from the drop-down menu. This defines the number of compute nodes to provision to the machine pool for the zone.
*** If you deployed your cluster using multiple availability zones, select a *Compute node count (per zone)* from the drop-down menu. This defines the number of compute nodes to provision to the machine pool per zone.
** *Manual node count*: If you do not enable autoscaling, select a *Compute node count* from the drop-down menu. This defines the number of compute nodes to provision to the machine pool for the availability zone.

. Optional: Configure advanced machine pool settings by expanding the appropriate sections and providing values:
** *Root disk size*: Specify a custom root disk size.
** *Reserved capacity*: Add reserved capacity to your machine pool:
*** Select a *Reservation Preference* from the list. Valid preferences include:
**** *None*: The instance does not use a Capacity Reservation even if one is available. The instance runs as an EC2 On-Demand instance. Choose this option when you want to avoid consuming purchased reserved capacity and use it for other workloads.
**** *Open*: The instance can run in any `open` Capacity Reservation that has matching attributes such as the instance type, platform, AZ, or tenancy. Choose this option for flexibility; if a reservation is not available, the instance can use regular unreserved EC2 capacity.
**** *CR only* (capacity reservation only): The instance can only run in a Capacity Reservation. If capacity is not available, the instance fails to launch.
*** Add a *Reservation ID*. You get an ID in the `cr-<capacity_reservation_id>` format when you purchase a Capacity Reservation from AWS. The ID can be for both On-Demand Capacity Reservations or Capacity Blocks for ML.
.. For *Node labels and taints*, expand the *Edit node labels and taints* menu.
.. Under *Node labels*, add *Key* and *Value* entries for your node labels.
.. Under *Taints*, add *Key* and *Value* entries for your taints. For each taint, select an *Effect* from the drop-down menu. Available options include `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.
+
[NOTE]
====
Creating a machine pool with taints is only possible if the cluster already has at least one machine pool without a taint. Alternatively, you can add node labels and taints after you create the machine pool.
====
** *Custom security groups*: Select additional custom security groups to use for nodes in this machine pool. You must have already created the security groups and associated them with the VPC that you selected for this cluster. You cannot add or edit security groups after you create the machine pool.
For more information, see the requirements for security groups in the "Additional resources" section.
+
[IMPORTANT]
====
You can use up to ten additional security groups for machine pools on OpenShift Container Platform clusters.
====
** *Amazon EC2 Spot Instances*: If you deployed OpenShift Container Platform on AWS using the Customer Cloud Subscription (CCS) model and want to configure your machine pool to deploy machines as non-guaranteed AWS Spot Instances, select *Use Amazon EC2 Spot Instances*. Leave *Use On-Demand instance price* selected to use the on-demand instance price, or select *Set maximum price* to define a maximum hourly price for a Spot Instance. For more information about Amazon EC2 Spot Instances, see the AWS documentation.
** *Amazon EC2 Spot Instances*: To configure your machine pool to deploy machines as non-guaranteed AWS Spot Instances, select *Use Amazon EC2 Spot Instances*. Leave *Use On-Demand instance price* selected to use the on-demand instance price, or select *Set maximum price* to define a maximum hourly price for a Spot Instance. For more information about Amazon EC2 Spot Instances, see the AWS documentation.
+
[IMPORTANT]
====
Your Amazon EC2 Spot Instances might be interrupted at any time. Use Amazon EC2 Spot Instances only for workloads that can tolerate interruptions.
====
+
[NOTE]
====
If you select *Use Amazon EC2 Spot Instances* for a machine pool, you cannot disable the option after the machine pool is created.
====
** *Shielded VMs* ({GCP} only): By default, OpenShift Container Platform on {GCP} instances in the machine pools inherit the Shielded VM settings at the cluster level. You can override the cluster level Shielded VM settings at the machine pool level by selecting or clearing the *Enable Secure Boot support for Shielded VMs* checkbox.
+
[IMPORTANT]
====
Once a machine pool is created, the *Enable Secure Boot support for Shielded VMs* setting cannot be changed. This setting is not supported for OpenShift Container Platform on {GCP} clusters created using bare-metal instance types. For more information, see Limitations in the {GCP} documentation.
====

. Click *Add machine pool* to create the machine pool.

.Verification

* Verify that the machine pool is visible on the *Machine pools* page and the configuration is as expected.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="creating_machine_pools_cli_{context}"]
= Creating a machine pool using the {rosa-cli}

[role="_abstract"]
You can create additional machine pools for your OpenShift Container Platform cluster by using the {rosa-cli-first}.

[NOTE]
====
To add a pre-purchased Capacity Reservation to a machine pool, see Creating a machine pool with Capacity Reservations.
====

.Prerequisites

* You installed and configured the latest {rosa-cli} on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.

.Procedure

* To add a machine pool that does not use autoscaling, create the machine pool and define the instance type, compute (also known as worker) node count, and node labels:
+
--
[source,terminal]
----
$ rosa create machinepool --cluster=<cluster-name> \
                          --name=<machine_pool_id> \
                          --replicas=<replica_count> \
                          --instance-type=<instance_type> \
                          --labels=<key>=<value>,<key>=<value> \
                          --taints=<key>=<value>:<effect>,<key>=<value>:<effect> \
                          --use-spot-instances \
                          --spot-max-price=<price> \
                          --disk-size=<disk_size> \
                          --availability-zone=<availability_zone_name> \
                          --additional-security-group-ids <sec_group_id> \
                          --subnet <subnet_id>
----

where:

`--name=<machine_pool_id>`:: Specifies the name of the machine pool.
`--replicas=<replica_count>`:: Specifies the number of compute nodes to provision. If you deployed OpenShift Container Platform using a single availability zone, this defines the number of compute nodes to provision to the machine pool for the zone. If you deployed your cluster using multiple availability zones, this defines the number of compute nodes to provision in total across all zones and the count must be a multiple of 3. The `--replicas` argument is required when autoscaling is not configured.
`--instance-type=<instance_type>`:: Optional: Sets the instance type for the compute nodes in your machine pool. The instance type defines the vCPU and memory allocation for each compute node in the pool. Replace `<instance_type>` with an instance type. The default is `m7i.xlarge`. You cannot change the instance type for a machine pool after the pool is created.
`--labels=<key>=<value>,<key>=<value>`:: Optional: Defines the labels for the machine pool. Replace `<key>=<value>,<key>=<value>` with a comma-delimited list of key-value pairs, for example `--labels=key1=value1,key2=value2`.
`--taints=<key>=<value>:<effect>,<key>=<value>:<effect>`:: Optional: Defines the taints for the machine pool. Replace `<key>=<value>:<effect>,<key>=<value>:<effect>` with a key, value, and effect for each taint, for example `--taints=key1=value1:NoSchedule,key2=value2:NoExecute`. Available effects include `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.
`--use-spot-instances`:: Optional: Configures your machine pool to deploy machines as non-guaranteed AWS Spot Instances. For information, see Amazon EC2 Spot Instances in the AWS documentation. If you select *Use Amazon EC2 Spot Instances* for a machine pool, you cannot disable the option after the machine pool is created.
`--spot-max-price=<price>`:: Optional: If you choose to use Spot Instances, you can specify this argument to define a maximum hourly price for a Spot Instance. If this argument is not specified, the on-demand price is used.
+
[IMPORTANT]
====
Your Amazon EC2 Spot Instances might be interrupted at any time. Use Amazon EC2 Spot Instances only for workloads that can tolerate interruptions.
====
`--disk-size=<disk_size>`:: Optional: Specifies the worker node disk size. The value can be in GB, GiB, TB, or TiB. Replace `<disk_size>` with a numeric value and unit, for example `--disk-size=200GiB`.
`--availability-zone=<availability_zone_name>`::
Optional: You can create a machine pool in an availability zone of your choice. Replace `<availability_zone_name>` with an availability zone name.
Optional: For Multi-AZ clusters, you can create a machine pool in a Single-AZ of your choice. Replace `<availability_zone_name>` with a Single-AZ name.
+
[NOTE]
====
Multi-AZ clusters retain a Multi-AZ control plane and can have worker machine pools across a Single-AZ or Multi-AZ. Machine pools distribute machines (nodes) evenly across availability zones.
====
+
[WARNING]
====
If you choose a worker machine pool with a Single-AZ, there is no fault tolerance for that machine pool, regardless of machine replica count.
For fault-tolerant worker machine pools, choosing a Multi-AZ machine pool distributes machines in multiples of 3 across availability zones.

* A Multi-AZ machine pool with three availability zones can have a machine count in multiples of 3 only, such as 3, 6, 9, and so on.
* A Single-AZ machine pool with one availability zone can have a machine count in multiples of 1, such as 1, 2, 3, 4, and so on.
====
`--additional-security-group-ids <sec_group_id>`:: Optional: For machine pools in clusters that do not have Red{nbsp}Hat managed VPCs, you can select additional custom security groups to use in your machine pools. You must have already created the security groups and associated them with the VPC that you selected for this cluster. You cannot add or edit security groups after you create the machine pool.
For more information, see the requirements for security groups in the "Additional resources" section.
+
[IMPORTANT]
====
You can use up to ten additional security groups for machine pools on OpenShift Container Platform clusters.
====
`--subnet <subnet_id>`:: Optional: For BYO VPC clusters, you can select a subnet to create a Single-AZ machine pool. If the subnet is out of your cluster creation subnets, there must be a tag with a key `kubernetes.io/cluster/<infra-id>` and value `shared`. Customers can obtain the Infra ID by using the following command:
+
[source,terminal]
----
$ rosa describe cluster -c <cluster name>|grep "Infra ID:"
----
+
.Example output
[source,terminal]
----
Infra ID:                   mycluster-xqvj7
----
+
[NOTE]
====
You cannot set both `--subnet` and `--availability-zone` at the same time, only 1 is allowed for a Single-AZ machine pool creation.
====
--
+
The following example creates a machine pool called `mymachinepool` that uses the `m7i.xlarge` instance type and has 2 compute node replicas. The example also adds 2 workload-specific labels:
+
[source,terminal]
----
$ rosa create machinepool --cluster=mycluster --name=mymachinepool --replicas=2 --instance-type=m7i.xlarge --labels=app=db,tier=backend
----
+
.Example output
[source,terminal]
----
I: Machine pool 'mymachinepool' created successfully on cluster 'mycluster'
I: To view all machine pools, run 'rosa list machinepools -c mycluster'
----

* To add a machine pool that uses autoscaling, create the machine pool and define the autoscaling configuration, instance type and node labels:
+
--
[source,terminal]
----
$ rosa create machinepool --cluster=<cluster-name> \
                          --name=<machine_pool_id> \
                          --enable-autoscaling \
                          --min-replicas=<minimum_replica_count> \
                          --max-replicas=<maximum_replica_count> \
                          --instance-type=<instance_type> \
                          --labels=<key>=<value>,<key>=<value> \
                          --taints=<key>=<value>:<effect>,<key>=<value>:<effect> \
                          --availability-zone=<availability_zone_name>
                          --availability-zone=<availability_zone_name> \
                          --use-spot-instances \
                          --spot-max-price=<price>
----

where:

`--name=<machine_pool_id>`:: Specifies the name of the machine pool. Replace `<machine_pool_id>` with the name of your machine pool.
`--enable-autoscaling`:: Enables autoscaling in the machine pool to meet the deployment needs.
`--min-replicas=<minimum_replica_count>` and `--max-replicas=<maximum_replica_count>`:: Defines the minimum and maximum compute node limits. The cluster autoscaler does not reduce or increase the machine pool node count beyond the limits that you specify.
+
If you deployed OpenShift Container Platform using a single availability zone, the `--min-replicas` and `--max-replicas` arguments define the autoscaling limits in the machine pool for the zone. If you deployed your cluster using multiple availability zones, the arguments define the autoscaling limits in total across all zones and the counts must be multiples of 3.
+
The `--min-replicas` and `--max-replicas` arguments define the autoscaling limits in the machine pool for the availability zone.
`--instance-type=<instance_type>`:: Optional: Sets the instance type for the compute nodes in your machine pool. The instance type defines the vCPU and memory allocation for each compute node in the pool. Replace `<instance_type>` with an instance type. The default is `m7i.xlarge`. You cannot change the instance type for a machine pool after the pool is created.
`--labels=<key>=<value>,<key>=<value>`:: Optional: Defines the labels for the machine pool. Replace `<key>=<value>,<key>=<value>` with a comma-delimited list of key-value pairs, for example `--labels=key1=value1,key2=value2`.
`--taints=<key>=<value>:<effect>,<key>=<value>:<effect>`:: Optional: Defines the taints for the machine pool. Replace `<key>=<value>:<effect>,<key>=<value>:<effect>` with a key, value, and effect for each taint, for example `--taints=key1=value1:NoSchedule,key2=value2:NoExecute`. Available effects include `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.
`--availability-zone=<availability_zone_name>`::
Optional: For Multi-AZ clusters, you can create a machine pool in a Single-AZ of your choice. Replace `<availability_zone_name>` with a Single-AZ name.
Optional: You can create a machine pool in an availability zone of your choice. Replace `<availability_zone_name>` with an availability zone name.
`--use-spot-instances`:: Optional: Configures your machine pool to deploy machines as non-guaranteed AWS Spot Instances. For information, see Amazon EC2 Spot Instances in the AWS documentation. If you select *Use Amazon EC2 Spot Instances* for a machine pool, you cannot disable the option after the machine pool is created.
+
[IMPORTANT]
====
Your Amazon EC2 Spot Instances might be interrupted at any time. Use Amazon EC2 Spot Instances only for workloads that can tolerate interruptions.
====
`--spot-max-price=<price>`:: Optional: If you choose to use Spot Instances, you can specify this argument to define a maximum hourly price for a Spot Instance. If this argument is not specified, the on-demand price is used.
--
+
The following example creates a machine pool called `mymachinepool` that uses the `m7i.xlarge` instance type and has autoscaling enabled. The minimum compute node limit is 3 and the maximum is 6 overall. The example also adds 2 workload-specific labels:
+
[source,terminal]
----
$ rosa create machinepool --cluster=mycluster --name=mymachinepool --enable-autoscaling --min-replicas=3 --max-replicas=6 --instance-type=m7i.xlarge --labels=app=db,tier=backend
----
+
.Example output
[source,terminal]
----
I: Machine pool 'mymachinepool' created successfully on cluster 'mycluster'
I: Machine pool 'mymachinepool' created successfully on hosted cluster 'mycluster'
I: To view all machine pools, run 'rosa list machinepools -c mycluster'
----

.Verification

You can list all machine pools on your cluster or describe individual machine pools.

. List the available machine pools on your cluster:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
ID             AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS                  TAINTS    AVAILABILITY ZONES                    SPOT INSTANCES
Default        No           3         m7i.xlarge                                        us-east-1a, us-east-1b, us-east-1c    N/A
mymachinepool  Yes          3-6       m7i.xlarge      app=db, tier=backend              us-east-1a, us-east-1b, us-east-1c    No
----
.Example output
[source,terminal]
----
ID             AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS                  TAINTS    AVAILABILITY ZONE  SUBNET                    VERSION  AUTOREPAIR
Default        No           1/1       m7i.xlarge                                       us-east-2c         subnet-00552ad67728a6ba3  4.14.34  Yes
mymachinepool  Yes          3/3-6     m7i.xlarge      app=db, tier=backend              us-east-2a         subnet-0cb56f5f41880c413  4.14.34  Yes
----

. Describe the information of a specific machine pool in your cluster:
+
[source,terminal]
----
$ rosa describe machinepool --cluster=<cluster_name> --machinepool=mymachinepool
----
+
.Example output
[source,terminal]
----
ID:                         mymachinepool
Cluster ID:                 27iimopsg1mge0m81l0sqivkne2qu6dr
Autoscaling:                Yes
Replicas:                   3-6
Instance type:              m7i.xlarge
Image type:                 Windows
Labels:                     app=db, tier=backend
Taints:
Availability zones:         us-east-1a, us-east-1b, us-east-1c
Subnets:
Spot instances:             No
Disk size:                  300 GiB
Security Group IDs:
----
.Example output
[source,terminal]
----
ID:                         mymachinepool
Cluster ID:                 2d6010rjvg17anri30v84vspf7c7kr6v
Autoscaling:                Yes
Desired replicas:           3-6
Current replicas:           3
Instance type:              m7i.xlarge
Labels:                     app=db, tier=backend
Taints:
Availability zone:          us-east-2a
Subnet:                     subnet-0cb56f5f41880c413
Version:                    4.14.34
Autorepair:                 Yes
Tuning configs:
Additional security group IDs:
Node drain grace period:
Message:
----

. Verify that the machine pool is included in the output and the configuration is as expected.
//OSDOCS-14809: Adding a separate module about Capacity Reservations. This might be a temporary solution since this module largely reuses content from modules/creating-a-machine-pool-cli.adoc. We might consider restructuring content from these 2 modules to meet ContentX and DITA migration goals.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="creating_a_machine_pools_cli_win_li_{context}"]
= Creating a machine pool with AWS Windows License Included enabled using the {rosa-cli}

[role="_abstract"]
If you are using {VirtProductName} on a OpenShift Container Platform cluster running Windows VMs you need to be license-compliant with Microsoft Windows in AWS. The hosts (AWS x86-64 bare metal EC2 instances) running these VMs must be enabled with AWS EC2 Windows License Included (LI).

[IMPORTANT]
====
Enabling AWS Windows LI on a machine pool applies the associated licensing fees on that specific machine pool. This includes billing for the full vCPU allocation of each AWS Windows LI enabled host in your OpenShift Container Platform cluster. Windows LI enabled machine pools will also deny vCPU over-allocation on {VirtProductName} VMs. For more information, see Microsoft Licensing on AWS and the OpenShift Container Platform instance types.
====

.Prerequisites

* You installed and configured the {rosa-cli} version 1.2.58 or above.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster version 4.19 or above.
* You identified an x86-64 bare metal EC2 instance type to use {VirtProductName}. For more, see Amazon EC2 Instance Types.
* You are in compliance with Microsoft and AWS requirements for the Microsoft licenses and associated costs.

.Procedure

* To add a Windows LI enabled machine pool to a OpenShift Container Platform cluster, create the machine pool with the following definitions:
+
[source,terminal]
----
$ rosa create machinepool --cluster=<cluster-name> \
                          --name=<machine_pool_id> \
                          --replicas=<replica_count> \
                          --instance-type=<instance_type> \
                          --type=<image_type>
----
where:

`--name=<machine_pool_id>`:: Specifies the name of the machine pool. Replace `<machine_pool_id>` with the name of your machine pool.
`--replicas=<replica_count>`:: Specifies the number of compute nodes to provision. If you deployed OpenShift Container Platform using a single availability zone, this defines the number of compute nodes to provision to the machine pool for the zone. If you deployed your cluster using multiple availability zones, this defines the number of compute nodes to provision in total across all zones and the count must be a multiple of 3. The `--replicas` argument is required when autoscaling is not configured.
`--instance-type=<instance_type>`:: Specifies the instance type. You can only select an x86-64 bare metal instance type to enable Windows LI. For example, you can use `m5zn.metal` or `i3.metal`. You cannot change the instance type for a machine pool after the pool is created.
`--type=<type>`:: You must specify `Windows` to ensure the machine pool is created with Windows LI enabled.
+
The following command creates a Windows LI enabled machine pool called `mymachinepool` using the `m5zn.metal` instance type with 1 compute node replica:
+
[source,terminal]
----
$ rosa create machinepool --cluster=mycluster --name=mymachinepool --type=Windows --instance-type=m5zn.metal --replicas=1
----
+
**Example output**
+
[source,terminal]
----
I: Machine pool 'mymachinepool' created successfully on cluster 'mycluster'
I: To view all machine pools, run 'rosa list machinepools -c mycluster'
----

.Verification

. List the available machine pools on your cluster by running the following command:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
. Describe the information of a specific machine pool in your cluster:
+
[source,terminal]
----
$ rosa describe machinepool --cluster=<cluster_name> --machinepool=mymachinepool
----
+
The output has the image type set to `Windows` as shown in the following example:
+
**Example output**
+
[source,terminal]
----
ID:                         mymachinepool
Cluster ID:                 mycluster
Autoscaling:                No
Desired replicas:           1
Current replicas:           1
Instance type:              m5zn.metal
Image type:                 Windows
Labels:
Tags:
Taints:
Availability zone:          us-east-1a
Subnet:                     <subnet-id>
Disk Size:                  300 GiB
Version:                    4.19.18
EC2 Metadata Http Tokens:   optional
Autorepair:                 Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
----
+
. For more information about running virtualized Windows workloads after you have set up a Windows LI enabled machine pool, see Creating a Windows VM compliant to AWS EC2 Windows License Included.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="creating_machine_pools_cli_capres_{context}"]
= Creating a machine pool with Capacity Reservations using the {rosa-cli}

[role="_abstract"]
You can create a new machine pool with Capacity Reservations by using the {rosa-cli-first}. Both On-Demand Capacity Reservations and Capacity Blocks for ML are supported.

[NOTE]
====
Currently, autoscaling is not supported on machine pools with Capacity Reservations.
====

.Prerequisites

* You installed and configured the latest {rosa-cli}.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster version 4.19 or above.
* The cluster already has a machine pool that is not using a Capacity Reservation or taints. The machine pool must have at least 2 worker nodes.
* You have a Capacity Reservation ID and capacity is reserved for the instance type required in the Availability Zone (AZ) of the machine pool that you are creating.

.Procedure

* Create the machine pool and define the Capacity Reservation preference and ID by running the following command:
+
[source,terminal]
----
$ rosa create machinepool --cluster=<cluster_name> \
                          --name=<machine_pool_id> \
                          --replicas=<replica_count> \
                          --capacity-reservation-preference none | open | capacity-reservations-only \
                          --capacity-reservation-id cr-<capacity_reservation_id> \
                          --instance-type=<instance_type> \
                          --subnet <subnet_id>
----

where:

*<machine_pool_id>*:: Specifies the name of the machine pool.
*<replica_count>*:: Specifies the number of provisioned compute nodes. If you deploy OpenShift Container Platform using a single AZ, this defines the number of compute nodes provisioned to the machine pool for the AZ. If you deploy your cluster using multiple AZs, this defines the total number of compute nodes provisioned across all AZs. For multi-zone clusters, the compute node count must be a multiple of 3. The `--replicas` argument is required when autoscaling is not configured.
*<capacity_reservation_preference>*:: Specifies the Capacity Reservation behaviour. Valid preferences include:

* `none`: The instance does not use a Capacity Reservation even if one is available. The instance runs as an EC2 On-Demand instance. Choose this option when you want to avoid consuming purchased reserved capacity and use it for other workloads.
* `open`: The instance can run in any `open` Capacity Reservation that has matching attributes such as the instance type, platform, AZ, or tenancy. Choose this option for flexibility; if a reservation is not available, the instance can use regular unreserved EC2 capacity.
* `capacity-reservations-only`: The instance can only run in a Capacity Reservation. If capacity is not available, the instance fails to launch.

*cr-<capacity_reservation_id>*:: Specifies the reservation ID. You get an ID in the `cr-<capacity_reservation_id>` format when you purchase a Capacity Reservation from AWS. The ID can be for both On-Demand Capacity Reservations or Capacity Blocks for ML, you do not need to specify the reservation type.
*<instance_type>*:: *Optional*: Specifies the instance type for the compute nodes in your machine pool. The instance type defines the vCPU and memory allocation for each compute node in the pool. Replace `<instance_type>` with an instance type. The default is `m5.xlarge`. You cannot change the instance type for a machine pool after the pool is created.
*<subnet_id>*:: *Optional*: Specifies the subnet ID. For Bring Your Own Virtual Private Cloud (BYO VPC) clusters, you can select a subnet to create a single-AZ machine pool. If you select a subnet that was not specified during the initial cluster creation, you must tag the subnet with the `kubernetes.io/cluster/<infra_id>` key and `shared` value. Customers can obtain the Infra ID by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster <cluster_name>|grep "Infra ID:"
----
+
.Example output
[source,terminal]
----
Infra ID:                   mycluster-xqvj7
----

.Example

The following example creates a machine pool called `mymachinepool` that uses the `c5.xlarge` instance type and has 1 compute node replica. The example also adds a Capacity Reservation ID. Example input and output:

[source,terminal]
----
$ rosa create machinepool --cluster=mycluster --name=mymachinepool --replicas 1 --capacity-reservation-id <capacity_reservation_id> --subnet <subnet_id> --instance-type c5.xlarge
----

[source,terminal]
----
I: Checking available instance types for machine pool 'mymachinepool'
I: Machine pool 'mymachinepool' created successfully on hosted cluster 'mycluster'
----

.Verification

You can list all machine pools on your cluster or describe individual machine pools.

* List the available machine pools on your cluster by running the following command:
+
[source,terminal]
----
$ rosa list machinepools --cluster <cluster_name>
----

* Describe the information of a specific machine pool in your cluster by running the following command.
+
[source,terminal]
----
$ rosa describe machinepool --cluster <cluster_name> --machinepool <machine_pool_name>
----
+
.Example output
[source,terminal]
----
ID:                         <machine_pool_name>
Cluster ID:                 <cluster_id>
Autoscaling:                No
Desired replicas:           1
Current replicas:           1
Instance type:              c5.xlarge
Labels:
Tags:                       red-hat-managed=true, api.openshift.com/environment=production, api.openshift.com/id=<cluster_name>, api.openshift.com/legal-entity-id=<legal_entity_id>, api.openshift.com/name=<cluster_name>, api.openshift.com/nodepool-hypershift=<cluster_name>-<machine_pool_name>, api.openshift.com/nodepool-ocm=<machine_pool_name>, red-hat-clustertype=rosa
Taints:
Availability zone:          us-east-1a
Subnet:                     <subnet_id>
Disk Size:                  300 GiB
Version:                    4.19.10
EC2 Metadata Http Tokens:   optional
Autorepair:                 Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Capacity Reservation:
    - ID:                   <capacity_reservation_id>
    - Type:                 OnDemand
    - Preference:           open
Management upgrade:
    - Type:                 Replace
    - Max surge:            1
    - Max unavailable:      0
Message:                    Minimum availability requires 1 replicas, current 1 available
----
+
The output should include the Capacity Reservation ID, type, and preference.

// TODO: This additional resource can be added back once all of the files are added to the ROSA HCP distro.
[role="_additional-resources"]
.Additional resources
* Additional custom security groups

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="configuring-machine-pool-disk-volume_{context}"]
= Configuring machine pool disk volume

Machine pool disk volume size can be configured for additional flexibility. The default disk size is 300 GiB.

For OpenShift Container Platform clusters version 4.13 or earlier, the disk size can be configured from a minimum of 128 GiB to a maximum of 1 TiB. For version 4.14 and later, the disk size can be configured to a minimum of 128 GiB to a maximum of 16 TiB.

For OpenShift Container Platform clusters, the disk size can be configured from a minimum of 75 GiB to a maximum of 16,384 GiB.

You can configure the machine pool disk size for your cluster by using {cluster-manager} or the {rosa-cli-first}.

[NOTE]
====
Existing cluster and machine pool node volumes cannot be resized.
====
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="configuring-machine-pool-disk-volume-ocm_{context}"]
= Configuring machine pool disk volume using OpenShift Cluster Manager

.Prerequisite for cluster creation
* You have the option to select the node disk sizing for the default machine pool during cluster installation.

.Procedure for cluster creation

. From the OpenShift Container Platform cluster wizard, navigate to *Cluster settings*.

. Navigate to *Machine pool* step.

. Select the desired *Root disk size*.

. Select *Next* to continue creating your cluster.

.Prerequisite for machine pool creation
* You have the option to select the node disk sizing for the new machine pool after the cluster has been installed.

.Procedure for machine pool creation

. Navigate to {cluster-manager-url} and select your cluster.

. Navigate to *Machine pool tab*.

. Click *Add machine pool*.

. Select the desired *Root disk size*.

. Select *Add machine pool* to create the machine pool.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="configuring-machine-pool-disk-volume-cli_{context}"]
= Configuring machine pool disk volume using the ROSA CLI

.Prerequisite for cluster creation

* You have the option to select the root disk sizing for the default machine pool during cluster installation.

.Procedure for cluster creation

* Run the following command when creating your OpenShift cluster for the desired root disk size:
+
[source,terminal]
----
$ rosa create cluster --worker-disk-size=<disk_size>
----
The value can be in GB, GiB, TB, or TiB. Replace `<disk_size>` with a numeric value and unit, for example `--worker-disk-size=200GiB`. You cannot separate the digit and the unit. No spaces are allowed.

.Prerequisite for machine pool creation

* You have the option to select the root disk sizing for the new machine pool after the cluster has been installed.

.Procedure for machine pool creation

. Scale up the cluster by executing the following command:
+
[source,terminal]
----
$ rosa create machinepool --cluster=<cluster_id> \// <1>
                          --disk-size=<disk_size> // <2>
----
<1> Specifies the ID or name of your existing OpenShift cluster.
<2> Specifies the worker node disk size. The value can be in GB, GiB, TB, or TiB. Replace `<disk_size>` with a numeric value and unit, for example `--disk-size=200GiB`. You cannot separate the digit and the unit. No spaces are allowed.

. Confirm new machine pool disk volume size by logging into the AWS console and find the EC2 virtual machine root volume size.

// TODO: This additional resource can be added back once all of the files are added to the ROSA HCP distro.
[role="_additional-resources"]
.Additional resources
* `rosa create machinepool` command

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="deleting-machine-pools_{context}"]
= Deleting a machine pool

[role="_abstract"]
You can delete a machine pool if your workload requirements have changed and your current machine pools no longer meet your needs. You can delete machine pools by using
{cluster-manager-first} or the {rosa-cli-first}.
{cluster-manager-first}.

.Prerequisites

* You have created an OpenShift Container Platform cluster.
* The cluster is in the ready state.
* You have an existing machine pool without any taints and with at least two replicas for a Single-AZ cluster or three replicas for a Multi-AZ cluster.

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that contains the machine pool that you want to delete.

. On the selected cluster, select the *Machine pools* tab.

. Under the *Machine pools* tab, click the Options menu {kebab} for the machine pool that you want to delete.

. Click *Delete*.

.Verification

* Verify that the machine pool no longer is displayed in the list of machine pools on the *Machine pools* tab.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

[id="deleting-machine-pools-ocm_{context}"]
= Deleting a machine pool

= Deleting a machine pool using {cluster-manager}

You can delete a machine pool for your OpenShift Container Platform cluster by using {cluster-manager-first}.

.Prerequisites

* You created a OpenShift Container Platform cluster.
* The cluster is in the ready state.
* You have an existing machine pool without any taints and with at least two instances for a single-AZ cluster or three instances for a multi-AZ cluster.
* You have created an OpenShift Container Platform cluster.
* The newly created cluster is in the ready state.

.Procedure
. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that contains the machine pool that you want to delete.

. On the selected cluster, select the *Machine pools* tab.

. Under the *Machine pools* tab, click the Options menu {kebab} for the machine pool that you want to delete.

. Click *Delete*.
+
The selected machine pool is deleted.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="deleting-machine-pools-cli_{context}"]
= Deleting a machine pool using the ROSA CLI

You can delete a machine pool for your OpenShift Container Platform cluster by using the {rosa-cli-first}.

[NOTE]
====
For users of `rosa` version 1.2.25 and earlier versions, the machine pool (ID='Default') that is created along with the cluster cannot be deleted. For users of `rosa` version 1.2.26 and later, the machine pool (ID='worker') that is created along with the cluster can be deleted if there is one machine pool within the cluster that contains no taints, and at least two replicas for a Single-AZ cluster or three replicas for a Multi-AZ cluster.
====

.Prerequisites

* You created a OpenShift Container Platform cluster.
* The cluster is in the ready state.
* You have an existing machine pool without any taints and with at least two instances for a Single-AZ cluster or three instances for a Multi-AZ cluster.
* You have created an OpenShift Container Platform cluster.

.Procedure
. From the {rosa-cli}, run the following command:
+
[source,terminal]
----
$ rosa delete machinepool -c=<cluster_name> <machine_pool_ID>
----
+
.Example output
[source,terminal]
----
? Are you sure you want to delete machine pool <machine_pool_ID> on cluster <cluster_name>? (y/N)
----
. Enter `y` to delete the machine pool.
+
The selected machine pool is deleted.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

[id="rosa-scaling-worker-nodes_{context}"]
= Scale compute nodes manually

[role="_abstract"]
If you have not enabled autoscaling for your machine pool, you can manually scale the number of compute nodes, also known as worker nodes, in the pool to meet your deployment needs. You must scale each machine pool separately.

.Prerequisites

* You installed and configured the latest {rosa-cli-first} on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.
* You created an OpenShift Container Platform cluster.
* You have an existing machine pool.

.Procedure

. List the machine pools in the cluster:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
*Example output*
+
[source,terminal]
----
ID        AUTOSCALING   REPLICAS    INSTANCE TYPE  LABELS    TAINTS   AVAILABILITY ZONES    DISK SIZE   SG IDs
default   No            2           m7i.xlarge                         us-east-1a            300GiB      sg-0e375ff0ec4a6cfa2
mp1       No            2           m7i.xlarge                         us-east-1a            300GiB      sg-0e375ff0ec4a6cfa2
----

. Increase or decrease the number of compute node replicas in a machine pool:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster_name> \
                        --replicas=<replica_count> \
                        <machine_pool_id>
----
+
where:
+
** `<replica_count>`: If you deployed OpenShift Container Platform using a single availability zone, the replica count defines the number of compute nodes to provision to the machine pool for the zone. If you deployed your cluster using multiple availability zones, the count defines the total number of compute nodes in the machine pool across all zones and must be a multiple of 3.
+
** `<replica_count>`: The replica count defines the number of compute nodes to provision to the machine pool for the zone.
+
** `<machine_pool_id>`: Replace with the ID of your machine pool, as listed in the output of the preceding command.

. List the available machine pools in your cluster:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
*Example output*
+
[source,terminal]
----
ID        AUTOSCALING   REPLICAS    INSTANCE TYPE  LABELS    TAINTS   AVAILABILITY ZONES    DISK SIZE   SG IDs
default   No            2           m7i.xlarge                         us-east-1a            300GiB      sg-0e375ff0ec4a6cfa2
mp1       No            3           m7i.xlarge                         us-east-1a            300GiB      sg-0e375ff0ec4a6cfa2
----

. In the output of the preceding command, verify that the compute node replica count is as expected for your machine pool. In the example output, the compute node replica count for the `mp1` machine pool is scaled to 3.

. Navigate to {cluster-manager-url} and select your cluster.
. Under the *Machine pools* tab, click the Options menu {kebab} for the machine pool that you want to scale.
. Select *Scale*.
. Specify the node count:
* If you deployed your cluster using a single availability zone, specify the *Node count* in the drop-down menu.
* If you deployed your cluster using multiple availability zones, specify the *Node count per zone* in the drop-down menu.
+
[NOTE]
====
Your subscription determines the number of nodes that you can select.
====
. Click *Apply* to scale the machine pool.

.Verification

* Verify that the compute node replica count is as expected for your machine pool by listing the machine pools and checking the REPLICAS column.
* Under the *Machine pools* tab, verify that the *Node count* for your machine pool is as expected.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

[id="rosa-osd-node-label-about_{context}"]
= Node labels for managing machine pools in OpenShift Container Platform

[role="_abstract"]
A label is a key-value pair applied to a `Node` object. You can use labels to organize sets of objects and control the scheduling of pods. You can add labels during cluster creation or after. Labels can be modified or updated at any time.

[role="_additional-resources"]
.Additional resources

* Kubernetes Labels and Selectors overview

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

[id="rosa-adding-node-labels_{context}"]
= Add node labels to a machine pool

[role="_abstract"]
Add or edit labels for compute nodes at any time to manage the nodes in a manner that is relevant to you. For example, you can assign types of workloads to specific nodes. Each key must be unique to the object it is assigned to.

.Prerequisites

* You installed and configured the latest {rosa-cli-first} on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.
* You created an OpenShift Container Platform cluster.
* You have an existing machine pool.

.Procedure

. List the machine pools in the cluster:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
*Example output*
+
[source,terminal]
----
ID           AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONES    SPOT INSTANCES
Default      No           2         m7i.xlarge                          us-east-1a            N/A
db-nodes-mp  No           2         m7i.xlarge                          us-east-1a            No
----
[source,terminal]
----
ID           AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    VERSION  AUTOREPAIR
workers      No           2/2       m7i.xlarge                          us-east-2a         subnet-0df2ec3377847164f  4.16.6   Yes
db-nodes-mp  No           2/2       m7i.xlarge                          us-east-2a         subnet-0df2ec3377847164f  4.16.6   Yes
----

. Add or update the node labels for a machine pool:

* To add or update node labels for a machine pool that does not use autoscaling, run the following command:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster_name> \
                        --labels=<key>=<value>,<key>=<value> \
                        <machine_pool_id>
----
+
Replace `<key>=<value>,<key>=<value>` with a comma-delimited list of key-value pairs, for example `--labels=key1=value1,key2=value2`. This list overwrites any modifications made to node labels on an ongoing basis.
+
The following example adds labels to the `db-nodes-mp` machine pool:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=mycluster --replicas=2 --labels=app=db,tier=backend db-nodes-mp
----
+
*Example output*
+
[source,terminal]
----
I: Updated machine pool 'db-nodes-mp' on cluster 'mycluster'
----
+
. Describe the details of the machine pool with the new labels:
+
[source,terminal]
----
$ rosa describe machinepool --cluster=<cluster_name> --machinepool=<machine-pool-name>
----
+
*Example output*
+
[source,terminal]
----
ID:                         db-nodes-mp
Cluster ID:                 <ID_of_cluster>
Autoscaling:                No
Replicas:                   2
Instance type:              m7i.xlarge
Labels:                     app=db, tier=backend
Taints:
Availability zones:         us-east-1a
Subnets:
Spot instances:             No
Disk size:                  300 GiB
Security Group IDs:
----
[source,terminal]
----
ID:                            db-nodes-mp
Cluster ID:                    <ID_of_cluster>
Autoscaling:                   No
Desired replicas:              2
Current replicas:              2
Instance type:                 m7i.xlarge
Labels:                        app=db, tier=backend
Tags:
Taints:
Availability zone:             us-east-2a
Subnet:                        subnet-0df2ec3377847164f
Disk size:                     300 GiB
Version:                       4.16.6
EC2 Metadata Http Tokens:      optional
Autorepair:                    Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Management upgrade:
 - Type:                       Replace
 - Max surge:                  1
 - Max unavailable:            0
Message:
----
+
. Verify that the labels are included for your machine pool in the output.
. Navigate to {cluster-manager-url} and select your cluster.
. Under the *Machine pools* tab, click the Options menu {kebab} for the machine pool that you want to add a label to.
. Select *Edit labels*.
. If you have existing labels in the machine pool that you want to remove, select *x* next to the label to delete it.
. Add a label using the format `<key>=<value>` and press enter. For example, add `app=db` and then press Enter. If the format is correct, the key value pair is then highlighted.
. Repeat the previous step if you want to add additional labels.
. Click *Save* to apply the labels to the machine pool.

.Verification

. Under the *Machine pools* tab, select *>* next to your machine pool to expand the view.
. Verify that your labels are listed under *Labels* in the expanded view.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="rosa-adding-tags_{context}"]
= Adding tags to a machine pool

You can add tags for compute nodes, also known as worker nodes, in a machine pool to introduce custom user tags for AWS resources that are generated when you provision your machine pool, noting that you can not edit the tags after you create the machine pool.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="rosa-adding-tags-cli_{context}"]
= Adding tags to a machine pool using the ROSA CLI

You can add tags to a machine pool for your OpenShift Container Platform cluster by using the {rosa-cli-first}. You can not edit the tags after after you create the machine pool.

[IMPORTANT]
====
You must ensure that your tag keys are not `aws`, `red-hat-managed`, `red-hat-clustertype`, or `Name`. In addition, you must not set a tag key that begins with `kubernetes.io/cluster/`. Your tag's key cannot be longer than 128 characters, while your tag's value cannot be longer than 256 characters. Red{nbsp}Hat reserves the right to add additional reserved tags in the future.
====

.Prerequisites

* You installed and configured the latest AWS (`aws`), ROSA (`rosa`), and OpenShift (`oc`) CLIs on your workstation.
* You logged in to your Red{nbsp}Hat account by using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.

.Procedure

* Create a machine pool with a custom tag by running the following command:
+
--
[source,terminal]
----
$ rosa create machinepools --cluster=<name> --replicas=<replica_count> \
     --name <mp_name> --tags='<key> <value>,<key> <value>' // <1>
----
<1> Replace `<key> <value>,<key> <value>` with a key and value for each tag.
--
+
.Example output
[source,terminal]
----
$ rosa create machinepools --cluster=mycluster --replicas 2 --tags='tagkey1 tagvalue1,tagkey2 tagvaluev2'

I: Checking available instance types for machine pool 'mp-1'
I: Machine pool 'mp-1' created successfully on cluster 'mycluster'
I: To view the machine pool details, run 'rosa describe machinepool --cluster mycluster --machinepool mp-1'
I: To view all machine pools, run 'rosa list machinepools --cluster mycluster'
----

.Verification

* Use the `describe` command to see the details of the machine pool with the tags, and verify that the tags are included for your machine pool in the output:
+
[source,terminal]
----
$ rosa describe machinepool --cluster=<cluster_name> --machinepool=<machinepool_name>
----
+
.Example output
[source,terminal]
----
ID:                                    mp-1
Cluster ID:                            2baiirqa2141oreotoivp4sipq84vp5g
Autoscaling:                           No
Replicas:                              2
Instance type:                         m7i.xlarge
Labels:
Taints:
Availability zones:                    us-east-1a
Subnets:
Spot instances:                        No
Disk size:                             300 GiB
Additional Security Group IDs:
Tags:                                  red-hat-clustertype=rosa, red-hat-managed=true, tagkey1=tagvalue1, tagkey2=tagvaluev2
----
[source,terminal]
----
ID:                            db-nodes-mp
Cluster ID:                    <ID_of_cluster>
Autoscaling:                   No
Desired replicas:              2
Current replicas:              2
Instance type:                 m7i.xlarge
Labels:
Tags:                          red-hat-clustertype=rosa, red-hat-managed=true, tagkey1=tagvalue1, tagkey2=tagvaluev2
Taints:
Availability zone:             us-east-2a
...
----
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

[id="rosa-adding-taints_{context}"]
= Add taints to a machine pool

[role="_abstract"]
You can add taints for compute nodes in a machine pool to control which pods are scheduled to them. When you apply a taint to a machine pool, the scheduler cannot place a pod on the nodes in the pool unless the pod specification includes a toleration for the taint.

Taints can be added to a machine pool using {cluster-manager-first} or the {rosa-cli-first}.

[NOTE]
====
A cluster must have at least one machine pool that does not contain any taints.
====
.Prerequisites
// ifdef::openshift-rosa[]
//   * You created a Red{nbsp}Hat OpenShift Service on AWS (ROSA) cluster.
// endif::openshift-rosa[]
 * You created an OpenShift Container Platform cluster.
 * You have an existing machine pool that does not contain any taints and contains at least two instances.

.Procedure
. Navigate to {cluster-manager-url} and select your cluster.
. Under the *Machine pools* tab, click the Options menu {kebab} for the machine pool that you want to add a taint to.
. Select *Edit taints*.
. Add *Key* and *Value* entries for your taint.
. Select an *Effect* for your taint from the list. Available options include `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.
. Select *Add taint* if you want to add more taints to the machine pool.
. Click *Save* to apply the taints to the machine pool.

.Verification

. Under the *Machine pools* tab, select *>* next to your machine pool to expand the view.
. Verify that your taints are listed under *Taints* in the expanded view.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

[id="rosa-adding-taints-ocm_{context}"]
= Adding taints to a machine pool using {cluster-manager}

You can add taints to a machine pool for your OpenShift Container Platform cluster by using {cluster-manager-first}.

.Prerequisites

* You created an OpenShift Container Platform cluster.
* You created a OpenShift Container Platform cluster.
* You have an existing machine pool that does not contain any taints and contains at least two instances.

.Procedure

//ifdef::openshift-dedicated[]
. Navigate to {cluster-manager-url} and select your cluster.
. Under the *Machine pools* tab, click the Options menu {kebab} for the machine pool that you want to add a taint to.
. Select *Edit taints*.
. Add *Key* and *Value* entries for your taint.
. Select an *Effect* for your taint from the list. Available options include `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.
. Optional: Select *Add taint* if you want to add more taints to the machine pool.
. Click *Save* to apply the taints to the machine pool.

.Verification

. Under the *Machine pools* tab, select *>* next to your machine pool to expand the view.
. Verify that your taints are listed under *Taints* in the expanded view.
//endif::[]
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
// * osd_cluster_admin/osd_nodes/osd-managing-worker-nodes.adoc

[id="rosa-adding-taints-cli_{context}"]
= Adding taints to a machine pool using the ROSA CLI

You can add taints to a machine pool for your OpenShift Container Platform cluster by using the {rosa-cli-first}.

[NOTE]
====
For users of `rosa` version 1.2.25 and prior versions, the number of taints cannot be changed within the machine pool (ID=`Default`) created along with the cluster. For users of `rosa` version 1.2.26 and beyond, the number of taints can be changed within the machine pool (ID=`worker`) created along with the cluster.
There must be at least one machine pool without any taints and with at least two replicas for a Single-AZ cluster or three replicas for a Multi-AZ cluster.
There must be at least one machine pool without any taints and with at least two replicas.
====

.Prerequisites

* You installed and configured the latest AWS (`aws`), ROSA (`rosa`), and OpenShift (`oc`) CLIs on your workstation.
* You logged in to your Red{nbsp}Hat account by using the `rosa` CLI.
* You created a OpenShift Container Platform cluster.
* You created an OpenShift Container Platform cluster.
* You have an existing machine pool that does not contain any taints and contains at least two instances.

.Procedure

. List the machine pools in the cluster by running the following command:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
ID           AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONES    SPOT INSTANCES     DISK SIZE   SG IDs
Default      No           2         m7i.xlarge                          us-east-1a            N/A                300 GiB     sg-0e375ff0ec4a6cfa2
db-nodes-mp  No           2         m7i.xlarge                          us-east-1a            No                 300 GiB     sg-0e375ff0ec4a6cfa2
----
[source,terminal]
----
ID           AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    VERSION  AUTOREPAIR
workers      No           2/2       m7i.xlarge                          us-east-2a         subnet-0df2ec3377847164f  4.16.6   Yes
db-nodes-mp  No           2/2       m7i.xlarge                          us-east-2a         subnet-0df2ec3377847164f  4.16.6   Yes
----

. Add or update the taints for a machine pool:

* To add or update taints for a machine pool that does not use autoscaling, run the following command:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=<cluster_name> \
                        --taints=<key>=<value>:<effect>,<key>=<value>:<effect> \// <1>
                        <machine_pool_id>
----
<1> Replace `<key>=<value>:<effect>,<key>=<value>:<effect>` with a key, value, and effect for each taint, for example `--taints=key1=value1:NoSchedule,key2=value2:NoExecute`. Available effects include `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.This list overwrites any modifications made to node taints on an ongoing basis.
+
The following example adds taints to the `db-nodes-mp` machine pool:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=mycluster --replicas 2 --taints=key1=value1:NoSchedule,key2=value2:NoExecute db-nodes-mp
----
+
.Example output
[source,terminal]
----
I: Updated machine pool 'db-nodes-mp' on cluster 'mycluster'
----

.Verification

. Describe the details of the machine pool with the new taints:
+
[source,terminal]
----
$ rosa describe machinepool --cluster=<cluster_name> --machinepool=<machinepool_name>
----
+
.Example output
[source,terminal]
----
ID:                         db-nodes-mp
Cluster ID:                 <ID_of_cluster>
Autoscaling:                No
Replicas:                   2
Instance type:              m7i.xlarge
Labels:
Taints:                     key1=value1:NoSchedule, key2=value2:NoExecute
Availability zones:         us-east-1a
Subnets:
Spot instances:             No
Disk size:                  300 GiB
Security Group IDs:
----
[source,terminal]
----
ID:                            db-nodes-mp
Cluster ID:                    <ID_of_cluster>
Autoscaling:                   No
Desired replicas:              2
Current replicas:              2
Instance type:                 m7i.xlarge
Labels:
Tags:
Taints:                        key1=value1:NoSchedule, key2=value2:NoExecute
Availability zone:             us-east-2a
...
----

. Verify that the taints are included for your machine pool in the output.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc
//

[id="rosa-configuring-autorepair_{context}"]
= Configuring machine pool AutoRepair

OpenShift Container Platform supports an automatic repair process for machine pools, called AutoRepair. AutoRepair is useful when you want the OpenShift Container Platform service to detect certain unhealthy nodes, drain the unhealthy nodes, and re-create the nodes. You can disable AutoRepair if the unhealthy nodes should not be replaced, such as in cases where the nodes should be preserved. AutoRepair is enabled by default on machine pools.

The AutoRepair process deems a node unhealthy when the state of the node is either `NotReady` or is in an unknown state for predefined amount of time (typically 8 minutes). Whenever two or more nodes become unhealthy simultaneously, the AutoRepair process stops repairing the nodes.
Similarly, when a new node is created unhealthy even after a predefined amount of time (typically 20 minutes), the service will auto-repair.

[NOTE]
====
Machine pool AutoRepair is only available for OpenShift Container Platform clusters.
====
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc

[id="rosa-autorepair-ocm_{context}"]
= Configuring AutoRepair on a machine pool using {cluster-manager}

You can configure machine pool AutoRepair for your OpenShift Container Platform cluster by using {cluster-manager-first}.

.Prerequisites

* You created a {hcp-title} cluster.
* You have an existing machine pool.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.
. Under the *Machine pools* tab, click the Options menu {kebab} for the machine pool that you want to configure auto repair for.
. From the menu, select *Edit*.
. From the *Edit Machine Pool* dialog box that displays, find the *AutoRepair* option.
. Select or clear the box next to *AutoRepair* to enable or disable.
. Click *Save* to apply the change to the machine pool.

.Verification

. Under the *Machine pools* tab, select *>* next to your machine pool to expand the view.
. Verify that your machine pool has the correct *AutoRepair* setting in the expanded view.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
// * nodes/rosa-managing-worker-nodes.adoc

[id="rosa-autorepair-cli_{context}"]
= Configuring machine pool AutoRepair using the ROSA CLI

You can configure machine pool AutoRepair for your OpenShift Container Platform cluster by using the {rosa-cli-first}.

.Prerequisites

* You installed and configured the latest AWS (`aws`) and ROSA (`rosa`) CLIs on your workstation.
* You logged in to your Red{nbsp}Hat account by using the `rosa` CLI.
* You created a OpenShift Container Platform cluster.
* You have an existing machine pool.

.Procedure

. List the machine pools in the cluster by running the following command:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
ID           AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    VERSION  AUTOREPAIR
workers      No           2/2       m7i.xlarge                          us-east-2a         subnet-0df2ec3377847164f  4.16.6   Yes
db-nodes-mp  No           2/2       m7i.xlarge                          us-east-2a         subnet-0df2ec3377847164f  4.16.6   Yes
----

. Enable or disable AutoRepair on a machine pool:

* To disable AutoRepair for a machine pool, run the following command:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=mycluster --machinepool=<machinepool_name>  --autorepair=false
----

* To enable AutoRepair for a machine pool, run the following command:
+
[source,terminal]
----
$ rosa edit machinepool --cluster=mycluster --machinepool=<machinepool_name>  --autorepair=true
----
+
.Example output
[source,terminal]
----
I: Updated machine pool 'machinepool_name' on cluster 'mycluster'
----

.Verification

. Describe the details of the machine pool:
+
[source,terminal]
----
$ rosa describe machinepool --cluster=<cluster_name> --machinepool=<machinepool_name>
----
+
.Example output
[source,terminal]
----
ID:                            machinepool_name
Cluster ID:                    <ID_of_cluster>
Autoscaling:                   No
Desired replicas:              2
Current replicas:              2
Instance type:                 m7i.xlarge
Labels:
Tags:
Taints:
Availability zone:             us-east-2a
...
Autorepair:                    Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Management upgrade:
 - Type:                               Replace
 - Max surge:                          1
 - Max unavailable:                    0
----

. Verify that the AutoRepair setting is correct for your machine pool in the output.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

[id="rosa-adding-tuning_{context}"]
= Adding node tuning to a machine pool

You can add tunings for compute, also called worker, nodes in a machine pool to control their configuration on OpenShift Container Platform clusters.

.Prerequisites

* You installed and configured the latest {rosa-cli-first} on your workstation.
* You logged in to your Red{nbsp}Hat account by using 'rosa'.
* You created a OpenShift Container Platform cluster.
* You have an existing machine pool.
* You have an existing tuning configuration.

.Procedure

. List all of the machine pools in the cluster:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
.Example output
+
[source,terminal]
----
ID           AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    VERSION  AUTOREPAIR
db-nodes-mp  No           0/2       m7i.xlarge                          us-east-2a         subnet-08d4d81def67847b6  4.14.34  Yes
workers      No           2/2       m7i.xlarge                          us-east-2a         subnet-08d4d81def67847b6  4.14.34  Yes
----

. You can add tuning configurations to an existing or new machine pool.

.. Add tunings when creating a machine pool:
+
[source,terminal]
----
$ rosa create machinepool -c <cluster-name> --name <machinepoolname> --tuning-configs <tuning_config_name>
----
+
.Example output
[source,terminal]
----
? Tuning configs: sample-tuning
I: Machine pool 'db-nodes-mp' created successfully on hosted cluster 'sample-cluster'
I: To view all machine pools, run 'rosa list machinepools -c sample-cluster'
----

.. Add or update the tunings for a machine pool:
+
[source,terminal]
----
$ rosa edit machinepool -c <cluster-name> --machinepool <machinepoolname> --tuning-configs <tuning_config_name>
----
+
.Example output
[source,terminal]
----
I: Updated machine pool 'db-nodes-mp' on cluster 'mycluster'
----

.Verification

. Describe the machine pool for which you added a tuning config:
+
[source,terminal]
----
$ rosa describe machinepool --cluster=<cluster_name> --machinepool=<machine_pool_name>
----
+
.Example output
[source,terminal]
----
ID:                                    db-nodes-mp
Cluster ID:                            <cluster_ID>
Autoscaling:                           No
Desired replicas:                      2
Current replicas:                      2
Instance type:                         m7i.xlarge
Labels:
Tags:
Taints:
Availability zone:                     us-east-2a
Subnet:                                subnet-08d4d81def67847b6
Version:                               4.14.34
EC2 Metadata Http Tokens:              optional
Autorepair:                            Yes
Tuning configs:                        sample-tuning
...
----

. Verify that the tuning config is included for your machine pool in the output.
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc
//this module applies to ROSA HCP only

[id="rosa-node-drain-grace-period_{context}"]
= Configuring node drain grace periods

You can configure the node drain grace period for machine pools in your cluster. The node drain grace period for a machine pool is how long the cluster respects the Pod Disruption Budget protected workloads when upgrading or replacing the machine pool. After this grace period, all remaining workloads are forcibly evicted. The value range for the node drain grace period is from `0` to `1 week`. With the default value `0`, or empty value, the machine pool drains without any time limitation until complete.

.Prerequisites

* You installed and configured the latest {rosa-cli-first} on your workstation.
* You created a OpenShift Container Platform cluster.
* You have an existing machine pool.

.Procedure

. List all of the machine pools in the cluster by running the following command:
+
[source,terminal]
----
$ rosa list machinepools --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
ID           AUTOSCALING  REPLICAS  INSTANCE TYPE  LABELS    TAINTS    AVAILABILITY ZONE  SUBNET                    VERSION  AUTOREPAIR
db-nodes-mp  No           2/2       m7i.xlarge                          us-east-2a         subnet-08d4d81def67847b6  4.14.34  Yes
workers      No           2/2       m7i.xlarge                          us-east-2a         subnet-08d4d81def67847b6  4.14.34  Yes
----

. Check the node drain grace period for a machine pool by running the following command:
+
[source,terminal]
----
$ rosa describe machinepool --cluster <cluster_name> --machinepool=<machinepool_name>
----
+
.Example output
[source,terminal]
----
ID:                                    workers
Cluster ID:                            2a90jdl0i4p9r9k9956v5ocv40se1kqs
...
Node drain grace period:               // <1>
...
----
+
<1> If this value is empty, the machine pool drains without any time limitation until complete.

. Optional: Update the node drain grace period for a machine pool by running the following command:
+
[source,terminal]
----
$ rosa edit machinepool --node-drain-grace-period="<node_drain_grace_period_value>" --cluster=<cluster_name>  <machinepool_name>
----
+
[NOTE]
====
Changing the node drain grace period during a machine pool upgrade applies to future upgrades, not in-progress upgrades.
====

.Verification

. Check the node drain grace period for a machine pool by running the following command:
+
[source,terminal]
----
$ rosa describe machinepool --cluster <cluster_name> <machinepool_name>
----
+
.Example output
[source,terminal]
----
ID:                                    workers
Cluster ID:                            2a90jdl0i4p9r9k9956v5ocv40se1kqs
...
Node drain grace period:               30 minutes
...
----

. Verify the correct `Node drain grace period` for your machine pool in the output.

== Additional resources
* About machine pools
* About autoscaling
* Enabling autoscaling
* Disabling autoscaling
* OpenShift Container Platform Service Definition
* OpenShift Container Platform Service Definition
