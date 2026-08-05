---
title: "{gcp-first} Filestore CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-google-cloud-file
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-google-cloud-file
version: 4.22
family: storage
documentKind: "Documentation"
---

# {gcp-first} Filestore CSI Driver Operator

[id="persistent-storage-csi-google-cloud-file"]
= {gcp-first} Filestore CSI Driver Operator

// TP features should be excluded from OSD and ROSA. When this feature is GA, it can be included in the OSD/ROSA docs, but with a warning that it is available as of version 4.x.

[id="persistent-storage-csi-google-cloud-file-overview"]
== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Google Compute Platform (GCP) Filestore Storage.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to {gcp-short} Filestore Storage assets, you install the {gcp-short} Filestore CSI Driver Operator and the {gcp-short} Filestore CSI driver in the `openshift-cluster-csi-drivers` namespace.

* The _{gcp-short} Filestore CSI Driver Operator_ does not provide a storage class by default, but you can create one if needed. The {gcp-short} Filestore CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on demand, eliminating the need for cluster administrators to pre-provision storage.

* The _{gcp-short} Filestore CSI driver_ enables you to create and mount {gcp-short} Filestore PVs.

OpenShift Container Platform {gcp-short} Filestore supports Workload Identity. This allows users to access Google Cloud resources using federated identities instead of a service account key. {gcp-wid-short} must be enabled globally during installation, and then configured for the {gcp-short} Filestore CSI Driver Operator.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-about_{context}"]
= About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

[id="installing-the-gcp-filestore-csi-driver-operator"]
== Installing the {gcp-short} Filestore CSI Driver Operator

// Module included in the following assemblies:
//
// * storage/container_storage_csi-google_cloud_file.adoc

[id="persistent-storage-csi-gcp-filestore-wif_{context}"]
= Preparing to install the {gcp-short} Filestore CSI Driver Operator with Workload Identity

If you are planning to use {gcp-wid-short} with Google Compute Platform Filestore, you must obtain certain parameters that you will use during the installation of the {gcp-short} Filestore Container Storage Interface (CSI) Driver Operator.

.Prerequisites
* Access to the cluster as a user with the cluster-admin role.

// Put note in install area of docs to remind users to take note of the identity pool ID and the provider ID

.Procedure

To prepare to install the {gcp-short} Filestore CSI Driver Operator with Workload Identity:

. Obtain the project number:

.. Obtain the project ID by running the following command:
+
[source, terminal]
----
$ export PROJECT_ID=$(oc get infrastructure/cluster -o jsonpath='{.status.platformStatus.gcp.projectID}')
----

.. Obtain the project number, using the project ID, by running the following command:
+
[source, terminal]
----
$ gcloud projects describe $PROJECT_ID --format="value(projectNumber)"
----

. Find the identity pool ID and the provider ID:
+
During cluster installation, the names of these resources are provided to the Cloud Credential Operator utility (`ccoctl`) with the `--name parameter`. See "Creating {gcp-short} resources with the Cloud Credential Operator utility".

. Create Workload Identity resources for the {gcp-short} Filestore Operator:

.. Create a `CredentialsRequest` file using the following example file:
+
.Example Credentials Request YAML file
[source, YAML]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: openshift-gcp-filestore-csi-driver-operator
  namespace: openshift-cloud-credential-operator
  annotations:
    include.release.openshift.io/self-managed-high-availability: "true"
    include.release.openshift.io/single-node-developer: "true"
spec:
  serviceAccountNames:
  - gcp-filestore-csi-driver-operator
  - gcp-filestore-csi-driver-controller-sa
  secretRef:
    name: gcp-filestore-cloud-credentials
    namespace: openshift-cluster-csi-drivers
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
	kind: GCPProviderSpec
    predefinedRoles:
    - roles/file.editor
    - roles/resourcemanager.tagUser
    skipServiceCheck: true
----

.. Use the `CredentialsRequest` file to create a {gcp-short} service account by running the following command:
+
[source, terminal]
----
$ ./ccoctl gcp create-service-accounts --name=<filestore-service-account> \// <1>
  --workload-identity-pool=<workload-identity-pool> \// <2>
  --workload-identity-provider=<workload-identity-provider> \// <3>
  --project=<project-id> \// <4>
  --credentials-requests-dir=/tmp/credreq <5>
----
<1> <filestore-service-account> is a user-chosen name.
<2> <workload-identity-pool> comes from Step 2 above.
<3> <workload-identity-provider> comes from Step 2 above.
<4> <project-id> comes from Step 1.a above.
<5> The name of directory where the `CredentialsRequest` file resides.
+
.Example output
[source, terminal]
----
2025/02/10 17:47:39 Credentials loaded from gcloud CLI defaults
2025/02/10 17:47:42 IAM service account filestore-service-account-openshift-gcp-filestore-csi-driver-operator created
2025/02/10 17:47:44 Unable to add predefined roles to IAM service account, retrying...
2025/02/10 17:47:59 Updated policy bindings for IAM service account filestore-service-account-openshift-gcp-filestore-csi-driver-operator
2025/02/10 17:47:59 Saved credentials configuration to: /tmp/install-dir/ <1>
openshift-cluster-csi-drivers-gcp-filestore-cloud-credentials-credentials.yaml
----
<1> The current directory.

.. Find the service account email of the newly created service account by running the following command:
+
[source, terminal]
----
$ cat /tmp/install-dir/manifests/openshift-cluster-csi-drivers-gcp-filestore-cloud-credentials-credentials.yaml | yq '.data["service_account.json"]' | base64 -d | jq '.service_account_impersonation_url'
----
+
.Example output
[source, terminal]
----
https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/filestore-se-openshift-g-ch8cm@openshift-gce-devel.iam.gserviceaccount.com:generateAccessToken
----
+
In this example output, the service account email is `filestore-se-openshift-g-ch8cm@openshift-gce-devel.iam.gserviceaccount.com`.

.Results

You now have the following parameters that you need to install the {gcp-short} Filestore CSI Driver Operator:

* Project number - from Step 1.b

* Pool ID - from Step 2

* Provider ID - from Step 2

* Service account email - from Step 3.c

[role="_additional-resources"]
.Additional resources
* Creating {gcp-short} resources with the Cloud Credential Operator utility

// Module included in the following assemblies:
//
// * storage/container_storage_csi-google_cloud_file.adoc

[id="persistent-storage-csi-olm-operator-install_{context}"]
= Installing the {gcp-short} Filestore CSI Driver Operator

The Google Compute Platform ({gcp-short}) Filestore Container Storage Interface (CSI) Driver Operator is not installed in OpenShift Container Platform by default.
Use the following procedure to install the {gcp-short} Filestore CSI Driver Operator in your cluster.

.Prerequisites
* Access to the OpenShift Container Platform web console.
* If using {gcp-wid-short}, certain {gcp-wid-short} parameters are needed. See the preceding Section _Preparing to install the {gcp-short} Filestore CSI Driver Operator with Workload Identity_.

.Procedure
To install the {gcp-short} Filestore CSI Driver Operator from the web console:

. Log in to the {cluster-manager-url}.

. Select your cluster.

. Click *Open console* and log in with your credentials.

. Log in to the web console.

. Enable the Filestore API in the GCE project by running the following command:
+
[source, command]
----
$ gcloud services enable file.googleapis.com  --project <my_gce_project> <1>
----
<1> Replace `<my_gce_project>` with your Google Cloud project.
+
You can also do this using Google Cloud web console.

. Install the {gcp-short} Filestore CSI Operator:

.. Click *Ecosystem* -> *Software Catalog*.

.. Locate the {gcp-short} Filestore CSI Operator by typing *{gcp-short} Filestore* in the filter box.

.. Click the *{gcp-short} Filestore CSI Driver Operator* button.

.. On the *{gcp-short} Filestore CSI Driver Operator* page, click *Install*.

.. On the *Install Operator* page, ensure that:
+
* *All namespaces on the cluster (default)* is selected.
* *Installed Namespace* is set to *openshift-cluster-csi-drivers*.
+
If using {gcp-wid-short}, enter values for the following fields obtained from the procedure in Section _Preparing to install the {gcp-short} Filestore CSI Driver Operator with Workload Identity_:
+
* *{gcp-short} Project Number*
* *{gcp-short} Pool ID*
* *{gcp-short} Provider ID*
* *{gcp-short} Service Account Email*

.. Click *Install*.
+
After the installation finishes, the {gcp-short} Filestore CSI Operator is listed in the *Installed Operators* section of the web console.

. Install the {gcp-short} Filestore CSI Driver:

.. Click *administration* → *CustomResourceDefinitions* → *ClusterCSIDriver*.

.. On the *Instances* tab, click *Create ClusterCSIDriver*.
+
Use the following YAML file:
+
[source, yaml]
----
apiVersion: operator.openshift.io/v1
kind: ClusterCSIDriver
metadata:
    name: filestore.csi.storage.gke.io
spec:
  managementState: Managed
----

.. Click *Create*.
+
.. Wait for the following Conditions to change to a "true" status:

* GCPFilestoreDriverCredentialsRequestControllerAvailable

* GCPFilestoreDriverNodeServiceControllerAvailable

* GCPFilestoreDriverControllerServiceControllerAvailable

[role="_additional-resources"]
.Additional resources
* Enabling an API in your Google Cloud.
* Enabling an API using the Google Cloud web console.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-google-cloud-file.adoc

[id="persistent-storage-csi-google-cloud-file-create-sc_{context}"]
= Creating a storage class for GCP Filestore Storage

After installing the Operator, you should create a storage class for dynamic provisioning of Google Compute Platform (GCP) Filestore volumes.

.Prerequisites
* You are logged in to the running OpenShift Container Platform cluster.

.Procedure
To create a storage class:

. Create a storage class using the following example YAML file:
+
[source,yaml]
.Example YAML file
--
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: filestore-csi
provisioner: filestore.csi.storage.gke.io
parameters:
  connect-mode: DIRECT_PEERING <1>
  network: network-name <2>
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
--
<1> For a shared VPC, use the `connect-mode` parameter set to `PRIVATE_SERVICE_ACCESS`. For a non-shared VPC, the value is `DIRECT_PEERING`, which is the default setting.
<2> Specify the name of the GCP virtual private cloud (VPC) network where Filestore instances should be created in.

. Specify the name of the VPC network where Filestore instances should be created in.
+
It is recommended to specify the VPC network that the Filestore instances should be created in. If no VPC network is specified, the Container Storage Interface (CSI) driver tries to create the instances in the default VPC network of the project.
+
On IPI installations, the VPC network name is typically the cluster name with the suffix "-network". However, on UPI installations, the VPC network name can be any value chosen by the user.
+
For a shared VPC (`connect-mode` = `PRIVATE_SERVICE_ACCESS`), the network needs to be the full VPC name. For example: `projects/shared-vpc-name/global/networks/gcp-filestore-network`.
+
You can find out the VPC network name by inspecting the `MachineSets` objects with the following command:
+
[source, command]
----
$ oc -n openshift-machine-api get machinesets -o yaml | grep "network:"
            - network: gcp-filestore-network
(...)
----
In this example, the VPC network name in this cluster is "gcp-filestore-network".

// Module included in the following assemblies:
//
// * storage/container_storage_csi-google_cloud_file.adoc

[id="persistent-storage-csi-gcp-filestore-nfs-export-options_{context}"]
= NFS export options

By default, a Filestore instance grants root level read/write access to all clients that share the same Google Cloud project and virtual private cloud (VPC) network. Network File System (NFS) export options can limit this access to certain IP ranges and specific user/group IDs for the Filestore instance. When creating a storage class, you can set these options using the `nfs-export-options-on-create` parameter.

.Prerequisites
* Access to the cluster as a user with the cluster-admin role.

* The {gcp-short} Filestore CSI Driver Operator and {gcp-short} Filestore CSI driver installed.

.Procedure

. Create a storage class using a file similar to the following sample YAML file:
+
[NOTE]
====
For more information about creating a storage class, see Section _Creating a storage class for GCP Filestore Operator_.
====
+
.Example storage class YAML file with NFS export options
[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name: SC-name
provisioner: filestore.csi.storage.gke.io
parameters:
 connect-mode: DIRECT_PEERING
 network: project-network
 nfs-export-options-on-create: '[ <1>
   {
     "accessMode": "READ_WRITE", <2>
     "squashMode": "NO_ROOT_SQUASH", <3>
     "anonUid": 65534 <4>
     "anonGid": 65534 <5>
     "ipRanges": [ <6>
       "10.0.0.0/16"
     ]
   }]'
allowVolumeExpansion: true
----
<1> *NFS export options parameter*
<2> *Access mode*: Either `READ_ONLY,` which allows only read requests on the exported directory; or `READ_WRITE`, which allows both read and write requests. The default is `READ_WRITE`.
<3> *Squash mode*: Either `NO_ROOT_SQUASH`, which allows root access on the exported directory; or ROOT_SQUASH, which does not allow root access. The default is `NO_ROOT_SQUASH`.
<4> *AnonUid*: An integer representing the anonymous user ID with a default value of 65534. `AnonUid` can only be set with `squashMode` set to `ROOT_SQUASH`; Otherwise, an error occurs.
<5> *AnonGid*: An integer representing the anonymous group ID with a default value of 65534. `AnonGid` can only be set with `squashMode` set to `ROOT_SQUASH`. Otherwise, an error occurs.
<6> *IP ranges*: List of either an IPv4 addresses in the format {octet1}.{octet2}.{octet3}.{octet4}, or CIDR ranges in the format {octet1}.{octet2}.{octet3}.{octet4}/{mask size}, which can mount the file share. Overlapping IP ranges are not allowed, both within and across NfsExportOptions, otherwise, an error is returned. The limit is 64 IP ranges or addresses for each `FileShareConfig` among all NFS export options.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-google-cloud-file.adoc

[id="persistent-storage-csi-google-cloud-file-delete-instances_{context}"]
= Destroying clusters and GCP Filestore

Typically, if you destroy a cluster, the OpenShift Container Platform installer deletes all of the cloud resources that belong to that cluster. However, due to the special nature of the Google Compute Platform (GCP) Filestore resources, the automated cleanup process might not remove all of them in some rare cases.

Therefore, Red Hat recommends that you verify that all cluster-owned Filestore resources are deleted by the uninstall process.

.Procedure
To ensure that all GCP Filestore PVCs have been deleted:

. Access your Google Cloud account using the GUI or CLI.

. Search for any resources with the `kubernetes-io-cluster-${CLUSTER_ID}=owned` label.
+
Since the cluster ID is unique to the deleted cluster, there should not be any remaining resources with that cluster ID.

. In the unlikely case there are some remaining resources, delete them.

[role="_additional-resources"]
== Additional resources
* Configuring CSI volumes
[id="osdk-cco-gpc_{context}"]
* CCO-based workflow for OLM-managed Operators with {gcp-short} Workload Identity.
