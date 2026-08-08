---
title: "MatchLabelKeysInPodTopologySpreadSelectorMerge"
type: reference
domain: openshift
slug: reference-matchlabelkeysinpodtopologyspreadselectormerge
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/MatchLabelKeysInPodTopologySpreadSelectorMerge
family: reference
documentKind: "doc"
---

# MatchLabelKeysInPodTopologySpreadSelectorMerge

Enable merging of selectors built from `matchLabelKeys` into `labelSelector` of 
[Pod topology spread constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/).
This feature gate can be enabled when `matchLabelKeys` feature is enabled with the `MatchLabelKeysInPodTopologySpread` feature flag.
