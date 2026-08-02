---
title: "Is kerberos over IP supported over a trusted domain to mount share?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/730037/is-kerberos-over-ip-supported-over-a-trusted-domai
question_id: 730037
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Is kerberos over IP supported over a trusted domain to mount share?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/730037/is-kerberos-over-ip-supported-over-a-trusted-domai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 domains, Domain A and Domain B which are trusted each other. And I have a Windows 10 Client in Domain A and a Windows 2019 Server in Domain B with hostname server1 and IP 10.6.12.12. And I want to mount a share from server1 to my Windows 10 client with IP.  

So followed the below steps:  

-  Added TrySpn in Windows 10 Client registry to enable Kerberos Over IP  

-  Added setspn HOST/10.6.12.12 server1 in Domain B  

-  Verified that mounting share folder via Hostname is authenticating with Kerberos  

But when I try to mount with server1 IP instead of hostname, authentication is happening via NTLM instead of Kerberos.  

Tried mounting using the command "net use * \10.6.12.12\share"  

Is there any additional changes to be made in the Domains to make kerberos via IP to work in trusted domains?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-10*

Hi @Jack AD       

Kerberos authentication is based on the SPNs, these are used to issue a token for the resource.  As soon as you use an IP address Windows will default back to NTLM authentication.    

Have a look at this post which provide some more details on Kerberos authentication across a trust (their certificate has expired, so there is a warning)    

Gary.
