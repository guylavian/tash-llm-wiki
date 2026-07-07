---
title: "Uninstalling the File Integrity Operator"
type: reference
domain: openshift
slug: security-4-22-fio-uninstalling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/fio-uninstalling
version: 4.22
family: security
documentKind: "Documentation"
---

# Uninstalling the File Integrity Operator

[id="fio-uninstalling"]
= Uninstalling the File Integrity Operator

You can remove the File Integrity Operator from your cluster by using the OpenShift Container Platform web console.

// Module included in the following assemblies:
//
// * security/file_integrity_operator/fio-uninstalling.adoc

[id="fio-uninstall-console_{context}"]
= Uninstall the File Integrity Operator using the web console

To remove the File Integrity Operator, you must first delete the `FileIntegrity` objects in all namespaces. After the objects are removed, you can then remove the Operator and its namespace.

.Prerequisites

* You have access to an OpenShift Container Platform cluster that uses an account with `cluster-admin` permissions.
* The File Integrity Operator is installed.

.Procedure

. Navigate to the *Ecosystem* -> *Installed Operators* -> *File Integrity Operator* page.

. From the *File Integrity* tab, ensure the *Show operands in: All namespaces* default option is selected to list all `FileIntegrity` objects in all namespaces.

. Click the Options menu {kebab} and then click *Delete FileIntegrity* to delete a `FileIntegrity` object. Ensure all `FileIntegrity` objects are deleted.

. Go to the *Administration* -> *Ecosystem* -> *Installed Operators* page.

. Click the Options menu {kebab} on the *File Integrity Operator* entry and select *Uninstall Operator*.

. Go to the *Home* -> *Projects* page.

. Search for `openshift-file-integrity`.

. Click the Options menu {kebab} for the *openshift-file-integrity* project entry, and then click *Delete Project*. A *Delete Project* dialog box opens on the web console.

.Verification

* Type `openshift-file-integrity` in the *Delete Project* dialog box and then click the *Delete* button.
