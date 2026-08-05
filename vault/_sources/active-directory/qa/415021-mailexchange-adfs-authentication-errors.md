---
title: "MailExchange ADFS Authentication Errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/415021/mailexchange-adfs-authentication-errors
question_id: 415021
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# MailExchange ADFS Authentication Errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/415021/mailexchange-adfs-authentication-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have issue with ADFS authentication on My exchange server. The problem encountered in the ADFS 3.0 of the window server 2012 and exchange server 2013 cu22. I followed the below instruction link to config AD FS claims-based authentication with Outlook Web App and EAC:    

https://learn.microsoft.com/en-us/exchange/using-ad-fs-claims-based-authentication-with-outlook-web-app-and-eac-exchange-2013-help    

In my web browser (Chrome, Firefox), I sign in OWA, response returns the http error 401. I try to sign in EAC by type my username (domain\user) and password, EAC show message "An error occurred. Contact your administrator for more information". I check event viewer of Exchange Server, there are no errors in event viewer. I check event viewer of ADFS server, the following error was reported:    

ncountered error during federation passive request.    

Additional Data    

Protocol Name:    

wsfed    

Relying Party:    

https://mailsrv.contoso.com/ecp/    

Exception details:    

Microsoft.IdentityServer.Web.InvalidRequestException: MSIS7042: The same client browser session has made '6' requests in the last '1' seconds. Contact your administrator for details.    

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.UpdateLoopDetectionCookie(WrappedHttpListenerContext context)    

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.SendSignInResponse(WSFederationContext context, MSISSignInResponse response)    

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)    

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)    

I already search in google  about error MSIS7042 but nothing can solve my problem.     

Any idea to help me?    

Thank for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-18*

@Nguyen Thanh Tung   I have the exact same issue. OWA gives me 401 and ECP access loops and ends up at ADFS with an error.    

Were you able to solve this?    

Thanks in Advance

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-03*

can anyone help me? Thank you so much.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-31*

I think browser add-in is not reason because chrome/firefox have just installed. I also try in incognito mode before I create this issue.    

I send SAML-Tracer image and SAML trace log.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-30*

My first thought is a browser add-in is causing this.  

Can you try disabling the add-ins on the one you are using?  

Also try in incognito mode.
