---
title: "KMS Server and Active Directory Based License Activation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1162166/kms-server-and-active-directory-based-license-acti
question_id: 1162166
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# KMS Server and Active Directory Based License Activation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1162166/kms-server-and-active-directory-based-license-acti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have set up Active Directory Based License Activation for Windows Server 2019.

However, there is a request to activate a workgroup Windows Server 2019.  

Can we use the same KMS Host Key (Used for ADBA) and create a KMS Server to meet the need ?  Can we use the same Domain Controller for both KMS Host & ADBA ?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-19*

Hello

Thank you for your question and reaching out. 

Only domain-joined machines can be activated using ADBA. In other words, the ADBA cannot be used to activate any workgroup or computer that is a member of a different AD forest. OR if you have workgroup computers outside the domain, you need to maintain a KMS host to maintain activation status.

Reference :

https://learn.microsoft.com/en-us/windows/deployment/volume-activation/activate-using-active-directory-based-activation-client

--If the reply is helpful, please Upvote and Accept as answer--
