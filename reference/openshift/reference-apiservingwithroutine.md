---
title: "APIServingWithRoutine"
type: reference
domain: openshift
slug: reference-apiservingwithroutine
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/APIServingWithRoutine
family: reference
documentKind: "doc"
---

# APIServingWithRoutine

This feature gate enables an API server performance improvement:
the API server can use separate goroutines (lightweight threads managed by the Go runtime)
to serve [**watch**](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes)
requests.
