---
title: "Does Outlook Kerberos authentication with Exchange 2016/19 (single server) does work out of the box?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1570964/does-outlook-kerberos-authentication-with-exchange
question_id: 1570964
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Does Outlook Kerberos authentication with Exchange 2016/19 (single server) does work out of the box?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1570964/does-outlook-kerberos-authentication-with-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Before writing here all my environment configuration (DNS, virtual directories namespace and authenticatin settings, SPN -Q and SPN -L output, etc) I will put it simple, eventually I will provide more info as long as the discussion will require it.

This question is not meant to get support for sometghing that does not work, but to know why something works, where it should not from my readings on the topic and a discussion with a (Exchange-Savvy in my opinion) Redditor.  

For the curiouses, you can find the discussion here

I am in a situation where in my simple Exchange environment, made by a single Exchange 2013 server, split-brain DNS (same namespace internally and externally), with MAPI/HTTP enabled at organization level, the Kerberos authentication works both internally and externally. 

I never followed any procedure in order to have it working, such as:  

https://tkolber.medium.com/https-medium-com-tkolber-configure-kerberos-authentication-with-exchange-2019-72293aa234c

https://learn.microsoft.com/en-us/exchange/architecture/client-access/kerberos-auth-for-load-balanced-client-access?view=exchserver-2019

My MAPI VDirs are set to accept "Negotiate" authentications. Just that. And my Outlook clients connect with Kerberos.

Now, I have been said that this should not happen. Not without registering SPNs for the service to work with Kerberos. So I have somewhere a misconfiguration that oddly allow Kerberos to work.

My question is: is that true or in my case is normal that Kerberos just works? You can think I am too apprensive, but Kerberos I think it's never too much :).

As said in the intro, if required in order to get to a conclusion without any doubts, I will provide detailed components configuration.

Thank you for helping,

******* EDIT 1 ****
After some digging and thanks to the inputs I received from a user of the Spiceworks community, I can add some useful discoverings:

-  First of all some details about my namespace to avoid confusion. For privacy resaons I will call namespaces this way:
`[PS] C:\>Get-MapiVirtualDirectory | fl external*, internal*, iis*`
`ExternalUrl: https://mail.contoso.com/mapi`
`ExternalAuthenticationMethods : {Ntlm, OAuth, Negotiate}`
`InternalUrl: https://mail.contoso.com/mapi`
`InternalAuthenticationMethods : {Ntlm, OAuth, Negotiate}`
`IISAuthenticationMethods: {Ntlm, OAuth, Negotiate}`
`[PS] C:\>Get-outlookanywhere | fl external*, internal*, iis*`
`ExternalHostname                   : mail.contoso.com`
`ExternalClientAuthenticationMethod : Ntlm`
`InternalHostname                   : mail.contoso.com`
`InternalClientAuthenticationMethod : Ntlm`
`IISAuthenticationMethods           : {Basic, Ntlm, Negotiate}`

-  Autodiscover returned names, from the test avalable in the Outlook system tray icon: 'mail.contoso.com'

-  I enabled Kerberos logging. I confirm errors are logged regarding mail.contoso.com and autodiscover.contoso.com:
`1)`
`ErrorCode 0x7 `
` ErrorMessage KDC_ERR_S_PRINCIPAL_UNKNOWN`
` ExtendedError `
` ClientRealm `
` ClientName `
` ServerRealm DOMAIN.LOCAL`
` ServerName HTTP/mail.contoso.com`
` TargetName HTTP/mail.contoso.com@DOMAIN.LOCAL`
`2)`
`ErrorCode 0x7 `
` ErrorMessage KDC_ERR_S_PRINCIPAL_UNKNOWN`
` ExtendedError `
` ClientRealm `
` ClientName `
` ServerRealm DOMAIN.LOCAL`
` ServerName HTTP/autodiscover.contoso.com`
`  TargetName HTTP/autodiscover.contoso.com@DOMAIN.LOCAL` 
Given the above we should get to the conclusion that I am not authenticating with Kerberos, but with NTLM, despite the fact I theorically set Outlook to only use Kerberos or fail authentication:

Question: in order to make Kerberos authentication work, can I follow the ASA procedure? Or, for single Exchange environments, is it more advisable another approach? My thought is to follow the ASA procedure outlined here. When I will add the 2019 CAS server, since I am migrating to Exchange 2019, it will be just a matter of running the 'RollAlternateServiceAccountPassword.ps1' with the '-CopyFrom' parameter. Am I right?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-28*

Problem solved. Other than the details provided in the original post, I managed to have my Outlook clients to authenticate with Kerberos. 
Community explainations on how and why to proceed the way I did can be found here on the Reddit r/Exchange community.
Explainations about how I discovered which actual authentication protocol my clients were leveraging can be found here on Spiceworks community
Summing it up:

-  Despite logs and Outlook Status connection dialog box showed "negotiate", I was actually leveraging NTLM. As a matter of fact, klist returned no entries for the name space Outlook uses to connect to Exchange.

-  I tried to figure out whether the official MS procedure were suitable for my single server deployment scenario as well. Redditors helped me in this. 

-  In the end I followed the step-by-step procedure outlined here by comparing it with the MS official documentation.

-  In order to test the outcome, I ran "klist" from my client to see if KDC gave me tickets for the SPNs just created. It correctly showed those tickets, so now I am correctly leveraging Kerberos authentication from all my clients.
Hope this can help someone who may face the same problem.
Francesco
