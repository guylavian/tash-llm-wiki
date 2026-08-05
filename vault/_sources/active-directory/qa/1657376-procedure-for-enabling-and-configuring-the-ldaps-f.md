---
title: "Procedure for enabling and configuring the LDAPs feature for the existing Domain Controllers globally."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657376/procedure-for-enabling-and-configuring-the-ldaps-f
question_id: 1657376
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-security", "windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Procedure for enabling and configuring the LDAPs feature for the existing Domain Controllers globally.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657376/procedure-for-enabling-and-configuring-the-ldaps-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to globally configure the LDAPS feature in over 20 on-premises Domain Controllers/Global Catalogs to support new security software integration.

My existing AD Domain controllers are Windows Server 2016 with Windows Server 2016 FFL/DFL.

What steps must I follow to manually enable LDAPS setup in all Domain Controllers or just one for the forest-wide? 

Thank you for your help, and I look forward to hearing back from you soon.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-19*

Hello,

 

Thank you for posting in Q&A forum.

To configure LDAPS on Windows Server, please kindly follow below Microsoft Official Documentation and check further.

https://techcommunity.microsoft.com/t5/sql-server-blog/step-by-step-guide-to-setup-ldaps-on-windows-server/ba-p/385362

After the implementation, please kindly test the function and see if it works.

To help other customers who may be facing the same issue, please don't forget to vote if the reply is helpful.

 

Best regards，

Jill Zhou
