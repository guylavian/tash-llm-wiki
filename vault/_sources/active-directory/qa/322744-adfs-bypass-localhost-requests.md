---
title: "ADFS bypass localhost requests"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/322744/adfs-bypass-localhost-requests
question_id: 322744
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS bypass localhost requests

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/322744/adfs-bypass-localhost-requests (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a need to set up HTTP monitoring CRM . The monitoring solution we use does not have a way to use encrypted values in the config files used for http checks. I am trying to determine if ADFS can be set up to allow certain users or requests from certain hosts to bypass ADFS authentication.   

We use CA Siteminder for our identity provider for internal applications. Siteminder has the ability to ignore authenticating requests that are made from the local server so it falls back to basic auth. By default ADFS is turned on for the entire site. Is there a way to disable ADFS auth for requests from localhost (127.0.0.1) or from specific accounts?

## Answers

_No answers on this thread._
