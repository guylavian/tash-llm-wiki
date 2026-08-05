---
title: "EWS Operation Item.Copy fails with 'full_access_as_app' permission"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1608048/ews-operation-item-copy-fails-with-full-access-as
question_id: 1608048
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# EWS Operation Item.Copy fails with 'full_access_as_app' permission

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1608048/ews-operation-item-copy-fails-with-full-access-as (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have been using the EWS Item.Copy Operation for nearly 5 years. Since last week (Monday 26th of February 18:00 CET) this operation started failing for 2 of our 40 customers. No configuration has changed in Azure. App Secrets and API Permissions are setup correctly and consent has been given once more to be sure. We ask our customers to grant us 'full_access_as_app', which should be enough for the EWS Item.Copy Operation and this has been enough for years.

Unfortunately for 2 customers the EWS API is denying us acces. I can get the message to be copied and I can get the target folder I want to copy the message to. But a copy operation throws the following error:

reason="Access to this API requires the following permissions: 'MailExport-Internal.Read.All,MailExport-Internal.Read.Shared,MailExport-Internal.ReadWrite.All,MailExport-Internal.ReadWrite.Shared'. However, the application only has the following permissions granted: 'full_access_as_app'."
error_category="invalid_grant"

Does anyone know how to fix this problem?

I have tested that I can get the message and target folder through the EWS API using Postman. I have renewed the App Secrets. I have checked all permissions requested and consent has been withdrawn and given to be sure. I have created a new mailbox to test if the target is an issue.

The problem still persists, even between other mailboxes and folders.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-03-04*

Likely related to this announcement: https://techcommunity.microsoft.com/t5/exchange-team-blog/retirement-of-rbac-application-impersonation-in-exchange-online/ba-p/4062671

Though the timelines they mentioned therein are not yet in effect... best open a support case to report this.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-21*

This forum post saved my day. Basically Microsoft had no idea what to do. We received instructions to register Service Principals in Exchange Admin, but we use Entra ID App Registrations to identity our application. So after 2 days of hell we've decided to refactor half of our application so we can use the MS Graph 'post message' endpoint and create copies of e-mails directly in the user mailboxes. 

Apparently you need to apply 3 'SingleValueExtendedProperties' in order to create a non-draft e-mail.
