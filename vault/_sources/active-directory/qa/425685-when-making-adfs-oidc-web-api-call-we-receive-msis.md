---
title: "When making ADFS OIDC web api call we receive MSIS9604 error - Win 2016 Standard Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/425685/when-making-adfs-oidc-web-api-call-we-receive-msis
question_id: 425685
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# When making ADFS OIDC web api call we receive MSIS9604 error - Win 2016 Standard Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/425685/when-making-adfs-oidc-web-api-call-we-receive-msis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When making ADFS OIDC web api call we receive MSIS9604 error - Win 2016 Standard Server 10.0.14393 Build 14393 we get following error:  

MSIS9604: An error occurred. The authorization server was not able to fulfill the request.  

GET https://domain/?error=server_error&error_description=MSIS9604%3a+An+error+occurred.+The+authorization+server+was+not+able+to+fulfill+the+request.&state=12345&client-request-id=7b4671cc-e938-4acf-d113-00800000007e HTTP/1.1

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-27*

In my case the problem was in CORS settings. Resolved by:  

Set-AdfsResponseHeaders -EnableCORS $true  

Set-AdfsResponseHeaders -CORSTrustedOrigins http... (Redirect URI, specified in ADFS Native Application Properties)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-20*

did you manage to solve the problem?   

I have the same
