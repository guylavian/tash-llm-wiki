---
title: "Creating a compute machine set on {aws-short}"
type: reference
domain: openshift
slug: machine-management-4-22-creating-machineset-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-machineset-aws
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Creating a compute machine set on {aws-short}

[id="creating-machineset-aws"]
= Creating a compute machine set on {aws-short}

[role="_abstract"]
You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on {aws-first}. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

//[IMPORTANT] admonition for UPI

//Sample YAML for a compute machine set custom resource on AWS
// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc

[id="machineset-yaml-aws_{context}"]
=  Sample YAML for a compute machine set custom resource on {aws-short}

[role="_abstract"]
The sample YAML defines a compute machine set that runs in the `us-east-1a` {aws-first} Local Zone and creates nodes that are labeled with
This sample YAML defines a compute machine set that runs in the `us-east-1-nyc-1a` {aws-short} zone and creates nodes that are labeled with `node-role.kubernetes.io/edge: ""`.

The sample YAML specifies a taint to prevent user workloads from being scheduled on
nodes.

After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or add toleration on `misscheduled` DNS pods.

[NOTE]
====
If you want to reference the sample YAML file in the context of Wavelength Zones, ensure that you replace the {aws-short} Region and zone information with supported Wavelength Zone values.
====

In this sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and
is the node label to add.

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-<role>-<zone>
  name: <infrastructure_id>-infra-<zone>
  name: <infrastructure_id>-edge-<zone>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-edge-<zone>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
        machine.openshift.io/cluster-api-machine-role: infra
        machine.openshift.io/cluster-api-machine-type: infra
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<zone>
        machine.openshift.io/cluster-api-machine-role: edge
        machine.openshift.io/cluster-api-machine-type: edge
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-edge-<zone>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
          node-role.kubernetes.io/infra: ""
          machine.openshift.io/parent-zone-name: <value_of_ParentZoneName>
          machine.openshift.io/zone-group: <value_of_GroupName>
          machine.openshift.io/zone-type: <value_of_ZoneType>
          node-role.kubernetes.io/edge: ""
      providerSpec:
        value:
          ami:
            id: ami-046fe691f52a953f9
          apiVersion: machine.openshift.io/v1beta1
          blockDevices:
            - ebs:
                iops: 0
                volumeSize: 120
                volumeType: gp2
          credentialsSecret:
            name: aws-cloud-credentials
          deviceIndex: 0
          iamInstanceProfile:
            id: <infrastructure_id>-worker-profile
          instanceType: m6i.large
          kind: AWSMachineProviderConfig
          placement:
            availabilityZone: <zone>
            region: <region>
          securityGroups:
            - filters:
                - name: tag:Name
                  values:
                    - <infrastructure_id>-node
            - filters:
                - name: tag:Name
                  values:
                    - <infrastructure_id>-lb
          subnet:
            filters:
              - name: tag:Name
                values:
                  - <infrastructure_id>-subnet-private-<zone>
              id: <value_of_PublicSubnetIds>
          publicIp: true
          tags:
            - name: kubernetes.io/cluster/<infrastructure_id>
              value: owned
            - name: <custom_tag_name>
              value: <custom_tag_value>
          userDataSecret:
            name: worker-user-data
      taints:
        - key: node-role.kubernetes.io/infra
        - key: node-role.kubernetes.io/edge
          effect: NoSchedule
----
where:

`<infrastructure_id>`:: Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----
`<infrastructure_id>-<role>-<zone>`:: Specifies the infrastructure ID, role node label, and zone.
`<role>`:: Specifies the role node label to add.
`<infrastructure_id>-infra-<zone>`:: Specifies the infrastructure ID, `infra` role node label, and zone.
`<infra>`:: Specifies the `infra` role node label.
`<infrastructure_id>-edge-<zone>`:: Specifies the infrastructure ID, `edge` role node label, and zone name.
`<edge>`:: Specifies the `edge` role node label.
[NOTE]
====
The `spec.template.spec.providerSpec.value.ami.id` stanza specifies a valid {op-system-first} Amazon Machine Image (AMI) for your {aws-short} zone for your OpenShift Container Platform nodes. If you want to use an {aws-short} Machine Image (AMI) for your {aws-short} zone as a boot image for your OpenShift Container Platform nodes, you should use the latest image when adding a new machine set. If you want to use an {aws-short} Marketplace image, you must complete the OpenShift Container Platform subscription from the AWS Marketplace to obtain an AMI ID for your region.

[source,terminal]
----
$ oc -n openshift-machine-api \
    -o jsonpath='{.spec.template.spec.providerSpec.value.ami.id}{"\n"}' \
    get machineset/<infrastructure_id>-<role>-<zone>
----
====
`<zone>`:: Specifies the zone name, for example, `us-east-1a`.
`<zone>`:: Specifies the zone name, for example, `us-east-1-nyc-1a`.
`<region>`:: Specifies the region, for example, `us-east-1`.
`<infrastructure_id>-subnet-private-<zone>`:: Specifies the infrastructure ID and zone.
`<value_of_PublicSubnetIds>`:: Indicates the ID of the public subnet that you created in {aws-short} {zone-type}. You created this public subnet ID when you finished the procedure for "Creating a subnet in an {aws-short} zone".
`<custom_tag_name>`:: Optional: Specifies custom tag data for your cluster. For example, you might add an admin contact email address by specifying a `name:value` pair of `Email:\admin-email@example.com`.
+
[NOTE]
====
Custom tags can also be specified during installation in the `install-config.yaml` file. If the `install-config.yaml` file and the machine set include a tag with the same `name` data, the value for the tag from the machine set takes priority over the value for the tag in the `install-config.yaml` file.
====

Machine sets running on {aws-short} support non-guaranteed Spot Instances. You can save on costs by using Spot Instances at a lower price compared to On-Demand Instances on {aws-short}. For more information, see "Machine sets that deploy machines as Spot Instances".

[role="_additional-resources"]
.Additional resources

* Manually updating the boot image

//Creating a compute machine set
// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-osp.adoc
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-aws.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-azure.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-gcp.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-nutanix.adoc

[id="machineset-creating_{context}"]
= Creating a compute machine set

[role="_abstract"]
To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

[NOTE]
====
Clusters that are installed with user-provisioned infrastructure have a different networking stack than clusters with infrastructure that is provisioned by the installation program. As a result of this difference, automatic load balancer management is unsupported on clusters that have user-provisioned infrastructure. For these clusters, a compute machine set can only create `worker` and `infra` type machines.
====

.Prerequisites

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.
* Have the necessary permissions to deploy VMs in your vCenter instance and have the required access to the datastore specified.
* If your cluster uses user-provisioned infrastructure, you have satisfied the specific Machine API requirements for that configuration.
* Create an availability set in which to deploy Azure Stack Hub compute machines.
* In disconnected environments, the image specified in the `MachineSet` custom resource (CR) must have the OpenSSH server v0.0.1.0 installed.

.Procedure

. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.
+
Ensure that you set the `<clusterID>` and `<role>` parameter values.
Ensure that you set the `<availabilitySet>`, `<clusterID>`, and `<role>` parameter values.

. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

.. To list the compute machine sets in your cluster, run the following command:
+
[source,terminal]
----
$ oc get machinesets -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d   0         0                             55m
agl030519-vplxk-worker-us-east-1e   0         0                             55m
agl030519-vplxk-worker-us-east-1f   0         0                             55m
----

.. To view values of a specific compute machine set custom resource (CR), run the following command:
+
[source,terminal]
----
$ oc get machineset <machineset_name> \
  -n openshift-machine-api -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-<role>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
    spec:
      providerSpec:
        ...
----
+
where:

`metadata.labels.machine.openshift.io/cluster-api-cluster`:: Specifies the cluster infrastructure ID.
`metadata.labels.name`:: Specifies a default node label.
+
[NOTE]
====
For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.
====
`spec.template.metadata.spec.providerSpec`:: Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.
.. If you are creating a compute machine set for a cluster that has user-provisioned infrastructure, note the following important values:
+
.Example vSphere `providerSpec` values
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
...
template:
  ...
  spec:
    providerSpec:
      value:
        apiVersion: machine.openshift.io/v1beta1
        credentialsSecret:
          name: vsphere-cloud-credentials
        dataDisks:
        - name: <disk_name>
          provisioningMode: <mode>
          sizeGiB: 10
        diskGiB: 120
        kind: VSphereMachineProviderSpec
        memoryMiB: 16384
        network:
          devices:
            - networkName: "<vm_network_name>"
        numCPUs: 4
        numCoresPerSocket: 4
        snapshot: ""
        template: <vm_template_name>
        userDataSecret:
          name: worker-user-data
        workspace:
          datacenter: <vcenter_data_center_name>
          datastore: <vcenter_datastore_name>
          folder: <vcenter_vm_folder_path>
          resourcepool: <vsphere_resource_pool>
          server: <vcenter_server_address>
----
+
where:

`vsphere-cloud-credentials`:: Specifies the name of the secret in the `openshift-machine-api` namespace that contains the required vCenter credentials.
`<disk_name>`:: Specifies the collection of data disk definitions. For more information, see "Configuring data disks by using machine sets".
`<vm_template_name>`:: Specifies the name of the {op-system} VM template for your cluster that was created during installation.
`worker-user-data`:: Specifies the name of the secret in the `openshift-machine-api` namespace that contains the required Ignition configuration credentials.
`<vcenter_server_address>`:: Specifies the IP address or fully qualified domain name (FQDN) of the vCenter server.

. Create a `MachineSet` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

. If you need compute machine sets in other availability zones, repeat this process to create more compute machine sets.

.Verification

* View the list of compute machine sets by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                       DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-windows-worker-us-east-1a  1         1         1       1           11m
agl030519-vplxk-edge-us-east-1-nyc-1a      1         1         1       1           11m
agl030519-vplxk-worker-us-east-1a          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d          0         0                             55m
agl030519-vplxk-worker-us-east-1e          0         0                             55m
agl030519-vplxk-worker-us-east-1f          0         0                             55m
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-infra-us-east-1a    1         1         1       1           11m
agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d   0         0                             55m
agl030519-vplxk-worker-us-east-1e   0         0                             55m
agl030519-vplxk-worker-us-east-1f   0         0                             55m
----
+
When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

* Optional: To check nodes that were created by the edge machine, run the following command:
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

//Labeling GPU machine sets for the cluster autoscaler
// Module included in the following assemblies:
//
// * machine_management/applying-autoscaling.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/creating_machinesets/creating-machineset-bare-metal.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-ibm-cloud.adoc
// * machine_management/creating_machinesets/creating-machineset-ibm-power-vs.adoc
// * machine_management/creating_machinesets/creating-machineset-nutanix.adoc
// * machine_management/creating_machinesets/creating-machineset-osp.adoc
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc

[id="machineset-label-gpu-autoscaler_{context}"]
= Labeling GPU machine sets for the cluster autoscaler

[role="_abstract"]
Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

.Prerequisites
* Your cluster uses a cluster autoscaler.

.Procedure

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:
+
--
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: machine-set-name
spec:
  template:
    spec:
      metadata:
        labels:
          cluster-api/accelerator: <accelerator_name>
----

where:

`<accelerator_name>`:: Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.
+
[NOTE]
====
You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR.
For more information, see "Cluster autoscaler resource definition".
====
--

[role="_additional-resources"]
.Additional resources
* Cluster autoscaler resource definition

//Assigning machines to placement groups by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating-machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-aws-existing-placement-group_{context}"]
= Assigning machines to placement groups for Elastic Fabric Adapter instances by using machine sets

[role="_abstract"]
You can configure a machine set to deploy machines on Elastic Fabric Adapter (EFA) instances within an existing {aws-first} placement group. Using EFA instances to run control plane machines can improve network performance.

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html[EFA] instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. This example uses both to demonstrate a configuration that can improve network performance for machines within the specified placement group.

.Prerequisites

* You created a placement group in the {aws-short} console.
+
[NOTE]
====
Ensure that the rules and limitations for the type of placement group that you create are compatible with your intended use case.
The control plane machine set spreads the control plane machines across multiple failure domains when possible. To use placement groups for the control plane, you must use a placement group type that can span multiple Availability Zones.
====

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following lines under the `providerSpec` field:

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    spec:
      providerSpec:
        value:
          instanceType: <supported_instance_type>
          networkInterfaceType: EFA
          placement:
            availabilityZone: <zone>
            region: <region>
          placementGroupName: <placement_group>
          placementGroupPartition: <placement_group_partition_number>
# ...
----

where:

--
`spec.template.spec.providerSpec.value.instanceType`:: Specifies an instance type that supports EFAs.
`spec.template.spec.providerSpec.value.networkInterfaceType`:: Specifies the `EFA` network interface type.
`spec.template.spec.providerSpec.value.placement.availabilityZone`:: Specifies the zone, for example, `us-east-1a`.
`spec.template.spec.providerSpec.value.placement.region`:: Specifies the region, for example, `us-east-1`.
`spec.template.spec.providerSpec.value.placementGroupName`:: Specifies the name of the existing {aws-short} placement group to deploy machines in.
`spec.template.spec.providerSpec.value.placementGroupPartition`:: Optional: Specifies the partition number of the existing AWS placement group to deploy machines in.
--

.Verification

* In the {aws-short} console, find a machine that the machine set created and verify the following in the machine properties:

** The placement group field has the value that you specified for the `placementGroupName` parameter in the machine set.

** The partition number field has the value that you specified for the `placementGroupPartition` parameter in the machine set.

** The interface type field indicates that it uses an EFA.

//Machine sets that enable the Amazon EC2 Instance Metadata Service
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-imds-options_{context}"]
= Machine set options for the Amazon EC2 Instance Metadata Service

[role="_abstract"]
You can use machine sets to create machines that use a specific version of the Amazon EC2 Instance Metadata Service (IMDS). Configuring Amazon EC2 IMDS behavior for control plane machines improves security.

Machine sets can create machines that allow the use of both IMDSv1 and IMDSv2 or machines that require the use of IMDSv2.

[NOTE]
====
To use IMDSv2 on {aws-first} clusters that were created with OpenShift Container Platform version 4.6 or earlier, you must update your boot image. For more information, see "Boot image management".
====

To deploy new compute machines with your preferred IMDS configuration, create a compute machine set YAML file with the appropriate values. You can also edit an existing machine set to create new machines with your preferred IMDS configuration when the machine set is scaled up.

[IMPORTANT]
====
Before configuring a machine set to create machines that require IMDSv2, ensure that any workloads that interact with the {aws-short} metadata service support IMDSv2.
====

[role="_additional-resources"]
.Additional resources
* Use the Instance Metadata Service to access instance metadata ({aws-short} documentation)
* Boot image management

//Creating machines that use the Amazon EC2 Instance Metadata Service
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-creating-imds-options_{context}"]
= Configuring IMDS by using machine sets

[role="_abstract"]
You can specify whether to require the use of IMDSv2 by adding or editing the value of `metadataServiceOptions.authentication` in the machine set YAML file for your machines.

.Prerequisites
* To use IMDSv2, your {aws-first} cluster must have been created with OpenShift Container Platform version 4.7 or later.

.Procedure
* Add or edit the following lines under the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  value:
    metadataServiceOptions:
      authentication: Required
----

where:

`providerSpec.value.metadataServiceOptions.authentication`:: Specifies whether to require IMDSv2. Set this parameter to `Required` to require IMDSv2. Set this parameter to `Optional` to allow the use of both IMDSv1 and IMDSv2. If you do not specify a value, both IMDSv1 and IMDSv2 are allowed.

//Configuring storage throughput for gp3 drives
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-creating-gp3-throughput_{context}"]
= Configuring storage throughput for gp3 drives

[role="_abstract"]
You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an {aws-short} cluster.
You can configure the storage throughput by editing your compute or control plane machine set.

.Prerequisites

* You use gp3 storage volume(s).

.Procedure
* Add or edit the following lines under the `providerSpec` field in your compute or control plane machine set:
+
[source,yaml]
----
providerSpec:
  value:
    blockDevices:
      - ebs:
          throughputMib: <throughput_value>
----
where:

`<throughput_value>`::
Specifies a value in MiB per second between 125 and 2,000.
You can only edit this value on gp3 volumes.
The default value is `125`.

//Machine sets that deploy machines as Dedicated Instances
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-dedicated-instance_{context}"]
= Machine sets that deploy machines as Dedicated Instances

[role="_abstract"]
You can create a machine set running on {aws-first} that deploys machines as Dedicated Instances. Dedicated Instances run in a virtual private cloud (VPC) on hardware that is dedicated to a single customer.

These Amazon EC2 instances are physically isolated at the host hardware level. The isolation of Dedicated Instances occurs even if the instances belong to different {aws-short} accounts that are linked to a single payer account. However, other instances that are not dedicated can share hardware with Dedicated Instances if they belong to the same {aws-short} account.

Instances with either public or dedicated tenancy are supported by the Machine API. Instances with public tenancy run on shared hardware. Public tenancy is the default tenancy. Instances with dedicated tenancy run on single-tenant hardware.

//Creating Dedicated Instances by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.adoc

[id="machineset-creating-dedicated-instance_{context}"]
= Creating Dedicated Instances by using machine sets

[role="_abstract"]
You can run a machine that is backed by a Dedicated Instance by using Machine API integration. Set the `tenancy` field in your machine set YAML file to launch a Dedicated Instance on {aws-first}.

.Procedure

* Specify a dedicated tenancy under the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  placement:
    tenancy: dedicated
----

//Machine sets that place machines on Dedicated Hosts
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc

[id="machineset-dedicated-hosts_{context}"]
= Machine sets that place machines on Dedicated Hosts

[role="_abstract"]
You can configure machine sets to place machines on {aws-first} Dedicated Hosts. Dedicated Hosts are physical servers with instance capacity that is fully dedicated to your use. You can use Dedicated Hosts with your existing per-socket, per-core, or per-VM software licenses. With dynamic host allocation, the Machine API Operator requests a Dedicated Host from {aws-short} and applies the specified tags to the Dedicated Host.

//Place machines on Dedicated Hosts by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc

[id="machineset-creating-dedicated-hosts_{context}"]
= Place machines on Dedicated Hosts by using machine sets

[role="_abstract"]
You can configure a machine set to place machines on {aws-first} Dedicated Hosts. With dynamic host allocation, the Machine API Operator requests a Dedicated Host from {aws-short} and applies the specified tags to the Dedicated Host.

.Procedure

* Specify the following `placement` fields in your machine set YAML file:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
# ...
spec:
  template:
    spec:
      providerSpec:
        placement:
          tenancy: host
          host:
            affinity: DedicatedHost
            dedicatedHost:
              allocationStrategy: Dynamic
              dynamicHostAllocation:
                tags:
                - name: <tag_name>
                  value: <tag_value>
----
where:

`spec.template.spec.providerSpec.placement.host.dedicatedHost.dynamicHostAllocation.tags`:: Optional: Specifies tags to apply to the dynamically allocated Dedicated Host. If you specify tags, you must specify both a key and a value. For `<tag_name>`, specify the tag key, for example `Environment`. For `<tag_value>`, specify the tag value, for example `production`.

.Verification

* Verify that the machine set exists by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----

//Place machines on a specific Dedicated Host by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc

[id="machineset-creating-dedicated-hosts-byo-machineset_{context}"]
= Place machines on a specific Dedicated Host by using machine sets

[role="_abstract"]
You can configure a machine set to place machines on a specific {aws-first} Dedicated Host by specifying the host ID.

.Procedure

* Specify the following `placement` fields in your machine set YAML file:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
# ...
spec:
  template:
    spec:
      providerSpec:
        placement:
          tenancy: host
          host:
            affinity: DedicatedHost
            dedicatedHost:
              id: <dedicated_host_id>
----
where:

`<dedicated_host_id>`:: Specifies the ID of the {aws-short} Dedicated Host on which to place the machine, for example `h-0123456789abcdef0`.

.Verification

* Verify that the machine set exists by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----

//Machine sets that deploy machines as Spot Instances
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc

[id="machineset-non-guaranteed-instance_{context}"]

[role="_abstract"]
You can save on costs by creating a compute machine set running on {aws-first} that deploys machines as non-guaranteed Spot Instances. Spot Instances utilize unused {aws-short} EC2 capacity and are less expensive than On-Demand Instances. You can use Spot Instances for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.
You can save on costs by creating a compute machine set running on {azure-first} that deploys machines as non-guaranteed Spot VMs. Spot VMs use unused {azure-short} capacity and are less expensive than standard VMs. You can use Spot VMs for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.
You can save on costs by creating a compute machine set running on {gcp-short} that deploys machines as non-guaranteed Spot VMs. Spot VMs use excess Compute Engine capacity and are less expensive than normal instances. You can use Spot VMs for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.
You can save on costs by creating a compute machine set running on {gcp-short} that deploys machines as non-guaranteed preemptible VM instances. Preemptible VM instances use excess Compute Engine capacity and are less expensive than normal instances. You can use preemptible VM instances for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.

{aws-short} EC2 can terminate a Spot Instance at any time. {aws-short} gives a two-minute warning to the user when an interruption occurs. OpenShift Container Platform begins to remove the workloads from the affected instances when {aws-short} issues the termination warning.

Interruptions can occur when using Spot Instances for the following reasons:

* The instance price exceeds your maximum price
* The demand for Spot Instances increases
* The supply of Spot Instances decreases

When {aws-short} terminates an instance, a termination handler running on the Spot Instance node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot Instance.
{azure-short} can terminate a Spot VM at any time. {azure-short} gives a 30-second warning to the user when an interruption occurs. OpenShift Container Platform begins to remove the workloads from the affected instances when {azure-short} issues the termination warning.

Interruptions can occur when using Spot VMs for the following reasons:

* The instance price exceeds your maximum price
* The supply of Spot VMs decreases
* {azure-short} needs capacity back

When {azure-short} terminates an instance, a termination handler running on the Spot VM node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot VM.
[NOTE]
====
{gcp-short} recommends using Spot VMs over preemptible VMs because Spot VMs include new features that preemptible VMs do not support.
====

{gcp-short} Compute Engine can terminate a Spot VM at any time.
Compute Engine sends a best-effort preemption notice to the user indicating that an interruption will occur after 30 seconds.
OpenShift Container Platform begins to remove the workloads from the affected instances when Compute Engine issues the preemption notice.
An ACPI G3 Mechanical Off signal is sent to the operating system after 30 seconds if the instance is not stopped.
The Spot VM is then transitioned to a `TERMINATED` state by Compute Engine.

Interruptions can occur when using Spot VMs for the following reasons:

* There is a system or maintenance event
* The supply of Spot VMs decreases

When {gcp-short} terminates an instance, a termination handler running on the Spot VM node deletes the machine resource.
To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot VM.
[NOTE]
====
{gcp-short} recommends using Spot VMs over preemptible VMs because Spot VMs include new features that preemptible VMs do not support.
====

{gcp-short} Compute Engine can terminate a preemptible VM instance at any time. Compute Engine sends a preemption notice to the user indicating that an interruption will occur after 30 seconds. OpenShift Container Platform begins to remove the workloads from the affected instances when Compute Engine issues the preemption notice. An ACPI G3 Mechanical Off signal is sent to the operating system after 30 seconds if the instance is not stopped. The preemptible VM instance is then transitioned to a `TERMINATED` state by Compute Engine.

Interruptions can occur when using preemptible VM instances for the following reasons:

* There is a system or maintenance event
* The supply of preemptible VM instances decreases
* The instance reaches the end of the allotted 24-hour period for preemptible VM instances

When {gcp-short} terminates an instance, a termination handler running on the preemptible VM instance node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a preemptible VM instance.

//Creating Spot Instances by using compute machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc

[id="machineset-creating-non-guaranteed-instance_{context}"]

[role="_abstract"]
You can save on costs by creating a compute machine set that deploys machines as non-guaranteed instances.
To launch a preemptible VM instance on {gcp-short}, you add `preemptible` to your compute machine set YAML file.

[NOTE]
====
{gcp-short} recommends using Spot VMs over preemptible VMs because Spot VMs include new features that preemptible VMs do not support.
====

.Procedure
* Add the following line under the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  value:
    spotMarketOptions: {}
----
+
--
You can optionally set the `spotMarketOptions.maxPrice` field to limit the cost of the Spot Instance. For example you can set `maxPrice: '2.50'`.

[NOTE]
====
If the `maxPrice` is set, this value is used as the hourly maximum spot price. If it is not set, the maximum price defaults to charge up to the On-Demand Instance price.

It is strongly recommended to use the default On-Demand price as the `maxPrice` value and to not set the maximum price for Spot Instances.
====
--
+
[source,yaml]
----
providerSpec:
  value:
    spotVMOptions: {}
----
+
--
You can optionally set the `spotVMOptions.maxPrice` field to limit the cost of the Spot VM. For example you can set `maxPrice: '0.98765'`. If the `maxPrice` is set, this value is used as the hourly maximum spot price. If it is not set, the maximum price defaults to `-1` and charges up to the standard VM price.

{azure-full} caps Spot VM prices at the standard price. {azure-short} will not evict an instance due to pricing if the instance is set with the default `maxPrice`. However, an instance can still be evicted due to capacity restrictions.

[NOTE]
====
It is strongly recommended to use the default standard VM price as the `maxPrice` value and to not set the maximum price for Spot VMs.
====
--
+
[source,yaml]
----
providerSpec:
  value:
    provisioningModel: "Spot"
----
+
If you specify `provisioningModel: "Spot"`, the machine is labeled as an `interruptible-instance` after the instance is launched.
+
[NOTE]
====
This parameter is not compatible with setting the `providerSpec.value.preemptible` value to `true`.
====
+
--
[source,yaml]
----
providerSpec:
  value:
    preemptible: true
----

If `preemptible` is set to `true`, the machine is labeled as an `interruptible-instance` after the instance is launched.

[NOTE]
====
This parameter is not compatible with setting the `providerSpec.value.provisioningModel` value to `"Spot"`.
====
--

//Configuring Capacity Reservation by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-supported-features-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-supported-features-aws.adoc

[id="machineset-capacity-reservation_{context}"]

OpenShift Container Platform version  and later supports

[role="_abstract"]
You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define.

These parameters specify the
region, and number of instances that you want to reserve.
If your
can accommodate the capacity request, the deployment succeeds.

For more information, including limitations and suggested use cases for this

[NOTE]
====
You cannot change an existing Capacity Reservation configuration for a machine set.
To use a different Capacity Reservation group, you must replace the machine set and the machines that the previous machine set deployed.
====

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You installed the {oc-first}.
* You created a Capacity Reservation group.
For more information, see Create a Capacity Reservation in the {azure-full} documentation.
* You purchased an On-Demand Capacity Reservation or Capacity Block for ML.
For more information, see On-Demand Capacity Reservations and Capacity Blocks for ML in the {aws-short} documentation.

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following section under the `providerSpec` field:
+
.Sample configuration
[source,yaml]
----
tag::compute[]
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
end::compute[]
tag::controlplane[]
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
end::controlplane[]
# ...
spec:
  template:
tag::compute[]
    spec:
      providerSpec:
        value:
          capacityReservationGroupID: <capacity_reservation_group>
          capacityReservationId: <capacity_reservation>
          marketType: <market_type>
end::compute[]
tag::controlplane[]
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            capacityReservationGroupID: <capacity_reservation_group>
            capacityReservationId: <capacity_reservation>
            marketType: <market_type>
end::controlplane[]
# ...
----
+
where:
+
tag::compute[]
`<capacity_reservation_group>`::
`<capacity_reservation>`::
end::compute[]
tag::controlplane[]
`<capacity_reservation_group>`::
`<capacity_reservation>`::
end::controlplane[]
Specifies the ID of the
that you want the machine set to deploy machines on.

`<market_type>`::
Specifies the market type to use.
The following values are valid:
+
--
`CapacityBlock`:: Use this market type with Capacity Blocks for ML.
`OnDemand`:: Use this market type with On-Demand Capacity Reservations.
tag::compute[]
`Spot`:: Use this market type with Spot Instances.
This option is not compatible with Capacity Reservations.
end::compute[]
--

.Verification

* To verify machine deployment, list the machines that the machine set created by running the following command:
+
[source,terminal]
----
tag::compute[]
$ oc get machines.machine.openshift.io \
  -n openshift-machine-api \
  -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
end::compute[]
tag::controlplane[]
$ oc get machine \
  -n openshift-machine-api \
  -l machine.openshift.io/cluster-api-machine-role=master
end::controlplane[]
----
tag::compute[]
+
where `<machine_set_name>` is the name of the compute machine set.
end::compute[]
+
In the output, verify that the characteristics of the listed machines match the parameters of your

//Adding a GPU node to a machine set (stesmith)
// Module included in the following assemblies:
//
//  * machine_management/creating-machinesets/creating-machineset-aws.adoc

[id="nvidia-gpu-aws-adding-a-gpu-node_{context}"]
= Adding a GPU node to an existing OpenShift Container Platform cluster

[role="_abstract"]
You can copy and modify a default compute machine set configuration to create a GPU-enabled machine set and machines for the AWS EC2 cloud provider.

For more information about the supported instance types, see the following NVIDIA documentation:

* NVIDIA GPU Operator Community support matrix

* NVIDIA AI Enterprise support matrix

.Procedure

. View the existing nodes, machines, and machine sets  by running the following command. Note that each node is an instance of a machine definition with a specific AWS region and OpenShift Container Platform role.
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
+
[source,terminal]
----
NAME                                        STATUS   ROLES                  AGE     VERSION
ip-10-0-52-50.us-east-2.compute.internal    Ready    worker                 3d17h   v1.35.4
ip-10-0-58-24.us-east-2.compute.internal    Ready    control-plane,master   3d17h   v1.35.4
ip-10-0-68-148.us-east-2.compute.internal   Ready    worker                 3d17h   v1.35.4
ip-10-0-68-68.us-east-2.compute.internal    Ready    control-plane,master   3d17h   v1.35.4
ip-10-0-72-170.us-east-2.compute.internal   Ready    control-plane,master   3d17h   v1.35.4
ip-10-0-74-50.us-east-2.compute.internal    Ready    worker                 3d17h   v1.35.4
----

. View the machines and machine sets that exist in the `openshift-machine-api` namespace by running the following command. Each compute machine set is associated with a different availability zone within the AWS region. The installer automatically load balances compute machines across availability zones.
+
[source,terminal]
----
$ oc get machinesets -n openshift-machine-api
----
+
.Example output
+
[source,terminal]
----
NAME                                        DESIRED   CURRENT   READY   AVAILABLE   AGE
preserve-dsoc12r4-ktjfc-worker-us-east-2a   1         1         1       1           3d11h
preserve-dsoc12r4-ktjfc-worker-us-east-2b   2         2         2       2           3d11h
----

. View the machines that exist in the `openshift-machine-api` namespace by running the following command. At this time, there is only one compute machine per machine set, though a compute machine set could be scaled to add a node in a particular region and zone.
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api | grep worker
----
+
.Example output
+
[source,terminal]
----
preserve-dsoc12r4-ktjfc-worker-us-east-2a-dts8r      Running   m5.xlarge   us-east-2   us-east-2a   3d11h
preserve-dsoc12r4-ktjfc-worker-us-east-2b-dkv7w      Running   m5.xlarge   us-east-2   us-east-2b   3d11h
preserve-dsoc12r4-ktjfc-worker-us-east-2b-k58cw      Running   m5.xlarge   us-east-2   us-east-2b   3d11h
----

. Make a copy of one of the existing compute `MachineSet` definitions and output the result to a JSON file by running the following command. This will be the basis for the GPU-enabled compute machine set definition.
+
[source,terminal]
----
$ oc get machineset preserve-dsoc12r4-ktjfc-worker-us-east-2a -n openshift-machine-api -o json > <output_file.json>
----

. Edit the JSON file and make the following changes to the new `MachineSet` definition:
+
* Replace `worker` with `gpu`. This will be the name of the new machine set.
* Change the instance type of the new `MachineSet` definition to `g4dn`, which includes an NVIDIA Tesla T4 GPU.
To learn more about AWS `g4dn` instance types, see Accelerated Computing.
+
[source,terminal]
----
$ jq .spec.template.spec.providerSpec.value.instanceType preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json

"g4dn.xlarge"
----
+
The `<output_file.json>` file is saved as `preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json`.

 . Update the following fields in `preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json`:
+
* `.metadata.name` to a name containing `gpu`.

* `.spec.selector.matchLabels["machine.openshift.io/cluster-api-machineset"]` to
match the new `.metadata.name`.

* `.spec.template.metadata.labels["machine.openshift.io/cluster-api-machineset"]`
to match the new `.metadata.name`.

* `.spec.template.spec.providerSpec.value.instanceType` to `g4dn.xlarge`.

. To verify your changes, perform a `diff` of the original compute definition and the new GPU-enabled node definition by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api get preserve-dsoc12r4-ktjfc-worker-us-east-2a -o json | diff preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json -
----
+
.Example output
+
[source,terminal]
----
10c10

< "name": "preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a",
---
> "name": "preserve-dsoc12r4-ktjfc-worker-us-east-2a",

21c21

< "machine.openshift.io/cluster-api-machineset": "preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a"
---
> "machine.openshift.io/cluster-api-machineset": "preserve-dsoc12r4-ktjfc-worker-us-east-2a"

31c31

< "machine.openshift.io/cluster-api-machineset": "preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a"
---
> "machine.openshift.io/cluster-api-machineset": "preserve-dsoc12r4-ktjfc-worker-us-east-2a"

60c60

< "instanceType": "g4dn.xlarge",
---
> "instanceType": "m5.xlarge",
----

. Create the GPU-enabled compute machine set from the definition by running the following command:
+
[source,terminal]
----
$ oc create -f preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json
----
+
.Example output
+
[source,terminal]
----
machineset.machine.openshift.io/preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a created
----

.Verification

. View the machine set you created by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api get machinesets | grep gpu
----
+
The MachineSet replica count is set to `1` so a new `Machine` object is created automatically.

+
.Example output
+
[source,terminal]
----
preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a   1         1         1       1           4m21s
----

. View the `Machine` object that the machine set created by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api get machines | grep gpu
----
+
.Example output
+
[source,terminal]
----
preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a    running    g4dn.xlarge   us-east-2   us-east-2a  4m36s
----

Note that there is no need to specify a namespace for the node. The node definition is cluster scoped.

//Deploying the Node Feature Discovery Operator (stesmith)
// Module included in the following assemblies:
//
//  * machine_management/creating_machinesets/creating-machineset-aws.adoc
//  * machine_management/creating_machinesets/creating-machineset-gcp.adoc
//  * machine_management/creating_machinesets/creating-machineset-azure.adoc

[id="nvidia-gpu-aws-deploying-the-node-feature-discovery-operator_{context}"]
= Deploying the Node Feature Discovery Operator

[role="_abstract"]
After the GPU-enabled node is created, you need to discover the GPU-enabled node so it can be scheduled. To do this, install the Node Feature Discovery (NFD) Operator.

The NFD Operator identifies hardware device features in nodes. It solves the general problem of identifying and cataloging hardware resources in the infrastructure nodes so they can be made available to OpenShift Container Platform.

.Procedure

. Install the Node Feature Discovery Operator from the software catalog in the OpenShift Container Platform console.

. After installing the NFD Operator, select *Node Feature Discovery* from the installed Operators list and select *Create instance*. This installs the `nfd-master` and `nfd-worker` pods, one `nfd-worker` pod for each compute node, in the `openshift-nfd` namespace.

. Verify that the Operator is installed and running by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-nfd
----
+
.Example output
+
[source,terminal]
----
NAME                                       READY    STATUS     RESTARTS   AGE

nfd-controller-manager-8646fcbb65-x5qgk    2/2      Running 7  (8h ago)   1d
----

. Browse to the installed Operator in the console and select *Create Node Feature Discovery*.

. Select *Create* to build a NFD custom resource. This creates NFD pods in the `openshift-nfd` namespace that poll the OpenShift Container Platform nodes for hardware resources and catalog them.

.Verification

. After a successful build, verify that a NFD pod is running on each nodes by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-nfd
----
+
.Example output
[source,terminal]
----
NAME                                       READY   STATUS      RESTARTS        AGE
nfd-controller-manager-8646fcbb65-x5qgk    2/2     Running     7 (8h ago)      12d
nfd-master-769656c4cb-w9vrv                1/1     Running     0               12d
nfd-worker-qjxb2                           1/1     Running     3 (3d14h ago)   12d
nfd-worker-xtz9b                           1/1     Running     5 (3d14h ago)   12d
----
+
The NFD Operator uses vendor PCI IDs to identify hardware in a node. NVIDIA uses the PCI ID `10de`.

. View the NVIDIA GPU discovered by the NFD Operator by running the following command:
+
[source,terminal]
----
$ oc describe node ip-10-0-132-138.us-east-2.compute.internal | egrep 'Roles|pci'
----
+
.Example output
[source,terminal]
----
Roles: worker

feature.node.kubernetes.io/pci-1013.present=true

feature.node.kubernetes.io/pci-10de.present=true

feature.node.kubernetes.io/pci-1d0f.present=true
----
+
`10de` appears in the node feature list for the GPU-enabled node. This mean the NFD Operator correctly identified the node from the GPU-enabled MachineSet.
