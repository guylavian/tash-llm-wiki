---
title: "ADFS :  SSO with Windows session"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/397997/adfs-sso-with-windows-session
question_id: 397997
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS :  SSO with Windows session

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/397997/adfs-sso-with-windows-session (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I'm searching for a solution to connect an external application capturing Windows session.  

We have an ADFS 2019.  

Today, we are able to connect to this application but we have to login to ADFS before access it, and I want to bypass this step if possible.  

Application access will only be from internal network.  

Thank you !  

Regards,

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-05-17*

SSO configuration are described here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia#configuring-wia-for-chrome    

In a nutshell, you need to make sure that:    

-  Your browser is configured to accept Windows Integrated Authentication for the ADFS URL (that might mean that you need to add the URL to some trusted zone security settings) - that's not specific to ADFS by the way, that's for all website on which you want to us WIA.    

-  Your ADFS is configured to accept your browser for SSO (that's the link I copied earlier). That's with the WIASupportedUserAgents parameter.    

-  Your authentication policy is allowing WIA (and the application not forcing Form Based Authentication).

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

You talk about a trace from events logs / ADFS Tracing ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

Hmm... I've just tested to copy ADSF generated URL to IE, and it seems to work without credentials prompt.

Probably due to MS Edge / ADFS misconfiguration ?

I found various syntaxes for ADFS to work with MS Edge : "=~Windows\s*NT.Edg.", "=~Windows\sNT./Edg, "=~Windows\sNT.*Edg", ...

Is there a real good syntax ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

Sorry I missed to say you I have already added our ADFS URL in Intranet zone.  

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

@Pierre Audonnet - MSFT   : I found a post from you about that here : https://learn.microsoft.com/en-us/answers/questions/100097/sso-support-for-edge-chromium-based-with-adfs-30.html    

Following that, now I have this ADFS configuration :    

```
Get-AdfsProperties | select -ExpandProperty WiaSupportedUserAgents  
MSAuthHost/1.0/In-Domain  
MSIE 6.0  
MSIE 7.0  
MSIE 8.0  
MSIE 9.0  
MSIE 10.0  
Trident/7.0  
MSIPC  
Windows Rights Management Client  
MS_WorkFoldersClient  
=~Windows\s*NT.*Edg.*
```

From that, I'm not landing on ADFS login page anymore, and Edge prompts for credentials. I guess to be on the good way.    

But SSO still doesn't work.    

Any idea please ?    

Thank you.    

Regards,
