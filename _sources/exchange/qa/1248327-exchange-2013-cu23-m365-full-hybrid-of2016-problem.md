---
title: "Exchange 2013 Cu23 > M365, Full Hybrid, OF2016, problem onpremise accesing M365 Calendar"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1248327/exchange-2013-cu23-m365-full-hybrid-of2016-problem
question_id: 1248327
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
---
# Exchange 2013 Cu23 > M365, Full Hybrid, OF2016, problem onpremise accesing M365 Calendar

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1248327/exchange-2013-cu23-m365-full-hybrid-of2016-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

19.04.2023
Exchange 2013 Cu23 > M365, Full Hybrid, OF2016, problem onpremise accesing M365 Calendar
Hello,
We have a problem with one of our last 2013, M365, Full Hybrid mode and mixing onprem and M365 calendar (2013>M365 not working). (M365 > 2013 working). Most blogs, articles handle the other side we are not affected.
We are unsure if this is related to the change force to modern authentication. With our test user we see following effect.

-  External DNS autodiscover.domain.ch pointing to onpremise Exchange 2013 IP 443 no breach/straight

-  Internal DNS SPLIT autodiscover.domain.ch from Exchange 2013

-  All Virtualdirectory outlook.domain.ch

-  Internal _autodiscover SRV Record

-  ) user "test.onpremise running on EX 2013 CU23 with Outlook 2016 all patches to 03/2023, OS22H2

-  ) user "test.m365" running on M365 E3 (Was generated there cloud side)
test.m365(CLOUD) we archived to get running that all ingoing to 2013 is working (Other calendar [Free/Busy], Public Folder) this with the Registry key [HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001] which forces Outlook 2016 to use OAUTH for Autodiscover.
As soon as the mailbox is moved to M365 we push that registry key via a GPO and ADS-group to the client. That works and we handle one part of the problem like that.

What we have a larger problem is:

If "test.onpremise" opens an additional calendar from "test.m365" and opens the calendar we see an "old" Authentication POPUP (username above/Password below).
With another larger customer where we have it working Hybrid FULL 10% Cloud rest inhouse and we do the same (Exchange 2016 onprem) we see a quick Microsoft white Authentication box with Outlook 2016 coming and going and then you see the other calendar (M365) fine.
IIS/On the EX2013 Logfiles when we do that we see a 200 and a 401 error from that client machine:

2023-04-19 11:22:56 192.168.20.198 POST /Autodiscover/Autodiscover.xml &CorrelationID=<empty>;&ClientId=VXRIEZFV0YQQFWRSGGW&cafeReqId=4e73377c-eca8-4fc9-9383-88765ed99457; 443 - 192.168.20.38 Microsoft+Office/16.0+(Windows+NT+10.0;+Microsoft+Outlook+16.0.5254;+Pro) - 401 1 2148074254 1

2023-04-19 11:22:56 192.168.20.198 POST /Autodiscover/Autodiscover.xml &CorrelationID=<empty>;&ClientId=VXRIETFV0YEQFWRSGGW&cafeReqId=98de9d99-62b7-485e-bda3-d46564798d99; 443 CUSTOMER\test.onpremise 192.168.20.38 Microsoft+Office/16.0+(Windows+NT+10.0;+Microsoft+Outlook+16.0.5254;+Pro) - 200 0 0 12

Any help welcome, Thank you for reading.
Greetings from Switzerland
A long term Microsoft customer

```
Get-AutodiscoverVirtualDirectory | fl

RunspaceId                      : 9d4496cb-c62d-459f-1102-50eb9a939221
Name                            : Autodiscover (Default Web Site)
InternalAuthenticationMethods   : {Basic, Ntlm, WindowsIntegrated, WSSecurity, OAuth}
ExternalAuthenticationMethods   : {Basic, Ntlm, WindowsIntegrated, WSSecurity, OAuth}
LiveIdNegotiateAuthentication   : False
WSSecurityAuthentication        : True
LiveIdBasicAuthentication       : False
BasicAuthentication             : True
DigestAuthentication            : False
WindowsAuthentication           : True
OAuthAuthentication             : True
AdfsAuthentication              : False
MetabasePath                    : IIS://EXCHANGE2013.customer.local/W3SVC/1/ROOT/Autodiscover
Path                            : D:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\Autodiscover
ExtendedProtectionTokenChecking : None
ExtendedProtectionFlags         : {}
ExtendedProtectionSPNList       : {}
AdminDisplayVersion             : Version 15.0 (Build 1497.2)
Server                          : EXCHANGE2013
InternalUrl                     :
ExternalUrl                     :
AdminDisplayName                :
ExchangeVersion                 : 0.10 (14.0.100.0)
DistinguishedName               : CN=Autodiscover (Default Web
                                  Site),CN=HTTP,CN=Protocols,CN=EXCHANGE2013,CN=Servers,CN=Exchange Administrative Group
                                  (FYDIBOHF21SPDLT),CN=Administrative Groups,CN=penta,CN=Microsoft
                                  Exchange,CN=Services,CN=Configuration,DC=customer,DC=local
Identity                        : EXCHANGE2013\Autodiscover (Default Web Site)
Guid                            : 8dd24194-eddc-4a6c-82af-96c1c5985595
ObjectCategory                  : customer.local/Configuration/Schema/ms-Exch-Auto-Discover-Virtual-Directory
ObjectClass                     : {top, msExchVirtualDirectory, msExchAutoDiscoverVirtualDirectory}
WhenChanged                     : 04.04.2016 10:50:11
WhenCreated                     : 04.04.2016 10:50:01
WhenChangedUTC                  : 04.04.2016 08:50:11
WhenCreatedUTC                  : 04.04.2016 08:50:01
OrganizationId                  :
Id                              : EXCHANGE2013\Autodiscover (Default Web Site)
OriginatingServer               : DC1.customer.local
IsValid                         : True
ObjectState                     : Changed
```

We have no proxy at that customer

Remote Mailbox and route:
We can logon to onpremise client with that credentials and all works fine with the test.m365 so route fine

DNS

Split DNS internal 2013 (SRV pointing to outlook.customer.ch not autodiscover.customer.ch (We changed had no affect on our poblem with M365)

## Answers

_No answers on this thread._
