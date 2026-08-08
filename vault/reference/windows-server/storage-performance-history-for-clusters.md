---
title: "Performance history for clusters"
type: reference
domain: windows-server
slug: storage-performance-history-for-clusters
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/performance-history-for-clusters
family: storage
documentKind: "concept-article"
abstract: "Learn more about: Performance history for clusters"
---

# Performance history for clusters

# Performance history for clusters

This sub-topic of [Performance history for Storage Spaces Direct](performance-history.md) describes the performance history collected for clusters.

There are no series that originate at the cluster level. Instead, server series, such as `clusternode.cpu.usage`, are aggregated for all servers in the cluster. Volume series, such as `volume.iops.total`, are aggregated for all volumes in the cluster. And drive series, such as `physicaldisk.size.total`, are aggregated for all drives in the cluster.

## Usage in PowerShell

Use the [Get-Cluster](/powershell/module/failoverclusters/get-cluster) cmdlet:

```PowerShell
Get-Cluster | Get-ClusterPerf
```

## Additional References

- [Performance history for Storage Spaces Direct](performance-history.md)
