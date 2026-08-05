---
title: "LDAP Users ONLY, no windows desktop access - Does it require CAL?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2045654/ldap-users-only-no-windows-desktop-access-does-it
question_id: 2045654
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# LDAP Users ONLY, no windows desktop access - Does it require CAL?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2045654/ldap-users-only-no-windows-desktop-access-does-it (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If you have 'X' number of LDAP Users Only in your AD, is there a charge to do so, or does it require a CAL?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-09*

Thanks, Wesley, for your reply to my post.  Additional Context - what if the "application" leveraging LDAP is not in our environment/domain.  If it sits in another vendor's data center and is not running on Windows?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-09*

Hello

For LDAP users who do not have access to Windows desktops, the requirement for a Client Access License (CAL) depends on the specific use case and the licensing terms of the software being used.

In general, if the LDAP users are only authenticating against Active Directory and not accessing any Windows Server services or applications that require a CAL, then a CAL may not be required. However, if these users are accessing services or applications that require a CAL, such as file sharing, printing, or other server-based applications, then a CAL would be necessary.
