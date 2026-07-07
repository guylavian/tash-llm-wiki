---
title: "SELinuxMount"
type: reference
domain: openshift
slug: reference-selinuxmount
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SELinuxMount
family: reference
documentKind: "doc"
---

# SELinuxMount

Speeds up container startup by allowing kubelet to mount volumes
for a Pod directly with the correct SELinux label instead of changing each file on the volumes
recursively.
It widens the performance improvements behind the `SELinuxMountReadWriteOncePod`
feature gate by extending the implementation to all volumes.

Enabling the `SELinuxMount` feature gate requires the feature gates `SELinuxMountReadWriteOncePod`
and `SELinuxChangePolicy` to be enabled.
