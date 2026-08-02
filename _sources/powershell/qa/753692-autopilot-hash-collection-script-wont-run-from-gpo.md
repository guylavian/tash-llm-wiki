---
title: "Autopilot Hash Collection Script Won't Run From GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/753692/autopilot-hash-collection-script-wont-run-from-gpo
question_id: 753692
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-windows-autopilot", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Autopilot Hash Collection Script Won't Run From GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/753692/autopilot-hash-collection-script-wont-run-from-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am attempting to run the get-windowsautopilotinfo script on Windows 10 domain devices in our network using Group Policy and PowerShell. The script as written (see below) should capture the hardware hash and then write it to a network location specified in the script.

If I run the script manually, it captures the hash and writes it to the target folder as expected. I also see the script run in the PowerShell logs on the device. So I know the actions should be logged with the current logging settings.

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force  

Install-Script -Name Get-WindowsAutoPilotInfo -Scope CurrentUser -Force  

Get-WindowsAutoPilotInfo -OutputFile "\Server-Name\Fileshare\Intune Script\Output\$env:computername-AutoPilotHWID.csv"

I've built a startup script policy and loaded the script into the GPO. I can see the GPO run both at login and after a gpupdate, in gpresult /h as well as in the event viewer. But nothing ever appears in the destination directory and the script events never appear in the PowerShell logs.

I have confirmed that SYSTEM has inherited full control permissions and Domain Computers has read, traverse, and read and execute permissions on the GPO's Machine\Scripts\Startup directory. So there shouldn't be any permissions issues. This is the only script in this GPO and the only script assigned the the OU it's running in (excepting the inherited GPOs like the domain default). There are no inherited GPOs that run scripts on this OU.

Does anyone have any idea why the script doesn't even appear to be starting, despite the policy running successfully?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-28*

The local system account acts as an anonymous account on the network (i.e., it present anonymous credentials). Do you allow anonymous users access to the "fileshare\intune" share on the machine "Server-Name"?  

One way to allow access is to create a domain group and populate the membership with the domain computer names you want to be allowed to write to the share. Then give the group permission on the share.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-28*

If the script is running as SYSTEM, then you need to grant access to Domain Computers on \Server-Name\Fileshare. Both the share permissions and the NTFS folder permissions. ("System" will authenticate as DomainName\ComputerName$)    

Add a transcript to the script to capture it's activity.     

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript?view=powershell-5.1    

```
Start-Transcript -Path C:\windows\temp\Myscript.log  
Install-Script -Name Get-WindowsAutoPilotInfo -Scope CurrentUser -Force  
Get-WindowsAutoPilotInfo -OutputFile "\\Server-Name\Fileshare\Intune Script\Output\$env:computername-AutoPilotHWID.csv"  
Stop-Transcript
```
