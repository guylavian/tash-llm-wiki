---
title: "Using preallocation for data volumes"
type: reference
domain: openshift
slug: virt-4-22-virt-using-preallocation-for-datavolumes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-using-preallocation-for-datavolumes
version: 4.22
family: virt
documentKind: "Documentation"
---

# Using preallocation for data volumes

[id="virt-using-preallocation-for-datavolumes"]
= Using preallocation for data volumes

[role="_abstract"]
The Containerized Data Importer (CDI) can preallocate disk space to improve write performance when creating data volumes. You can enable preallocation for specific data volumes.

// Module included in the following assemblies:
//
// * virt/storage/virt-using-preallocation-for-datavolumes.adoc

[id="virt-about-preallocation_{context}"]
= About preallocation

[role="_abstract"]
The Containerized Data Importer (CDI) can use the QEMU preallocate mode for data volumes to improve write performance. You can use preallocation mode for importing and uploading operations and when creating blank data volumes.

If preallocation is enabled, CDI uses the better preallocation method depending on the underlying file system and device type:

`fallocate`::
If the file system supports it, CDI uses the operating system's `fallocate` call to preallocate space by using the `posix_fallocate` function, which allocates blocks and marks them as uninitialized.

`full`::
If `fallocate` mode cannot be used, `full` mode allocates space for the image by writing data to the underlying storage. Depending on the storage location, all the empty allocated space might be zeroed.

// Module included in the following assemblies:
//
// * virt/storage/virt-using-preallocation-for-datavolumes.adoc

[id="virt-enabling-preallocation-for-dv_{context}"]
= Enabling preallocation for a data volume

[role="_abstract"]
You can enable preallocation for specific data volumes by including the `spec.preallocation` field in the data volume manifest. You can enable preallocation mode in either the web console or by using the OpenShift CLI (`oc`).

Preallocation mode is supported for all CDI source types. However, preallocation is ignored for cloning operations.

.Procedure

* Specify the `spec.preallocation` field in the data volume manifest:
+
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: preallocated-datavolume
spec:
  source:
    registry:
      url: <image_url>
  storage:
    resources:
      requests:
        storage: 1Gi
  preallocation: true
# ...
----
+
where:
+
`<image_url>`:: Specifies the URL of the data source in your registry.
