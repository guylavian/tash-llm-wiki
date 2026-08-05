---
title: "How to deploy printer in a GPO via powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/845545/how-to-deploy-printer-in-a-gpo-via-powershell
question_id: 845545
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-print-jobs"]
answer_author_roles: ["Q&A User"]
---
# How to deploy printer in a GPO via powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/845545/how-to-deploy-printer-in-a-gpo-via-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'd like to add printers into a GPO via powershell because eventually I need to add 50-100 printers.    

This is the process.    

    

Then, I need to add printers inside "Control Panel Settings"    

    

So, I created the first part of the script:    

Set-GPPrefRegistryValue -Name "GPO Name" -Context Computer -Key "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Ports" -ValueName "\PrintServer\Printer" -Value "" -Type String -Action Create    

With this command, I changed the manual proccess in the dialog box    

    

I don't need to do it anymore, but the second part, I still have to...    

    

If I can do it via powershell like the first proccess, I would do it much faster...    

May someone help me... I searched on the Microsoft Learn and only found commands to add registries... I don't know how to add local printers via powershell...

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-16*

Hello ClaudianorJunior,    

I think you have half of it.  The Printer GPO will not allow you to run a Powershell script. The best way to deploy Powershell script for printer deployment would be as a Logon Script. You can create different scripts with the different Printers to be assigned, and then link the specific policy (for Example "Printer001") to the right OU (for example "Users that need the Printer001"). This way, every time the user logs in, you ensure that the printer is reloaded.     

There is a very good official article from Microsoft that explains how to configure them: https://devblogs.microsoft.com/scripting/using-group-policy-to-deploy-a-windows-powershell-logon-script/    

If you are also interested in the GUI process for GPO, but starting from Print Server role, please check the next:    

Steps to deploy Printers Using a Group Policy:    

Click Start, point to "Administrative Tools" and then click "Print Management."    

Expand "Print Servers" from the left pane and then select the print server from the list.    

Click "Printers." Right-click the target device and then select "Deploy With Group Policy."    

Click "Browse" and then select the GPO to associate with the printer.    

Select "The Users That This GPO Applies to (Per User)" to enable a group of users to access the printer; select "The Users That This GPO Applies to (Per Machine)" to enable a set of computers to access the printer.    

Click "Add," then "OK" to deploy the printers to the GPO.    

Reference:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/printing/use-group-policy-to-control-ad-printer    

-----------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-12*

@Anonymous       

The PowerShell command    

add-printer    

You will need to start the process by adding the print driver but in order to use the PowerShell command     

add-printerdriver the driver must first exist in the Windows Driverstore so it's generally easier to use the prndrvr.vbs file to get the driver installed.   You can also use the Group Policy Preferences Printers trick to install a driver but I don't recommend it.     

You will also need to use the PowerShell command     

add-printerport    

To add the Standard TCP/IP port to the device.    

The PowerShell command     

get-help print    

Is your friend.     

I've installed over 500000 printers using PowerShell.  Let me know if you get stuck.    

Thanks
