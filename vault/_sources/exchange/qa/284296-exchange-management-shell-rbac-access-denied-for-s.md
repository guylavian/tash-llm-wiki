---
title: "Exchange Management Shell RBAC Access Denied for Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/284296/exchange-management-shell-rbac-access-denied-for-s
question_id: 284296
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Management Shell RBAC Access Denied for Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/284296/exchange-management-shell-rbac-access-denied-for-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

On a 2019 Exchange server I have issues running the Management Shell, as it is started it throws an error related to RBAC:  

[AuthZRequestId=8a7b453d-47e2-468d-8f62-ffdd36a728dc][FailureCategory=AuthZ-CmdletAccessDeniedException] The user  

"<domain name>/SERVERS/<ExchangeServerName>" isn't assigned to any management roles.  

followed by the message:  

Failed to connect to an Exchange server in the current site.  

Enter the server FQDN where you want to connect.:  

When I start a standard Powershell session and load the Exchange plugin, this works, and I can execute Exchange commands:  

Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn  

I also see repeated combinations of errors 17, 23 and 258 in the event viewer, all related to RBAC, about once every minute:  

Error 17:  

[AuthZRequestId=8a7b453d-47e2-468d-8f62-ffdd36a728dc][FailureCategory=AuthZ-CmdletAccessDeniedException] The user  

"<domain name>/SERVERS/<ExchangeServerName>" isn't assigned to any management roles.  

Error 23:  

(Process w3wp.exe, PID 30316) "Exchange AuthZPlugin Fails to finish method GetApplicationPrivateData due to application exception Microsoft.Exchange.Configuration.Authorization.CmdletAccessDeniedException: The user "<domain name>/SERVERS/<ExchangeServerName>" isn't assigned to any management roles.  

Error 258:  

(Process 30316, PID w3wp.exe)"RemotePS Public API Func GetApplicationPrivateData throws Exception Microsoft.Exchange.Configuration.Authorization.CmdletAccessDeniedException: The user "<domain name>/SERVERS/<ExchangeServerName>" isn't assigned to any management roles.  

I have tried many things but none seem to help. The addition of the Exchange server name to the Exchange Organization Management group appeared to work, as Powershell could be started without errors, but other functions were impacted in this situation, so this was clearly not a solution. Example: room reservations were no longer possible.  

Exchange Server 2019 on top of Windows Server 2019, latest updates installed.  

Other than Exchange, the server has ESET Mail Security installed and running, as well as CodeTwo Exchange Rules 2019 for signature management, latest release.  

Any tips very welcome.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-24*

Hi KaelYao-MSFT,  

Thanks for the reply, no need to apologize for asking questions.  

The system was installed very recently, in December of last year, but I can't recall when we first detected this. All Exchange functionality works well, including Outlook, OWA and EAC.  As this was part of a larger migration, we decided to leave it aside and focus our efforts on the other parts of the installation.  

Continuing with a server that doesn't do all that is expected of it is undesirable, and as the migration activities have subsided, I am now trying to resolve this issue. Additionally, we need to link Exchange to 365 in a hybrid scenario, which is clearly impossible in the current situation.  

I have tried to find the exact information related to this particular problem, by scouring the different websites, but very little is to be found about this particular problem; of those found none have provided a solution. So in essence I haven't been able to try much.   

What I did try:  

-  Uninstall ESET Mail Security antivirus  

-  Disabled the CodeTwo email signature services  

-  Checked Task Scheduler for any tasks that had failed  

-  Checked Event Viewer for other errors or failures  

-  Applied all updates to the operating system and Exchange server, save for the last, U8, but the release notes do not appear to provide a fix.  

-  Checked the installation logs of Exchange  

The event viewer and installation log files contain quite a number of errors, so I am suspecting this problem was introduced during the installation. To further analyze the errors and potential installation issues, I am currently building a new server alongside the existing, and try to perform a fresh installation of Exchange. If this system works well and the errors do not show, I could migrate the mailboxes over and decommission the original Exchange server.  

What do you think?  

Thanks for your help.  

Jaap

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-24*

Hi, @Jaap Hoetmer       

Sorry I need to ask a few questions:    

-  What changes have you done before the problem occurs?     

-  What solutions have you tried so far?    

-  Do EAC and OWA work correctly?    

The addition of the Exchange server name to the Exchange Organization Management group appeared to work, as Powershell could be started without errors, but other functions were impacted in this situation, so this was clearly not a solution.    

Yes the server should not be added to the Exchange Organization Management group as mentioned in this document: Error occurs in EMS, EAC, ECP, OWA, or Outlook on the web in Exchange Server 2013 or Exchange Server 2016    

    

It should only be in these groups:    

Domain Computers    

Exchange Install Domain Servers    

Exchange Servers    

Exchange Trusted Subsystem    

Managed Availability Servers    

I notice that you mentioned the server has ESET Mail Security and CodeTwo Exchange Rules 2019 installed.    

To my knowledge, third-party software may be the possible cause of the problem.    

If possible please uninstall the software and check if EMS will work.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
