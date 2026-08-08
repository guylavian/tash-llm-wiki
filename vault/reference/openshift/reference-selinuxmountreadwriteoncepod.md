---
title: "SELinuxMountReadWriteOncePod"
type: reference
domain: openshift
slug: reference-selinuxmountreadwriteoncepod
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SELinuxMountReadWriteOncePod
family: reference
documentKind: "doc"
---

# SELinuxMountReadWriteOncePod

Speeds up container startup by allowing kubelet to mount volumes
for a Pod directly with the correct SELinux label instead of changing each file on the volumes
recursively. The initial implementation focused on ReadWriteOncePod volumes.
