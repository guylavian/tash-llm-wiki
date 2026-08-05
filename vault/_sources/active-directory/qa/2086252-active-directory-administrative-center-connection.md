---
title: "Active Directory Administrative Center connection error: How to fix \"Cannot connect to any domain\" issue?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2086252/active-directory-administrative-center-connection
question_id: 2086252
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Administrative Center connection error: How to fix "Cannot connect to any domain" issue?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2086252/active-directory-administrative-center-connection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am having trouble opening the Active Directory Administrative Center due to the error message "Cannot connect to any domain. Refresh or try again when connection is available." My network has two servers and two domain controllers with DNS pointing to PDC and secondary DC pointing to PDC's IP address. DFS Replication is active, the firewall is off, and the Active Directory Web Services are running on both servers. Active Directory Users and Computers work fine, but the connection issue persists.

I have checked the Active Directory Web Service on both servers, and they are listening on port "9389." What should I do next to resolve this issue?

Server1:

      DC: \DC1

 Address: \192.168.100.180

 Dom Guid: xx

 Dom Name: test

 Forest Name: test.domain

 Dc Site Name: Default-First-Site-Name

 Our Site Name: Default-First-Site-Name

 Flags: GC DS LDAP KDC WRITABLE DNS_FOREST CLOSE_SITE FULL_SECRET WS DS_8

The command completed successfully

 

Server2:

 

       DC: \DC2

 Address: \192.168.100.181

 Dom Guid: xx

 Dom Name: test

 Forest Name: test.domain

 Dc Site Name: Default-First-Site-Name

 Our Site Name: Default-First-Site-Name

 Flags: GC DS LDAP KDC WRITABLE DNS_FOREST CLOSE_SITE FULL_SECRET WS DS_8 DS_9

The command completed successfully

 

 

I have checked the ports on both servers and ADWS are running.

I found [Microsoft.ActiveDirectory.WebServices.exe] is listening different ports.

 

Server1:

[svchost.exe]

TCP   0.0.0.0:5985   0.0.0.0   LISTENING   4

Can not obtain ownership information

TCP   0.0.0.0:9389   0.0.0.0   LISTENING   14312

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   0.0.0.0:17779  0.0.0.0   LISTENING   4

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   [::]:17779  [::]:0   LISTENING   4

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   127.0.0.1:59241  127.0.0.1:3268   ESTABLISHED    14312

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   127.0.0.1:59241  127.0.0.1:389   ESTABLISHED    14312

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   127.0.0.1:59375  127.0.0.1:59376  ESTABLISHED  3508

 

Server2:

[svchost.exe]

TCP   0.0.0.0:5985   0.0.0.0   LISTENING   4

Can not obtain ownership information

TCP   0.0.0.0:9389   0.0.0.0   LISTENING   3716

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   0.0.0.0:47001   0.0.0.0   LISTENING   4

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   [::]:47001   [::]:0   LISTENING   4

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   127.0.0.1:56333   127.0.0.1:3268   ESTABLISHED   3716

[Microsoft.ActiveDirectory.WebServices.exe]

TCP   127.0.0.1:56334   127.0.0.1:56335   TIME_WAIT   0

TCP   127.0.0.1:56340   127.0.0.1:56341   TIME_WAIT   0

TCP   127.0.0.1:57787   127.0.0.1:389     ESTABLISHED  1848

Really appreciated if anyone can help.

Best

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-22*

Anyone can help?
