---
title: "Cluster API configuration options for {azure-full}"
type: reference
domain: openshift
slug: machine-management-4-22-cluster-api-config-options-azure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cluster-api-config-options-azure
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Cluster API configuration options for {azure-full}

[id="cluster-api-config-options-azure"]
= Cluster API configuration options for {azure-full}

You can change the configuration of your {azure-first} Cluster API machines by updating values in the Cluster API custom resource manifests.

[id="cluster-api-sample-yaml-azure_{context}"]
== Sample YAML for configuring {azure-full} clusters

The following example YAML files show configurations for an {azure-short} cluster.

//Sample YAML for CAPI Azure machine template resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-azure.adoc

[id="capi-yaml-machine-template-azure_{context}"]
= Sample YAML for a Cluster API machine template resource on {azure-full}

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates.
The compute machine set references this template when creating machines.

[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AzureMachineTemplate # <1>
metadata:
  name: <template_name> # <2>
  namespace: openshift-cluster-api
spec:
  template:
    spec: # <3>
      disableExtensionOperations: true
      identity: UserAssigned
      image:
        id: /subscriptions/<subscription_id>/resourceGroups/<cluster_name>-rg/providers/Microsoft.Compute/galleries/gallery_<compliant_cluster_name>/images/<cluster_name>-gen2/versions/latest # <4>
      networkInterfaces:
        - acceleratedNetworking: true
          privateIPConfigs: 1
          subnetName: <cluster_name>-worker-subnet
      osDisk:
        diskSizeGB: 128
        managedDisk:
          storageAccountType: Premium_LRS
        osType: Linux
      sshPublicKey: <ssh_key_value>
      userAssignedIdentities:
        - providerID: 'azure:///subscriptions/<subscription_id>/resourcegroups/<cluster_name>-rg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<cluster_name>-identity'
      vmSize: Standard_D4s_v3
----
<1> Specify the machine template kind.
This value must match the value for your platform.
<2> Specify a name for the machine template.
<3> Specify the details for your environment.
The values here are examples.
<4> Specify an image that is compatible with your instance type.
The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix.
+
[NOTE]
====
Default OpenShift Container Platform cluster names contain hyphens (`-`), which are not compatible with {azure-short} gallery name requirements.
The value of `<compliant_cluster_name>` in this configuration must use underscores (`_`) instead of hyphens to comply with these requirements.
Other instances of `<cluster_name>` do not change.

For example, a cluster name of `jdoe-test-2m2np` transforms to `jdoe_test_2m2np`.
The full string for `gallery_<compliant_cluster_name>` in this example is `gallery_jdoe_test_2m2np`, not `gallery_jdoe-test-2m2np`.
The complete value of `spec.template.spec.image.id` for this example value is `/subscriptions/<subscription_id>/resourceGroups/jdoe-test-2m2np-rg/providers/Microsoft.Compute/galleries/gallery_jdoe_test_2m2np/images/jdoe-test-2m2np-gen2/versions/latest`.
====

//Sample YAML for a CAPI Azure compute machine set resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-azure.adoc

[id="capi-yaml-machine-set-azure_{context}"]
= Sample YAML for a Cluster API compute machine set resource on {azure-full}

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
  clusterName: <cluster_name>
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
        kind: AzureMachineTemplate # <3>
        name: <template_name> # <4>
----
<1> Specify a name for the compute machine set.
The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.
<2> Specify the cluster ID as the name of the cluster.
<3> Specify the machine template kind.
This value must match the value for your platform.
<4> Specify the machine template name.

// [id="cluster-api-supported-features-azure_{context}"]
// == Enabling {azure-full} features with the Cluster API

// You can enable the following features by updating values in the Cluster API custom resource manifests.

//Not sure what, if anything, we can add here at this time.
