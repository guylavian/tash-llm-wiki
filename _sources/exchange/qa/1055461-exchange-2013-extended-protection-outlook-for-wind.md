---
title: "Exchange 2013, Extended Protection, Outlook for Windows can no longer connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1055461/exchange-2013-extended-protection-outlook-for-wind
question_id: 1055461
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013, Extended Protection, Outlook for Windows can no longer connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1055461/exchange-2013-extended-protection-outlook-for-wind (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

-  On-prem Exchange 2013 CU23 + all patches, on Server 2012 R2. Bare-metal server is the AD PDC as well as hosting Exchange    

-  Local Windows domain is company.local, Exchange server hostname is server.company.local    

-  Mail domain is company.com. External DNS MX record points to mail.company.com.    

-  The server has a trusted 3rd-party cert for mail.company.com. There are also 2 self-signed certs for server.company.local    

-  Internal and public DNS are (I believe) configured properly. Both server.company.local and mail.company.com resolve properly from either outside or inside the LAN and are appropriately reachable    

Previously, Outlook for Windows clients (M365) worked fine. Exchange mailboxes were set up while srv.company.local was resolvable (either on LAN or connected via VPN). The only nagging issue is that every time Outlook starts, one or two certificate errors came up because the trusted 3rd-party cert (mail.company.com) didn't match the (presumed) server name under which the Outlook account was set up (srv.company.local). The users could bypass the warning (i.e. proceed anyways) and Outlook worked as expected.    

After configuring Extended Protection by running the script (ExchangeExtendedProtectionManagement.ps1), Outlook for Windows clients can no longer connect. They get a message:    

“There is a problem with the proxy server’s security certificate. The name on the security certificate is invalid or does not match the name of the target site srv.company.local. Outlook is unable to connect to the proxy server. (Error code 10)”    

Users can no longer bypass this error message and they can't connect.    

While installing EP I had to deal with some prerequisite failures:    

-  TLS configuration had some items not configured as expected. I explicitly enabled TLS 1.2, 1.1 and 1.0 per https://learn.microsoft.com/en-us/Exchange/exchange-tls-configuration?view=exchserver-2019    

-  SSL Offloading was apparently set to True (I have no idea why, maybe default for Exchange 2013?). I ran this cmdlet to turn it off: Set-OutlookAnywhere 'SRV\RPC (Default Web Site)' -SSLOffloading $false -InternalClientsRequireSsl $true -ExternalClientsRequireSsl $true    

After that the EP update script passed prerequisites and reported a successful installation. Outlook for Windows can't connect, Outlook for Mac works fine, most smartphones work fine.    

I rolled back the EP update by running ExchangeExtendedProtectionManagement.ps1 -RollbackType "RestoreIISAppConfig" and restarting the server, but Outlook for Windows still can't connect.    

I think what might be happening:    

-  The SSL offloading cmdlet may now force clients to connect with SSL so the Windows clients can't bypass the warning any longer    

-  The ultimate root cause is probably the technical debt of originally setting up AD and Exchange using company.local and srv.company.local    

Outlook for Windows apparently uses AutoDiscover (and RPC over HTTP). The online connectivity tester https://testconnectivity.microsoft.com/ shows that the AutoDiscover URL is properly found, and it shows the AutoDiscover.xml result that's being returned. The XML has the string "srv.company.local" in 5 places. My guess is the most important location for this discussion is:    

X-CalculatedBETarget: srv.company.local    

I think what I ultimately want to do is somehow get the XML to return "mail.company.com" at least for X-CalculatedBETarget, and anywhere else it makes sense.    

I recognize this may not help with existing Outlook profiles that were originally created pointing to srv.company.local but it's not the end of the world if users need to delete their profiles and re-establish them. My thinking is this would get mail.company.com from AutoDiscover, and when connecting the server certs would work for that server name and the Outlook errors would no longer happen.    

As a fallback I might experiment with the SSL offloading, setting external and internal clients to $false which might allow Outlook for Windows users to bypass the warnings as they did previously.    

Thanks very much to everyone who made it through all of this, and thanks in advance for insights anyone may have.

## Answers

_No answers on this thread._
