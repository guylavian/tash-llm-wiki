---
title: "Problem with Exchange 2016 after update to CU 18 and CU19 - mail size"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/303488/problem-with-exchange-2016-after-update-to-cu-18-a
question_id: 303488
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Problem with Exchange 2016 after update to CU 18 and CU19 - mail size

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/303488/problem-with-exchange-2016-after-update-to-cu-18-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Morning,  

In last weekend, i've updated two exchange servers - firts to CU 18, second to CU19.  

In both servers now, i have issue with sending mail with size above 10MB. Already regonfigure everything with mailsize or attachmentsize - no results.  

Somebody have that problem after update ? There is any tips to solve this problem ?  

The problem is only, when i try to send email outside the organization - mail sending inside the organization and mail which i received has no problem with attachment bigger than 10MB.

On second Exchange Server i've already try to change InternalDsn and ExternalDsn - with no results.

Exchange Server working on Windows Server 2016 Standart fully updated in both situation. As a spam filter i'm using Barracuda Email Security Gateway.

In attachment i'm sending SS of configuration from Powershell and ECP (ECP is in polish language).

I'll wil be very grateful to help me solve this issue.

Here is returned e-mail which i already receiving trying to send e-mail with attachment:

Remote Server returned '550 5.3.4 SMTPSEND.OverAdvertisedSize; message size exceeds fixed maximum size'  

Oryginalne nagłówki wiadomości:

Received: from mail.domena.delta.pl (192.168.90.212) by  

mail.domena.delta.pl (192.168.90.212) with Microsoft SMTP Server  

(version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id  

15.1.2176.2; Mon, 8 Mar 2021 08:20:29 +0100  

Received: from mail.domena.delta.pl ([fe80::70ce:9777:24ec:d98d]) by  

mail.domena.delta.pl ([fe80::70ce:9777:24ec:d98d%7]) with mapi id  

15.01.2176.002; Mon, 8 Mar 2021 08:20:28 +0100

From: Administrator <Administrator@Gabriel  .pl>  

To: "admin@Arjun  .pl" <admin@Arjun  .pl>  

Subject: =?iso-8859-2?Q?Testy_za=B3=B1cznika?=  

Thread-Topic: =?iso-8859-2?Q?Testy_za=B3=B1cznika?=  

Thread-Index: AQHXE+tzRD6xVb7NaU+z0DfpULVUmg==  

Date: Mon, 8 Mar 2021 07:20:28 +0000  

Message-ID: <a19ab465754640d194c51b2cf766610c@Gabriel  .pl>  

Accept-Language: pl-PL, en-US  

Content-Language: pl-PL  

X-MS-Has-Attach: yes  

X-MS-TNEF-Correlator:  

x-originating-ip: [xx.xx.64.86]  

x-esetresult: clean, is OK  

x-esetid: 37303A295C230E64627463  

Content-Type: multipart/mixed;  

boundary="_004_a19ab465754640d194c51b2cf766610cajprofibudpl_"  

MIME-Version: 1.0

1

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

Hello again,  

Problem solved. In my case, firewall rule blocked attachment bigger than 10MB.  

So if you have UTM device, like Stormshield, Fortigate or simmilar, chceck youre rules on firewall. My rule was:  from Network In  >  to ANY > port: plugins >  filter :IPS, Antivirus  

I added new rule: from IP Exchange> to Barracuda > port: SMTP >  filter: only IPS  

That's worked for me.
