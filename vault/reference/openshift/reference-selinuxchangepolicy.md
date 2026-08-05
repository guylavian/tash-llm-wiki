---
title: "SELinuxChangePolicy"
type: reference
domain: openshift
slug: reference-selinuxchangepolicy
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SELinuxChangePolicy
family: reference
documentKind: "doc"
---

# SELinuxChangePolicy

Enables `spec.securityContext.seLinuxChangePolicy` field.
This field can be used to opt-out from applying the SELinux label to the pod
volumes using mount options. This is required when a single volume that supports
mounting with SELinux mount option is shared between Pods that have different
SELinux labels, such as a privileged and unprivileged Pods.

Enabling the `SELinuxChangePolicy` feature gate requires the feature gate `SELinuxMountReadWriteOncePod` to
be enabled.
