---
title: "Decommision of Old Exchange Server 2013 to New Exchange Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1571809/decommision-of-old-exchange-server-2013-to-new-exc
question_id: 1571809
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Decommision of Old Exchange Server 2013 to New Exchange Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1571809/decommision-of-old-exchange-server-2013-to-new-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Do we require to get the old exchange server 2013 online before we do the decommission of the server?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-23*

No, you do not need to get the old Exchange Server 2013 online before decommissioning it as long as you've completed the necessary steps.
During decommissioning, the old server doesn't need to be online. The focus is ensuring all mailboxes and functionalities have already been transferred to the new platform.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-23*

Hello @Wei Jie Chua  ,

Welcome to our forum！

Yes, it is recommended to bring your old Exchange Server 2013 online before decommissioning it. This is to ensure that all mailboxes and other data are correctly migrated to the new Exchange Server 2016 before the old server is removed from the environment. Once the migration is complete and all data has been verified on the new server, you can proceed with decommissioning the old server. And you could refer to this link for general steps of decommissioning Exchange Server 2013.Additionally, you may could use the Exchange Deployment Assistant to guide you in planning your migration.

Hope the above information is helpful to you！

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
