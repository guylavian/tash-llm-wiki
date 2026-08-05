---
title: "RDWeb with ADFS Windows server 2019/2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1168031/rdweb-with-adfs-windows-server-2019-2022
question_id: 1168031
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# RDWeb with ADFS Windows server 2019/2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1168031/rdweb-with-adfs-windows-server-2019-2022 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have ADFS+AD and RDweb on two hosts Windows Server 2019. I configured RDWeb. I want to configure RDWeb login via ADFS. I installed WIF and modified web.config. But when i try to access the RDWeb i get redirected to ADFS and after authentication i get this error:

 

Microsoft.IdentityServer.Web.InvalidRequestException: MSIS7042: The same client browser session has made '6' requests in the last '1' seconds. Contact your administrator for details

 

 

Rdweb log:

w3wp.exe          Information       0             2023/02/06 14:09:49 [Verbose] 64 Page Requested : Pages, Request Type : GET.

w3wp.exe          Information       0             2023/02/06 14:09:49 [Verbose] 64 Request.RawUrl: /RDWeb/Pages

w3wp.exe          Information       0             2023/02/06 14:09:49 [Info] 64 ExtractInfoFromCookies returning : False.

w3wp.exe          Information       0             2023/02/06 14:09:49 [Info] 64 Info from Form or Auth Cookie extracted : False.

w3wp.exe          Information       0             2023/02/06 14:10:04 [Verbose] 33 Page Requested : Pages, Request Type : GET.

w3wp.exe          Information       0             2023/02/06 14:10:04 [Verbose] 33 Request.RawUrl: /RDWeb/Pages

w3wp.exe          Information       0             2023/02/06 14:10:04 [Info] 33 ExtractInfoFromCookies returning : False.

w3wp.exe          Information       0             2023/02/06 14:10:04 [Info] 33 Info from Form or Auth Cookie extracted : False.

w3wp.exe          Information       0             2023/02/06 14:10:04 [Verbose] 33 Page Requested : Pages, Request Type : GET.

w3wp.exe          Information       0             2023/02/06 14:10:04 [Verbose] 33 Request.RawUrl: /RDWeb/Pages

Web.config.xml

 web.config In attachment…

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-07*

I enabled log  <add name="TraceTSWA" value="4" /> in C:\Windows\Web\RDWeb\Web.config

 I included the rdweb logs, i put them above.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-07*

Enable the logs of the app and try to understand why it rejects the token and redirects the user to the ADFS server.

Sometimes the token validity is too short, and sometimes there is a type on the relying party ID, sometimes it is a time difference, sometimes a wrong certificate, etc.
