---
title: "BoundServiceAccountTokenVolume"
type: reference
domain: openshift
slug: reference-boundserviceaccounttokenvolume
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/BoundServiceAccountTokenVolume
family: reference
documentKind: "doc"
---

# BoundServiceAccountTokenVolume

Migrate ServiceAccount volumes to use a projected volume
consisting of a ServiceAccountTokenVolumeProjection. Cluster admins can use metric
`serviceaccount_stale_tokens_total` to monitor workloads that are depending on the extended
tokens. If there are no such workloads, turn off extended tokens by starting `kube-apiserver` with
flag `--service-account-extend-token-expiration=false`.

Check [Bound Service Account Tokens](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md)
for more details.
