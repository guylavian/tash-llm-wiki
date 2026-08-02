---
title: "Manage basic volumes"
type: reference
domain: windows-server
slug: storage-manage-basic-volumes
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/storage/disk-management/manage-basic-volumes
family: storage
documentKind: "concept-article"
abstract: "This article describes basic disks and the requirements to add space to existing primary partitions and logical drives."
---

# Manage basic volumes

# Manage basic volumes

> **

A basic disk is a physical disk that contains primary partitions, extended partitions, or logical drives. Partitions and logical drives on basic disks are called basic volumes. You can only create basic volumes on basic disks.

You can add more space to existing primary partitions and logical drives by extending them into adjacent, contiguous unallocated space on the same disk. To extend a basic volume, format it with the NTFS file system. You can extend a logical drive within contiguous free space in the extended partition that contains it. If you extend a logical drive beyond the free space available in the extended partition, the extended partition grows to contain the logical drive only if the extended partition is followed by contiguous unallocated space.

## Related topics

- [Mount a drive in a folder](assign-a-mount-point-folder-path-to-a-drive.md)
- [Extend a basic volume](extend-a-basic-volume.md)
- [Shrink a basic volume](shrink-a-basic-volume.md)
