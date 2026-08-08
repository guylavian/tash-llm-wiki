---
title: "Windows Server _ GPO & SMBV1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168020/windows-server-gpo-smbv1
question_id: 168020
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows Server _ GPO & SMBV1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168020/windows-server-gpo-smbv1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have Windows server 2016,Whenever i try to push gpo update in the client machine, it throws error  

C:\Users\Administrator>gpupdate  

Updating policy...  

Computer policy could not be updated successfully. The following errors were encountered:  

The processing of Group Policy failed. Windows attempted to read the file \sb.com\SysVol\sb.com\Policies{8E7CF1BD-C9F9-4B6C-AE32-64293DAA5F55}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following:  

a) Name Resolution/Network Connectivity to the current domain controller.  

b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller).  

c) The Distributed File System (DFS) client has been disabled.  

User Policy could not be updated successfully. The following errors were encountered:  

The processing of Group Policy failed. Windows attempted to read the file \sb.com\SysVol\sb.com\Policies{FE33FBFF-63AF-42B4-840B-286C6F31A7EE}\gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following:  

a) Name Resolution/Network Connectivity to the current domain controller.  

b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller).  

c) The Distributed File System (DFS) client has been disabled.  

To diagnose the failure, review the event log or run GPRESULT /H GPReport.html from the command line to access information about Group Policy results.  

So far i found that disabling the SMBV1 protocol cause this issue.  

Is there any solution to push update after disabling the SMBv1 protocol from Windows 10 client

## Answers

_No answers on this thread._
