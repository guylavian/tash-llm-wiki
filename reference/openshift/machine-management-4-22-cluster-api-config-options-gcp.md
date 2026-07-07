---
title: "Cluster API configuration options for {gcp-full}"
type: reference
domain: openshift
slug: machine-management-4-22-cluster-api-config-options-gcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cluster-api-config-options-gcp
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Cluster API configuration options for {gcp-full}

[id="cluster-api-config-options-gcp"]
= Cluster API configuration options for {gcp-full}

You can change the configuration of your {gcp-first} Cluster API machines by updating values in the Cluster API custom resource manifests.

[id="cluster-api-sample-yaml-gcp_{context}"]
== Sample YAML for configuring {gcp-full} clusters

The following example YAML files show configurations for a {gcp-full} cluster.

//Sample YAML for CAPI GCP machine template resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-gcp.adoc

[id="capi-yaml-machine-template-gcp_{context}"]
= Sample YAML for a Cluster API machine template resource on {gcp-full}

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates.
The compute machine set references this template when creating machines.

[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: GCPMachineTemplate # <1>
metadata:
  name: <template_name> # <2>
  namespace: openshift-cluster-api
spec:
  template:
    spec: # <3>
      rootDeviceType: pd-ssd
      rootDeviceSize: 128
      instanceType: n1-standard-4
      image: projects/rhcos-cloud/global/images/rhcos-411-85-202203181601-0-gcp-x86-64
      subnet: <cluster_name>-worker-subnet
      serviceAccounts:
        email: <service_account_email_address>
        scopes:
          - https://www.googleapis.com/auth/cloud-platform
      additionalLabels:
        kubernetes-io-cluster-<cluster_name>: owned
      additionalNetworkTags:
        - <cluster_name>-worker
      ipForwarding: Disabled
----
<1> Specify the machine template kind.
This value must match the value for your platform.
<2> Specify a name for the machine template.
<3> Specify the details for your environment.
The values here are examples.

//Sample YAML for a CAPI GCP compute machine set resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-gcp.adoc

[id="capi-yaml-machine-set-gcp_{context}"]
= Sample YAML for a Cluster API compute machine set resource on {gcp-full}

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
        kind: GCPMachineTemplate # <3>
        name: <template_name> # <4>
      failureDomain: <failure_domain> # <5>
----
<1> Specify a name for the compute machine set.
The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.
<2> Specify the cluster ID as the name of the cluster.
<3> Specify the machine template kind.
This value must match the value for your platform.
<4> Specify the machine template name.
<5> Specify the failure domain within the {gcp-short} region.

// [id="cluster-api-supported-features-gcp_{context}"]
// == Enabling {gcp-full} features with the Cluster API

// You can enable the following features by updating values in the Cluster API custom resource manifests.

//Not sure what, if anything, we can add here at this time.
