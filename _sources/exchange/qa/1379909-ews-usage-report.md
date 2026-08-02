---
title: "EWS Usage Report"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1379909/ews-usage-report
question_id: 1379909
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# EWS Usage Report

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1379909/ews-usage-report (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

How can we get EWS usage report? This is in reference to Retirement of Exchange Web Services in Exchange Online in 2026.

We have already got rid of EWS Basic Auth but there is not logs available for modern EWS. To remediate and transfer this, we need to know what devices/apps are using EWS.

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-04*

Hi Kael, 

How we can get this:

Now that basic auth was deprecated and all apps should be using OAuth to access EWS, I'd say the easiest way to identify such apps would be to check Azure AD admin center for registered app with either EWS.AccessAsUser.All or full_access_as_app permissions listed, it'd probably make sense to also check Azure AD sign-in logs to validate those apps are still active. I'm positive this should be achievable through PowerShell; I will ask someone from the team to take a look at it and get back to us. 

i can see all registered apps and they are plenty. How do i filter them based on permissions?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-03*

Hi @Hasan Siddiqui,

As far as I know, there is currently no built-in report available on EWS usage and you may probably need to check the Azure sign-in log to see app usage.

While it is now under work for tenants that are using EWS.

Please refer to the comments in this Exchange blog:

Retirement of Exchange Web Services in Exchange Online

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
