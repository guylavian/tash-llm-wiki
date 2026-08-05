---
title: "Active Directory: Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/92764/active-directory-authentication
question_id: 92764
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory: Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/92764/active-directory-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a question:  

In my organization we have a requirement for users of a certain OU. Those users should only be able to authenticate to the domain but not access its resources.  

You only need to use active directory authentication to access certain web applications.  

I have not found how to limit access, do you have any ideas?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-14*

Hi,    

You can use set a GPO to be applied on domain computers to deny logon locally this user:    

deny-log-on-locally    

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-14*

One of the requirements is that these users cannot log in to domain computers. But they must be able to authenticate to the domain.  

The "Log On To" option is not functional for me.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-14*

Hi,    

Based on my research, if you want to limit access to domain objects, you can consider use the delegation control on the domain or a OU:    

Add the users to a security group , and assign the permission what you want.    

    

    

If you want to limit access to the resource in from file servers or other resource, i'm afraid you have to limit the acce from the resource side (the share permission and the NTFS permission)    

Best Regards,

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-13*

Hi,  

By default when you create a simple domain user, he will have only the read right on all active directory object , so he is unable to modify any object in domain.  

So, you don't need perform any action to limit user access. because he don't have any access by default.  

Please don't forget to mark this reply as answer if help you to fix your issue
