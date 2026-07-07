---
title: "ZeroLimitedNominalConcurrencyShares"
type: reference
domain: openshift
slug: reference-zerolimitednominalconcurrencyshares
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ZeroLimitedNominalConcurrencyShares
family: reference
documentKind: "doc"
---

# ZeroLimitedNominalConcurrencyShares

Allow [priority & fairness](/docs/concepts/cluster-administration/flow-control/)
in the API server to use a zero value for the `nominalConcurrencyShares` field of
the `limited` section of a priority level.
