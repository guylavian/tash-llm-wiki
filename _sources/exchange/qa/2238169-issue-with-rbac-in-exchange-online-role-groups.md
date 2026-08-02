---
title: "Issue with RBAC in Exchange Online Role Groups"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2238169/issue-with-rbac-in-exchange-online-role-groups
question_id: 2238169
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue with RBAC in Exchange Online Role Groups

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2238169/issue-with-rbac-in-exchange-online-role-groups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In designing a support operational model, several custom role groups have been created with specific permissions. Testing in a development tenant was successful, but in the production environment, some users are missing access to certain cmdlets (e.g., `Get-MessageTrace`, `Add-RecipientPermission`) despite being assigned to the correct role group.

```
New-RoleGroup -Name "Exchange Operator" -Description "Handles simple user-related tasks and basic issue resolution. Members can manage mailbox permissions, track messages, and view quarantined emails." -DisplayName "Exchange Operator" -ManagedBy "[******@pepe.com](mailto:******@pepe.com)", "[******@pepe.com](mailto:******@pepe.com)" -Roles "Mail Recipients","Message Tracking","View-Only Recipients","User Options"   

New-RoleGroup -Name "Exchange Engineer" -Description "Handles more complex tasks and advanced troubleshooting. Includes all Operator permissions, plus management of distribution groups, transport rules, and quarantined emails." -DisplayName "Exchange Engineer" -ManagedBy "[******@pepe.com](mailto:******@pepe.com)", "[******@pepe.com](mailto:******@pepe.com)" -Roles "Mail Recipients","Message Tracking","View-Only Recipients","User Options", "Distribution Groups", "Mail Tips", "Migration", "Transport Rules", "Mailbox Search", "Audit Logs", "Mail Recipient Creation", "Security Reader"
```

Access is granted through PIM roles in Azure, which has been functioning properly until now. What could be causing the discrepancies in cmdlet access in the production environment?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-25*

To add more info, if I assign users directly to the role created on the EAC, permissions work fine! It only seems to fail when using PIM Role

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-25*

No "error" shown. 

The issue is that certain options don’t even appear in the GUI for these users. For example, members of the Operator group cannot run a message trace — the option simply isn’t visible. Similarly, members of the Engineering group are unable to add recipient permissions to a mailbox, as that option is also missing (grant access and send on behalf are present).

This behavior is consistent both in the Exchange Admin Center (GUI) and when using PowerShell — the relevant cmdlets aren’t available either.

Regarding the second part of your question: yes, we’ve also tried assigning the roles directly in the Exchange Admin Center (instead of using PIM in Azure), but the result is exactly the same.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-25*

Hi,@Manu

Thanks for posting your question in the Microsoft Q&A forum.

Based on your description, you assigned permissions to the user, but the user still doesn't seem to be able to use some of the commands.

What is the error reported when the user is unable to use these commands?

Has there been any attempt to set up role groups in EAC and does the same problem occur?
