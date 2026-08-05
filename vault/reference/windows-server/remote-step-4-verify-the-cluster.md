---
title: "Step 4 Verify the Cluster"
type: reference
domain: windows-server
slug: remote-step-4-verify-the-cluster
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/ras/cluster/configure/Step-4-Verify-the-Cluster
family: remote
documentKind: "how-to"
abstract: "Learn how to verify that you have correctly configured your DirectAccess cluster deployment."
---

# Step 4 Verify the Cluster

# Step 4 Verify the Cluster

This topic describes how to verify that you have correctly configured your DirectAccess cluster deployment.

### To verify access to internal resources through the cluster

1.  Connect a DirectAccess client computer to the corporate network and obtain the group policy.

2.  Connect the client computer to the external network and attempt to access internal resources.

    You should be able to access all corporate resources.

3.  Test connectivity through each server in the cluster by turning off, or disconnecting from the external network, all but one of the cluster servers. On the client computer, attempt to access corporate resources. Repeat the test on a different cluster server.

    You should be able to access all corporate resources through each cluster server.
