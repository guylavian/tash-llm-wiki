---
title: "ConcurrentWatchObjectDecode"
type: reference
domain: openshift
slug: reference-concurrentwatchobjectdecode
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ConcurrentWatchObjectDecode
family: reference
documentKind: "doc"
---

# ConcurrentWatchObjectDecode

Enable concurrent watch object decoding. This is to avoid starving the API server's
watch cache when a conversion webhook is installed.
