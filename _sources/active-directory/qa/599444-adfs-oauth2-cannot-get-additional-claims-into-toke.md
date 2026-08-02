---
title: "ADFS Oauth2 Cannot get additional claims into token"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/599444/adfs-oauth2-cannot-get-additional-claims-into-toke
question_id: 599444
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 3
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Oauth2 Cannot get additional claims into token

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/599444/adfs-oauth2-cannot-get-additional-claims-into-toke (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been trying to configure ADFS 2016 to work with OAUTH2 using an Application Group - configured with a Server Application and a Web API. The target system (opentext) successfully redirects to adfs on logon, I enter the logon details into ADFS and it generates the token and passes it back to the app - BUT it does not contain the additional claims (email in this case) I added in the claims issuance policy. I know this as the token is logged in the application and I can view it in jwt.io (the web page). There is obviously a parameter / config setting missing - and I'm open to all and any suggestions!

## Answers

_No answers on this thread._
