---
title: "ADFS 3.0 error 364 (msis 7042) on ADFS + error 224 on ADFS PROXY maybe after windows update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/17851/adfs-3-0-error-364-msis-7042-on-adfs-error-224-on
question_id: 17851
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 3.0 error 364 (msis 7042) on ADFS + error 224 on ADFS PROXY maybe after windows update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/17851/adfs-3-0-error-364-msis-7042-on-adfs-error-224-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all!  

Dynamics on premise, exposed with ADFS 3.0 and ADFS PROXY  

So i have this scenario:

1 vm x sql (lan)  

1 vm x dynamics (lan)  

2 vm x dns and dc (lan)  

1 vm x adfs (lan)  

1 vm x adfs proxy (Dmz)

After windows update for windows 2012 r2 on ADFS and ADFS PROXY vm, it stops to authenticate from external  

When i try opening https url, it loops until error  

On lan, it works

on browser client this error:

```
Activity ID: 00000000-0000-0000-5000-0080000000d0
Relying party: CRM CLAIMS RELYING PARTY
Error time: Tue, 24 Mar 2020 07:53:03 GMT
Cookie: enabled
User agent string: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0
```

on ADFS server i can try this log:  

error id 364  

Encountered error during federation passive request.

Additional Data

Protocol Name:  

wsfed

Relying Party:  

https://mydynamics.mydomain.com/

Exception details:  

Microsoft.IdentityServer.Web.InvalidRequestException: MSIS7042: The same client browser session has made '6' requests in the last '1' seconds. Contact your administrator for details.  

at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.UpdateLoopDetectionCookie(WrappedHttpListenerContext context)  

at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.SendSignInResponse(WSFederationContext context, MSISSignInResponse response)  

at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)  

at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)

on ADFS SERVER, enabling AD FS tracing, this 3 error:

-   Error 1

Detected an instance where RP is not configured properly, and requesting tokens repeatedly

-   Error 2

Exception: MSIS7042: The same client browser session has made '6' requests in the last '2' seconds. Contact your administrator for details.  

StackTrace: at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.UpdateLoopDetectionCookie(WrappedHttpListenerContext context)  

at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.ProcessCommonCookiesInLastAuthenticationStage(ProtocolContext context)  

at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.SendSignInResponse(WSFederationContext context, MSISSignInResponse response)  

at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.Process(ProtocolContext context)  

at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)  

at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)

-   Error 3

Passive pipeline error

on ADFS proxy  

error id 224

user: NETWORK SERVICE Event id 224

The federation server proxy configuration could not be loaded correctly from the configuration file ''.  

Additional Data  

Error:

User Action: A configuration element specified in the data above is misconfigured. Correct the specified error in the AD FS configuration database.

This happens with different client, with different browser (no trust site oro protection mode IE works)  

Just rebooted , vm CRM DYNAMICS, vm ADFS and vm ADFS PROXY no success  

Thanks ask me for details  

M

## Answers

_No answers on this thread._
