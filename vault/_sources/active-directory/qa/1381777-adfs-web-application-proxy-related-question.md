---
title: "adfs web application proxy related question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1381777/adfs-web-application-proxy-related-question
question_id: 1381777
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adfs web application proxy related question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1381777/adfs-web-application-proxy-related-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Recently built a parallel farm of 2012 R2 with WID (the production used sql) and added 2022 servers to the farm. Then took out the 2012 R2. And raised farm behavior level to 2022. 

Added two 2022 proxy servers. Each proxy was set to point the sso dns to one of the adfs servers.

When the proxy servers are rebooted the ADFS logs in proxy are populated with "The federation server proxy successfully retrieved and updated its configuration from the Federation Service..." for a brief period and then stops. The logging is enabled. 

In previous environment it used to be constantly updated. 

Is this a new behavior in 2022 or do we need to enable something somewhere to get this going again? 

@Pierre Audonnet - MSFT

## Answers

_No answers on this thread._
