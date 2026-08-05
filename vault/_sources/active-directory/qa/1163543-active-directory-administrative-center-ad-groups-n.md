---
title: "Active Directory Administrative Center - AD groups not opening"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163543/active-directory-administrative-center-ad-groups-n
question_id: 1163543
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Active Directory Administrative Center - AD groups not opening

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163543/active-directory-administrative-center-ad-groups-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all! I have an issue where I am unable to open groups via Active Directory Administrative Center on a Windows Server machine, no error but just hangs instead, no window opens visibly but does show a dead window when you hover over its icon in the taskbar. Doesn't affect all users, and attempted restart as well as a repair using software center.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

```
Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to unable to open groups via Active Directory Administrative Center.

First of please reboot your Computer and check if the issue resolved automatically.
If still issue persists follow below steps which should help you to resolve the issue.

1. Disable any Antivirus program or Windows firewall you may have for temporary purpose.

2. Cleanup below Temp folders location -> Open Start -> Run -> Type below location one-by-one and press enter 
     C:\Windows\Temp
     %USERPROFILE%\AppData\Local\Temp

3. Run Disk Cleanup from Select C:\ Drive from Properties- > General -> Disk Cleanup - >Cleanup system files

4. Run sfc /scannow from elevated prompt.

5.  Run below DISM commands  from elevated prompt.

DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online  /Cleanup-Image /RestoreHealth

6. Try to open   Administrative Center from different user on this server.

--If the reply is helpful, please Upvote and Accept as answer--
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-24*

Hi,

You can use dsa.msc console instead of Administrative Center to open group properties.

Please don't forget to mark helpful answer as accepted
