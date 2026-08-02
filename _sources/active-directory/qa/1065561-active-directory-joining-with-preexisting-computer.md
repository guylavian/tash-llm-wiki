---
title: "Active Directory - Joining With Preexisting Computer Object (Post KB5020276)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1065561/active-directory-joining-with-preexisting-computer
question_id: 1065561
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory - Joining With Preexisting Computer Object (Post KB5020276)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1065561/active-directory-joining-with-preexisting-computer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

With KB5020276, our team members are no longer able to join objects to the domain that were created by privileged team members.    

We have two groups: 'Admins' and 'Technicians', our Admins have permission to create Computer objects, and will create preexisting computer objects in the proper OU's, adding the Technicians group to the 'User or Group' that 'can join this computer to a domain'. When imaging, our Technicians will join the computer to the domain. However, with the KB5020276 update, now only the creator of the OU is currently able to join the computer.     

Is there an additional setting necessary so our techs can join computers to the domain?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-11-03*

Hello ChristianFarley-6650,    

Thank you for posting in our Q&A forum.    

From the following link, it seems you can only join the machines domain with one of the following methods.    

The user attempting the operation is the creator of the existing account.    

OR    

The computer was created by a member of domain administrators.    

KB5020276—Netjoin: Domain join hardening changes    

https://support.microsoft.com/en-us/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
