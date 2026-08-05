---
title: "[Migrated from MSDN Exchange Dev]Intermittingly failing New-Pssession to Exchange Online https://outlook.office365.com/powershell-liveid/"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/161823/migrated-from-msdn-exchange-dev-intermittingly-fai
question_id: 161823
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# [Migrated from MSDN Exchange Dev]Intermittingly failing New-Pssession to Exchange Online https://outlook.office365.com/powershell-liveid/

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/161823/migrated-from-msdn-exchange-dev-intermittingly-fai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hi, I have a script written for to set mailbox quotas on ExchangeOnline. I am validating licenses and service plan in O365 License assigned to User before setting Mailbox quotas.  

But while establishing a PSsession with "https://outlook.office365.com/powershell-liveid/".  It fails 6/10 times with this error.  

[New-PSSession|2613] Failed to connect to exchange online. |Reason: Connecting to remote server outlook.office365.com failed with the following error message : The SSL connection cannot be established. Verify that the service on the remote host is properly configured to listen for HTTPS requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig -transport:https". For more information, see the about_Remote_Troubleshooting Help topic.  

Any help would be appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-18*

We had a similar issue with connections to Office365 periodically failing with the same error.  

Turns out the issue wasn't with Windows Remote Management (WinRM) but another process limiting what security protocols could be used, which was stopping the powershell session (`New-PSSession`) for https://outlook.office365.com/powershell-liveid/ from being established. Resolved by adding TLS 1.2 prior to the session being created, i.e.;  

[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12  

$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $yourCredentials -Authentication Basic -AllowRedirection  

Import-PSSession $Session -DisableNameChecking -AllowClobber

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

Hi,    

Does this problem only occur occasionally?    

What is the command line you are running, please make sure you run the correct command line.    

What’s the version of your Windows server？For the old version of Windows, you need to install the Microsoft .NET Framework 4.5 or later and then an updated version of the Windows Management Framework: 3.0 or 4.0 or 5.1 .    

Please run the "winrm quickconfig -transport:https" in CMD start as administrator and see how it turns out. WinRM HTTPS requires a local computer Server Authentication certificate with a CN matching the hostname, that is not expired, revoked, or self-signed to be installed.    

For more information you could refer to: How to configure WINRM for HTTPS    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
