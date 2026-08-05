---
title: "Advanced Threat Analytics (atauser) leaks NTLMv2 hashes, captured by SpiderLabs\\Responder red teaming tool."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/221463/advanced-threat-analytics-atauser-leaks-ntlmv2-has
question_id: 221463
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Advanced Threat Analytics (atauser) leaks NTLMv2 hashes, captured by SpiderLabs\Responder red teaming tool.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/221463/advanced-threat-analytics-atauser-leaks-ntlmv2-has (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We have Advanced Threat Analytics (ATA) 1.9 on-premise. The lightweight agents are deployed to domain controllers.    

Directory services data source is configured with a domain account.    

When running a red teaming assessment, if we run Responder (tool used to capture NTLMv2 hashes) in the background while assessing the domain controllers with an vulnerability reporting tool such as Nessus, Responder captures NTLMv2 hashes of the atauser domain account from the domain controllers.    

This is a serious concern within a security product such as ATA, is there a fix/workaround for this?    

This issue is very easy to reproduce, the NTLMv2 hashes can be used for pass-the-hash (PtH) type of cyber attacks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-11*

Hi Rita,    

I think you missed the point here.    

The issue here is not that ATA did not alert about a NTLM hash, what happened is that we were able to capture the NTLMv2 hash of the account configured under Configuration > Data Sources > Directory Services inside ATA. This account hash was leaked when we were running vuln. assessments against the domain controller where the lightweight ATA agents are installed.    

This is a security issue with the product leaking NTLM hash of the account configured in Directory Services screen.    

While I appreciate there are now alternatives to ATA, the focus of this post is for the on-premise 1.9.3 that as of posting is still in mainstream support.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

Hi c3rberus,    

Thanks for your posting on this forum.    

According to the Official Document from Microsoft, ATA identify theft using Pass-the-Hash attack through the following two steps:    

-  Attackers steal a user's NTLM hash from one computer    

-  Attackers use the NTLM hash to gain access to another computer    

In my opinion, the reason the ATA didn't alert is that we just stolen NTLM hash from DC but didn't use the NTLM hash to access the computer. Please refer to the below link for details:    

https://learn.microsoft.com/en-us/advanced-threat-analytics/suspicious-activity-guide    

It seems that the final release of ATA is ATA 1.9.3. And ATA will end Mainstream Support on January 12, 2021. In order to get new features and updates, we could move to the Microsoft Defender for Identity service.     

In addition, we could refer to the below link to learn more about the differences between ATA and Defender for Identity:    

https://learn.microsoft.com/en-us/defender-for-identity/technical-faq#what-is-azure-atp    

Thanks for your time and have a nice day.    

Regards,    

Rita    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
