---
title: "CIFS/SMB CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-smb-cifs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-smb-cifs
version: 4.22
family: storage
documentKind: "Documentation"
---

# CIFS/SMB CSI Driver Operator

[id="persistent-storage-csi-smb-cifs"]
= CIFS/SMB CSI Driver Operator

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) with a Container Storage Interface (CSI) driver for Common Internet File System (CIFS) dialect/Server Message Block (SMB) protocol.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver.

After installing the CIFS/SMB CSI Driver Operator, OpenShift Container Platform installs corresponding pods for the Operator and driver in the `openshift-cluster-csi-drivers` namespace by default. This allows the CIFS/SMB CSI Driver to create CSI-provisioned persistent volumes (PVs) that mount to CIFS/SMB shares.

* The _CIFS/SMB CSI Driver Operator_, after being installed, does not create a storage class by default to use to create persistent volume claims (PVCs). However, you can manually create the CIFS/SMB `StorageClass` for dynamic provisioning. The CIFS/SMB CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand.
This eliminates the need for cluster administrators to pre-provision storage.

* The _CIFS/SMB CSI driver_ enables you to create and mount CIFS/SMB PVs.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-about_{context}"]
= About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-smb-cifs.adoc

[id="persistent-storage-csi-smb-cifs-limits_{context}"]
= Limitations

The following limitations apply to the Common Internet File System (CIFS)/Server Message Block (SMB) Container Storage Interface (CSI) Driver Operator:

* FIPS mode is not supported:
+
When Federal Information Processing Standards (FIPS) mode is enabled, the use of md4 and md5 are disabled, which prevents users from using ntlm, ntlmv2, or ntlmssp authentication. Also, signing cannot be used because it uses md5. Any CIFS mount that uses these methods fails when FIPS mode is enabled.

* Using HTTP proxy configuration to connect to outside of the cluster SMB servers is not supported by the CSI driver.
+
Since CIFS/SMB is a LAN protocol, and though it can be routed to subnets, it is not designed to be extended over the WAN, and does not support HTTP proxy settings.

* The CIFS/SMB CSI Driver Operator does _not_ support Windows Distributed File System (DFS).

* Kerberos authentication is not supported.

* SMB CSI was tested with Samba v4.21.2 and Windows Server 2019 and Windows Server 2022.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/osd-persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/persistent-storage-csi-smb-cifs.adoc

[id="persistent-storage-csi-olm-operator-install_{context}"]
= Installing the {FeatureName} CSI Driver Operator

The {FeatureName} CSI Driver Operator (a Red{nbsp}Hat Operator) is not installed in OpenShift Container Platform by default. Use the following procedure to install and configure the {FeatureName} CSI Driver Operator in your cluster.

// The following ifeval and restricted ifdef statements exclude STS and a note about avoiding
// installing community operator content for CSI drivers other than EWS

.Prerequisites
* Access to the OpenShift Container Platform web console.

.Procedure
To install the {FeatureName} CSI Driver Operator from the web console:

. Log in to the web console.

. Install the {FeatureName} CSI Operator:

.. Click *Ecosystem* -> *Software Catalog*.

.. Locate the {FeatureName} CSI Operator by typing *{FeatureName} CSI* in the filter box.

.. Click the *{FeatureName} CSI Driver Operator* button.

+
[IMPORTANT]
====
Be sure to select the *{FeatureName} CSI Driver Operator* and not the *{FeatureName} Operator*. The *{FeatureName} Operator* is a community Operator and is not supported by Red Hat.
====

.. On the *{FeatureName} CSI Driver Operator* page, click *Install*.

.. On the *Install Operator* page, ensure that:
+
* If you are using {FeatureName} with AWS Secure Token Service (STS), in the *role ARN* field, enter the ARN role copied from the last step of the _Obtaining a role Amazon Resource Name for Security Token Service_ procedure.
* *All namespaces on the cluster (default)* is selected.
* *Installed Namespace* is set to *openshift-cluster-csi-drivers*.

.. Click *Install*.
+
After the installation finishes, the {FeatureName} CSI Operator is listed in the *Installed Operators* section of the web console.

// The following ifeval statements exclude STS and a note about avoiding
// installing community operator content for CSI drivers other than EWS

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-smb-cifs.adoc

[id="persistent-storage-csi-smb-cifs-driver-install_{context}"]
= Installing the {FeatureName} CSI Driver

After installing the {FeatureName} Container Storage Interface (CSI) Driver Operator, install the {FeatureName} CSI driver.

.Prerequisites
* Access to the OpenShift Container Platform web console.
* {FeatureName} CSI Driver Operator installed.

.Procedure

. Click *Administration* -> *CustomResourceDefinitions* -> *ClusterCSIDriver*.

. On the *Instances* tab, click *Create ClusterCSIDriver*.

. Use the following YAML file:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: ClusterCSIDriver
metadata:
    name: smb.csi.k8s.io
spec:
  managementState: Managed
----

. Click *Create*.

. Wait for the following Conditions to change to a "True" status:
+

* `SambaDriverControllerServiceControllerAvailable`

* `SambaDriverNodeServiceControllerAvailable`

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-smb-cifs.adoc

[id="persistent-storage-csi-smb-cifs-provision-dynamic_{context}"]
= Dynamic provisioning

You can create a storage class for dynamic provisioning of Common Internet File System (CIFS) dialect/Server Message Block (SMB) protocol volumes. Provisioning volumes creates a subdirectory with the persistent volume (PV) name under `source` defined in the storage class.

.Prerequisites
* {FeatureName} CSI Driver Operator and driver installed.
* You are logged in to the running OpenShift Container Platform cluster.
* You have installed the SMB server and know the following information about the server:
** Hostname
** Share name
** Username and password

.Procedure

To set up dynamic provisioning:

. Create a Secret for access to the Samba server using the following command with the following example YAML file:
+
[source,terminal]
--
$ oc create -f <file_name>.yaml
--
+
[source,yaml]
.Secret example YAML file
--
apiVersion: v1
kind: Secret
metadata:
  name: smbcreds <1>
  namespace: samba-server <2>
stringData:
  username: <username> <3>
  password: <password> <4>
--
<1> Name of the Secret for the Samba server.
<2> Namespace for the Secret for the Samba server.
<3> Username for the Secret for the Samba server.
<4> Password for the Secret for the Samba server.

. Create a storage class by running the following command with the following example YAML file:
+
[source,terminal]
--
$ oc create -f <sc_file_name>.yaml <1>
--
<1> Name of the storage class YAML file.
+
[source,yaml]
.Storage class example YAML file
--
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <sc_name> <1>
provisioner: smb.csi.k8s.io
parameters:
  source: //<hostname>/<shares> <2>
  csi.storage.k8s.io/provisioner-secret-name: smbcreds <3>
  csi.storage.k8s.io/provisioner-secret-namespace: samba-server <4>
  csi.storage.k8s.io/node-stage-secret-name: smbcreds <3>
  csi.storage.k8s.io/node-stage-secret-namespace: samba-server <4>
reclaimPolicy: Delete
volumeBindingMode: Immediate
mountOptions:
  - dir_mode=0777
  - file_mode=0777
  - uid=1001
  - gid=1001
--
<1> The name of the storage class.
<2> The Samba server must be installed somewhere and reachable from the cluster with <`hostname>` being the hostname for the Samba server and `<shares>` the path the server is configured to have among the exported shares.
<3> Name of the Secret for the Samba server that was set in the previous step. If the `csi.storage.k8s.io/provisioner-secret` is provided, a subdirectory is created with the PV name under `source`.
<4> Namespace for the Secret for the Samba server that was set in the previous step.

. Create a PVC:

.. Create a PVC by running the following command with the following example YAML file:
+
[source, terminal]
----
$ oc create -f <pv_file_name>.yaml <1>
----
<1> The name of the PVC YAML file.
+
.Example PVC YAML file
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: <pvc_name> <1>
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: <storage_amount> <2>
  storageClassName: <sc_name> <3>
----
<1> The name of the PVC.
<2> Storage request amount.
<3> The name of the CIFS/SMB storage class that you created in the previous step.

.. Ensure that the PVC was created and is in the "Bound" status by running the following command:
+
[source, terminal]
----
$ oc describe pvc <pvc_name> <1>
----
<1> The name of the PVC that you created in the preceding step.
+
.Example output
+
[source,terminal]
----
Name:          pvc-test
Namespace:     default
StorageClass:  samba
Status:        Bound <1>
...
----
<1> PVC is in Bound status.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-smb-cifs.adoc

[id="persistent-storage-csi-smb-cifs-provision-static_{context}"]
= Static provisioning

You can use static provisioning to create a persistent volume (PV) and persistent volume claim (PVC) to consume existing Server Message Block protocol (SMB) shares:

.Prerequisites
* Access to the OpenShift Container Platform web console.
* {FeatureName} CSI Driver Operator and driver installed.
* You have installed the SMB server and know the following information about the server:
** Hostname
** Share name
** Username and password

.Procedure

To set up static provisioning:

. Create a Secret for access to the Samba server using the following command with the following example YAML file:
+
[source,terminal]
--
$ oc create -f <file_name>.yaml
--
+
[source,yaml]
.Secret example YAML file
--
apiVersion: v1
kind: Secret
metadata:
  name: smbcreds <1>
  namespace: samba-server <2>
stringData:
  username: <username> <3>
  password: <password> <4>
--
<1> Name of the Secret for the Samba server.
<2> Namespace for the Secret for the Samba server.
<3> Username for the Secret for the Samba server.
<4> Password for the Secret for the Samba server.

. Create a PV by running the following command with the following example YAML file:
+
[source,terminal]
----
$ oc create -f <pv_file_name>.yaml <1>
----
<1> The name of the PV YAML file.
+
.Example PV YAML file
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    pv.kubernetes.io/provisioned-by: smb.csi.k8s.io
  name: <pv_name> <1>
spec:
  capacity:
    storage: 100Gi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  storageClassName: ""
  mountOptions:
    - dir_mode=0777
    - file_mode=0777
  csi:
    driver: smb.csi.k8s.io
    volumeHandle: smb-server.default.svc.cluster.local/share## <2>
    volumeAttributes:
      source: //<hostname>/<shares> <3>
    nodeStageSecretRef:
      name: <secret_name_shares> <4>
      namespace: <namespace> <5>
----
<1> The name of the PV.
<2> `volumeHandle` format: {smb-server-address}#{sub-dir-name}#{share-name}. Ensure that this value is unique for every share in the cluster.
<3> The Samba server must be installed somewhere and reachable from the cluster with <hostname> being the hostname for the Samba server and <shares> the path the server is configured to have among the exported shares.
<4> The name of the Secret for the shares.
<5> The applicable namespace.

. Create a PVC:

.. Create a PVC by running the following command with the following example YAML file:
+
[source, terminal]
----
$ oc create -f <pv_file_name>.yaml <1>
----
<1> The name of the PVC YAML file.
+
.Example PVC YAML file
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: <pvc_name> <1>
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: <storage_amount> <2>
  storageClassName: ""
  volumeName: <pv_name> <3>
----
<1> The name of the PVC.
<2> Storage request amount.
<3> The name of the PV from the first step.

.. Ensure that the PVC was created and is in the "Bound" status by running the following command:
+
[source, terminal]
----
$ oc describe pvc <pvc_name> <1>
----
<1> The name of the PVC that you created in the preceding step.
+
.Example output
+
[source,terminal]
----
Name:          pvc-test
Namespace:     default
StorageClass:
Status:        Bound <1>
...
----
<1> PVC is in Bound status.

. Create a deployment on Linux by running the following command with the following example YAML file:
+
[NOTE]
====
The following deployment is not mandatory for using the PV and PVC created in the previous steps. It is example of how they can be used.
====
+
[source, terminal]
----
$ oc create -f <deployment_file_name>.yaml <1>
----
<1> The name of the deployment YAML file.
+
.Example deployment YAML file
+
[source, yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: <deployment_name> <1>
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
      name: <deployment_name> <1>
    spec:
      nodeSelector:
        "kubernetes.io/os": linux
      containers:
        - name: <deployment_name> <1>
          image: quay.io/centos/centos:stream8
          command:
            - "/bin/bash"
            - "-c"
            - set -euo pipefail; while true; do echo $(date) >> <mount_path>/outfile; sleep 1; done <2>
          volumeMounts:
            - name: <vol_mount_name> <3>
              mountPath: <mount_path> <2>
              readOnly: false
      volumes:
        - name: <vol_mount_name> <3>
          persistentVolumeClaim:
            claimName: <pvc_name> <4>
  strategy:
    rollingUpdate:
      maxSurge: 0
      maxUnavailable: 1
    type: RollingUpdate
----
<1> The name of the deployment.
<2> The volume mount path.
<3> The name of the volume mount.
<4> The name of the PVC created in the preceding step.

. Check the setup by running the `df -h` command in the container:
+
[source, terminal]
----
$ oc exec -it <pod_name> -- df -h <1>
----
<1> The name of the pod.
+
.Example output
+
[source, terminal]
----
Filesystem            Size  Used Avail Use% Mounted on
...
/dev/sda1              97G   21G   77G  22% /etc/hosts
//20.43.191.64/share   97G   21G   77G  22% /mnt/smb
...
----
+
In this example, there is a `/mnt/smb` directory mounted as a Common Internet File System (CIFS) filesystem.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Configuring CSI volumes
