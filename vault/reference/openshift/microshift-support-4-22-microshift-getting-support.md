---
title: "Support resources"
type: reference
domain: openshift
slug: microshift-support-4-22-microshift-getting-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_support/microshift-getting-support
version: 4.22
family: microshift_support
documentKind: "Documentation"
---

# Support resources

[id="microshift-getting-support"]
= Support resources

[role="_abstract"]
Use the following information to get more help with {op-system-bundle}, including OpenShift Container Platform or {op-system-ostree-first}. You can search the Red{nbsp}Hat Knowledgebase for immediate solutions, provide feedback on documentation, or open a formal support case through the Red{nbsp}Hat Customer Portal if you cannot resolve the issue yourself.

//OCP module
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
// microshift_support/

[id="microshift-provide-feedback-jira-link_{context}"]
= Documentation feedback

[role="_abstract"]
To report an error or to improve our documentation, you can submit a Jira issue by using your Red Hat Jira account.

//OCP module
// Module included in the following assemblies:
//
// * serverless/serverless-support.adoc
// * support/getting-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * osd_architecture/osd-support.adoc
// * microshift_support/microshift-getting-support.adoc
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/telco-troubleshooting-intro.adoc

[id="support-knowledgebase-about_{context}"]
= About the Red Hat Knowledgebase

[role="_abstract"]
The Red{nbsp}Hat Knowledgebase provides rich content aimed at helping you make the most of Red{nbsp}Hat's products and technologies. The Red{nbsp}Hat Knowledgebase consists of articles, product documentation, and videos outlining best practices on installing, configuring, and using Red Hat products. In addition, you can search for solutions to known issues, each providing concise root cause descriptions and remedial steps.

//OCP module
// Module included in the following assemblies:
//
// * serverless/serverless-support.adoc
// * support/getting-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * osd_architecture/osd-support.adoc
// * microshift_support/microshift-getting-support.adoc
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/telco-troubleshooting-intro.adoc

[id="support-knowledgebase-search_{context}"]
= Searching the Red Hat Knowledgebase

[role="_abstract"]
In the event of an OpenShift Container Platform issue, you can perform an initial search to determine if a solution already exists within the Red Hat Knowledgebase.

.Prerequisites

* You have a Red Hat Customer Portal account.

.Procedure

. Log in to the Red Hat Customer Portal.

. Click *Search*.

. In the search field, input keywords and strings relating to the problem, including:
+
* OpenShift Container Platform components (such as *etcd*)
* Related procedure (such as *installation*)
* Warnings, error messages, and other outputs related to explicit failures

. Click the *Enter* key.

. Optional: Select the *OpenShift Container Platform* product filter.

. Optional: Select the *Documentation* content type filter.

// Module included in the following assemblies:
//
// * microshift_support/microshift-getting-support.adoc

[id="microshift-support-submitting-a-case_{context}"]
= Submitting a support case

[role="_abstract"]
If you encounter issues with {microshift-short} that cannot be resolved through the standard troubleshooting, you can submit a support case to Red{nbsp}Hat. Providing detailed descriptions and diagnostic data helps Red{nbsp}Hat Support to analyze the problem and help you with a resolution.

.Prerequisites

* The {microshift-short} service is running.
* You have installed the OpenShift CLI (`oc`).
* You have a Red Hat Customer Portal account.
* You have a Red Hat Standard or Premium subscription.

.Procedure

. Log in to the *Customer Support* page of the Red Hat Customer Portal.

. Click *Get support*.

. On the *Cases* tab of the *Customer Support* page:

.. Optional: Change the pre-filled account and owner details if needed.

.. Select the appropriate category for your issue, such as *Bug or Defect*, and click *Continue*.

. Enter the following information:

.. In the *Summary* field, enter a concise but descriptive problem summary and further details about the symptoms being experienced, as well as your expectations.

.. Select *{op-system-bundle}* from the *Product* drop-down menu.

.. Select *{rhde-version}* from the *Version* drop-down.

. Review the list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that is being reported. If the suggested articles do not address the issue, click *Continue*.

. Review the updated list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that is being reported. The list is refined as you provide more information during the case creation process. If the suggested articles do not address the issue, click *Continue*.

. Ensure that the account information presented is as expected, and if not, amend accordingly.

. Complete the following questions where prompted. Include which type of install type you are using, either RPM or embedded-image. Click *Continue*:
+
* What are you experiencing? What are you expecting to happen?
* Define the value or impact to you or the business.
* Where are you experiencing this behavior? What environment?
* When does this behavior occur? Frequency? Repeatedly? At certain times?

. Upload relevant diagnostic data files and click *Continue*. Include data gathered using the `sos` tool or etcd as a starting point, plus any issue-specific data that is not collected in those logs.

. Add relevant case management details and click *Continue*.

. Preview the case details and click *Submit*.
