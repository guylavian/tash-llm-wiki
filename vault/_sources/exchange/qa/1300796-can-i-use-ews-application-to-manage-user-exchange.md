---
title: "Can I use ews application to manage user exchange on-premise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1300796/can-i-use-ews-application-to-manage-user-exchange
question_id: 1300796
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Can I use ews application to manage user exchange on-premise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1300796/can-i-use-ews-application-to-manage-user-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I'm referring to this document https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-authenticate-an-ews-application-by-using-oauth#app-only-authentication (session App-only authentication code) to get all the folders of exchange on-premise users.

My exchange server has these users, one of them having type O365. 

It works well on user 3 with type O365, but with user_1, and user_2 which is in exchange on-premise. It throws an exception mailbox not found in this line. So I wonder If that this can only work with O365 email? Can someone confirm that for me? It will be a big help. 

```
var folders = ewsClient.FindFolders(WellKnownFolderName.MsgFolderRoot, new FolderView(10));
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-07*

Correct, that will only work in Exchange Online
