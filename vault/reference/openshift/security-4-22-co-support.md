---
title: "Compliance Operator support"
type: reference
domain: openshift
slug: security-4-22-co-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/co-support
version: 4.22
family: security
documentKind: "Documentation"
---

# Compliance Operator support

//OpenShift Compliance Operator support page
[id="co-support"]
= Compliance Operator support

[id="co-lifecycle_{context}"]
== Compliance Operator lifecycle

The Compliance Operator is a "Rolling Stream" Operator, meaning updates are available asynchronously of OpenShift Container Platform releases. For more information, see OpenShift Operator Life Cycles on the Red Hat Customer Portal.

// Module included in the following assemblies:
//
// * security/compliance_operator/co-support.adoc
// * support/getting-support.adoc
// * distr_tracing/distributed-tracing-release-notes.adoc
// * service_mesh/v2x/ossm-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * osd_architecture/osd-support.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-0.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-1.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-2.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-3.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-4.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-5.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-6.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-7.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-8.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-2-9.adoc
// * distr_tracing/distr_tracing_rn/distr-tracing-rn-3-0.adoc
// * microshift_support/microshift-getting-support.adoc

[id="support_{context}"]
= Getting support

[role="_abstract"]
If you experience difficulty with a procedure described in this documentation, or with OpenShift Container Platform in general, visit the Red Hat Customer Portal.

From the Customer Portal, you can:

* Search or browse through the Red Hat Knowledgebase of articles and solutions relating to Red Hat products.
* Submit a support case to Red Hat Support.
* Access other product documentation.

To identify issues with your cluster, you can use {red-hat-lightspeed} in {cluster-manager-url}. {red-hat-lightspeed} provides details about issues and, if available, information on how to solve a problem.

// TODO: verify that these settings apply for Service Mesh and OpenShift virtualization, etc.
If you have a suggestion for improving this documentation or have found an
error, submit a Jira issue for the most relevant documentation component. Please provide specific details, such as the section name and OpenShift Container Platform version.

// Module included in the following assemblies:
//
// * security/compliance_operator/co-support.adoc

[id="compliance-must-gather_{context}"]
= Using the must-gather tool for the Compliance Operator

Starting in Compliance Operator v1.6.0, you can collect data about the Compliance Operator resources by running the `must-gather` command with the Compliance Operator image.

[NOTE]
====
Consider using the `must-gather` tool when opening support cases or filing bug reports, as it provides additional details about the Operator configuration and logs.
====

.Procedure

* Run the following command to collect data about the Compliance Operator:
+
[source,terminal]
----
$ oc adm must-gather --image=$(oc get csv compliance-operator.v1.6.0 -o=jsonpath='{.spec.relatedImages[?(@.name=="must-gather")].image}')
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* About the must-gather tool
* Product Compliance
