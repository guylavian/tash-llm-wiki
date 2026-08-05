---
title: "Duplicate Active Directory Accounts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2103489/duplicate-active-directory-accounts
question_id: 2103489
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Duplicate Active Directory Accounts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2103489/duplicate-active-directory-accounts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I had to create a new Active Directory account for a user but put a 2 at the end. I want to completely delete the old account because it is throwing errors about duplicate account.

The old account is linked through Azure Entra ID.

His old account is also linked with his mailbox. 

If I delete his old account will this affect the new one at all? Especially O365 Applications.

Thanks,

Tom

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-15*

Hello,

Here’s what you need to know:

Impact on the New Account:

If you delete the old account, it should not affect the new account you created. The new account is separate and should function independently. However, if there are any shared resources or permissions, you might want to double-check those.

Mailbox Association:

Since the old account is linked to a mailbox, deleting it will also remove access to that mailbox. If the mailbox is critical, consider converting it to a shared mailbox or ensuring that all necessary data is migrated to the new account before deletion.

O365 Applications:

If the old account is used for any O365 applications, those links will break upon deletion. Ensure that any necessary access or data is transferred to the new account.

Best Practices:

Before deleting the old account, you might want to disable it first. This way, you can monitor for any issues before making a permanent deletion.

Backup Important Data:

Always back up any important data associated with the old account to avoid accidental loss.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
