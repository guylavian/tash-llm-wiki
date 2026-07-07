---
title: "BtreeWatchCache"
type: reference
domain: openshift
slug: reference-btreewatchcache
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/BtreeWatchCache
family: reference
documentKind: "doc"
---

# BtreeWatchCache

When enabled, the API server will replace the legacy HashMap-based _watch cache_
with a BTree-based implementation. This replacement may bring performance improvements.
