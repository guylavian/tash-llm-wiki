---
title: "How to enable owa only for a class of IPs, original problem: Outlook NEW needs OWA enablet"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2241034/how-to-enable-owa-only-for-a-class-of-ips-original
question_id: 2241034
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to enable owa only for a class of IPs, original problem: Outlook NEW needs OWA enablet

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2241034/how-to-enable-owa-only-for-a-class-of-ips-original (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone, I'm trying to solve an issue related to the new version of Outlook (Outlook NEW), which requires OWA (Outlook Web App) to be enabled in order to function correctly.

In our environment, OWA is currently disabled for security reasons. However, to make Outlook NEW work, we are considering enabling OWA — but only for a specific range of IP addresses.

Is there a way to allow OWA access only from a specific class or range of IPs, while keeping it blocked elsewhere?

We are using Exchange Online (Microsoft 365).  

Any suggestions would be greatly appreciated!

Thanks in advance!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-31*

Hi @Eros Rodigari ,  

Welcome to the Microsoft Q&A platform!  

You can use Conditional Access policies in Azure Active Directory . Here are the steps to achieve this:

Create a Conditional Access Policy:

Go to Azure Active Directory > Security > Conditional Access.

Click on New policy.

Under Assignments, select Users and groups and choose the users or groups you want to apply this policy to.

Under Cloud apps or actions, select Office 365 Exchange Online.

Click on Create to create the policy.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
