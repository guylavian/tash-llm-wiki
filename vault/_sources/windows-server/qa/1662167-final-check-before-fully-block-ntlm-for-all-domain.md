---
title: "Final check before Fully Block NTLM for all Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1662167/final-check-before-fully-block-ntlm-for-all-domain
question_id: 1662167
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Final check before Fully Block NTLM for all Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1662167/final-check-before-fully-block-ntlm-for-all-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear PPL, 

I would like to set our Default Domain Policy "Restrict NTLM: Incoming NTLM Traffic" to Deny All Accounts. 

Before I do it, I have enabled Auditing Logs, can see some devices or services are still using NTLM, for example, Win10 devices, Palo UserID Agent, some LDAP queries from OP Manager etc.. 

My concern now is: there is no way disabling NTLM will break: 

Microsoft HyperV Failover Cluster, DFS or User Based 802.1x Wifi etc? 

Also, how can add third party servers or services to be exclusion to still be able to use NTLMv2? I dont see a way to add IP address? 

Thanks a lot,

Larry

## Answers

_No answers on this thread._
