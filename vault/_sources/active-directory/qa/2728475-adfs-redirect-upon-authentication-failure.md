---
title: "ADFS Redirect upon authentication failure."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2728475/adfs-redirect-upon-authentication-failure
question_id: 2728475
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ADFS Redirect upon authentication failure.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2728475/adfs-redirect-upon-authentication-failure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have implemented ADFS in our environment. We have two ADFS servers in our farm, and two ADFS proxies in the DMZ that sit behind a load balancer.

Our HR department is using a web application and everything is set up and working. What we are trying to do now is redirect the user to a specific URL anytime the authentication fails. Currently, failed authentication is redirected to an error page on the
 relying party's website. We want to change that.

I have been to many forums and TechNet documents in an attempt to find an answer and so far, I have not found where anyone else has been able to do this. It is my understanding that when authentication fails at the relying party's website, ADFS doesn't even
 know about it. So we don't know if this is even possible.

Before we pursue this avenue any farther, we need to know if it is even possible.

Thank you.

## Answers

_No answers on this thread._
