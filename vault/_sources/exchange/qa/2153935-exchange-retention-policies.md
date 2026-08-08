---
title: "Exchange Retention Policies"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2153935/exchange-retention-policies
question_id: 2153935
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Retention Policies

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2153935/exchange-retention-policies (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi 

I would like to configure a retention policy in the compliance center.  

The goal is to retain items for 7 years, even if users choose to permanently delete items.  

After the 7 years, all items in the Recoverable Items > Purges folder, that are older than 7 years should be deleted.  

Items for example in the inbox, that are older than 7 years should not be deleted.  

Is this configuration correct, or will then completely all items older than 7 years be deleted?

Thanks and regards  

Peter

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-04*

Hi, @Peter

Based on your description, you want to perform different retention actions for different folders.

Based on the screenshot you provided, the configuration does enable items to be retained for seven years and then automatically deleted, but this would apply to all folders in the mailbox, rather than performing different retention actions for different folders.

Given your needs, in Exchange Online, you can use a messaging records management (MRM) retention policy to manage the email lifecycle. You can fulfill specific retention needs by creating retention tags, adding them to retention policies, and then applying the policies to mailbox users.

You can create retention tags that act on inboxes and deleted items to fulfill this retention requirement.

More information can be found Create a Retention Policy in Exchange Online | Microsoft Learn

Similar cases can be found in enable mailbox archival - Microsoft Q&A

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
