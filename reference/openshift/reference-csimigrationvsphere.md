---
title: "CSIMigrationvSphere"
type: reference
domain: openshift
slug: reference-csimigrationvsphere
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationvSphere
family: reference
documentKind: "doc"
---

# CSIMigrationvSphere

Enables shims and translation logic to route volume operations
from the vSphere in-tree plugin to vSphere CSI plugin. Supports falling back
to in-tree vSphere plugin for mount operations to nodes that have the feature
disabled or that do not have vSphere CSI plugin installed and configured.
Does not support falling back for provision operations, for those the CSI
plugin must be installed and configured. Requires CSIMigration feature flag
enabled.
