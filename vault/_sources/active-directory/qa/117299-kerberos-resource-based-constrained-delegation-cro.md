---
title: "Kerberos resource based Constrained Delegation Cross forest"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/117299/kerberos-resource-based-constrained-delegation-cro
question_id: 117299
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
---
# Kerberos resource based Constrained Delegation Cross forest

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/117299/kerberos-resource-based-constrained-delegation-cro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

I'm attempting to setup resource based constrained delegation, but failing to perform a successful authentication. Here is my setup:    

EXAMPLE.COM (Windows 2012 server):     

-  Service account: server(SPN: HTTP/server.example.com@ssss  .COM)    

TEST.NET (Windows 2016 server):    

-  user: testUser (To be impersonated)    

-  service: ldap (SPN: ldap/<hostname>@test  .NET)    

EXAMPLE.COM and TEST.NET have two way forest trust setup. I've successfully verified the trust with command [1] and verified kerberos referrals are working as expected.    

The goal is to authenticate ******@EXMAPLE.COM on behalf of testUser@test  .NET, and retrieve service ticket to TEST.NET's ldap server on behalf of testUser.     

I can successfully perform S4U2Self protocol, and retrieve service ticket for testUser@test  .NET to server@ssss  .COM. However, when trying to perform S4U2Proxy protocol to fetch service ticket to TEST.NET's ldap server, the request fails at TEST.NET's KDC. All the previous referral service tickets were successful against EXAMPLE.COM's KDC, as per MS-SFU protocol [2]. This only fails when it follows the referral to TEST.NET's KDC server.    

The KDC Response returned KDC error 12 with no additional information. When reviewing the Audit log information on DC of TEST.NET, it shows the past TGT request failure code 0xC000019B.     

I have followed the steps to setup resource based constrained delegation on the ldap account. I've also enabled allow for constrained delegation with any authentication method on the server@ssss  .COM account.    

My questions are:    

-  What could be the likely cause of this error? Given that the forest trust has verified to be working?    

-  Is there any debugging information I can turn on within domain controller to see why KDC is returning error code 12?    

[1] - netdom trust example.com /d:test.net /verify /KERBEROS (Successful on both domain sides)    

[2] - https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/3bff5864-8135-400e-bdd9-33b552051d94

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-07-23*

Take a look at:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/overlapping-forest-names-problem-forest-trust-established
