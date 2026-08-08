---
title: "NodeDeclaredFeatures"
type: reference
domain: openshift
slug: reference-nodedeclaredfeatures
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/NodeDeclaredFeatures
family: reference
documentKind: "doc"
---

# NodeDeclaredFeatures

Enables Nodes to report supported features via their `.status`. This enables the 
scheduler and admission controller to prevent operations on nodes lacking features
required by the pod. See [Node Declared Features](/docs/concepts/scheduling-eviction/node-declared-features/).
