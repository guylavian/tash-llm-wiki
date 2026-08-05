---
title: "Change Active Directory Builtin administrator account to something different"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1525861/change-active-directory-builtin-administrator-acco
question_id: 1525861
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Change Active Directory Builtin administrator account to something different

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1525861/change-active-directory-builtin-administrator-acco (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!
We have our AD builtin admin account as administrator and we want to change it to something different. What is the safest way to do this without breaking anything? We are running AD 2012.
Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-11*

Hi,
Yes you can rename it also along with the guest account, and in fact its recommended from a security standpoint. 
Here is an older guide but should work fine.
https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/rename-administrator-and-guest-account
Good luck!
Marius Ene - https://mariusene.com/

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-06*

Hi

Of course You can rename builtin administrator without any issue.
I have already renamed it in our production environment without any issue.
You can rename it manually or use a GPO to rename builtin administrator in default domain controller policy.

Please don’t forget to accept helpful answer
