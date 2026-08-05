---
title: "How to fix Schema Update for Exchange 2013 Setup."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1520784/how-to-fix-schema-update-for-exchange-2013-setup
question_id: 1520784
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# How to fix Schema Update for Exchange 2013 Setup.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1520784/how-to-fix-schema-update-for-exchange-2013-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The Active Directory Schema isn't up-to-date, and this user account isn't a member of the 'Schema Admin' and/or 'Enterprise Admin' but the user is already a member of both groups.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-03-12*

Do you still face this issue?

This error can occur when the Windows Server running the schema update is not in the same Active Directory site as the schema master.

Run /PrepareSchema on a server in the same AD site as the schema master to move the FSMO role to a DC in the AD site of the server executing the schema update.

-Thomas

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-01*

Hello @Daniel Brown,

To fix a schema update issue with Exchange 2013 Setup, you may need to perform the following steps:

-  Verify group membership: Make sure the user account used to update the schema is a member of the Schema Administrators and Enterprise Administrators groups.

-  Update the schema by running Exchange 2013 Setup with the /PrepareSchema parameter.

-  After the schema update is complete, run Exchange 2013 Setup using the /PrepareAD and /PrepareAllDomains parameters

For detailed information, please refer to Prepare Active Directory and domains for Exchange Server, Active Directory Exchange Server, Exchange Server Active Directory, Exchange 2019 Active Directory | Microsoft Learn

Hope the above information is helpful to you！

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
