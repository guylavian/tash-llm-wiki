---
title: "active directory disaster recovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192510/active-directory-disaster-recovery
question_id: 2192510
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# active directory disaster recovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192510/active-directory-disaster-recovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a corrupted Windows Server 2012 R2 I need to migrate/transfer to a Windows 2019 server.  How do i accomplish this without rebuilding active directory from scratch.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-16*

Hello James Enlow,  

Thank you for posting in Microsoft Community forum.  

If must try to fix corrupted Windows Server 2012 R2 and then migrate Windows Server 2012 R2 to Windows Server 2019.  

The recommended way to upgrade Windows Server 2012 R2 domain controllers to 2019 domain controllers is adding new 2019 server to domain and promoting this 2019 server as Domain Controller, we do not recommend performing in-place upgrade the OS of 2012 R2 Domain Controller from 2012 R2 to 2019.  

Is your Windows Server 2012 R2 Domain Controller also a DNS server? If so, steps below are for your reference.  

Step 1  

The minimum requirement to add one a domain controller of one of these versions of Windows Server is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.
Step 2You should check SYSVOL replication type. If it is FRS or DFSR.
Here is checking method via registry:  

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

If it is DFSR, that is OK.  

If it is FRS, you should migrate from FRS to DFSR first.  

For how to migrate SYSVOL from FRS to DFSR, we can refer to the following article.

qUICKLY Explained: Migrate Your SYSVOL Replication from FRS to DFSR  

https://blogs.technet.microsoft.com/qzaidi/2012/01/16/quickly-explained-migrate-your-sysvol-replication-from-frs-to-dfsr/

Step 3

Before we do any changes to our AD environment, we had better to check our AD environment health. So we can try the following steps:  

1.We need to check if all the DCs works fine, we can run Dcdiag /v on each DC to check.  

2.Run Repadmin /showrepl and repadmin /replsum on all DCs to check AD replication status if you have multiple DCs in your domain.

Step 4  

1.Add new 2019 server to the existing domain.  

2.Promote this new 2019 server to Domain Controller (add AD DS role and DNS role).  

3.Also make this new 2019 DC as GC.  

4.Check the health status of new DC and old DC and AD replication status (if you have more than one DC) followed Steps 2.  

5.If you have more than one Domain Controllers to migrate from lower OS level (2012 R2) to higher OS level (2019), please repeat 1-4 within Step 3.  

6.After all DCs have migrate from lower OS (2012 R2) to higher OS (2019), transfer FSMO roles to the new 2019 DC if needed.  

We can check whether you have successfully transferred the FSMO roles by running the command as administrator on any DC: netdom query fsmo  

7.Raise forest functional level and domain functional level if needed.

How to raise Active Directory domain and forest functional levels:

https://support.microsoft.com/en-us/help/322692/how-to-raise-active-directory-domain-and-forest-functional-levels  

8.Because old 2012 R2 DC was a DNS server, update the DNS client configuration on all member workstations, member servers, and other DCs that might have used this DNS server for name resolution. If it is required, modify the DHCP scope to reflect the removal of the DNS server.  

9.Because old 2012 R2 DC was a DNS server, update the Forwarder settings and the Delegation settings on any other DNS servers that might have pointed to the old 2012 R2 DC for name resolution.  

10.Migrate all other roles on old 2012 R2 DC to new 2019 DC (or other member servers) if you have or if you need.  

11.After you transfer FSMO roles and update all DNS settings and migrate other roles if you have. And after a period of time, if everything is OK, we can consider demoting the old 2012 R2 DC if needed.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
