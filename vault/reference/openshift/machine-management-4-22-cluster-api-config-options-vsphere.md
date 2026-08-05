---
title: "Cluster API configuration options for VMware vSphere"
type: reference
domain: openshift
slug: machine-management-4-22-cluster-api-config-options-vsphere
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cluster-api-config-options-vsphere
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Cluster API configuration options for VMware vSphere

[id="cluster-api-config-options-vsphere"]
= Cluster API configuration options for VMware vSphere

You can change the configuration of your {vmw-first} Cluster API machines by updating values in the Cluster API custom resource manifests.

[id="cluster-api-sample-yaml-vsphere_{context}"]
== Sample YAML for configuring {vmw-full} clusters

The following example YAML files show configurations for a {vmw-full} cluster.

//Sample YAML for CAPI vSphere machine template resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-vsphere.adoc

[id="capi-yaml-machine-template-vsphere_{context}"]
= Sample YAML for a Cluster API machine template resource on {vmw-full}

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates.
The compute machine set references this template when creating machines.

[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: VSphereMachineTemplate # <1>
metadata:
  name: <template_name> # <2>
  namespace: openshift-cluster-api
spec:
  template:
    spec: # <3>
      template: <vm_template_name> # <4>
      server: <vcenter_server_ip> # <5>
      diskGiB: 128
      cloneMode: linkedClone # <6>
      datacenter: <vcenter_data_center_name> # <7>
      datastore: <vcenter_datastore_name> # <8>
      folder: <vcenter_vm_folder_path> # <9>
      resourcePool: <vsphere_resource_pool> # <10>
      numCPUs: 4
      memoryMiB: 16384
      network:
        devices:
        - dhcp4: true
          networkName: "<vm_network_name>" # <11>
----
<1> Specify the machine template kind.
This value must match the value for your platform.
<2> Specify a name for the machine template.
<3> Specify the details for your environment.
The values here are examples.
<4> Specify the vSphere VM template to use, such as `user-5ddjd-rhcos`.
<5> Specify the vCenter server IP or fully qualified domain name.
<6> Specify the type of VM clone to use.
The following values are valid:
+
--
* `fullClone`
* `linkedClone`
--
+
When using the `linkedClone` type, the disk size matches the clone source instead of using the `diskGiB` value.
For more information, see the {vmw-short} documentation about VM clone types.
<7> Specify the vCenter data center to deploy the compute machine set on.
<8> Specify the vCenter datastore to deploy the compute machine set on.
<9> Specify the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.
<10> Specify the vSphere resource pool for your VMs.
<11> Specify the vSphere VM network to deploy the compute machine set to.
This VM network must be where other compute machines reside in the cluster.

//Sample YAML for a CAPI vSphere compute machine set resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-vsphere.adoc

[id="capi-yaml-machine-set-vsphere_{context}"]
= Sample YAML for a Cluster API compute machine set resource on {vmw-full}

The compute machine set resource defines additional properties of the machines that it creates.
The compute machine set also references the cluster resource and machine template when creating machines.

[source,yaml]
----
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name> # <1>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name> # <2>
spec:
  clusterName: <cluster_name> # <2>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: VSphereMachineTemplate # <3>
        name: <template_name> # <4>
      failureDomain: # <5>
        - name: <failure_domain_name>
          region: <region_a>
          zone: <zone_a>
          server: <vcenter_server_name>
          topology:
            datacenter: <region_a_data_center>
            computeCluster: "</region_a_data_center/host/zone_a_cluster>"
            resourcePool: "</region_a_data_center/host/zone_a_cluster/Resources/resource_pool>"
            datastore: "</region_a_data_center/datastore/datastore_a>"
            networks:
            - port-group
----
<1> Specify a name for the compute machine set.
The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.
<2> Specify the cluster ID as the name of the cluster.
<3> Specify the machine template kind.
This value must match the value for your platform.
<4> Specify the machine template name.
<5> Specify the failure domain configuration details.
+
[NOTE]
====
Using multiple regions and zones on a {vmw-short} cluster that uses the Cluster API is not a validated configuration.
====
// This callout section can be updated if this configuration is validated. (see also: additional resources in cluster-api-config-options-vsphere.adoc)
// <5> Specify one or more failure domains.
// For more information about specifying multiple regions and zones on a {vmw-short} cluster, see "Multiple regions and zones configuration for a cluster on {vmw-full}."

// This additional resources section can be added if this configuration is validated. (see also: callout in capi-yaml-machine-set-vsphere.adoc)
// [role="_additional-resources"]
// .Additional resources
// * Multiple regions and zones configuration for a cluster on {vmw-full}

// [id="cluster-api-supported-features-vsphere_{context}"]
// == Enabling {vmw-full} features with the Cluster API

// You can enable the following features by updating values in the Cluster API custom resource manifests.

//Not sure what, if anything, we can add here at this time.
