---
title: "Changing the ADFS service account options \"this account supports kerberos AES ... \""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1367962/changing-the-adfs-service-account-options-this-acc
question_id: 1367962
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Changing the ADFS service account options "this account supports kerberos AES ... "

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1367962/changing-the-adfs-service-account-options-this-acc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to join windows 2022 to 2012 R2 farm with WID and are encountering issues during pre-requisite checks. 

One option that we are thinking of trying is to enable "this account supports Keberos AES 128 bit encryption" and "this account supports Keberos AES 128 bit encryption" in the account tab of the adfs service account in Active Directory. 

The DCs, ADFS servers all have the RC4_HMAC_SHA1 , “AES128_HMAC_SHA1”, “AES256_HMAC_SHA1” set in the msds-supportedEncryptionTypes. 

One would expect that one doesn't have to select these kerberos options in the account tab since RC4_HMAC_SHA1 , “AES128_HMAC_SHA1”, “AES256_HMAC_SHA1”, “Future encryption types”  have been set through the group policy and these show up in msDS-supportedEncryptionTypes. 

So the question is, if SSO encounters issues after setting two options in service account will unchecking be enough to get things working again? Does checking those options mean that the service account with henceforth use AES even if the application (thinking adfs 2012 r2) may not support AES? And, will unchecking it revert it to use the RC4?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-28*

Hello

Enabling the options “this account supports Kerberos AES 128 bit encryption” and “this account supports Kerberos AES 256 bit encryption” in the account tab of the ADFS service account in Active Directory could potentially change the encryption type used by the service account.

If Single Sign-On (SSO) encounters issues after setting these two options, unchecking them might help to get things working again. However, this would depend on the specific issues encountered and the overall configuration of your system.

Checking those options could mean that the service account will use AES encryption, even if the application (like ADFS 2012 R2) may not support AES. Unchecking it could potentially revert it to use the RC4, given that RC4_HMAC_SHA1 is set in the msds-supportedEncryptionTypes.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-28*

Hello

Enabling the options “this account supports Kerberos AES 128 bit encryption” and “this account supports Kerberos AES 256 bit encryption” in the account tab of the ADFS service account in Active Directory could potentially change the encryption type used by the service account.

If Single Sign-On (SSO) encounters issues after setting these two options, unchecking them might help to get things working again. However, this would depend on the specific issues encountered and the overall configuration of your system.

Checking those options could mean that the service account will use AES encryption, even if the application (like ADFS 2012 R2) may not support AES. Unchecking it could potentially revert it to use the RC4, given that RC4_HMAC_SHA1 is set in the msds-supportedEncryptionTypes.
