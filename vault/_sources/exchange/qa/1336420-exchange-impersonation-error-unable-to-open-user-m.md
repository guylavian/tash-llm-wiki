---
title: "Exchange Impersonation error. Unable to open user mailbox due to impersonation error. Please make sure impersonation is set properly. (11021)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1336420/exchange-impersonation-error-unable-to-open-user-m
question_id: 1336420
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange Impersonation error. Unable to open user mailbox due to impersonation error. Please make sure impersonation is set properly. (11021)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1336420/exchange-impersonation-error-unable-to-open-user-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This has been asked and answered before. And while some people said the answer fixed the problem, many others including me cannot get this fix to work.

This is the error I get inside Google when I set up and execute a migration of an account.

Exchange Impersonation error. Unable to open user mailbox due to impersonation error. Please make sure impersonation is set properly. (11021)

I login to the Exchange Admin Center using the global admin account and this is in Microsoft 365 purchased through Comcast Business (which was a huge mistake, Comcast support has no clue how to admin Microsoft 365.)

I did the steps outlined below realizing the menu choices have changed since 2019 and 2022. But the general steps are the same.

When I attempt to create and assign the admin roles to the Global Admin account I get the following error:

Error executing request. You don't have access to create, change, or remove the "xx-xx.onmicrosoft.com\ApplicationImpersonation-GSuiteMigration" management role assignment. You must be assigned a delegating role assignment to the management role or its parent in the hierarchy without a scope restriction.

How do you assign a delegating role to global admin or is the problem something else and this is a less than-helpful or inaccurate error message?

Here is the link that is often posted in other answers from 2019 and 2022.

https://answers.microsoft.com/en-us/msoffice/forum/all/exchange-impersonation-error-unable-to-open-user/834c4ea9-6cb5-4df4-9011-433ba501f6d2

The problem is the menu options and choices have changed. Even following the expected new steps, it still doesn't work.

-  Log into to ECP e.g. https://outlook.office365.com/ecp

-  Select the Permissions menu, then Admin Roles

-  Create a new role by clicking on the + sign

-  Give it a name e.g. GSuiteMigration

-  Click on the + under roles and add the ApplicationImpersonation & ViewOnly-Configuration

-  Click the + sign under members and add the admin that requires the impersonation role

-  Save and rerun the migration steps

sp

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-11*

The above was half a solution. 

You need to ensure you add your user under both: 

-  Organization Management, AND

-  View-Only Organization Management

Once I did this, I was able to add the Group.
