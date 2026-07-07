---
title: "Getting support"
type: reference
domain: openshift
slug: support-4-22-getting-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/getting-support
version: 4.22
family: support
documentKind: "Documentation"
---

# Getting support

[id="getting-support"]
= Getting support

[role="_abstract"]
You can get support for OpenShift Container Platform by searching the knowledge base, submitting a support case, and using remote health monitoring tools.

// Getting support

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
// * serverless/serverless-support.adoc
// * support/getting-support.adoc
// * service_mesh/v2x/ossm-troubleshooting-istio.adoc
// * osd_architecture/osd-support.adoc
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/telco-troubleshooting-intro.adoc

[id="support-submitting-a-case_{context}"]
= Submitting a support case

[role="_abstract"]
Submit a support case to Red Hat Support to get help with issues you encounter with OpenShift Container Platform.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).
* You have access to the {cluster-manager-first}.
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

.. Select *OpenShift Container Platform* from the *Product* drop-down menu.

.. Select ** from the *Version* drop-down.

. Review the list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that is being reported. If the suggested articles do not address the issue, click *Continue*.

. Review the updated list of suggested Red Hat Knowledgebase solutions for a potential match against the problem that is being reported. The list is refined as you provide more information during the case creation process. If the suggested articles do not address the issue, click *Continue*.

. Ensure that the account information presented is as expected, and if not, amend accordingly.

. Check that the autofilled OpenShift Container Platform Cluster ID is correct. If it is not, manually obtain your cluster ID.
+
* To manually obtain your cluster ID using {cluster-manager-url}:
.. Navigate to *Cluster List*.
.. Click on the name of the cluster you need to open a support case for.
.. Find the value in the *Cluster ID* field of the *Details* section of the *Overview* tab.
+
* To manually obtain your cluster ID using the OpenShift Container Platform web console:
.. Navigate to *Home* -> *Overview*.
.. Find the value in the *Cluster ID* field of the *Details* section.
+
* Alternatively, it is possible to open a new support case through the OpenShift Container Platform web console and have your cluster ID autofilled.
.. From the toolbar, navigate to *(?) Help* -> *Open Support Case*.
.. The *Cluster ID* value is autofilled.
+
* To obtain your cluster ID using the OpenShift CLI (`oc`), run the following command:
+
[source,terminal]
----
$ oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}'
----

. Complete the following questions where prompted and then click *Continue*:
+
* What are you experiencing? What are you expecting to happen?
* Define the value or impact to you or the business.
* Where are you experiencing this behavior? What environment?
* When does this behavior occur? Frequency? Repeatedly? At certain times?

. Upload relevant diagnostic data files and click *Continue*.
It is recommended to include data gathered using the `oc adm must-gather` command as a starting point, plus any issue specific data that is not collected by that command.

. Input relevant case management details and click *Continue*.

. Preview the case details and click *Submit*.

[id="getting-support-additional-resources"]
[role="_additional-resources"]
== Additional resources

* Using {red-hat-lightspeed} to identify issues with your cluster
