---
title: "The term '-SysvolPath' is not recognized..?!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179551/the-term-sysvolpath-is-not-recognized
question_id: 1179551
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# The term '-SysvolPath' is not recognized..?!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179551/the-term-sysvolpath-is-not-recognized (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have the following Powershell script :

```
$password = ConvertTo-SecureString "Password" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ("Administrator", $password)
Install-WindowsFeature -name AD-Domain-Services -IncludeManagementTools
Import-Module ADDSDeployment
Install-ADDSDomainController `
-NoGlobalCatalog:$false `
-CreateDnsDelegation:$false `
-Credential $cred `
-SafeModeAdministratorPassword $password `
-CriticalReplicationOnly:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainName $domainName `
-InstallDns:$true `
-LogPath "C:\Windows\NTDS" `
-NoRebootOnCompletion:$true `
-SiteName $serverSite `
-SysvolPath "C:\Windows\SYSVOL" `
-Confirm:$false `
-Force:$true
```

Unsure why I'm receiving the error 

```
The term '-SiteName' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
```

If I remove -SiteName then I receive error:

```
The term '-SysvolPath' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
```

Not understanding why the error appears.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-10*

That would seem to indicate that the command continuation is not being recognized on the line above the "not recognized" cmdlet. I haven't been able to find any document that says that there is a limit on the number of line continuations, so maybe you have an unprintable character somewhere. 

Try changing the order of the switches. Move '-SiteName' above the NoRebootOnCompletion line. Keep doing that to see if you can identify the problem line. 

Maybe copy and paste the entire script into notepad and then copy and paste it back into ISE or VScode (or whatever editor you use). If you already use notepad to edit the script, then try editing it with ISE to see if it shows a formatting error.
