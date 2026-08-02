---
title: "Deploy Teams machine-wide via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163703/deploy-teams-machine-wide-via-gpo
question_id: 1163703
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-teams-teams-business-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Deploy Teams machine-wide via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163703/deploy-teams-machine-wide-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,  

Lately we are receiving multiple complaints from users who are not able to start Teams (path doesn't exist).  

Instead of installing Teams for these users one by one, we would like to deploy Teams (machine-wide) via GPO.

I already downloaded the Teams Machine-wide installer (msi) and created a new GPO, added the msi to new package in software installation, but unfortunately after applying the GPO to the pc, Teams won't get installed.  

Is there any way to deploy Teams through GPO (perhaps with help of a Powershell script)?  

Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

Hi, thank you for your comments.

Instead of running the script at startup, I set up the GPO as a scheduled (immediate) task.  

Via this way it places the installer under Program Files (x86), so it seems to work correctly.  

I just haven't managed to get to the point where it also automatically installs Teams for users who do not have Teams installed yet. For now, I have sent out a manual instruction so the users will have to click manually on the Teams.exe file in the Teams installer folder, after which Teams installs succesfully.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-24*

Hi,

Yes, it's possible to deploy teams through powershell script :

`msiexec /i "`\`Teamsfilepath\Teams_windows_x64.msi" OPTIONS="noAutoStart=true"`

You can create powershell script and add it as Startup/Shutdown scripts through GPO.

Please don't forget to mark helpful answer as accepted
