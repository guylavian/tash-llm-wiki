---
title: "Exchange 2016 On-Prem - Auto delete messages in a Shared mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1003570/exchange-2016-on-prem-auto-delete-messages-in-a-sh
question_id: 1003570
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 On-Prem - Auto delete messages in a Shared mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1003570/exchange-2016-on-prem-auto-delete-messages-in-a-sh (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears    

In an Exchange 2016 On-prem environment I would like to auto delete messages older than 3 days in a Shared mailbox.    

I read about this on the net and I found that the only soulition would be an outlook rule (the is a non presidiated mailbox) OR an exchange Retention policy rule.    

On our server we have only Default Role Assignment Policy (MyRetentionPolicies option is not ON) and Default MRM Retention policy.    

If I understood correctly, to achieve my goal I would have to:    

-  Create a new Default Role Assignment Policy and enable the MyRetentionPolicies option    

    

-  Create a new Tag for the 3 days Retention    

    

-  Create a new Retention policy and add a new tag for 3 days --> delete     

    

-  Assign here the new REtention policy (still not created in the screenshots)    

     

Is it correct?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-13*

Hi @A Ska   ,    

Agree with Andy, If the tag you are talking about is this one in the screenshot, then you need to create a new default tag.    

    

Default policy tags can be applied to shared mailboxes while Personal tags cannot. You may need this:    

    

You could refer to:    

    

Official Documentation: https://learn.microsoft.com/en-us/Exchange/policy-and-compliance/mrm/retention-tags-and-retention-policies?view=exchserver-2016    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-12*

Create a new policy and add the existing one week tag to the policy, then assign the policy to the shared mailbox.    

If the existing one week tag is a personal tag, then create a one week DEFAULT tag and assign to a new policy instead. Assign that policy to the shared mailbox.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-12*

Everything but that first step.     

No need for this:    

Create a new Default Role Assignment Policy and enable the MyRetentionPolicies option    

You are assigning the new policy as an admin, the MyRetentionPolicies just gives a user the ability to access see the policies.
