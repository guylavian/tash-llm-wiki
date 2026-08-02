---
title: "Exchange 2013 Cu23 > M365, Full Hybrid, OF2016, problem onpremise accesing M365 Calendar"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1248391/exchange-2013-cu23-m365-full-hybrid-of2016-problem
question_id: 1248391
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 Cu23 > M365, Full Hybrid, OF2016, problem onpremise accesing M365 Calendar

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1248391/exchange-2013-cu23-m365-full-hybrid-of2016-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

19.04.2023 Exchange 2013 Cu23 > M365, Full Hybrid, OF2016, problem onpremise accesing M365 Calendar

Hello, We have a problem with one of our last 2013, M365, Full Hybrid mode and mixing onprem and M365 calendar (2013>M365 not working). (M365 > 2013 working). Most blogs, articles handle the other side we are not affected.

We are unsure if this is related to the change force to modern authentication or to some Autodiscover mismatch.

External DNS 

autodiscover.customer.ch pointing to onpremise Exchange 2013 IP 443 no breach/straight

INTERNAL ADS SPLIT DNS

ZONE: customer.ch, autodiscover HOST (A) 192.168.20.198 (Exchange 2013)

ZONE: customer.ch, outlook HOST (A) 192.168.20.198 (Exchange 2013)

ZONE: _TCP.customer.local autodiscover, Service Location (SRV) [0][0][443] outlook.customer.ch

ZONE: customer.local (we have NO autodiscover A-record THERE)

Users we test with:

user "test.onpremise running on EX 2013 CU23 with Outlook 2016 all patches to 03/2023, OS22H2
user "test.m365" running on M365 E3 (Was generated there cloud side) 

test.m365(CLOUD) we archived to get running all fine that all ingoing to 2013 is working (Other calendar [Free/Busy], Public Folder) this with the Registry key [HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001] which forces Outlook 2016 to use OAUTH for Autodiscover.

As soon as the mailbox is moved to M365 we push that registry key via a GPO and ADS-group to the client. That works and we handle one part of the problem like that.

What we have a problem with is following:

If user "test.onpremise" opens an additional calendar from user "test.m365" and opens the calendar we see an "old" Authentication POPUP (username above/Password below).

With another larger customer where we have it working Hybrid FULL 10% Cloud rest inhouse and we do the same (Exchange 2016 onprem) we see a quick Microsoft white Authentication box with Outlook 2016 coming and going and then you see the other calendar (M365) fine.

Any help welcome, Thank you for reading. 
Greetings from Switzerland A long-term Microsoft customer and partner

On the 2013 Logfiles when we do that we see a 200 and a 401 error from that client machine:

All data has been anomyzed:

2023-04-19 11:22:56 192.168.20.198 POST /Autodiscover/Autodiscover.xml &CorrelationID=<empty>;&ClientId=VXRIEZFV0YQQFWRSGGW&cafeReqId=4e73377c-eca8-4fc9-9383-88765ed99457; 443 - 192.168.20.38 Microsoft+Office/16.0+(Windows+NT+10.0;+Microsoft+Outlook+16.0.5254;+Pro) - `401` 1 2148074254 1 

04-19 11:22:56 192.168.20.198 POST /Autodiscover/Autodiscover.xml &CorrelationID=<empty>;&ClientId=VXRIETFV0YEQFWRSGGW&cafeReqId=98de9d99-62b7-485e-bda3-d46564798d99; 443 CUSTOMER\test.onpremise 192.168.20.38 Microsoft+Office/16.0+(Windows+NT+10.0;+Microsoft+Outlook+16.0.5254;+Pro) - `200` 0 0 12 
Below: 

W10 22H2, Outlook 2016, MAIN account oNpremise on EX2013 add account M365 account WITHOUT [HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001

We see following as soon as we try to access the other calendar. Also other people who have per AUTOSHARE get a calendar from someone which is already on M365.

Logs M365 for that user 1) From SARA DIAG tool which said MODERN AUTH is fine and "Microsoft Office" which fails with same credentials to M365

With inhouse Registry set to use "useMSOAuthForAutodiscover"

We do not see the POPUS Credentials but still have the "unable to Update" on the Remote M365 folder.
We just found out a few hours ago. We assumed that FORCE ofg MSOAuthforDISCOVER will not work inhouse with existing Outlook 2016, Exchange 2013. Does aynbody know that?

Below: W10 22H2, Outlook 2016, MAIN account on-premise on EX2013 add account M365 account `WITH` [HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001 SET

we don't see the "old style" popup but it keeps on turning almost forever until finally some Autodiscover message comes. (7-15 minutes first time....never seen this effect in 15 years Exchange Migrations)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-20*

20.04.2023, 18:33
Following steps where done add. based on local HYBRID documentation from several Blogs (Not on experience with on-premise migrations)
changes done:
DNS on-premise SPLIT inhouse:
We removed on ADS domain.local > _TCP > The _autodiscover SRV record

DNS PUBLIC:
FROM:

`autodiscover.customer.ch   		A       Exchange_2013_WAN_IP_VIP`

`outlook.customer.ch             	A       Exchange_2013_WAN_IP_VIP`

TO:

`outlook.customer.ch             	A       Exchange_2013_WAN_IP_VIP`

`autodiscover.customer.ch    	 	CNAME 	outlook.customer.ch`

Following positive effect
(Question: Does outlook.exe ONLY accept CNAME records over A-Records?)

WITHOUT "[HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001" 
Still Credential POPUP

WITH "[HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001"
We can NOW see the remote calendar faster

Question over all in general. 

Outlook 2016 latest Updates 04/2023 and Exchange 2013 RU23 on Server OS 2012 R2.
For all existing Exchange 2013 users could we BEFORE we move them to M365 enable the AlwaysUseMSOAuthForAutoDiscover with no side effect.
Current situation:

As soon as we move a user to M365 we will have to enable AlwaysUseMSOAuthForAutoDiscover for him OTHERWISE he is not able to access Public Folder existing on onrepmise Exchange 2013. (That is all solved)

But can we pre enable it all for all users running on 2013?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-20*

Hello,

Thank for taking time and helping us.

If we open outlook.exe with default user "test.onpremise" which is located on onpremise Exchange 2013 all is fine (With legacy authentication OR with the modern > Registry Key HKCU Force) > No PUPOP or in modern delay

TEST1: 

NO/Without "[HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001" 

As soon as the user "test.onpremise" opens an "test.m365" users calendar we see the credentials old style username/password POPUP from the "test.onpremise" user account.

TEST2:

With "[HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001" SET 

As soon as the user "test.onpremise" opens an M365 users calendar we see the endless Updating circle for the Remote M365 account turning and after 5-15 Minutes it's done and works.

Here are the two settings:

Question/Answer:

```
Question/Answer:

Q: Does an additional calendar in this sentence refer to the default user calendar? Or is it a new personal calendar created by the cloud user?

> Yes the DEFAULT user calendar of a regular user (Not Room Resource or Shared Mailbox)

q: How did you share your calendar from the cloud to your on-prem user?

> It is not an "AUTOSHARE"
> We, for test purpose, did open it manual from address book and select to "test.m365" cloud user
> We also has the same effect on productive/sharp users with the first sharp user migrated to M365. In that case the calendar was autoshared or per invite.
```

Effect we have WITH "[HKEY_CURRENT_USER\Software\Microsoft\Exchange] "AlwaysUseMSOAuthForAutoDiscover"=dword:00000001" SET 
It open the M365-side calendar 5-15 minutes later. We think the error still appears but the MSO does not display it or tries longer.

Trace of FQDN on W10 22H2 client

Regards

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-20*

Hi @switzerland,

In order to better understand your question, I would also like to confirm the following points with you:

1.“ If user "test.onpremise" opens an additional calendar from user "test.m365" and opens the calendar we see an "old" Authentication POPUP (username above/Password below).“

Does an additional calendar in this sentence refer to the default user calendar? Or is it a new personal calendar created by the cloud user?

-  How did you share your calendar from the cloud to your on-prem user?

 
For further troubleshooting, run the following commands separately:

Exchange Online:

```
Get-IntraOrganizationConnector | FL Name,Enabled,TargetAddressDomains,DiscoveryEndpoint,TargetSharingEpr​
```

Exchange On-Prem:

```
Get-IntraOrganizationConnector | FL Name,Enabled,TargetAddressDomains,DiscoveryEndpoint,​
```

 

（Note: You can share screenshots after removing all private information, such as domain name and email address.）
 

In addition, please check whether the Application Log on the on-prem Exchange server logs the relevant error.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
