---
title: "Preparing to install {ServerlessProductName}"
type: reference
domain: openshift
slug: serverless-4-22-preparing-serverless-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/preparing-serverless-install
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Preparing to install {ServerlessProductName}

[id="preparing-serverless-install"]
= Preparing to install {ServerlessProductName}

Read the following information about supported configurations and prerequisites before you install {ServerlessProductName}.

// OCP specific docs
[id="install-serverless-operator-before-you-begin"]

* {ServerlessProductName} is supported for installation in a restricted network environment.

* {ServerlessProductName} currently cannot be used in a multi-tenant configuration on a single cluster.

[id="about-serverless-supported-configs"]
== Supported configurations

The set of supported features, configurations, and integrations for {ServerlessProductName}, current and past versions, are available at the Supported Configurations page.

[id="about-serverless-scalability-performance"]
== Scalability and performance

{ServerlessProductName} has been tested with a configuration of 3 main nodes and 3 worker nodes, each of which has 64 CPUs, 457 GB of memory, and 394 GB of storage each.

The maximum number of Knative services that can be created using this configuration is 3,000. This corresponds to the OpenShift Container Platform Kubernetes services limit of 10,000, since 1 Knative service creates 3 Kubernetes services.

The average scale from zero response time was approximately 3.4 seconds, with a maximum response time of 8 seconds, and a 99.9th percentile of 4.5 seconds for a simple Quarkus application. These times might vary depending on the application and the runtime of the application.

// OCP specific docs
[id="install-serverless-operator-before-you-begin"]

// Module included in the following assemblies:
//
// * /serverless/install/preparing-serverless-install.adoc

[id="serverless-cluster-sizing-req_{context}"]
= Defining cluster size requirements

To install and use {ServerlessProductName}, the OpenShift Container Platform cluster must be sized correctly.

[NOTE]
====
The following requirements relate only to the pool of worker machines of the OpenShift Container Platform cluster. Control plane nodes are not used for general scheduling and are omitted from the requirements.
====

The minimum requirement to use {ServerlessProductName} is a cluster with 10 CPUs and 40GB memory.
By default, each pod requests ~400m of CPU, so the minimum requirements are based on this value.

The total size requirements to run {ServerlessProductName} are dependent on the components that are installed and the applications that are deployed, and might vary depending on your deployment.

[id="install-serverless-operator-scaling-with-machinesets"]
== Scaling your cluster using compute machine sets

You can use the OpenShift Container Platform `MachineSet` API to manually scale your cluster up to the desired size. The minimum requirements usually mean that you must scale up one of the default compute machine sets by two additional machines. See Manually scaling a compute machine set.

// Module included in the following assemblies:
//
// * /serverless/install/install-serverless-operator.adoc

[id="serverless-cluster-sizing-req-additional_{context}"]
= Additional requirements for advanced use-cases

For more advanced use-cases such as logging or metering on OpenShift Container Platform, you must deploy more resources. Recommended requirements for such use-cases are 24 CPUs and 96GB of memory.

If you have high availability (HA) enabled on your cluster, this requires between 0.5 - 1.5 cores and between 200MB - 2GB of memory for each replica of the Knative Serving control plane.
HA is enabled for some Knative Serving components by default. You can disable HA by following the documentation on "Configuring high availability replicas".

// TODO: Add OSD specific docs for auto scaling compute machine sets? These docs aren't available for OSD so we need to look into what's required to doc here.
// QE thread related: https://coreos.slack.com/archives/CD87JDUB0/p1643986092796179

// OSD and ROSA docs

[id="additional-resources_preparing-serverless-install"]
[role="_additional-resources"]
== Additional resources
* Using Operator Lifecycle Manager in disconnected environments
* Understanding the software catalog
* Cluster capabilities
