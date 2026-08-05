---
title: "ADFS Certificate authentication fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/34092/adfs-certificate-authentication-fails
question_id: 34092
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Certificate authentication fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/34092/adfs-certificate-authentication-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,  

Have a Web Application Proxy with ADFS (both Server 2019). Behind is an IIS with a website (enabled Windows authentication).  

ADFS Party trust is configured as non-claims-aware. Now authentication by ADFS form is working like a charme. can login and get to the website.  

If I use certificate authentication, I get error "Error details: MSIS7009: The request was malformed or not valid."  

ADFS Eventlog:   

The incoming sign-in request is not allowed due to an invalid Federation Service configuration.    

Request url:   

 /adfs/ls/?version=1.0&action=signin&realm=urn'%'3AAppProxy'%'3Acom&appRealm=0afb0ee4-63aa-ea11-9cce-00155d010b17&returnUrl=https'%'3A'%'2F'%'2Fextranet.thurnheer.sh'%'2F&client-request-id=4B0FD864-3E6B-0001-62DE-0F4B6B3ED601&pullStatus=0   

User Action:  

 Examine the Federation Service configuration and take the following actions:   

  Verify that the sign-in request has all the required parameters and is formatted correctly.   

  Verify that a web application proxy relying party trust exists, is enabled, and has identifiers which match the sign-in request parameters.   

  Verify that the target relying party trust object exists, is published through the web application proxy, and has identifiers which match the sign-in request parameters.  

Encountered error during federation passive request.   

Additional Data   

Protocol Name:   

Relying Party:   

Exception details:   

Microsoft.IdentityServer.Web.InvalidRequestException: MSIS7009: The request was malformed or not valid. Contact your administrator for details.  

   at Microsoft.IdentityServer.Web.Protocols.MSISHttp.MSISHttpProtocolHandler.ValidateSignInContext(MSISHttpSignInRequestContext msisContext, WrappedHttpListenerRequest request)  

   at Microsoft.IdentityServer.Web.Protocols.MSISHttp.MSISHttpProtocolHandler.CreateProtocolContext(WrappedHttpListenerRequest request)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.GetProtocolHandler(WrappedHttpListenerRequest request, ProtocolContext& protocolContext, PassiveProtocolHandler& protocolHandler)  

   at Microsoft.IdentityServer.Web.PassiveProtocolTlsClientListener.OnGetContext(WrappedHttpListenerContext context)  

I did run the ADFS analyzer, no error so far.  

Any idea what I missed? Is there any tutrorial how to do so - I guess the non-claims-aware is the wrong party trust, right?  

Thanks,  

Chris

## Answer (community) — community member

*upvotes: 1 · updated: 2020-06-12*

I think they do: I only have one external IP address, let's say IPExternal = 213.144.0.1  

fs.contoso.com = IPExternal, as well the application = IPExternal. IPExternal going through NAT on the firewall to the WAP. fs.contoso.com on WAP is configured as pass-through to the ADFS server. Only port 49443 (for certifacte auth) goes through NAT to ADFS directly. If I configure 49443 to the WAP I get error 'page could not be found'.  

Thoughts?  

Update: I get the same error, when I don't have a certifiacte installed on the client. Do I need to set a trust for the certifiacte on ADFS? (Certifcate issued by Windows CA, domain joined).  

Update II: wehn I test with the Sing-In page, https://fs.domain.com/adfs/ls/idpinitiatedsignon, it works with username/password. however with the certificate it seems not to work. can select the certificate, the login page does not show an error, it just returns to its initlia status. Don't get an error in the event log nor on the login page. Guess something  with the client certificate has to be wrong.
