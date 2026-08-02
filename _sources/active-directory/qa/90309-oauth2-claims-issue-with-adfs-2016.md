---
title: "oAuth2 claims issue with ADFS 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/90309/oauth2-claims-issue-with-adfs-2016
question_id: 90309
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# oAuth2 claims issue with ADFS 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/90309/oauth2-claims-issue-with-adfs-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

We have a web development team who is trying to test Oauth2 application code with ADFS on Windows 2016. There are several SAML applications getting authenticated via same ADFS server and AD. For this application they are using Postman client for testing.   

On ADFS side we have configured application group, which has given us the client ID and the redirect URL and Identifier is configured as per application.  

The client ID is provided to Application team which they have put in their code  

In application group we have granted access on Allataclaim, Email, Profile, OpenID etc and created claim rule to send email ID and Name.  

The issue is that in ID_Token we can see the UPN of the user, but no email ID or name is flowing.   

They are using scope as User:read+openId+profile+email  

Can someone guide us the correct way to configure ADFS with OAuth2 authentication and claims

## Answers

_No answers on this thread._
