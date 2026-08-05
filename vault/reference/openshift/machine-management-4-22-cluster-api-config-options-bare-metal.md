---
title: "Cluster API configuration options for bare metal"
type: reference
domain: openshift
slug: machine-management-4-22-cluster-api-config-options-bare-metal
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cluster-api-config-options-bare-metal
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Cluster API configuration options for bare metal

[id="cluster-api-config-options-bare-metal"]
= Cluster API configuration options for bare metal

You can change the configuration of your bare metal Cluster API machines by updating values in the Cluster API custom resource manifests.

[id="cluster-api-sample-yaml-bare-metal_{context}"]
== Sample YAML for configuring bare metal clusters

The following example YAML files show configurations for a bare metal cluster.

//Sample YAML for CAPI bare metal machine template resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-bare-metal.adoc

[id="capi-yaml-machine-template-bare-metal_{context}"]
= Sample YAML for a Cluster API machine template resource on bare metal

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates.
The compute machine set references this template when creating machines.

[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: Metal3MachineTemplate # <1>
metadata:
  name: <template_name>  # <2>
  namespace: openshift-cluster-api
spec:
  template:
    spec: # <3>
      customDeploy: install_coreos
      userData:
        name: worker-user-data-managed # <4>
----
<1> Specify the machine template kind.
This value must match the value for your platform.
<2> Specify a name for the machine template.
<3> Specify the details for your environment. The values here are examples.
<4> The `userData` parameter refers to the Ignition configuration, which the Machine API Operator generates during installation. You must apply the `openshift-cluster-api` namespace to ensure the cluster can access the secret by running the following command:
+
[source,terminal]
----
$ oc get secret worker-user-data-managed \
  -n openshift-machine-api -o yaml | \
  sed 's/namespace: .*/namespace: openshift-cluster-api/' | oc apply -f -
----

//Sample YAML for a CAPI bare metal compute machine set resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-bare-metal.adoc

[id="capi-yaml-machine-set-bare-metal_{context}"]
= Sample YAML for a Cluster API compute machine set resource on bare metal

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
        node-role.kubernetes.io/worker: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data-managed
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: Metal3MachineTemplate # <3>
        name: <template_name> # <4>
----
<1> Specify a name for the compute machine set.
The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.
<2> Specify the cluster ID as the name of the cluster.
<3> Specify the machine template kind.
This value must match the value for your platform.
<4> Specify the machine template name.

//Section depends on migration support
[id="cluster-api-supported-features-bare-metal_{context}"]
== Enabling bare metal features with the Cluster API

You can enable features by updating values in the Cluster API custom resource manifests.

// Cluster autoscaler GPU labels

[role="_additional-resources"]
.Additional resources
* Cluster autoscaler resource definition
