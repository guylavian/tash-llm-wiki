---
title: "New two Domain Controllers altering when reporting to WSUS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/744196/new-two-domain-controllers-altering-when-reporting
question_id: 744196
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# New two Domain Controllers altering when reporting to WSUS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/744196/new-two-domain-controllers-altering-when-reporting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team  

Please advise on my dilemma here  

I have just recently promoted two Domain Controllers, and they were reporting well to WSUS server for two days  

From day three, now those servers are not reporting at the same time but they alternate (today DC05 , then following day DC06)  

As part of my troubleshooting, i created a separate Computer group and move xxDC06 to that group as it was the one appearing.  

The following day on the separate computer group, the DC was showing now as xxDC05.  

I remove the computer again and check the GUID if not conflicting and found they differ.  

Please help on what might cause the computers to report only one at the time not all of them  

Regards, Shakoane

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-22*

Hello Shakoane,  

Thanks for your posting on Q&A.  

It seems that the issue is due to the duplicate SusClientId. Please open the CMD as an administrator and run the below commands one by one to delete the SusClientId. Then we could check whether the issue will be resolved or not.  

```
net stop wuauserv

del /S /Q C:\Windows\SoftwareDistribution\*.*
RMDIR /S /Q C:\Windows\SoftwareDistribution\ 

reg.exe delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate /v PingID /f
reg.exe delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate /v AccountDomainSid /f
reg.exe delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate /v SusClientId /f
reg.exe delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate /v SusClientIDValidation /f

net start wuauserv
```

Then we could force the two Servers check for updates manually. Please wait for a while and the two servers should report to the WSUS server.  

In addition, please run the Server Cleanup Wizard to clean up if you haven't maintenance the WSUS server for a long time.  

Please keep us in touch if there are any updates of the case. Looking forward for your updates.  

Have a great day.  

Regards,  

Rita  

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
