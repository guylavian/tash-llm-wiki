---
title: "Error installed AD CS using \"RSA#Microsoft Enhanced RSA and AES Cryptographic Storage Provider\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189017/error-installed-ad-cs-using-rsa-microsoft-enhanced
question_id: 1189017
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Microsoft Moderator"]
---
# Error installed AD CS using "RSA#Microsoft Enhanced RSA and AES Cryptographic Storage Provider"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189017/error-installed-ad-cs-using-rsa-microsoft-enhanced (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

If I installed AD CS as follows (on Windows 2019 Server Core)

Install-AdcsCertificationAuthority –CAType EnterpriseSubordinateCA  –CACommonName "Core-CA-02" `

 –KeyLength 2048 –HashAlgorithmName SHA256 `

 –CryptoProviderName  "RSA#Microsoft Software Key Storage Provider"

The above works no problem

If I change the –CryptoProviderName to the following 

–CryptoProviderName 'RSA#Microsoft Enhanced RSA and AES Cryptographic Storage Provider'

It fails to install  

 (I can use the 'Microsoft Enhanced RSA and AES Cryptographic Storage Provider' via a GUI install with no issues, this this is Windows Server Core so no GUI). So I know it is not the CryptoProviderName (unless the syntax is slightly wrong as you have to add RSA# to the beginning of the name.

I do not have the exact error message to hand at the moment (apologies), but it is something along the lines of 

Incorrect parameter, or unrecognized parameter 

Any ideas please?  

thanks in advance

CXMelga

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-13*

Hi @Charlie Melga  

It seems that the syntax is not correct : 

Did your try use  `–CryptoProviderNam Microsoft Enhanced RSA and AES Cryptographic Provider` ?

Please don't forget to mark helpful answer as accepted
