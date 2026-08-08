---
title: "Access both EWS and Graph"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/298599/access-both-ews-and-graph
question_id: 298599
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Access both EWS and Graph

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/298599/access-both-ews-and-graph (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we have an application that utilizes Exchange Webservices (EWS). For accounts on O365 we user OAuth2/ModernAuth via MSAL.    

I would like to add functionality that is only available via the Graph API, for example creating an online meeting.    

According to https://learn.microsoft.com/en-us/outlook/rest/compare-graph#moving-from-outlook-endpoint-to-microsoft-graph     

you cannot mix permissions for one endpoint with permissions for the other in a single request    

My default authorization is EWS.AccessAsUser.All, and for the calendar operation i need Calendars.ReadWrite.    

I have tried the following scenarios:    

-  Use both scopes (prior to reading the article linked above). Results in a token that can be used for Graph, but gets a 401 on EWS    

-  Aquire a token with EWS permission. Then use MSAL acquireTokenSilent with the graph scope. Gives me the same token for both, resulting in an "Invalid Audience" error on the Graph API    

-  Use interactive authorization (MSAL acquireToken). This gives me a second token with the correct scope, but now i have to present the user with two authentication flows and would probably have to retain two separate IMultipleAccountPublicClientApplication instances (which i have not tried yet, maybe not even possible)    

Any tips on how i can use both EWS and Graph API?

## Answers

_No answers on this thread._
