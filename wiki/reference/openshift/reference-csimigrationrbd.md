---
title: "CSIMigrationRBD"
type: reference
domain: openshift
slug: reference-csimigrationrbd
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationRBD
family: reference
documentKind: "doc"
---

# CSIMigrationRBD

Enables shims and translation logic to route volume
operations from the RBD in-tree plugin to Ceph RBD CSI plugin. Requires
CSIMigration and csiMigrationRBD feature flags enabled and Ceph CSI plugin
installed and configured in the cluster.

This feature gate was deprecated in favor of the `InTreePluginRBDUnregister` feature gate,
which prevents the registration of in-tree RBD plugin.
