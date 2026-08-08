---
title: "Forbidden error for Exchange Web Service request with Authorization Code Flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1118088/forbidden-error-for-exchange-web-service-request-w
question_id: 1118088
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Forbidden error for Exchange Web Service request with Authorization Code Flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1118088/forbidden-error-for-exchange-web-service-request-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The Exchange Web Service requests to `https://outlook.office365.com/EWS/Exchange.asmx` with the access token received by the `OAuth 2.0 Authorization Code Flow` results to a status code 403 Forbidden.

Steps:  

-  Opening and authorizing the application with `https://login.microsoftonline.com/common/oauth2/v2.0/authorize` and the parameters:  

-  `client_id`: `5fafd813-xxx`  

-  `response_type` : `<redirect uri specified in azure>`  

-  `respone_mode` : query` -`scope`:`openid offline_access email https://outlook.office.com/Calendars.ReadWrite https://outlook.office.com/EWS.AccessAsUser.All\`

After authorization with my personal account, this redirects to the specified redirect uri with a code.

-   Generate a token via `https://login.microsoftonline.com/common/oauth2/v2.0/token` with the parameters:

-    `client_id`: `5fafd813-xxx`

-    `response_type`: `<redirect uri specified in azure>`

-    `respone_mode`: `query`

-    `scope`: `openid offline_access email <outlook url>/Calendars.ReadWrite <outlook url>/EWS.AccessAsUser.All`

-    `client_secret`: `6Mp8Q\~4...RD`

-    `code`: `<code from the previous step>`

This generates an access token and refresh token

-   Getting the Calendar Folder Id with a SOAP request by passing the received access token in `Authorization: Bearer <access token>`:    

Unfortunately this results to `403 Forbidden`

Is the scope of the authorization incorrect ? Is the SOAP request incorrect ?

Notes:  

-  I tested the SOAP request without impersonation that changed nothing  

-  I tested the SOAP request with the Client credentials flow and a private account `onmicrosoft` that worked correctly

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-14*

Any update on this, i have same issue, although i have a valid token and logged in succesfully.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-08*

According to the OAuth 2.0 specification, the authorization code expires shortly after it is issued, with a maximum authorization code lifetime of 10 minutes (could potentially be shorter). If you are making your requests immediately after receiving your authorization code, you can eliminate this error as a possibility.
