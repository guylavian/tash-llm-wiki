---
title: "CORS issue when accessing https://{ADFS_SERVER}/adfs/userinfo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/436931/cors-issue-when-accessing-https-adfs-server-adfs-u
question_id: 436931
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# CORS issue when accessing https://{ADFS_SERVER}/adfs/userinfo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/436931/cors-issue-when-accessing-https-adfs-server-adfs-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are able to sucessfully login and get the token using the following code,  

oauthService.clientId = 'd3263663-7950-4f48-99a9-ad10d7907245';  

oauthService.loginUrl = 'https://{ADFS_SERVER}/adfs/oauth2/authorize';  

oauthService.issuer = 'https://{ADFS_SERVER}/adfs';  

oauthService.scope = "openid profile";  

oauthService.responseType = 'id_token token';  

But by using the token, we have called the userinfo API - https://{ADFS_SERVER}/adfs/userinfo  

But it shows CORS error. anything to be done on ADFS Server for this issue.

## Answers

_No answers on this thread._
