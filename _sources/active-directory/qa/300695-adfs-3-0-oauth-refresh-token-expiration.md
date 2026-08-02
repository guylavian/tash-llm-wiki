---
title: "ADFS 3.0 OAuth refresh token expiration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/300695/adfs-3-0-oauth-refresh-token-expiration
question_id: 300695
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 3.0 OAuth refresh token expiration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/300695/adfs-3-0-oauth-refresh-token-expiration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I'm struggling with a problem at one of my customers. An external web application is querying a RESTful service which is secured by ADFS 3.0 (Windows Server 2012 R2).    

I configured a Relying Party Trust and created a client application with a redirect uri.    

-  User initiates logon within external web app (Cyclr integration tool)    

-  On ADFS login dialog, types email/password and ticks "keep me signed in"    

-  External web app receives authorization code    

-  Using the auth code, gets a set of OAuth tokens (access and refresh token)    

-  When access token expires, gets a new access token by using refresh token    

-  When refresh token is about to expire, external web app should get a new refresh token as well, but it doesn't    

I found documentation regarding ADFS 4.0 (Windows server 2016) only:     

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/overview/ad-fs-openid-connect-oauth-flows-scenarios    

According to it, a refresh_token_expires_in parameter should be received and the client (int this case external web app) can get a new refresh token when the old one is about to expire. Now we don't receive any such parameter and can't get a new refresh token.    

Is there a way to convince ADFS 3.0 to work as expected?    

Thank you,    

Laszlo

## Answers

_No answers on this thread._
