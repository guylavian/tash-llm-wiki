---
title: "[Migrated from MSDN Exchange Dev] Having issues adding server to hybrid mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/191552/migrated-from-msdn-exchange-dev-having-issues-addi
question_id: 191552
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# [Migrated from MSDN Exchange Dev] Having issues adding server to hybrid mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/191552/migrated-from-msdn-exchange-dev-having-issues-addi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/9ff03b6b-3646-4798-9fbe-c07ef0ffb3da/having-issues-adding-server-to-hybrid-mode?forum=exchangesvrdevelopment   

Hello,  

Currently running into an issue when attempting to place my Exchange server in hybrid mode.  

Connecting to remote server failed with the following error message: Connecting to remote server failed with the following error message : The SSL connection cannot be established. Verify that the service on the remote host is properly configured to listen for HTTPS requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig -transport:https". For more information, see the about_Remote_Troubleshooting Help topic.  

I have tried the winrm command but still getting the same issue.  I also tried connecting via powershell and receive the same error.  

Am I missing a step?  

I was running this on Windows Server 2008 R2 SP1 running Exchange 2013 CU23.  

On a side note, I tried upgrading WMF from 3.0 to 5.1  Now i get an issue where opening Powershell crashes with the error message  

Application: powershell.exe  

Framework Version: v4.0.30319  

Description: The application requested process termination through System.Environment.FailFast(string message).  

Message: Access to the path 'C:\Users(username)\AppData\Local\Temp\2\sagbztm4.xiu.ps1' is denied.  

Any help would definitely be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-09*

Enabling TLS 1.0 and 1.1 did help fix this issue.  While putting this in hybrid is temporary while we migrate over to 365, is there a way to have this done over TLS 1.2 or should i just use TLS 1.0/1.1 for the short period of time?  

I did try running this command:  

[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12;  

but it didn't seem to work.  Either way, it seems I am good to go.  Thanks again for your guys help.  Truly appreciate it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-09*

Hi,    

For the HCW error, could you please check the below,    

-  Are you using the valid public certificate for Hybrid?    

-  Are you able to browse portal.office365.com    

-  Please allow the required network communication between the Exchange server and Office365    

-  Check the TLS protocols in Windows server using registry - this require installation of patch and enable it using registry. Reboot is required after enabling TLS     

https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide    

https://support.microsoft.com/en-us/help/4019276/update-to-add-support-for-tls-1-1-and-tls-1-2-in-windows    

If the above suggestion helps, please click on Accept Answer and upvote it.
