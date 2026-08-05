---
title: "Difference between Active Directory roles and groups"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/181546/difference-between-active-directory-roles-and-grou
question_id: 181546
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Difference between Active Directory roles and groups

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/181546/difference-between-active-directory-roles-and-grou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

What's the difference between AD roles and groups ?  

How can I query the AD roles I'm assigned to ?  

Thanks  

Priyanka

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-02*

Hi,    

If you mean the FSMO roles on the DC:    

Active Directory has five FSMO roles, two of which are enterprise-level and three of which are domain-level . The enterprise-level FSMO roles are called the Schema Master and the Domain Naming Master. The domain-level FSMO roles are called the Primary Domain Controller Emulator, the Relative Identifier Master, and the Infrastructure Master.    

The following commands can be used to identify FSMO role owners. Command Prompt:    

netdom query fsmo /domain:<DomainName>    

For more details you can refer to the following link:    

Active Directory FSMO roles in Windows    

Security Groups are used to collect user accounts, computer accounts, and other groups into manageable units.    

For more details you can refer to:    

Active Directory Security Groups    

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-01*

On any domain controller you can query the roles  

`netdom query fsmo`  

to find the groups you're a member of  

`whoami /groups`  

--please don't forget to Accept as answer if the reply is helpful--
