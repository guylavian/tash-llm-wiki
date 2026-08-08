---
title: "Uninstalling OpenShift GitOps"
type: reference
domain: openshift
slug: cicd-4-22-uninstalling-openshift-gitops
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/uninstalling-openshift-gitops
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Uninstalling OpenShift GitOps

[id="uninstalling-openshift-gitops"]
= Uninstalling OpenShift GitOps

Uninstalling the {gitops-title} Operator is a two-step process:

. Delete the Argo CD instances that were added under the default namespace of the {gitops-title} Operator.
. Uninstall the {gitops-title} Operator.

Uninstalling only the Operator will not remove the Argo CD instances created.

// Module included in the following assemblies:
//
// */gitops/uninstalling-openshift-gitops.adoc

[id='go-deleting-argocd-instance_{context}']
= Deleting the Argo CD instances

Delete the Argo CD instances added to the namespace of the GitOps Operator.

.Procedure
. In the *Terminal* type the following command:

[source,terminal]
----
$ oc delete gitopsservice cluster -n openshift-gitops
----

[NOTE]
====
You cannot delete an Argo CD cluster from the web console UI.
====

After the command runs successfully all the Argo CD instances will be deleted from the `openshift-gitops` namespace.

Delete any other Argo CD instances from other namespaces using the same command:

[source,terminal]
----
$ oc delete gitopsservice cluster -n <namespace>
----

// Module included in the following assemblies:
//
// */gitops/uninstalling-openshift-gitops.adoc

[id='go-uninstalling-gitops-operator_{context}']
= Uninstalling the GitOps Operator

.Procedure
. From the *Ecosystem* -> *Software Catalog* page, use the *Filter by keyword* box to search for `{gitops-title} Operator` tile.

. Click the *Red Hat OpenShift GitOps Operator* tile. The Operator tile indicates it is installed.

. In the *Red Hat OpenShift GitOps Operator* descriptor page, click *Uninstall*.

[role="_additional-resources"]
.Additional resources

* You can learn more about uninstalling Operators on OpenShift Container Platform in the Deleting Operators from a cluster section.
