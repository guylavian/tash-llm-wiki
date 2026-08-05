---
title: "{oadp-short} Self-Service cluster admin use cases"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-self-service-cluster-admin-use-cases
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-self-service-cluster-admin-use-cases
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# {oadp-short} Self-Service cluster admin use cases

[id="oadp-self-service-cluster-admin-use-cases"]
= {oadp-short} Self-Service cluster admin use cases

[role="_abstract"]
Configure and manage {oadp-short} Self-Service by enabling the feature, reviewing backup storage location requests, and enforcing policy templates. This helps you provide Self-Service backup capabilities while maintaining administrative control.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service-cluster-admin-use-cases.adoc

[id="oadp-self-service-admin-enable-disable_{context}"]
= Enabling and disabling {oadp-short} Self-Service

[role="_abstract"]
Enable or disable the {oadp-short} Self-Service feature to allow namespace administrators to manage their own backup and restore operations without cluster admin privileges. This helps you delegate backup responsibilities while maintaining administrative control.

[NOTE]
====
You can install only one instance of the `NonAdminController` (NAC) CR in the cluster. If you install multiple instances of the NAC CR, you get the following error:

[source,terminal]
----
message: only a single instance of Non-Admin Controller can be installed across the entire cluster. Non-Admin controller is already configured and installed in openshift-adp namespace.
----
====

.Prerequisites

* You are logged in to the cluster with the `cluster-admin` role.
* You have installed the {oadp-short} Operator.
* You have configured the DPA.

.Procedure

* To enable {oadp-short} Self-Service, edit the DPA CR to configure the `nonAdmin.enable` section. See the following example configuration:
+
.Example `DataProtectionApplication` CR
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: oadp-backup
  namespace: openshift-adp
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    velero:
      defaultPlugins:
        - aws
        - openshift
        - csi
      defaultSnapshotMoveData: true
  nonAdmin:
    enable: true
  backupLocations:
    - velero:
        config:
          profile: "default"
          region: noobaa
          s3Url: https://s3.openshift-storage.svc
          s3ForcePathStyle: "true"
          insecureSkipTLSVerify: "true"
        provider: aws
        default: true
        credential:
          key: cloud
          name:  <cloud_credentials>
        objectStorage:
          bucket: <bucket_name>
          prefix: oadp
----
+
where:
+
`nonAdmin`:: Specifies the section in the `spec` section of the DPA to enable or disable the Self-Service feature.
`enable`:: Specifies whether to enable the Self-Service feature. Set to `true` to enable the feature. Set to `false` to disable the feature.

.Verification

* To verify that the `NonAdminController` (NAC) pod is running in the {oadp-short} namespace, run the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-adp -l control-plane=non-admin-controller
----
+
.Example output
[source,terminal]
----
NAME                                  READY   STATUS    RESTARTS   AGE
non-admin-controller-5d....f5-p..9p   1/1     Running   0          99m
----

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service-cluster-admin-use-cases.adoc

[id="oadp-self-service-enabling-nabsl-approval_{context}"]
= Enabling NonAdminBackupStorageLocation administrator approval workflow

[role="_abstract"]
Enable the administrator approval workflow for `NonAdminBackupStorageLocation` custom resource to review backup storage location requests from namespace administrators before they are applied. This helps you maintain control over backup storage configurations.

.Prerequisites

* You are logged in to the cluster with the `cluster-admin` role.
* You have installed the {oadp-short} Operator.
* You have enabled {oadp-short} Self-Service in the `DataProtectionApplication` CR.

.Procedure

* To enable the NABSL administrator approval workflow, edit the DPA CR by using the following example configuration:
+
.Example `DataProtectionApplication` CR
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: oadp-backup
  namespace: openshift-adp
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    velero:
      defaultPlugins:
        - aws
        - openshift
        - csi
      noDefaultBackupLocation: true
  nonAdmin:
    enable: true
    requireApprovalForBSL: true
----
+
where:
+
`noDefaultBackupLocation`:: Specifies that there is no default backup storage location configured in the DPA CR. Set to `true` to enable the namespace admin user to create a NABSL CR and send the CR request for approval.
`requireApprovalForBSL`:: Specifies whether the NABSL administrator approval workflow is enabled. Set to `true` to enable the approval workflow.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service-cluster-admin-use-cases.adoc

[id="oadp-self-service-approving-nabsl_{context}"]
= Approving a NonAdminBackupStorageLocation request

[role="_abstract"]
Approve `NonAdminBackupStorageLocation` (NABSL) custom resource requests from namespace administrators to grant access to their specified backup storage locations. This enables self-service backup and restore operations for namespace resources.

.Prerequisites

* You are logged in to the cluster with the `cluster-admin` role.
* You have installed the {oadp-short} Operator.
* You have enabled {oadp-short} Self-Service in the `DataProtectionApplication` (DPA) CR.
* You have enabled the NABSL CR approval workflow in the DPA.

.Procedure

. To see the NABSL CR requests that are in queue for administrator approval, run the following command:
+
[source,terminal]
----
$ oc -n openshift-adp get NonAdminBackupStorageLocationRequests
----
+
.Example output
[source,terminal]
----
NAME                          REQUEST-PHASE   REQUEST-NAMESPACE     REQUEST-NAME               AGE
non-admin-bsl-test-.....175   Approved        non-admin-bsl-test    incorrect-bucket-nabsl    4m57s
non-admin-bsl-test-.....196   Approved        non-admin-bsl-test    perfect-nabsl             5m26s
non-admin-bsl-test-s....e1a   Rejected        non-admin-bsl-test    suspicious-sample         2m56s
non-admin-bsl-test-.....5e0   Pending         non-admin-bsl-test    waitingapproval-nabsl     4m20s
----

. To approve the NABSL CR request, set the `approvalDecision` field to `approve` by running the following command:
+
[source,terminal]
----
$ oc patch nabslrequest <nabsl_name> -n openshift-adp --type=merge -p '{"spec": {"approvalDecision": "approve"}}'
----
Replace `<nabsl_name>` with the name of the `NonAdminBackupStorageLocationRequest` CR.

.Verification

* Verify that the Velero backup storage location is created and the phase is `Available` by running the following command:
+
[source,terminal]
----
$ oc get velero.io.backupstoragelocation
----
+
.Example output

[source,terminal]
----
NAME                         PHASE       LAST VALIDATED   AGE   DEFAULT
test-nac-test-bsl-cd...930   Available   62s              62s
----

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service-cluster-admin-use-cases.adoc

[id="oadp-self-service-rejecting-nabsl_{context}"]
= Rejecting a NonAdminBackupStorageLocation request

[role="_abstract"]
Reject `NonAdminBackupStorageLocation` (NABSL) custom resource (CR) requests from namespace administrators to deny access to backup storage locations that do not meet requirements. This helps you maintain security and compliance standards.

.Prerequisites

* You are logged in to the cluster with the `cluster-admin` role.
* You have installed the {oadp-short} Operator.
* You have enabled {oadp-short} Self-Service in the `DataProtectionApplication` (DPA) CR.
* You have enabled the NABSL CR approval workflow in the DPA.

.Procedure

. To see the NABSL CR requests that are in queue for administrator approval, run the following command:
+
[source,terminal]
----
$ oc -n openshift-adp get NonAdminBackupStorageLocationRequests
----
+
.Example output

[source,terminal]
----
$ oc get nabslrequest
NAME                          REQUEST-PHASE   REQUEST-NAMESPACE     REQUEST-NAME               AGE
non-admin-bsl-test-.....175   Approved        non-admin-bsl-test    incorrect-bucket-nabsl    4m57s
non-admin-bsl-test-.....196   Approved        non-admin-bsl-test    perfect-nabsl             5m26s
non-admin-bsl-test-s....e1a   Rejected        non-admin-bsl-test    suspicious-sample         2m56s
non-admin-bsl-test-.....5e0   Pending         non-admin-bsl-test    waitingapproval-nabsl     4m20s
----

. To reject the NABSL CR request, set the `approvalDecision` field to `reject` by running the following command:
+
[source,terminal]
----
$ oc patch nabslrequest <nabsl_name> -n openshift-adp --type=merge -p '{"spec": {"approvalDecision": "reject"}}'
----
Replace `<nabsl_name>` with the name of the `NonAdminBackupStorageLocationRequest` CR.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service-cluster-admin-use-cases.adoc

[id="oadp-self-service-admin-spec-enforcement_{context}"]
= {oadp-short} Self-Service administrator DPA spec enforcement

[role="_abstract"]
Enforce policy templates in the `DataProtectionApplication` (DPA) custom resource (CR) to control `NonAdminBackup`, `NonAdminRestore`, and `NonAdminBackupStorageLocation` custom resources created by namespace administrators. This helps you maintain compliance standards.

The cluster administrator can enforce a company, or a compliance policy by using the following fields in the `DataProtectionApplication` (DPA) CR:

`enforceBSLSpec`:: To enforce a policy on the `NonAdminBackupStorageLocation` CR.
`enforceBackupSpec`:: To enforce a policy on the `NonAdminBackup` CR.
`enforceRestoreSpec`:: To enforce a policy on the `NonAdminRestore` CR.

By using the enforceable fields, administrators can ensure that the NABSL, NAB, and NAR CRs created by a namespace admin user, comply with the administrator defined policy.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service-cluster-admin-use-cases.adoc

[id="oadp-self-service-admin-spec-enforce-nabsl_{context}"]
= Self-Service administrator spec enforcement for NABSL

[role="_abstract"]
Enforce specific fields in `NonAdminBackupStorageLocation` (NABSL) custom resource (CR) to control storage bucket, credentials, configuration, access mode, and validation settings used by namespace administrators. This helps you maintain organizational policies.

You can enforce the following fields for a NABSL:

* `objectStorage`
* `credential`
* `config`
* `accessMode`
* `validationFrequency`

For example, if you want to enforce a namespace admin user to use a specific storage bucket, you can set up the `DataProtectionApplication` (DPA) CR as following:

.Example `DataProtectionApplication` CR
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
spec:
  nonAdmin:
    enable: true
    enforceBSLSpec:
      config:
        checksumAlgorithm: ""
        profile: default
        region: us-west-2
      objectStorage:
        bucket: my-company-bucket
        prefix: velero
      provider: aws
----

where:

`enforceBSLSpec`:: Specifies the section to enforce policies for the `NonAdminBackupStorageLocation` CR.
`config`:: Specifies the configuration to enforce for the NABSL. In this example, it enforces the use of an {aws-short} S3 bucket in the `us-west-2` region.
`objectStorage`:: Specifies the object storage settings to use a company bucket named `my-company-bucket`.

When a namespace admin user creates a NABSL, they must follow the template set up in the DPA. Otherwise, the `status.phase` field on the NABSL CR is set to `BackingOff` and the NABSL fails to create.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service-cluster-admin-use-cases.adoc

[id="oadp-self-service-admin-spec-enforce-nab_{context}"]
= Self-Service administrator spec enforcement for NAB

[role="_abstract"]
Enforce specific fields in `NonAdminBackup` (NAB) custom resource (CR) to control timeout settings, resource policies, label selectors, snapshot configurations, and time-to-live values used by namespace administrators. This helps you maintain backup standards.

You can enforce the following fields for a NAB CR:

* `csiSnapshotTimeout`
* `itemOperationTimeout`
* `resourcePolicy`
* `includedResources`
* `excludedResources`
* `orderedResources`
* `includeClusterResources`
* `excludedClusterScopedResources`
* `excludedNamespaceScopedResources`
* `includedNamespaceScopedResources`
* `labelSelector`
* `orLabelSelectors`
* `snapshotVolumes`
* `ttl`
* `snapshotMoveData`
* `uploaderConfig.parallelFilesUpload`

If you want to enforce a `ttl` value and a Data Mover backup for a namespace admin user, you can set up the `DataProtectionApplication` (DPA) CR as shown in the following example:

.Example `DataProtectionApplication` CR
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
spec:
  nonAdmin:
    enable: true
    enforceBackupSpec:
      snapshotMoveData: true
      ttl: 158h0m0s
----

where:

`enforceBackupSpec`:: Specifies the section to enforce policies for the `NonAdminBackup` CR.
`snapshotMoveData`:: Specifies whether to enforce Data Mover. Set to `true` to enforce Data Mover backups.
`ttl`:: Specifies the time-to-live value to enforce for backups. In this example, it is set to `158h0m0s`.

When a namespace admin user creates a NAB CR, they must follow the template set up in the DPA. Otherwise, the `status.phase` field on the NAB CR is set to `BackingOff` and the NAB CR fails to create.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service-cluster-admin-use-cases.adoc

[id="oadp-self-service-admin-spec-enforce-nar_{context}"]
= Self-Service administrator spec enforcement for NAR

[role="_abstract"]
Enforce specific fields in `NonAdminRestore` (NAR) custom resource (CR) to control timeout settings, resource policies, label selectors, persistent volume restoration, and node port configurations used by namespace administrators. This helps you maintain restore standards.

You can enforce the following fields for a NAR CR:

* `itemOperationTimeout`
* `uploaderConfig`
* `includedResources`
* `excludedResources`
* `restoreStatus`
* `includeClusterResources`
* `labelSelector`
* `orLabelSelectors`
* `restorePVs`
* `preserveNodePorts`
