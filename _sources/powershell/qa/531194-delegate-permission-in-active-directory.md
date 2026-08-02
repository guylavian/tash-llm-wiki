---
title: "Delegate permission in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/531194/delegate-permission-in-active-directory
question_id: 531194
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Delegate permission in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/531194/delegate-permission-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

I try write a script which delegate permission on OU in AD, but when I try add both below permission, every time I get on ACL only generic all permission. It looks like they have higher priority than create, delete. What will be cause in this case and how I can fix it?   

$ace = New-Object System.DirectoryServices.ActiveDirectoryAccessRule $sid, "CreateChild, DeleteChild", "Allow", $Groups, "All"  

$ace2 = New-Object System.DirectoryServices.ActiveDirectoryAccessRule $sid, "GenericAll", "Allow", "Descendents", $Groups  

Regards

## Answers

_No answers on this thread._
