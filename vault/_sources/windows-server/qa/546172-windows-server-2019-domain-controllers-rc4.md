---
title: "Windows Server 2019 Domain Controllers - RC4"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/546172/windows-server-2019-domain-controllers-rc4
question_id: 546172
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows Server 2019 Domain Controllers - RC4

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/546172/windows-server-2019-domain-controllers-rc4 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our environment is running only Windows Server 2019 domain controllers, which I was under the impression no longer supported Kerberos RC4.  If that is the case, why I am still seeing “Ticket Encryption Type: 0x17 “ in the event logs?  

Is RC4 still available on 2019?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-10*

For clarity, I'm reviewing event 4769 and looking for "Ticket Encryption Type: 0x17"  which is a RC4 encrypted Kerberos ticket  

Reviewing the event logs, we only see this behavior with non-windows devices that are AD joined.  Other posts I have read suggest that it is because the AD object does not have msDS-SupportedEncryptionTypes defined, causing the DC to fall back to RC4.  Checking other similar objects where this value is set to 0x1C, shows them using AES-256 encrypted Kerberos tickets.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-10*

Hello @Coyote2045  ,    

It supports Kerberos    

Do Follow the below link to get to know more about Network security: Configure encryption types allowed for Kerberos    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos    

In an Active Directory Domain Services (AD DS) environment, the integrated accounts receive RC4 tickets instead of Advanced Encryption Standard (AES) encrypted tickets when using Kerberos authentication.     

This policy setting allows you to set the encryption types that the Kerberos protocol is allowed to use. If it isn't selected, the encryption type won't be allowed. This setting might affect compatibility with client computers or services and applications. Multiple selections are permitted.    

Hope this answers all your queries, if not please do repost back.     

If an Answer is helpful, please click "Accept Answer" and upvote it : )

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-09*

Hi @Coyote2045  ,    

I believe it still supports RC4, however even Microsoft states that it is considered less secure than the newer encryption types. (source)    

The following article by Microsoft goes through the selection of Kerberos encryption types in detail, it may be of some help.    

Decrypting the Selection of Supported Kerberos Encryption Types    

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797    

----------    

If the reply was helpful please don't forget to `upvote` and/or `accept as answer`, thank you!    

Best regards,    

Leon
