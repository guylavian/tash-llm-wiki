---
title: "AllowUnsafeMalformedObjectDeletion"
type: reference
domain: openshift
slug: reference-allowunsafemalformedobjectdeletion
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/AllowUnsafeMalformedObjectDeletion
family: reference
documentKind: "doc"
---

# AllowUnsafeMalformedObjectDeletion

Enables the cluster operator to identify corrupt resource(s) using the **list**
operation, and introduces an option `ignoreStoreReadErrorWithClusterBreakingPotential`
that the operator can set to perform unsafe and force **delete** operation of
such corrupt resource(s) using the Kubernetes API.
