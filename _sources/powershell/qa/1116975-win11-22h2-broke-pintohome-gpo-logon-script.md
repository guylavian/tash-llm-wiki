---
title: "Win11 22H2 Broke PINTOHOME GPO Logon Script"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1116975/win11-22h2-broke-pintohome-gpo-logon-script
question_id: 1116975
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Win11 22H2 Broke PINTOHOME GPO Logon Script

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1116975/win11-22h2-broke-pintohome-gpo-logon-script (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I use a script set to run at logon to pin network folders to quick access on user desktops. After this update users that logon no longer see their shared folders. I am guessing it is due to the quick access being changed to "Home" in Windows 11 22H2.     

Any idea why this script would no longer function via GPO logon script? It works on every other version of Windows in our environment.     

If I run the script manually on the affected devices in Powershell it works and will repopulate the shared folders, but they will disappear again when the user logs off and back on.     

$folder1 = "\my.domain.com\asharedfolder"    

$QuickAccess = New-Object -ComObject shell.application    

$QuickAccess.Namespace($folder1).Self.InvokeVerb("pintohome")

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-28*

Did anyone work this out?

I found that the pinned folder is added when i run the script and when i run the script for a 2nd time it gets removed and so on in a loop. This could explain why it's removed after log off/on assuming it then gets added back again with another log off/on.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-17*

Same problem here. Commands don't work onb WIndows 11 clients, when typed in a powershell session either.

Works in Windows 10.

Is there some registry change envolved?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-07*

Hello there,    

As the same script works fine with other versions this might one of the changes that has been brought to the 22H2 update.    

Try disabling the policy at Computer Configuration\Policies\Administrative Templates\System\Group Policy\Configure Logon Script Delay and see if that helps. I too doubt that the script is being executed before retrieving the required information.    

Something you might dig on here https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-gpscr/a8e62e3b-08f5-4c41-b77a-31f1ee4f3125    

You can also raise feedback to the Microsoft team. The Feedback Hub app lets you tell Microsoft about any problems you run into https://support.microsoft.com/en-us/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332    

--------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-12-06*

Hi    

Like we discussed in comment; I higly recommand that settings firrst;    

You need to create another for that one as it's a computer settings    

Computer Configuration > Administrative Templates > System > Logon, enable the Always wait for the network at computer startup and logon setting.    

I recommand it as the problem you have can happen if the computer execute the script before the network card receive the IP and be ready on the network, as such the script can fail to map.
