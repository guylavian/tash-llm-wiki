---
title: "Accessing Sharepoint on-prem with ADFS using OAUTH"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4999410/accessing-sharepoint-on-prem-with-adfs-using-oauth
question_id: 4999410
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Accessing Sharepoint on-prem with ADFS using OAUTH

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4999410/accessing-sharepoint-on-prem-with-adfs-using-oauth (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a stand-alone app (not Sharepoint add-in) that allows users to connect to O365 resources using OAUTH.  We would like to extend the apps' functionality to allow access to on prem Sharepoint, however we do not want to develop and manage Sharepoint
 Add-ins for this purpose.  

We took the approach of configuring Sharepoint (2016 multi tenant host header site collections) to use ADFS3 and then set up OAUTH on the ADFS server and created a Trusted Security Token Issuer on Sharepoint with the certificate and ID of the ADFS client. 
 Everything works up to the point where we present the tokens we received from ADFS to the Sharepoint server.  The error we get is:

{"error":"invalid_client","error_description":"Invalid audience Uri 'urn:qa16oauth:adfstwo'."}  

Is this even possible without a sharepoint add-in or is there a different approach?   We want to allow the customer to access their own Sharepoint files with as few changes as possible to their Sharepoint environment.

## Answers

_No answers on this thread._
