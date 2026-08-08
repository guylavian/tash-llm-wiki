---
title: "ADFS-SuccessFactors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1154222/adfs-successfactors
question_id: 1154222
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS-SuccessFactors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1154222/adfs-successfactors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

adfs - sso - SuccessFactors    

异常详细信息:     

Microsoft.IdentityServer.Service.Policy.PolicyServer.Engine.DuplicateNameIdentifierPolicyException: MSIS3046: 处理范围“https://www.successfactors.com/*”的策略之后生成了多个基于 SamlNameIdentifierClaimResource 的声明。

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-13*

The error suggests that there is an issue with the NameIdentifierPolicy.   

To help you, we need to know:

-  What is expected by the application (here Succesfactor)?

-  What is configured as Claims Issuance Rules on the relaying party trust?

For 1, you can share a SAML trace (with browser plugin or with a tool such as Fiddler). For 2, you can share the output of a `Get-ADFSRelyingPartyTrust` command ran on the AD FS primary server.
