---
title: "ServiceNodeExclusion"
type: reference
domain: openshift
slug: reference-servicenodeexclusion
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ServiceNodeExclusion
family: reference
documentKind: "doc"
---

# ServiceNodeExclusion

Enable the exclusion of nodes from load balancers created by a cloud provider.
A node is eligible for exclusion if labelled with "`node.kubernetes.io/exclude-from-external-load-balancers`".
