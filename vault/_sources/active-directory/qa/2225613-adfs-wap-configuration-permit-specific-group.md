---
title: "ADFS + WAP configuration - Permit specific group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2225613/adfs-wap-configuration-permit-specific-group
question_id: 2225613
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS + WAP configuration - Permit specific group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2225613/adfs-wap-configuration-permit-specific-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

How can ADFS and WAP be configured to check for user membership in a specific Active Directory group during authentication? The goal is to allow authentication only for users who are members of this group, rejecting access otherwise.

The current setup involves the following flow:

External User --> OWA:

External User --> WAP --> ADFS --> OWA

Currently, with the "Access Control Policy" set to "Permit specific group," authentication is successful for users regardless of their group membership. It was expected that users not in the specified group would be denied authentication. What steps are needed to achieve the desired outcome?

## Answers

_No answers on this thread._
