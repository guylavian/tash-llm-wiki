---
title: "Windows Server2012 Kerberos Domain Logon Without AS Response Ticket"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/864536/windows-server2012-kerberos-domain-logon-without-a
question_id: 864536
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-authenticator", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows Server2012 Kerberos Domain Logon Without AS Response Ticket

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/864536/windows-server2012-kerberos-domain-logon-without-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,    

I'm currently doing some experiments with domain logon, and find something makes me confused.    

When the domain user logins with kerberos protocol, the normal chanllenge-response should like below:    

-  Client  -> Server : AS Request    

-  Server -> Client  : Normally send back KDC_ERR_PREAUTH_REQUIRED first    

-  Client  -> Server : Send AS Request agin    

-  Server -> Client  : (Success) AS Response Ticket  / (Failed) KDC_ERR_PREAUTH_FAILD    

I tried to intercept the response ticket so that the client can't receive AS response, and found that the client can still login to domain account!    

Why can domain user login without domain server response ticket?    

How does windows judge whether a user can login?     

The screenshot is provided below. IP 198 is server, and 155 is client.    

Environment : (Client) Windows 10 (Server) Windows Server 2012

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-26*

I found the reason why the user can still login is because of WinLogon cache mechanism.  

If the user login before, he would leave some information in the cache.  

Next time, when user logins in and finds that he cannot connect to the domain controller, he will turn to cache login.  

This mechanism will pass the user login but without the ability to use domain resources(Because user haven't taken the kerberos ticket).  

By setting the cache count in the host computer  

(Go regedit.exe -> HKEY_LOCAL_MACHINE -> SOFTWARE -> Microsoft -> Window NT -> CurrentVersion -> WinLogon -> CachedLogonCount set to 0)  

And you will find no user can login without finishing kerberos authentication.  

Hope that it would help anyone who get into trouble with the same problem.  

Best regards.
