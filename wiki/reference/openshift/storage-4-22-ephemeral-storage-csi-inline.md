---
title: "CSI inline ephemeral volumes"
type: reference
domain: openshift
slug: storage-4-22-ephemeral-storage-csi-inline
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/ephemeral-storage-csi-inline
version: 4.22
family: storage
documentKind: "Documentation"
---

# CSI inline ephemeral volumes

[id="ephemeral-storage-csi-inline"]
= CSI inline ephemeral volumes

// TP features should be excluded from OSD and ROSA. When this feature is GA, it can be included in the OSD/ROSA docs, but with a warning that it is available as of version 4.x.

[role="_abstract"]
Container Storage Interface (CSI) inline ephemeral volumes allow you to define a `Pod` spec that creates inline ephemeral volumes when a pod is deployed and delete them when a pod is destroyed.

This feature is only available with supported Container Storage Interface (CSI) drivers:

* Azure File CSI driver
* {secrets-store-driver}

// Module included in the following assemblies:
//
// * storage/container_storage_interface/ephemeral-storage-csi-inline.adoc

[id="ephemeral-storage-csi-inline-overview_{context}"]
= Overview of CSI inline ephemeral volumes

[role="_abstract"]
Traditionally, volumes that are backed by Container Storage Interface (CSI) drivers can only be used with a `PersistentVolume` and `PersistentVolumeClaim` object combination.

This feature allows you to specify CSI volumes directly in the `Pod` specification, rather than in a `PersistentVolume` object. Inline volumes are ephemeral and do not persist across pod restarts.

== Support limitations

[IMPORTANT]
====
The Shared Resource CSI Driver feature is now generally available in {builds-v2title} 1.1. This feature is now removed in OpenShift Container Platform 4.18 and later. To use this feature, ensure that you are using {builds-v2title} 1.1 or later.
====

By default, OpenShift Container Platform supports CSI inline ephemeral volumes with these limitations:

* Support is only available for CSI drivers. In-tree and FlexVolumes are not supported.

* Community or storage vendors provide other CSI drivers that support these volumes. Follow the installation instructions provided by the CSI driver provider.

CSI drivers might not have implemented the inline volume functionality, including `Ephemeral` capacity. For details, see the CSI driver documentation.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/ephemeral-storage-csi-inline.adoc

[id="ephemeral-storage-csi-overview-admin-plugin_{context}"]
= CSI Volume Admission plugin

[role="_abstract"]
The Container Storage Interface (CSI) Volume Admission plugin allows you to restrict the use of an individual CSI driver capable of provisioning CSI ephemeral volumes on pod admission. Administrators can add a `csi-ephemeral-volume-profile` label, and this label is then inspected by the Admission plugin and used in enforcement, warning, and audit decisions.

[id="overview-admission-plugin"]
== Overview

To use the CSI Volume Admission plugin, administrators add the `security.openshift.io/csi-ephemeral-volume-profile` label to a `CSIDriver` object, which declares the CSI driver’s effective pod security profile when it is used to provide CSI ephemeral volumes, as shown in the following example:

.Example CSIDriver YAML file enabling using of the CSI Admission plugin
[source, yaml]
----
kind: CSIDriver
metadata:
  name: csi.mydriver.company.org
  labels:
    security.openshift.io/csi-ephemeral-volume-profile: restricted
----
* `metadata.labels.security.openshift.io/csi-ephemeral-volume-profile`: Setting the `csi-ephemeral-volume-profile` label to "restricted" enables use of the CSI Admission plugin.

This “effective profile” communicates that a pod can use the CSI driver to mount CSI ephemeral volumes when the pod’s namespace is governed by a pod security standard.

The CSI Volume Admission plugin inspects pod volumes when pods are created; existing pods that use CSI volumes are not affected. If a pod uses a container storage interface (CSI) volume, the plugin looks up the `CSIDriver` object and inspects the `csi-ephemeral-volume-profile` label, and then use the label’s value in its enforcement, warning, and audit decisions.

[id="security-profile-enforcement"]
== Pod security profile enforcement
When a CSI driver has the `csi-ephemeral-volume-profile` label, pods using the CSI driver to mount CSI ephemeral volumes must run in a namespace that enforces a pod security standard of equal or greater permission. If the namespace enforces a more restrictive standard, the CSI Volume Admission plugin denies admission. The following table describes the enforcement behavior for different pod security profiles for given label values.

.Pod security profile enforcement
[cols=",^v,^v,^v,^v width="100%",options="header"]
|===
|Pod security profile|Driver label: restricted| Driver label: baseline | Driver label: privileged

|Restricted
|Allowed
|Denied
|Denied

|Baseline
|Allowed
|Allowed
|Denied

|Privileged
|Allowed
|Allowed
|Allowed
|===

[id="security-profile-warning"]
== Pod security profile warning
The CSI Volume Admission plugin can warn you if the CSI driver’s effective profile is more permissive than the pod security warning profile for the pod namespace. The following table shows when a warning occurs for different pod security profiles for given label values.

.Pod security profile warning
[cols=",^v,^v,^v,^v width="100%",options="header"]
|===
|Pod security profile|Driver label: restricted| Driver label: baseline | Driver label: privileged

|Restricted
|No warning
|Warning
|Warning

|Baseline
|No warning
|No warning
|Warning

|Privileged
|No warning
|No warning
|No warning
|===

[id="security-profile-audit"]
== Pod security profile audit
The CSI Volume Admission plugin can apply audit annotations to the pod if the CSI driver’s effective profile is more permissive than the pod security audit profile for the pod namespace. The following table shows the audit annotation applied for different pod security profiles for given label values.

.Pod security profile audit
[cols=",^v,^v,^v,^v width="100%",options="header"]
|===
|Pod security profile|Driver label: restricted| Driver label: baseline | Driver label: privileged

|Restricted
|No audit
|Audit
|Audit

|Baseline
|No audit
|No audit
|Audit

|Privileged
|No audit
|No audit
|No audit
|===

[id="admission-plugin-default-behavior"]
== Default behavior for the CSI Volume Admission plugin
If the referenced CSI driver for a CSI ephemeral volume does not have the `csi-ephemeral-volume-profile` label, the CSI Volume Admission plugin considers the driver to have the privileged profile for enforcement, warning, and audit behaviors. Likewise, if the pod’s namespace does not have the pod security admission label set, the Admission plugin assumes the restricted profile is allowed for enforcement, warning, and audit decisions. Therefore, if no labels are set, CSI ephemeral volumes using that CSI driver are only usable in privileged namespaces by default.

The CSI drivers that ship with OpenShift Container Platform and support ephemeral volumes have a reasonable default set for the `csi-ephemeral-volume-profile` label:

* Azure File CSI driver: privileged

If desired, an admin can change the default value of the label.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/ephemeral-storage-csi-inline-pod-scheduling.adoc

[id="ephemeral-storage-csi-inline-pod_{context}"]
= Embedding a CSI inline ephemeral volume in the pod specification

[role="_abstract"]
You can embed a CSI inline ephemeral volume in the `Pod` specification in OpenShift Container Platform. At runtime, nested inline volumes follow the ephemeral lifecycle of their associated pods so that the CSI driver handles all phases of volume operations as pods are created and destroyed.

.Procedure

. Create the `Pod` object definition and save it to a file.

. Embed the CSI inline ephemeral volume in the file as in the following pod YAML file:
+
.Example pod YAML file with embedded ephemeral volume
[source,yaml]
----
kind: Pod
apiVersion: v1
metadata:
  name: my-csi-app
spec:
  containers:
    - name: my-frontend
      image: busybox
      volumeMounts:
      - mountPath: "/data"
        name: my-csi-inline-vol
      command: [ "sleep", "1000000" ]
  volumes:
    - name: my-csi-inline-vol
      csi:
        driver: inline.storage.kubernetes.io
        volumeAttributes:
          foo: bar
----
+
* `spec.volumes.name`: The name of the volume that is used by pods.

. Create the object definition file that you saved in the previous step by running the following command.
+
[source,terminal]
----
$ oc create -f my-csi-app.yaml
----

[id="additional-resources_ephemeral-storage-csi-inline"]
[role="_additional-resources"]
== Additional resources
* Pod Security Standards
