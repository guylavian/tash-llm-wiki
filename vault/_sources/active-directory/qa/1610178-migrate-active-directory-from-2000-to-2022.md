---
title: "Migrate Active Directory from 2000 to 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1610178/migrate-active-directory-from-2000-to-2022
question_id: 1610178
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Migrate Active Directory from 2000 to 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1610178/migrate-active-directory-from-2000-to-2022 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,

We have a Windows 2000 Active Directory need to migrate to Windows 2022. Do below migration path correct? 

-  Setup new Windows 2003 DC

-  Move FSMO, remove Windows 2000 DC and raise functional level

-  Setup new Windows 2012 R2 DC

-  Move FSMO, remove Windows 2003 DC and raise functional level

-  Migrate FRS to DFRS

-  Setup new Windows 2022 DC

-  Move FSMO, remove Windows 2012 R2 DC and raise functional level  

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-08*

Hello Chong，

Thank you for posting in Q&A forum.

Based on your description, your migration steps are feasible. However, you can also make some optimization adjustments, you can remove Windows 200 0DC from Windows 2000 AD - Windows 2008 R2 DC - Mobile FSMO. Raise the functional level to Windows 2008 R2 - Migrate FRS to DFRS (Windows 2012R2 DC can be skipped) - Add Windows 2022DC directly - Move FSMO, remove Windows 2008 R2 DC, raise functional level to Windows 2022. The above skips the Windows 2012 R2 DC step, which is possible because migrating from Windows 2000 to 2008 R2 allows you to jump directly to 2022 after migrating from FRS to DFRS.

Here are the general steps, but please note that this is only an overview. Before you make the migration, be sure to back up your Active Directory data and test it out of production.

To upgrade to an intermediate version:

First, upgrade your Windows Server 2000 to an intermediate version that supports lift-and-shift, such as Windows Server 2008 or Windows Server 2012. This is a necessary step because there is no migration path from Windows Server 2000 to 2022 that is directly supported.

Migrating to a new domain controller:

Install Windows Server 2022 and add it as a new domain controller. Make sure it becomes a member of the domain and copy all the necessary directory information.

To migrate the FSMO role:

Migrate the Flexible Single Master Operations (FSMO) role from the old domain controller to the new domain controller. This includes Schema Master, Domain Naming Master, Relative Identity Master, Domain Controller Naming Master, and Schema Master.

To migrate users and groups:

Migrate users, groups, and computer objects. You can use the Active Directory Migration Tool (ADMT) or other tools to do this. Ensure that all SIDs and permissions are properly mapped.

DNS Migration:

If your DNS is integrated with Active Directory, ensure that your DNS settings are properly migrated to the new domain controllers. Ensure that all clients and servers correctly resolve the names of the new domain controllers.

Validation & Testing:

Verify that all users and groups were successfully migrated to ensure that all domain controllers are working properly. Conduct appropriate testing to ensure that applications and services work with the new environment.

To remove the old domain controller:

Securely remove old Windows Server 2000 domain controllers from the domain. Ensure that all data has been successfully migrated and there are no services that depend on the legacy domain controller before performing this step.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-07*

This seems like a valid plan - details would depend on the number of domain controllers, but the high-level approach looks fine.

You could potentially use in-place upgrade in some of these steps, but deploying another domain controller in the same domain increases the resiliency and facilitates failback. 

hth

Marcin
