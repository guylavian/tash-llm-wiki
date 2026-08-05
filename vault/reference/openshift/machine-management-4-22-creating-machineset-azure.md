---
title: "Creating a compute machine set on {azure-short}"
type: reference
domain: openshift
slug: machine-management-4-22-creating-machineset-azure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-machineset-azure
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Creating a compute machine set on {azure-short}

[id="creating-machineset-azure"]
= Creating a compute machine set on {azure-short}

[role="_abstract"]
You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on {azure-first}. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

//[IMPORTANT] admonition for UPI

//Sample YAML for a compute machine set custom resource on Azure
// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * machine_management/creating-machineset-azure.adoc

[id="machineset-yaml-azure_{context}"]
= Sample YAML for a compute machine set custom resource on {azure-short}

[role="_abstract"]
You can define a machine set YAML to provision nodes by specifying parameters such as `vmSize` and `image`. You can use this to automate and scale infrastructure consistently, to ensure compute nodes meet specific workload requirements within the cluster.

The sample YAML defines a compute machine set that runs in the `1` {azure-first} zone in a region and creates nodes that are labeled with
The YAML file specifies a taint to prevent user workloads from being scheduled on infra nodes. After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or add toleration on `misscheduled` DNS pods.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and
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
    machine.openshift.io/cluster-api-machine-role: infra
    machine.openshift.io/cluster-api-machine-type: infra
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
        machine.openshift.io/cluster-api-machine-role: infra
        machine.openshift.io/cluster-api-machine-type: infra
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          machine.openshift.io/cluster-api-machineset: <machineset_name>
          node-role.kubernetes.io/<role>: ""
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/<infrastructure_id>-rg/providers/Microsoft.Compute/galleries/gallery_<infrastructure_id>/images/<infrastructure_id>-gen2/versions/latest
            sku: ""
            version: ""
          internalLoadBalancer: ""
          kind: AzureMachineProviderSpec
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
          tags:
            <custom_tag_name_1>: <custom_tag_value_1>
            <custom_tag_name_2>: <custom_tag_value_2>
          subnet: <infrastructure_id>-<role>-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_D4s_v3
          vnet: <infrastructure_id>-vnet
          zone: "1"
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
----

where:

`<infrastructure_id>`:: Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:
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
[NOTE]
====
The value of the `metadata.labels.machine.openshift.io/cluster-api-machine-role` parameter specifies the `infra` node label.
====
`<infrastructure_id>-infra-<region>`:: Specifies the infrastructure ID, `infra` node label, and region.

[NOTE]
====
The value of the `spec.template.spec.providerSpec.value.image` parameter specifies the image details for your compute machine set. If you want to use an {azure-short} Marketplace image, see "Using the {azure-short} Marketplace offering".

The value of the `spec.template.spec.providerSpec.value.image.resourceID` parameter specifies an image that is compatible with your instance type. The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix.

The value of the `spec.template.spec.providerSpec.value.location` parameter specifies the region to place machines on.
====

`<custom_tag_name_1>`:: Optional: Specifies custom tags in your machine set. Provide the tag name in `<custom_tag_name>` field and the corresponding tag value in `<custom_tag_value>` field.

[NOTE]
====
The value of the `spec.template.spec.providerSpec.value.zone` parameter specifies the zone within your region to place machines on. Ensure that your region supports the zone that you specify. If your region supports availability zones, you must specify the zone. Specifying the zone avoids volume node affinity failure when a pod requires a persistent volume attachment. To do this, you can create a compute machine set for each zone in the same region.
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

//Using the Azure Marketplace offering
// Module included in the following assemblies:
//
// * installing/installing_aws/installing-azure-customizations.adoc
// * installing/installing_aws/installing-azure-user-infra.adoc
// * machine_management/creating-machineset-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

//mpytlak: The procedure differs depending on whether this module is used in an IPI or UPI assembly.
//jrouth: Also some variations for when it appears in the machine management content (`mapi`).

[id="installation-azure-marketplace-subscribe_{context}"]
= Using the {azure-short} Marketplace offering

[role="_abstract"]
You can use the {azure-short} Marketplace offering to deploy an OpenShift Container Platform cluster, which is billed on pay-per-use basis (hourly, per core) through {azure-short}, while still being supported directly by Red{nbsp}Hat.

To deploy an OpenShift Container Platform cluster using the {azure-short} Marketplace offering, you must first obtain the {azure-short} Marketplace image. The installation program uses this image to deploy worker or control plane nodes. When obtaining your image, consider the following:
You can create a machine set running on {azure-short} that deploys machines that use the {azure-short} Marketplace offering. To use this offering, you must first obtain the {azure-short} Marketplace image. When obtaining your image, consider the following:

* While the images are the same, the {azure-short} Marketplace publisher is different depending on your region. If you are located in North America, specify `redhat` as the publisher. If you are located in EMEA, specify `redhat-limited` as the publisher.
* The offer includes a `rh-ocp-worker` SKU and a `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker` SKU represents a Hyper-V generation version 2 VM image. The default instance types used in OpenShift Container Platform are version 2 compatible. If you plan to use an instance type that is only version 1 compatible, use the image associated with the `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker-gen1` SKU represents a Hyper-V version 1 VM image.
//What happens with control plane machines? "worker" SKU seems incorrect

[IMPORTANT]
====
Installing images with the {azure-short} marketplace is not supported on clusters with 64-bit ARM instances.

====

.Prerequisites

* You have installed the {azure-short} CLI client `(az)`.
* Your {azure-short} account is entitled for the offer and you have logged into this account with the {azure-short} CLI client.

.Procedure

. Display all of the available OpenShift Container Platform images by running one of the following commands:
+
--
** North America:
+
[source,terminal]
----
$  az vm image list --all --offer rh-ocp-worker --publisher redhat -o table
----
+
.Example output
[source,terminal]
----
Offer          Publisher       Sku                 Urn                                                             Version
-------------  --------------  ------------------  --------------------------------------------------------------  -----------------
rh-ocp-worker  RedHat          rh-ocp-worker       RedHat:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
rh-ocp-worker  RedHat          rh-ocp-worker-gen1  RedHat:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
----
** EMEA:
+
[source,terminal]
----
$  az vm image list --all --offer rh-ocp-worker --publisher redhat-limited -o table
----
+
.Example output
[source,terminal]
----
Offer          Publisher       Sku                 Urn                                                                     Version
-------------  --------------  ------------------  --------------------------------------------------------------          -----------------
rh-ocp-worker  redhat-limited  rh-ocp-worker       redhat-limited:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
rh-ocp-worker  redhat-limited  rh-ocp-worker-gen1  redhat-limited:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
----
--
+
[NOTE]
====
Use the latest image that is available for compute and control plane nodes. If required, your VMs are automatically upgraded as part of the installation process.
====
. Inspect the image for your offer by running one of the following commands:
** North America:
+
[source,terminal]
----
$ az vm image show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
----
** EMEA:
+
[source,terminal]
----
$ az vm image show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
----
. Review the terms of the offer by running one of the following commands:
** North America:
+
[source,terminal]
----
$ az vm image terms show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
----
** EMEA:
+
[source,terminal]
----
$ az vm image terms show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
----
. Accept the terms of the offering by running one of the following commands:
** North America:
+
[source,terminal]
----
$ az vm image terms accept --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
----
** EMEA:
+
[source,terminal]
----
$ az vm image terms accept --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
----
. Record the image details of your offer. You must update the `compute` section in the `install-config.yaml` file with values for `publisher`, `offer`, `sku`, and `version` before deploying the cluster. You may also update the `controlPlane` section to deploy control plane machines with the specified image details, or the `defaultMachinePlatform` section to deploy both control plane and compute machines with the specified image details. Use the latest available image for control plane and compute nodes.
. Record the image details of your offer. If you use the {azure-short} Resource Manager (ARM) template to deploy your compute nodes:
+
.. Update `storageProfile.imageReference` by deleting the `id` parameter and adding the `offer`, `publisher`, `sku`, and `version` parameters by using the values from your offer.
.. Specify a `plan` for the virtual machines (VMs).
+
.Example `06_workers.json` ARM template with an updated `storageProfile.imageReference` object and a specified `plan`
+
[source,json,subs="none"]
----
...
  "plan" : {
    "name": "rh-ocp-worker",
    "product": "rh-ocp-worker",
    "publisher": "redhat"
  },
  "dependsOn" : [
    "[concat('Microsoft.Network/networkInterfaces/', concat(variables('vmNames')[copyIndex()], '-nic'))]"
  ],
  "properties" : {
...
  "storageProfile": {
    "imageReference": {
    "offer": "rh-ocp-worker",
    "publisher": "redhat",
    "sku": "rh-ocp-worker",
    "version": "413.92.2023101700"
    }
    ...
   }
...
  }
----

. Record the image details of your offer, specifically the values for `publisher`, `offer`, `sku`, and `version`.

.Sample `install-config.yaml` file with the {azure-short} Marketplace compute nodes

[source,yaml]
----
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    azure:
      type: Standard_D4s_v5
      osImage:
        publisher: redhat
        offer: rh-ocp-worker
        sku: rh-ocp-worker
        version: 413.92.2023101700
  replicas: 3
----
. Add the following parameters to the `providerSpec` section of your machine set YAML file using the image details for your offer:
+
.Sample `providerSpec` image values for {azure-short} Marketplace machines
[source,yaml]
----
providerSpec:
  value:
    image:
      offer: rh-ocp-worker
      publisher: redhat
      resourceID: ""
      sku: rh-ocp-worker
      type: MarketplaceWithPlan
      version: 413.92.2023101700
----
//offer also has "worker"

//Enabling Azure boot diagnostics
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

//Machine sets that deploy machines as Spot VMs
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

//Creating Spot VMs by using compute machine sets
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

//Machine sets that deploy machines on Ephemeral OS disks
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc

[id="machineset-azure-ephemeral-os_{context}"]
= Machine sets that deploy machines on Ephemeral OS disks

[role="_abstract"]
You can create a compute machine set running on {azure-first} that deploys machines on Ephemeral OS disks. Ephemeral OS disks use local VM capacity rather than remote {azure-short} Storage. This configuration therefore incurs no additional cost and provides lower latency for reading, writing, and reimaging.

[role="_additional-resources"]
.Additional resources

* Ephemeral OS disks for {azure-short} VMs ({azure-full} documentation)

//Creating machines on Ephemeral OS disks by using compute machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc

[id="machineset-creating-azure-ephemeral-os_{context}"]
= Creating machines on Ephemeral OS disks by using compute machine sets

[role="_abstract"]
To improve performance and reduce storage costs, you can host the OS disk directly on the local storage of the virtual machines (VMs) rather than on remote {azure-first} Storage. You can launch machines on Ephemeral OS disks on {azure-short} by editing your compute machine set YAML file.

.Prerequisites

* Have an existing {azure-full} cluster.

.Procedure

. Edit the custom resource (CR) by running the following command:
+
[source,terminal]
----
$ oc edit machineset <machine-set-name>
----
+
where `<machine-set-name>` is the compute machine set that you want to provision machines on Ephemeral OS disks.

. Add the following to the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  value:
    ...
    osDisk:
       ...
       diskSettings:
         ephemeralStorageLocation: Local
       cachingType: ReadOnly
       managedDisk:
         storageAccountType: Standard_LRS
       ...
----
+
where:
+
`providerSpec.value.osDisk.diskSettings`, `providerSpec.value.osDisk.diskSettings.ephemeralStorageLocation`, and `providerSpec.value.osDisk.cachingType`:: Enables the use of Ephemeral OS disks.
`providerSpec.value.osDisk.managedDisk.storageAccountType`:: Ephemeral OS disks are only supported for VMs or scale set instances that use the Standard LRS storage account type.
+
[IMPORTANT]
====
The implementation of Ephemeral OS disk support in OpenShift Container Platform only supports the `CacheDisk` placement type. Do not change the `placement` configuration setting.
====

. Create a compute machine set using the updated configuration:
+
[source,terminal]
----
$ oc create -f <machine-set-config>.yaml
----

.Verification

* On the {azure-full} portal, review the *Overview* page for a machine deployed by the compute machine set, and verify that the `Ephemeral OS disk` field is set to `OS cache placement`.

//Machine sets that deploy machines on ultra disks as data disks
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * storage/persistent_storage/persistent-storage-azure.adoc
// * storage/persistent_storage/persistent-storage-csi-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-azure-ultra-disk_{context}"]
= Machine sets that deploy machines with ultra disks as data disks
= Machine sets that deploy machines with ultra disks using PVCs

[role="_abstract"]
You can create a machine set running on {azure-first} that deploys machines with ultra disks. Ultra disks are high-performance storage that are intended for use with the most demanding data workloads.

You can also create a persistent volume claim (PVC) that dynamically binds to a storage class backed by {azure-short} ultra disks and mounts them to pods.

[NOTE]
====
Data disks do not support the ability to specify disk throughput or disk IOPS. You can configure these properties by using PVCs.
====

Both the in-tree plugin and CSI driver support using PVCs to enable ultra disks. You can also deploy machines with ultra disks as data disks without creating a PVC.

[role="_additional-resources"]
.Additional resources
* {azure-full} ultra disks documentation
* Machine sets that deploy machines on ultra disks using CSI PVCs
* Machine sets that deploy machines on ultra disks using in-tree PVCs

//Creating machines on ultra disks by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * storage/persistent_storage/persistent-storage-azure.adoc
// * storage/persistent_storage/persistent-storage-csi-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-creating-azure-ultra-disk_{context}"]
= Creating machines with ultra disks by using machine sets

[role="_abstract"]
You can deploy machines with ultra disks on {azure-first} by editing your machine set YAML file.

.Prerequisites

* Have an existing {azure-full} cluster.

.Procedure

. Create a custom secret in the `openshift-machine-api` namespace using the `{machine-role}` data secret by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api \
get secret <role>-user-data \
--template='{{index .data.userData | base64decode}}' | jq > userData.txt
----
+
where:
+
--
`<role>`:: Replace with `{machine-role}`.
`userData.txt`:: Specifies `userData.txt` as the name of the new custom secret.
--
. In a text editor, open the `userData.txt` file and locate the final `}` character in the file.

.. On the immediately preceding line, add a `,`.

.. Create a new line after the `,` and add the following configuration details:
+
[source,json]
----
"storage": {
  "disks": [
    {
      "device": "/dev/disk/azure/scsi1/lun0",
      "partitions": [
        {
          "label": "lun0p1",
          "sizeMiB": 1024,
          "startMiB": 0
        }
      ]
    }
  ],
  "filesystems": [
    {
      "device": "/dev/disk/by-partlabel/lun0p1",
      "format": "xfs",
      "path": "/var/lib/lun0p1"
    }
  ]
},
"systemd": {
  "units": [
    {
      "contents": "[Unit]\nBefore=local-fs.target\n[Mount]\nWhere=/var/lib/lun0p1\nWhat=/dev/disk/by-partlabel/lun0p1\nOptions=defaults,pquota\n[Install]\nWantedBy=local-fs.target\n",
      "enabled": true,
      "name": "var-lib-lun0p1.mount"
    }
  ]
}
----
+
where:
+
--
`"disks"`:: Specifies the configuration details for the disk that you want to attach to a node as an ultra disk.
`"device"`:: Specifies the `lun` value that is defined in the `dataDisks` stanza of the machine set you are using. For example, if the machine set contains `lun: 0`, specify `lun0`. You can initialize multiple data disks by specifying multiple `"disks"` entries in this configuration file. If you specify multiple `"disks"` entries, ensure that the `lun` value for each matches the value in the machine set.
`"partitions"`:: Specifies the configuration details for a new partition on the disk.
`"label"`:: Specifies a label for the partition. You might find it helpful to use hierarchical names, such as `lun0p1` for the first partition of `lun0`.
`"sizeMiB"`:: Specifies the total size in MiB of the partition.
`"filesystems"`:: Specifies the filesystem to use when formatting a partition. Use the partition label to specify the partition.
`"units"`:: Specifies a `systemd` unit to mount the partition at boot. Use the partition label to specify the partition. You can create multiple partitions by specifying multiple `"partitions"` entries in this configuration file. If you specify multiple `"partitions"` entries, you must specify a `systemd` unit for each.
`"contents"`:: Specifies the value of `storage.filesystems.path` for `Where`. Specifies the value of `storage.filesystems.device` for `What`.
--
. Extract the disabling template value to a file called `disableTemplating.txt` by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api get secret <role>-user-data \
--template='{{index .data.disableTemplating | base64decode}}' | jq > disableTemplating.txt
----
+
Replace `<role>` with `{machine-role}`.

. Combine the `userData.txt` file and `disableTemplating.txt` file to create a data secret file by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api create secret generic <role>-user-data-x5 \
--from-file=userData=userData.txt \
--from-file=disableTemplating=disableTemplating.txt
----
+
For `<role>-user-data-x5`, specify the name of the secret. Replace `<role>` with `{machine-role}`.

. Copy an existing {azure-short} `MachineSet` custom resource (CR) and edit it by running the following command:
+
[source,terminal]
----
$ oc edit machineset <machine_set_name>
----
+
where:

`<machine_set_name>`:: Indicates the machine set that you want to provision machines with ultra disks.

. Add the following lines in the positions indicated:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
spec:
  template:
    spec:
      metadata:
        labels:
          disk: ultrassd
      providerSpec:
        value:
          ultraSSDCapability: Enabled
          dataDisks:
          - nameSuffix: ultrassd
            lun: 0
            diskSizeGB: 4
            deletionPolicy: Delete
            cachingType: None
            managedDisk:
              storageAccountType: UltraSSD_LRS
          userDataSecret:
            name: <role>-user-data-x5
----
+
where:
+
--
`spec.template.spec.metadata.labels.disk`:: Specifies a label to use to select a node that is created by this machine set. The example uses `disk.ultrassd` for this value.
`spec.template.spec.providerSpec.value.ultraSSDCapability`:: Enables the use of ultra disks.
For `dataDisks`, include the entire stanza.
`spec.template.spec.providerSpec.value.dataDisks`:: Ensure you include the entire stanza for `dataDisks`.
`spec.template.spec.providerSpec.value.userDataSecret.name`:: Specifies the user data secret created earlier. Replace `<role>` with `{machine-role}`.
--
. Create a machine set using the updated configuration by running the following command:
+
[source,terminal]
----
$ oc create -f <machine_set_name>.yaml
----

. Edit your control plane machine set CR by running the following command:
+
[source,terminal]
----
$ oc --namespace openshift-machine-api edit controlplanemachineset.machine.openshift.io cluster
----

. Add the following lines in the positions indicated:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: ControlPlaneMachineSet
spec:
  template:
    spec:
      metadata:
        labels:
          disk: ultrassd
      providerSpec:
        value:
          ultraSSDCapability: Enabled
          dataDisks:
          - nameSuffix: ultrassd
            lun: 0
            diskSizeGB: 4
            deletionPolicy: Delete
            cachingType: None
            managedDisk:
              storageAccountType: UltraSSD_LRS
          userDataSecret:
            name: <role>-user-data-x5
----
+
where:
+
--
`spec.template.spec.metadata.labels.disk`:: Specifies a label to use to select a node that is created by this machine set. The example uses `disk.ultrassd` for this value.
`spec.template.spec.providerSpec.value.ultraSSDCapability`:: Enables the use of ultra disks. For `dataDisks`, include the entire stanza.
`spec.template.spec.providerSpec.value.userDataSecret.name`:: Specifies the user data secret created earlier. Replace `<role>` with `{machine-role}`.
--
. Save your changes.

** For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

** For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

. Create a storage class that contains the following YAML definition:
+
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ultra-disk-sc
parameters:
  cachingMode: None
  diskIopsReadWrite: "2000"
  diskMbpsReadWrite: "320"
  kind: managed
  skuname: UltraSSD_LRS
provisioner: disk.csi.azure.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
----
+
where:
+
--
`metadata.name`:: Specifies the name of the storage class. The example uses `ultra-disk-sc` for this value.
`parameters.diskIopsReadWrite`:: Specifies the number of Input/Output Operations Per Second (IOPS) for the storage class.
`parameters.diskMbpsReadWrite`:: Specifies the throughput in MBps for the storage class.
`provisioner`:: For {azure-full} Kubernetes Service (AKS) version 1.21 or later, use `disk.csi.azure.com`. For earlier versions of AKS, use `kubernetes.io/azure-disk`.
`volumeBindingMode`:: Optional parameter. Specifies this parameter to wait for the creation of the pod that will use the disk.
--
. Create a persistent volume claim (PVC) to reference the `ultra-disk-sc` storage class that contains the following YAML definition:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ultra-disk
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: ultra-disk-sc
  resources:
    requests:
      storage: 4Gi
----
+
where:
+
--
`metadata.name`:: Specifies the name of the PVC. The example uses `ultra-disk` for this value.
`spec.storageClassName`:: Specifies the name of the storage class to use. The example  uses `ultra-disk-sc` storage class.
`spec.resources.requests.storage`:: Specifies the size for the storage class. The minimum value is `4Gi`.
--
. Create a pod that contains the following YAML definition:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: nginx-ultra
spec:
  nodeSelector:
    disk: ultrassd
  containers:
  - name: nginx-ultra
    image: alpine:latest
    command:
      - "sleep"
      - "infinity"
    volumeMounts:
    - mountPath: "/mnt/azure"
      name: volume
  volumes:
    - name: volume
      persistentVolumeClaim:
        claimName: ultra-disk
----
+
where:
+
--
`spec.nodeSelector.disk`:: Specifies the label of the machine set that enables the use of ultra disks. The example uses `disk.ultrassd` for this value.
`spec.volumes.persistentVolumeClaim.claimName`:: Specifies the name of the PVC to attach. This pod references the `ultra-disk` PVC.
--

.Verification

. Validate that the machines are created by running the following command:
+
[source,terminal]
----
$ oc get machines
----
+
The machines should be in the `Running` state.

. For a machine that is running and has a node attached, validate the partition by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host lsblk
----
+
In this command, `oc debug node/<node_name>` starts a debugging shell on the node `<node_name>` and passes a command with `--`. The passed command `chroot /host` provides access to the underlying host OS binaries, and `lsblk` shows the block devices that are attached to the host OS machine.

.Next steps

* To use an ultra disk from within a pod, create a workload that uses the mount point. Create a YAML file similar to the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: ssd-benchmark1
spec:
  containers:
  - name: ssd-benchmark1
    image: nginx
    ports:
      - containerPort: 80
        name: "http-server"
    volumeMounts:
    - name: lun0p1
      mountPath: "/tmp"
  volumes:
    - name: lun0p1
      hostPath:
        path: /var/lib/lun0p1
        type: DirectoryOrCreate
  nodeSelector:
    disktype: ultrassd
----

* To use an ultra disk on the control plane, reconfigure your workload to use the control plane's ultra disk mount point.

//Troubleshooting resources for machine sets that enable ultra disks
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * storage/persistent_storage/persistent-storage-azure.adoc
// * storage/persistent_storage/persistent-storage-csi-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-troubleshooting-azure-ultra-disk_{context}"]
= Troubleshooting resources for machine sets that enable ultra disks

[role="_abstract"]
You can recover from issues that you might encounter when you enable ultra disks for machine sets. Review fields, such as disk settings, and ensure that the parameters are correctly configured.

[id="ts-pvc-mounting-ultra_{context}"]
== Unable to mount a persistent volume claim backed by an ultra disk

If there is an issue mounting a persistent volume claim backed by an ultra disk, the pod becomes stuck in the `ContainerCreating` state and an alert is triggered.

For example, if the `additionalCapabilities.ultraSSDEnabled` parameter is not set on the machine that backs the node that hosts the pod, the following error message appears:

[source,terminal]
----
StorageAccountType UltraSSD_LRS can be used only when additionalCapabilities.ultraSSDEnabled is set.
----

* To resolve this issue, describe the pod by running the following command:
+
[source,terminal]
----
$ oc -n <stuck_pod_namespace> describe pod <stuck_pod_name>
----

[id="ts-mapi-attach-misconfigure_{context}"]
== Incorrect ultra disk configuration

If an incorrect configuration of the `ultraSSDCapability` parameter is specified in the machine set, the machine provisioning fails.

For example, if the `ultraSSDCapability` parameter is set to `Disabled`, but an ultra disk is specified in the `dataDisks` parameter, the following error message appears:

[source,terminal]
----
StorageAccountType UltraSSD_LRS can be used only when additionalCapabilities.ultraSSDEnabled is set.
----

* To resolve this issue, verify that your machine set configuration is correct.

[id="ts-mapi-attach-unsupported_{context}"]
== Unsupported disk parameters

If a region, availability zone, or instance size that is not compatible with ultra disks is specified in the machine set, the machine provisioning fails. Check the logs for the following error message:

[source,terminal]
----
failed to create vm <machine_name>: failure sending request for machine <machine_name>: cannot create vm: compute.VirtualMachinesClient#CreateOrUpdate: Failure sending request: StatusCode=400 -- Original Error: Code="BadRequest" Message="Storage Account type 'UltraSSD_LRS' is not supported <more_information_about_why>."
----

* To resolve this issue, verify that you are using this feature in a supported environment and that your machine set configuration is correct.

[id="ts-mapi-delete_{context}"]
== Unable to delete disks

If the deletion of ultra disks as data disks is not working as expected, the machines are deleted and the data disks are orphaned. You must delete the orphaned disks manually if desired.

//Enabling customer-managed encryption keys for a machine set
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

//Configuring trusted launch for Azure virtual machines by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-azure-trusted-launch_{context}"]
= Configuring trusted launch for {azure-short} virtual machines by using machine sets

[role="_abstract"]
OpenShift Container Platform  supports trusted launch for {azure-full} virtual machines (VMs). By editing the machine set YAML file, you can configure the trusted launch options that a machine set uses for machines that it deploys. For example, you can configure these machines to use UEFI security features such as Secure Boot or a dedicated virtual Trusted Platform Module (vTPM) instance.

[NOTE]
====
Some feature combinations result in an invalid configuration.
====

.UEFI feature combination compatibility
|====
|Secure Boot^[1]^ |vTPM^[2]^ |Valid configuration

|Enabled
|Enabled
|Yes

|Enabled
|Disabled
|Yes

|Enabled
|Omitted
|Yes

|Disabled
|Enabled
|Yes

|Omitted
|Enabled
|Yes

|Disabled
|Disabled
|No

|Omitted
|Disabled
|No

|Omitted
|Omitted
|No
|====
[.small]
--
1. Using the `secureBoot` field.
2. Using the `virtualizedTrustedPlatformModule` field.
--

For more information about related features and functionality, see the {azure-full} documentation about Trusted launch for {azure-short} virtual machines.

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following section under the `providerSpec` field to provide a valid configuration:
+
.Sample valid configuration with UEFI Secure Boot and vTPM enabled
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            securityProfile:
              settings:
                securityType: TrustedLaunch
                trustedLaunch:
                  uefiSettings:
                    secureBoot: Enabled
                    virtualizedTrustedPlatformModule: Enabled
# ...
----
+
where:
+
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.securityType`:: Enables the use of trusted launch for {azure-short} virtual machines. This value is required for all valid configurations.
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings`:: Specifies which UEFI security features to use. This section is required for all valid configurations.
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings.secureBoot`:: Enables UEFI Secure Boot.
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings.virtualizedTrustedPlatformModule`:: Enables the use of a vTPM.

.Verification

* On the {azure-full} portal, review the details for a machine deployed by the machine set and verify that the trusted launch options match the values that you configured.

//Configuring Azure confidential virtual machines by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-azure-confidential-vms_{context}"]
= Configuring {azure-short} confidential virtual machines by using machine sets

[role="_abstract"]
OpenShift Container Platform  supports {azure-full} confidential virtual machines (VMs). By enabling {azure-short} confidential VMs, you can use memory encryption to improve data confidentiality.

[NOTE]
====
Confidential VMs are currently not supported on 64-bit ARM architectures.
====

By editing the machine set YAML file, you can configure the confidential VM options that a machine set uses for machines that it deploys. For example, you can configure these machines to use UEFI security features such as Secure Boot or a dedicated virtual Trusted Platform Module (vTPM) instance.

[WARNING]
====
Not all instance types support confidential VMs. Do not change the instance type for a control plane machine set that is configured to use confidential VMs to a type that is incompatible. Using an incompatible instance type can cause your cluster to become unstable.
====

For more information about related features and functionality, see the {azure-full} documentation about Confidential virtual machines.

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following section under the `providerSpec` field:
+
--
.Sample configuration
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
          osDisk:
            # ...
            managedDisk:
              securityProfile:
                securityEncryptionType: VMGuestStateOnly
            # ...
          securityProfile:
            settings:
                securityType: ConfidentialVM
                confidentialVM:
                  uefiSettings:
                    secureBoot: Disabled
                    virtualizedTrustedPlatformModule: Enabled
          vmSize: Standard_DC16ads_v5
# ...
----

where:

`spec.template.spec.providerSpec.value.osDisk.managedDisk.securityProfile`:: Specifies security profile settings for the managed disk when using a confidential VM.
`spec.template.spec.providerSpec.value.osDisk.managedDisk.securityProfile.securityEncryptionType`:: Enables encryption of the {azure-full} VM Guest State (VMGS) blob. This setting requires the use of vTPM.
`spec.template.spec.providerSpec.value.securityProfile`:: Specifies security profile settings for the confidential VM.
`spec.template.spec.providerSpec.value.securityProfile.settings.securityType`:: Enables the use of confidential VMs. This value is required for all valid configurations.
`spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings`::  Specifies which UEFI security features to use. This section is required for all valid configurations.
`spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings.secureBoot`:: Disables UEFI Secure Boot.
`spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings.virtualizedTrustedPlatformModule`:: Enables the use of a vTPM.
`spec.template.spec.providerSpec.value.vmSize`:: Specifies an instance type that supports confidential VMs.
--

.Verification

* On the {azure-full} portal, review the details for a machine deployed by the machine set and verify that the confidential VM options match the values that you configured.

// Accelerated Networking for Microsoft Azure VMs
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-azure-accelerated-networking_{context}"]
= Accelerated Networking for {azure-first} VMs

[role="_abstract"]
Accelerated Networking uses single root I/O virtualization (SR-IOV) to provide {azure-first} VMs with a more direct path to the switch. This enhances network performance. You can enable this feature
after installation.

[id="machineset-azure-accelerated-networking-limits_{context}"]
== Limitations

Consider the following limitations when deciding whether to use Accelerated Networking:

* Accelerated Networking is only supported on clusters where the Machine API is operational.

* {empty}
+
Accelerated Networking requires an {azure-short} VM size that includes at least four vCPUs. To satisfy this requirement, you can change the value of `vmSize` in your machine set. For information about {azure-short} VM sizes, see {azure-first} documentation.

//iiuc, this is not true for control planes since the operator will roll out changes according to the update strategy
* When this feature is enabled on an existing {azure-short} cluster, only newly provisioned nodes are affected. Currently running nodes are not reconciled. To enable the feature on all nodes, you must replace each existing machine. This can be done for each machine individually, or by scaling the replicas down to zero, and then scaling back up to your desired number of replicas.

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
//  * machine_management/creating-machinesets/creating-machineset-azure.adoc

[id="nvidia-gpu-aws-adding-a-gpu-node_{context}"]
= Adding a GPU node to an existing OpenShift Container Platform cluster

[role="_abstract"]
To provide specialized hardware for compute-intensive workloads that require NVIDIA GPU acceleration, you can copy and modify a default compute machine set configuration to create a GPU-enabled machine set and machines for the {azure-first} cloud provider.

The following table lists the validated instance types:

[cols="1,1,1,1"]
|===
|vmSize |NVIDIA GPU accelerator |Maximum number of GPUs |Architecture

|`Standard_NC24s_v3`
|V100
|4
|x86

|`Standard_NC4as_T4_v3`
|T4
|1
|x86

|`ND A100 v4`
|A100
|8
|x86
|===

[NOTE]
====
By default, {azure-full} subscriptions do not have a quota for the {azure-full} instance types with GPU. Customers have to request a quota increase for the {azure-full} instance families in the preceding list.
====

.Procedure

. View the machines and machine sets that exist in the `openshift-machine-api` namespace by running the following command. Each compute machine set is associated with a different availability zone within the {azure-full} region. The installation program automatically load balances compute machines across availability zones.
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
+
[source,terminal]
----
NAME                              DESIRED   CURRENT   READY   AVAILABLE   AGE
myclustername-worker-centralus1   1         1         1       1           6h9m
myclustername-worker-centralus2   1         1         1       1           6h9m
myclustername-worker-centralus3   1         1         1       1           6h9m
----

. Make a copy of one of the existing compute `MachineSet` definitions and output the result to a YAML file by running the following command.
This will be the basis for the GPU-enabled compute machine set definition.
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api myclustername-worker-centralus1 -o yaml > machineset-azure.yaml
----

. View the content of the machineset:
+
[source,terminal]
----
$ cat machineset-azure.yaml
----
+
.Example `machineset-azure.yaml` file
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  annotations:
    machine.openshift.io/GPU: "0"
    machine.openshift.io/memoryMb: "16384"
    machine.openshift.io/vCPU: "4"
  creationTimestamp: "2023-02-06T14:08:19Z"
  generation: 1
  labels:
    machine.openshift.io/cluster-api-cluster: myclustername
    machine.openshift.io/cluster-api-machine-role: worker
    machine.openshift.io/cluster-api-machine-type: worker
  name: myclustername-worker-centralus1
  namespace: openshift-machine-api
  resourceVersion: "23601"
  uid: acd56e0c-7612-473a-ae37-8704f34b80de
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: myclustername
      machine.openshift.io/cluster-api-machineset: myclustername-worker-centralus1
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: myclustername
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: myclustername-worker-centralus1
    spec:
      lifecycleHooks: {}
      metadata: {}
      providerSpec:
        value:
          acceleratedNetworking: true
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          diagnostics: {}
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/myclustername-rg/providers/Microsoft.Compute/galleries/gallery_myclustername_n6n4r/images/myclustername-gen2/versions/latest
            sku: ""
            version: ""
          kind: AzureMachineProviderSpec
          location: centralus
          managedIdentity: myclustername-identity
          metadata:
            creationTimestamp: null
          networkResourceGroup: myclustername-rg
          osDisk:
            diskSettings: {}
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Linux
          publicIP: false
          publicLoadBalancer: myclustername
          resourceGroup: myclustername-rg
          spotVMOptions: {}
          subnet: myclustername-worker-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_D4s_v3
          vnet: myclustername-vnet
          zone: "1"
status:
  availableReplicas: 1
  fullyLabeledReplicas: 1
  observedGeneration: 1
  readyReplicas: 1
  replicas: 1
----

. Make a copy of the `machineset-azure.yaml` file by running the following command:
+
[source,terminal]
----
$ cp machineset-azure.yaml machineset-azure-gpu.yaml
----

. Update the following fields in `machineset-azure-gpu.yaml`:
+
* Change `.metadata.name` to a name containing `gpu`.

* Change `.spec.selector.matchLabels["machine.openshift.io/cluster-api-machineset"]` to match the new .metadata.name.

* Change `.spec.template.metadata.labels["machine.openshift.io/cluster-api-machineset"]` to match the new `.metadata.name`.

* Change `.spec.template.spec.providerSpec.value.vmSize` to `Standard_NC4as_T4_v3`.
+
.Example `machineset-azure-gpu.yaml` file
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  annotations:
    machine.openshift.io/GPU: "1"
    machine.openshift.io/memoryMb: "28672"
    machine.openshift.io/vCPU: "4"
  creationTimestamp: "2023-02-06T20:27:12Z"
  generation: 1
  labels:
    machine.openshift.io/cluster-api-cluster: myclustername
    machine.openshift.io/cluster-api-machine-role: worker
    machine.openshift.io/cluster-api-machine-type: worker
  name: myclustername-nc4ast4-gpu-worker-centralus1
  namespace: openshift-machine-api
  resourceVersion: "166285"
  uid: 4eedce7f-6a57-4abe-b529-031140f02ffa
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: myclustername
      machine.openshift.io/cluster-api-machineset: myclustername-nc4ast4-gpu-worker-centralus1
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: myclustername
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: myclustername-nc4ast4-gpu-worker-centralus1
    spec:
      lifecycleHooks: {}
      metadata: {}
      providerSpec:
        value:
          acceleratedNetworking: true
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          diagnostics: {}
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/myclustername-rg/providers/Microsoft.Compute/galleries/gallery_myclustername_n6n4r/images/myclustername-gen2/versions/latest
            sku: ""
            version: ""
          kind: AzureMachineProviderSpec
          location: centralus
          managedIdentity: myclustername-identity
          metadata:
            creationTimestamp: null
          networkResourceGroup: myclustername-rg
          osDisk:
            diskSettings: {}
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Linux
          publicIP: false
          publicLoadBalancer: myclustername
          resourceGroup: myclustername-rg
          spotVMOptions: {}
          subnet: myclustername-worker-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_NC4as_T4_v3
          vnet: myclustername-vnet
          zone: "1"
status:
  availableReplicas: 1
  fullyLabeledReplicas: 1
  observedGeneration: 1
  readyReplicas: 1
  replicas: 1
----

. To verify your changes, perform a `diff` of the original compute definition and the new GPU-enabled node definition by running the following command:
+
[source,terminal]
----
$ diff machineset-azure.yaml machineset-azure-gpu.yaml
----
+
.Example output
[source,terminal]
----
14c14
<   name: myclustername-worker-centralus1
---
>   name: myclustername-nc4ast4-gpu-worker-centralus1
23c23
<       machine.openshift.io/cluster-api-machineset: myclustername-worker-centralus1
---
>       machine.openshift.io/cluster-api-machineset: myclustername-nc4ast4-gpu-worker-centralus1
30c30
<         machine.openshift.io/cluster-api-machineset: myclustername-worker-centralus1
---
>         machine.openshift.io/cluster-api-machineset: myclustername-nc4ast4-gpu-worker-centralus1
67c67
<           vmSize: Standard_D4s_v3
---
>           vmSize: Standard_NC4as_T4_v3
----

. Create the GPU-enabled compute machine set from the definition file by running the following command:
+
[source,terminal]
----
$ oc create -f machineset-azure-gpu.yaml
----
+
.Example output
+
[source,terminal]
----
machineset.machine.openshift.io/myclustername-nc4ast4-gpu-worker-centralus1 created
----

. View the machines and machine sets that exist in the `openshift-machine-api` namespace by running the following command. Each compute machine set is associated with a different availability zone within the {azure-full} region. The installation program automatically load balances compute machines across availability zones.
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
+
[source,terminal]
----
NAME                                               DESIRED   CURRENT   READY   AVAILABLE   AGE
clustername-n6n4r-nc4ast4-gpu-worker-centralus1    1         1         1       1           122m
clustername-n6n4r-worker-centralus1                1         1         1       1           8h
clustername-n6n4r-worker-centralus2                1         1         1       1           8h
clustername-n6n4r-worker-centralus3                1         1         1       1           8h
----

. View the machines that exist in the `openshift-machine-api` namespace by running the following command. You can only configure one compute machine per set, although you can scale a compute machine set to add a node in a particular region and zone.
+
[source,terminal]
----
$ oc get machines -n openshift-machine-api
----
+
.Example output
+
[source,terminal]
----
NAME                                                PHASE     TYPE                   REGION      ZONE   AGE
myclustername-master-0                              Running   Standard_D8s_v3        centralus   2      6h40m
myclustername-master-1                              Running   Standard_D8s_v3        centralus   1      6h40m
myclustername-master-2                              Running   Standard_D8s_v3        centralus   3      6h40m
myclustername-nc4ast4-gpu-worker-centralus1-w9bqn   Running      centralus   1      21m
myclustername-worker-centralus1-rbh6b               Running   Standard_D4s_v3        centralus   1      6h38m
myclustername-worker-centralus2-dbz7w               Running   Standard_D4s_v3        centralus   2      6h38m
myclustername-worker-centralus3-p9b8c               Running   Standard_D4s_v3        centralus   3      6h38m
----

. View the existing nodes, machines, and machine sets by running the following command. Note that each node is an instance of a machine definition with a specific Azure region and OpenShift Container Platform role.
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
NAME                                                STATUS   ROLES                  AGE     VERSION
myclustername-master-0                              Ready    control-plane,master   6h39m   v1.35.4
myclustername-master-1                              Ready    control-plane,master   6h41m   v1.35.4
myclustername-master-2                              Ready    control-plane,master   6h39m   v1.35.4
myclustername-nc4ast4-gpu-worker-centralus1-w9bqn   Ready    worker                 14m     v1.35.4
myclustername-worker-centralus1-rbh6b               Ready    worker                 6h29m   v1.35.4
myclustername-worker-centralus2-dbz7w               Ready    worker                 6h29m   v1.35.4
myclustername-worker-centralus3-p9b8c               Ready    worker                 6h31m   v1.35.4
----

. View the list of compute machine sets:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
+
[source,terminal]
----
NAME                                   DESIRED   CURRENT   READY   AVAILABLE   AGE
myclustername-worker-centralus1        1         1         1       1           8h
myclustername-worker-centralus2        1         1         1       1           8h
myclustername-worker-centralus3        1         1         1       1           8h
----

. Create the GPU-enabled compute machine set from the definition file by running the following command:
+
[source,terminal]
----
$ oc create -f machineset-azure-gpu.yaml
----

. View the list of compute machine sets:
+
[source,terminal]
----
oc get machineset -n openshift-machine-api
----
+
.Example output
+
[source,terminal]
----
NAME                                          DESIRED   CURRENT   READY   AVAILABLE   AGE
myclustername-nc4ast4-gpu-worker-centralus1   1         1         1       1           121m
myclustername-worker-centralus1               1         1         1       1           8h
myclustername-worker-centralus2               1         1         1       1           8h
myclustername-worker-centralus3               1         1         1       1           8h
----

.Verification

. View the machine set you created by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api | grep gpu
----
+
The MachineSet replica count is set to `1` so a new `Machine` object is created automatically.
+
.Example output
+
[source,terminal]
----
myclustername-nc4ast4-gpu-worker-centralus1   1         1         1       1           121m
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
myclustername-nc4ast4-gpu-worker-centralus1-w9bqn   Running   Standard_NC4as_T4_v3   centralus   1      21m
----

[NOTE]
====
There is no need to specify a namespace for the node. The node definition is cluster scoped.
====

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

[role="_additional-resources"]
.Additional resources
* Enabling Accelerated Networking during installation

// Enabling Accelerated Networking on an existing Microsoft Azure cluster
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.adoc

[id="machineset-azure-enabling-accelerated-networking-existing_{context}"]
= Enabling Accelerated Networking on an existing {azure-full} cluster

[role="_abstract"]
You can enable Accelerated Networking on {azure-full} by adding `acceleratedNetworking` to your machine set YAML file. This uses SR-IOV to help improve network performance for new node.

.Prerequisites

* Have an existing {azure-short} cluster where the Machine API is operational.

.Procedure
//Trying to move towards a more streamlined approach, but leaving this in in case needed
. List the compute machine sets in your cluster by running the following command:
+
[source,terminal]
----
$ oc get machinesets -n openshift-machine-api
----
+
The compute machine sets are listed in the form of `<cluster-id>-worker-<region>`.
+
.Example output
[source,terminal]
----
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
jmywbfb-8zqpx-worker-centralus1     1         1         1       1           15m
jmywbfb-8zqpx-worker-centralus2     1         1         1       1           15m
jmywbfb-8zqpx-worker-centralus3     1         1         1       1           15m
----

. For each compute machine set:

.. Edit the custom resource (CR) by running the following command:
+
[source,terminal]
----
$ oc edit machineset <machine-set-name>
----

.. Add the following to the `providerSpec` field:
* Add the following to the `providerSpec` field:
+
[source,yaml]
----
providerSpec:
  value:
    acceleratedNetworking: true
    vmSize: <azure-vm-size>
----
where:

`providerSpec.value.acceleratedNetworking`:: Enables Accelerated Networking.
`providerSpec.value.vmSize`:: Specifies an {azure-short} VM size that includes at least four vCPUs. For information about VM sizes, see the {azure-full} documentation Sizes for virtual machines in {azure-short}.

.Next steps

* To enable the feature on currently running nodes, you must replace each existing machine. This can be done for each machine individually, or by scaling the replicas down to zero, and then scaling back up to your desired number of replicas.

.Verification

* On the {azure-full} portal, review the *Networking* settings page for a machine provisioned by the machine set, and verify that the `Accelerated networking` field is set to `Enabled`.

[role="_additional-resources"]
.Additional resources
* Manually scaling a compute machine set
