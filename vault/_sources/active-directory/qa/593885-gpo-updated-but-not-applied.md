---
title: "GPO updated but not applied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/593885/gpo-updated-but-not-applied
question_id: 593885
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# GPO updated but not applied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/593885/gpo-updated-but-not-applied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 different GPOs, both which contain the same settings. These 2 GPOs are applied only one at a time, with the other unlinked if one of the GPOs are linked.  

One GPO was configured using the GPMC.msc, the other is configured using Powershell "Set-GPRegistryValue" cmdlet.  

Using GPMC.msc, i can confirm that the settings in the GPO have been updated from the Powershell cmdlets.  

Even on the Client RSOP.msc, I am able to view the settings for both of these policies.  

However, when applying to an Organizational Unit (OU), the GPO that was configured by Powershell does not apply (despite rsop.msc saying so) , but the GPO configured by the GPMC.msc GUI applies.  

The particular settings that were tested is from LAPS, with the following commands:  

Reset-AdmPwdPassword  

Get-AdmPwdPassword  

Reset-AdmPwdPassword and Get-AdmPwdPassword works when GPO that is created using GUI is applied, but not the GPO created using Powershell. [On the GPO created by Powershell, Reset-AdmPwdPassword does not change password even after client has done a gpupdate. Get-AdmPwdPassword will give blank when it is the first GPO applied]  

Do I need to do something else after using the Set-GPRegistryValue?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-19*

Hey @GaryReynolds-8098 ,    

You're right, it was an oversight on my part, and I can verify that the policy is being updated on the client..    

By using the GPO Explorer tool, it seems that the difference between the 2 GPOs are that the working version has the LAPs Client extension, while the non-working version does not.     

As I've compared all the settings available in the GPMC, and was unable to find this particular setting, I hope that you're able to help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-18*

Hi @Jie wei       

The policy hasn't been applied because the version is 0, which indicates that policy is empty. However, this is the local policy, this is not the policy you created in gpmc so shouldn't be linked to your problem.    

Check for the name of the policy you created, I'm assuming its gp_raw, which is showing a green indicator meaning it was applied to the machine.  Use the GPO Explorer option to compare the two gpos you created, and see if there any differences, the Settings tab lets you see the raw settings.    

If the GPO is being applied but it is not working as expected using the powershell command, there gpmc might be adding additional settings that enable the feature.    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-18*

Hi @GaryReynolds-8098 ,    

 I've looked at the post that you mentioned and have the following results. It is mentioned that the GPO section is empty, and yet, in the RSOP.msc, the values are set. Hope you are able to help.  The result is for the GPO created by Powershell.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-18*

Hi @Jie wei       

Have a look at this post to help troubleshoot why the policy is not being applied and review what settings are being written to the policy.    

Gary.
