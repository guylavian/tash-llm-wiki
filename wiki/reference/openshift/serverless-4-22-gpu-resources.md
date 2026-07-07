---
title: "Using NVIDIA GPU resources with serverless applications"
type: reference
domain: openshift
slug: serverless-4-22-gpu-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/gpu-resources
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Using NVIDIA GPU resources with serverless applications

[id="gpu-resources"]
= Using NVIDIA GPU resources with serverless applications

NVIDIA supports using GPU resources on OpenShift Container Platform.
See GPU Operator on OpenShift for more information about setting up GPU resources on OpenShift Container Platform.

// Module included in the following assemblies:
//
//  * serverless/integrations/gpu-resources.adoc

[id="serverless-gpu-resources-kn_{context}"]
= Specifying GPU requirements for a service

After GPU resources are enabled for your OpenShift Container Platform cluster, you can specify GPU requirements for a Knative service using the Knative (`kn`) CLI.

.Prerequisites

* The {ServerlessOperatorName}, Knative Serving and Knative Eventing are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* GPU resources are enabled for your OpenShift Container Platform cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

[NOTE]
====
Using NVIDIA GPU resources is not supported for {ibm-z-name} and {ibm-power-name}.
====

.Procedure

. Create a Knative service and set the GPU resource requirement limit to `1` by using the `--limit nvidia.com/gpu=1` flag:
+
[source,terminal]
----
$ kn service create hello --image <service-image> --limit nvidia.com/gpu=1
----
+
A GPU resource requirement limit of `1` means that the service has 1 GPU resource dedicated. Services do not share GPU resources. Any other services that require GPU resources must wait until the GPU resource is no longer in use.
+
A limit of 1 GPU also means that applications exceeding usage of 1 GPU resource are restricted. If a service requests more than 1 GPU resource, it is deployed on a node where the GPU resource requirements can be met.

. Optional. For an existing service, you can change the GPU resource requirement limit to `3` by using the `--limit nvidia.com/gpu=3` flag:
+
[source,terminal]
----
$ kn service update hello --limit nvidia.com/gpu=3
----

[id="additional-requirements_gpu-resources"]
[role="_additional-resources"]
== Additional resources
* Setting resource quotas for extended resources
