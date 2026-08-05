---
title: "LegacyNodeRoleBehavior"
type: reference
domain: openshift
slug: reference-legacynoderolebehavior
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/LegacyNodeRoleBehavior
family: reference
documentKind: "doc"
---

# LegacyNodeRoleBehavior

When disabled, legacy behavior in service load balancers and
node disruption will ignore the `node-role.kubernetes.io/master` label in favor of the
feature-specific labels provided by `NodeDisruptionExclusion` and `ServiceNodeExclusion`.
