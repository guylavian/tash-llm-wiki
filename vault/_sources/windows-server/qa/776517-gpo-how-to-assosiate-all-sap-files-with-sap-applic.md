---
title: "GPO how to assosiate all .SAP files with SAP application using GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/776517/gpo-how-to-assosiate-all-sap-files-with-sap-applic
question_id: 776517
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-sap", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# GPO how to assosiate all .SAP files with SAP application using GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/776517/gpo-how-to-assosiate-all-sap-files-with-sap-applic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI,  

How to set all files with sap extension to be always open by SAP using GPO?

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2022-03-17*

Hi,  

You can use Group Policy Preference to set file extension ans specify associated program :  

```
Computer Configuration > Preferences > Control Panel Settings > Folder Options.
```

Please don't forget to mark helpful reply as answer

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-21*

Hello @Anonymous       

Windows 10 introduced the settings for default application as XML files. You can export you current file association and edit or add if needed, then deploy using GPO to a group of computers:    

Extract current XML file    

Dism.exe /online /Export-DefaultAppAssociations:C:\PS\DefaultAssoc.xml    

Import XML file association file    

Dism.exe /Online /Import-DefaultAppAssociations:C:\PS\DefaultAssoc.xml    

GPO settings:    

Path: Computer Configuration\Policies\Administrative Templates\Windows Components\File Explorer    

Policy: DefaultAssociationsConfiguration    

Status: Enabled    

Value: UNC path to DefaultAssoc.xml in shared storage     

Hope this helps with your query,    

------    

--If the reply is helpful, please Upvote and Accept as answer--
