---
title: "How to change mailflow to Exchange online as all active mailbox are now on Exchange online in our Hybrid exchange 2016 environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1608388/how-to-change-mailflow-to-exchange-online-as-all-a
question_id: 1608388
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to change mailflow to Exchange online as all active mailbox are now on Exchange online in our Hybrid exchange 2016 environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1608388/how-to-change-mailflow-to-exchange-online-as-all-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 3 Exchange 2016 servers. All active mailboxes have been migrated to Exchange online. All emails still come to Exchange On-prem servers and then to Exchange online. How can the mailflow or mail routing be changed so that all emails directly go to Exchange online. I understand the send and receive connectors will need to be looked at, too.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-05*

Hi @Ashwani A. Kumar,

To have inbound emails be delivered to Exchange Online directly, you need to point your MX record to Exchange Online Protection service.

More detailed information are introduced in this link: Inbound messages from the Internet

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
