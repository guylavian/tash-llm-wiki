---
title: "Uninstalling {pipelines-shortname}"
type: reference
domain: openshift
slug: cicd-4-22-uninstalling-pipelines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/uninstalling-pipelines
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Uninstalling {pipelines-shortname}

[id="uninstalling-pipelines"]
= Uninstalling {pipelines-shortname}

Cluster administrators can uninstall the {pipelines-title} Operator by performing the following steps:

. Delete the Custom Resources (CRs) that were added by default when you installed the {pipelines-title} Operator.
. Delete the CRs of the optional components such as {tekton-hub} that depend on the Operator.
+
[CAUTION]
====
If you uninstall the Operator without removing the CRs of optional components, you cannot remove them later.
====
. Uninstall the {pipelines-title} Operator.

Uninstalling only the Operator will not remove the {pipelines-title} components created by default when the Operator is installed.

// Module included in the following assemblies:
//
// */openshift_pipelines/uninstalling-pipelines.adoc

[id='op-deleting-the-pipelines-component-and-custom-resources_{context}']
= Deleting the {pipelines-title} components and Custom Resources

Delete the Custom Resources (CRs) created by default during installation of the {pipelines-title} Operator.

[discrete]
.Procedure
. In the *Administrator* perspective of the web console, navigate to *Administration* -> *Custom Resource Definition*.

. Type `config.operator.tekton.dev` in the *Filter by name* box to search for the {pipelines-title} Operator CRs.

. Click *CRD Config* to see the *Custom Resource Definition Details* page.

. Click the *Actions* drop-down menu and select *Delete Custom Resource Definition*.

+
[NOTE]
====
Deleting the CRs will delete the {pipelines-title} components, and all the tasks and pipelines on the cluster will be lost.
====

. Click *Delete* to confirm the deletion of the CRs.

[IMPORTANT]
====
Repeat the procedure to find and remove CRs of optional components such as {tekton-hub} before uninstalling the Operator. If you uninstall the Operator without removing the CRs of optional components, you cannot remove them later.
====

// Module included in the following assemblies:
//
// */openshift_pipelines/uninstalling-pipelines.adoc

[id='op-uninstalling-the-pipelines-operator_{context}']
= Uninstalling the {pipelines-title} Operator

You can uninstall the {pipelines-title} Operator by using the *Administrator* perspective in the web console.

[discrete]
.Procedure

. From the *Ecosystem* -> *Software Catalog* page, use the *Filter by keyword* box to search for the *{pipelines-title}* Operator.

. Click the *{pipelines-title}* Operator tile. The Operator tile indicates that the Operator is installed.

. In the *{pipelines-title}* Operator description page, click *Uninstall*.

[role="_additional-resources"]
.Additional resources

* You can learn more about uninstalling Operators on OpenShift Container Platform in the deleting Operators from a cluster section.
