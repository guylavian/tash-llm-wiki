---
title: "Configuring the registry for Red Hat OpenShift Data Foundation"
type: reference
domain: openshift
slug: registry-4-22-configuring-registry-storage-rhodf
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/configuring-registry-storage-rhodf
version: 4.22
family: registry
documentKind: "Documentation"
---

# Configuring the registry for Red Hat OpenShift Data Foundation

[id="configuring-registry-storage-rhodf"]
= Configuring the registry for Red Hat OpenShift Data Foundation

[role="_abstract"]
To configure the {product-registry} on bare metal and vSphere to use {rh-storage-first} storage, you must install {rh-storage} and then configure image registry using Ceph or Noobaa.

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc
//
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
//
// * registry/configuring_registry_storage/Configuring-the-registry-for-rhodf.adoc

[id="registry-configuring-registry-storage-rhodf-cephrgw_{context}"]
= Configuring the Image Registry Operator to use Ceph RGW storage with Red Hat OpenShift Data Foundation

[role="_abstract"]
{rh-storage-first} integrates multiple storage types that you can use with the {product-registry}:

* Ceph, a shared and distributed file system and on-premise object storage
* NooBaa, providing a Multicloud Object Gateway

Use the following, procedure to configure the image registry to use Ceph RGW storage.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift Container Platform web console.
* You installed the `oc` CLI.
* You installed the {rh-storage} Operator to provide object storage and Ceph RGW object storage.

.Procedure

. Create the object bucket claim using the `ocs-storagecluster-ceph-rgw` storage class. For example:
+
[source,terminal]
----
cat <<EOF | oc apply -f -
apiVersion: objectbucket.io/v1alpha1
kind: ObjectBucketClaim
metadata:
  name: rgwbucket
  namespace: openshift-storage
spec:
  storageClassName: ocs-storagecluster-ceph-rgw
  generateBucketName: rgwbucket
EOF
----
+
Alternatively, you can use the `openshift-image-registry` for the `namespace` value.

. Get the bucket name by entering the following command:
+
[source,terminal]
----
$ bucket_name=$(oc get obc -n openshift-storage rgwbucket -o jsonpath='{.spec.bucketName}')
----

. Get the AWS credentials by entering the following commands:
+
[source,terminal]
----
$ AWS_ACCESS_KEY_ID=$(oc get secret -n openshift-storage rgwbucket -o jsonpath='{.data.AWS_ACCESS_KEY_ID}' | base64 --decode)
----
+
[source,terminal]
----
$ AWS_SECRET_ACCESS_KEY=$(oc get secret -n openshift-storage rgwbucket -o jsonpath='{.data.AWS_SECRET_ACCESS_KEY}' | base64 --decode)
----

. Create the secret `image-registry-private-configuration-user` with the AWS credentials for the new bucket under `openshift-image-registry project` by entering the following command:
+
[source,terminal]
----
$ oc create secret generic image-registry-private-configuration-user --from-literal=REGISTRY_STORAGE_S3_ACCESSKEY=${AWS_ACCESS_KEY_ID} --from-literal=REGISTRY_STORAGE_S3_SECRETKEY=${AWS_SECRET_ACCESS_KEY} --namespace openshift-image-registry
----

. Get the `route` host by entering the following command:
+
[source,terminal]
----
$ route_host=$(oc get route ocs-storagecluster-cephobjectstore -n openshift-storage --template='{{ .spec.host }}')
----
+

. Create a config map that uses an ingress certificate by entering the following commands:
+
[source,terminal]
----
$ oc extract secret/$(oc get ingresscontroller -n openshift-ingress-operator default -o json | jq '.spec.defaultCertificate.name // "router-certs-default"' -r) -n openshift-ingress --confirm
----
+
[source,terminal]
----
$ oc create configmap image-registry-s3-bundle --from-file=ca-bundle.crt=./tls.crt  -n openshift-config
----

. Configure the image registry to use the Ceph RGW object storage by entering the following command:
+
[source,terminal]
----
$ oc patch config.image/cluster -p '{"spec":{"managementState":"Managed","replicas":2,"storage":{"managementState":"Unmanaged","s3":{"bucket":'\"${bucket_name}\"',"region":"us-east-1","regionEndpoint":'\"https://${route_host}\"',"virtualHostedStyle":false,"encrypt":false,"trustedCA":{"name":"image-registry-s3-bundle"}}}}}' --type=merge
----

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc
//
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
//
// * registry/configuring_registry_storage/Configuring-the-registry-for-rhodf.adoc

[id="registry-configuring-registry-storage-rhodf-nooba_{context}"]
= Configuring the Image Registry Operator to use Noobaa storage with Red Hat OpenShift Data Foundation

[role="_abstract"]
{rh-storage-first} integrates multiple storage types that you can use with the {product-registry}:

* Ceph, a shared and distributed file system and on-premise object storage
* NooBaa, providing a Multicloud Object Gateway

Use the following the procedure to configure the image registry to use Noobaa storage.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift Container Platform web console.
* You installed the `oc` CLI.
* You installed the {rh-storage} Operator to provide object storage and Noobaa object storage.

.Procedure

. Create the object bucket claim using the `openshift-storage.noobaa.io` storage class. For example:
+
[source,terminal]
----
cat <<EOF | oc apply -f -
apiVersion: objectbucket.io/v1alpha1
kind: ObjectBucketClaim
metadata:
  name: noobaatest
  namespace: openshift-storage
spec:
  storageClassName: openshift-storage.noobaa.io
  generateBucketName: noobaatest
EOF
----
+
Alternatively, you can use the `openshift-image-registry` for the `namespace` value.

. Get the bucket name by entering the following command:
+
[source,terminal]
----
$ bucket_name=$(oc get obc -n openshift-storage noobaatest -o jsonpath='{.spec.bucketName}')
----

. Get the AWS credentials by entering the following commands:
+
[source,terminal]
----
$ AWS_ACCESS_KEY_ID=$(oc get secret -n openshift-storage noobaatest -o yaml | grep -w "AWS_ACCESS_KEY_ID:" | head -n1 | awk '{print $2}' | base64 --decode)
----
+
[source,terminal]
----
$ AWS_SECRET_ACCESS_KEY=$(oc get secret -n openshift-storage noobaatest -o yaml | grep -w "AWS_SECRET_ACCESS_KEY:" | head -n1 | awk '{print $2}' | base64 --decode)
----

. Create the secret `image-registry-private-configuration-user` with the AWS credentials for the new bucket under `openshift-image-registry project` by entering the following command:
+
[source,terminal]
----
$ oc create secret generic image-registry-private-configuration-user --from-literal=REGISTRY_STORAGE_S3_ACCESSKEY=${AWS_ACCESS_KEY_ID} --from-literal=REGISTRY_STORAGE_S3_SECRETKEY=${AWS_SECRET_ACCESS_KEY} --namespace openshift-image-registry
----

. Get the route host by entering the following command:
+
[source,terminal]
----
$ route_host=$(oc get route s3 -n openshift-storage -o=jsonpath='{.spec.host}')
----
. Create a config map that uses an ingress certificate by entering the following commands:
+
[source,terminal]
----
$ oc extract secret/$(oc get ingresscontroller -n openshift-ingress-operator default -o json | jq '.spec.defaultCertificate.name // "router-certs-default"' -r) -n openshift-ingress --confirm
----
+
[source,terminal]
----
$ oc create configmap image-registry-s3-bundle --from-file=ca-bundle.crt=./tls.crt  -n openshift-config
----

. Configure the image registry to use the Nooba object storage by entering the following command:
+
[source,terminal]
----
$ oc patch config.image/cluster -p '{"spec":{"managementState":"Managed","replicas":2,"storage":{"managementState":"Unmanaged","s3":{"bucket":'\"${bucket_name}\"',"region":"us-east-1","regionEndpoint":'\"https://${route_host}\"',"virtualHostedStyle":false,"encrypt":false,"trustedCA":{"name":"image-registry-s3-bundle"}}}}}' --type=merge
----

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc
//
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
//
// * registry/configuring_registry_storage/Configuring-the-registry-for-rhodf.adoc

[id="registry-configuring-registry-storage-rhodf-cephfs_{context}"]
= Configuring the Image Registry Operator to use CephFS storage with Red Hat OpenShift Data Foundation

[role="_abstract"]
{rh-storage-first} integrates multiple storage types that you can use with the {product-registry}:

* Ceph, a shared and distributed file system and on-premise object storage
* NooBaa, providing a Multicloud Object Gateway

Use the following procedure to configure the image registry to use CephFS storage.

[NOTE]
====
CephFS uses persistent volume claim (PVC) storage. It is not recommended to use PVCs for image registry storage if there are other options are available, such as Ceph RGW or Noobaa.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift Container Platform web console.
* You installed the `oc` CLI.
* You installed the {rh-storage} Operator to provide object storage and CephFS file storage.

.Procedure

. Create a PVC to use the `cephfs` storage class. For example:
+
[source,terminal]
----
cat <<EOF | oc apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: registry-storage-pvc
 namespace: openshift-image-registry
spec:
 accessModes:
 - ReadWriteMany
 resources:
   requests:
     storage: 100Gi
 storageClassName: ocs-storagecluster-cephfs
EOF
----

. Configure the image registry to use the CephFS file system storage by entering the following command:
+
[source,terminal]
----
$ oc patch config.image/cluster -p '{"spec":{"managementState":"Managed","replicas":2,"storage":{"managementState":"Unmanaged","pvc":{"claim":"registry-storage-pvc"}}}}' --type=merge
----

[id="configuring-registry-storage-ocs"]
[role="_additional-resources"]
== Additional resources

* Configuring Image Registry to use {rh-storage}
* Performance tuning guide for Multicloud Object Gateway (NooBaa)
