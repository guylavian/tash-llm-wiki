---
title: "Moving Exchange domain into o365 Tenant"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1013207/moving-exchange-domain-into-o365-tenant
question_id: 1013207
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Moving Exchange domain into o365 Tenant

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1013207/moving-exchange-domain-into-o365-tenant (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,    

As part of acquiring domain - currently pointing to messagelabs gateway to exchange 2010(messagelabs subscription going to expire, we need to add the Domain to the o365 domain so email redirections are filtered via o365 domain tenant.    

we still forwarding emails from exchange to our o365.    

We migrated mailbox -    

Source mailbox - Exchangeserver 2010 .pst file provided in Azure Storage    

Destination -  user mailbox    

Copied over contents of PST to a newly created folder in user's mailbox called 'exchange Emails;.    

Public folders still on exchange 2010.    

what should be our plans to move the exchange 2010 domain to o365 domain without loosing emails?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-22*

Hi @Saurabh Singh   ,    

Your requirement is to migrate public folder to Exchange Online, and there are two options supported by Microsoft:    

-  Migrate directly with administrator privileges, but you cannot use this method without privileges.    

-  Use the Outlook export feature, but Microsoft does not recommend it.    

    

In addition is what you mentioned about migrating EDB files, you can use the relevant three-party tool to do so, but this is not a practice supported by Microsoft, so support for it cannot be provided.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-20*

Please have a look at below given informative resources that might help you to get more details and lets you get this done:    

Support for Multiple Top Level Domains:- https://community.office365.com/en-us/w/sso/support-for-multiple-top-level-domains    

Setting up AD FS and Enabling Single Sign-On to Office 365:- https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-setting-up-ad-fs-and-enabling-single-sign-on-to/ba-p/295302    

Directory synchronization roadmap:- https://learn.microsoft.com/en-us/microsoft-365/enterprise/deploy-microsoft-365-directory-synchronization-dirsync-in-microsoft-azure?view=o365-worldwide
