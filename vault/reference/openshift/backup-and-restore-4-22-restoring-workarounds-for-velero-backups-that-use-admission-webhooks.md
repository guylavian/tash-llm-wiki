---
title: "Restoring workarounds for Velero backups that use admission webhooks"
type: reference
domain: openshift
slug: backup-and-restore-4-22-restoring-workarounds-for-velero-backups-that-use-admission-webhooks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/restoring-workarounds-for-velero-backups-that-use-admission-webhooks
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Restoring workarounds for Velero backups that use admission webhooks

[id="restoring-workarounds-for-velero-backups-that-use-admission-webhooks"]
= Restoring workarounds for Velero backups that use admission webhooks

[role="_abstract"]
Resolve restore failures caused by admission webhooks by applying workarounds for workloads such as Knative and {ibm-title} AppConnect resources. This helps you to successfully restore workloads that have mutating or validating admission webhooks.

Velero has limited abilities to resolve admission webhook issues during a restore. If you have workloads with admission webhooks, you might need to use an additional Velero plugin or make changes to how you restore the workload. Typically, workloads with admission webhooks require you to create a resource of a specific kind first. This is especially true if your workload has child resources because admission webhooks typically block child resources.

For example, creating or restoring a top-level object such as `service.serving.knative.dev` typically creates child resources automatically. If you do this first, you will not need to use Velero to create and restore these resources. This avoids the problem of child resources being blocked by an admission webhook that Velero might use.

[NOTE]
====
Velero plugins are started as separate processes. After a Velero operation has completed, either successfully or not, it exits.
Receiving a `received EOF, stopping recv loop` message in the debug logs indicates that a plugin operation has completed. It does not mean that an error has occurred.
====

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/restoring-workarounds-for-velero-backups-that-use-admission-webhooks.adoc
//
[id="migration-debugging-velero-admission-webhooks-knative_{context}"]
= Restoring Knative resources

[role="_abstract"]
Resolve issues with restoring Knative resources that use admission webhooks by restoring the top-level `service.serving.knative.dev` service resource with Velero. This helps you to ensure that Knative resources are restored successfully without admission webhook errors.

.Procedure

* Restore the top level `service.serving.knative.dev Service` resource by using the following command:
+
[source,terminal]
----
$ velero restore <restore_name> \
  --from-backup=<backup_name> --include-resources \
  service.serving.knative.dev
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting/restoring-workarounds-for-velero-backups-that-use-admission-webhooks.adoc
[id="migration-debugging-velero-admission-webhooks-ibm-appconnect_{context}"]
= Restoring {ibm-title} AppConnect resources

[role="_abstract"]
Troubleshoot Velero restore failures for {ibm-name} AppConnect resources that use admission webhooks. Verify your webhook rules and check that the installed Operator supports the backup's version to successfully complete the restore.

.Procedure

. Check if you have any mutating admission plugins of `kind: MutatingWebhookConfiguration` in the cluster by entering/running the following command:
+
[source,terminal]
----
$ oc get mutatingwebhookconfigurations
----

. Examine the YAML file of each `kind: MutatingWebhookConfiguration` to ensure that none of its rules block creation of the objects that are experiencing issues. For more information, see the official Kubernetes documentation.

. Check that any `spec.version` in `type: Configuration.appconnect.ibm.com/v1beta1` used at backup time is supported by the installed Operator.

// Module included in the following assemblies:
// oadp-features-plugins-known-issues
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc
// * backup_and_restore/application_backup_and_restore/troubleshooting/restoring-workarounds-for-velero-backups-that-use-admission-webhooks.adoc
//

[id="avoiding-the-velero-plugin-panic-error_{context}"]
= Avoiding the Velero plugin panic error

[role="_abstract"]
Label a custom Backup Storage Location (BSL) to resolve Velero plugin panic errors during `imagestream` backups. This helps you to ensure the {oadp-short} controller creates the required registry secret when you manage the BSL outside the `DataProtectionApplication` (DPA) CR.

A missing secret can cause a panic error for the Velero plugin during image stream backups. When the backup and the BSL are managed outside the scope of the DPA, the OADP controller does not create the relevant `oadp-<bsl_name>-<bsl_provider>-registry-secret` parameter.

During the backup operation, the OpenShift Velero plugin panics on the `imagestream` backup, with the following panic error:

[source,text]
----
024-02-27T10:46:50.028951744Z time="2024-02-27T10:46:50Z" level=error msg="Error backing up item"
backup=openshift-adp/<backup name> error="error executing custom action (groupResource=imagestreams.image.openshift.io,
namespace=<BSL Name>, name=postgres): rpc error: code = Aborted desc = plugin panicked:
runtime error: index out of range with length 1, stack trace: goroutine 94…
----

.Procedure

. Label the custom BSL with the relevant label by using the following command:
+
[source,terminal]
----
$ oc label backupstoragelocations.velero.io <bsl_name> app.kubernetes.io/component=bsl
----

. After the BSL is labeled, wait until the DPA reconciles.
+
[NOTE]
====
You can force the reconciliation by making any minor change to the DPA itself.
====

.Verification

* After the DPA is reconciled, confirm that the parameter has been created and that the correct registry data has been populated into it by entering the following command:
+
[source,terminal]
----
$ oc -n openshift-adp get secret/oadp-<bsl_name>-<bsl_provider>-registry-secret -o json | jq -r '.data'
----

// Module included in the following assemblies:
// oadp-features-plugins-known-issues
// * backup_and_restore/application_backup_and_restore/oadp-features-plugins.adoc
// * backup_and_restore/application_backup_and_restore/troubleshooting/restoring-workarounds-for-velero-backups-that-use-admission-webhooks.adoc
//

[id="workaround-for-openshift-adp-controller-segmentation-fault_{context}"]
= Workaround for OpenShift ADP Controller segmentation fault

[role="_abstract"]
Define either `velero` or `cloudstorage` in your Data Protection Application (DPA) configuration to prevent indefinite pod crashes. This configuration resolves a segmentation fault in the `openshift-adp-controller-manager` pod that occurs when both components are enabled.

The `openshift-adp-controller-manager` pod fails with a crash loop segmentation fault due to the following settings:

* If you define both `velero` and `cloudstorage`, the `openshift-adp-controller-manager` fails.
* If you do not define both `velero` and `cloudstorage`, the `openshift-adp-controller-manager` fails.

See _OADP-1054_ for more information.

[role="_additional-resources"]
.Additional resources

* OADP-1054

[role="_additional-resources"]
.Additional resources
* Admission plugins

* Webhook admission plugins

* Types of webhook admission plugins
