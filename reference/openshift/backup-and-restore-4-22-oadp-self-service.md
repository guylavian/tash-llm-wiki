---
title: "{oadp-short} Self-Service"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-self-service
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-self-service
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# {oadp-short} Self-Service

[id="oadp-self-service"]
= {oadp-short} Self-Service

[role="_abstract"]
Use {oadp-short} Self-Service to enable namespace administrators to back up and restore their applications without cluster admin privileges. This helps you delegate backup operations while maintaining administrative control.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-overview_{context}"]
= About {oadp-short} Self-Service

[role="_abstract"]
From {oadp-short} 1.5.0 onward, you do not need the `cluster-admin` role to perform the backup and restore operations. You can use {oadp-short} with the namespace `admin` role. The namespace `admin` role has administrator access only to the namespace the user is assigned to.

You can use the Self-Service feature only after the cluster administrator installs the {oadp-short} Operator and provides the necessary permissions.

The {oadp-short} Self-Service feature provides secure self-service data protection capabilities for users without `cluster-admin` privileges while maintaining proper access controls.

The {oadp-short} cluster administrator creates a user with the namespace `admin` role and provides the necessary Role Based Access Controls (RBAC) to the user to perform {oadp-short} Self-Service actions. As this user has limited access compared to the `cluster-admin` role, this user is referred to as a namespace admin user.

As a namespace admin user, you can back up and restore applications deployed in your authorized namespace on the cluster.

{oadp-short} Self-Service offers the following benefits:

* As a cluster administrator:
** You allow namespace-scoped backup and restore operations to a namespace admin user. This means, a namespace admin user cannot access a namespace that they are not authorized to.
** You keep administrator control over non-administrator operations through `DataProtectionApplication` configuration and policies.

* As a namespace admin user:
** You can create backup and restore custom resources for your authorized namespace.
** You can create dedicated backup storage locations in your authorized namespace.
** You have secure access to backup logs and status information.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-overview-namespace-scope_{context}"]
= What namespace-scoped backup and restore means

[role="_abstract"]
{oadp-short} Self-Service ensures that namespace admin users can only operate within their authorized namespace. For example, if you do not have access to a namespace, as a namespace admin user, you cannot back up that namespace.

A namespace admin user cannot access backup and restore data of other users.

The cluster administrator enforces the access control through custom resources (CRs) that securely manage the backup and restore operations.

Additionally, the cluster administrator can control the allowed options within the CRs, restricting certain operations for added security by using `spec` enforcements in the `DataProtectionApplication` (DPA) CR.

Namespace `admin` users can perform the following Self-Service operations:

* Create and manage backups of their authorized namespaces.
* Restore data to their authorized namespaces.
* Configure their own backup storage locations.
* Check backup and restore status.
* Request retrieval of relevant logs.

[role="_additional-resources"]
.Additional resources

* Configuring an htpasswd identity provider

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-custom-resources_{context}"]
= {oadp-short} Self-Service custom resources

[role="_abstract"]
Use {oadp-short} Self-Service custom resources to control backup, restore, storage location, and download operations for namespace-scoped applications. This provides namespace administrators with self-service data protection tools.

The {oadp-short} Self-Service feature has the following new custom resources (CRs) to perform the backup and restore operations for a namespace admin user:

.Custom resources
|===
|*CR* |*Description*
|`NonAdminController` (NAC)| Controls and orchestrates the Self-Service operations.
|`NonAdminBackup` (NAB)| Manages namespace-scoped backup operations.
|`NonAdminRestore` (NAR)| Manages namespace-scoped restore operations.
|`NonAdminBackupStorageLocation` (NABSL)| Defines user-specific backup storage location.
|`NonAdminDownloadRequest` (NADR)| Manages namespace-scoped download request operations.
|===

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-how-it-works_{context}"]
= How {oadp-short} Self-Service works

[role="_abstract"]
Review how {oadp-short} Self-Service processes backup requests through the `NonAdminController` (NAC) custom resource, which validates namespace administrator requests and creates corresponding `Velero` backup objects.

The diagram describes the following workflow:

. A namespace admin user creates a `NonAdminBackup` (NAB) custom resource (CR) request.
. The `NonAdminController` (NAC) CR receives the NAB CR request.
. The NAC validates the request and updates the NAB CR about the request.
. The NAC creates the `Velero` backup object.
. The NAC monitors the `Velero` backup object and cascades the status back to the NAB CR.

.How {oadp-short} Self-Service works
image::oadp-self-service.svg[{oadp-short} Self-Service]

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-prerequisites_{context}"]
= {oadp-short} Self-Service prerequisites

[role="_abstract"]
Configure your cluster environment to enable {oadp-short} Self-Service backup and restore operations by meeting the following prerequisites. This helps namespace administrators perform data protection tasks in their assigned namespaces.

* The cluster administrator has configured the {oadp-short} `DataProtectionApplication` (DPA) CR to enable Self-Service.
* The cluster administrator has completed the following tasks:
** Created a namespace `admin` user account.
** Created a namespace for the namespace `admin` user.
** Assigned appropriate privileges for the namespace admin user's namespace. This ensures that the namespace admin user is authorized to access and perform backup and restore operations in their assigned namespace.
* Optionally, the cluster administrator can create a `NonAdminBackupStorageLocation` (NABSL) CR for the namespace `admin` user.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-namespace-permissions_{context}"]
= {oadp-short} Self-Service namespace permissions

[role="_abstract"]
Assign namespace permissions to namespace administrators to create and manage backup, restore, and storage location resources in their assigned namespaces. This grants namespace administrators the required access for Self-Service data protection operations.

As a cluster administrator, ensure that a namespace admin user has editor roles assigned for the following list of objects in their namespace.

* `nonadminbackups.oadp.openshift.io`
* `nonadminbackupstoragelocations.oadp.openshift.io`
* `nonadminrestores.oadp.openshift.io`
* `nonadmindownloadrequests.oadp.openshift.io`

For more details on the namespace `admin` role, see Default cluster roles.

A cluster administrator can also define their own specifications so that users can have rights similar to `project` or namespace `admin` roles.

[id="oadp-self-service-yaml-backup-operation_{context}"]
== Example RBAC YAML for backup operation

See the following role-based access control (RBAC) YAML file example with namespace permissions for a namespace `admin` user to perform a backup operation.

.Example RBAC manifest
[source,yaml]
----
...
- apiGroups:
      - oadp.openshift.io
    resources:
      - nonadminbackups
      - nonadminrestores
      - nonadminbackupstoragelocations
      - nonadmindownloadrequests
    verbs:
      - create
      - delete
      - get
      - list
      - patch
      - update
      - watch
  - apiGroups:
      - oadp.openshift.io
    resources:
      - nonadminbackups/status
      - nonadminrestores/status
    verbs:
      - get
----

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-unsupported-features_{context}"]
= {oadp-short} Self-Service limitations

[role="_abstract"]
Review the limitations and unsupported features of {oadp-short} Self-Service to understand which operations are restricted for namespace administrators. This helps you plan appropriate backup and restore strategies within the supported functionality.

The following features are not supported by {oadp-short} Self-Service:

* Cross cluster backup and restore, or migrations are not supported. These {oadp-short} operations are supported for the cluster administrator.

* A namespace `admin` user cannot create a `VolumeSnapshotLocation` (VSL) CR. The cluster administrator creates and configures the VSL in the `DataProtectionApplication` (DPA) CR for a namespace `admin` user.

* The `ResourceModifiers` CR and volume policies are not supported for a namespace `admin` user.

* A namespace `admin` user can request backup or restore logs by using the `NonAdminDownloadRequest` CR, only if the backup or restore is created by a user by using the `NonAdminBackupStorageLocation` CR.
+
If the backup or restore CRs are created by using the cluster-wide default backup storage location, a namespace `admin` user cannot request the backup or restore logs.

* To ensure secure backup and restore, {oadp-short} Self-Service automatically excludes the following CRs from being backed up or restored:

** `NonAdminBackup`
** `NonAdminRestore`
** `NonAdminBackupStorageLocation`
** `SecurityContextConstraints`
** `ClusterRole`
** `ClusterRoleBinding`
** `CustomResourceDefinition`
** `PriorityClasses`
** `VirtualMachineClusterInstanceTypes`
** `VirtualMachineClusterPreferences`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-phases_{context}"]
= {oadp-short} Self-Service backup and restore phases

[role="_abstract"]
Review the status phases of `NonAdminBackup` (NAB) and `NonAdminRestore` (NAR) custom resources to track the progress and state of backup and restore operations. This helps you monitor and troubleshoot Self-Service backup and restore requests.

The phase of the CRs only progress forward. Once a phase transitions to the next phase, it cannot revert to a previous phase.

.Phases
|===
|*Value* |*Description*
|`New`|A creation request of the NAB or NAR CR is accepted by the NAC, but it has not yet been validated by the NAC.
|`BackingOff`|NAB or NAR CR is invalidated by the NAC CR because of an invalid `spec` of the NAB or NAR  CR.

The namespace admin user can update the NAB or NAR `spec` to comply with the policies set by the administrator. After the namespace admin user edits the CRs, the NAC reconciles the CR again.
|`Created`|NAB or NAR CR is validated by the NAC, and the `Velero` backup or restore object is created.
|`Deletion`|NAB or NAR CR is marked for deletion. The NAC deletes the corresponding `Velero` backup or restore object. When the `Velero` object is deleted, the NAB or NAR CR is also deleted.
|===

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-self-service/oadp-self-service.adoc

[id="oadp-self-service-about-nabsl_{context}"]
= About NonAdminBackupStorageLocation CR

[role="_abstract"]
Review the `NonAdminBackupStorageLocation` (NABSL) custom resource (CR) workflows to understand how namespace administrators define backup storage locations through administrator creation, approval, or automatic processes. This helps you choose the appropriate workflow based on security requirements.

To ensure that the NABSL CR is created and used securely, use cluster administrator controls. The cluster administrator manages the NABSL CR to comply with company policies, and compliance requirements.

You can create a NABSL CR by using one of the following workflows:

* *Administrator creation workflow*: In this workflow, the cluster administrator creates the NABSL CR for the namespace admin user. The namespace admin user then references the NABSL in the `NonAdminBackup` CR.
* *Administrator approval workflow*: The cluster administrator must explicitly enable this opt-in feature in the DPA by setting the `nonAdmin.requireApprovalForBSL` field to `true`. The cluster administrator approval process works as follows:
.. A namespace admin user creates a NABSL CR. Because the administrator has enforced an approval process in the DPA, it triggers the creation of a `NonAdminBackupStorageLocationRequest` CR in the `openshift-adp` namespace.
.. The cluster administrator reviews the request and either approves or rejects the request.
** If approved, a `Velero` `BackupStorageLocation` (BSL) is created in the `openshift-adp` namespace, and the NABSL CR status is updated to reflect the approval.
** If rejected, the status of the NABSL CR is updated to reflect the rejection.
.. The cluster administrator can also revoke a previously approved NABSL CR. The `approve` field is set back to `pending` or `reject`. This results in the deletion of the `Velero` BSL, and the namespace admin user is notified of the rejection.
* *Automatic approval workflow*: In this workflow, the cluster administrator does not enforce an approval process for the NABSL CR by setting the `nonAdmin.requireApprovalForBSL` field in the DPA to `false`. The default value of this field is `false`. Not setting the field results in an automatic approval of the NABSL. Therefore, the namespace admin user can create the NABSL CR from their authorized namespace.

[IMPORTANT]
====
For security purposes, use either the administrator creation or the administrator approval workflow. The automatic approval workflow is less secure as it does not require administrator review.
====
