---
title: "Exchange server 0Auth authorization for single mailbox from backend service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/293684/exchange-server-0auth-authorization-for-single-mai
question_id: 293684
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Exchange server 0Auth authorization for single mailbox from backend service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/293684/exchange-server-0auth-authorization-for-single-mai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Background:  

I'm upgrading a backend service that currently uses basic authentication to read and delete emails from a single mailbox on an exchange server to authenticate using OAuth2.0. I'm having difficulty finding conclusive documentation about the best authorization flow for this.  

Question:  

What is the best authorization flow that achieves the following?  

-  Authorizes a connection from backend service to an Exchange 2013 server, an Exchange 2016 server, an Exchange 2019 server, or Office365.  

-  Authorizes access to a specific mailbox and does not allow acess to other mailboxes within the organization.  

-  Allows read/write access.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-01*

-  For Exchange Online the Client Credentials flow https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow would be the best option for what you doing.  Exchange OnPrem needs to handle differently and would require that the Organization have Hybrid modern Authentication configured to be able to use OAuth    

-  For Exchange Online use application access polices that allow you to scope Application permissions to one mailbox https://techcommunity.microsoft.com/t5/exchange-team-blog/application-access-policy-support-in-ews/ba-p/2110361    

-  If your using EWS then the only scopes its support allow Full Access, if you need Read access only you need to use the Microsoft Graph
