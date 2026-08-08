---
title: "ADFS with Web Application Proxy for User certificate Authentication failure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2046929/adfs-with-web-application-proxy-for-user-certifica
question_id: 2046929
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADFS with Web Application Proxy for User certificate Authentication failure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2046929/adfs-with-web-application-proxy-for-user-certifica (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,

I have deployed the AD servers, ADFS servers, Internal CA servers, and Web Application Proxy (WAP).

Forms Authentication (via Direct ADFS server) - Successful authentication.

Forms Authentication (via Web Application Proxy(ADFS)) - Successful authentication.

User Certificate Authentication  (via Direct ADFS server) - Successful authentication.

User Certificate Authentication  (via Web Application Proxy(ADFS)) - Failed

Ports(443 & 49443) and connectivity are reachable from the Client machine.

Server OS: Windows Server 2022 --> (ADFS & ADFS web proxy)

It is failing via Proxy only.

please help me to fix the issue. i just configured the basic configuration only. 

Error in login Web page:-

No valid client certificate found in the request. No valid certificates found in the user's certificate store. Please try again after closing and reopening the browser and choose a different authentication method.

Event Log in ADFS server:-

Encountered error during federation passive request. 

Additional Data 

Protocol Name: 

Saml 

Relying Party: 

http://xxxxxxxxxx/adfs/services/trust 

Exception details: 

Microsoft.IdentityServer.NoValidCertificateException: MSIS7121: The request did not contain a valid client certificate that can be used for authentication. This occurs when there are no valid certificates on the client computer, for example if all certificates have expired or been revoked. 

Error Code: 0x80092013 

   at Microsoft.IdentityServer.Web.Authentication.TlsClientAuthenticationHandler.ThrowCertificateErrorException(Int32 errorCode)

   at Microsoft.IdentityServer.Web.Authentication.TlsClientAuthenticationHandler.ProcessExtranetRequest(ProtocolContext context, WrappedHttpListenerRequest request)

   at Microsoft.IdentityServer.Web.Authentication.TlsClientAuthenticationHandler.Process(ProtocolContext context)

   at Microsoft.IdentityServer.Web.Authentication.AuthenticationOptionsHandler.Process(ProtocolContext context)

   at Microsoft.IdentityServer.Web.PassiveProtocolTlsClientListener.OnGetContext(WrappedHttpListenerContext context)

## Answers

_No answers on this thread._
