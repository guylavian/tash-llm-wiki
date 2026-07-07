---
title: "Uninstalling {VirtProductName}"
type: reference
domain: openshift
slug: virt-4-22-uninstalling-virt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/uninstalling-virt
version: 4.22
family: virt
documentKind: "Documentation"
---

# Uninstalling {VirtProductName}

[id="uninstalling-virt"]
= Uninstalling {VirtProductName}

[role="_abstract"]
You can uninstall {VirtProductName} by using the web console or the command-line interface (CLI) to delete {VirtProductName} workloads, the Operator, and its resources.

To uninstall {VirtProductName}, perform the following tasks:

. Delete the `HyperConverged` CR.
. Delete the {VirtProductName} Operator.
. Delete the `openshift-cnv` namespace.
. Delete the {VirtProductName} custom resource definitions (CRDs).

[id="prerequisites_{context}"]
== Prerequisites

* Delete all virtual machine instances. You cannot uninstall {VirtProductName} while its workloads remain on the cluster.

// Module included in the following assemblies:
//
// * virt/install/uninstalling-virt-web.adoc

[id="virt-deleting-deployment-custom-resource_{context}"]
= Deleting the HyperConverged custom resource

[role="_abstract"]
To uninstall {VirtProductName}, you first delete the `HyperConverged` custom resource (CR).

.Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

.Procedure

. Navigate to the *Ecosystem* -> *Installed Operators* page.

. Select the {VirtProductName} Operator.

. Click the *{VirtProductName} Deployment* tab.

. Click the Options menu {kebab} beside `kubevirt-hyperconverged` and select *Delete HyperConverged*.

. Click *Delete* in the confirmation window.
// Module included in the following assemblies:
//
// * operators/admin/olm-deleting-operators-from-a-cluster.adoc
// * backup_and_restore/application_backup_and_restore/installing/uninstalling-oadp.adoc
// * serverless/install/removing-openshift-serverless.adoc
// * virt/install/uninstalling-virt.adoc

[id="olm-deleting-operators-from-a-cluster-using-web-console_{context}"]
= Deleting Operators from a cluster using the web console

[role="_abstract"]
Cluster administrators can delete installed Operators from a selected namespace by using the web console.

.Prerequisites

- You have access to the OpenShift Container Platform cluster web console using an account with
`cluster-admin` permissions.
`dedicated-admin` permissions.

.Procedure

. Navigate to the *Ecosystem* -> *Installed Operators* page.

. Scroll or enter a keyword into the *Filter by name* field to find the Operator that you want to remove. Then, click on it.

. On the right side of the *Operator Details* page, select *Uninstall Operator* from the *Actions* list.
+
An *Uninstall Operator?* dialog box is displayed.

. Select *Uninstall* to remove the Operator, Operator deployments, and pods. Following this action, the Operator stops running and no longer receives updates.
+
[NOTE]
====
This action does not remove resources managed by the Operator, including custom resource definitions (CRDs) and custom resources (CRs). Dashboards and navigation items enabled by the web console and off-cluster resources that continue to run might need manual clean up. To remove these after uninstalling the Operator, you might need to manually delete the Operator CRDs.
====
// Module included in the following assemblies:
//
// * virt/install/uninstalling-virt.adoc

[id="deleting-a-namespace-using-the-web-console_{context}"]
= Deleting a namespace using the web console

[role="_abstract"]
You can delete a namespace by using the OpenShift Container Platform web console.

.Prerequisites

* You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

.Procedure

. Navigate to *Administration* -> *Namespaces*.

. Locate the namespace that you want to delete in the list of namespaces.

. On the far right side of the namespace listing, select *Delete Namespace* from the
Options menu {kebab}.

. When the *Delete Namespace* pane opens, enter the name of the namespace that
you want to delete in the field.

. Click *Delete*.
// Module included in the following assemblies:
//
// * virt/install/uninstalling-virt.adoc

[id="virt-deleting-virt-crds-web_{context}"]
= Deleting {VirtProductName} custom resource definitions

[role="_abstract"]
You can delete the {VirtProductName} custom resource definitions (CRDs) by using the web console.

.Prerequisites

* You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

.Procedure

. Navigate to *Administration* -> *CustomResourceDefinitions*.

. Select the *Label* filter and enter `operators.coreos.com/kubevirt-hyperconverged.openshift-cnv` in the *Search* field to display the {VirtProductName} CRDs.

. Click the Options menu {kebab} beside each CRD and select *Delete CustomResourceDefinition*.
// Module included in the following assemblies:
//
// * virt/install/uninstalling-virt.adoc

[id="virt-deleting-virt-cli_{context}"]
= Uninstalling {VirtProductName} by using the CLI

[role="_abstract"]
You can uninstall {VirtProductName} by using the OpenShift CLI (`oc`).

.Prerequisites

* You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have installed the {oc-first}.
* You have deleted all virtual machines and virtual machine instances. You cannot uninstall {VirtProductName} while its workloads remain on the cluster.

.Procedure

. Delete the `HyperConverged` custom resource:
+
[source,terminal,subs="attributes+"]
----
$ oc delete HyperConverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Delete the {VirtProductName} Operator subscription:
+
[source,terminal,subs="attributes+"]
----
$ oc delete subscription hco-operatorhub -n {CNVNamespace}
----

. Delete the {VirtProductName} `ClusterServiceVersion` resource:
+
[source,terminal,subs="attributes+"]
----
$ oc delete csv -n openshift-cnv -l operators.coreos.com/kubevirt-hyperconverged.{CNVNamespace}
----

. Delete the {VirtProductName} namespace:
+
[source,terminal]
----
$ oc delete namespace openshift-cnv
----

. List the {VirtProductName} custom resource definitions (CRDs) by running the `oc delete crd` command with the `dry-run` option:
+
[source,terminal,subs="attributes+"]
----
$ oc delete crd --dry-run=client -l operators.coreos.com/kubevirt-hyperconverged.{CNVNamespace}
----
+
Example output:
+
----
customresourcedefinition.apiextensions.k8s.io "cdis.cdi.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "hostpathprovisioners.hostpathprovisioner.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "hyperconvergeds.hco.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "kubevirts.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "networkaddonsconfigs.networkaddonsoperator.network.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "ssps.ssp.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "tektontasks.tektontasks.kubevirt.io" deleted (dry run)
----

. Delete the CRDs by running the `oc delete crd` command without the `dry-run` option:
+
[source,terminal,subs="attributes+"]
----
$ oc delete crd -l operators.coreos.com/kubevirt-hyperconverged.{CNVNamespace}
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Deleting the `HyperConverged` custom resource
* Deleting Operators from a cluster using the web console
* Deleting a namespace using the web console
* Deleting {VirtProductName} custom resource definitions
* Deleting a virtual machine using the web console
* Deleting a standalone virtual machine instance using the CLI
