---
title: "Creating a compute machine set on Azure Stack Hub"
type: reference
domain: openshift
slug: machine-management-4-22-creating-machineset-azure-stack-hub
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-machineset-azure-stack-hub
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Creating a compute machine set on Azure Stack Hub

[id="creating-machineset-azure-stack-hub"]
= Creating a compute machine set on Azure Stack Hub

[role="_abstract"]
You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on {azure-first} Stack Hub. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

//[IMPORTANT] admonition for UPI

//Sample YAML for a compute machine set custom resource on Azure Stack Hub
// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc

[id="machineset-yaml-azure-stack-hub_{context}"]
= Sample YAML for a compute machine set custom resource on {azure-short} Stack Hub

[role="_abstract"]
You can create a machine set on {azure-first} Stack Hub. By defining a YAML configuration with specific cluster IDs and provider details, you can automate the provisioning of specialized nodes.

The {azure-full} sample YAML defines a compute machine set that runs in the `1` {azure-short} zone in a region and creates nodes that are labeled with
`node-role.kubernetes.io/<role>: ""`.
`node-role.kubernetes.io/infra: ""`. The sample YAML specifies a taint to prevent user workloads from being scheduled on infra nodes. After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or add toleration on `misscheduled` DNS pods.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and
`<role>`
`<infra>`
is the node label to add.

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
  name: <infrastructure_id>-<role>-<region>
    machine.openshift.io/cluster-api-machine-role: <infra>
    machine.openshift.io/cluster-api-machine-type: <infra>
  name: <infrastructure_id>-infra-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/<role>: ""
          node-role.kubernetes.io/infra: ""
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          availabilitySet: <availability_set>
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/<infrastructure_id>-rg/providers/Microsoft.Compute/images/<infrastructure_id>
            sku: ""
            version: ""
          internalLoadBalancer: ""
          kind: AzureMachineProviderSpec
          location: <region>
          location: <region>
          managedIdentity: <infrastructure_id>-identity
          metadata:
            creationTimestamp: null
          natRule: null
          networkResourceGroup: ""
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Linux
          publicIP: false
          publicLoadBalancer: ""
          resourceGroup: <infrastructure_id>-rg
          sshPrivateKey: ""
          sshPublicKey: ""
          subnet: <infrastructure_id>-<role>-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_DS4_v2
          vnet: <infrastructure_id>-vnet
          zone: "1"
          zone: "1"
----

where:

`<infrastructure_id>`:: Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift Container Platform CLI installed, you can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----
+
You can obtain the subnet by running the following command:
+
[source,terminal]
----
$  oc -n openshift-machine-api \
    -o jsonpath='{.spec.template.spec.providerSpec.value.subnet}{"\n"}' \
    get machineset/<infrastructure_id>-worker-centralus1
----
You can obtain the vnet by running the following command:
+
[source,terminal]
----
$  oc -n openshift-machine-api \
    -o jsonpath='{.spec.template.spec.providerSpec.value.vnet}{"\n"}' \
    get machineset/<infrastructure_id>-worker-centralus1
----
`<role>`:: Specifies the node label to add.
`<infrastructure_id>-<role>-<region>`:: Specifies the infrastructure ID, node label, and region.
`<region>`:: Specifies the region to place machines on.
+
[NOTE]
====
The `spec.template.spec.providerSpec.value.zone` specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify.
====

`<availability_set>`:: Specifies the availability set for the cluster.
`<image>`:: Specifies the boot image to use. You should use the use the latest image when adding a new machine set.
`<infra>`:: Specifies the `<infra>` node label.
`<infrastructure_id>-infra-<region>`::  Specifies the infrastructure ID, `<infra>` node label, and region.
`<region>`:: Specifies the region to place machines on.
+
[NOTE]
====
The `spec.template.spec.providerSpec.value.zone` specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify.
====

`<availability_set>`:: Specifies the availability set for the cluster.
`<image>`:: Specifies the boot image to use. You should use the use the latest image when adding a new machine set.

[NOTE]
====
Machine sets running on Azure Stack Hub do not support non-guaranteed Spot VMs.
====

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

//Enabling Azure boot diagnostics on compute machines
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-azure-boot-diagnostics_{context}"]
= Enabling {azure-first} boot diagnostics

[role="_abstract"]
You can enable boot diagnostics on {azure-full} machines that your machine set creates. Use this to store console logs that you can use to troubleshoot why a node fails to boot.

.Prerequisites

* Have an existing {azure-short}
cluster.

.Procedure

* Add the `diagnostics` configuration that is applicable to your storage type to the `providerSpec` field in your machine set YAML file:

** For an {azure-short} Managed storage account:
+
[source,yaml]
----
providerSpec:
  value:
    diagnostics:
      boot:
        storageAccountType: <azure_managed>
----
+
where:
+
--
`<azure_managed>`:: Specifies an {azure-short} Managed storage account.
--

** For an {azure-short} Unmanaged storage account:
+
[source,yaml]
----
providerSpec:
  value:
    diagnostics:
      boot:
        storageAccountType: <customer_managed>
        customerManaged:
          storageAccountURI: <https://<storage_account>.blob.core.windows.net>
----
+
where:
+
--
`<customer_managed>`:: Specifies an {azure-short} Unmanaged storage account.
`\https://<storage_account>.blob.core.windows.net`:: Specifies the storage account URL. Replace `<storage_account>` with the name of your storage account.
--
+
[NOTE]
====
Only the {azure-short} Blob Storage data service is supported.
====

.Verification

* On the {azure-short} portal, review the *Boot diagnostics* page for a machine deployed by the machine set, and verify that you can see the serial logs for the machine.

//Enabling customer-managed encryption keys for a compute machine set
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-enabling-customer-managed-encryption-azure_{context}"]
= Enabling customer-managed encryption keys for a machine set

[role="_abstract"]
To enhance data security, enable customer-managed encryption on {azure-full} by adding the disk encryption set ID to your machine set.

You can supply an encryption key to {azure-short} to encrypt data on managed disks at rest. You can enable server-side encryption with customer-managed keys by using the Machine API.

An {azure-short} Key Vault, a disk encryption set, and an encryption key are required to use a customer-managed key. The disk encryption set must be in a resource group where the Cloud Credential Operator (CCO) has granted permissions. If not, an additional reader role is required to be granted on the disk encryption set.

.Prerequisites

* You created an {azure-short} Key Vault instance ({azure-short} documentation).
* You created an instance of a disk encryption set ({azure-short} documentation).
* You granted the disk encryption set access to key vault ({azure-short} documentation).

.Procedure

* Configure the disk encryption set under the `providerSpec` field in your machine set YAML file. For example:
+
[source,yaml]
----
providerSpec:
  value:
    osDisk:
      diskSizeGB: 128
      managedDisk:
        diskEncryptionSet:
          id: /subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.Compute/diskEncryptionSets/<disk_encryption_set_name>
        storageAccountType: Premium_LRS
----

[role="_additional-resources"]
.Additional resources
* https://docs.microsoft.com/en-us/azure/virtual-machines/disk-encryption#customer-managed-keys[Customer-managed keys ({azure-short} documentation)]
