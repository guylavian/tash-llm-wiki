---
title: "CSIServiceAccountTokenSecrets"
type: reference
domain: openshift
slug: reference-csiserviceaccounttokensecrets
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/CSIServiceAccountTokenSecrets
family: reference
documentKind: "doc"
---

# CSIServiceAccountTokenSecrets

Enables CSI drivers to opt-in for receiving service account tokens from kubelet
through the dedicated secrets field in NodePublishVolumeRequest instead of the volume_context field.
