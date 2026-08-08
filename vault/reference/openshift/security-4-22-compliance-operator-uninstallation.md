---
title: "Uninstalling the Compliance Operator"
type: reference
domain: openshift
slug: security-4-22-compliance-operator-uninstallation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/compliance-operator-uninstallation
version: 4.22
family: security
documentKind: "Documentation"
---

# Uninstalling the Compliance Operator

[id="compliance-operator-uninstallation"]
= Uninstalling the Compliance Operator

You can remove the OpenShift Compliance Operator from your cluster by using the OpenShift Container Platform web console or the CLI.

// Module included in the following assemblies:
//
// security/compliance_operator/co-management/compliance-operator-uninstallation.adoc

[id="compliance-operator-uninstall_{context}"]
= Uninstalling the OpenShift Compliance Operator from OpenShift Container Platform using the web console

To remove the Compliance Operator, you must first delete the objects in the namespace. After the objects are removed, you can remove the Operator and its namespace by deleting the *openshift-compliance* project.

.Prerequisites

* Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* The OpenShift Compliance Operator must be installed.

.Procedure

To remove the Compliance Operator by using the OpenShift Container Platform web console:

. Go to the *Ecosystem* -> *Installed Operators* -> *Compliance Operator* page.

.. Click *All instances*.

.. In *All namespaces*, click the Options menu {kebab} and delete all ScanSettingBinding, ComplainceSuite, ComplianceScan, and ProfileBundle objects.

. Switch to the *Administration* -> *Ecosystem* -> *Installed Operators* page.

. Click the Options menu {kebab} on the *Compliance Operator* entry and select *Uninstall Operator*.

. Switch to the *Home* -> *Projects* page.

. Search for 'compliance'.

. Click the Options menu {kebab} next to the *openshift-compliance* project, and select *Delete Project*.

.. Confirm the deletion by typing `openshift-compliance` in the dialog box, and click *Delete*.

// Module included in the following assemblies:
//
// security/compliance_operator/co-management/compliance-operator-uninstallation.adoc

[id="compliance-operator-uninstall-cli_{context}"]
= Uninstalling the OpenShift Compliance Operator from OpenShift Container Platform using the CLI

To remove the Compliance Operator, you must first delete the objects in the namespace. After the objects are removed, you can remove the Operator and its namespace by deleting the *openshift-compliance* project.

.Prerequisites

* Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* The OpenShift Compliance Operator must be installed.

.Procedure

. Delete all objects in the namespace.

.. Delete the `ScanSettingBinding` objects:
+
[source,terminal]
----
$ oc delete ssb --all -n openshift-compliance
----

.. Delete the `ScanSetting` objects:
+
[source,terminal]
----
$ oc delete ss --all -n openshift-compliance
----

.. Delete the `ComplianceSuite` objects:
+
[source,terminal]
----
$ oc delete suite --all -n openshift-compliance
----

.. Delete the `ComplianceScan` objects:
+
[source,terminal]
----
$ oc delete scan --all -n openshift-compliance
----

.. Delete the `ProfileBundle` objects:
+
[source,terminal]
----
$ oc delete profilebundle.compliance --all -n openshift-compliance
----

. Delete the Subscription object:
+
[source,terminal]
----
$ oc delete sub --all -n openshift-compliance
----

. Delete the CSV object:
+
[source,terminal]
----
$ oc delete csv --all -n openshift-compliance
----

. Delete the project:
+
[source,terminal]
----
$ oc delete project openshift-compliance
----
+
.Example output
[source,terminal]
----
project.project.openshift.io "openshift-compliance" deleted
----

.Verification

. Confirm the namespace is deleted:
+
[source,terminal]
----
$ oc get project/openshift-compliance
----
+
.Example output
[source,terminal]
----
Error from server (NotFound): namespaces "openshift-compliance" not found
----
