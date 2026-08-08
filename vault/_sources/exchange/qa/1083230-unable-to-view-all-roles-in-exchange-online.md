---
title: "Unable to view all roles in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1083230/unable-to-view-all-roles-in-exchange-online
question_id: 1083230
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to view all roles in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1083230/unable-to-view-all-roles-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody,    

So, when login in a customer tenant, I able to view and assign a role like "view-ony organization management" for example, having 44 roles in total, but in other customer I only have 41, and all "view-only" type, "role management", etc doesn't appear...     

In thouse tenants, I'm logging with an account that has the role "Global Admin", so I think I'm able to see all of this.    

What is going on?    

Thank you!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-11-22*

Hi @Francisco José Martí García    ,    

 It's solved, thank you so much for the support :)    

Great to know that you've already thought of a solution and really appreciate it for your sharing!    

By the way, since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others.". and according to the scenario introduced here: Answering your own questions on Microsoft Q&A, I would make a brief summary of this thread:    

[Unable to view all roles in Exchange Online]    

Issue Symptom:    

when login in a customer tenant, I able to view and assign a role like "view-ony organization management" for example, having 44 roles in total, but in other customer I only have 41, and all "view-only" type, "role management", etc doesn't appear...    

In thouse tenants, I'm logging with an account that has the role "Global Admin", so I think I'm able to see all of this.    

What is going on?    

The Solution:    

I've created another user with global admin permission and now I can see this roles. It's solved.    

----------    

You could click the "Accept Answer" button for this summary to close this thread, and this can make it easier for other community member's to see the useful information when reading this thread. Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-21*

I've created another user with global admin permission and now I can see this roles. It's solved, thank you so much for the support :)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-11*

You can restart the Active Roles Administration Service, which will reset and reconnect to the Exchange Online session.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-11-11*

Hi @Francisco José Martí García   ，    

I tested in a different tenant and checked different licenses. By default, global administrator with E5 licenses only can see a total of 42 permissions.    

When my organization is configured to connect an application, the permissions corresponding to the application will appear here. In my tenant, there are 65 total of all permissions.    

    

As a workaround , I would recommend that you could try adding your missing roles to this role group in the Classic Exchange admin center. And then see whether it appears in the new EAC.    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
