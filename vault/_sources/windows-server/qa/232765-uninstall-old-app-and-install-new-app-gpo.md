---
title: "Uninstall old app and install new app GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/232765/uninstall-old-app-and-install-new-app-gpo
question_id: 232765
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Uninstall old app and install new app GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/232765/uninstall-old-app-and-install-new-app-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to uninstall an old outdated version of an app and install a the new version. The original install of the app was not done via GPO rather manually, so I can't simply remove the GPO and it uninstall.  

Should I create a shutdown script to uninstall the old app and then create an install script to install the new version? I already have a GPO scripted to install the new app. It will only work on new freshly imaged machines because it doesn't have the old app version on there, but what about the ones that have the old version?  

Also, how do I find the exact name of the app that I want to uninstall? I'm sure there is a powershell or cmd command for that. This is in a Windows Server 2019 domain environment.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-20*

You can use PowerShell to uninstall the software, or use the tool to speed up the process.    

Link to the article directly:    

https://www.silentinstall.org/uninstall-gpo/

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-21*

Hello,    

Thank you so much for your kindly reply.    

Yeah, we could totally understand our situation. So sorry that we are not professional with script. According to my research:    

WMIC – ‘Windows Management Interface Command’ can be used for .EXE’s    

MSIEXEC – ‘Microsoft Installer Executable’ can be used for programs that installed using a .MSI file    

I think startup script would work. Below is the discussion about the similar case, and we could kindly have a check.    

https://social.technet.microsoft.com/Forums/en-US/f48c0093-d7db-4c0f-b4a6-f72aa5730935/removing-software-via-group-policy?forum=winserverGP    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Yeah, that makes since. It would have been a lot easier had the app been applied via GPO in the first place.   

Unfortunately, I work in a "rush, rush" environment and the person before me did a lot of the installs manually.  

The app I want uninstall was installed using an .exe file not .msi. When creating the script should I use the WMIC or MSIEXEC command? I believe the MSIEXEC command only works on packages that were install with an msi file?  

My question is would a logoff script work?   

Thanks,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

Hello,    

Thank you so much for posting here.    

We mainly focus on the GPO issue. GPO can only uninstall what it installed.  If it was manually installed, then it will have to be manually uninstalled prior to GPO deployment of the new one. So the manually installed app should be uninstalled first, whether manually or shutdown script.     

So sorry that we are not professional with the powershell or cmd command. If we have more questions about powershell script, there is dedicated forum. We could turn to this for further assistance.     

https://learn.microsoft.com/en-us/answers/topics/windows-server-powershell.html    

Thank you so much for your understanding and support.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
