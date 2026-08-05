---
title: "Can I have multiple sites each with their own adfs claims providers?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1421027/can-i-have-multiple-sites-each-with-their-own-adfs
question_id: 1421027
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Can I have multiple sites each with their own adfs claims providers?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1421027/can-i-have-multiple-sites-each-with-their-own-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have the following sites:

```
https://example.com/ClientA

https://example.com/ClientB

https://example.com/ClientC
```

Right now if I go to https://example.com/ClientA then I'm sent to `https://adfsco.example.com/adfs/ls?...` and there is the claims providers we trust for that site.

Now I'd like to have it so when https://example.com/ClientB is navigated to, the user would see different providers that only matter for that site.

I've seen things about home realm discovery pages, but no step-by-step guide explaining how to actually wire this up. I'm assuming one ADFS can handle this, but not sure how. Is this where relying parties come in?

## Answers

_No answers on this thread._
