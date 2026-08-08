---
title: "GPO password settings not applied in full"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1823800/gpo-password-settings-not-applied-in-full
question_id: 1823800
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO password settings not applied in full

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1823800/gpo-password-settings-not-applied-in-full (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a small issue with a GPO settings being applied to the device. I have changed some password settings in Default Domain Policy and when I run gpupdate /force or restart the device the settings don't change in full. 

What changed is Minimum password length and Maximum password history. Settings like Enforce password history were never set and somehow I have this set to 42 days. And I have noticed that on some devices the value Minimum password length audit is set to 8 characters instead and Minimum password length is set to 0.

Does anyone know how can I figure out from where these settings are coming? I have went over all the settings that are applied with all other GPO's and there is no other GPO's that would contain password settings.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-19*

Hello,

Thank you for posting in Q&A forum.

Here are a few steps you can take to troubleshoot and identify the source of these settings:

1.Group Policy Results Wizard: Use the Group Policy Results Wizard to generate a report on the affected device. This tool will show you which policies are being applied to the device and from where they are coming. Here's how you can use it:

(1)On the affected device, open Command Prompt or PowerShell as an administrator.

(2)Type gpresult /h C:\gpresult.html and press Enter. This command generates a detailed HTML report of applied policies.

(3)Open the generated gpresult.html file in a web browser to view the results.

(4)Look for the sections related to password policies (like Minimum password length, Enforce password history, etc.) to see which GPOs are setting these policies.

2.Group Policy Management Console (GPMC):

(1)Open the GPMC on your domain controller or a machine with the Remote Server Administration Tools (RSAT) installed.

(2)Navigate to "Group Policy Results" under "Group Policy Management".

(3)Enter the computer name of the affected device to run a simulation of applied GPOs and see which ones affect password policies.

3.Check Local Policies: Sometimes local policies can override domain policies. Ensure that no local policies on the affected devices are conflicting with domain policies.

4.Check Security Filtering and OU Linking: Verify that the affected device is in the correct Organizational Unit (OU) and that no security filtering is accidentally applying additional policies.

5.Review Event Logs: Look in the Event Viewer logs on the affected device for any Group Policy-related errors or warnings that might shed light on the issue.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
