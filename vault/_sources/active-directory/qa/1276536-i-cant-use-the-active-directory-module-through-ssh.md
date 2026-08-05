---
title: "I can't use the active directory module through ssh"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1276536/i-cant-use-the-active-directory-module-through-ssh
question_id: 1276536
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
---
# I can't use the active directory module through ssh

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1276536/i-cant-use-the-active-directory-module-through-ssh (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I can use active directory module on my windows 11  computer to get group members. This command gives me the email of all members of a given group Staff

```
(Get-ADGroupMember -Identity "Staff" | Get-ADUser).UserPrincipalName
```

I have activate the ssh server in the windows11 computer and set up powershell 7 as ssh shell connection

Now executing this command from may a Linux computer I get an error

```
$ ssh -i id_ecdsa.win.key user@my.windows11.computer '(Get-ADGroupMember -Identity "Staff" | Get-ADUser).UserPrincipalName'
Get-ADGroupMember: Impossible de contacter le serveur. Il se peut que le serveur n'existe pas, est actuellement hors service ou ne dispose pas des services Web Active Directory.
```

In more details and importing the activedirectory module before get command

```
$ ssh -i id_ecdsa.win.key user@my.windows11.computer 'Import-Module activedirectory -verbose; Get-ADGroupMember -Identity "Staff" -verbose'
VERBOSE: Loading module from path 'C:\windows\system32\WindowsPowerShell\v1.0\Modules\activedirectory\activedirectory.psd1'.
VERBOSE: Loading 'Assembly' from path 'C:\windows\system32\WindowsPowerShell\v1.0\Modules\activedirectory\Microsoft.ActiveDirectory.Management.dll'.
VERBOSE: Loading 'TypesToProcess' from path 'C:\windows\system32\WindowsPowerShell\v1.0\Modules\activedirectory\ActiveDirectory.Types.ps1xml'.
VERBOSE: Loading 'FormatsToProcess' from path 'C:\windows\system32\WindowsPowerShell\v1.0\Modules\activedirectory\ActiveDirectory.Format.ps1xml'.
VERBOSE: Loading module from path 'C:\windows\Microsoft.NET\assembly\GAC_64\Microsoft.ActiveDirectory.Management\v4.0_10.0.0.0__31bf3856ad364e35\Microsoft.ActiveDirectory.Management.dll'.
**WARNING: Erreur d'initialisation du lecteur par défaut�: ��Impossible de contacter le serveur. Il se peut que le serveur n'existe pas, est actuellement hors service ou ne dispose pas des services Web Active Directory.**
VERBOSE: Importing cmdlet 'Get-ADRootDSE'.
VERBOSE: Importing cmdlet 'New-ADObject'.
VERBOSE: Importing cmdlet 'Rename-ADObject'.
....
....
VERBOSE: Importing cmdlet 'Uninstall-ADServiceAccount'.
VERBOSE: Importing cmdlet 'Unlock-ADAccount'.
Get-ADGroupMember: Impossible de contacter le serveur. Il se peut que le serveur n'existe pas, est actuellement hors service ou ne dispose pas des services Web Active Directory.
```

Powershell version in windows 11 computer

```
$ ssh -i id_ecdsa.win.key user@my.windows11.computer '$PSVersionTable'
Name                           Value
----                           -----
PSVersion                      7.3.4
PSEdition                      Core
GitCommitId                    7.3.4
OS                             Microsoft Windows 10.0.22000
Platform                       Win32NT
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0.}
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
WSManStackVersion              3.0
```

how can execute AD cmdlets from a Linux computer?

Thanks

Juan

## Answers

_No answers on this thread._
