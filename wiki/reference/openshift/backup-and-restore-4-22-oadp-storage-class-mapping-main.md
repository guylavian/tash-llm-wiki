---
title: "OADP storage class mapping"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-storage-class-mapping-main
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-storage-class-mapping-main
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# OADP storage class mapping

[id="oadp-storage-class-mapping-main"]
= OADP storage class mapping

[role="_abstract"]
Map your storage classes with {oadp-full} to define rules for how different data types are stored. This helps you automate storage assignments to optimize cost and efficiency during backup and restore operations.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-advanced-topics/oadp-storage-class-mapping-main.adoc

[id="oadp-storage-class-mapping_{context}"]
= Storage class mapping

[role="_abstract"]
Define rules for your storage classes to automate how different data types are stored. Mapping your storage classes helps optimize your storage efficiency and lower costs based on access frequency and data importance.

Storage class mapping allows you to define rules or policies specifying which storage class should be applied to different types of data. This feature automates the process of determining storage classes based on access frequency, data importance, and cost considerations. It optimizes storage efficiency and cost-effectiveness by ensuring that data is stored in the most suitable storage class for its characteristics and usage patterns.

You can use the `change-storage-class-config` field to change the storage class of your data objects, which lets you optimize costs and performance by moving data between different storage tiers, such as from standard to archival storage, based on your needs and access patterns.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-advanced-topics/oadp-storage-class-mapping-main.adoc

[id="oadp-storage-class-mapping-oadp_{context}"]
= Mapping storage classes with OADP

[role="_abstract"]
Change the storage class of a persistent volume (PV) during a restore by configuring a storage class mapping in the Velero namespace. This helps you customize storage destinations when recovering applications with {oadp-short}.

To deploy ConfigMap with OADP, use the `change-storage-class-config` field. You must change the storage class mapping based on your cloud provider.

.Procedure
. Change the storage class mapping by running the following command:
+
[source,terminal]
----
$ cat change-storageclass.yaml
----
. Create a config map in the Velero namespace as shown in the following example:
+
.Example
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: change-storage-class-config
  namespace: openshift-adp
  labels:
    velero.io/plugin-config: ""
    velero.io/change-storage-class: RestoreItemAction
data:
  standard-csi: ssd-csi
----
. Save your storage class mapping preferences by running the following command:
+
[source,terminal]
----
$ oc create -f change-storage-class-config
----
