---
title: "Chrome brower version 85   error with ADFS 3.0 when reddirect Mail exchnage web"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/89744/chrome-brower-version-85-error-with-adfs-3-0-when
question_id: 89744
fetched: 2026-07-25
answer_count: 13
has_accepted_answer: false
upvotes: 2
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Chrome brower version 85   error with ADFS 3.0 when reddirect Mail exchnage web

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/89744/chrome-brower-version-85-error-with-adfs-3-0-when (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After Chrome update to versin 85.xxxx.83 , some client PC when user webmail  exhcnage over ADFS 3.0 face with issue,    

can't redirect to web mail from ADFS , if client reinstall chrome that work normal    

    

Please Help to fix this problem.    

Brs,

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-01*

Encountered same issue. This resolves.  

https://support.microsoft.com/en-us/help/4547705/authentication-loop-between-msft-sts-microsoft-com-adfs-and-owa-in-exc   

Disable chrome://flags/#reduced-referrer-granularity and also if same site setting used then disable that too.   

Although the links says exchange 2016 and 2019, it works for 2013 as well.   

By the way, no issues with chrome 84. Chrome 85 has it. If only these vendors coordinated and rolled it out.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-29*

We are seeing the same problem here in the ADFS log. Really frustrating.  

The release notes for Chrome 85 are here - https://support.google.com/chrome/a/answer/7679408#85  

It does mention changing the UserAgent string which may be why it's stopped working but not sure, I spent an hour trying to find a solution for it last week but have drawn a blank, it seems to effect all minor versions of Chrome 85 too.  

What version of Exchange server are you running? I am thinking about patching ours to the latest release (Currently on Exchange 2016 CU10).

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-29*

On ADFS log we only saw this eror Event ID364  

Exception details:   

Microsoft.IdentityServer.Web.InvalidRequestException: MSIS7042: The same client browser session has made '6' requests in the last '13' seconds. Contact your administrator for details.  

   at Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.UpdateLoopDetectionCookie(WrappedHttpListenerContext context)  

   at Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.SendSignInResponse(WSFederationContext context, MSISSignInResponse response)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)  

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)  

And only effect on chrome, can anyone help fix this problem?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-23*

We are seeing the same issue on all devices running Chrome 85 (Chromebook, iOS, MacOS, Windows and Android).  

Version 84 works flawlessly, our users just see a Error 440 (MS Timeout) error on 85, other ADFS relaying parties seem unaffected on 85, only MS Exchange 2016 OWA.  

Really hope this is sorted quickly by Google or Microsoft, easy to keep managed devices on 84 but not so easy for the 2000+ unmanaged BYO devices.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-18*

same problem here with Chrome 85. when installing chrome 84 no problem.
