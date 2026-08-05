---
title: "Backing up and restoring 3scale API Management by using OADP"
type: reference
domain: openshift
slug: backup-and-restore-4-22-backing-up-and-restoring-3scale-api-management-by-using-oadp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/backing-up-and-restoring-3scale-api-management-by-using-oadp
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Backing up and restoring 3scale API Management by using OADP

[id="backing-up-and-restoring-3scale-api-management-by-using-oadp"]
= Backing up and restoring 3scale API Management by using OADP

[role="_abstract"]
Back up and restore Red{nbsp}Hat 3scale API Management deployments by using {oadp-first} to protect application resources, persistent volumes, and configurations. This helps you to safeguard your 3scale components for disaster recovery.

You can deploy 3scale components on-premise, in the cloud, as a managed service, or in any combination based on your requirements.

With {oadp-first}, you can safeguard 3scale API Management deployments by backing up application resources, persistent volumes, and configurations.

[NOTE]
====
You can use the {oadp-first} Operator to back up and restore your 3scale API Management on-cluster storage databases without affecting your running services
====

You can configure {oadp-short} to perform the following operations with 3scale API Management:

* Create a backup of 3scale components. For more details, see _Backing up 3scale API Management_.

* Restore the components to scale up the 3scale operator and deployment. For more details, see _Restoring 3scale API Management_.

[role="_additional-resources"]
.Additional resources

* Backing up 3scale API Management

* Restoring 3scale API Management
