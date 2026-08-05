---
title: "ADFS Authentication Failing in Chrome: MSISConext Cookie Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2120114/adfs-authentication-failing-in-chrome-msisconext-c
question_id: 2120114
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 3
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# ADFS Authentication Failing in Chrome: MSISConext Cookie Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2120114/adfs-authentication-failing-in-chrome-msisconext-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are using ADFS to redirect authentication to our underlying IDP. Previously, we ran our app within an iframe of another app, and it worked fine. However, with Chrome’s recent changes regarding third-party cookies, we are now facing issues.

Upon debugging, we found that the failure is due to the inability to get the MSISConext cookie. Are there any plans to enhance ADFS to include additional parameters like ‘Partitioned’ to allow the MSISConext cookie to be saved?

Additionally, is there any temporary workaround for this problem?

## Answers

_No answers on this thread._
