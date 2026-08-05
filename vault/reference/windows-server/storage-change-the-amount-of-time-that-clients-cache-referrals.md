---
title: "Change the Amount of Time that Clients Cache Referrals"
type: reference
domain: windows-server
slug: storage-change-the-amount-of-time-that-clients-cache-referrals
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/change-the-amount-of-time-that-clients-cache-referrals
family: storage
documentKind: "how-to"
abstract: "This article describes how to change the amount of time that clients cache referrals"
---

# Change the Amount of Time that Clients Cache Referrals

# Change the amount of time that clients cache referrals

A referral is an ordered list of targets that a client computer receives from a domain controller or namespace server when the user accesses a namespace root or folder with targets in the namespace. You can adjust how long clients cache a referral before requesting a new one.

## To change the amount of time that clients cache namespace root referrals

1.  Click **Start**, point to **Administrative Tools**, and then click **DFS Management**.

2.  In the console tree, under the **Namespaces** node, right-click a namespace, and then click **Properties**.

3.  On the **Referrals** tab, in the **Cache duration (in seconds)** text box, type the amount of time (in seconds) that clients cache namespace root referrals. The default setting is 300 seconds (five minutes).

> [!TIP]
> To change the amount of time that clients cache namespace root referrals by using Windows PowerShell, use the [Set-DfsnRoot TimeToLiveSec](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753448(v=ws.11))
cmdlet. These cmdlets were introduced in Windows Server 2012.

## To change the amount of time that clients cache folder referrals

1.  Click **Start** , point to **Administrative Tools**, and then click **DFS Management**.

2.  In the console tree, under the **Namespaces** node, right-click a folder that has targets, and then click **Properties**.

3.  On the **Referrals** tab, in the **Cache duration (in seconds)** text box, type the amount of time (in seconds) that clients cache folder referrals. The default setting is 1800 seconds (30 minutes).

## Additional References

-   [Tuning DFS Namespaces](tuning-dfs-namespaces.md)
-   [Delegate Management Permissions for DFS Namespaces](delegate-management-permissions-for-dfs-namespaces.md)
