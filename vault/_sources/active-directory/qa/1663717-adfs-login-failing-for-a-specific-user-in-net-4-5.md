---
title: "ADFS login failing for a specific user in .Net 4.5"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1663717/adfs-login-failing-for-a-specific-user-in-net-4-5
question_id: 1663717
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS login failing for a specific user in .Net 4.5

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1663717/adfs-login-failing-for-a-specific-user-in-net-4-5 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an MVC application utilizing ADFS authentication. Authentication for a specific user has been failing over the past few weeks. The SAML response status is 200, indicating successful authentication from the server. Upon inspecting the SAML response for this user, it appears that the user is a member of numerous Active Directory (AD) groups, resulting in the SAML response containing around 250 claim attributes (saml:AttributeValue). Could this large number of claims be causing the issue? Most other users have fewer than 50 claims. Is there a maximum number of groups that a user can be a member of for a successful SAML token? This user was able to log in previously. Is this an issue within the application or could it be an ADFS SAML issue?

## Answers

_No answers on this thread._
