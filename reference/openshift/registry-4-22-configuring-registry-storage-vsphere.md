---
title: "Configuring the registry for vSphere"
type: reference
domain: openshift
slug: registry-4-22-configuring-registry-storage-vsphere
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/configuring-registry-storage-vsphere
version: 4.22
family: registry
documentKind: "Documentation"
---

# Configuring the registry for vSphere

[id="configuring-registry-storage-vsphere"]
= Configuring the registry for vSphere

[role="_abstract"]
Configure image registry storage for vSphere clusters after installation. Because vSphere installations do not automatically provision storage, you must change the registry management state from `Removed` to `Managed` and configure persistent storage or use {rh-storage-first} before the registry can store container images.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring-registry-operator.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="registry-removed_{context}"]
= Image registry removed during installation

[role="_abstract"]
On platforms that do not provide shareable object storage, the OpenShift Image Registry Operator bootstraps itself as `Removed`. This allows `openshift-installer` to complete installations on these platform types.

After installation, you must edit the Image Registry Operator configuration to switch the `managementState` from `Removed` to `Managed`. When this has completed, you must configure storage.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="registry-change-management-state_{context}"]
= Changing the image registry's management state

[role="_abstract"]
To start the image registry, you must change the Image Registry Operator configuration's `managementState` from `Removed` to `Managed`.

.Procedure

* Change `managementState` Image Registry Operator configuration from `Removed` to `Managed`. For example:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"managementState":"Managed"}}'
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="installation-registry-storage-config_{context}"]
= Image registry storage configuration

[role="_abstract"]
Amazon Web Services provides default storage, which means the Image Registry Operator is available after installation. However, if the Registry Operator cannot create an S3 bucket and automatically configure storage, you must manually configure registry storage.
[role="_abstract"]
The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="registry-configuring-storage-vsphere_{context}"]
= Configuring registry storage for VMware vSphere

[role="_abstract"]
As a cluster administrator, following installation you must configure your registry to use storage.

.Prerequisites

* Cluster administrator permissions.
* A cluster on VMware vSphere.
* Persistent storage provisioned for your cluster, such as {rh-storage-first}.
+
[IMPORTANT]
====
OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required.
====
+
* Must have "100Gi" capacity.

[IMPORTANT]
====
Testing shows issues with using the NFS server on RHEL as storage backend for
core services. This includes the OpenShift Container Registry and Quay,
Prometheus for monitoring storage, and Elasticsearch for logging storage.
Therefore, using RHEL NFS to back PVs used by core services is not recommended.

Other NFS implementations on the marketplace might not have these issues.
Contact the individual NFS implementation vendor for more information on any
testing that was possibly completed against these OpenShift Container Platform core
components.
====

.Procedure

. Change the `spec.storage.pvc` field in the `configs.imageregistry/cluster` resource.
+
[NOTE]
====
When you use shared storage, review your security settings to prevent outside access.
====

. Verify that you do not have a registry pod by running the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-image-registry -l docker-registry=default
----
+
.Example output
[source,terminal]
----
No resourses found in openshift-image-registry namespace
----
+
[NOTE]
=====
If you do have a registry pod in your output, you do not need to continue with this procedure.
=====
. Check the registry configuration by running the following command:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io
----
+
.Example output
[source,yaml]
----
storage:
  pvc:
    claim:
----
+
Leave the `claim` field blank to allow the automatic creation of an `image-registry-storage` persistent volume claim (PVC). The PVC is generated based on the default storage class. However, be aware that the default storage class might provide ReadWriteOnce (RWO) volumes, such as a RADOS Block Device (RBD), which can cause issues when you replicate to more than one replica.

. Check the `clusteroperator` status by running the following command:
+
[source,terminal]
----
$ oc get clusteroperator image-registry
----
+
.Example output
[source,terminal]
----
NAME             VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
image-registry   4.7       True        False         False      6h50m
----

//+
//There will be warning similar to:
//+
//----
//- lastTransitionTime: 2019-03-26T12:45:46Z
//message: storage backend not configured
//reason: StorageNotConfigured
//status: "True"
//type: Degraded
//----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc

[id="installation-registry-storage-non-production_{context}"]
= Configuring storage for the image registry in non-production clusters

[role="_abstract"]
You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory. If you do so, all images are lost if you restart the registry.

.Procedure

* To set the image registry storage to an empty directory:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
----
+
[WARNING]
====
Configure this option only for non-production clusters.
====
+
If you run this command before the Image Registry Operator initializes its
components, the `oc patch` command fails with the following error:
+
[source,terminal]
----
Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
----
+
Wait a few minutes and run the command again.

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="installation-registry-storage-block-recreate-rollout_{context}"]
= Configuring block registry storage for VMware vSphere

[role="_abstract"]
To allow the image registry to use block storage types such as vSphere Virtual Machine Disk (VMDK) during upgrades as a cluster administrator, you can use the `Recreate` rollout strategy.

[IMPORTANT]
====
Block storage volumes are supported but not recommended for use with image
registry on production clusters. An installation where the registry is
configured on block storage is not highly available because the registry cannot
have more than one replica.
====

.Procedure

. Enter the following command to set the image registry storage as a block storage type, patch the registry so that it uses the `Recreate` rollout strategy, and runs with only `1` replica:
+
[source,terminal]
----
$ oc patch config.imageregistry.operator.openshift.io/cluster --type=merge -p '{"spec":{"rolloutStrategy":"Recreate","replicas":1}}'
----
+
. Provision the persistent volume (PV) for the block storage device, and create a persistent volume claim (PVC) for that volume. The requested block volume uses the ReadWriteOnce (RWO) access mode.
.. Create a `pvc.yaml` file with the following contents to define a VMware vSphere `PersistentVolumeClaim` object:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: image-registry-storage
  namespace: openshift-image-registry
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 100Gi
----
+
where:
--
`metadata.name`:: Specifies a unique name that represents the `PersistentVolumeClaim` object.
`metadata.namespace`:: Specifies the `namespace` for the `PersistentVolumeClaim` object, which is `openshift-image-registry`.
`spec.accessModes`:: Specifies the access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node.
`spec.resources.requests.storage`:: Specifies the size of the persistent volume claim.
--

.. Enter the following command to create the `PersistentVolumeClaim` object from the file:
+
[source,terminal]
----
$ oc create -f pvc.yaml -n openshift-image-registry
----

+
. Enter the following command to edit the registry configuration so that it references the correct PVC:
+
[source,terminal]
----
$ oc edit config.imageregistry.operator.openshift.io -o yaml
----
+
.Example output
[source,yaml]
----
storage:
  pvc:
    claim:
----
+
By creating a custom PVC, you can leave the `claim` field blank for the default automatic creation of an `image-registry-storage` PVC.

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

[id="configuring-registry-storage-vsphere-addtl-resources"]
[role="_additional-resources"]
== Additional resources

* Configuring the registry for vSphere
* Recommended configurable storage technology
* Configuring Image Registry to use {rh-storage}
