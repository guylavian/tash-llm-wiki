---
title: "Domain Controller Upgrade Process from Windows Server 2016 to 2022 with Same Name and IP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3318926/domain-controller-upgrade-process-from-windows-ser
question_id: 3318926
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Domain Controller Upgrade Process from Windows Server 2016 to 2022 with Same Name and IP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3318926/domain-controller-upgrade-process-from-windows-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What is the process for upgrading Domain Controllers from Windows Server 2016 to Windows Server 2022 while ensuring that the new Domain Controllers retain the same names and IP addresses as the old ones?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-07-16*

You can’t do an in-place OS upgrade and keep the same DC name/IP cleanly — the correct way is to install new 2022 DCs, replicate, then demote old ones. Here’s how.

✅ Correct Upgrade Process (Retain Same Name/IP Eventually)

-  Prep:

-  Full backup of current DC (System State + AD)

-  Ensure current domain/forest functional level supports 2022

-  Run:

```
adprep /forestprep
```

adprep /domainprep
     ```

```
*(from 2022 ISO on existing DC)*
```

-  Build Temporary 2022 DC:

-  New VM or physical server with temporary name + IP

-  Join domain

-  Promote to Domain Controller using Server Manager or `dcpromo`

-  Wait for replication to fully complete

-  Transfer FSMO Roles to new DC

```
netdom query fsmo
```

ntdsutil (to transfer)

```
1. **Demote & Decommission Old 2016 DC**

   - Use Server Manager or `dcpromo`
   
   - Remove from domain
   
   - Shutdown
   
1. **Rename and Re-IP 2022 DC to old DC’s name/IP**

   - Use:
   
     ```yaml
     
     netdom computername  /add:
netdom computername  /makeprimary:
netdom computername  /remove:
     ```
     
   - Reboot
   
   - Set static IP to match old DC
   
Best Regards,
```
