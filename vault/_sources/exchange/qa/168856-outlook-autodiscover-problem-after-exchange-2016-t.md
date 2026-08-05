---
title: "Outlook(autodiscover) problem after Exchange 2016 to Exchange 2019 migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168856/outlook-autodiscover-problem-after-exchange-2016-t
question_id: 168856
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Outlook(autodiscover) problem after Exchange 2016 to Exchange 2019 migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168856/outlook-autodiscover-problem-after-exchange-2016-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have migrated exchange 2016 to 2019. Moved all mailboxes (arbitration, public folder, etc. everything). We dismounted all the databases and now shut down the 2016 server. Unfortunately outlook is trying to connect with the old server. If I do a connectivity test on outlook sometime mapi is showing new server url and sometime old server url. The problem is the same with connection status in outlook, sometime showing new server url and sometime old server url.  

Thanks in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-19*

Every details are below.  

owa.mydomain.com -> XCH19 (exists both private DNS and public DNS)  

autodiscover.mydomain.com -> XCH19 (exists both private DNS and public DNS)  

oldowa.mydomain.com -> EXCH16 (only exists in internal DNS, just using this instead of exch16.internal.local because of the certificate)  

External connections:  

HTTPS: Internet - (NAT) - XCH19  

SMTP: Internet - (NAT) - Spam filter - XCH19  

EXCH16 not accessible from internet.  

Internal connections:  

There is no loadbalancer or anything else in front of Exchange servers. Clients connecting directly.  

EXCH16 URLs:  

Server      : EXCH16  

Name        : Microsoft-Server-ActiveSync (Default Web Site)  

InternalUrl : https://oldowa.mydomain.com/Microsoft-Server-ActiveSync  

ExternalUrl :   

Server      : EXCH16  

Name        : Autodiscover (Default Web Site)  

InternalUrl :   

ExternalUrl :   

Server      : EXCH16  

Name        : ecp (Default Web Site)  

InternalUrl : https://oldowa.mydomain.com/ecp  

ExternalUrl :   

Server      : EXCH16  

Name        : mapi (Default Web Site)  

InternalUrl : https://oldowa.mydomain.com/mapi  

ExternalUrl :   

Server      : EXCH16  

Name        : OAB (Default Web Site)  

InternalUrl : https://oldowa.mydomain.com/OAB  

ExternalUrl :   

Server      : EXCH16  

Name        : owa (Default Web Site)  

InternalUrl : https://oldowa.mydomain.com/owa  

ExternalUrl :   

Server      : EXCH16  

Name        : PowerShell (Default Web Site)  

InternalUrl : http://exch16.internal.local/powershell  

ExternalUrl :   

Server      : EXCH16  

Name        : EWS (Default Web Site)  

InternalUrl : https://oldowa.mydomain.com/EWS/Exchange.asmx  

ExternalUrl :   

Name                           : EXCH16  

AutoDiscoverServiceInternalUri :   

Server                             : EXCH16  

ExternalHostname                   :   

InternalHostname                   : oldowa.mydomain.com  

ExternalClientsRequireSsl          : False  

InternalClientsRequireSsl          : True  

ExternalClientAuthenticationMethod : Ntlm  

InternalClientAuthenticationMethod : Ntlm  

XCH19 URLs:  

Server      : XCH19  

Name        : Microsoft-Server-ActiveSync (Default Web Site)  

InternalUrl : https://owa.mydomain.com/Microsoft-Server-ActiveSync  

ExternalUrl : https://owa.mydomain.com/Microsoft-Server-ActiveSync  

Server      : XCH19  

Name        : Autodiscover (Default Web Site)  

InternalUrl : https://autodiscover.mydomain.com/Autodiscover/Autodiscover.xml  

ExternalUrl : https://autodiscover.mydomain.com/Autodiscover/Autodiscover.xml  

Server      : XCH19  

Name        : ecp (Default Web Site)  

InternalUrl : https://owa.mydomain.com/ecp  

ExternalUrl : https://owa.mydomain.com/ecp  

Server      : XCH19  

Name        : mapi (Default Web Site)  

InternalUrl : https://owa.mydomain.com/mapi  

ExternalUrl : https://owa.mydomain.com/mapi  

Server      : XCH19  

Name        : OAB (Default Web Site)  

InternalUrl : https://owa.mydomain.com/OAB  

ExternalUrl : https://owa.mydomain.com/OAB  

Server      : XCH19  

Name        : owa (Default Web Site)  

InternalUrl : https://owa.mydomain.com/owa  

ExternalUrl : https://owa.mydomain.com/owa  

Server      : XCH19  

Name        : PowerShell (Default Web Site)  

InternalUrl : http://xch19.internal.local/powershell  

ExternalUrl :   

Server      : XCH19  

Name        : EWS (Default Web Site)  

InternalUrl : https://owa.mydomain.com/EWS/Exchange.asmx  

ExternalUrl : https://owa.mydomain.com/EWS/Exchange.asmx  

Name                           : XCH19  

AutoDiscoverServiceInternalUri : https://autodiscover.mydomain.com/Autodiscover/Autodiscover.xml  

Server                             : XCH19  

ExternalHostname                   : owa.mydomain.com  

InternalHostname                   : owa.mydomain.com  

ExternalClientsRequireSsl          : True  

InternalClientsRequireSsl          : True  

ExternalClientAuthenticationMethod : Negotiate  

InternalClientAuthenticationMethod : Ntlm

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-19*

And all the virtual directories and autodiscover settings on the new server are pointing to the new 2019 server?    

and you are positive all the mailboxes have been moved?    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/configure-mail-flow-and-client-access?view=exchserver-2019#step-5-configure-internal-urls    

Example:    

Set-ClientAccessService -Identity <server> -AutoDiscoverServiceInternalUri https://mail.mydomain.com/autodiscover/autodiscover.xml    

Set-OwaVirtualDirectory -Identity "<server>\OWA (Default Web Site)" -ExternalUrl https://mail.mydomain.com/owa -InternalUrl https://mail.mydomain.com/owa    

Set-EcpVirtualDirectory -Identity "<server>\ECP (Default Web Site)" -ExternalUrl https://mail.mydomain.com/ecp -InternalUrl https://mail.mydomain.com/ecp    

Set-WebServicesVirtualDirectory -Identity "<server>\EWS (Default Web Site)" -ExternalUrl https://mail.mydomain.com/EWS/Exchange.asmx -InternalUrl https://mail.mydomain.com/EWS/Exchange.asmx    

Set-ActiveSyncVirtualDirectory -Identity "<server>\Microsoft-Server-ActiveSync (Default Web Site)" -ExternalUrl https://mail.mydomain.com/Microsoft-Server-ActiveSync -InternalUrl https://mail.mydomain.com/Microsoft-Server-ActiveSync    

Set-OabVirtualDirectory -Identity "<server>\OAB (Default Web Site)" -ExternalUrl https://mail.mydomain.com/OAB -InternalUrl https://mail.mydomain.com/OAB    

Set-MapiVirtualDirectory -Identity "<server>\mapi (Default Web Site)" -ExternalUrl https://mail.mydomain.com/mapi -InternalUrl https://mail.mydomain.com/mapi    

Set-ClientAccessServer -Identity <server> –AutoDiscoverServiceInternalUri https://mail.mydomain.com/Autodiscover/Autodiscover.xml    

Set-OutlookAnywhere -Identity "<server>\RPC (Default Web Site)" -ExternalHostname mail.mydomain.com -InternalHostname mail.mydomain.com -ExternalClientsRequireSsl $true -InternalClientsRequireSsl $true -DefaultAuthenticationMethod NTLM
