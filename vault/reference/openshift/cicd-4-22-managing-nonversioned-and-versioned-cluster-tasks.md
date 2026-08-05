---
title: "Managing non-versioned and versioned cluster tasks"
type: reference
domain: openshift
slug: cicd-4-22-managing-nonversioned-and-versioned-cluster-tasks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/managing-nonversioned-and-versioned-cluster-tasks
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Managing non-versioned and versioned cluster tasks

[id="managing-nonversioned-and-versioned-cluster-tasks"]
= Managing non-versioned and versioned cluster tasks

As a cluster administrator, installing the {pipelines-title} Operator creates variants of each default cluster task known as _versioned cluster tasks_ (VCT) and _non-versioned cluster tasks_ (NVCT). For example, installing the {pipelines-title} Operator v1.7 creates a `buildah-1-7-0` VCT and a `buildah` NVCT.

Both NVCT and VCT have the same metadata, behavior, and specifications, including `params`, `workspaces`, and `steps`. However, they behave differently when you disable them or upgrade the Operator.

[IMPORTANT]
====
In {pipelines-title} 1.10, cluster task functionality is deprecated and is planned to be removed in a future release.
====

// This module is part of the following assembly:
//
// *cicd/pipelines/managing-nonversioned-and-versioned-cluster-tasks.adoc
[id="differences-between-non-versioned-and-versioned-cluster-tasks_{context}"]
= Differences between non-versioned and versioned cluster tasks

Non-versioned and versioned cluster tasks have different naming conventions. And, the {pipelines-title} Operator upgrades them differently.

.Differences between non-versioned and versioned cluster tasks
[options="header"]
|===

| | Non-versioned cluster task | Versioned cluster task

| Nomenclature
| The NVCT only contains the name of the cluster task. For example, the name of the NVCT of Buildah installed with Operator v1.7 is `buildah`.
| The VCT contains the name of the cluster task, followed by the version as a suffix. For example, the name of the VCT of Buildah installed with Operator v1.7 is `buildah-1-7-0`.

| Upgrade
| When you upgrade the Operator, it updates the non-versioned cluster task with the latest changes. The name of the NVCT remains unchanged.
| Upgrading the Operator installs the latest version of the VCT and retains the earlier version. The latest version of a VCT corresponds to the upgraded Operator. For example, installing Operator 1.7 installs `buildah-1-7-0` and retains `buildah-1-6-0`.

|===

// This module is part of the following assembly:
//
// *cicd/pipelines/managing-nonversioned-and-versioned-cluster-tasks.adoc
[id="advantages-and-disadvantages-of-non-versioned-and-versioned-cluster-tasks_{context}"]
= Advantages and disadvantages of non-versioned and versioned cluster tasks

Before adopting non-versioned or versioned cluster tasks as a standard in production environments, cluster administrators might consider their advantages and disadvantages.

.Advantages and disadvantages of non-versioned and versioned cluster tasks
[options="header"]
|===

| Cluster task | Advantages | Disadvantages

| Non-versioned cluster task (NVCT)
a|
* If you prefer deploying pipelines with the latest updates and bug fixes, use the NVCT.
* Upgrading the Operator upgrades the non-versioned cluster tasks, which consume fewer resources than multiple versioned cluster tasks.
a| If you deploy pipelines that use NVCT, they might break after an Operator upgrade if the automatically upgraded cluster tasks are not backward-compatible.

| Versioned cluster task (VCT)
a|
* If you prefer stable pipelines in production, use the VCT.
* The earlier version is retained on the cluster even after the later version of a cluster task is installed. You can continue using the earlier cluster tasks.
a|
* If you continue using an earlier version of a cluster task, you might miss the latest features and critical security updates.
* The earlier versions of cluster tasks that are not operational consume cluster resources.
* * After it is upgraded, the Operator cannot manage the earlier VCT. You can delete the earlier VCT manually by using the `oc delete clustertask` command, but you cannot restore it.
|

|===

// This module is part of the following assembly:
//
// *cicd/pipelines/managing-nonversioned-and-versioned-cluster-tasks.adoc
[id="disabling-non-versioned-and-versioned-cluster-tasks_{context}"]
= Disabling non-versioned and versioned cluster tasks

As a cluster administrator, you can disable cluster tasks that the {pipelines-shortname} Operator installed.

.Procedure

. To delete all non-versioned cluster tasks and latest versioned cluster tasks, edit the `TektonConfig` custom resource definition (CRD) and set the `clusterTasks` parameter in `spec.addon.params` to `false`.
+
.Example `TektonConfig` CR
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  params:
  - name: createRbacResource
    value: "false"
  profile: all
  targetNamespace: openshift-pipelines
  addon:
    params:
    - name: clusterTasks
      value: "false"
...
----
+
When you disable cluster tasks, the Operator removes all the non-versioned cluster tasks and only the latest version of the versioned cluster tasks from the cluster.
+
[NOTE]
====
Re-enabling cluster tasks installs the non-versioned cluster tasks.
====

. Optional: To delete earlier versions of the versioned cluster tasks, use any one of the following methods:
.. To delete individual earlier versioned cluster tasks, use the `oc delete clustertask` command followed by the versioned cluster task name. For example:
+
[source,terminal]
----
$ oc delete clustertask buildah-1-6-0
----
.. To delete all versioned cluster tasks created by an old version of the Operator, you can delete the corresponding installer set. For example:
+
[source,terminal]
----
$ oc delete tektoninstallerset versioned-clustertask-1-6-k98as
----
+
[CAUTION]
====
If you delete an old versioned cluster task, you cannot restore it. You can only restore versioned and non-versioned cluster tasks that the current version of the Operator has created.
====
