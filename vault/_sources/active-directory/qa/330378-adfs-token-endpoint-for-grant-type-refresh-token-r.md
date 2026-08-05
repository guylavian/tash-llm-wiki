---
title: "adfs \"token\" endpoint for grant_type = refresh_token return only access_token and id_token"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/330378/adfs-token-endpoint-for-grant-type-refresh-token-r
question_id: 330378
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adfs "token" endpoint for grant_type = refresh_token return only access_token and id_token

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/330378/adfs-token-endpoint-for-grant-type-refresh-token-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,     

when user authanticate with "Authorization code grant flow" on browser responded  refresh_token with access_token. but if i wan't to renew  access_token with "Refresh Token Grant Flow" adfs server don't return refresh_token. my request as same as this document request and response are bellow . I not sure what i mıssed.     

Thanks.    

Request    

POST https://xxxx/adfs/oauth2/token/ HTTP/1.1    

Host: xxxx    

User-Agent: Microsoft ASP.NET Core OpenIdConnect handler    

Request-Id: |b9e7f119-45d782aaa95ef147.    

Content-Type: application/x-www-form-urlencoded    

Content-Length: 3006    

client_id=<xxx>&grant_type=refresh_token&refresh_token=<yyy>    

Response     

HTTP/1.1 200 OK    

Cache-Control: no-store    

Pragma: no-cache    

Content-Length: 2469    

Content-Type: application/json;charset=UTF-8    

Server: Microsoft-HTTPAPI/2.0    

Strict-Transport-Security: max-age = 31536000    

X-Content-Type-Options: nosniff    

X-XSS-Protection: 1; mode=block    

Content-Security-Policy: default-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:;    

Access-Control-Allow-Origin: *    

Access-Control-Allow-Method: *    

Access-Control-Allow-Headers: *    

Date: Wed, 24 Mar 2021 19:54:33 GMT    

{"access_token":"xxxx,"token_type":"bearer","expires_in":300,"id_token":"xxxxxx"}

## Answers

_No answers on this thread._
