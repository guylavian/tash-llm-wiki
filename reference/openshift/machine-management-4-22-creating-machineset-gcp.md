---
title: "Creating a compute machine set on {gcp-short}"
type: reference
domain: openshift
slug: machine-management-4-22-creating-machineset-gcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-machineset-gcp
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Creating a compute machine set on {gcp-short}

[id="creating-machineset-gcp"]
= Creating a compute machine set on {gcp-short}

[role="_abstract"]
You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on {gcp-first}. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

//[IMPORTANT] admonition for UPI

//Sample YAML for a compute machine set custom resource on GCP
// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * machine_management/creating-machineset-gcp.adoc

[id="machineset-yaml-gcp_{context}"]
=  Sample YAML for a compute machine set custom resource on {gcp-short}

[role="_abstract"]
The sample YAML defines a compute machine set for {gcp-first}, enabling the automated provisioning of nodes within a specific VPC. When you apply this configuration by using the OpenShift Container Platform CLI, you can ensure consistent scaling, scheduling, and infrastructure ID labeling for compute resources in your cluster.

The sample YAML defines a compute machine set that runs in {gcp-full} and creates nodes that are labeled with
where
is the node label to add.

[id="cpmso-yaml-provider-spec-gcp-oc_{context}"]
== Values obtained by using the  OpenShift CLI

In the following example, you can obtain some of the values for your cluster by using the OpenShift Container Platform CLI.

Infrastructure ID:: The `<infrastructure_id>` string is the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----

Image path:: The `<path_to_image>` string is the path to the image that was used to create the disk. If you have the OpenShift CLI installed, you can obtain the path to the image by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api \
  -o jsonpath='{.spec.template.spec.providerSpec.value.disks[0].image}{"\n"}' \
  get machineset/<infrastructure_id>-worker-a
----

.Sample {gcp-short} `MachineSet` values
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-w-a
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-w-a
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-w-a
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          canIPForward: false
          credentialsSecret:
            name: gcp-cloud-credentials
          deletionProtection: false
          disks:
          - autoDelete: true
            boot: true
            image: <path_to_image>
            labels: null
            sizeGb: 128
            type: pd-ssd
          gcpMetadata:
          - key: <custom_metadata_key>
            value: <custom_metadata_value>
          kind: GCPMachineProviderSpec
          machineType: n1-standard-4
          metadata:
            creationTimestamp: null
          networkInterfaces:
          - network: <infrastructure_id>-network
            subnetwork: <infrastructure_id>-worker-subnet
          projectID: <project_name>
          region: us-central1
          serviceAccounts:
          - email: <infrastructure_id>-w@<project_name>.iam.gserviceaccount.com
            scopes:
            - https://www.googleapis.com/auth/cloud-platform
          tags:
            - <infrastructure_id>-worker
          userDataSecret:
            name: worker-user-data
          zone: us-central1-a
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
----

where:

`<infrastructure_id>`:: Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster.
`<role>`:: Specifies the node label to add.
`<infra>`:: Specifies the `<infra>` node label.
`<path_to_image>`:: Specifies the path to the image that is used as a boot image in current compute machine sets. You should use the use the latest image when adding a new machine set. To use a {gcp-short} Marketplace image, specify the offer to use:
+
* OpenShift Container Platform: `\https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-ocp-413-x86-64-202305021736`
* {opp}: `\https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-opp-413-x86-64-202305021736`
* {oke}: `\https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-oke-413-x86-64-202305021736`

`<gcpMetadata>`:: Optional: Specifies the custom metadata in the form of a `key:value` pair. For example use cases, see the {gcp-short} documentation for setting custom metadata.
`<project_name>`:: Specifies the name of the {gcp-short} project that you use for your cluster.
`<serviceAccounts>`:: Specifies a single service account. Multiple service accounts are not supported.
`<taints>`:: Specifies a taint to prevent user workloads from being scheduled on infra nodes.

[NOTE]
====
After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or add toleration on `misscheduled` DNS pods.
====

Machine sets running on {gcp-short} support non-guaranteed preemptible VM instances. You can save on costs by using preemptible VM instances at a lower price compared to normal instances on {gcp-short}. You can configure preemptible VM instances by adding `preemptible` to the `MachineSet` YAML file.

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

//Configuring persistent disk types by using compute machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-gcp.adoc

[id="machineset-gcp-pd-disk-types_{context}"]
= Configuring persistent disk types by using machine sets

[role="_abstract"]
Configure the persistent disk type for your machine set on {gcp-first} to match your workload requirements. Editing the `MachineSet` YAML file allows you to choose between standard, balanced, or SSD persistent disks.

For more information about persistent disk types, compatibility, regional availability, and limitations, see the {gcp-short} Compute Engine documentation about persistent disks.

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following line under the `providerSpec` field:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
...
spec:
  template:
    spec:
      providerSpec:
        value:
          disks:
            type: <pd-disk-type>
            type: pd-ssd
----

+
where:
+
--
`spec.template.spec.providerSpec.value.disks.type`:: Specifies the persistent disk type. Valid values are `pd-ssd`, `pd-standard`, and `pd-balanced`. The default value is `pd-standard`.
--
+
where:
+
--
`spec.template.spec.providerSpec.value.disks.type`:: Uses the `pd-ssd` disk type for control plane nodes. Using the `pd-ssd` disk type is required for control plane nodes.
--

.Verification

* Using the {gcp-full} console, review the details for a machine deployed by the machine set and verify that the `Type` field matches the configured disk type.

//Configuring Confidential VM by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-gcp.adoc

[id="machineset-gcp-confidential-vm_{context}"]
= Configuring Confidential VM by using machine sets

[role="_abstract"]
You create machine sets to scale clusters on {gcp-first}. By editing the machine set YAML file, you can configure the Confidential VM options that a machine set uses for machines that it deploys.

For more information about Confidential VM features, functions, and compatibility, see the {gcp-short} Compute Engine documentation about Confidential VM.

[NOTE]
====
Confidential VMs are currently not supported on 64-bit ARM architectures.
If you use Confidential VM, you must ensure that you select a supported region. For details on supported regions and configurations, see the {gcp-short} Compute Engine documentation about supported zones.
====

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following section under the `providerSpec` field:
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
        value:
          confidentialCompute: Enabled
          onHostMaintenance: Terminate
          machineType: n2d-standard-8
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            confidentialCompute: Enabled
            onHostMaintenance: Terminate
            machineType: n2d-standard-8
# ...
----
+
where:
+
`spec.template.spec.providerSpec.value.confidentialCompute`:: Specifies whether Confidential VM is enabled.
The following values are valid:
`Enabled`:: Enables Confidential VM with a default selection of Confidential VM technology. The default selection is AMD Secure Encrypted Virtualization (AMD SEV).
+
[IMPORTANT]
====
The `Enabled` value selects Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV), which is deprecated.
====
`Disabled`:: Disables Confidential VM.
`AMDEncryptedVirtualizationNestedPaging`:: Enables Confidential VM using AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). AMD SEV-SNP supports n2d machines.
`AMDEncryptedVirtualization`:: Enables Confidential VM using AMD SEV. AMD SEV supports c2d, n2d, and c3d machines.
+
[IMPORTANT]
====
The use of Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV) has been deprecated and will be removed in a future release.
====

`IntelTrustedDomainExtensions`:: Enables Confidential VM using Intel Trusted Domain Extensions (Intel TDX). Intel TDX supports n2d machines.

`spec.template.spec.providerSpec.value.onHostMaintenance`:: Specifies the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VM does not support live VM migration.
`spec.template.spec.providerSpec.value.machineType`:: Specifies a machine type that supports the Confidential VM option that you specified in the `confidentialCompute` field.

`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.confidentialCompute`:: Specifies whether Confidential VM is enabled.
The following values are valid:
`Enabled`:: Enables Confidential VM with a default selection of Confidential VM technology. The default selection is AMD Secure Encrypted Virtualization (AMD SEV).
+
[IMPORTANT]
====
The `Enabled` value selects Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV), which is deprecated.
====
`Disabled`:: Disables Confidential VM.
`AMDEncryptedVirtualizationNestedPaging`:: Enables Confidential VM using AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). AMD SEV-SNP supports n2d machines.
`AMDEncryptedVirtualization`:: Enables Confidential VM using AMD SEV. AMD SEV supports c2d, n2d, and c3d machines.
+
[IMPORTANT]
====
The use of Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV) has been deprecated and will be removed in a future release.
====

`IntelTrustedDomainExtensions`:: Enables Confidential VM using Intel Trusted Domain Extensions (Intel TDX). Intel TDX supports n2d machines.

`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.onHostMaintenance`:: Specifies the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VM does not support live VM migration.
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.machineType`:: Specifies a machine type that supports the Confidential VM option that you specified in the `confidentialCompute` field.

.Verification

* On the {gcp-full} console, review the details for a machine deployed by the machine set and verify that the Confidential VM options match the values that you configured.

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

//Module is reused a second time for legacy option and gets new context, which is reset after this feature
//Machine sets that deploy machines as preemptible VM instances

//Creating preemptible VM instances by using compute machine sets

//Configuring Shielded VM options by using machine sets
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-gcp.adoc

[id="machineset-gcp-shielded-vms_{context}"]
= Configuring Shielded VM options by using machine sets

[role="_abstract"]
Configure Shielded Virtual Machine (VM) options for your machine sets on {gcp-first} to help secure your cluster instances. By editing the `MachineSet` YAML file, you can configure the Shielded VM options that a machine set uses for machines that it deploys.

For more information about Shielded VM features and functionality, see the {gcp-short} Compute Engine documentation about Shielded VM.

.Procedure

. In a text editor, open the YAML file for an existing machine set or create a new one.

. Edit the following section under the `providerSpec` field:
+
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
          shieldedInstanceConfig:
            integrityMonitoring: Enabled
            secureBoot: Disabled
            virtualizedTrustedPlatformModule: Enabled
# ...
----
+
where:
+
--
`spec.template.spec.providerSpec.value.shieldedInstanceConfig`:: Specifies the Shielded VM configuration.
`spec.template.spec.providerSpec.value.shieldedInstanceConfig`:: Specifies the Shielded VM configuration.
`spec.template.spec.providerSpec.value.shieldedInstanceConfig.integrityMonitoring`:: Specifies whether integrity monitoring is enabled. Valid values are `Disabled` or `Enabled`.
+
[NOTE]
====
When integrity monitoring is enabled, you must not disable virtual trusted platform module (vTPM).
====
`spec.template.spec.providerSpec.value.shieldedInstanceConfig.secureBoot`:: Specifies whether UEFI Secure Boot is enabled. Valid values are `Disabled` or `Enabled`.
`spec.template.spec.providerSpec.value.shieldedInstanceConfig.virtualizedTrustedPlatformModule`:: Specifies whether vTPM is enabled. Valid values are `Disabled` or `Enabled`.
--

.Verification

* Using the {gcp-full} console, review the details for a machine deployed by the machine set and verify that the Shielded VM options match the values that you configured.

[role="_additional-resources"]
.Additional resources
* What is Shielded VM?
* Secure Boot
* Virtual Trusted Platform Module (vTPM)
* Integrity monitoring

//Enabling customer-managed encryption keys for a compute machine set

// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-gcp.adoc

[id="machineset-gcp-enabling-customer-managed-encryption_{context}"]
= Enabling customer-managed encryption keys for a machine set

[role="_abstract"]
Use {gcp-first} Compute Engine to supply an encryption key to encrypt data on disks at rest. The key is used to encrypt the data encryption key, not to encrypt the customer's data. By default, Compute Engine encrypts this data by using Compute Engine keys.

You can enable encryption with a customer-managed key in clusters that use the Machine API. You must first create a KMS key and assign the correct permissions to a service account. The KMS key name, key ring name, and location are required to allow a service account to use your key.

[NOTE]
====
If you do not want to use a dedicated service account for the KMS encryption, the Compute Engine default service account is used instead. You must grant the default service account permission to access the keys if you do not use a dedicated service account. The Compute Engine default service account name follows the `service-<project_number>@compute-system.iam.gserviceaccount.com` pattern.
====

.Procedure

. To allow a specific service account to use your KMS key and to grant the service account the correct IAM role, run the following command with your KMS key name, key ring name, and location:
+
[source,terminal]
----
$ gcloud kms keys add-iam-policy-binding <key_name> \
  --keyring <key_ring_name> \
  --location <key_ring_location> \
  --member "serviceAccount:service-<project_number>@compute-system.iam.gserviceaccount.com” \
  --role roles/cloudkms.cryptoKeyEncrypterDecrypter
----

. Configure the encryption key under the `providerSpec` field in your machine set YAML file. For example:
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
...
spec:
  template:
    spec:
      providerSpec:
        value:
          disks:
          - type:
            encryptionKey:
              kmsKey:
                name: machine-encryption-key
                keyRing: openshift-encryption-ring
                location: global
                projectID: openshift-gcp-project
              kmsKeyServiceAccount: openshift-service-account@openshift-gcp-project.iam.gserviceaccount.com
----
+
where:
+
--
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.name`:: Specifies the name of the customer-managed encryption key that is used for the disk encryption.
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.keyRing`:: Specifies the name of the KMS key ring that the KMS key belongs to.
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.location`:: Specifies the {gcp-short} location in which the KMS key ring exists.
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.projectID`:: Optional: Specifies the ID of the project in which the KMS key ring exists. If a project ID is not set, the machine set `projectID` in which the machine set was created is used.
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKeyServiceAccount`:: Optional: Specifies the service account that is used for the encryption request for the given KMS key. If a service account is not set, the Compute Engine default service account is used.
+
When a new machine is created by using the updated `providerSpec` object configuration, the disk encryption key is encrypted with the KMS key.
--

//Enabling GPU support for a compute machine set
// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc

[id="machineset-gcp-enabling-gpu-support_{context}"]
= Enabling GPU support for a compute machine set

[role="_abstract"]
Use the {gcp-first} Compute Engine to add GPUs to Virtual Machine (VM) instances. Workloads that benefit from access to GPU resources can perform better on compute machines with this feature enabled. OpenShift Container Platform on {gcp-short} supports NVIDIA GPU models in the A2 and N1 machine series.

.Supported GPU configurations
|====
|Model name |GPU type |Machine types ^[1]^

|NVIDIA A100
|`nvidia-tesla-a100`
a|* `a2-highgpu-1g`
* `a2-highgpu-2g`
* `a2-highgpu-4g`
* `a2-highgpu-8g`
* `a2-megagpu-16g`

|NVIDIA K80
|`nvidia-tesla-k80`
.5+a|* `n1-standard-1`
* `n1-standard-2`
* `n1-standard-4`
* `n1-standard-8`
* `n1-standard-16`
* `n1-standard-32`
* `n1-standard-64`
* `n1-standard-96`
* `n1-highmem-2`
* `n1-highmem-4`
* `n1-highmem-8`
* `n1-highmem-16`
* `n1-highmem-32`
* `n1-highmem-64`
* `n1-highmem-96`
* `n1-highcpu-2`
* `n1-highcpu-4`
* `n1-highcpu-8`
* `n1-highcpu-16`
* `n1-highcpu-32`
* `n1-highcpu-64`
* `n1-highcpu-96`

|NVIDIA P100
|`nvidia-tesla-p100`

|NVIDIA P4
|`nvidia-tesla-p4`

|NVIDIA T4
|`nvidia-tesla-t4`

|NVIDIA V100
|`nvidia-tesla-v100`

|====
[.small]
--
1. For more information about machine types, including specifications, compatibility, regional availability, and limitations, see the {gcp-short} Compute Engine documentation about N1 machine series, A2 machine series, and GPU regions and zones availability.
--

You can define which supported GPU to use for an instance by using the Machine API.

You can configure machines in the N1 machine series to deploy with one of the supported GPU types. Machines in the A2 machine series come with associated GPUs, and cannot use guest accelerators.

[NOTE]
====
GPUs for graphics workloads are not supported.
====

.Procedure

. In a text editor, open the YAML file for an existing compute machine set or create a new one.

. Specify a GPU configuration under the `providerSpec` field in your compute machine set YAML file. See the following examples of valid configurations:
+
.Example configuration for the A2 machine series
[source,yaml]
----
  providerSpec:
    value:
      machineType: a2-highgpu-1g
      onHostMaintenance: Terminate
      restartPolicy: Always
----
+
where
+
--
`spec.template.spec.providerSpec.value.machineType`:: Specifies the machine type. Ensure that the machine type is included in the A2 machine series.
`spec.template.spec.providerSpec.value.onHostMaintenance`:: Sets `onHostMaintenance` to `Terminate`. When using GPU support, you must set `onHostMaintenance` to `Terminate`.
`spec.template.spec.providerSpec.value.restartPolicy`:: Specifies the restart policy for machines deployed by the compute machine set. The allowed values are `Always` or `Never`.
--
+
.Example configuration for the N1 machine series
[source,yaml]
----
providerSpec:
  value:
    gpus:
    - count: 1
      type: nvidia-tesla-p100
    machineType: n1-standard-1
    onHostMaintenance: Terminate
    restartPolicy: Always
----
+
where
+
--
`spec.template.spec.providerSpec.value.gpus.count`:: Specifies the number of GPUs to attach to the machine.
`spec.template.spec.providerSpec.value.gpus.type`:: Specifies the type of GPUs to attach to the machine. Ensure that the machine type and GPU type are compatible.
`spec.template.spec.providerSpec.value.machineType`:: Specifies the machine type. Ensure that the machine type and GPU type are compatible.
`spec.template.spec.providerSpec.value.onHostMaintenance`:: Sets `onHostMaintenance` to `Terminate`. When using GPU support, you must set `onHostMaintenance` to `Terminate`.
`spec.template.spec.providerSpec.value.restartPolicy`:: Specifies the restart policy for machines deployed by the compute machine set. The allowed values are `Always` or `Never`.
--

//Adding a GPU node to a machine set (stesmith)
// Module included in the following assemblies:
//
//  * machine_management/creating-machinesets/creating-machineset-aws.adoc

[id="nvidia-gpu-gcp-adding-a-gpu-node_{context}"]
= Adding a GPU node to an existing OpenShift Container Platform cluster

[role="_abstract"]
You can copy and modify a default compute machine set configuration to create a GPU-enabled machine set and machines for the {gcp-short} provider. This assists compute-intensive workloads that require hardware acceleration.

The following table lists the validated instance types:

[cols="1,1,1,1"]
|===
|Instance type |NVIDIA GPU accelerator |Maximum number of GPUs |Architecture

|`a2-highgpu-1g`
|A100
|1
|x86

|`n1-standard-4`
|T4
|1
|x86
|===

.Procedure

. Make a copy of an existing `MachineSet` configuration.

. In the new copy, change the machine set `name` in `metadata.name` and in both instances of `machine.openshift.io/cluster-api-machineset`.

. Change the instance type to add the following two lines to the newly copied `MachineSet` configuration:
+
----
machineType: a2-highgpu-1g
onHostMaintenance: Terminate
----
+
.Example `a2-highgpu-1g.json` file
+
[source,json]
----
{
    "apiVersion": "machine.openshift.io/v1beta1",
    "kind": "MachineSet",
    "metadata": {
        "annotations": {
            "machine.openshift.io/GPU": "0",
            "machine.openshift.io/memoryMb": "16384",
            "machine.openshift.io/vCPU": "4"
        },
        "creationTimestamp": "2023-01-13T17:11:02Z",
        "generation": 1,
        "labels": {
            "machine.openshift.io/cluster-api-cluster": "myclustername-2pt9p"
        },
        "name": "myclustername-2pt9p-worker-gpu-a",
        "namespace": "openshift-machine-api",
        "resourceVersion": "20185",
        "uid": "2daf4712-733e-4399-b4b4-d43cb1ed32bd"
    },
    "spec": {
        "replicas": 1,
        "selector": {
            "matchLabels": {
                "machine.openshift.io/cluster-api-cluster": "myclustername-2pt9p",
                "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-gpu-a"
            }
        },
        "template": {
            "metadata": {
                "labels": {
                    "machine.openshift.io/cluster-api-cluster": "myclustername-2pt9p",
                    "machine.openshift.io/cluster-api-machine-role": "worker",
                    "machine.openshift.io/cluster-api-machine-type": "worker",
                    "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-gpu-a"
                }
            },
            "spec": {
                "lifecycleHooks": {},
                "metadata": {},
                "providerSpec": {
                    "value": {
                        "apiVersion": "machine.openshift.io/v1beta1",
                        "canIPForward": false,
                        "credentialsSecret": {
                            "name": "gcp-cloud-credentials"
                        },
                        "deletionProtection": false,
                        "disks": [
                            {
                                "autoDelete": true,
                                "boot": true,
                                "image": "projects/rhcos-cloud/global/images/rhcos-412-86-202212081411-0-gcp-x86-64",
                                "labels": null,
                                "sizeGb": 128,
                                "type": "pd-ssd"
                            }
                        ],
                        "kind": "GCPMachineProviderSpec",
                        "machineType": "a2-highgpu-1g",
                        "onHostMaintenance": "Terminate",
                        "metadata": {
                            "creationTimestamp": null
                        },
                        "networkInterfaces": [
                            {
                                "network": "myclustername-2pt9p-network",
                                "subnetwork": "myclustername-2pt9p-worker-subnet"
                            }
                        ],
                        "preemptible": true,
                        "projectID": "myteam",
                        "region": "us-central1",
                        "serviceAccounts": [
                            {
                                "email": "myclustername-2pt9p-w@myteam.iam.gserviceaccount.com",
                                "scopes": [
                                    "https://www.googleapis.com/auth/cloud-platform"
                                ]
                            }
                        ],
                        "tags": [
                            "myclustername-2pt9p-worker"
                        ],
                        "userDataSecret": {
                            "name": "worker-user-data"
                        },
                        "zone": "us-central1-a"
                    }
                }
            }
        }
    },
    "status": {
        "availableReplicas": 1,
        "fullyLabeledReplicas": 1,
        "observedGeneration": 1,
        "readyReplicas": 1,
        "replicas": 1
    }
}
----

. View the existing nodes, machines, and machine sets by running the following command. Note that each node is an instance of a machine definition with a specific {gcp-short} region and OpenShift Container Platform role.
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
NAME                                                             STATUS     ROLES                  AGE     VERSION
myclustername-2pt9p-master-0.c.openshift-qe.internal             Ready      control-plane,master   8h      v1.35.4
myclustername-2pt9p-master-1.c.openshift-qe.internal             Ready      control-plane,master   8h      v1.35.4
myclustername-2pt9p-master-2.c.openshift-qe.internal             Ready      control-plane,master   8h      v1.35.4
myclustername-2pt9p-worker-a-mxtnz.c.openshift-qe.internal       Ready      worker                 8h      v1.35.4
myclustername-2pt9p-worker-b-9pzzn.c.openshift-qe.internal       Ready      worker                 8h      v1.35.4
myclustername-2pt9p-worker-c-6pbg6.c.openshift-qe.internal       Ready      worker                 8h      v1.35.4
myclustername-2pt9p-worker-gpu-a-wxcr6.c.openshift-qe.internal   Ready      worker                 4h35m   v1.35.4
----

. View the machines and machine sets that exist in the `openshift-machine-api` namespace by running the following command. Each compute machine set is associated with a different availability zone within the {gcp-short} region. The installation program automatically load balances compute machines across availability zones.
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
NAME                               DESIRED   CURRENT   READY   AVAILABLE   AGE
myclustername-2pt9p-worker-a       1         1         1       1           8h
myclustername-2pt9p-worker-b       1         1         1       1           8h
myclustername-2pt9p-worker-c       1         1                             8h
myclustername-2pt9p-worker-f       0         0                             8h
----

. View the machines that exist in the `openshift-machine-api` namespace by running the following command. You can only configure one compute machine per set, although you can scale a compute machine set to add a node in a particular region and zone.
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
myclustername-2pt9p-worker-a-mxtnz       Running   n2-standard-4   us-central1   us-central1-a   8h
myclustername-2pt9p-worker-b-9pzzn       Running   n2-standard-4   us-central1   us-central1-b   8h
myclustername-2pt9p-worker-c-6pbg6       Running   n2-standard-4   us-central1   us-central1-c   8h
----

. Make a copy of one of the existing compute `MachineSet` definitions and output the result to a JSON file by running the following command. This will be the basis for the GPU-enabled compute machine set definition.
+
[source,terminal]
----
$ oc get machineset myclustername-2pt9p-worker-a -n openshift-machine-api -o json  > <output_file.json>
----

. Edit the JSON file to make the following changes to the new `MachineSet` definition:
+
* Rename the machine set `name` by inserting the substring `gpu` in `metadata.name` and in both instances of `machine.openshift.io/cluster-api-machineset`.
* Change the `machineType` of the new `MachineSet` definition to `a2-highgpu-1g`, which includes an NVIDIA A100 GPU.
+
[source,terminal,subs="attributes+"]
----
jq .spec.template.spec.providerSpec.value.machineType ocp__machineset-a2-highgpu-1g.json

"a2-highgpu-1g"
----
+
The `<output_file.json>` file is saved as `ocp__machineset-a2-highgpu-1g.json`.

. Update the following fields in `ocp__machineset-a2-highgpu-1g.json`:
+
* Change `.metadata.name` to a name containing `gpu`.

* Change `.spec.selector.matchLabels["machine.openshift.io/cluster-api-machineset"]` to
match the new `.metadata.name`.

* Change `.spec.template.metadata.labels["machine.openshift.io/cluster-api-machineset"]`
to match the new `.metadata.name`.

* Change `.spec.template.spec.providerSpec.value.MachineType` to `a2-highgpu-1g`.

* Add the following line under `machineType`: `"onHostMaintenance": "Terminate". For example:
+
[source,json]
----
"machineType": "a2-highgpu-1g",
"onHostMaintenance": "Terminate",
----

. To verify your changes, perform a `diff` of the original compute definition and the new GPU-enabled node definition by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get machineset/myclustername-2pt9p-worker-a -n openshift-machine-api -o json | diff ocp__machineset-a2-highgpu-1g.json -
----
+
.Example output
+
[source,terminal]
----
15c15
<         "name": "myclustername-2pt9p-worker-gpu-a",
---
>         "name": "myclustername-2pt9p-worker-a",
25c25
<                 "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-gpu-a"
---
>                 "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-a"
34c34
<                     "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-gpu-a"
---
>                     "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-a"
59,60c59
<                         "machineType": "a2-highgpu-1g",
<                         "onHostMaintenance": "Terminate",
---
>                         "machineType": "n2-standard-4",
----

. Create the GPU-enabled compute machine set from the definition file by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f ocp__machineset-a2-highgpu-1g.json
----
+
.Example output
+
[source,terminal]
----
machineset.machine.openshift.io/myclustername-2pt9p-worker-gpu-a created
----

.Verification

. View the machine set you created by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api get machinesets | grep gpu
----
+
The `MachineSet` replica count is set to `1` so a new `Machine` object is created automatically.

+
.Example output
+
[source,terminal]
----
myclustername-2pt9p-worker-gpu-a   1         1         1       1           5h24m
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
myclustername-2pt9p-worker-gpu-a-wxcr6   Running   a2-highgpu-1g   us-central1   us-central1-a   5h25m
----

[NOTE]
====
Note that there is no need to specify a namespace for the node. The node definition is cluster scoped.
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
