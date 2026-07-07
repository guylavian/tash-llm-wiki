---
title: "Managing compute nodes"
type: reference
domain: openshift
slug: osd-cluster-admin-4-22-osd-managing-worker-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_cluster_admin/osd-managing-worker-nodes
version: 4.22
family: osd_cluster_admin
documentKind: "Documentation"
---

# Managing compute nodes

[id="osd-managing-worker-nodes"]
= Managing compute nodes

[role="_abstract"]
Manage compute nodes, also known as worker nodes, in OpenShift Container Platform clusters to optimize workload placement and resource allocation. Configure machine pools to control node scaling, apply labels for workload targeting, and add taints to control pod scheduling.

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
//include::modules/deleting-machine-pools-ocm.adoc[leveloffset=+2]
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
* Additional custom security groups

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

[role="_additional-resources"]
== Additional resources
* About machine pools
* Enabling autoscaling
* Disabling autoscaling
* OpenShift Container Platform service definition
* Kubernetes Taints and Tolerations
* Controlling pod placement using node taints
* Working with nodes
