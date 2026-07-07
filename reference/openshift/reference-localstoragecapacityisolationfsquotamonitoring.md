---
title: "LocalStorageCapacityIsolationFSQuotaMonitoring"
type: reference
domain: openshift
slug: reference-localstoragecapacityisolationfsquotamonitoring
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/LocalStorageCapacityIsolationFSQuotaMonitoring
family: reference
documentKind: "doc"
---

# LocalStorageCapacityIsolationFSQuotaMonitoring

When `LocalStorageCapacityIsolation` 
is enabled for 
[local ephemeral storage](/docs/concepts/configuration/manage-resources-containers/), 
the backing filesystem for [emptyDir volumes](/docs/concepts/storage/volumes/#emptydir) supports project quotas,
and `UserNamespacesSupport` is enabled, 
project quotas are used to monitor `emptyDir` volume storage consumption rather than using filesystem walk, ensuring better performance and accuracy.
