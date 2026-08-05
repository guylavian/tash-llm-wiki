---
title: "[Migrated from MSDN Exchange Dev]Exchange Hybrid Uninstalled & exchange services decommissioned but facing issues in office 365 online Distribution group."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/214933/migrated-from-msdn-exchange-dev-exchange-hybrid-un
question_id: 214933
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Exchange Hybrid Uninstalled & exchange services decommissioned but facing issues in office 365 online Distribution group.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/214933/migrated-from-msdn-exchange-dev-exchange-hybrid-un (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

can't modify the owner or do any changes on Distribution Group error indicates to contact on-premise server.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-31*

Hi,    

Is there any error in other functions besides distribution group?    

What is the specific error message? Can you give it to us? Please pay attention to covering your personal information.    

Is this distribution group synchronized from AD to Exchange online? If it is a distribution group synchronized to Exchange online in the on-premises environment, then the owner must manage the group by using on-premises tools for Exchange Server.    

For more information: Owners of an on-premises distribution group synced to O365 can't manage the distribution group in Exchange Online    

Please try to create the new distribution group in Exchange online and try to modify the owner.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
