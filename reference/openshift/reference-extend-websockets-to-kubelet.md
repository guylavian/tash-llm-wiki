---
title: "ExtendWebSocketsToKubelet"
type: reference
domain: openshift
slug: reference-extend-websockets-to-kubelet
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/extend-websockets-to-kubelet
family: reference
documentKind: "doc"
---

# ExtendWebSocketsToKubelet

When ExtendWebSocketsToKubelet is enabled and a kubelet node advertises support,
exec/attach/portforward streams are proxied directly to the kubelet rather than
being translated or tunneled at the API server. Critically, the same
stream translation and tunneling handlers used at the API server are now set up
identically at the kubelet — the logic is simply moved closer to the container
runtime. This feature depends on NodeDeclaredFeatures graduating to beta so that
kubelet capability advertisement is reliable in production clusters.
