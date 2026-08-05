---
title: "O365 Sync Issues After On-Premises Exchange Decommissioning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2157450/o365-sync-issues-after-on-premises-exchange-decomm
question_id: 2157450
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-hybrid-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# O365 Sync Issues After On-Premises Exchange Decommissioning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2157450/o365-sync-issues-after-on-premises-exchange-decomm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In a transition from a Hybrid environment to nearly full cloud usage, the on-premises Exchange was shut down due to security concerns, following documentation and recommendations while leaving the schema intact.

Currently facing issues managing user email attributes for the second time. In this scenario, attempting to add my Global Admin (so i can get admin emails) to a regular email address has resulted in an error indicating that the attribute is managed on-premises. The on-premises attribute 'proxyAddresses' was manually updated, and the sync ran without issues, confirming the update in the Sync log. However, the alias still does not appear.

The specific question is: "How can an email alias be added to a user that was previously managed on-premises, now that the Exchange server no longer exists?"

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2025-02-14*

Hi @Anonymous  

The specific question is: "How can an email alias be added to a user that was previously managed on-premises, now that the Exchange server no longer exists?"

All synced object from AD to entra ID can be modified only from on-prem active directory.

That's why you should keep at least on Exchange server to be able to modify Exchange attributes from on-prem AD.

You can try to edit attribute from Active directory if all Exchange server are removed.

Please don't forget to accept helpful answer

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-02-14*

Every scenario involving directory synchronization requires you to make changes to synchronized users and their properties on-premises. This is not specific to Exchange and disabling/removing the Exchange bits do not change things - the objects will still need to be managed on-premises, until you disable synchronization.

Now, for the specific query on updating proxyaddresses, there is a workaround you might be able to use. In a nutshell, run the following cmdlet:

```
Set-Mailbox ******@domain.com -WindowsEmailAddress ******@domain.com
```

This will add ******@domain.com as the primary SMTP address for the user, while preserving existing aliases. Keep in mind that changes might be overwritten during a full sync cycle, so in the long run, you should consider removing the sync altogether.
