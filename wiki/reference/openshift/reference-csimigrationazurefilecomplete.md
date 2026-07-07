---
title: "CSIMigrationAzureFileComplete"
type: reference
domain: openshift
slug: reference-csimigrationazurefilecomplete
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/CSIMigrationAzureFileComplete
family: reference
documentKind: "doc"
---

# CSIMigrationAzureFileComplete

Stops registering the Azure-File in-tree
plugin in kubelet and volume controllers and enables shims and translation
logic to route volume operations from the Azure-File in-tree plugin to
AzureFile CSI plugin. Requires CSIMigration and CSIMigrationAzureFile feature
flags  enabled and AzureFile CSI plugin installed and configured on all nodes
in the cluster. This flag has been deprecated in favor of the
`InTreePluginAzureFileUnregister` feature flag which prevents the registration
 of in-tree AzureFile plugin.
