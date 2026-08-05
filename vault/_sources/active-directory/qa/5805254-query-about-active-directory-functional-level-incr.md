---
title: "Query about - Active directory functional level increase (DFL and FFL)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5805254/query-about-active-directory-functional-level-incr
question_id: 5805254
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Query about - Active directory functional level increase (DFL and FFL)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5805254/query-about-active-directory-functional-level-incr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

We need your suggestion for the Domain and forest functional level. In the single forest and 3 domains 1 parent and 2child domains ,  Currently the ffl and dfl is server 2012 R2. We would like to increase it to 2016.

We dont have any 2012 OS DCs and all dcs are mixed of 2016 and 2022 only. I tried to explore whether will it create any impact, I believe this increase will not harm anythingt to applications, this will bring only the new features for the forest and domain.

Can we increase the Domain functional level first then the forest functional level? Is it possible to rollback this changes if any issue? BEfore the changes there will be SSB backup taken.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2026-03-12*

Hey there! It sounds like you’re planning to raise your domain (DFL) and forest (FFL) from Server 2012 R2 to Server 2016 in your single-forest, three-domain environment (one parent + two child domains), and all your DCs already run 2016 or 2022. That’s great news—you're already past the minimum requirement. Here’s a high-level playbook:

-  Validate your environment     • Confirm every DC (including in child domains) is at least Windows Server 2016 or newer.     • Ensure SYSVOL replication is on DFSR (FRS was deprecated).     • Run dcdiag and repadmin /replsummary to verify healthy replication and no lingering errors.     • Check that all FSMO roles are on supported DCs.

-  Take backups & prep     • You’ve mentioned you’ll take a system-state backup—good call.     • Consider a quick lab test (if possible) to simulate the raise.     • Schedule a maintenance window and notify application teams in case of any impact.

-  Raise the Domain Functional Levels first     You can raise each domain’s functional level independently (parent and child) to 2016. You can do that via:     • Active Directory Domains and Trusts UI (right-click domain → Raise Domain Functional Level → select “Windows Server 2016”)     • PowerShell:       Set-ADDomainMode –Identity contoso.com –DomainMode Windows2016Domain  

-  Then raise the Forest Functional Level     Once all domains show 2016, raise the forest level:     • Active Directory Domains and Trusts UI (right-click top → Raise Forest Functional Level → “Windows Server 2016”)     • PowerShell:       Set-ADForestMode –Identity contoso.com –ForestMode Windows2016Forest  

-  Rollback considerations     • Raising DFL/FFL is effectively irreversible. You cannot “lower” back to 2012 R2 once changed.     • Your only real rollback is a restore from your system-state backup or a full VM/host snapshot taken prior to the change.

-  Post-raise tasks     • Verify replication, group policy, DNS, and application authentication flows.     • Test any scripts or monitoring tools that rely on AD schema/role info.     • Enjoy new features like Kerberos enhancements, privileged access management, authentication policy silos, and more.

Follow-Up Questions (if you hit a snag or want to double-check readiness):  

-  Are you using any legacy features in AD (for example, any application still expecting FRS-based SYSVOL)?  

-  Do any on-prem apps rely on downlevel protocols (NTLMv1, DES/RC4 ciphers) that might stop working once you enforce the 2016 DFL?  

-  Are all DCs—including any RODCs—replicating properly and free of errors?  

-  Which DC holds your FSMO roles, and is it on Windows Server 2016 or newer?  

Hope that helps! Let us know if you need more details before you pull the trigger.  

Reference Links:  

• Planning to upgrade the domain and forest functional level and need more information  

  https://onesupport.crm.dynamics.com/.../incident/1891997b-5e7c-f011-b4cc-6045bdd5411f  

• Directory Services component updates (DFL & FFL overview)  

  https://learn.microsoft.com/.../directory-services-component-updates?wt.mc_id=knowledgesearch_inproduct_azure-cxp-community-insider#domain-and-forest-functional-levels  

• How to raise Active Directory domain and forest functional levels  

  https://learn.microsoft.com/troubleshoot/.../raise-active-directory-domain-forest-functional-levels?wt.mc_id=knowledgesearch_inproduct_azure-cxp-community-insider  

• Active Directory Domain Services functional levels (interoperability & features)  

  https://learn.microsoft.com/.../active-directory-functional-levels?wt.mc_id=knowledgesearch_inproduct_azure-cxp-community-insider#windows-server-functional-level-interoperability

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-03*

Raising the domain and forest functional levels from Windows Server 2012 R2 to Windows Server 2016 in a forest where all domain controllers run Windows Server 2016 or 2022 is a supported and recommended path.

Key points for the planned change:

-  Prerequisites and impact

-  All domain controllers in the forest must run Windows Server 2016, 2019, 2022, or later to use the Windows Server 2016 functional level. This requirement is already met because there are no 2012 DCs and only 2016/2022 DCs are present.

-  Functional levels affect only how domain controllers operate together. Clients and applications are not directly broken by raising functional levels; they continue to authenticate and use AD as before. Applications can optionally take advantage of new features available at the higher functional level.

-  Raising functional levels also limits which Windows Server versions can be used as DCs going forward (older DC OS versions will no longer be allowed to join as DCs).

Relevant behavior from the documentation:

-  “To enable the latest domain features, all domain controllers in the domain must run the version of Windows Server that matches or is newer than the desired functional level.”

-  “The domain and forest functional levels only affect how the domain controllers operate together as a group. The clients that interact with the domain or with the forest are unaffected by the changes. Applications are also unaffected by these changes. However, applications can use new features found in later versions of Windows Server after the administrator raises the domain level.”

-  Order: domain functional level vs forest functional level

-  To enable the latest forest-wide features, all domains in the forest must already be at the latest domain functional level.

-  Therefore, the correct order is:

-  Raise the domain functional level (DFL) in each domain (parent and both child domains) to Windows Server 2016.

-  After all domains are at Windows Server 2016 DFL, raise the forest functional level (FFL) to Windows Server 2016.

-  Supported DC OS versions at Windows Server 2016 functional level

-  With a Windows Server 2016 forest and domain functional level, the following DC OS versions are supported:

-  Windows Server 2016

-  Windows Server 2019

-  Windows Server 2022

-  Windows Server 2025

-  Windows Server 2012 R2 DCs are not supported at the 2016 functional level, which aligns with the current environment (no 2012 DCs).

-  Irreversibility and rollback

-  Raising domain and forest functional levels is generally irreversible.

-  The documentation states: “Changes to the domain and forest functional levels are irreversible. To undo the change, you must perform a forest recovery to revert to an earlier point in time.”

-  Earlier guidance about limited rollback scenarios applied to specific cases (for example, Windows Server 2008 R2), but the general rule remains: do not plan on an in-place downgrade of functional levels.

-  Because of this, taking a full backup (including system state/SSB) of all domain controllers and having a tested forest recovery plan is essential if rollback is required.

-  How to raise the functional levels (high level)

-  After verifying all DCs are at supported OS versions and replication is healthy:

-  Raise each domain functional level (for example, using AD administrative tools or PowerShell `Set-ADDomainMode`).

-  Then raise the forest functional level (for example, using PowerShell `Set-ADForestMode`).

-  Example PowerShell syntax from the documentation for forest level:

```
Set-ADForestMode -Identity  -ForestMode 
```

Summary:

-  Yes, the environment described can safely raise DFL and FFL from 2012 R2 to 2016, provided all DCs are 2016/2019/2022 or later.

-  Raise all domain functional levels first, then the forest functional level.

-  The change is effectively one-way; rollback requires full forest recovery from backup, not a simple functional-level downgrade.

References:

-  Raise domain and forest functional levels in Active Directory Domain Services

-  Active Directory Domain Services functional levels

-  Enabling Advanced Features for AD DS

-  Identifying your functional level upgrade

-  How to raise Active Directory domain and forest functional levels
