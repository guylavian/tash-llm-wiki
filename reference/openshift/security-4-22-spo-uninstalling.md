---
title: "Uninstalling the Security Profiles Operator"
type: reference
domain: openshift
slug: security-4-22-spo-uninstalling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/spo-uninstalling
version: 4.22
family: security
documentKind: "Documentation"
---

# Uninstalling the Security Profiles Operator

[id="spo-uninstalling"]
= Uninstalling the Security Profiles Operator

You can remove the Security Profiles Operator from your cluster by using the OpenShift Container Platform web console.

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-troubleshooting.adoc

[id="spo-uninstall-console_{context}"]
= Uninstall the Security Profiles Operator using the web console

To remove the Security Profiles Operator, you must first delete the `seccomp` and SELinux profiles. After the profiles are removed, you can then remove the Operator and its namespace by deleting the *openshift-security-profiles* project.

.Prerequisites

* You have access to the web console as a user with `cluster-admin` privileges.
* The Security Profiles Operator is installed.

.Procedure

To remove the Security Profiles Operator by using the OpenShift Container Platform web console:

. Navigate to the *Ecosystem* -> *Installed Operators* page.

. Delete all `seccomp` profiles, SELinux profiles, and webhook configurations.

. Switch to the *Administration* -> *Ecosystem* -> *Installed Operators* page.

. Click the Options menu {kebab} on the *Security Profiles Operator* entry and select *Uninstall Operator*.

. Switch to the *Home* -> *Projects* page.

. Search for `security profiles`.

. Click the Options menu {kebab} next to the *openshift-security-profiles* project, and select *Delete Project*.

.. Confirm the deletion by typing `openshift-security-profiles` in the dialog box, and click *Delete*.

. Delete the `MutatingWebhookConfiguration` object by running the following command:
+
[source,terminal]
----
$ oc delete MutatingWebhookConfiguration spo-mutating-webhook-configuration
----
