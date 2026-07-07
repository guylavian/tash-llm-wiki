---
title: "Backing up workloads on OADP with {product-title}"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-rosa-backup-restore
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-rosa-backup-restore
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Backing up workloads on OADP with {product-title}

[id="oadp-rosa-backing-up-and-cleaning-example"]
= Backing up workloads on OADP with OpenShift Container Platform

[role="_abstract"]
To back up and restore workloads on ROSA, you can use {oadp-short}. You can create a backup of a workload, restore it from the backup, and verify the restoration. You can also clean up the {oadp-short} Operator, backup storage, and {aws-short} resources when they are no longer needed.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-rosa/oadp-rosa-backing-up-applications.adoc

[id="performing-a-backup-oadp-rosa-sts_{context}"]
= Example: Performing a backup with OADP and OpenShift Container Platform

[role="_abstract"]
Perform a backup by using {oadp-first} with OpenShift Container Platform. The following example `hello-world` application has no persistent volumes (PVs) attached.

Either Data Protection Application (DPA) configuration will work.

.Procedure

. Create a workload to back up by running the following commands:
+
[source,terminal]
----
$ oc create namespace hello-world
----
+
[source,terminal]
----
$ oc new-app -n hello-world --image=docker.io/openshift/hello-openshift
----

. Expose the route by running the following command:
+
[source,terminal]
----
$ oc expose service/hello-openshift -n hello-world
----

. Check that the application is working by running the following command:
+
[source,terminal]
----
$ curl `oc get route/hello-openshift -n hello-world -o jsonpath='{.spec.host}'`
----
+
You should see an output similar to the following example:
+
[source,terminal]
----
Hello OpenShift!
----

. Back up the workload by running the following command:
+
[source,terminal]
----
$ cat << EOF | oc create -f -
  apiVersion: velero.io/v1
  kind: Backup
  metadata:
    name: hello-world
    namespace: openshift-adp
  spec:
    includedNamespaces:
    - hello-world
    storageLocation: ${CLUSTER_NAME}-dpa-1
    ttl: 720h0m0s
EOF
----

. Wait until the backup is complete, and then run the following command:
+
[source,terminal]
----
$ watch "oc -n openshift-adp get backup hello-world -o json | jq .status"
----
+
You should see an output similar to the following example:
+
[source,json]
----
{
  "completionTimestamp": "2022-09-07T22:20:44Z",
  "expiration": "2022-10-07T22:20:22Z",
  "formatVersion": "1.1.0",
  "phase": "Completed",
  "progress": {
    "itemsBackedUp": 58,
    "totalItems": 58
  },
  "startTimestamp": "2022-09-07T22:20:22Z",
  "version": 1
}
----

. Delete the demo workload by running the following command:
+
[source,terminal]
----
$ oc delete ns hello-world
----

. Restore the workload from the backup by running the following command:
+
[source,terminal]
----
$ cat << EOF | oc create -f -
  apiVersion: velero.io/v1
  kind: Restore
  metadata:
    name: hello-world
    namespace: openshift-adp
  spec:
    backupName: hello-world
EOF
----

. Wait for the Restore to finish by running the following command:
+
[source,terminal]
----
$ watch "oc -n openshift-adp get restore hello-world -o json | jq .status"
----
+
You should see an output similar to the following example:
+
[source,json]
----
{
  "completionTimestamp": "2022-09-07T22:25:47Z",
  "phase": "Completed",
  "progress": {
    "itemsRestored": 38,
    "totalItems": 38
  },
  "startTimestamp": "2022-09-07T22:25:28Z",
  "warnings": 9
}
----

. Check that the workload is restored by running the following command:
+
[source,terminal]
----
$ oc -n hello-world get pods
----
+
You should see an output similar to the following example:
+
[source,terminal]
----
NAME                              READY   STATUS    RESTARTS   AGE
hello-openshift-9f885f7c6-kdjpj   1/1     Running   0          90s
----
. Check the JSONPath by running the following command:
+
[source,terminal]
----
$ curl `oc get route/hello-openshift -n hello-world -o jsonpath='{.spec.host}'`
----
+
You should see an output similar to the following example:
+
[source,terminal]
----
Hello OpenShift!
----
+
[NOTE]
====
For troubleshooting tips, see the troubleshooting documentation.
====

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-rosa/oadp-rosa-backing-up-applications.adoc

[id="cleanup-a-backup-oadp-rosa-sts_{context}"]
= Cleaning up a cluster after a backup with OADP and ROSA STS

[role="_abstract"]
Uninstall the {oadp-first} Operator together with the backups and the S3 bucket from the hello-world example.

.Procedure

. Delete the workload by running the following command:
+
[source,terminal]
----
$ oc delete ns hello-world
----

. Delete the Data Protection Application (DPA) by running the following command:
+
[source,terminal]
----
$ oc -n openshift-adp delete dpa ${CLUSTER_NAME}-dpa
----

. Delete the cloud storage by running the following command:
+
[source,terminal]
----
$ oc -n openshift-adp delete cloudstorage ${CLUSTER_NAME}-oadp
----

+
[WARNING]
====
If this command hangs, you might need to delete the finalizer by running the following command:

[source,terminal]
----
$ oc -n openshift-adp patch cloudstorage ${CLUSTER_NAME}-oadp -p '{"metadata":{"finalizers":null}}' --type=merge
----
====

. If the Operator is no longer required, remove it by running the following command:
+
[source,terminal]
----
$ oc -n openshift-adp delete subscription oadp-operator
----

. Remove the namespace from the Operator:
+
[source,terminal]
----
$ oc delete ns openshift-adp
----

. If the backup and restore resources are no longer required, remove them from the cluster by running the following command:
+
[source,terminal]
----
$ oc delete backups.velero.io hello-world
----

. To delete backup, restore and remote objects in {aws-short} S3 run the following command:
+
[source,terminal]
----
$ velero backup delete hello-world
----

. If you no longer need the Custom Resource Definitions (CRD), remove them from the cluster by running the following command:
+
[source,terminal]
----
$ for CRD in `oc get crds | grep velero | awk '{print $1}'`; do oc delete crd $CRD; done
----

. Delete the {aws-short} S3 bucket by running the following commands:
+
[source,terminal]
----
$ aws s3 rm s3://${CLUSTER_NAME}-oadp --recursive
----
+
[source,terminal]
----
$ aws s3api delete-bucket --bucket ${CLUSTER_NAME}-oadp
----

. Detach the policy from the role by running the following command:
+
[source,terminal]
----
$ aws iam detach-role-policy --role-name "${ROLE_NAME}"  --policy-arn "${POLICY_ARN}"
----

. Delete the role by running the following command:
+
[source,terminal]
----
$ aws iam delete-role --role-name "${ROLE_NAME}"
----
