---
title: "KDC / Kerberos Eventlog Provider not registered - fails to find 2022-11 related entries"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1091704/kdc-kerberos-eventlog-provider-not-registered-fail
question_id: 1091704
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# KDC / Kerberos Eventlog Provider not registered - fails to find 2022-11 related entries

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1091704/kdc-kerberos-eventlog-provider-not-registered-fail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

According to the description for the issues with the 2022-11 Updates "Sign in failures and other issues related to Kerberos authentication" on https://learn.microsoft.com/en-us/windows/release-health/status-windows-10-1607-and-windows-server-2016#2953msgdesc : "When this issue is encountered you might receive a Microsoft-Windows-Kerberos-Key-Distribution-Center Event ID 14 error event in the System section of Event Log on your Domain Controller with the below text."

Searching Domain Controller System Eventlog for this event with Powershell fails with the error messages "The specified providers do not write events to any of the specified logs." and "The parameter is incorrect"

--  

Get-WinEvent -ComputerName 'dc.contoso.com' -FilterHashtable @{ LogName = 'System'; ProviderName = 'Microsoft-Windows-Kerberos-Key-Distribution-Center'; Id = 14 }

Get-WinEvent : The specified providers do not write events to any of the specified logs.  

At line:1 char:1  

-  Get-WinEvent -ComputerName 'dc.contoso.com' -FilterHashtable @{ LogN ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : InvalidArgument: (:) [Get-WinEvent], Exception  

-  FullyQualifiedErrorId : LogsAndProvidersDontOverlap,Microsoft.PowerShell.Commands.GetWinEventCommand

Get-WinEvent : The parameter is incorrect  

At line:1 char:1  

-  Get-WinEvent -ComputerName 'dc.contoso.com' -FilterHashtable @{ LogN ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : NotSpecified: (:) [Get-WinEvent], EventLogException  

-  FullyQualifiedErrorId : System.Diagnostics.Eventing.Reader.EventLogException,Microsoft.PowerShell.Commands.GetWinEventCommand  

--

## Answers

_No answers on this thread._
