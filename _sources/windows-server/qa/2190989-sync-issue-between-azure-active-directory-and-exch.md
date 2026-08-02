---
title: "Sync issue between Azure Active Directory and Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190989/sync-issue-between-azure-active-directory-and-exch
question_id: 2190989
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 5
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Sync issue between Azure Active Directory and Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190989/sync-issue-between-azure-active-directory-and-exch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings, colleagues!

I hope everyone is enjoying your time and I appreciate your time and attention.

In our company, we had a disabled account for a user and 2 days ago I activated it using AD users and computers.

It synced with the cloud and user can log in using their new email and password.

Today they contacted me with the request that colleagues cannot find the email from the list, because the recommended email contains "@onmicrosoft.com" instead of @companyname.com

Steps I have taken to solve it:

-  Checked AD users and computers, and specified these fields manually: 

-  proxyAddress - SMTP:******@companyname.com

-  mail - ******@companyname.com

It didn't help

-  I opened Exchange and for the user I can see "Primary email" is ******@onmicrosoft.com, SMTP: ******@companyname.com

2.1. I try to change the primary email but I gtt the following error:

Error:

Error executing request. An Azure Active Directory call was made to keep object in sync between Azure Active Directory and Exchange Online. However, it failed. Detailed error message: Unable to update the specified properties for on-premises mastered Directory Sync objects or objects currently undergoing migration. DualWrite (Graph) RequestId: d5807dd2-e490-4f08-9e1a-b3c5ad239445 The issue may be transient and please retry a couple of minutes later. If issue persists, please see exception members for more information.

-  I opened the Entra and there are correct fields for the user, like nickname.

At this moment I am stuck and cannot fix it.

I need your experience and advice, please, to solve it.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-26*

Hi,

Did you find a fix for this error?
