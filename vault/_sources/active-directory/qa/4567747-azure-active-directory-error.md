---
title: "Azure Active Directory - error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4567747/azure-active-directory-error
question_id: 4567747
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 81
qa_tags: []
---
# Azure Active Directory - error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4567747/azure-active-directory-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a problem with my login account to Azure AD.

None of the info is showing and there is a "No access" windows showing in all panels

Some details are:

-  Microsoft_AAD_IAM

-  UsersListBladeV3

-  403

When you click on summary it shows:

{ "shellProps": { "sessionId": "43ea3c70dd8e41e1af300efcf0592066", "extName": "Microsoft_AAD_IAM", "contentName": "UsersListBladeV3", "code": 403 }, "error": { "message": "No access", "code": 403 }}

There is also an issue here:

The portal is having issues getting an authentication token. The experience rendered may be degraded. Additional information from the call to get a token: Extension:
 Microsoft_AAD_Devices Resource: graph Details: AADSTS50020: User account '{EmailHidden}' from identity provider 'live.com' does not exist in tenant 'Microsoft Services' and cannot access the application 'c44b4083-3bb0-49c1-b47d-974e53cbdf3c'(Azure Portal)
 in that tenant. The account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Azure Active Directory user account. Trace ID: 84a27b79-4cfb-4578-935a-8ead4c688e00 Correlation ID: b4a694c8-b091-4ea4-9880-a7a5be738dcd
 Timestamp: 2020-10-26 13:42:13Z

Anyone any ideas?

## Answer (community) — community member

*upvotes: 3 · updated: 2020-10-26*

I have resolved this one - there was a blank tenant in the AD tenant list and I created a new one and it all works now
