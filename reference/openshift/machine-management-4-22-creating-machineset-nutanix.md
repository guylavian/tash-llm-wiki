---
title: "Creating a compute machine set on Nutanix"
type: reference
domain: openshift
slug: machine-management-4-22-creating-machineset-nutanix
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-machineset-nutanix
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Creating a compute machine set on Nutanix

[id="creating-machineset-nutanix"]
= Creating a compute machine set on Nutanix

[role="_abstract"]
You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on Nutanix. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines, which helps ensure efficient resource allocation.

//[IMPORTANT] admonition for UPI

//Sample YAML for a compute machine set custom resource on Nutanix
// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * machine_management/creating_machinesets/creating-machineset-nutanix.adoc

[id="machineset-yaml-nutanix_{context}"]
= Sample YAML for a compute machine set custom resource on Nutanix

[role="_abstract"]
You can use a YAML file to automate node provisioning and ensure workloads are scheduled correctly based on role and infrastructure requirements.

The sample YAML shows how to define a Nutanix compute MachineSet for your cluster. It explains how to configure roles, labels, sizing, networking, and boot settings so new nodes are created consistently.

The sample YAML defines a Nutanix compute machine set that creates nodes that are labeled with

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and
is the node label to add.

[id="machineset-yaml-nutanix-oc_{context}"]
== Values obtained by using the OpenShift CLI

In the following example, you can obtain some of the values for your cluster by using the OpenShift CLI (`oc`).

Infrastructure ID:: The `<infrastructure_id>` string is the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
  name: <infrastructure_id>-<role>-<zone>
    machine.openshift.io/cluster-api-machine-role: <infra>
    machine.openshift.io/cluster-api-machine-type: <infra>
  name: <infrastructure_id>-<infra>-<zone>
  namespace: openshift-machine-api
  annotations:
    machine.openshift.io/memoryMb: "16384"
    machine.openshift.io/vCPU: "4"
spec:
  replicas: 3
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<zone>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1
          bootType: ""
          categories:
          - key: <category_name>
            value: <category_value>
          cluster:
            type: uuid
            uuid: <cluster_uuid>
          credentialsSecret:
            name: nutanix-credentials
          image:
            name: <infrastructure_id>-rhcos
            type: name
          kind: NutanixMachineProviderConfig
          memorySize: 16Gi
          project:
            type: name
            name: <project_name>
          subnets:
          - type: uuid
            uuid: <subnet_uuid>
          systemDiskSize: 120Gi
          userDataSecret:
            name: <user_data_secret>
          vcpuSockets: 4
          vcpusPerSocket: 1
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
----
where:
+
--
`<infrastructure_id>`:: Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster.
`<role>`:: Specifies the node label to add.
`<infrastructure_id>-<infra>-<region>`:: Specifies the infrastructure ID, node label, and zone.
`<infra>`:: Specifies the `<infra>` node label.
`<infrastructure_id>-<role>-<zone>`:: Specifies the infrastructure ID, `<infra>` node label, and zone.
`annotations`:: Specifies annotations for the cluster autoscaler.
`bootType`:: Specifies the boot type that the compute machines use. For more information about boot types, see Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment. Valid values are `Legacy`, `SecureBoot`, or `UEFI`. The default is `Legacy`.
+
[NOTE]
====
You must use the `Legacy` boot type in OpenShift Container Platform .
====
`<categories>`:: Specifies one or more Nutanix Prism categories to apply to compute machines. This stanza requires `key` and `value` parameters for a category key-value pair that exists in Prism Central. For more information about categories, see Category management.
`<cluster>`:: Specifies a Nutanix Prism Element cluster configuration. In this example, the cluster type is `uuid`, so there is a `uuid` stanza.
`<infrastructure_id>-rhcos`:: Specifies the image to use as a boot image for your nodes. You should use the use the latest image when adding a new machine set.
`16Gi`:: Specifies the amount of memory for the cluster in Gi.
`project`:: Specifies the Nutanix project that you use for your cluster. In this example, the project type is `name`, so there is a `name` stanza.
`subnets`:: Specifies one or more UUID for the Prism Element subnet object.
The CIDR IP address prefix for one of the specified subnets must contain the virtual IP addresses that the OpenShift Container Platform cluster uses.
A maximum of 32 subnets for each Prism Element failure domain in the cluster is supported.
All subnet UUID values must be unique.
`120Gi`:: Specifies the size of the system disk in Gi.
`<user_data_secret>`:: Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.
`4`:: Specifies the number of vCPU sockets.
`1`:: Specifies the number of vCPUs per socket.
taints::  Specifies a taint to prevent user workloads from being scheduled on infra nodes.
+
[NOTE]
====
After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or add toleration on `misscheduled` DNS pods.
====
--

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

//Failure domains for Nutanix clusters
// Module included in the following assemblies:
//
// * machine_management/cpmso-configuration.adoc
// * machine_management/creating_machinesets/creating-machineset-nutanix.adoc

[id="mapi-failure-domain-nutanix_{context}"]
= Failure domains for Nutanix clusters

[role="_abstract"]
Update failure domain configurations on a Nutanix cluster by coordinating changes to specific resources. You must modify the cluster infrastructure, control plane machine set, and compute machine set custom resources (CRs) to apply the new configuration.

To add or update the failure domain configuration on a Nutanix cluster, you must make coordinated changes to several resources. The following actions are required:

. Modify the cluster infrastructure custom resource (CR).

. Modify the cluster control plane machine set CR.

. Modify or replace the compute machine set CRs.

For more information, see "Adding failure domains to an existing Nutanix cluster" in the _Post-installation configuration_ content.

//Improving reliability for multiple subnet configurations on Nutanix
// Module included in the following assemblies:
//
// * installing/installing_nutanix/nutanix-failure-domains.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-nutanix.adoc
// * machine_management/control_plane_machine_management/cpmso-troubleshooting.adoc
// * machine_management/creating_machinesets/creating-machineset-nutanix.adoc

[id="cpmso-ts-nutanix-multiple-subnet_{context}"]
= Improving reliability for multiple subnet configurations on Nutanix

[role="_abstract"]
To improve reliability and avoid common networking problems with multiple subnet configurations on Nutanix, adhere to the configuration practices that minimize networking conflicts.

The following networking configuration and management practices can help your multiple subnet configuration perform more reliably:

* To avoid overlapping IP address assignments, use predefined static IP addresses in the `cloud-init` metadata.

* Tag all VMs, disks, and networks with a unique cluster ID.

* Avoid IP address conflicts by using dedicated subnets for each OpenShift Container Platform cluster:
+
Nutanix uses Nutanix Acropolis Hypervisor (AHV) and Nutanix Prism networking to assign IP addresses to virtual machines (VMs).
If a single subnet provides IP addresses for more than one OpenShift Container Platform cluster, AHV or Prism might assign the same IP address to a VM or pod in more than one cluster.
+
To avoid this issue, use dedicated subnets for each OpenShift Container Platform cluster, even when you have more than one cluster on a single Prism Central instance.
You can use the Prism UI or automation tools, such as Terraform or Ansible, to create separate IP address pools for each OpenShift Container Platform cluster.

* Ensure that each OpenShift Container Platform cluster uses distinct DNS zones and virtual IP address ranges.

* Avoid DHCP conflicts by maintaining DHCP allocations:
+
If you use Nutanix to manage DHCP allocation, objects in your cluster might have duplicate leases.
Duplicate leases can cause DHCP conflicts when you apply changes to the control plane machine set custom resource (CR) specification.
+
To avoid this issue, regularly remove stale DHCP leases.

* Use automation tools, such as Terraform or Ansible, to isolate the infrastructure for each OpenShift Container Platform cluster.

[role="_additional-resources"]
.Additional resources
* Cluster autoscaler resource definition
* Adding failure domains to an existing Nutanix cluster
