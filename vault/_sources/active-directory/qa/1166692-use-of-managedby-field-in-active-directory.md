---
title: "Use of ManagedBy field in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166692/use-of-managedby-field-in-active-directory
question_id: 1166692
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Use of ManagedBy field in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166692/use-of-managedby-field-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can you assigned  ore than only user to the ManagedBy field in Active Directory.  I would like to start using this field to generate access reviews to Owners and some groups have multiple owners.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-03*

Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to

If you wish to Add multiple managers in Distribution group then you can do using below powershell However for User it may be not possible as it is by Design of AD.

Set-DistributionGroup -Identity "DL-with-multiple-managers" -managedby "Manager 1,"Manager 2","Manager 3" -BypassSecurityGroupManagerCheck

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-03*

Hi @Ian Slowey  

It’s not possible because the managedby attributes is a single value as mentioned in the link below:

Managed-By attribute

Please don’t forget to mark helpful answer as accepted*
