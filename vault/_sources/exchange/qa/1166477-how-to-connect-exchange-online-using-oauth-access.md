---
title: "How to connect Exchange Online using oauth access token"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166477/how-to-connect-exchange-online-using-oauth-access
question_id: 1166477
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# How to connect Exchange Online using oauth access token

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166477/how-to-connect-exchange-online-using-oauth-access (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a requirement to connect exchange using access token. So following documentation is found about  using access token to Connect ExchangeOnline.

https://www.michev.info/Blog/Post/4249/connecting-to-exchange-online-powershell-by-passing-an-access-token#comment-21247

According to this documentation, I used auth code flow to get the access token since delegate permission is added here. I am getting following error when trying to connect.

 Connect-ExchangeOnline -UserPrincipalName {userprincipalname} -AccessToken {access_token}

Can someone help me to fix the error?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query.

The following steps describe how to connect to Exchange Online using an OAuth access token:

-  Take advantage of the Google API Console to first obtain OAuth 2.0 credentials.

-  the Google Authorization Server's access token next.

-  Next, trade your authorisation code for access and refresh tokens.

-  Once you receive your refresh and access tokens, sign in to Exchange Online using them.

-  Finally, to control the mailbox, utilize the Exchange Online PowerShell cmdlets.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.
