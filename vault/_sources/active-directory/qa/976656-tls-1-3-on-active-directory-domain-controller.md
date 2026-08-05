---
title: "TLS 1.3 on Active Directory/Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/976656/tls-1-3-on-active-directory-domain-controller
question_id: 976656
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# TLS 1.3 on Active Directory/Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/976656/tls-1-3-on-active-directory-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to enable TLS 1.3 on Active Directory / Domain Controller.    

-  Is TLS 1.3 support on Active Directory / Domain Controller?     

-  If supported, can you please point to any documentation / steps to enable it.    

thanks    

Kotesh

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-08-22*

Hi     

TLS 1.3 is only available on Windows 2022 and only when fully patched.    

Gary.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-08-22*

Hi Kotesh,    

Is TLS 1.3 support on Active Directory / Domain Controller?    

Yes TLS is supported Domain Controller. But i assume you are looking forward to enable 1.3 for server through GPO.    

To enable please create Following registry key on server.     

Starting at HKEY_LOCAL_MACHINE on the left hand side of the window, please navigate through the hive to the location \SYSTEM\CurrentcontrolSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.3 in the registry, as below    

Right click on the “Protocols” key, and select New then select Key    

Name the new key TLS 1.3    

Right click the TLS 1.3 key, select New then select Key    

Name the new key Server    

Right click the TLS 1.3 key, select New then select Key    

Name the new key Client    

Select the Server key, right click and select New, then select DWORD (32-bit) Value. A new value will now be created in the main field of the regedit window. In the Name field, type Enabled and click away from the key.    

Create the last step in Client Key as well.     

Feel free to ask for queries. Please accept the answer if this works for you.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-08-22*

Hi,    

It depends what is the Operating System version of your AD DC?    

Please check this article as you requested and the supported OS and TLS settings  - protocols-in-tls-ssl--schannel-ssp-    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
