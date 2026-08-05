---
title: "Exchange 2019 - external mail stopped coming"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1302428/exchange-2019-external-mail-stopped-coming
question_id: 1302428
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 - external mail stopped coming

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1302428/exchange-2019-external-mail-stopped-coming (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello! Faced with a strange problem on my Exchange 2019 (15.2.1118.26) - last night external mail stopped coming, I checked MX-records - it was OK. So I decided to reboot Exchange server - and everything worked after that. But - how to find out what it was? What logs to see? Thank you for support.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-12*

Hi @Evgenii Shupik  ,

Currently you can view event logs through event viewer. Find the corresponding time period and view the corresponding error report.

Now that the problem has been solved, it may be difficult to locate the specific cause of the problem at that time. According to personal experience, if you encounter a similar problem next time, in addition to the event viewer, you can also check the queue viewer to see if the email is stuck in the queue and whether there is any relevant error message. You can also check the message tracking log to see if there are any relevant clues.

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
