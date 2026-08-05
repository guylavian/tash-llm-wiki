---
title: "Azure AD Connect: Password Sync -- existing Tenant to new/empty domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5269126/azure-ad-connect-password-sync-existing-tenant-to
question_id: 5269126
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Azure AD Connect: Password Sync -- existing Tenant to new/empty domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5269126/azure-ad-connect-password-sync-existing-tenant-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a client, they have an existing Office 365 tenant with active users in, and I have just built a new empty on-premise Active Directory domain for them to join workstations to.

I have exported the list of users from Office 365 and imported them into Active Directory.

I have installed Azure AD Connect and left it in staging mode, because it looks like it is going to push the dummy passwords of the new users in AD up to Office 365, and cause carnage.

The questions I have are as follows:

-  Is my theory correct?

-  How do I change the sync direction to pull the passwords down from Office 365 and store them in AD?

-  If I can't do this immediately how do I configure the password sync to be one-way until everyone changes their password (and the user's password gets synchronised)?

Thank you

Daniel

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-19*

Hi Daniel,

Good day.

Thank you for reaching out to Microsoft community.

According to your description, Your theory is correct. If you enable password sync in Azure AD Connect, it might be synchronized the dummy passwords from your new on-premise Active Directory to Office 365, which can cause issues for your users. 

Furthermore, since your concern environment is related to Azure AD and Exchange on-premise., I would like to share some more specific information with you. Actually, Microsoft has specific channel resources where our related most valuable professional and community members can provide possible information for certain different support scope and attributes, so would you mind to contact and place your concern on our dedicated Microsoft Q&A forum channel resources? Because this forum does not focus any Azure AD and Exchange on-premise related scenario, but this forum is mainly focusing pure Office 365 exchange online service related scenario.

I would really appreciate your precious time. Thank you again for your kind cooperation.

Sincerely  

Darpan
