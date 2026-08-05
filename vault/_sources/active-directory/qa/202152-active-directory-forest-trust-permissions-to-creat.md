---
title: "Active Directory Forest Trust Permissions to create"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202152/active-directory-forest-trust-permissions-to-creat
question_id: 202152
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Forest Trust Permissions to create

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202152/active-directory-forest-trust-permissions-to-creat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Folks,  

Our Scenario: 1 forest and 1 domain and we are dividing it in two companies so we are preparing new forest and new domain.  

I have a question we are creating active directory forest trust between two companies and i would like to know what permissions we need to create a successful trust.  

-  User Account rights and permissions to create a trust between two companies  

Once creating a trust we have tom migrate the users,groups and computers from other domain so what permission are required to delegate a user to migrate the objects.  

-  ADMT tool will be used to migrate the objects.  

Appreciate your feedback !!  

Regards,  

Arif

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-18*

HI,  

To set the up the trust between the forest , the user need the administrative privilege, you either use the member of Domain Admins or members with delegated permissions.  

To run the ADMT, users need to be the member of domain admins in both the source forest and target forest. You may decide to create a user specifically for the ADMT Migration, or you may use an existing user e.g. the default administrator account.    

Best Regards,
