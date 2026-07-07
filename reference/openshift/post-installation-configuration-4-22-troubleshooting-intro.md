---
title: "Troubleshooting and maintaining {product-title} clusters"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-troubleshooting-intro
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/troubleshooting-intro
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Troubleshooting and maintaining {product-title} clusters

[id="troubleshooting-intro"]
= Troubleshooting and maintaining OpenShift Container Platform clusters

Troubleshooting and maintenance are weekly tasks that can be a challenge if you do not have the tools to reach your goal, whether you want to update a component or investigate an issue.
Part of the challenge is knowing where and how to search for tools and answers.

To maintain and troubleshoot a bare-metal environment with high performance requirements, see the following procedures.

[IMPORTANT]
====
This troubleshooting information is not a reference for configuring OpenShift Container Platform or developing cloud-native applications.

For information about developing cloud-native applications on OpenShift Container Platform, see Red Hat Best Practices for Kubernetes.
====

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/telco-troubleshooting-intro.adoc

[id="support-getting-support_{context}"]
= Getting Support

[role="_abstract"]
If you experience difficulty with a procedure, visit the Red{nbsp}Hat Customer Portal.
From the Customer Portal, you can find help in various ways:

* Search or browse through the Red{nbsp}Hat Knowledgebase of articles and solutions about Red{nbsp}Hat products.
* Submit a support case to Red{nbsp}Hat Support.
* Access other product documentation.

To identify issues with your deployment, you can use the debugging tool or check the health endpoint of your deployment.
After you have debugged or obtained health information about your deployment, you can search the Red{nbsp}Hat Knowledgebase for a solution or file a support ticket.

//If you have a suggestion for improving this documentation or have found an error, submit a Jira issue to the ProjectQuay project. Provide specific details, such as the section name and {quay} version.
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
