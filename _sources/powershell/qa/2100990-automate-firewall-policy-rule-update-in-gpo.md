---
title: "Automate firewall policy rule update in GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2100990/automate-firewall-policy-rule-update-in-gpo
question_id: 2100990
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Automate firewall policy rule update in GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2100990/automate-firewall-policy-rule-update-in-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

We are applying firewall rules for all my domain machines through GPO. I have three GPOs for firewall rules that apply to workstations, servers, and domain controllers. Therefore, we have different sets of inbound and outbound firewall rules for each GPO.

Now, I need a PowerShell script that updates the remote address for a particular rule in a specific GPO . I would like to provide input in a data preparation file, and the script should apply the remote address for that particular GPO.

For example, I have the GPOs `Wks_Firewall_GPO`, `Server_Firewall_GPO`, and `DC_Firewall_GPO` on my domain controller. In the `Wks_Firewall_GPO`, I have an inbound rule for which I need to add a few more remote addresses via the PowerShell script. i need to execute this script from my domain controller.

Could you please assist me with this?

Regards,

Mowlee

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-11*

Hello P Mowleeswaran,

Thank you for posting in Q&A forum.

I am sorry we don’t directly write script for use on the forum, and I am not familiar with script.

I think you could use the Get-GPO, Get-GPRegistryValue, and Set-GPRegistryValue cmdlets to achieve it.

For example:

Get-GPO -Name "YourGPOName"

Get-GPRegistryValue -Name "YourGPOName" -Key “registryPath”  -ValueName ”ruleName”

References:

Get-GPO (GroupPolicy) | Microsoft Learn

Get-GPRegistryValue (GroupPolicy) | Microsoft Learn

Set-GPRegistryValue (GroupPolicy) | Microsoft Learn

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
