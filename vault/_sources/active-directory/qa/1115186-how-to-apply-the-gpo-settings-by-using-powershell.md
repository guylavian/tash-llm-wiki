---
title: "How to apply the GPO settings by using PowerShell scripts."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1115186/how-to-apply-the-gpo-settings-by-using-powershell
question_id: 1115186
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to apply the GPO settings by using PowerShell scripts.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1115186/how-to-apply-the-gpo-settings-by-using-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,    

We required your help to create the GPO settings via PowerShell script.     

Example : I would like to apply the GPO settings to turn of the handwriting recognition error reporting via from PowerShell.    

I know steps how to apply the settings by manually to navigate the path location, but I would like to know the same steps from using PowerShell Script    

Appreciate your help! Thanks

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-06*

Hi @Vinodh Kumar S  ,    

There is no universal method to configure a GPO using PowerShell. However, to configure the registry-based GPOs like "Turn off handwriting recognition error reporting", you can use New-GPO to create a new GPO and Set-GPRegistryValue to set the registry values of that.    

 https://learn.microsoft.com/en-us/powershell/module/grouppolicy/new-gpo    

https://learn.microsoft.com/en-us/powershell/module/grouppolicy/set-gpregistryvalue    

Best Regards,    

Ian Xue    

-----------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
