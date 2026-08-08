---
title: "GPO related"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1294034/gpo-related
question_id: 1294034
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO related

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1294034/gpo-related (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there any GPO which cannot be set into disable after disabled it?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-05-31*

@ネパリ サンデャ

To delete a Group Policy Object (GPO) that is not visible in the Group Policy Management Console (GPMC) GUI, you can use the PowerShell cmdlets provided by the Group Policy module. Here's a step-by-step guide:

Open an elevated PowerShell session. Right-click on the PowerShell icon and select "Run as Administrator".

-  Import the Group Policy module by running the following command:

```
Import-Module GroupPolicy
```

3-List all the GPOs to identify the GPO you want to delete. Run the following command:

```
Get-GPO -All
```

This will display a list of all GPOs in the domain, including the hidden ones.

Identify the GPO you want to delete based on its name or other relevant details.

-  To delete the GPO, use the `Remove-GPO` cmdlet followed by the GPO's display name. For example, if the GPO's display name is "Windows XP Settings", you can use the following command:

```
Remove-GPO -Name "Windows XP Settings"
```

Please ensure that you replace "Windows XP Settings" with the actual display name of the GPO you want to delete.

Confirm the deletion when prompted.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-05-30*

Hi ネパリ サンデャ

No, it is not accurate to assume that Group Policy Objects (GPOs) that cannot be reverted after enabling them can be determined solely from their description. The ability to revert or undo a GPO change depends on various factors, including the specific settings applied by the GPO, the nature of the change, and the configuration of the affected systems.

While the description of a GPO can provide insights into its purpose and intended effects, it may not indicate whether the changes made by the GPO are reversible or permanent. The reversibility of a GPO typically depends on the individual settings and their impact on the system or network.

To determine if a particular GPO change is reversible, it's crucial to understand the settings and policies being modified, as well as the potential implications of those changes. Consulting the documentation or seeking expert advice can help in evaluating the impact and reversibility of specific GPO settings. Additionally, creating backups or snapshots of system configurations before making significant GPO changes can provide a safety net to restore previous settings if needed.

#Another opinion

it is important to carefully consider the implications of enabling a GPO before doing so.

Here are some examples of GPOs that cannot be reverted:

-  GPOs that change the default user profile

-  GPOs that change the default security settings

-  GPOs that install software

-  GPOs that create or delete user accounts

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-30*

Hi JK

In general, Group Policy Objects (GPOs) are designed to be reversible, meaning that settings applied through GPOs can typically be disabled or reverted back to their original state. However, there are some scenarios where certain GPO settings may not revert back to their previous state after they have been disabled. Here are a few examples:

-  Preferences vs. Policy settings: Group Policy Preferences (GPP) and Group Policy Policy settings (GPPolicy) behave differently in terms of reversibility. GPP settings, such as mapped drives or printer preferences, are typically reversible and will revert back once the GPO is disabled or removed. On the other hand, GPPolicy settings, which are typically found in Administrative Templates, may persist even after the GPO is disabled. This is because GPPolicy settings modify registry values directly, and disabling the GPO does not automatically revert those changes.

-  Software installation: If you use Group Policy to deploy software installations, the installed software might not be automatically uninstalled when the GPO is disabled or removed. Group Policy-based software installations are typically assigned to computers rather than users, and the software remains installed until explicitly removed or uninstalled.

-  Registry modifications: Some GPOs modify registry settings to enforce specific configurations. If a GPO modifies registry settings that are not part of a specific policy area, such as Administrative Templates, the changes may persist even after the GPO is disabled. Disabling the GPO does not automatically revert the registry modifications made by the GPO.

It's important to carefully plan and test GPO changes to understand the potential impact they may have. If you need to revert specific settings or configurations applied by a GPO, you may need to manually reverse the changes by modifying the affected settings or registry values directly.

Remember to exercise caution when making changes to GPOs, especially if they modify system settings or configurations. Always test GPO changes in a controlled environment before applying them to production systems.
