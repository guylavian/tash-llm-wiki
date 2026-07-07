---
title: "Getting support"
type: reference
domain: openshift
slug: ai-workloads-4-22-getting-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/getting-support
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Getting support

[id="getting-support"]
= Getting support

If you experience difficulty with a procedure described in this documentation, or with {kueue-name} in general, visit the Red{nbsp}Hat Customer Portal.

From the Customer Portal, you can:

* Search or browse through the Red{nbsp}Hat Knowledgebase of articles and solutions relating to Red{nbsp}Hat products.
* Submit a support case to Red{nbsp}Hat Support.
* Access other product documentation.

[id="getting-support-rh-kb"]
== About the Red Hat Knowledgebase

The Red{nbsp}Hat Knowledgebase provides rich content aimed at helping you make the most of Red{nbsp}Hat's products and technologies. The Red{nbsp}Hat Knowledgebase consists of articles, product documentation, and videos outlining best practices on installing, configuring, and using Red{nbsp}Hat products. In addition, you can search for solutions to known issues, each providing concise root cause descriptions and remedial steps.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/getting-support.adoc

[id="gathering-cluster-data_{context}"]
= Collecting data for Red Hat Support

You can use the `oc adm must-gather` CLI command to collect the information about your {kueue-name} instance that is most likely needed for debugging issues, including:

* {kueue-name} custom resources, such as workloads, cluster queues, local queues, resource flavors, admission checks, and their corresponding cluster resource definitions (CRDs)
* Services
* Endpoints
* Webhook configurations
* Logs from the `openshift-kueue-operator` namespace and `kueue-controller-manager` pods

Collected data is written into a new directory named `must-gather/` in the current working directory by default.

.Prerequisites

* The {kueue-name} Operator is installed on your cluster.
* You have installed the {oc-first}.

.Procedure

. Navigate to the directory where you want to store the `must-gather` data.

. Collect `must-gather` data by running the following command:
+
[source,terminal]
----
$ oc adm must-gather \
  --image=registry.redhat.io/kueue/kueue-must-gather-rhel9:<version>
----
+
Where `<version>` is your current version of {kueue-name}.

. Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique `must-gather` data. For more information about how to find the cluster ID, see How to find the cluster-id or name on OpenShift cluster.

. Attach the compressed file to your support case on the the *Customer Support* page of the Red{nbsp}Hat Customer Portal.

[id="getting-support-additional-resources"]
[role="_additional-resources"]
== Additional resources
* Support overview
