---
title: "NTLM Authentication Levels"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1623725/ntlm-authentication-levels
question_id: 1623725
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# NTLM Authentication Levels

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1623725/ntlm-authentication-levels (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I need your help to understand the NTLM authentication level. I am quite confused with NTLM authentication levels.

For Example, 

In Scenario 1, If my Client machine ClientA has following setting configured.

Send NTLM response only -  Client devices use NTLMv1 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

And this ClientA try to access MemberServerA & We have DC1 and on MemberServerA and DC1 we have following NTLM setting configured.

Send NTLMv2 response only. Refuse LM - Client devices use NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers refuse to accept LM authentication, and they'll accept only NTLM and NTLMv2 authentication.

Then what will happen? how NTLM authentication will be performed in this scenario 1.

Now In Scenario 2, If my Client machine ClientA has following setting configured.

Send NTLM response only - Client devices use NTLMv1 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.

And this ClientA try to access MemberServerA & We have DC1 and on MemberServerA and DC1 we have following NTLM setting configured.

Send NTLMv2 response only. Refuse LM & NTLM -  Client devices use NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers refuse to accept LM and NTLM authentication, and they'll accept only NTLMv2 authentication.

Then what will happen? how NTLM authentication will be performed in this scenario 2.

We have configured Client, Server and DC with following setting but still I can see in the logs that Client and Member server still using NTLMv1.

Send NTLMv2 response only. Refuse LM -  Client devices use NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers refuse to accept LM authentication, and they'll accept only NTLM and NTLMv2 authentication.

Thanks,

Raj

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-20*

Hi @raj a 

`My ``MemberServerA``&``DC1``both are having``Send NTLMv2 response only. Refuse LM``configured. so``MemberServerA``should send``NTLMv2 and Session security``and``DC1``should accept that``NTLMv2``but what I am getting in logs that``MemberServerA``is using``NTLMv1``for authenitcation and I unable to understand why it is using``NTLMv1``.`

It using  ntlmv1 authentication request because it receive a client authentication request with ntlmv1. In this case it will answer using the  same version it's not refused.

But when server initiates the ntlm authentication process , it will use ntlmv2.

Please don't forget to accept helpful answer

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-20*

Hello raj a,  

Thank you for posting in Q&A forum.

For scenario 1:  

DC1 only accepts NTLM and NTLMv2, clientA sends NTLM and Session security, so NTLM authentication will be successful (they will use NTLM).

For scenario 2:  

DC1 only accepts NTLMv2, clientA sends NTLM and Session security, so NTLM authentication will be not successful.  

Reference:

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
