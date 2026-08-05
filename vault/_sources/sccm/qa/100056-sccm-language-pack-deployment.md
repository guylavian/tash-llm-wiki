---
title: "SCCM Language Pack Deployment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/100056/sccm-language-pack-deployment
question_id: 100056
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-deployment"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM Language Pack Deployment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/100056/sccm-language-pack-deployment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently building Windows Server(s) 2019 via SCCM Task Sequence and everything is great my issue is integrating the en-Gb language pack.  

I have a task that injects the language pack after the operating system deployment but I get an error code of 2, which indicates that the file is not found.  

I'm using DISM in image mode to deploy the language pack and this is my syntax  

dism.exe /Image:"%OSDTargetSystemDrive%" /ScratchDir:%OSDTargetSystemDrive%\Windows\Temp /Add-Package /PackagePath:".\Microsoft-Windows-Server-Language-Pack_x64_en-gb.cab"  

I've also tried  

dism.exe /Image:"%OSDTargetSystemDrive%" /ScratchDir:%OSDTargetSystemDrive%\Windows\Temp /Add-Package /PackagePath:"Microsoft-Windows-Server-Language-Pack_x64_en-gb.cab"  

Both are failing, is their anything I'm missing?

## Answer (community) — community member

*upvotes: 2 · updated: 2020-09-22*

I fixed the issue. It was a syntax error in the command  

The correct command is as follows:  DISM.exe /image:%OSDTargetSystemDrive%\ /ScratchDir:%OSDTargetSystemDrive%\windows\TEMP /Add-Package /PackagePath:Microsoft-Windows-Server-Language-Pack_x64_en-gb.cab

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-22*

Any update on this????

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-21*

Hi,

Thank you for coming Microsoft MECM Q&A forum.

1.May we know what version of SCCM you are using? Please help examine the smsts.log on the target system to see if there is any further information, refer to:  

SCCM: How to copy SMSTS.log when a Task Sequence fails

2.We can try to deploy the en-Gb language pack as an application, refer to:  

How to deploy a Windows language pack as an application in Configuration Manager

3.For more detailed steps about using task sequence to deploy language pack, refer to:  

Language Packs, Language Experience Packs, Language Interface Packs  

Windows 10 – SCCM Language Pack Integration

Thanks for your time.

Best regards,  

Simon  

If the response is helpful, please click "Accept Answer" and upvote it.
