---
title: "Server 2019 active directory 계정 삭제 후 같은 이름의 계정을 생성 할 수 없게 할 수 있나요?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1497230/server-2019-active-directory
question_id: 1497230
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Server 2019 active directory 계정 삭제 후 같은 이름의 계정을 생성 할 수 없게 할 수 있나요?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1497230/server-2019-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Server 2019 active directory 계정 삭제 후 같은 이름의 계정을 생성 할 수 없게 할 수 있나요?
active directory recycle bin을 사용하면 가능 하나요?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-17*

Hello 성현 박,
Thank you for posting in Q&A forum.
When you delete an account, it is possible to create an account with the same name by default. If you want to prevent the reuse of the same username, you can keep the deleted account and not completely delete it from AD immediately, but only disable it. This means that the username will remain in the system and new accounts with the same name cannot be created.
As for the Active Directory Recycle Bin feature, it is a feature available in Windows Server 2008 R2 and above to restore AD objects after deletion. After enabling the Active Directory Recycle Bin feature, deleted objects will first enter a "tombstone" state, during which they can be restored. In this state, the object will not appear in the normal query results of Active Directory, but still exists in the database.
I hope the information above is helpful.
If you have any questions or concerns, please feel free to let us know.

Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-16*

Yes, it is possible to prevent the creation of an account with the same name after deleting an Active Directory account. One way to achieve this is by using the Active Directory Recycle Bin feature. When an account is deleted and the Recycle Bin feature is enabled, the deleted account is moved to the Recycle Bin instead of being permanently deleted. The Recycle Bin keeps track of the deleted object's unique identifier (GUID), which prevents the creation of a new object with the same name and GUID. Therefore, if you try to create a new account with the same name as the deleted account, you will receive an error message stating that the name already exists.

References:

-  Access to Active Directory - Recovery of deleted Exchange objects
