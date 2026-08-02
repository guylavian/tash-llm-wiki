---
title: "Active directory based activation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194709/active-directory-based-activation
question_id: 2194709
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active directory based activation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194709/active-directory-based-activation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

Today my customer has domain controller with 2012R2. 

Migration to 2025 is planed for this year. 

He is using only KMS server to activate all server + clients today.

The plan is to migrate it to Active directory based activation. 

He has different members servers : 2012r2 until 2025 and W10 + W11. 

1)Is it possible to install volume activation role on domain controller and use 2025 CSVLK key ?

On MS documentation, I think I understand 2025 CSVLK key is not possible on 2012R2. 

Should I use a member server 2025 and install volume activation role on it to create the activation AD on the domain for it to work ? 

-  If I use a 2022 CSVLK key for ADBA activation, will 2025 server will be automatically activated on a supported environment or do I need to enter a 2025 CSVLK key to create a new activation object to be able to activate 2025?

## Answer (community) — community member

*upvotes: 1 · updated: 2025-02-17*

Hello

-  You are correct that Windows Server 2025 CSVLK keys cannot be used on Windows Server 2012 R2. To implement Active Directory-Based Activation (ADBA) for Windows Server 2025, you should use a member server running Windows Server 2025 and install the Volume Activation Services role on it to create the activation object in Active Directory.

-  If you use a 2022 CSVLK key for ADBA activation, it will not automatically activate Windows Server 2025. You will need to enter a 2025 CSVLK key to create a new activation object to be able to activate Windows Server 2025.

Have a nice day.

Best Regards,

Hania
