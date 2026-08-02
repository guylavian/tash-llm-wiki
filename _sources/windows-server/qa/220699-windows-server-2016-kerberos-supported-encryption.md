---
title: "Windows Server 2016 / Kerberos: Supported encryption algorithms"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/220699/windows-server-2016-kerberos-supported-encryption
question_id: 220699
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows Server 2016 / Kerberos: Supported encryption algorithms

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/220699/windows-server-2016-kerberos-supported-encryption (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, where can I find a list of all encrypted algorithms that are supported by Kerberos in Windows Server 2016? Thanks for your answers in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

Open the Group Policy Management Console. By default, the gpmc.msc tool is in the C:\Windows\System32 directory.  

Locate the relevant domain. Then, select Default Domain Policy.  

Right-click Default Domain Policy and select Edit. The Group Policy Management Editor opens.  

Click Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options.  

Double-click Network security: Configure encryption types allowed for Kerberos.  

Select one of the following encryption-type couplings.  

To prohibit the use of AES 256-bit (AES-256) encryption, select RC4_HMAC_MD5 and AES128_HMAC_SHA1.  

To allow the use of AES-256 encryption, which is the default policy setting, select RC4_HMAC_MD5, AES128_HMAC_SHA1, and AES256_HMAC_SHA1.  

For the Default Domain Controller Policy, complete the following steps.  

In the Group Policy Management Console, select Default Domain Controller Policy.  

Right-click Default Domain Controller Policy and select Edit. The Group Policy Management Editor opens.  

Repeat steps 4-6.  

reference：https://www.ibm.com/support/knowledgecenter/SSYMRC_6.0.0/com.ibm.jazz.install.doc/topics/t_kerSso_svr_enfor_encr_ad_cli.html  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky
