---
title: "Configuring the vSphere connection settings after an installation"
type: reference
domain: openshift
slug: installing-4-22-installing-vsphere-post-installation-configuration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-vsphere-post-installation-configuration
version: 4.22
family: installing
documentKind: "Documentation"
---

# Configuring the vSphere connection settings after an installation

[id="installing-vsphere-post-installation-configuration"]
= Configuring the vSphere connection settings after an installation

After installing an OpenShift Container Platform cluster on vSphere with the platform integration feature enabled, you might need to update the vSphere connection settings manually, depending on the installation method.

For installations using the Assisted Installer, you must update the connection settings. This is because the Assisted Installer adds default connection settings to the *vSphere connection configuration* wizard as placeholders during the installation.

For installer-provisioned or user-provisioned infrastructure installations, you should have entered valid connection settings during the installation. You can use the *vSphere connection configuration* wizard at any time to validate or modify the connection settings, but this is not mandatory for completing the installation.

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-vsphere-post-installation-configuration.adoc

[id="configuring-vSphere-connection-settings_{context}"]
= Configuring the vSphere connection settings

[role="_abstract"]
Modify the following vSphere configuration settings as required:

* vCenter address
* vCenter cluster
* vCenter username
* vCenter password
* vCenter address
* vSphere data center
* vSphere datastore
* Virtual machine folder

.Prerequisites
* The {ai-full} has finished installing the cluster successfully.
* The cluster is connected to `https://console.redhat.com`.

.Procedure
. In the Administrator perspective, navigate to *Home -> Overview*.
. Under *Status*, click *vSphere connection* to open the *vSphere connection configuration* wizard.
. In the *vCenter* field, enter the network address of the vSphere vCenter server. This can be either a domain name or an IP address. It appears in the vSphere web client URL; for example `https://[your_vCenter_address]/ui`.
. In the *vCenter cluster* field, enter the name of the vSphere vCenter cluster where OpenShift Container Platform is installed.
+
[IMPORTANT]
====
This step is mandatory if you installed OpenShift Container Platform 4.13 or later.
====

. In the *Username* field, enter your vSphere vCenter username.
. In the *Password* field, enter your vSphere vCenter password.
+
[WARNING]
====
The system stores the username and password in the `vsphere-creds` secret in the `kube-system` namespace of the cluster. An incorrect vCenter username or password makes the cluster nodes unschedulable.
====
+
. In the *Datacenter* field, enter the name of the vSphere data center that contains the virtual machines used to host the cluster; for example, `SDDC-Datacenter`.
. In the *Default data store* field, enter the path and name of the vSphere data store that stores the persistent data volumes; for example, `/SDDC-Datacenter/datastore/datastorename`.
+
[WARNING]
====
Updating the vSphere data center or default data store after the configuration has been saved detaches any active vSphere `PersistentVolumes`.
====
+
. In the *Virtual Machine Folder* field, enter the data center folder that contains the virtual machine of the cluster; for example, `/SDDC-Datacenter/vm/ci-ln-hjg4vg2-c61657-t2gzr`. For the OpenShift Container Platform installation to succeed, all virtual machines comprising the cluster must be located in a single data center folder.
. Click *Save Configuration*. This updates the `cloud-provider-config` ConfigMap resource in the `openshift-config` namespace, and starts the configuration process.
. Reopen the *vSphere connection configuration* wizard and expand the *Monitored operators* panel. Check that the status of the operators is either *Progressing* or *Healthy*.

// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-vsphere-post-installation-configuration.adoc

[id="configuring-vSphere-monitoring-configuration-completion_{context}"]
= Verifying the configuration

The connection configuration process updates operator statuses and control plane nodes. It takes approximately an hour to complete. During the configuration process, the nodes will reboot. Previously bound `PersistentVolumeClaims` objects might become disconnected.

.Prerequisites
* You have saved the configuration settings in the *vSphere connection configuration* wizard.

.Procedure

. Check that the configuration process completed successfully:
+
--
.. In the OpenShift Container Platform Administrator perspective, navigate to *Home -> Overview*.
.. Under *Status* click *Operators*. Wait for all operator statuses to change from  *Progressing* to *All succeeded*.  A *Failed* status indicates that the configuration failed.
.. Under *Status*, click *Control Plane*. Wait for the response rate of all Control Pane components to return to 100%. A *Failed* control plane component indicates that the configuration failed.
--
A failure indicates that at least one of the connection settings is incorrect. Change the settings in the *vSphere connection configuration* wizard and save the configuration again.

. Check that you are able to bind `PersistentVolumeClaims` objects by performing the following steps:

.. Create a `StorageClass` object using the following YAML:
+
[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name: vsphere-sc
provisioner: kubernetes.io/vsphere-volume
parameters:
 datastore: YOURVCENTERDATASTORE
 diskformat: thin
reclaimPolicy: Delete
volumeBindingMode: Immediate
----
.. Create a `PersistentVolumeClaims` object using the following YAML:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
 name: test-pvc
 namespace: openshift-config
 annotations:
   volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
 finalizers:
   - kubernetes.io/pvc-protection
spec:
 accessModes:
   - ReadWriteOnce
 resources:
   requests:
    storage: 10Gi
 storageClassName: vsphere-sc
 volumeMode: Filesystem
----
+
If you are unable to create a `PersistentVolumeClaims` object, you can troubleshoot by navigating to *Storage* -> *PersistentVolumeClaims* in the *Administrator* perspective of the OpenShift Container Platform web console.

For instructions on creating storage objects, see Dynamic provisioning.
