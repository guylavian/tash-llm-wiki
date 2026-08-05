---
title: "NodeOutOfServiceVolumeDetach"
type: reference
domain: openshift
slug: reference-nodeoutofservicevolumedetach
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/NodeOutOfServiceVolumeDetach
family: reference
documentKind: "doc"
---

# NodeOutOfServiceVolumeDetach

When a Node is marked out-of-service using the
`node.kubernetes.io/out-of-service` taint, Pods on the node will be forcefully deleted
 if they can not tolerate this taint, and the volume detach operations for Pods terminating
 on the node will happen immediately. The deleted Pods can recover quickly on different nodes.
