---
title: "GPO Script at startup only work when reboot"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1510838/gpo-script-at-startup-only-work-when-reboot
question_id: 1510838
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO Script at startup only work when reboot

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1510838/gpo-script-at-startup-only-work-when-reboot (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I have a DC on Windows server 2022 and client computer on Windows 10/11
I cretated a Computer GPO who execute a powershell script when the computer start.
I try my powershell script : It Work
I try to reboot my computer : It Work 
But when i shutdown my computer and do a normal start up it doesn't work :(
Why my result is different if i do a reboot or a shutdown/startup ? 
Do you have any idea ?
I can't use a user gpo because some computer are in the domain but use local account ;) 
Thank's
Yoan

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-01-25*

Hello Yoan L,
Thank you for posting in Q&A forum.

You can first check the operating conditions of the configured group policy and confirm whether to turn on or restart the computer. Secondly, disable quick start.
If the content of the PowerShell script you configure is related to the network, you need to schedule the policy runtime after networking.
Specific operations: Computer Configuration>Policies>Management Templates>System>Group Policy>Start Policy Processing Wait Time (set to 90 seconds)
Computer Configuration>Policies>Administrative Templates>System>Login>Always wait for network when computer starts and logs in (enable this policy)
Alternatively, you can use the startup script group policy settings:
Open the Group Policy Manager, create a new Group Policy in the appropriate location, and then name it.
Right click on the group policy and select "Edit" to open the Group Policy Management Editor.
Navigation to Computer Configuration>Policies>Windows Settings>Scripts (Start/Shutdown).
Double click on "Start" on the right side, then select "PowerShell" and configure the script you need according to the situation.
If the problem still cannot be solved, you can take a screenshot of the detailed configuration policy and post it on the forum.
I hope the information above is helpful.
If you have any questions or concerns, please feel free to let us know.
Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-25*

Hello,It worked yes : I have setup a new gpo registry policy who modify the HiberbootEnable from 1 to 0 and now my policy work when i shutdown or restart my computer. The key :
Copy

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power\HiberbootEnabled
```

Thank you ! PS : i also have a policy who wait the network at the boot : Computer Configuration>Policies>Administrative Templates>System>Login>Always wait for network when computer starts
