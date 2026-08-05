---
title: "Troubleshooting Local Policies/Audit Policy GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1519176/troubleshooting-local-policies-audit-policy-gpo
question_id: 1519176
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Troubleshooting Local Policies/Audit Policy GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1519176/troubleshooting-local-policies-audit-policy-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On our AD domain, I'm trying to turn on auditing so we can see password changes. I found this https://www.netwrix.com/how_to_detect_password_changes.html instructing to enable Success/Failure under the Local Policies/Audit Policy object in the Default Domain Policy. I've done this, but now I'm checking in Event Viewer and I see a bunch of Audit Policy Change events indicating that the policy was applied and then immediately reverted twice in the last 24 hours. I've checked GPResult but I only see two policies being applied on the Domain Controller and there's nothing conflicting between those two. What else should I check?

## Answers

_No answers on this thread._
