---
title: "{ServerlessProductName} support"
type: reference
domain: openshift
slug: serverless-4-22-serverless-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-support
version: 4.22
family: serverless
documentKind: "Documentation"
---

# {ServerlessProductName} support

[id="serverless-support"]
= {ServerlessProductName} support

If you experience difficulty with a procedure described in this documentation, visit the Red Hat Customer Portal at http://access.redhat.com. You can use the Red Hat Customer Portal to search or browse through the Red Hat Knowledgebase of technical support articles about Red Hat products. You can also submit a support case to Red Hat Global Support Services (GSS), or access other product documentation.

If you have a suggestion for improving this guide or have found an error, you can submit a Jira issue for the most relevant documentation component. Provide specific details, such as the section number, guide name, and {ServerlessProductName} version so we can easily locate the content.
// TODO: Update once https://issues.redhat.com/browse/OSDOCS-3730 is done to update this to Jira

// Generic help topics

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

[id="serverless-support-gather-info"]
== Gathering diagnostic information for support

When you open a support case, it is helpful to provide debugging information about your cluster to Red Hat Support. The `must-gather` tool enables you to collect diagnostic information about your OpenShift Container Platform cluster, including data related to {ServerlessProductName}. For prompt support, supply diagnostic information for both OpenShift Container Platform and {ServerlessProductName}.

// Module included in the following assemblies:
//
// * sandboxed_containers/troubleshooting-sandboxed-containers.adoc
// * virt/support/virt-collecting-virt-data.adoc
// * support/gathering-cluster-data.adoc
// * service_mesh/v2x/ossm-support.adoc
// * service_mesh/v1x/servicemesh-release-notes.adoc
// * serverless/serverless-support.adoc

[id="about-must-gather_{context}"]
= About the must-gather tool

[role="_abstract"]
The `oc adm must-gather` CLI command collects the information from your cluster that is most likely needed for debugging issues, including:

* Resource definitions
* Service logs

By default, the `oc adm must-gather` command uses the default plugin image and writes into `./must-gather.local`.

Alternatively, you can collect specific information by running the command with the appropriate arguments as described in the following sections:

* To collect data related to one or more specific features, use the `--image` argument with an image, as listed in a following section.
+
For example:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion}
----

* To collect the audit logs, use the `-- /usr/bin/gather_audit_logs` argument, as described in a following section.
+

For example:
+
[source,terminal]
----
$ oc adm must-gather -- /usr/bin/gather_audit_logs
----
+
[NOTE]
====
- Audit logs are not collected as part of the default set of information to reduce the size of the files.
- On a Windows operating system, install the `cwRsync` client and add to the `PATH`  variable for use with the `oc rsync` command.
====

When you run `oc adm must-gather`, a new pod with a random name is created in a new project on the cluster. The data is collected on that pod and saved in a new directory that starts with `must-gather.local` in the current working directory.

For example:

[source,terminal]
----
NAMESPACE                      NAME                 READY   STATUS      RESTARTS      AGE
...
openshift-must-gather-5drcj    must-gather-bklx4    2/2     Running     0             72s
openshift-must-gather-5drcj    must-gather-s8sdh    2/2     Running     0             72s
...
----
// todo: table or ref module listing available images?
Optionally, you can run the `oc adm must-gather` command in a specific namespace by using the `--run-namespace` option.

For example:

[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --run-namespace <namespace> \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v{HCOVersion}
----
// Module included in the following assemblies:
//
// * serverless/serverless-support.adoc

[id="serverless-about-collecting-data_{context}"]
= About collecting {ServerlessProductName} data

You can use the `oc adm must-gather` CLI command to collect information about your cluster, including features and objects associated with {ServerlessProductName}. To collect {ServerlessProductName} data with `must-gather`, you must specify the {ServerlessProductName} image and the image tag for your installed version of {ServerlessProductName}.

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

* Collect data by using the `oc adm must-gather` command:
+
[source,terminal]
----
$ oc adm must-gather --image=registry.redhat.io/openshift-serverless-1/svls-must-gather-rhel8:<image_version_tag>
----
+
.Example command
[source,terminal]
----
$ oc adm must-gather --image=registry.redhat.io/openshift-serverless-1/svls-must-gather-rhel8:1.14.0
----
