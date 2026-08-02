---
title: "Computer/Domain Controller Certificate Autoenroll CNG 3 Template"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2149937/computer-domain-controller-certificate-autoenroll
question_id: 2149937
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Computer/Domain Controller Certificate Autoenroll CNG 3 Template

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2149937/computer-domain-controller-certificate-autoenroll (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am trying to recall how Certificate Autoenrollment chooses the correct CNG 3 Certificate Template. When you configure the Automatic Certificate Request Settings, you're only given the CNG 1 templates:  

We have duplicated the "Computer" template a few times for different templates. The only difference is, I've only specifically set one to allow "Autoenroll" permissions from Domain Computers (or Domain Controllers for that specific autoenroll GPO), so it's working correctly in our environment, since we only have one Version 3 template for "Computer" or "Domain Controller" to autoenroll. What if you have multiple templates that allow autoenroll (whether by accident or not)? Does it choose based on the latest Schema and Version of the duplicated template?

-J

## Answers

_No answers on this thread._
