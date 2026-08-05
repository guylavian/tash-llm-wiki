---
title: "How to Install SSL Certificate on ADFS Secondary server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/606926/how-to-install-ssl-certificate-on-adfs-secondary-s
question_id: 606926
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How to Install SSL Certificate on ADFS Secondary server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/606926/how-to-install-ssl-certificate-on-adfs-secondary-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI All,

How to install SSL Certificate on ADFS secondary server due to I got teh error below:

Set-AdfsSslCertificate -Thumbprint <xxxxxxxxxxxx>

PS C:\Windows\system32> Set-AdfsSslCertificate -Thumbprint <xxxxxxxxxxxxxxx>  

Set-AdfsSslCertificate : PS0033: This cmdlet cannot be executed from a secondary server in a local database farm. The  

primary server is presently: xxxxx.xxxx.co.id. To execute management cmdlets, either log onto the primary server  

or connect using PowerShell remoting. For more information see https://go.microsoft.com/fwlink/?LinkId=294129.  

At line:1 char:1  

-  Set-AdfsSslCertificate -Thumbprint xxxxxxxxxxxxxxx ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (:) [Set-AdfsSslCertificate], InvalidOperationException  

-  FullyQualifiedErrorId : PS0033,Microsoft.IdentityServer.Management.Commands.SetSslCertificateCommand

Regards,  

Nana Sutisna

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-11-04*

Assuming you are using ADFS on Windows Server 2016 or higher (else let us know), you only need to run the cmdLet from the primary and it uses WinRM on the background to change the certificate binding on all nodes.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-09*

We are using ADFS on Windows Server 2019.   

Before I just run cmdlet " Set-AdfsSslCertificate -Thumbprint <xxxxxxxxxxxxxxx>" on primary server, but the process took a long time and there was an error. Sorry I didn't capture the error.   

I closed teh error and restart ADFS service, then I run "Get-AdfsSslCertificate" , the certificate is available on primary server. But it is not available on secondary server. So I install the certificate on secondary server and run again Set-AdfsSslCertificate -Thumbprint <xxxxxxxxxxxxxxx> on primary server. The problem solved.
