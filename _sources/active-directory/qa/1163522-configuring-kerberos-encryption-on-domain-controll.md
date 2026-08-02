---
title: "Configuring Kerberos Encryption on Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163522/configuring-kerberos-encryption-on-domain-controll
question_id: 1163522
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Configuring Kerberos Encryption on Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163522/configuring-kerberos-encryption-on-domain-controll (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're implementing a 3rd party product and the configuration guide calls for enabling AES encryption for Kerberos on the AD servers by configuring a GPO and modifying Network security: Configure encryption types allowed for Kerberos and selecting AES128_HMAC_SHA1, AES256_HMAC_SHA1 and Future Encryption Types.

Currently this setting is not configured on our Domain Controllers. Are there potential issues that might be caused by configuring this? Are there logs that can be audited before and after to look for potential issues?

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-01-23*

Something here could help.  

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/how-do-i-know-if-my-ad-environment-is-impacted-by-the-november/ba-p/3679869  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

Hello, 

Initially there is no specific official documentation of any potential issue regarding this GPO as it will be implemented on a Network Authentication Level, not AD authentication.

I am sharing the article describing this GPO for more details: https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-24*

Hi @Richard Long  ,

If you want force the AES encryption for kerberos authentication , you have to set the value 24 in the attribute msds-supportedencryptiontypes of the account (it can a service account or computer account) which host the SPN of  your 3rd party product.

For your information , AES 256 is supported by Windows 2008R2 and Windows 7 or later.

Before disabling RC4 , you should check if you still have a Windows 2003 or Windows XP in your environment. For more details, I invite you to read the following link : 

Decrypting the Selection of Supported Kerberos Encryption Types

Please don't forget to mark helpful answer as accepted
