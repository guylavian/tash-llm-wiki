---
title: "Exchange Token Validation Error with a JWT from Exchange Microservice"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1529794/exchange-token-validation-error-with-a-jwt-from-ex
question_id: 1529794
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange Token Validation Error with a JWT from Exchange Microservice

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1529794/exchange-token-validation-error-with-a-jwt-from-ex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!
I am struggling with the validation of the Exchange Token.
The documented process on how to validate the token worked for a long time but does not anymore.
Please see "Validate token contents" here Office 365 Exchange MicroserviceOffice 365 Exchange Microservice for the documentation.
I assume the validation failed due to the missing x5t in https://outlook.office365.com/autodiscover/metadata/json/1
The error is: IDX10501: Signature validation failed. Unable to match key: kid: 'System.String'. Exceptions caught: 'System.Text.StringBuilder'. token: 'System.IdentityModel.Tokens.Jwt.JwtSecurityToken'
It is obious that something changed. The JWT says that the app is "Office 365 Exchange Microservice" now. 
I would be grateful if you could give me a hint how to validate the new JWT from the Exchange Microservice.
Best regards  

Paul

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-11*

Hi Paul,

If the JWT you’re trying to validate lacks the `x5t` parameter, it might be due to changes in the token generation process or the certificate used. The absence of `x5t` could lead to signature validation failures, as you’ve observed.

The absence of `x5t` might indicate a change in the token generation process. Ensure that the certificate used for signing is correctly configured.

You may need validate the new JWT from the Exchange Microservice - retrieving the public key, checking the thumbprint and verifying the signature.
