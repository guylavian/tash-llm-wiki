---
title: "Backing up 3scale API Management by using OADP"
type: reference
domain: openshift
slug: backup-and-restore-4-22-backing-up-3scale-api-management-by-using-oadp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/backing-up-3scale-api-management-by-using-oadp
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Backing up 3scale API Management by using OADP

[id="backing-up-3scale-api-management-by-using-oadp"]
= Backing up 3scale API Management by using OADP

[role="_abstract"]
Back up Red{nbsp}Hat 3scale API Management components, including the 3scale Operator, MySQL database, and Redis database, by using {oadp-first}. This helps you protect your API management infrastructure and provides recovery in case of data loss.

For more information about installing and configuring Red{nbsp}Hat 3scale API Management, see _Installing 3scale API Management on OpenShift_ and _Red Hat 3scale API Management_.

//included in backing-up-3scale-api-management-by-using-oadp.adoc assembly

[id="creating-the-data-protection-application_{context}"]
= Creating the Data Protection Application

[role="_abstract"]
Create a Data Protection Application (DPA) custom resource (CR) to configure backup storage and Velero settings for Red{nbsp}Hat 3scale API Management. This helps you set up the backup infrastructure required for protecting your 3scale components.

.Procedure

. Create a YAML file with the following configuration:
+
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: dpa-sample
  namespace: openshift-adp
spec:
  configuration:
    velero:
      defaultPlugins:
        - openshift
        - aws
        - csi
      resourceTimeout: 10m
    nodeAgent:
      enable: true
      uploaderType: kopia
  backupLocations:
    - name: default
      velero:
        provider: aws
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: <prefix>
        config:
          region: <region>
          profile: "default"
          s3ForcePathStyle: "true"
          s3Url: <s3_url>
        credential:
          key: cloud
          name: cloud-credentials
----
+
where:
+
`<bucket_name>`:: Specifies a bucket as the backup storage location. If the bucket is not a dedicated bucket for Velero backups, you must specify a prefix.
`<prefix>`:: Specifies a prefix for Velero backups, for example, `velero`, if the bucket is used for multiple purposes.
`<region>`:: Specifies a region for backup storage location.
`<s3_url>`:: Specifies the URL of the object store that you are using to store backups.

. Create the DPA CR by running the following command:
+
[source,terminal]
----
$ oc create -f dpa.yaml
----

//included in backing-up-3scale-api-management-by-using-oadp.adoc assembly

[id="backing-up-the-3scale-operator-secret-apimanager_{context}"]
= Backing up the 3scale API Management operator, secret, and APIManager

[role="_abstract"]
Back up the Red{nbsp}Hat 3scale API Management operator resources, including the `Secret` and APIManager custom resources (CRs), by creating backup CRs. This helps you preserve your 3scale operator configuration for recovery scenarios.

.Prerequisites

* You created the Data Protection Application (DPA).

.Procedure

. Back up your 3scale operator CRs, such as `operatorgroup`, `namespaces`, and `subscriptions`, by creating a YAML file with the following configuration:
+

[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: operator-install-backup
  namespace: openshift-adp
spec:
  csiSnapshotTimeout: 10m0s
  defaultVolumesToFsBackup: false
  includedNamespaces:
  - threescale
  includedResources:
  - operatorgroups
  - subscriptions
  - namespaces
  itemOperationTimeout: 1h0m0s
  snapshotMoveData: false
  ttl: 720h0m0s
----
+
where:
+
`operator-install-backup`:: Specifies the value of the `metadata.name` parameter in the backup. This is the same value used in the `metadata.backupName` parameter used when restoring the 3scale operator.
`threescale`:: Specifies the namespace where the 3scale operator is installed.
+
[NOTE]
====
You can also back up and restore `ReplicationControllers`, `Deployment`, and `Pod` objects to ensure that all manually set environments are backed up and restored. This does not affect the flow of restoration.
====

. Create a backup CR by running the following command:
+
[source,terminal]
----
$ oc create -f backup.yaml
----
+
.Example output

[source,terminal]
----
backup.velero.io/operator-install-backup created
----

. Back up the `Secret` CR by creating a YAML file with the following configuration:
+

[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: operator-resources-secrets
  namespace: openshift-adp
spec:
  csiSnapshotTimeout: 10m0s
  defaultVolumesToFsBackup: false
  includedNamespaces:
  - threescale
  includedResources:
  - secrets
  itemOperationTimeout: 1h0m0s
  labelSelector:
    matchLabels:
      app: 3scale-api-management
  snapshotMoveData: false
  snapshotVolumes: false
  ttl: 720h0m0s
----
+
`name`:: Specifies the value of the `metadata.name` parameter in the backup. Use this value in the `metadata.backupName` parameter when restoring the `Secret`.

. Create the `Secret` backup CR by running the following command:
+
[source,terminal]
----
$ oc create -f backup-secret.yaml
----
+
.Example output

[source,terminal]
----
backup.velero.io/operator-resources-secrets created
----

. Back up the APIManager CR by creating a YAML file with the following configuration:
+

[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: operator-resources-apim
  namespace: openshift-adp
spec:
  csiSnapshotTimeout: 10m0s
  defaultVolumesToFsBackup: false
  includedNamespaces:
  - threescale
  includedResources:
  - apimanagers
  itemOperationTimeout: 1h0m0s
  snapshotMoveData: false
  snapshotVolumes: false
  storageLocation: ts-dpa-1
  ttl: 720h0m0s
  volumeSnapshotLocations:
  - ts-dpa-1
----
+
`name`:: Specifies the value of the `metadata.name` parameter in the backup. Use this value in the `metadata.backupName` parameter when restoring the APIManager.

. Create the APIManager CR by running the following command:
+
[source,terminal]
----
$ oc create -f backup-apimanager.yaml
----
+
.Example output

[source,terminal]
----
backup.velero.io/operator-resources-apim created
----

//included in backing-up-3scale-api-management-by-using-oadp.adoc assembly

[id="backing-up-the-mysql-database_{context}"]
= Backing up a MySQL database

[role="_abstract"]
Back up a MySQL database by creating a persistent volume claim (PVC) to store the database dump. This helps you preserve your 3scale system database data for recovery scenarios.

.Prerequisites

* You have backed up the Red{nbsp}Hat 3scale API Management operator.

.Procedure

. Create a YAML file with the following configuration for adding an additional PVC:
+

[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: example-claim
  namespace: threescale
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: gp3-csi
  volumeMode: Filesystem
----

. Create the additional PVC by running the following command:
+
[source,terminal]
----
$ oc create -f ts_pvc.yml
----

. Attach the PVC to the system database pod by editing the `system-mysql` deployment to use the MySQL dump:
+
[source,terminal]
----
$ oc edit deployment system-mysql -n threescale
----
+
[source,yaml]
----
  volumeMounts:
    - name: example-claim
      mountPath: /var/lib/mysqldump/data
    - name: mysql-storage
      mountPath: /var/lib/mysql/data
    - name: mysql-extra-conf
      mountPath: /etc/my-extra.d
    - name: mysql-main-conf
      mountPath: /etc/my-extra
    ...
      serviceAccount: amp
  volumes:
        - name: example-claim
          persistentVolumeClaim:
            claimName: example-claim
    ...
----
+
`claimName`:: Specifies the PVC that contains the dumped data.

. Create a YAML file with following configuration to back up the MySQL database:
+

[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: mysql-backup
  namespace: openshift-adp
spec:
  csiSnapshotTimeout: 10m0s
  defaultVolumesToFsBackup: true
  hooks:
    resources:
    - name: dumpdb
      pre:
      - exec:
          command:
          - /bin/sh
          - -c
          - mysqldump -u $MYSQL_USER --password=$MYSQL_PASSWORD system --no-tablespaces
            > /var/lib/mysqldump/data/dump.sql
          container: system-mysql
          onError: Fail
          timeout: 5m
  includedNamespaces:
  - threescale
  includedResources:
  - deployment
  - pods
  - replicationControllers
  - persistentvolumeclaims
  - persistentvolumes
  itemOperationTimeout: 1h0m0s
  labelSelector:
    matchLabels:
      app: 3scale-api-management
      threescale_component_element: mysql
  snapshotMoveData: false
  ttl: 720h0m0s
----
+
where:
+
`mysql-backup`:: Specifies the value of the `metadata.name` parameter in the backup. Use this value in the `metadata.backupName` parameter when restoring the MySQL database.
`/var/lib/mysqldump/data/dump.sql`:: Specifies the directory where the data is backed up.
`includedResources`:: Specifies the resources to back up.

. Back up the MySQL database by running the following command:
+
[source,terminal]
----
$ oc create -f mysql.yaml
----
+
.Example output

[source,terminal]
----
backup.velero.io/mysql-backup created
----

.Verification

* Verify that the MySQL backup is completed by running the following command:
+
[source,terminal]
----
$ oc get backups.velero.io mysql-backup -o yaml
----
+
.Example output

[source,terminal]
----
status:
completionTimestamp: "2025-04-17T13:25:19Z"
errors: 1
expiration: "2025-05-17T13:25:16Z"
formatVersion: 1.1.0
hookStatus: {}
phase: Completed
progress: {}
startTimestamp: "2025-04-17T13:25:16Z"
version: 1
----

//included in backing-up-3scale-api-management-by-using-oadp.adoc assembly

[id="backing-up-the-backend-redis-database_{context}"]
= Backing up the back-end Redis database

[role="_abstract"]
Back up the back-end Redis database by configuring Velero annotations and creating a backup CR with the required resources. This helps you preserve your 3scale back-end Redis data for recovery scenarios.

.Prerequisites

* You backed up the Red{nbsp}Hat 3scale API Management operator.
* You backed up your MySQL database.
* The Redis queues have been drained before performing the backup.

.Procedure

. Edit the annotations on the `backend-redis` deployment by running the following command:
+
[source, terminal]
----
$ oc edit deployment backend-redis -n threescale
----
+
[source,yaml]
----
annotations:
post.hook.backup.velero.io/command: >-
         ["/bin/bash", "-c", "redis-cli CONFIG SET auto-aof-rewrite-percentage
         100"]
       pre.hook.backup.velero.io/command: >-
         ["/bin/bash", "-c", "redis-cli CONFIG SET auto-aof-rewrite-percentage
         0"]
----

. Create a YAML file with the following configuration to back up the Redis database:
+

[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: redis-backup
  namespace: openshift-adp
spec:
  csiSnapshotTimeout: 10m0s
  defaultVolumesToFsBackup: true
  includedNamespaces:
  - threescale
  includedResources:
  - deployment
  - pods
  - replicationcontrollers
  - persistentvolumes
  - persistentvolumeclaims
  itemOperationTimeout: 1h0m0s
  labelSelector:
    matchLabels:
      app: 3scale-api-management
      threescale_component: backend
      threescale_component_element: redis
  snapshotMoveData: false
  snapshotVolumes: false
  ttl: 720h0m0s
----
+
`name`:: Specifies the value of the `metadata.name` parameter in the backup. Use this value in the `metadata.backupName` parameter when restoring the Redis database.

. Back up the Redis database by running the following command:
+
[source,terminal]
----
$ oc create -f redis-backup.yaml
----
+
.Example output

[source,terminal]
----
backup.velero.io/redis-backup created
----

.Verification

* Verify that the Redis backup is completed by running the following command:
+
[source,terminal]
----
$ oc get backups.velero.io redis-backup -o yaml
----
+
.Example output

[source,terminal]
----
status:
completionTimestamp: "2025-04-17T13:25:19Z"
errors: 1
expiration: "2025-05-17T13:25:16Z"
formatVersion: 1.1.0
hookStatus: {}
phase: Completed
progress: {}
startTimestamp: "2025-04-17T13:25:16Z"
version: 1
----

[role="_additional-resources"]
.Additional resources

* Installing 3scale API Management on OpenShift

* Red Hat 3scale API Management

* Installing the Data Protection Application

* Creating a Backup CR
