---
title: "ADFS SSO not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/116842/adfs-sso-not-working
question_id: 116842
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS SSO not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/116842/adfs-sso-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

i have setup ADFS as a trusted identity server for my Sharepoint 2019 site.   

my ADFS server is also the DC and AD  

Steps on ADFS Server  

-  login a domain user  

-  browse sharepoint site with IE 11  

-  seamlessly redirect user to adfs/ls/wia then automatically redirect back to sharepoint with the user log in  

Steps on a client PC  

-  joined the domain  

-  login to a domain user  

-  browse sharepoint site with IE  

-  user get redirect to adfs/ls/wia  

-  user get prompt to enter credentials  

-  the flow stopped here and IE show HTTP 400 webpage not found  

i am not sure what steps i have missed out.  

i have check my ADFS service account, the SPN has being set correctly.  

i have tested using Chrome on both client PC and ADFS server.   

on ADFS server SSO is able to work. But on the client PC, user get prompt to entered the credentials, after entering , they are able to log in. this is not what i wanted. i wanted to flow to be like the ADFS where user are seamlessly logged in.  

ADFS version 2016

## Answers

_No answers on this thread._
