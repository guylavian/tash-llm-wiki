---
title: "Control plane configuration options for Nutanix"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-config-options-nutanix
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-config-options-nutanix
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Control plane configuration options for Nutanix

[id="cpmso-config-options-nutanix"]
= Control plane configuration options for Nutanix

[role="_abstract"]
You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for a Nutanix cluster.

//Sample Nutanix provider specification
// Module included in the following assemblies:
//
// * machine_management/cpmso-configuration.adoc

[id="cpmso-yaml-provider-spec-nutanix_{context}"]
= Sample Nutanix provider specification

[role="_abstract"]
You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for a Nutanix cluster.

.Sample Nutanix `providerSpec` values
[source,yaml]
----
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
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
              name: <cluster_id>-rhcos
              type: name
            kind: NutanixMachineProviderConfig
            memorySize: 16Gi
            metadata:
              creationTimestamp: null
            project:
              type: name
              name: <project_name>
            subnets:
            - type: uuid
              uuid: <subnet_uuid>
            systemDiskSize: 120Gi
            userDataSecret:
              name: master-user-data
            vcpuSockets: 8
            vcpusPerSocket: 1
----
where:

`spec.template.spec.providerSpec.value.bootType`::
Specifies the boot type that the control plane machines use.
For more information about boot types, see Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment (Nutanix documentation).
+
Valid values are `Legacy`, `SecureBoot`, or `UEFI`.
The default is `Legacy`.
+
[NOTE]
====
You must use the `Legacy` boot type in OpenShift Container Platform .
====

`spec.template.spec.providerSpec.value.categories`::
Specifies one or more Nutanix Prism categories to apply to control plane machines.
This stanza requires `key` and `value` parameters for a category key-value pair that exists in Prism Central.
For more information about categories, see Category management.

`spec.template.spec.providerSpec.value.cluster`::
Specifies a Nutanix Prism Element cluster configuration.
In this example, the cluster type is `uuid`, so there is a `uuid` stanza.
+
[NOTE]
====
====

`spec.template.spec.providerSpec.value.credentialsSecret`::
Specifies the secret name for the cluster.
Do not change this value.

`spec.template.spec.providerSpec.value.image`::
Specifies the path to the source image for the disk.

`spec.template.spec.providerSpec.value.kind`::
Specifies the cloud provider platform type.
Do not change this value.

`spec.template.spec.providerSpec.value.memorySize`::
Specifies the memory allocated for the control plane machines.

`spec.template.spec.providerSpec.value.project`::
Specifies the Nutanix project that you use for your cluster.
In this example, the project type is `name`, so there is a `name` stanza.

`spec.template.spec.providerSpec.value.subnets`::
Specify one or more Prism Element subnet objects.
In this example, the subnet type is `uuid`, so there is a `uuid` stanza.
A maximum of 32 subnets for each Prism Element failure domain in the cluster is supported.
+
[IMPORTANT]
====
Do not remove the original subnet, which hosts the API server and ingress server, from the cluster.
====
+
The CIDR IP address prefix for one of the specified subnets must contain the virtual IP addresses that the OpenShift Container Platform cluster uses.
All subnet UUID values must be unique.
+
[NOTE]
====
====

`spec.template.spec.providerSpec.value.systemDiskSize`::
Specifies the VM disk size for the control plane machines.

`spec.template.spec.providerSpec.value.userDataSecret`::
Specifies the control plane user data secret.
Do not change this value.

`spec.template.spec.providerSpec.value.vcpuSockets`::
Specifies the number of vCPU sockets allocated for the control plane machines.

`spec.template.spec.providerSpec.value.vcpusPerSocket`::
Specifies the number of vCPUs for each control plane vCPU socket.

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

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources
* Updating the control plane configuration
* Adding failure domains to an existing Nutanix cluster
