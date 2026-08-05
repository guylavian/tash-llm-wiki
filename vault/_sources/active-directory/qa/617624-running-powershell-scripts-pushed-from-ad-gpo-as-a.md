---
title: "Running Powershell scripts pushed from AD GPO as admin on domain computers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/617624/running-powershell-scripts-pushed-from-ad-gpo-as-a
question_id: 617624
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Running Powershell scripts pushed from AD GPO as admin on domain computers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/617624/running-powershell-scripts-pushed-from-ad-gpo-as-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

Needed some help getting a simple task done at work.  

I have about 30 machines in my work domain that i want to run a power-shell script on at startup.  

I have created a GPO that runs the script on all machines at startup and all machines have the GPO applied successfully.  

The power-shell script is supposed to lookup a service on the machine and if it finds it, it starts it up and that's it. If the service does not exist, the script continues running and copies a file stored on a shared folder in the domain into the machine and then creates the service then starts it up.  

MY PROBLEM: the script does not run automatically on all machines.  

After some troubleshooting i found out that running scripts on the machines with the domain user logged in is not allowed and when i try to run the script manually on each machine i get an error that says running scripts is disabled, so i created a GPO that enables running scripts on the machines by enabling the Turn on Script Execution Policy. Regardless the script did not do it's job after restarting the machines and i still get the same error when i try manually.  

Then i tried to run the script manually as admin on the machines and the script performed it's work perfectly.  

Also tried adding the following two commands -based on suggestions from other people having similar problems- in the beginning of the power-shell script, the first to elevate the script to run as admin and the second to allow running scripts on the machine and it did not make any change.  

COMMAND #1: start-process powershell –verb runAs  

COMMAND #2: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  

Currently the number of device is going to get close to 200 and i need to get this script to run as admin on all machines from the applied GPO. Waiting to read some solutions from you shortly  

Thanks in advance.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-09*

You could also not use PowerShell :) What about a good old bat file?  

```
sc query MySvc
if %ERRORLEVEL% GTR 0 (
 copy \\server\share\file.exe c:\folder\file.exe
 sc create MySvc binpath= c:\folder\file.exe start= auto
)
```

MySvc is the service to check the existance of. \server\share\file.exe is where the binary is (assuming that's what you want from the share, else you can adjust) and then you create the service...
