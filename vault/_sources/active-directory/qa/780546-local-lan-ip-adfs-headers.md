---
title: "Local LAN IP - ADFS Headers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/780546/local-lan-ip-adfs-headers
question_id: 780546
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Local LAN IP - ADFS Headers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/780546/local-lan-ip-adfs-headers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have users that login through ADFS from WAP PRoxy and also directly from the LAN.  

Clearly when a user logs in through WAP, the Nework headers show the end user client IP:    

X-MS-Forwarded-Client-IP = 77.174.143.66<br>,X-MS-ADFS-Proxy-Client-IP = 77.174.143.66<br>,client-request-id = 964ad453-4c39-43c5-93e2-e3855467265a<br>,X-MS-Proxy = WAP-2019<br>,X-MS-Endpoint-Absolute-Path = /adfs/ls/<br>,  

But when the user logs into ADFS from the local LAN, the Local LAN IP is nowhere to be found in the network header request or response.   

I would like to be able to see/pull the local LAN IP of the user for a security application.  

Anyone have any idea where the local LAN IP is saved? Clearly ADFS must know it, or it could not reply back to the user.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-03-23*

Hi,    

When you're building an AD FS MFA Adapter yourself, you will see that the method that actually performs the authentication, the BeginAuthentication method, has a parameter of type HttpListenerRequest. This parameter might have the information you are looking for as per documentation system.net.httplistenerrequest    

I have a basic MFA Adapter implementation available here: adfsmfaadapter    

Hope that helps!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-25*

After spending a week on this, we are giving up. From what we can see, MSFT left out the IP discovery in ADFS because all the IP claims are null.   

We are now working to implement our own encrypted Local LAN IP pinger website to get the client IP.   

This is a real pain, but knowing the client IP is vital to our adapter.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-03-23*

Is that a generic question about .Net programming (AD FS heavily leverages the .Net framework)? I am no dev, but I guess AD FS get the IP address from the request received by the http listener. But this is not the ideal tag (AD FS) to have a proper answer to that question. Now if you are trying to do some AD FS specific things, maybe we can help :)    

Are you building an MFA provider? If so the IP is in a claim available in the pipeline accessible through the IAuthenticationAdapter adapter https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/development/ad-fs-build-custom-auth-method.    

Or are you building a risk assessment plug in? If so the client IP is also available through an existing interface: IPostAuthenticationThreatDetectionModule. https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/development/ad-fs-risk-assessment-model

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-03-23*

The source IP address in the datagram is the source IP in the case of intranet signins.
