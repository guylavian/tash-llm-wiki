---
title: ".NET 6 Blazor server on Windows domain - Kerberos delegation and impersonation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/830189/net-6-blazor-server-on-windows-domain-kerberos-del
question_id: 830189
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-dotnet-blazor", "windows-business-windows-server-user-experience-user-experience-other", "windows-development-iis"]
---
# .NET 6 Blazor server on Windows domain - Kerberos delegation and impersonation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/830189/net-6-blazor-server-on-windows-domain-kerberos-del (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,   

I'm trying to solve a problem which appear to be simple in theory but somewhat hard in reality. After reading a lot of posts online I feel the need to ask for help in here.   

What I'm trying to do is this (all via Kerberos / Windows auth)  

Client user (Windows, Domain A, has domain SPN) -> Blazor Server on Server 1 (Wndows Server, Domain A, IIS10, SPN TrusedForDelegation) -> Service API (Windows Server, Domain A, has domain SPN)  

The trick is that I want the Blazor server app to call the "Service API" as the "Client user" (impersonation). This is working as expected when debugging using IIS Express on my laptop, however, when I deploy the build to the production server it does not work. The server hosting the Blazor Server app is trusted for delegation and I see no Kerberos errors on the network traffic.   

I believe that I have tried every single permutation of IIS settings and ways to impersonate without any luck. My "Blazor server" gets a 401 back from the Service API. I can see that Authentication and AD authorization on the Blazor server is working as expected.   

Is there a official way of configuring impersonation in .NET 6 with IIS 10 in a Blazor Server app using Kerberos as the authentication protocol?   

Thank you for the help.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-03*

Hi there,  

KRB Error: KRB5KDC_ERR_BADOPTION error occurs when the BIG-IP APM system is unable to obtain a Kerberos service ticket on behalf of the user and Kerberos SSO fails for the user.   

When these messages occur, consider the following:  

-In the Active Directory delegation account (Account Properties > Delegation), add the requested service to the Services to which this account can present delegated credentials box.  

-When using a non-Windows Kerberos KDC environment, ensure that the KDC can support the same options as Active Directory.  

The below thread discusses the same issue and you can get some insights from this.  

Kerberos error when using a DNS name that doesn't match the Active Directory domain name https://social.technet.microsoft.com/Forums/windowsserver/en-US/736b4f5e-536f-455d-bf73-3c4d147de4b6/kerberos-error-when-using-a-dns-name-that-doesnt-match-the-active-directory-domain-name?forum=winservergen  

--If the reply is helpful, please Upvote and Accept it as an answer–
