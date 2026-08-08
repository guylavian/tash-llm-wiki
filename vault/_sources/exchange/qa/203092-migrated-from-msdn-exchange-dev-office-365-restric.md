---
title: "[Migrated from MSDN Exchange Dev] Office 365 restricted user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/203092/migrated-from-msdn-exchange-dev-office-365-restric
question_id: 203092
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Office 365 restricted user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/203092/migrated-from-msdn-exchange-dev-office-365-restric (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/5fa75d91-fc44-4434-8b6b-8b16da21cd26/office-365-restricted-user?forum=exchangesvrdevelopment  

Hi,  

Question regarding a user's account that triggered the anti Spam policy and got restricted.  

We have the policy to restrict untill the next day.  

-  Even if I change the policy, will the user still be restricted untill the next day?  

-  If I disable the policy, how long does it take for an account to no longer be restricted.  

Also, the user is restricted due to the Anti SPAM policy, but it is not showing in the list of restricted accounts  

The list is actually emptly.  

Thank you,

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-18*

In gernal, when we change or disable an anti-spam policy,  it may take up to 1 hour to take effect.    

Does the "list of restricted accounts" mean the Block sender list?     

If so, the Block lists section should be managed manually. Based on my knowledge, the email address or email domain restricted automatically by anti-spam protection won't be added to the list.    

Please also provide more information about what anti-spam policy you created, and the restricted account.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
