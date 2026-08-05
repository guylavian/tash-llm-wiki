---
title: "Disable Win 11 factory reset (GPO/MDM)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2123457/disable-win-11-factory-reset-gpo-mdm
question_id: 2123457
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Disable Win 11 factory reset (GPO/MDM)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2123457/disable-win-11-factory-reset-gpo-mdm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to create a GPO & a MDM ( Hybrid environment) policy to disable users from performing factory reset to their Win11 PCs/Laptops. (Something like denying access to C:\Windows\system32\systemreset.exe =  Which I cannot find on Win 11)

Also, it will be much better if I could create something that will allow reset feature to domain admins only, not even the local admin cannot reset the PC.

Cheers. 

~lmgmcg~

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-11-27*

@lmgmcg  Thanks for posting in our Q&A. 

From intune's point of view, there is no built-in setting can disable Win 11 factory reset. To make it, it is suggested to write a PowerShell script with commend "reagentc.exe /disable" and deploy this script via intune. 

https://learn.microsoft.com/en-us/mem/intune/apps/intune-management-extension

Hope it will give you some ideas.

If the answer is helpful, please click "Accept Answer"  and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-11-26*

Configure Windows Reset Settings in Intune: (MDM)

Navigate to Endpoint security > Windows settings in the Intune portal.

Create a policy to restrict resetting options.

Set `Block users from resetting their devices` to Yes (apply this policy to all users except domain admins).

Prevent factory reset using GPO

-  Disable Access to Recovery Options: Use Group Policy to disable access to the recovery options, including the reset functionality. Here's how to configure it:

-  Open Group Policy Management: On a domain controller or machine with the GPO management tools, open `Group Policy Management Console (GPMC)`.

-  Create or Edit a GPO: Right-click on an existing GPO or create a new one. Navigate to the following path:

-  `Computer Configuration ``->`` Administrative Templates ``->`` System ``->`` Recovery`

-  Enable the policy to disable Reset:

-  Disable or Hide the "Reset this PC" option: This prevents users from accessing the "Reset this PC" feature from the Settings.

-  Policy Name: `Do not allow reset of the PC`

-  Set this policy to: `Enabled`

-  This will prevent users from accessing the "Reset this PC" option in the settings.

-  Apply the GPO: Link the GPO to the appropriate Organizational Unit (OU) where your user and computer accounts reside.

-  Disable Recovery Environment: Additionally, you can disable access to the Recovery Environment entirely, which would further prevent users from performing a reset in any situation.

-  Path: `Computer Configuration -> Administrative Templates -> System -> Recovery`

-  Policy Name: `Disable Recovery Environment`

-  Set to: `Enabled`
