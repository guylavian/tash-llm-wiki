---
title: "Windows 10 authentication via Active Directory to Big Sur Share Files"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/361099/windows-10-authentication-via-active-directory-to
question_id: 361099
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows 10 authentication via Active Directory to Big Sur Share Files

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/361099/windows-10-authentication-via-active-directory-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an active directory domain which I have near 20 macs using with no issues. I also have a OS X iMac as a File Sharing server. Now I am trying to add a new Mac Mini with Big Sur as a File Sharing server also. It is connected to the domain with no issues. I can connect to the file shares via Win7 and Win2008R2 server with no issues. When I try to connect with a Win10 Pro pc it appears the Big Sur does not see the active directory login credentials and I get a login security screen. It will not login using domain credentails, only the local Mac user.   

Thanks for any possible help!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-21*

Hi,  

I have on Win7, Server 2008R2, and Win10 all as undefined - Win10 the only one that does not work.  

I tried the NTLMv2 only on Win10 but it also failed.  

Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-21*

Hi,  

In Windows 7 and Windows Vista, this setting is undefined. In Windows Server 2008 R2 and Windows Server 2008 this setting is configured to Send NTLMv2 responses only.   

What's the result if you change the setting to Send NTLMv2 responses only or not defined on Win10 pro?  

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-19*

There is no error message that is involved. On the Windows7 and Servers the connection recognizes my domain account and functions as I would expect. On the Windows10 it does not recognize the domain account and opens a login window.  

The Security on the Windows 7 PC was as shown above - all we "Not Defined"  

On my Windows 10 PC the LAN Manager authentication is set to "Send LM & NTLM - use NTLMv2 session security if negotiated". The others were Not Defined as above.  

Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-19*

Hi,    

Before going further, would you please tell what's the error message when you try to access files from the WIN10 Pro?    

Then i would recommend you compare the NTLM policy between the WIN10 Pro and the Win7 clients:    

The Network Security: Restrict NTLM: NTLM authentication in this domain policy setting    

    

    

Best Regards,
