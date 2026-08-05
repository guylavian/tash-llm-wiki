---
title: "ADFS DES disabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181282/adfs-des-disabled
question_id: 1181282
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# ADFS DES disabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181282/adfs-des-disabled (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, 

Can anyone advise if the ADFS DES is disabled. And does domain controller or users account need to enable force to use RC4 or AES256 authenticate? 

We are encounter users authenticate is failed on the adfs.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-16*

Hi @Russell Ang  

Following to value in registry key DES seems enabled in the oprating system of ADFS server.

In other hand ,the supported encryption for kerberos can be controled by the attribute MS-DS-SupportedEncryptionTypes in computer object and service account where you set the SPN for you ADFS service. It can be also managed by GPO.

It's recommended to force AES encryption instead of DES and RC4. You should start to disable them on computer client and servers before domain controllers.

For more details , I invite you to read the following article: Decrypting the Selection of Supported Kerberos Encryption Types

Please don't forget to mark helpful answer as accepted
