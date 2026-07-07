---
title: "VolumeScheduling"
type: reference
domain: openshift
slug: reference-volumescheduling
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/VolumeScheduling
family: reference
documentKind: "doc"
---

# VolumeScheduling

Enable volume topology aware scheduling and make the PersistentVolumeClaim
(PVC) binding aware of scheduling decisions. It also enables the usage of
[`local`](/docs/concepts/storage/volumes/#local) volume type when used together with the
`PersistentLocalVolumes` feature gate.
