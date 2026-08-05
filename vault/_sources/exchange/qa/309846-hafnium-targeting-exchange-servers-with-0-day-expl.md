---
title: "HAFNIUM targeting Exchange Servers with 0-day exploits -is it my Exchange Server is Critical? Need to be re-build the Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/309846/hafnium-targeting-exchange-servers-with-0-day-expl
question_id: 309846
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# HAFNIUM targeting Exchange Servers with 0-day exploits -is it my Exchange Server is Critical? Need to be re-build the Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/309846/hafnium-targeting-exchange-servers-with-0-day-expl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support

https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/?s=09

After my Exchange2016(CU19) has been installed. When i tried this below command

Import-Csv -Path (Get-ChildItem -Recurse -Path "$env:PROGRAMFILES\Microsoft\Exchange Server\V15\Logging\HttpProxy" -Filter '.log').FullName | Where-Object { $_.AnchorMailbox -like 'ServerInfo~/' -or $_.BackEndCookie -like 'Server~/~'} | select DateTime, AnchorMailbox, UrlStem, RoutingHint, ErrorCode, TargetServerVersion, BackEndCookie, GenericInfo, GenericErrors, UrlHost, Protocol, Method, RoutingType, AuthenticationType, ServerHostName, HttpStatus, BackEndStatus, UserAgent

DateTime AnchorMailbox

2021-03-03T04:23:22.370Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-03T06:44:29.341Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-03T06:44:34.294Z ServerInfo~a]@EXC01.LOCAL:444/mapi/emsmdb/?#  

2021-03-03T06:44:37.622Z ServerInfo~a]@EXC01.LOCAL:444/ecp/proxyLogo...  

2021-03-03T06:44:38.982Z ServerInfo~a]@EXC01.LOCAL:444/ecp/DDI/DDISe...  

2021-03-03T07:02:11.493Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-03T07:02:11.899Z ServerInfo~a]@EXC01.LOCAL:444/mapi/emsmdb/?#  

2021-03-03T07:02:12.962Z ServerInfo~a]@EXC01.LOCAL:444/ecp/proxyLogo...  

2021-03-03T07:02:13.383Z ServerInfo~a]@EXC01.LOCAL:444/ecp/DDI/DDISe...  

2021-03-03T07:43:13.396Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-03T10:41:11.464Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-03T10:41:11.823Z ServerInfo~a]@EXC01.LOCAL:444/mapi/emsmdb/?#  

2021-03-03T10:41:12.386Z ServerInfo~a]@EXC01.LOCAL:444/ecp/proxyLogo...  

2021-03-03T10:41:12.886Z ServerInfo~a]@EXC01.LOCAL:444/ecp/DDI/DDISe...  

2021-03-03T11:14:15.947Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-03T14:59:37.707Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-03T14:59:39.145Z ServerInfo~a]@EXC01.LOCAL:444/mapi/emsmdb/?#  

2021-03-03T14:59:42.098Z ServerInfo~a]@EXC01.LOCAL:444/ecp/proxyLogo...  

2021-03-03T14:59:43.707Z ServerInfo~a]@EXC01.LOCAL:444/ecp/DDI/DDISe...  

2021-03-03T19:03:08.088Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-04T03:37:04.919Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-04T03:37:10.684Z ServerInfo~a]@EXC01.LOCAL:444/mapi/emsmdb/?#  

2021-03-04T03:37:17.700Z ServerInfo~a]@EXC01.LOCAL:444/ecp/proxyLogo...  

2021-03-04T03:37:24.544Z ServerInfo~a]@EXC01.LOCAL:444/ecp/DDI/DDISe...  

2021-03-05T06:49:04.896Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-05T18:59:18.860Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-06T05:28:57.010Z ServerInfo~akak]@EXC01.LOCAL:444/autodiscov...  

2021-03-06T10:36:34.479Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-06T15:38:52.872Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-06T15:39:20.404Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-06T15:41:52.656Z ServerInfo~akak]@EXC01.LOCAL:444/autodiscov...  

2021-03-06T18:48:25.164Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-06T22:50:04.125Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-06T22:50:04.204Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-07T01:46:54.059Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-07T03:38:32.487Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-07T03:38:32.691Z ServerInfo~a]@EXC01.LOCAL:444/autodiscover/...  

2021-03-07T10:27:14.379Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-07T10:51:30.728Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-07T14:19:57.268Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-07T16:26:48.416Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-08T03:30:21.129Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-08T07:10:44.912Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-08T12:29:06.447Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-08T13:34:16.809Z ServerInfo~localhost/owa/auth/logon.aspx?  

2021-03-08T16:54:34.000Z ServerInfo~localhost/owa/auth/logon.aspx?  

Import-Csv : Could not find file 'C:\Program Files\Microsoft\Exchange  

Server\V15\Logging\HttpProxy\Mapi\HttpProxy_2021022516-5.LOG'.  

At line:1 char:1  

-  Import-Csv -Path (Get-ChildItem -Recurse -Path "$env:PROGRAMFILES\Microsoft\Exch ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (:) [Import-Csv], FileNotFoundException  

-  FullyQualifiedErrorId : FileOpenFailure,Microsoft.PowerShell.Commands.ImportCsvCommand

What does it mean?

Can you advise need to be re-build the new Exchange Server?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hello Andy    

I have run this tool as given above https://learn.microsoft.com/en-us/windows/security/threat-protection/intelligence/safety-scanner-download    

Result says below    

i.e:-
