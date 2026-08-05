---
title: "Active directory tools found on a non domain controller machine!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/780603/active-directory-tools-found-on-a-non-domain-contr
question_id: 780603
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active directory tools found on a non domain controller machine!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/780603/active-directory-tools-found-on-a-non-domain-contr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have a 2012R2 server running as a Hyper-V host joined to a domain, at the host level, I found the following tools installed with write access to the PDC  

-  Active Directory domain and trusts  

-  Active Directory sites and services  

-  Active Directory users and computers  

-  ADSI Edit  

In server manager/Active directory roles and features none of the Active directory roles are installed!  

Can some explain this and how to remove them and is it safe to remove them  

Thank you in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-21*

Thank you for your help, I found it under administration tools

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-21*

Ok, hard to say for sure but sounds like the host may have once been a domain controller. If you can't rebuild it then you can surely delete the offending shortcuts.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
