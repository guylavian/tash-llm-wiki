---
title: "StatefulSetAutoDeletePVC"
type: reference
domain: openshift
slug: reference-statefulsetautodeletepvc
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/StatefulSetAutoDeletePVC
family: reference
documentKind: "doc"
---

# StatefulSetAutoDeletePVC

Allows the use of the optional `.spec.persistentVolumeClaimRetentionPolicy` field, 
providing control over the deletion of PVCs in a StatefulSet's lifecycle.
See
[PersistentVolumeClaim retention](/docs/concepts/workloads/controllers/statefulset/#persistentvolumeclaim-retention)
for more details.
