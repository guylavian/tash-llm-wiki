---
title: "Active Directory Migration and PKI"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/343009/active-directory-migration-and-pki
question_id: 343009
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Migration and PKI

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/343009/active-directory-migration-and-pki (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everybody,  

I have a little question about AD Migration.  

I have 3 DC servers in my domaine and want to upgrade these to server 2019 (with forest and domaine upgrade).  

However, one of my DC has also role of PKI.  

I want to create 3 new servers to migrate them one by one with promotion and dismiss on DC little by little.  

If i use the same name and the same IP on my new PKI server that the old (with change of name and ip before, for no duplicate), can you think that i need to recreate all my certificats or as i use old name and IP on my new PKI server there is no problem ?  

Many thanks for your answer and your help !  

Have a nice day   

Regards

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-05*

Hi,  

Since you are going to migrate the CA , not decommission the CA, the old certificates can be used until the lifetime is expired .  

Here is the steps you can refer to  for how to Migrating The Active Directory Certificate Service From Windows Server 2008 R2 to 2019  

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-migrating-the-active-directory-certificate-service/ba-p/697674  

Best Regards,
