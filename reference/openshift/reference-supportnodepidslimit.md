---
title: "SupportNodePidsLimit"
type: reference
domain: openshift
slug: reference-supportnodepidslimit
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/SupportNodePidsLimit
family: reference
documentKind: "doc"
---

# SupportNodePidsLimit

Enable the support to limiting PIDs on the Node.  The parameter
`pid=<number>` in the `--system-reserved` and `--kube-reserved` options can be specified to
ensure that the specified number of process IDs will be reserved for the system as a whole and for
 Kubernetes system daemons respectively.
