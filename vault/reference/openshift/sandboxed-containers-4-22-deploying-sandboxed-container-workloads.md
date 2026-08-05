---
title: "Deploying {sandboxed-containers-first} workloads"
type: reference
domain: openshift
slug: sandboxed-containers-4-22-deploying-sandboxed-container-workloads
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/sandboxed_containers/deploying-sandboxed-container-workloads
version: 4.22
family: sandboxed_containers
documentKind: "Documentation"
---

# Deploying {sandboxed-containers-first} workloads

[id="deploying-sandboxed-containers-workloads"]
= Deploying {sandboxed-containers-first} workloads

You can install the {sandboxed-containers-operator} using either the web console or OpenShift CLI (`oc`). Before installing the {sandboxed-containers-operator}, you must prepare your OpenShift Container Platform cluster.

[role="_additional-resources"]
.Additional resources
* Installing a user-provisioned cluster on bare metal

[role="_additional-resources"]
.Additional resources

* For more information about installing the Node Feature Discovery (NFD) Operator, see Installing NFD.

[id="deploying-sandboxed-containers-workloads-web-console"]
== Deploying {sandboxed-containers-first} workloads using the web console

You can deploy {sandboxed-containers-first} workloads from the web console. First, you must install the {sandboxed-containers-operator}, then create the `KataConfig` custom resource (CR). Once you are ready to deploy a workload in a sandboxed container, you must manually add `kata` as the `runtimeClassName` to the workload YAML file.

//include::modules/sandboxed-containers-selecting-nodes-web-console.adoc[leveloffset=+3]

[id="deploying-sandboxed-containers-workloads-cli"]
== Deploying {sandboxed-containers-first} workloads using the CLI

You can deploy {sandboxed-containers-first} workloads using the CLI. First, you must install the {sandboxed-containers-operator}, then create the `KataConfig` custom resource. Once you are ready to deploy a workload in a sandboxed container, you must add `kata` as the `runtimeClassName` to the workload YAML file.

[role="_additional-resources"]
.Additional resources
* Installing from OperatorHub using the CLI

[role="_additional-resources"]
.Additional resources
* Understanding how to update labels on nodes

//include::modules/sandboxed-containers-selecting-nodes.adoc[leveloffset=+3]

[id="deploying-sandboxed-containers-workloads_additional-resources"]
[role="_additional-resources"]
== Additional resources

* The {sandboxed-containers-operator} is supported in a restricted network environment. For more information, Using Operator Lifecycle Manager on restricted networks.
* When using a disconnected cluster on a restricted network, you must configure proxy support in Operator Lifecycle Manager to access the OperatorHub. Using a proxy allows the cluster to fetch the {sandboxed-containers-operator}.
