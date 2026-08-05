---
title: "Exchange on-premises distribution groups migration to Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2006866/exchange-on-premises-distribution-groups-migration
question_id: 2006866
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange on-premises distribution groups migration to Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2006866/exchange-on-premises-distribution-groups-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We need to migrate on-premises Exchange distribution groups, around 1000, to Exchange Online.

Please share the process and scripts for the same.

Regards,

Rakesh

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 2 · updated: 2024-08-28*

Hi @Rakesh Kumar,

Welcome to the Microsoft Q&A platform!

Migrating on-premises Exchange distribution groups to Exchange Online involves multiple steps. Here’s a high-level overview of the process:

-  Prepare for Migration:

   - Ensure that your on-premises environment and Exchange Online are properly configured.

   - Verify that your on-premises Active Directory is properly synchronized with Azure AD using Azure AD Connect.

   - Verify you have sufficient permissions to perform these tasks both on-premises and in Exchange Online.

-  Directory Synchronization:

   - If you haven't done so already, set up Azure AD Connect to synchronize your on-premises Active Directory with Azure Active Directory (AAD). This will synchronize all your distribution groups to Azure AD.

   - Run a synchronization and ensure all objects are syncing correctly.

-  Verify Group Data:

   - Confirm that the distribution groups and their memberships are correctly synchronized to Azure AD. You can use the Microsoft 365 admin center or PowerShell to verify this.

-  Convert to Cloud-Managed Groups (if necessary):

   - If you want to manage the groups in the cloud instead of on-premises post-migration, you might need to convert the synchronized distribution groups to cloud-managed groups. This process involves creating new groups in Exchange Online and migrating the members.

   - You can use PowerShell scripts to automate parts of this process.

-  Export Group Information:

   - Use PowerShell to export information about your on-premises distribution groups.

```
Get-DistributionGroup -ResultSize Unlimited | Export-Csv -Path "C:\DistributionGroups.csv"
```

-  Create Groups in Exchange Online:

   - Use a PowerShell script to create these groups in Exchange Online.

```
$groups = Import-Csv -Path "C:\DistributionGroups.csv"
     foreach ($group in $groups) {
         New-DistributionGroup -Name $group.Name -Alias $group.Alias -PrimarySmtpAddress $group.PrimarySmtpAddress
     }
```

-  Add Members to Groups:

   - After creating the groups in Exchange Online, add members to these groups based on the exported data.

```
foreach ($group in $groups) {
         $members = Get-DistributionGroupMember -Identity $group.Identity
         foreach ($member in $members) {
             Add-DistributionGroupMember -Identity $group.Name -Member $member.PrimarySmtpAddress
         }
     }
```

-  Verify Membership:

   - Once the groups are created and members are added, verify the group membership to ensure everything has migrated correctly.

-  Update or Decommission On-Premises Groups:

   - Update your on-premises groups' attributes to reflect their migration status or decommission them if they are no longer needed on-premises.

-  Monitor and Test:

    - Monitor the new distribution groups in Exchange Online to ensure they are functioning as expected.

    - Conduct tests to ensure email flows correctly to and from the new groups.

This is a simplified overview, and the actual steps may vary depending on your specific environment and requirements.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang

## Answer (community) — community member

*upvotes: 1 · updated: 2024-08-28*

Hi, 

There is no direct migration method available to migrate your Distribution groups from On-premises to Office365. You have to re-create the whole list of Distribution groups in Exchange Online. This method is a bit complicated especially if you have nested groups in your environment.

All your distribution groups are stored in your Active Directory. Unless you are going to decommission your Active Directory domain, there is no need to migrate/recreate your Distribution groups in Exchange Online.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-25*

Migration of Mail Enabled Security Group from Exchange On-Premise 2016 to Exchange Online

As part of the migration to Exchange online, all the mailboxes are migrated to Exchange Online. Now, we are left with Distribution lists and Mail enabled security groups(around 5000) needs to be migrated to Exchange Online. Please share the impact on SPO, and other resources. And what are the scripts to get the sites and applications are using these Mail enabled security groups. Please share the step by step script to migrate them?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-28*

If you have firmly decided to recreate the Distribution groups, here are the high level steps.

-  Get a complete report of all the Distribution groups and Members from On-premises.

-  Now, Create the Distribution groups in Exchange Online with a Suffix and add all the correpsonding members .(Example : If On-premises DL is ******@domain.com, you have to create Exchange Online DL as ******@domain.com).  If there are nested DLs, make sure you nest the EXO DLs as well. Make sure you "hide" the EXO distribution groups so that your users wont see them in outlook.

-  Once you have created all the Distribution groups and added corresponding members to it, Schedule a downtime.

-  Delete all the On-premises Distribution groups and Perform Azure AD connect sync.

-  Now, Rename all your EXO distributiongroup email addresses back to its original email address (Example : ******@domain.com will be renamed to ******@domain.com)
