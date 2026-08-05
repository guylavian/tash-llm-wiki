---
title: "Exporting GPO setting on Member Servers using  Secedit not Working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/111380/exporting-gpo-setting-on-member-servers-using-sece
question_id: 111380
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Exporting GPO setting on Member Servers using  Secedit not Working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/111380/exporting-gpo-setting-on-member-servers-using-sece (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

OS Windows server 2012 R2 Datacenter  

I want to be able to export some Software Restriction Policies from the Local Security Policy. I am trying this  on  member server  machines.  

The command I am trying to run is:  

In powershell run as  administration   

Cd c:\  

Secedit /export /mergedpolicy /cfg outputdata /quiet  

I open the outputdata  and it has not exported anything... Just this...  

[Unicode]  

Unicode=yes  

[Version]  

signature="$CHICAGO$"  

Revision=1  

[Profile Description]  

Description=Default Security Settings. (Windows Server)   

I am a little stuck now... any help would be appreciated!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-30*

Hi，@Pinkal Ganjawala       

The local group policy settings and security settings can be transferred in a couple of steps:    

-  Security Settings:    

Right click Security Settings in Local Group Policy Editor (Edit Group Policy) and select Export Policy... Save the .inf file and transfer to the machine you wish to use the same settings. On the new machine, open a command prompt and use the secedit command    

secedit /configure /db c:\windows\security\local.sdb /cfg {.\path\to.inf}    

Review any errors that come back, I was dealing with user accounts trying to be set for permissions that did not exist on the new machine.    

-  The rest of Local Group Policy    

Locate the %systemroot%\system32\grouppolicy\ hidden folder and copy the sub folders to the target machine in the same location.    

Open a command prompt and use    

gpupdate /force    

-  The remains    

For the miscellanous I was able to use powershell commands to add or edit registry keys:    

Add:    

New-Item -Path HKCU:\Software -Name hsg –Force    

Edit:    

PS C:> Push-Location    

PS C:> Set-Location HKCU:\Software\hsg    

PS HKCU:\Software\hsg> Set-ItemProperty . newproperty "mynewvalue"    

Hope this information can help you    

Best wishes    

Vicky
