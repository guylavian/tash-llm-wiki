---
title: "Restoring GPO from Backup does not restore it completely ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166099/restoring-gpo-from-backup-does-not-restore-it-comp
question_id: 1166099
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Restoring GPO from Backup does not restore it completely ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166099/restoring-gpo-from-backup-does-not-restore-it-comp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have tested this several times, I make a GPO backup and restore it in a different machine and the backup does not restore the GPO completely. In particular the Network Manager List - Network Name Value is not restored, however, when I check the GPO after restore it shows the value exists in the GPO, upon reboot the value is lost from the restored GPO.

Any idea on how to get this working, or is this a bug ?

Thank You

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hi,

Just so there is clarity in the post. I make the backup with the Backup-GPO command, and restore it the same way as in @Limitless Technology script which is when this problem happens, I'm automating this so I'm using powershell for this, but it does not work as expected.

There is no error when restoring with Powershell.

`$gpoPath = Join-Path -Path $PSScriptRoot -ChildPath "HLABGPO"`

`Import-Module GroupPolicy`

`New-GPO -Name "HLAB"`

`Import-GPO -BackupGpoName "HLAB" -TargetName "HLAB" -Path $gpoPath`

`Get-GPO -Name "HLAB" | New-GPLink -Target "dc=hlab,dc=lab" -LinkEnabled Yes - Enforced Yes`

`gpupdate /force`

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hi,,

Just so there is clarity in the post.

I make the backup with the Backup-GPO command, and restore it the same way as in @Limitless Technology  script which is when this problem happens, I'm automating this so I'm using powershell for this, but it doesn't restore the Network Manager List - Network Name.

So I tried backing up manually and restoring manually, this way works fine.

Unsure whats going on.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hello there,

Do you get any error messages ?

Instead of restoring the GPO, create a new empty GPO then right-click on it and choose import settings. The backup that you exported from SCM will show up here and you can import all the settings to the new GPO.

Also try the below Scritp and see if that helps,

Import-Module GroupPolicy

New-GPO -Name "Homelab"

Import-GPO -BackupGpoName "Homelab" -TargetName "Homelab" -Path C:\

Get-GPO -Name "Homelab" | New-GPLink -Target "dc=homelab,dc=lab" -LinkEnabled Yes -Enforced Yes

https://learn.microsoft.com/en-us/powershell/module/grouppolicy/restore-gpo?view=windowsserver2022-ps

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-01*

Hi,

 When you Open GPMC be sure that you are connecting on your PDC and try to import GPO setting from restored GPO .

If you still have same behavior , run `dcdiag` to check the DC health and sysvol replication.

***Please don't forget to mark helpful answer
