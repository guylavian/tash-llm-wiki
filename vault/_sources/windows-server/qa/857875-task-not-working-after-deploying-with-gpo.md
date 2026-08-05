---
title: "task not working after deploying with gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/857875/task-not-working-after-deploying-with-gpo
question_id: 857875
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# task not working after deploying with gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/857875/task-not-working-after-deploying-with-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon reader,    

I've made a virtual samba ad that runs windows 2008R2 (i couldn't upgrade to 2012R2 even though it's samba 4.15, not the issue right now) and i've authenticated a virtual windows 10 computer agaisn't it.    

I installed the RSAT tools on the virtual windows computer. GPO and Lightweight directory.    

I created some users and a group policies to try things out.    

Everything works well except a task scheduler gpo. When I look at gpresult, the gpo is applied without any issue.    

Here's my gpo :    

    

    

I can also find it in the administrator task scheduler on the client :    

    

What it does : it should start the rasdial.exe executable and, with the vpn connection "Linkso VPN" as argument it should start the vpn at the boot of the machine.    

But nothing happens. I went to the admin task scheduler and executed it manually but it stucks on "ready" and nothing happens.    

The event viewer doesn't notice anything except some past errors about past gpos that don't apply to the machine.    

What i've found so far about this was a user security issue but nothing that really compares to my issue. I'm not that experienced in ldap and i've wanted some tips or leads if possible...    

I feel like i miss the difference between a local and a computer local task scheduler...    

Thanks in advance for any answer, have a fantastic day !

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-20*

I went back to %APPDATA%\Microsoft\Network\Connections\Pbk\  

%APPDATA% points to my user folders.  

```
C:\>set app
APPDATA=C:\Users\Dave\AppData\Roaming
```

If your task is running as the system account, then I'm not sure what folder that will get resolved to. Do you copy the phonebook somewhere? You might have to use the /PHONEBOOK:phonebookfile switch.  

If the task is running at startup, then maybe you need add in a delay to let the network fully initialize before trying to initialize the VPN. Verify that the phonebook exists and contains your entry.   

```
@echo %date% %time% Task starting.
@timeout /t 30 > nul
@echo %date% %time% Finished with startup delay.
@echo.
dir %APPDATA%\Microsoft\Network\Connections\Pbk\
@echo.
@echo.
type %APPDATA%\Microsoft\Network\Connections\Pbk\rasphone.pbk
@echo.
@echo.
@echo %date% %time% Calling rasdial.
C:\Windows\System32\rasdial.exe "Linkso VPN" 
@echo %date% %time% Task ending. Result = %errorlevel%
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-20*

You have to capture the output (stdout/stderr) that rasdial.exe displays in order to know what error it encountered.  

Create a c:\temp\vpn.bat file that calls it.   

```
@echo %date% %time% Task starting.
C:\Windows\System32\rasdial.exe  "Linkso VPN" 
@echo %date% %time% Task ending. Result = %errorlevel%
```

Modify the task to call cmd.exe with this argument.  

```
/c c:\temp\vpn.bat 1>>c:\temp\vpn.log 2>&1
```

Run the task and then review the log.
