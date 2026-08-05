---
title: "ADFS Cookie Handling Issue with SamlSession"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2121637/adfs-cookie-handling-issue-with-samlsession
question_id: 2121637
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Cookie Handling Issue with SamlSession

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2121637/adfs-cookie-handling-issue-with-samlsession (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm experiencing issues with ADFS cookie handling. After creating a Relying Party Trust, everything seemed to work fine initially. However, when calling ADFS repeatedly with the same user, the SamlSession cookie size gradually increases, leading to a 400 error with the message: "Header field too long." 

Upon inspecting the headers, I found multiple SamlSession cookies (SamlSession, SamlSession1, ..., SamlSession7). The first SamlSession cookie contains user information and some UUID, while the others consist of concatenated UUIDs separated by the `&` symbol, which I believe refer to assertion IDs.

What steps can be taken to resolve this issue?

## Answers

_No answers on this thread._
