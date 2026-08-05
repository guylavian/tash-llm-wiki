---
title: "ADFS Authentication with Multiple Forests for Remote Desktop Services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/22777/adfs-authentication-with-multiple-forests-for-remo
question_id: 22777
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Authentication with Multiple Forests for Remote Desktop Services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/22777/adfs-authentication-with-multiple-forests-for-remo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

How can I do ADFS Authentication with Multiple Forests for Remote Desktop Services?  

I have an on-premises Remote Desktop environment and now we are merged with other company and they want to access our Remote Desktop Environment with their AD User through Active Directory Federation Services (ADFS).  

They don't want to use a VPN tunnel for AD trust.  

Is there any way, we can do ADFS Authentication with AD Forest trust for on-premises Remote Desktop environment?   

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-04-23*

Is this possible users from other AD Forest can access RDS from WebClient authentication with the federation services?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-04-16*

Remote Desktop needs Windows users (either local or from an ADDS domain). You cannot replace RDP authentication with federation.    

You could publish an RDP gateway with web access and use federation to access the web part, but once on the gateway you would still need a user account on the target server.
