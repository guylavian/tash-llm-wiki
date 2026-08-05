---
title: "Unable to open Active directory administrative center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1025151/unable-to-open-active-directory-administrative-cen
question_id: 1025151
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Unable to open Active directory administrative center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1025151/unable-to-open-active-directory-administrative-cen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We experienced an issue with our domain controllers servers when opening the active directory administrative center, I received the below error    

The procedure entry point could not be located in the dynamic link library C:\Windows\system32\dsac.exe    

Windows Server 2019    

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2024-07-10*

Deleting the user config has fixed this for me. 

```
C:\Users\[user]\AppData\Roaming\IsolatedStorage\StrongName.cc1bdxpzcw0hn1lld3fth5uorokeuzbv\AssemFiles\dsac.exe.usersettings.dat
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

From https://learn.microsoft.com/en-us/answers/questions/547502/servermanager-will-not-launch-on-2-2019-servers  

If I copy both EXE files from %windir%\system32 to C:\Temp\

C:\temp\dsac.exe  

C:\temp\ServerManager.exe

I can start both, Server manager and ADAC.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

Hello    

Thank you for your question and reaching out.     

It could some corruption in Windows OS system files.    

-  Disable any Antivirus program or Windows firewall you may have for temporary purpose.    

-  Cleanup below Temp folders     

     C:\Windows\Temp  

     %USERPROFILE%\AppData\Local\Temp  

-  Run below DISM commands  from elevated prompt.    

DISM /Online /Cleanup-Image /CheckHealth    

DISM /Online /Cleanup-Image /ScanHealth    

DISM /Online  /Cleanup-Image /RestoreHealth    

------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-27*

Hi Ahmed,    

Seems like a DLL corruption, does it show DLL details? try to register it again, regsrv32 path to the DLL.    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
