---
title: "Cluster API configuration options for Red{nbsp}Hat OpenStack Platform"
type: reference
domain: openshift
slug: machine-management-4-22-cluster-api-config-options-rhosp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cluster-api-config-options-rhosp
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Cluster API configuration options for Red{nbsp}Hat OpenStack Platform

[id="cluster-api-config-options-rhosp"]
= Cluster API configuration options for Red{nbsp}Hat OpenStack Platform

You can change the configuration of your {rh-openstack-first} Cluster API machines by updating values in the Cluster API custom resource manifests.

[id="cluster-api-sample-yaml-rhosp_{context}"]
== Sample YAML for configuring {rh-openstack} clusters

The following example YAML files show configurations for a {rh-openstack} cluster.

//Sample YAML for CAPI RHOSP machine template resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-rhosp.adoc

[id="capi-yaml-machine-template-rhosp_{context}"]
= Sample YAML for a Cluster API machine template resource on {rh-openstack}

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates.
The compute machine set references this template when creating machines.

[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: OpenStackMachineTemplate # <1>
metadata:
  name: <template_name> # <2>
  namespace: openshift-cluster-api
spec:
  template:
    spec: # <3>
      flavor: <openstack_node_machine_flavor> # <4>
      image:
        filter:
          name: <openstack_image> # <5>
----
<1> Specify the machine template kind.
This value must match the value for your platform.
<2> Specify a name for the machine template.
<3> Specify the details for your environment.
The values here are examples.
<4> Specify the {rh-openstack} flavor to use.
For more information, see Creating flavors for launching instances.
<5> Specify the image to use.

//Sample YAML for a CAPI RHOSP compute machine set resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-rhosp.adoc

[id="capi-yaml-machine-set-rhosp_{context}"]
= Sample YAML for a Cluster API compute machine set resource on {rh-openstack}

The compute machine set resource defines additional properties of the machines that it creates.
The compute machine set also references the infrastructure resource and machine template when creating machines.

[source,yaml]
----
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name> # <1>
  namespace: openshift-cluster-api
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
         dataSecretName: worker-user-data # <3>
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: OpenStackMachineTemplate # <4>
        name: <template_name> # <5>
      failureDomain: <nova_availability_zone> # <6>
----
<1> Specify a name for the compute machine set.
<2> Specify the cluster ID as the name of the cluster.
<3> For the Cluster API Technology Preview, the Operator can use the worker user data secret from the `openshift-machine-api` namespace.
<4> Specify the machine template kind.
This value must match the value for your platform.
<5> Specify the machine template name.
<6> Optional: Specify the name of the Nova availability zone for the machine set to create machines in.
If you do not specify a value, machines are not restricted to a specific availability zone.

// [id="cluster-api-supported-features-rhosp_{context}"]
// == Enabling {rh-openstack} features with the Cluster API

// You can enable the following features by updating values in the Cluster API custom resource manifests.

//Not sure what, if anything, we can add here at this time.
