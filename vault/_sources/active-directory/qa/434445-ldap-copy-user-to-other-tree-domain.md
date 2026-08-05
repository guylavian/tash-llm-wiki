---
title: "LDAP copy user to other Tree domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/434445/ldap-copy-user-to-other-tree-domain
question_id: 434445
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# LDAP copy user to other Tree domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/434445/ldap-copy-user-to-other-tree-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'd like to know if it's possible to have a user sync between two domain, one master ans other as a tree domain added to the forest ?    

As you can see in the picture, it's a particular infrastrcuture. We have a specifique entreprise AD, who's connected by an other Tree domain (dom2). The reason is administrative, entreprise AD is managed by someone else, and I manage dom2.    

ADs are linked (trust) to use entreprise authentification and it works well. But if entreprise AD aren't responding, all authentification isn't working. And this is normal.    

But, is it possible to sync users in a read only mode to dom2. So if entreprise AD are down, authentification will still be fonctunal.    

Thanks for your help.    

BR

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-22*

Hi,  

Now I'm not copying any user.  

If/when dom1 crash, I'n not able to restore or do anithing on it. It's managed by an external compagny. That's why I'd like to syncronise user on dom2.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-22*

Hi,  

I'm not sure how did you copy the users from dom1 to dom2, here are some of my views：  

Since the dom1.com is already crashed, the user can't be used anymore since there are no DCs for authentication.  

If you have a backup for it, you may consider restoring it.  

If you don't need the dom1 anymore, you may try to do user accounts /computer accounts migration from dom1 to dom2.  

Best Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-21*

Hi,    

Thanks for your feedback, and sorry for the delay. COVID-19 second shot was quit challenging.    

Exactly, two domain in the same forest.    

I'd like to have a full copy of users and password from dom1 to dom2, automatically synchronised. Point is dom1 isn't safe enough and already crashed. So we lost all connexion LDAP and Radius on all our equipment.    

On a web service, I successively tested LDAP authentification, settings based on dom2 but with suffix @Dominic Dupuis  .com. But when on firewall I've block all traffic from dom1 to dom2, to test a crash, authentification failed.    

Why this ? Because our user for laptop/desktop are in dom1. And we would like to use the same user for authentification on our devices but using dom2. We need a second domain (dom2) for specific user account and for security groups.    

Is it understandable ?    

Thanks for your feedback.    

Best regads

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-15*

Hi,  

Based on my understanding, there are 2 domains in the same forest, right?  

Users can be migrated between domains or forests.  

To understand your question more clearly, can you explain what do you exactly mean to when you said "ADs are linked (trust) to use entreprise authentification"?  

What's the purpose you want to achieve?  

Best Regards,
