---
title: "Exchange 2013 end users cannot connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/375042/exchange-2013-end-users-cannot-connect
question_id: 375042
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 end users cannot connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/375042/exchange-2013-end-users-cannot-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Today, clients are unable to connect to our Exchange server. Outlook freezes upon opening, OWA takes users to a blank screen. I've tried restarting Exchange Back End and that didn't fix it. The SSL certificate is valid, the server is still communicating with an external spam filter. The most recent update was on April 7th.

I ran Get-MapiVirtualDirectory|fl Identity,method and this is what I got:  

Identity :_____\mapi (Default Web Site)  

IISAuthenticationMethods : {Ntlm, OAuth, Negotiate}  

InternalAuthenticationMethods : {Ntlm, OAuth, Negotiate}  

ExternalAuthenticationMethods : {}

## Answers

_No answers on this thread._
