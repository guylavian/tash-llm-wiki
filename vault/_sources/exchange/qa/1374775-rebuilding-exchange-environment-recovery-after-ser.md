---
title: "Rebuilding Exchange Environment Recovery After Server Loss"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374775/rebuilding-exchange-environment-recovery-after-ser
question_id: 1374775
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Rebuilding Exchange Environment Recovery After Server Loss

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374775/rebuilding-exchange-environment-recovery-after-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have a serious problem that I can't handle on my own. Specifically, I have two Exchange 2019 servers on-premises (MB01 and MB02), both of which were part of a Database Availability Group (DAG). However, the second server, MB02, suffered a complete failure and had to be removed, with no possibility of recovery. Not knowing how to solve this problem, I removed it from the schema, which turned out to be a mistake, I believe. Later on, I rebuilt the server from scratch, unaware that it could be restored from an Active Directory backup (a mistake stemming from my inexperience). Now, I'm encountering some critical issues, such as problems with autodiscover. My question is, would it be a good solution to install a third server, MB03, deactivate MB02, and create a new DAG with MB01 and MB03?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-25*

Hi @Sebastian，

From my personal understanding, even if there is only one server in the environment, it can theoretically work fine, so I don't think installing a new server will solve the problem. For now, you should troubleshoot Autodiscover first.

Also, noticed that you mentioned that you lack experience in this, it is recommended that you test it in a test environment before applying it to the production environment. (if permit).

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
