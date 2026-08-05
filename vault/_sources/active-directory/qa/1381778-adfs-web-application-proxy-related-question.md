---
title: "adfs web application proxy related question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1381778/adfs-web-application-proxy-related-question
question_id: 1381778
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adfs web application proxy related question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1381778/adfs-web-application-proxy-related-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

used rapid restore tool to build a parallel farm of 2012 r2 with wid. Added two 2022 to the farm. Removed the 2012 r2 servers from the farm. Added two proxies with each proxy hosts file pointing the federation address to one adfs server. 

The issue is the logging for the proxy is populated constantly. In previous environment we had "The federation server proxy successfully retrieved and updated its configuration from the Federation Service" show up constantly. With the new one it only populates when the proxy server is rebooted. After four or five iterations of checks it stops populating. 

Is this new in 2022 or do we need to enable the constant logging somewhere? The Admin logs under adfs of the proxy is enabled. 

@Pierre Audonnet - MSFT

## Answers

_No answers on this thread._
