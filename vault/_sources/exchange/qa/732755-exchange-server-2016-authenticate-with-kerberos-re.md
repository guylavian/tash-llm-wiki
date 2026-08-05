---
title: "Exchange server 2016 authenticate with Kerberos require Outlook 2016 input password when connect mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/732755/exchange-server-2016-authenticate-with-kerberos-re
question_id: 732755
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange server 2016 authenticate with Kerberos require Outlook 2016 input password when connect mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/732755/exchange-server-2016-authenticate-with-kerberos-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,     

Currently, our organization run Exchange Hybrid mode, we deploy Windows Hello for Business, user with on-premise mailbox will connect to Exchange Server using Kerberos. After complete deployment, we encounter issues when user with on-premise mailbox connect to Exchange, Outlook 2016 prompt require input passwords, i cancel prompt and double click to Need Password, Outlook 2016 can connect to Exchange.     

Bellow is result my checked:      

-  "Negotiate" configured for both Outlook Anywhere and MAPI virtual directories, I only have 01 server.     

-  Get-MapiVirtualDirectory | Fl authen,InternalUrl,ExternalUrl    

IISAuthenticationMethods      : {Ntlm, OAuth, Negotiate}    

InternalAuthenticationMethods : {Ntlm, OAuth, Negotiate}    

ExternalAuthenticationMethods : {Ntlm, OAuth, Negotiate}    

InternalUrl                   : https://mail.mydomain/mapi    

ExternalUrl                   : https://mail.mydomain/mapi    

-  Get-OutlookAnywhere| fl InternalClientAuthenticationMethod, authen,InternalUrl,ExternalUrl    

InternalClientAuthenticationMethod : Negotiate    

ExternalClientAuthenticationMethod : Negotiate    

InternalClientAuthenticationMethod : Negotiate    

IISAuthenticationMethods           : {Basic, Ntlm, Negotiate}    

-  Get-OrganizationConfig  | Fl MapiHttpEnabled    

MapiHttpEnabled : True    

Our server run hybrid mode, but OAuth disabled on my server.     

I also check configure Kerberos follow link Configure Kerberos authentication for load-balanced Client Access services | Microsoft Learn, i correct configure, Negotiate occur in RpcHttp, HttpProxy, Autodiscover logs. But result of klist only have http/mail.mydomain.com, does not have http/autodiscover.mydomain.com     

We only encounter this issues with Outlook 2016, our environment: Exchange Server 2016 CU22, configure Hybrid Wizard Exchange, Outlook 2013 doesn't impact by issues.     

Please help me solve this issues.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-08*

After I update Outlook 2016 by KB5001998, Outlook 2016 doesn't popup require password for access mailbox.  

Thanks for all support me.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-02-12*

I suspect:    

ExcludeExplicitO365Endpoint  is coming into play here:    

https://learn.microsoft.com/en-us/outlook/troubleshoot/profiles-and-accounts/unexpected-autodiscover-behavior    

try adding these Reg Keys to a worksation and test to see if that goes away:    

https://gist.github.com/ridercz/dc485d38da104835559c1ed8b78afad0    

Another article:    

https://medium.com/jj365/outlook-issue-with-direct-connect-to-office365-352dd29de65
