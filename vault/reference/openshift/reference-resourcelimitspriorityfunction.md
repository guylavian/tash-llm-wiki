---
title: "ResourceLimitsPriorityFunction"
type: reference
domain: openshift
slug: reference-resourcelimitspriorityfunction
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ResourceLimitsPriorityFunction
family: reference
documentKind: "doc"
---

# ResourceLimitsPriorityFunction

Enable a scheduler priority function that
assigns a lowest possible score of 1 to a node that satisfies at least one of
the input Pod's cpu and memory limits. The intent is to break ties between
nodes with same scores.
